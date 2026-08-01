---
name: mb-save-system
description: >
  Skill MB per la conservazione del contesto e l'ottimizzazione dei token a fine sessione.
  Permette di effettuare salvataggi rapidi, compattazione del contesto in HANDOFF.md,
  aggiornamento dei cicli di loop e push automatico su GitHub (tramite comandi come /mb, /mb salva, /mb salva-compatta, /mb salva-push).
---

# 💾 MB Skill - System Save & Context Preservation

Questa skill fornisce all'agente un **protocollo avanzato per il salvataggio della sessione, la compattazione del contesto e la sincronizzazione con Git/GitHub**, con priorità assoluta sulla **conservazione del contesto senza perdita di informazioni** e sul **risparmio massimo di token**.

---

## 🎯 Quando Usare Questa Skill

Attiva questa skill ogni volta che l'utente usa un comando o frase come:
- `/mb` o `/mb salva`
- `/mb salva-compatta` o `/mb compact`
- `/mb salva-push` o `/mb push`
- `/mb compact-loop`
- `/mb ripristina`
- Frasi come *"salva la sessione"*, *"compatti il contesto prima di chiudere"*, *"fai il push e salva lo stato"*.

---

## 🛠️ Comandi Operativi & Modalità

### 1. `/mb salva` (Salvataggio Semplice)
Crea o aggiorna il file `SESSION_STATE.md` nel workspace con:
- Data e ora del salvataggio.
- Branch Git attivo e ultimo commit.
- Elenco dei file modificati non ancora committati.

**Esecuzione Agente**:
```bash
python skills/mb-save-system/scripts/save_cli.py save --note "Descrizione sintetica dello stato attuale"
```

---

### 2. `/mb salva-compatta` (Salvataggio & Compattazione Contesto)
Genera sia `SESSION_STATE.md` che un file **`HANDOFF.md`** altamente compresso e ottimizzato a basso consumo di token per il riavvio della sessione.

**Esecuzione Agente**:
1. Esegui la compattazione:
   ```bash
   python skills/mb-save-system/scripts/save_cli.py compact --objective "Obiettivo principale della sessione"
   ```
2. Aggiorna `HANDOFF.md` assicurandoti che contenga:
   - **Obiettivi Raggiunti**: Cosa è stato completato nella sessione.
   - **Decisioni Architetturali**: Regole o scelte fondamentali da non dimenticare.
   - **Loop / Task Aperti**: Cosa rimane da fare nella sessione successiva.
   - **Prossimi Passi**: I primi 2-3 comandi o azioni da compiere al riavvio.

---

### 3. `/mb salva-push` (Salvataggio, Compattazione & Push su GitHub)
Esegue la compattazione del contesto (`salva-compatta`), poi effettua lo stage dei file, il commit ed il push su GitHub.

**Esecuzione Agente**:
```bash
python skills/mb-save-system/scripts/save_cli.py push --message "feat/save: salva e compattazione sessione"
```

---

### 4. `/mb compact-loop` (Compattazione Cicli di Loop)
Pulisce i file di lavoro temporanei e sintetizza i log prolissi di sviluppo o debug per evitare sovraccarico di token nel contesto dell'agente.

---

### 5. `/mb ripristina` (Ripristino Context a Inizio Sessione)
All'avvio di una nuova sessione, se è presente un file `HANDOFF.md` o `SESSION_STATE.md`, leggi immediatamente quel file usando `view_file` per ripristinare istantaneamente il contesto con il minimo consumo di token.

---

## 📌 Regole di Conservazione Contesto

> [!IMPORTANT]
> - **Priorità Assoluta**: Non perdere MAI dettagli critici (es. bug risolti, scelte di configurazione, path modificati).
> - **Compattazione Intelligente**: Mantieni la massima densità informativa riducendo le parole superflue nei riassunti.
> - **Igiene Repository**: Assicurati che file temporanei non necessari vengano esclusi da `.gitignore`.
