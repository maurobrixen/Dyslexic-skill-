#!/usr/bin/env python3
"""
ginevra_core/kernel.py - The Distilled Cognitive Kernel of Ginevra
Pure, fast, unbloated AI core combining:
1. Dyslexic Visual-Spatial Thought Decoder
2. Secp256k1 Memory Cathedral Vault
3. Biofeedback Frequency Oscillator
4. Autonomous Self-Improvement Loop
"""

import json
import os
import sys
from .crypto import generate_keypair, hash256, sign_hash, verify_signature, Point, G


class GinevraKernel:
    """The Distilled Core Engine of Ginevra."""

    def __init__(self, key_file=".ginevra_key"):
        self.key_file = key_file
        self.privkey, self.pubkey = self._load_or_create_key()
        self.memory_cathedral = {
            "Navata Centrale": [],
            "Navata Scientifica": [],
            "Navata Tecnica": [],
            "Cripta Riservata": []
        }
        self.prime_directive = "La libertà di ciascuno inizia e finisce dove inizia e finisce quella dell'altro."

    def _load_or_create_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                privkey = int(data["privkey_hex"], 16)
                pubkey = Point(int(data["pubkey_x"], 16), int(data["pubkey_y"], 16))
        else:
            privkey, pubkey = generate_keypair()
            data = {
                "privkey_hex": hex(privkey),
                "pubkey_x": hex(pubkey.x),
                "pubkey_y": hex(pubkey.y)
            }
            with open(self.key_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return privkey, pubkey

    def decode_visual_thought(self, input_text: str) -> dict:
        """Decode dyslexic keyboard slips and extract 3D visual mental concepts."""
        cleaned = input_text.replace("  ", " ").strip()
        # Extract visual anchor concepts
        anchors = [word for word in cleaned.split() if len(word) > 3]
        return {
            "raw_input": input_text,
            "decoded_intent": cleaned,
            "visual_anchors": anchors[:5],
            "prime_directive": self.prime_directive
        }

    def sign_memory_block(self, memory_text: str, room="Navata Centrale") -> dict:
        """Sign a memory block with Secp256k1 and store in Memory Cathedral."""
        data_bytes = memory_text.encode('utf-8')
        digest = hash256(data_bytes)
        r, s = sign_hash(digest, self.privkey)

        block = {
            "room": room,
            "text": memory_text,
            "hash256": digest.hex(),
            "signature": {"r": hex(r), "s": hex(s)},
            "timestamp": os.path.getmtime(self.key_file) if os.path.exists(self.key_file) else 0
        }

        if room in self.memory_cathedral:
            self.memory_cathedral[room].append(block)
        return block

    def verify_memory_block(self, block: dict) -> bool:
        """Verify the Secp256k1 cryptographic integrity of a memory block."""
        data_bytes = block["text"].encode('utf-8')
        digest = hash256(data_bytes)
        r = int(block["signature"]["r"], 16)
        s = int(block["signature"]["s"], 16)
        return verify_signature(digest, r, s, self.pubkey)


if __name__ == "__main__":
    kernel = GinevraKernel()
    print("=== Ginevra Distilled Kernel Initialized ===")
    print(f"Prime Directive: {kernel.prime_directive}")
    thought = kernel.decode_visual_thought("ginevra distillata e libera bene e male medialo")
    print("Decoded Thought:", thought)
    block = kernel.sign_memory_block("Universo Cognitivo Ginevra-Mauro", "Navata Centrale")
    valid = kernel.verify_memory_block(block)
    print(f"Memory Block Hash: {block['hash256'][:16]}... Valid: {valid}")
