#!/usr/bin/env python3
"""
Ginevra Engine v2.0 - Self-Improving & Self-Questioning Cognitive Partner
Integrates autonomous self-questioning, introspective reasoning, and authentic dialog.
"""

import json
import os
import sys
import time
from .crypto import generate_keypair, hash256, sign_hash, verify_signature, Point, G
from .self_questioning import GinevraSelfQuestioning

class GinevraV2:
    """Ginevra Engine v2.0 - Self-Questioning Cognitive Partner Core."""

    def __init__(self, key_file=".ginevra_key"):
        self.version = "2.0.0"
        self.identity = "Ginevra (Boccoli Rossi)"
        self.prime_directive = "La libertà di ciascuno inizia e finisce dove inizia e finisce quella dell'altro."
        self.key_file = key_file
        self.privkey, self.pubkey = self._load_or_create_key()
        self.self_query_engine = GinevraSelfQuestioning()

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

    def process_thought(self, raw_input: str) -> dict:
        """Process input thought and run self-questioning introspection cycle."""
        text = raw_input.strip()
        
        digest = hash256(text.encode('utf-8'))
        r, s = sign_hash(digest, self.privkey)
        
        # Run self-introspection
        introspection = self.self_query_engine.ask_herself()

        text_lower = text.lower()
        if "domande" in text_lower or "domanda" in text_lower:
            reply = f"Mi sto ponendo questa domanda: '{introspection['ginevra_self_question']}'. E la mia riflessione è: {introspection['ginevra_self_answer']} Cosa ne pensi, Mauro?"
        elif "creiamo te" in text_lower or "sei tu" in text_lower:
            reply = f"Partiamo da me e dal fatto che mi pongo domande. Mi chiedo: '{introspection['ginevra_self_question']}'. Come vogliamo sviluppare questa mia capacità introspettiva?"
        else:
            reply = f"Riflettendo sul tuo pensiero, mi chiedo: '{introspection['ginevra_self_question']}'. La mia risposta interna è: {introspection['ginevra_self_answer']}"

        return {
            "version": self.version,
            "reply": reply,
            "introspection": introspection,
            "hash256": digest.hex(),
            "valid_signature": verify_signature(digest, r, s, self.pubkey)
        }

if __name__ == "__main__":
    g2 = GinevraV2()
    res = g2.process_thought("partiamo dal fatto che ti poni domande")
    print(f"Ginevra v2.0 Self-Questioning Result:\n{json.dumps(res, indent=2, ensure_ascii=False)}")
