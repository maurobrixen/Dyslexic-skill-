# 🚀 MB Skills - Raccolta Skill Custom per Agenti AI & Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Antigravity Compatible](https://img.shields.io/badge/Antigravity-Compatible-brightgreen.svg)]()
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()

> **MB Skills** è un repository completo e strutturato di **Skill personalizzate** per Agenti AI (Antigravity IDE / Gemini Agent).  
> È progettato per estendere le capacità degli agenti con un focus prioritario su **conservazione del contesto**, **ottimizzazione del consumo di token** e **integrazioni API avanzate**.

---

## 🇮🇹 Documentazione in Italiano

### 📌 Caratteristiche Principali

- 💾 **MB Save System (`mb-save-system`)**: Sistema avanzato per il salvataggio della sessione (`/ms`), compattazione del contesto in `HANDOFF.md`, pulizia dei cicli di loop e sincronizzazione automatica con GitHub.
- 🧪 **ChEMBL Bio-Database (`mb-chembl-database`)**: Interrogazione farmacologica, dati di bioattività (`IC50`, `Ki`), target molecolari, download di strutture SDF 3D e immagini 2D.
- 📐 **Template Riutilizzabile (`_template`)**: Modello standard con intestazione YAML per creare rapidamente nuove skill conforme alle specifiche ufficiali.

---

### 📂 Struttura del Repository

```text
Skil/
├── README.md                 # Documentazione principale (ITA / ENG)
├── .gitignore                # Regole di esclusione file e secret
├── HANDOFF.md                # File di stato sessione compattato ad alto risparmio token
├── SESSION_STATE.md          # Snapshot veloce dello stato di lavoro
└── skills/                   # Raccolta delle Skill attive
    ├── _template/            # Modello base per nuove skill
    │   └── SKILL.md
    ├── mb-save-system/       # Sistema di salvataggio sessione e sync Git
    │   ├── SKILL.md
    │   ├── scripts/save_cli.py
    │   └── resources/handoff_template.md
    └── mb-chembl-database/   # Integrazione ChEMBL API
        ├── SKILL.md
        ├── scripts/chembl_api.py
        └── references/
```

---

### 🚀 Come Attivare le Skill negli Agenti AI

Per rendere disponibili le skill nel tuo agente Antigravity / Gemini:

#### Opzione 1: Inserimento Diretto nel Workspace
Copia le cartelle desiderate da `skills/` nella directory del tuo progetto:
```text
.agents/skills/mb-save-system/
.agents/skills/mb-chembl-database/
```

#### Opzione 2: Registrazione Globale (`skills.json`)
Aggiungi il percorso di questo repository all'interno del file di configurazione `skills.json` nel tuo profilo utente:
```json
{
  "entries": [
    { "path": "C:/Users/tuo_utente/OneDrive/Desktop/!! Ai/--Antigravity/Skil/skills" }
  ]
}
```

---

### 📚 Indice delle Skill Disponibili

| Nome Skill | Descrizione | Comandi / Trigger | Percorso |
| :--- | :--- | :--- | :--- |
| **`mb-save-system`** | Salvataggio sessione, compattazione contesto & push Git | `/ms`, `/ms salva-push`, `/ms salva-compatta` | [`skills/mb-save-system/SKILL.md`](./skills/mb-save-system/SKILL.md) |
| **`mb-chembl-database`** | Interrogazione molecole bioattive, target e bioattività | `/chembl-database`, ChEMBL queries | [`skills/mb-chembl-database/SKILL.md`](./skills/mb-chembl-database/SKILL.md) |
| **`_template`** | Modello standard per la creazione di nuove skill | Custom | [`skills/_template/SKILL.md`](./skills/_template/SKILL.md) |

---

### 💾 Guida Dettagliata a `mb-save-system` (`/ms`)

La skill `mb-save-system` risolve il problema della **perdita di memoria tra le sessioni** e **riduce drasticamente il consumo dei token** sintetizzando lo stato in un file `HANDOFF.md`.

#### Modalità di utilizzo:

- **`/ms salva`**: Genera un report rapido `SESSION_STATE.md` contenente status git, commit recente e file modificati.
- **`/ms salva-compatta`**: Genera un file `HANDOFF.md` compresso con obiettivi raggiunti, decisioni architetturali e task aperti a bassissimo costo di token per il riavvio della sessione.
- **`/ms salva-push`**: Esegue la compattazione del contesto, lo stage dei file (`git add .`), il commit ed il `git push` su GitHub.
- **`/ms compact-loop`**: Sintetizza i cicli di loop lunghi o iterativi per liberare contesto nell'agente.
- **`/ms ripristina`**: Consente all'agente di riprendere la sessione ricaricando all'istante lo stato da `HANDOFF.md`.

---

### ➕ Come Creare una Nuova Skill

1. Copia la cartella `skills/_template/` rinominandola con il nome della tua skill (es. `skills/mb-mia-skill/`).
2. Edita `SKILL.md` mantenendo il frontmatter YAML:
   ```yaml
   ---
   name: mb-mia-skill
   description: Descrizione chiara delle funzionalità e di quando l'agente deve attivarla.
   ---
   ```
3. Aggiungi eventuali script in `scripts/`, file statici in `resources/` o documentazione in `references/`.
4. Aggiorna la tabella in `README.md` ed effettua il commit.

---

<br>

---

## 🇬🇧 English Documentation

### 📌 Project Overview

**MB Skills** is a modular repository of custom **AI Agent Skills** designed for the Antigravity IDE and Gemini Agent framework.  
It focuses on **context preservation**, **token efficiency**, and **seamless workflow automation**.

### 🛠️ Featured Skills

- **`mb-save-system`**: Context compaction, session handoff generation (`HANDOFF.md`), and automated Git/GitHub synchronization.
- **`mb-chembl-database`**: Bioactive compound searches, drug target lookups, bioactivity normalization (IC50/Ki), and 3D structure downloads via ChEMBL REST API.
- **`_template`**: Production-ready template for creating new custom skills with YAML frontmatter.

### ⚡ Quick Start

Copy any skill from `skills/` to your project's `.agents/skills/` directory or reference this repository path in your global `skills.json` configuration file.

---

## 📄 Licenza / License

Distribuito sotto licenza [MIT](LICENSE). Libero per uso personale e commerciale.
