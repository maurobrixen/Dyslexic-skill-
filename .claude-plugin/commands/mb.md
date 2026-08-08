---
description: Salvataggio avanzato della sessione, compattazione contesto Secp256k1 e sync Git.
---

Attiva la skill `mb-save-system`:
1. Esegui lo script `python skills/mb-save-system/scripts/save_cli.py save`.
2. Firma il blocco di contesto con crittografia Secp256k1.
3. Aggiorna `HANDOFF.md` e `SESSION_STATE.md` mantenendo il massimo risparmio di token.
4. Esegui il commit ed il push automatico su Git se richiesto.
