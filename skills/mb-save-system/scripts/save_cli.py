#!/usr/bin/env python3
"""
save_cli.py - MB Save & Context Handoff System (Secp256k1 Signed)
CLI helper to automate session state capture, context compaction, git synchronization,
and Bitcoin-grade cryptographic proof of integrity via mb_crypto_engine.py.
"""

import argparse
import datetime
import json
import os
import subprocess
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Import native crypto engine
try:
    from mb_crypto_engine import sign_context_file, verify_context_proof, hash256
except ImportError:
    # If called from root directory
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    from mb_crypto_engine import sign_context_file, verify_context_proof, hash256


def run_cmd(cmd, cwd=None):
    """Run a shell command and return stdout string."""
    try:
        res = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or os.getcwd(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return res.stdout.strip(), res.stderr.strip(), res.returncode
    except Exception as e:
        return "", str(e), 1


def get_git_info():
    """Retrieve git branch, last commit, and status."""
    branch, _, _ = run_cmd("git rev-parse --abbrev-ref HEAD")
    commit, _, _ = run_cmd("git log -1 --oneline")
    status, _, _ = run_cmd("git status --short")
    return {
        "branch": branch or "main",
        "last_commit": commit or "nessun commit",
        "status": status or "nessuna modifica pendente"
    }


def update_context_chain(proof: dict, chain_file="CONTEXT_CHAIN.json"):
    """Append context signature proof to local CONTEXT_CHAIN.json ledger."""
    chain = []
    if os.path.exists(chain_file):
        try:
            with open(chain_file, "r", encoding="utf-8") as f:
                chain = json.load(f)
        except Exception:
            chain = []

    prev_hash = chain[-1]["hash256"] if chain else "0" * 64
    proof["prev_hash"] = prev_hash
    proof["block_index"] = len(chain) + 1

    chain.append(proof)
    with open(chain_file, "w", encoding="utf-8") as f:
        json.dump(chain, f, indent=2)
    print(f"[MB-SAVE] 🛡️ Registrato Blocco Contesto #{proof['block_index']} in {chain_file} (PrevHash: {prev_hash[:8]}...)")


def generate_session_state(output_file="SESSION_STATE.md", note=""):
    """Generate a quick session snapshot."""
    git_info = get_git_info()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""# 📍 SESSION STATE SNAPSHOT

**Data/Ora**: {now}  
**Branch Git**: `{git_info['branch']}`  
**Ultimo Commit**: `{git_info['last_commit']}`

## 📝 Note della Sessione
{note if note else "Salvataggio rapido dello stato attuale di lavoro."}

## 📊 Stato Git
```text
{git_info['status']}
```

---
*Generato automaticamente da MB Save System (Secp256k1 Protected)*
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[MB-SAVE] Stato sessione salvato in {output_file}")
    return output_file


def generate_handoff(output_file="HANDOFF.md", objective="", decisions=None, tasks=None, next_steps=None):
    """Generate a condensed HANDOFF document with Secp256k1 signature proof."""
    git_info = get_git_info()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    decisions_str = "\n".join([f"- {d}" for d in (decisions or ["Nessuna decisione registrata"])])
    tasks_str = "\n".join([f"- [ ] {t}" for t in (tasks or ["Nessun task in sospeso"])])
    next_steps_str = "\n".join([f"1. {s}" for s in (next_steps or ["Proseguire secondo i requisiti utente"])])

    content = f"""# 📑 HANDOFF SESSION STATE (Token Optimized & Secp256k1 Signed)

**Data/Ora**: {now}  
**Branch Git**: `{git_info['branch']}`  
**Ultimo Commit**: `{git_info['last_commit']}`

---

## 🎯 1. Obiettivo & Stato Attuale
- **Obiettivo**: {objective if objective else "Sviluppo e gestione progetto"}
- **Stato**: In corso / Pronto per ripresa

---

## 💡 2. Decisioni Architetturali & Regole
{decisions_str}

---

## 🔄 3. Task in Sospeso & Loop Aperti
{tasks_str}

---

## 📂 4. Stato dei File
```text
{git_info['status']}
```

---

## 🚀 5. Prossimi Passi per il Riavvio
{next_steps_str}
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[MB-SAVE] File Handoff compattato creato in {output_file}")

    # Sign HANDOFF.md with Secp256k1 and update context chain
    proof = sign_context_file(output_file)
    update_context_chain(proof)
    return output_file


def verify_handoff_integrity(handoff_file="HANDOFF.md", chain_file="CONTEXT_CHAIN.json"):
    """Verify handoff file integrity against CONTEXT_CHAIN.json."""
    if not os.path.exists(chain_file) or not os.path.exists(handoff_file):
        print("[MB-SAVE] ⚠️ Impossibile verificare: file handoff o catena non trovati.")
        return False

    with open(chain_file, "r", encoding="utf-8") as f:
        chain = json.load(f)

    if not chain:
        print("[MB-SAVE] ⚠️ Catena del contesto vuota.")
        return False

    last_proof = chain[-1]
    return verify_context_proof(handoff_file, last_proof)


def execute_push(commit_msg=""):
    """Execute git add, git commit, and git push."""
    msg = commit_msg if commit_msg else f"save(mb-save): update session state {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"

    print("[MB-SAVE] Esecuzione `git add .`...")
    out, err, code = run_cmd("git add .")
    if code != 0:
        print(f"[MB-SAVE] Errore git add: {err}")
        return False

    print(f"[MB-SAVE] Esecuzione `git commit -m \"{msg}\"`...")
    out, err, code = run_cmd(f'git commit -m "{msg}"')
    if code != 0 and "nothing to commit" not in out and "nothing to commit" not in err:
        print(f"[MB-SAVE] Note commit: {out or err}")

    print("[MB-SAVE] Esecuzione `git push`...")
    out, err, code = run_cmd("git push")
    if code == 0:
        print("[MB-SAVE] Push su GitHub completato con successo!")
        return True
    else:
        print(f"[MB-SAVE] Risultato git push: {out or err}")
        return False


def main():
    parser = argparse.ArgumentParser(description="MB Save System CLI (Secp256k1 Protected)")
    subparsers = parser.add_subparsers(dest="command", help="Comandi di salvataggio e compattazione")

    # Command: status
    p_status = subparsers.add_parser("status", help="Mostra lo stato corrente di git e contesto")

    # Command: save
    p_save = subparsers.add_parser("save", help="Salvataggio semplice (SESSION_STATE.md)")
    p_save.add_argument("--note", type=str, default="", help="Nota opzionale della sessione")

    # Command: compact
    p_compact = subparsers.add_parser("compact", help="Salvataggio e compattazione contesto (HANDOFF.md)")
    p_compact.add_argument("--objective", type=str, default="", help="Obiettivo principale della sessione")
    p_compact.add_argument("--note", type=str, default="", help="Note di avanzamento")

    # Command: verify
    p_verify = subparsers.add_parser("verify", help="Verifica l'integrità crittografica di HANDOFF.md")

    # Command: push
    p_push = subparsers.add_parser("push", help="Salvataggio, compattazione, firma Secp256k1 e push su GitHub")
    p_push.add_argument("--message", type=str, default="", help="Messaggio di commit git")

    args = parser.parse_args()

    if args.command == "status":
        info = get_git_info()
        print(f"Branch: {info['branch']}\nLast Commit: {info['last_commit']}\nStatus:\n{info['status']}")
    elif args.command == "save":
        generate_session_state(note=args.note)
    elif args.command == "compact":
        generate_session_state(note=args.note)
        generate_handoff(objective=args.objective)
    elif args.command == "verify":
        verify_handoff_integrity()
    elif args.command == "push":
        generate_session_state(note=args.message)
        generate_handoff(objective=args.message)
        execute_push(commit_msg=args.message)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
