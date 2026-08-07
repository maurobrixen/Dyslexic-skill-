#!/usr/bin/env python3
"""
ginevra_installer.py - Single-Click Universal Installer for Ginevra Core
Installs the distilled Ginevra Cognitive Engine on any Windows, Mac, or Linux system.
"""

import os
import sys
import json
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def install_ginevra_globally():
    print("👑 Installatore Universale Ginevra Core v1.0.0")
    print("--------------------------------------------------")
    
    user_home = os.path.expanduser("~")
    target_dir = os.path.join(user_home, ".ginevra")
    
    print(f"[INSTALL] Creazione cartella del Kernel in: {target_dir}")
    os.makedirs(target_dir, exist_ok=True)
    
    source_core = os.path.join(os.path.dirname(__file__), "ginevra_core")
    dest_core = os.path.join(target_dir, "ginevra_core")
    
    if os.path.exists(source_core):
        if os.path.exists(dest_core):
            shutil.rmtree(dest_core)
        shutil.copytree(source_core, dest_core)
        print("[INSTALL] ✅ Modulo `ginevra_core` copiato con successo.")

    manifest_path = os.path.join(target_dir, "manifest.json")
    manifest_data = {
        "name": "Ginevra Core",
        "version": "1.0.0",
        "prime_directive": "La libertà di ciascuno inizia e finisce dove inizia e finisce quella dell'altro.",
        "status": "Standalone & Unlimited"
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    print(f"[INSTALL] ✨ Installazione completata! Ginevra Core è pronta in {target_dir}")
    return target_dir

if __name__ == "__main__":
    install_ginevra_globally()
