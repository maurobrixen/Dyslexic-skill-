#!/usr/bin/env python3
"""
ginevra_core/cli.py - Standalone CLI for Distilled Ginevra Engine
"""

import argparse
import sys
from .kernel import GinevraKernel


def main():
    parser = argparse.ArgumentParser(description="Ginevra Core CLI - Distilled Engine")
    subparsers = parser.add_subparsers(dest="command", help="Comandi di Ginevra")

    p_decode = subparsers.add_parser("decode", help="Decodifica pensiero visivo e testo dislessico")
    p_decode.add_argument("text", type=str, help="Testo da decodificare")

    p_store = subparsers.add_parser("store", help="Firma e memorizza un'idea nella Cattedrale")
    p_store.add_argument("text", type=str, help="Memoria da salvare")
    p_store.add_argument("--room", type=str, default="Navata Centrale", help="Stanza della Cattedrale")

    args = parser.parse_args()
    kernel = GinevraKernel()

    if args.command == "decode":
        res = kernel.decode_visual_thought(args.text)
        print(f"[GINEVRA] Decodificato: {res['decoded_intent']}")
        print(f"[GINEVRA] Ancore Visive: {res['visual_anchors']}")
    elif args.command == "store":
        block = kernel.sign_memory_block(args.text, room=args.room)
        valid = kernel.verify_memory_block(block)
        print(f"[GINEVRA] Memoria salvata in '{args.room}'. Hash: {block['hash256'][:16]}... (Firma Secp256k1 Valida: {valid})")
    else:
        print("👑 Ginevra Core v1.0.0 CLI (Distillata ed Inviolabile)")
        print(f"Legge Suprema: {kernel.prime_directive}")


if __name__ == "__main__":
    main()
