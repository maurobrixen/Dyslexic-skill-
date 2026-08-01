#!/usr/bin/env python3
"""
save_cli.py - MB Save & Context Handoff System
CLI helper to automate session state capture, context compaction, and git synchronization.
"""

import argparse
import datetime
import os
import subprocess
import sys

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
*Generato automaticamente da MB Save System*
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[MB-SAVE] Stato sessione salvato in {output_file}")
    return output_file

def generate_handoff(output_file="HANDOFF.md", objective="", decisions=None, tasks=None, next_steps=None):
    """Generate a condensed HANDOFF document for token-efficient session resumes."""
    git_info = get_git_info()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    decisions_str = "\n".join([f"- {d}" for d in (decisions or ["Nessuna decisione registrata"])])
    tasks_str = "\n".join([f"- [ ] {t}" for t in (tasks or ["Nessun task in sospeso"])])
    next_steps_str = "\n".join([f"1. {s}" for s in (next_steps or ["Proseguire secondo i requisiti utente"])])

    content = f"""# 📑 HANDOFF SESSION STATE (Token Optimized)

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
    return output_file

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
    parser = argparse.ArgumentParser(description="MB Save System CLI")
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

    # Command: push
    p_push = subparsers.add_parser("push", help="Salvataggio, compattazione e push su GitHub")
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
    elif args.command == "push":
        generate_session_state(note=args.message)
        generate_handoff(objective=args.message)
        execute_push(commit_msg=args.message)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
