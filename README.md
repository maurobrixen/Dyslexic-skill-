# 🚀 MB Skills - Raccolta Skill Custom per Agenti AI & Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Antigravity Compatible](https://img.shields.io/badge/Antigravity-Compatible-brightgreen.svg)]()
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()

> **MB Skills** è un repository completo e strutturato di **Skill personalizzate** per Agenti AI (Antigravity IDE / Gemini Agent).  
> È progettato per estendere le capacità degli agenti con un focus prioritario su **conservazione del contesto**, **ottimizzazione del consumo di token** e **integrazioni API avanzate**.

---

## 🇮🇹 Documentazione in Italiano

### 📌 Caratteristiche Principali

- 💾 **MB Save System (`mb-save-system`)**: Sistema avanzato per il salvataggio della sessione (`/mb`), compattazione del contesto in `HANDOFF.md`, pulizia dei cicli di loop e sincronizzazione automatica con GitHub.
- 🧪 **ChEMBL Bio-Database (`mb-chembl-database`)**: Interrogazione farmacologica, dati di bioattività (`IC50`, `Ki`), target molecolari, download di strutture SDF 3D e immagini 2D.
- 🧠 **MB Dyslexia & Visual Thought Decoder (`mb-dyslexia-visual-thought-decoder`)**: Skill ad alto risparmio di token per la decodifica in tempo reale della scrittura dislessica (refusi QWERTY, agglutinazioni, elisioni) e traduzione del pensiero visivo-spaziale non lineare in risposte strutturate *Visual-First*.
- 🏰 **MB Second Brain & Memory Vault (`mb-second-brain-memory-vault`)**: Integrazione per la Cattedrale della Memoria, allineamento col Mao Mind Clone, gestione del grafo di conoscenza e protezione dati tramite Vault crittografato.
- 🔊 **MB Biofeedback & Frequency Engine (`mb-biofeedback-frequency-engine`)**: Elaborazione segnali fisiologici (HRV, EEG, tono vocale) e modulazione armonica di frequenze acustiche/visive.
- 🎨 **MB Web Dashboard Builder (`mb-web-dashboard-builder`)**: Generatore di Dashboard Web standalone in Vanilla HTML/CSS/JS (Dark mode neon, glassmorphism, grafici Canvas/SVG).
- ⚒️ **MB Agent Skill Forge (`mb-agent-skill-forge`)**: Meta-skill per progettare, validare, documentare e registrare nuove competenze per Agenti AI.
- 🌿 **MB Autonomous Git Orchestrator (`mb-autonomous-git-orchestrator`)**: Orchestrazione avanzata di versione Git, commit semantici, tag di release e sync remoto.
- 🌌 **MB Antigravity UI Designer (`mb-antigravity-ui-designer`)**: Design System per interfacce utente visive ad alto impatto, micro-animazioni CSS3 e temi ad alto contrasto.
- 📐 **Template Riutilizzabile (`_template`)**: Modello standard con intestazione YAML per creare rapidamente nuove skill conforme alle specifiche ufficiali.

---

### 🧠 Gerarchia Tassativa di Sviluppo (Zero Spreco)

Tutte le modifiche ed il codice sviluppato in questo repository seguono la regola d'oro in 4 livelli:
1. 🔍 **RE-USE FIRST**: Audit del codice e degli script esistenti (`save_cli.py`, ecc.) per riutilizzare funzioni già pronte.
2. 📦 **STANDARD LIB SECOND**: Utilizzo prioritario dei moduli della libreria standard (`pathlib`, `json`, `subprocess`, `asyncio`, `hashlib`).
3. 📚 **EXTERNAL LIB THIRD**: Adozione di librerie esterne collaudate solo se la libreria standard non soddisfa i requisiti.
4. ✍️ **CUSTOM CODE LAST RESORT**: Scrittura di codice personalizzato ex-novo **solo ed esclusivamente come extrema ratio**.

> 🕸️ **Mappa Concettuale 3D**: Consulta il file [**ARCHITECTURE_MAP.md**](./ARCHITECTURE_MAP.md) per il grafo della conoscenza Graphify completo dell'ecosistema.

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
    ├── mb-chembl-database/   # Integrazione ChEMBL API
    ├── mb-dyslexia-visual-thought-decoder/ # Decodifica dislessia e pensiero per immagini
    ├── mb-second-brain-memory-vault/ # Cattedrale della Memoria & Mind Clone Sync
    ├── mb-biofeedback-frequency-engine/ # Elaborazione segnali biometrici & frequenze
    ├── mb-web-dashboard-builder/  # Generatore di Dashboard Web standalone
    ├── mb-agent-skill-forge/      # Meta-skill per la forgiatura di nuove skill
    ├── mb-autonomous-git-orchestrator/ # Orchestratore Git & commit semantici
    └── mb-antigravity-ui-designer/     # Design System & micro-animazioni UI/UX
```

---

### 🚀 Come Attivare le Skill negli Agenti AI

> 📖 **Guida Dettagliata**: Per le istruzioni complete con comandi PowerShell e modelli di configurazione, consulta la guida [**INSTALL.md**](./INSTALL.md).

Per rendere disponibili le skill nel tuo agente Antigravity / Gemini:

#### Opzione 1: Inserimento Diretto nel Workspace
Copia le cartelle desiderate da `skills/` nella directory del tuo progetto:
```text
.agents/skills/mb-save-system/
.agents/skills/mb-second-brain-memory-vault/
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
| **`mb-save-system`** | Salvataggio sessione, compattazione contesto & push Git | `/mb`, `/mb salva-push`, `/mb salva-compatta` | [`skills/mb-save-system/SKILL.md`](./skills/mb-save-system/SKILL.md) |
| **`mb-chembl-database`** | Interrogazione molecole bioattive, target e bioattività | `/chembl-database`, ChEMBL queries | [`skills/mb-chembl-database/SKILL.md`](./skills/mb-chembl-database/SKILL.md) |
| **`mb-dyslexia-visual-thought-decoder`** | Decodifica scrittura dislessica, refusi fonetico-tattili e pensiero per immagini 3D | Refusi QWERTY, dislessia, pensiero visivo, salti logici | [`skills/mb-dyslexia-visual-thought-decoder/SKILL.md`](./skills/mb-dyslexia-visual-thought-decoder/SKILL.md) |
| **`mb-second-brain-memory-vault`** | Cattedrale della Memoria, allineamento Mao Mind Clone & Vault crittografato | Memoria lungo termine, Secondo Cervello, Mind Clone, Vault | [`skills/mb-second-brain-memory-vault/SKILL.md`](./skills/mb-second-brain-memory-vault/SKILL.md) |
| **`mb-biofeedback-frequency-engine`** | Elaborazione biofeedback (HRV, EEG) e sintesi di frequenze di risonanza | Biofeedback, HRV, EEG, frequenze binaurali | [`skills/mb-biofeedback-frequency-engine/SKILL.md`](./skills/mb-biofeedback-frequency-engine/SKILL.md) |
| **`mb-web-dashboard-builder`** | Generazione dashboard web standalone Vanilla HTML/CSS/JS | Dashboard web, HTML/CSS, glassmorphism, UI | [`skills/mb-web-dashboard-builder/SKILL.md`](./skills/mb-web-dashboard-builder/SKILL.md) |
| **`mb-agent-skill-forge`** | Fucina e validazione automatica di nuove Skill per Agenti AI | Crea skill, nuova competenza agentica | [`skills/mb-agent-skill-forge/SKILL.md`](./skills/mb-agent-skill-forge/SKILL.md) |
| **`mb-autonomous-git-orchestrator`** | Orchestrazione avanzata di versione Git, release e commit semantici | Git status, commit semantici, release, push | [`skills/mb-autonomous-git-orchestrator/SKILL.md`](./skills/mb-autonomous-git-orchestrator/SKILL.md) |
| **`mb-antigravity-ui-designer`** | Design System UI/UX premium, micro-animazioni CSS3 & temi visivi | UI design, animazioni CSS, layout spaziali | [`skills/mb-antigravity-ui-designer/SKILL.md`](./skills/mb-antigravity-ui-designer/SKILL.md) |
| **`_template`** | Modello standard per la creazione di nuove skill | Custom | [`skills/_template/SKILL.md`](./skills/_template/SKILL.md) |

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
- **`mb-dyslexia-visual-thought-decoder`**: Real-time decoding of dyslexic typing patterns, QWERTY keystroke slips, and non-linear visual-spatial thinking ("pensiero per immagini").
- **`mb-second-brain-memory-vault`**: Long-term memory cathedral indexing, Mao Mind Clone alignment, knowledge graph visual synchronization, and encrypted vault privacy protection.
- **`mb-biofeedback-frequency-engine`**: Physiological signal analysis (HRV, EEG, voice tone) and binaural/harmonic resonance frequency modulation.
- **`mb-web-dashboard-builder`**: Standalone HTML5/CSS3/JS dark-mode dashboard generator with canvas charts and glassmorphism.
- **`mb-agent-skill-forge`**: Meta-skill for forging, validating, documenting, and registering new AI Agent Skills.
- **`mb-autonomous-git-orchestrator`**: Advanced Git version orchestrator for conventional semantic commits, release tagging, and remote sync.
- **`mb-antigravity-ui-designer`**: Premium UI/UX design system, CSS3 micro-animations, and high-contrast spatial themes for visual thinkers.
- **`_template`**: Production-ready template for creating new custom skills with YAML frontmatter.

### ⚡ Quick Start

Copy any skill from `skills/` to your project's `.agents/skills/` directory or reference this repository path in your global `skills.json` configuration file.

---

## 📄 Licenza / License

Distribuito sotto licenza [MIT](LICENSE). Libero per uso personale e commerciale.

