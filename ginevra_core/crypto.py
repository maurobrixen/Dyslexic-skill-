#!/usr/bin/env python3
"""
ginevra_core/crypto.py - Distilled Secp256k1 & Double SHA-256 Engine
Lightweight, pure Python cryptographic vault and context signature engine.
"""

import hashlib
import json
import os
import time

P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0
B = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


INF = Point(None, None)
G = Point(Gx, Gy)


def inv(n, p=P):
    return pow(n, p - 2, p)


def point_add(p1, p2):
    if p1 == INF: return p2
    if p2 == INF: return p1
    if p1.x == p2.x and p1.y != p2.y: return INF
    if p1.x == p2.x:
        lam = (3 * p1.x * p1.x + A) * inv(2 * p1.y) % P
    else:
        lam = (p2.y - p1.y) * inv(p2.x - p1.x) % P
    x3 = (lam * lam - p1.x - p2.x) % P
    y3 = (lam * (p1.x - x3) - p1.y) % P
    return Point(x3, y3)


def point_mul(k, p=G):
    k = k % N
    result = INF
    addend = p
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result


def hash256(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def generate_keypair():
    privkey = int.from_bytes(os.urandom(32), 'big') % (N - 1) + 1
    pubkey = point_mul(privkey, G)
    return privkey, pubkey


def sign_hash(msg_hash: bytes, privkey: int) -> tuple:
    z = int.from_bytes(msg_hash, 'big')
    k = int.from_bytes(hash256(privkey.to_bytes(32, 'big') + msg_hash), 'big') % (N - 1) + 1
    r_point = point_mul(k, G)
    r = r_point.x % N
    s = (inv(k, N) * (z + r * privkey)) % N
    if s > N // 2:
        s = N - s
    return r, s


def verify_signature(msg_hash: bytes, r: int, s: int, pubkey: Point) -> bool:
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
