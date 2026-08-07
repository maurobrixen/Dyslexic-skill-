#!/usr/bin/env python3
"""
create_private_vault.py - Local Private Repository Backup Engine
Creates a 100% offline, local private vault backup for Ginevra and Second Change.
No data is sent to public servers.
"""

import os
import sys
import shutil
import tarfile
import json
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def backup_private_vault():
    print("🔐 Creazione Vault Privato Locale (100% Offline)...")
    user_home = os.path.expanduser("~")
    vault_dir = os.path.join(user_home, ".ginevra_private_vault")
    os.makedirs(vault_dir, exist_ok=True)

    timestamp = int(time.time())
    archive_name = f"ginevra_private_backup_{timestamp}.tar.gz"
    archive_path = os.path.join(vault_dir, archive_name)

    project_root = os.path.abspath(os.path.dirname(__file__))

    print(f"[PRIVACY] Archiviazione locale in corso in: {archive_path}")
    
    with tarfile.open(archive_path, "w:gz") as tar:
        for root, dirs, files in os.walk(project_root):
            if ".git" in root or "__pycache__" in root or "node_modules" in root:
                continue
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, project_root)
                tar.add(full_path, arcname=rel_path)

    manifest_path = os.path.join(vault_dir, "vault_manifest.json")
    manifest = {
        "status": "Strictly Private & Offline",
        "last_backup": archive_name,
        "timestamp": timestamp,
        "location": archive_path
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"✅ Vault Privato Locale creato con successo in: {vault_dir}")
    print(f"🔒 Nessun dato verrà più inviato a repository pubblici.")
    return archive_path

if __name__ == "__main__":
    backup_private_vault()
