# 🕸️ ARCHITECTURE MAP & GRAPHIFY KNOWLEDGE MAP

> **MB Skills Suite - Mappa Concettuale dell'Ecosistema Agentico**

---

## 🏛️ Grafo Concettuale 3D (Graphify)

```mermaid
graph TD
    subgraph Core ["🌌 Antigravity IDE & Gemini Agent Framework"]
        IDE["Antigravity IDE"]
        CLAUDE["Claude Code / Claude Desktop"]
        GEMINI["Gemini Agent / Custom Prompt Engine"]
    end

    subgraph Registry ["📦 Registrazione & Plugin Manifest"]
        SKILLS_JSON["skills.json (Config Globale)"]
        CLAUDE_MARKETPLACE[".claude-plugin/marketplace.json"]
        CLAUDE_PLUGIN[".claude-plugin/plugin.json"]
    end

    subgraph Skills ["⚡ MB Skills Suite (10 Moduli)"]
        S1["mb-dyslexia-visual-thought-decoder"]
        S2["mb-capo-council-planner"]
        S3["mb-save-system"]
        S4["mb-agent-skill-forge"]
        S5["mb-antigravity-ui-designer"]
        S6["mb-autonomous-git-orchestrator"]
        S7["mb-biofeedback-frequency-engine"]
        S8["mb-second-brain-memory-vault"]
        S9["mb-web-dashboard-builder"]
        S10["mb-chembl-database"]
    end

    subgraph Helpers ["🐍 Python Helper Scripts"]
        SAVE_CLI["skills/mb-save-system/scripts/save_cli.py"]
    end

    IDE --> SKILLS_JSON
    CLAUDE --> CLAUDE_MARKETPLACE
    CLAUDE --> CLAUDE_PLUGIN
    SKILLS_JSON --> Skills
    CLAUDE_MARKETPLACE --> Skills

    S3 --> SAVE_CLI
    S2 --> S1
    S4 --> S5
```

---

## ⚡ Gerarchia Tassativa di Codice (Zero Spreco)

Tutti gli agenti ed i contributori di questo repository sono vincolati a seguire questa gerarchia prima di produrre qualsiasi riga di codice:

```mermaid
flowchart LR
    Step1["1. 🔍 Audit Codice Esistente\n(Re-use First)"] --> Step2["2. 📦 Libreria Standard\n(Standard Library)"]
    Step2 --> Step3["3. 📚 Libreria Esterna Solida\n(External Package)"]
    Step3 --> Step4["4. ✍️ Codice Custom Ex-Novo\n(Extrema Ratio)"]
```

### 1. 🔍 Level 1: Audit & Re-Use First
* **Azione**: Cerca nel codebase se esiste già una funzione, helper o script (es. `save_cli.py`, funzioni utility).
* **Obiettivo**: Zero duplicazione di logica.

### 2. 📦 Level 2: Standard Library Second
* **Azione**: Sfrutta i moduli nativi del linguaggio prima di importare dipendenze esterne.
* **Esempi Python**: `pathlib` (file/path), `json` (serialization), `hashlib` (crypto/sha256), `subprocess` (shell execution), `asyncio` (concorrenza), `argparse` (CLI parsing).
* **Esempi JS/Node**: `fs/promises`, `path`, `crypto`, `events`, `url`.

### 3. 📚 Level 3: External Library Third
* **Azione**: Se la libreria standard non è sufficiente, identifica ed utilizza pacchetti aperti, solidi e testati dalla community.
* **Esempi Python**: `pydantic` (validazione tipi), `httpx` / `requests` (HTTP client), `pyyaml` (YAML parsing), `rich` (interfaccia terminale).
* **Esempi JS**: `zod`, `axios`, `express`.

### 4. ✍️ Level 4: Custom Code Last Resort
* **Azione**: Scrivi algoritmi e funzioni personalizzate **solo se nessuna libreria esistente copre il fabbisogno**.
