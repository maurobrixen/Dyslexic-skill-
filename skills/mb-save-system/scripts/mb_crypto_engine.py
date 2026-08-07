#!/usr/bin/env python3
"""
mb_crypto_engine.py - Bitcoin-Grade Secp256k1 & Double SHA-256 Engine
Inspired by Andrej Karpathy's `cryptos` library (pure Python, zero dependencies).

Provides:
- Secp256k1 Elliptic Curve Arithmetic
- ECDSA Signature Generation & Verification
- Double SHA-256 & RIPEMD160 Hashing
- Context Block Hashing & Proof-of-Integrity for HANDOFF.md and Memory Vault
"""

import hashlib
import hmac
import os
import json
import time

# -----------------------------------------------------------------------------
# Secp256k1 Curve Parameters (Same as Bitcoin)
# -----------------------------------------------------------------------------
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


class Point:
    """A point on the Secp256k1 curve."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        if self.x is None and self.y is None:
            return "Point(Infinity)"
        return f"Point({hex(self.x)}, {hex(self.y)})"


INF = Point(None, None)
G = Point(Gx, Gy)


def inv(n, p=P):
    """Modular inverse using Extended Euclidean Algorithm."""
    if n == 0:
        raise ZeroDivisionError("division by zero in modular inverse")
    return pow(n, p - 2, p)


def point_add(p1, p2):
    """Add two points on the Secp256k1 curve."""
    if p1 == INF:
        return p2
    if p2 == INF:
        return p1
    if p1.x == p2.x and p1.y != p2.y:
        return INF
    if p1.x == p2.x:
        lam = (3 * p1.x * p1.x + A) * inv(2 * p1.y) % P
    else:
        lam = (p2.y - p1.y) * inv(p2.x - p1.x) % P
    x3 = (lam * lam - p1.x - p2.x) % P
    y3 = (lam * (p1.x - x3) - p1.y) % P
    return Point(x3, y3)


def point_mul(k, p=G):
    """Scalar multiplication k * Point on Secp256k1 curve."""
    k = k % N
    result = INF
    addend = p
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result


# -----------------------------------------------------------------------------
# Cryptographic Hashing Functions
# -----------------------------------------------------------------------------
def sha256(data: bytes) -> bytes:
    """Single SHA-256 hash."""
    return hashlib.sha256(data).digest()


def hash256(data: bytes) -> bytes:
    """Double SHA-256 hash (Bitcoin style)."""
    return sha256(sha256(data))


def hash160(data: bytes) -> bytes:
    """RIPEMD-160(SHA-256(data))."""
    r = hashlib.new('ripemd160')
    r.update(sha256(data))
    return r.digest()


# -----------------------------------------------------------------------------
# ECDSA Signing & Verification
# -----------------------------------------------------------------------------
def generate_keypair():
    """Generate a random private key and corresponding Secp256k1 public key."""
    privkey = int.from_bytes(os.urandom(32), 'big') % (N - 1) + 1
    pubkey = point_mul(privkey, G)
    return privkey, pubkey


def sign_hash(msg_hash: bytes, privkey: int) -> tuple:
    """Sign a 32-byte message hash using ECDSA (RFC 6979 deterministic k)."""
    z = int.from_bytes(msg_hash, 'big')
    # Deterministic k generation (RFC 6979 simplified)
    k = int.from_bytes(hash256(privkey.to_bytes(32, 'big') + msg_hash), 'big') % (N - 1) + 1
    r_point = point_mul(k, G)
    r = r_point.x % N
    if r == 0:
        return sign_hash(msg_hash, privkey + 1)
    s = (inv(k, N) * (z + r * privkey)) % N
    if s > N // 2:
        s = N - s  # Low-S rule for Bitcoin compatibility
    return r, s


def verify_signature(msg_hash: bytes, r: int, s: int, pubkey: Point) -> bool:
    """Verify an ECDSA signature (r, s) against a message hash and public key."""
    if not (1 <= r < N and 1 <= s < N):
        return False
    z = int.from_bytes(msg_hash, 'big')
    w = inv(s, N)
    u1 = (z * w) % N
    u2 = (r * w) % N
    p = point_add(point_mul(u1, G), point_mul(u2, pubkey))
    if p == INF:
        return False
    return (p.x % N) == r


# -----------------------------------------------------------------------------
# Context Block Proof-of-Integrity Functions
# -----------------------------------------------------------------------------
def get_or_create_vault_key(key_file=".vault_key"):
    """Retrieve or create persistent Secp256k1 private key for vault signing."""
    if os.path.exists(key_file):
        with open(key_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            privkey = int(data["privkey_hex"], 16)
    else:
        privkey, pubkey = generate_keypair()
        data = {
            "privkey_hex": hex(privkey),
            "pubkey_x": hex(pubkey.x),
            "pubkey_y": hex(pubkey.y),
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(key_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[MB-CRYPTO] Nuova chiave Secp256k1 creata in {key_file}")
    return privkey


def sign_context_file(filepath: str, key_file=".vault_key") -> dict:
    """Compute double SHA-256 hash of file and generate ECDSA proof."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File {filepath} non trovato.")

    privkey = get_or_create_vault_key(key_file)
    pubkey = point_mul(privkey, G)

    with open(filepath, "rb") as f:
        file_bytes = f.read()

    file_hash = hash256(file_bytes)
    r, s = sign_hash(file_hash, privkey)

    proof = {
        "file": os.path.basename(filepath),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "hash256": file_hash.hex(),
        "pubkey": {"x": hex(pubkey.x), "y": hex(pubkey.y)},
        "signature": {"r": hex(r), "s": hex(s)}
    }
    return proof


def verify_context_proof(filepath: str, proof: dict) -> bool:
    """Verify that file content matches hash256 and ECDSA signature in proof."""
    if not os.path.exists(filepath):
        return False

    with open(filepath, "rb") as f:
        file_bytes = f.read()

    current_hash = hash256(file_bytes)
    if current_hash.hex() != proof["hash256"]:
        print("[MB-CRYPTO] ❌ VERIFICA FALLITA: Il contenuto del file è stato modificato o corrotto!")
        return False

    pubkey = Point(int(proof["pubkey"]["x"], 16), int(proof["pubkey"]["y"], 16))
    r = int(proof["signature"]["r"], 16)
    s = int(proof["signature"]["s"], 16)

    is_valid = verify_signature(current_hash, r, s, pubkey)
    if is_valid:
        print(f"[MB-CRYPTO] ✅ VERIFICA RIUSCITA: Firma ECDSA Secp256k1 valida per {proof['file']}")
    else:
        print("[MB-CRYPTO] ❌ VERIFICA FALLITA: Firma ECDSA non valida!")
    return is_valid


if __name__ == "__main__":
    print("=== MB Crypto Engine Test ===")
    priv, pub = generate_keypair()
    msg = b"MB-Skills Bitcoin Grade Integrity Test"
    m_hash = hash256(msg)
    r, s = sign_hash(m_hash, priv)
    valid = verify_signature(m_hash, r, s, pub)
    print(f"Hash: {m_hash.hex()}\nFirma r: {hex(r)}\nFirma s: {hex(s)}\nVerifica: {valid}")
