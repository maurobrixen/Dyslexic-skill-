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

    subgraph Security ["🛡️ DevSecOps Bitcoin Crypto Engine (karpathy/cryptos)"]
        CRYPTO_ENGINE["skills/mb-save-system/scripts/mb_crypto_engine.py"]
        CHAIN["CONTEXT_CHAIN.json (Context Blockchain Ledger)"]
        VAULT_KEY[".vault_key (Secp256k1 Private Key)"]
        CRYPTO_ENGINE --> CHAIN
        VAULT_KEY --> CRYPTO_ENGINE
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
    SAVE_CLI --> CRYPTO_ENGINE
    S8 --> CRYPTO_ENGINE
    S2 --> S1
    S4 --> S5
```

---

## 🔐 Integrità Crittografica del Contesto (Bitcoin Secp256k1 + SHA-256)

Tutti i salvataggi ed i riavvii di contesto (`HANDOFF.md`, `SESSION_STATE.md`) utilizzano il motore crittografico nativo:

1. **Double SHA-256 Digest**: Impronta digitale univoca calcolata ad ogni compattazione.
2. **Firma ECDSA Secp256k1**: Firma del digest mediante la chiave privata del Vault (`.vault_key`).
3. **Context Blockchain Ledger**: Ogni blocco firmato è collegato al digest del blocco precedente in `CONTEXT_CHAIN.json`.
4. **Zero Hallucination / Anti-Tampering**: Al riavvio dell'Agente, la firma ed il digest vengono verificati. Se il file è stato manomesso, l'Agente notifica l'alterazione.

---

## ⚡ Gerarchia Tassativa di Codice (Zero Spreco)

```mermaid
flowchart LR
    Step1["1. 🔍 Audit Codice Esistente\n(Re-use First)"] --> Step2["2. 📦 Libreria Standard\n(Standard Library)"]
    Step2 --> Step3["3. 📚 Libreria Esterna Solida\n(External Package)"]
    Step3 --> Step4["4. ✍️ Codice Custom Ex-Novo\n(Extrema Ratio)"]
```

### 1. 🔍 Level 1: Audit & Re-Use First
* **Azione**: Cerca nel codebase se esiste già una funzione, helper o script (es. `save_cli.py`, `mb_crypto_engine.py`).
* **Obiettivo**: Zero duplicazione di logica.

### 2. 📦 Level 2: Standard Library Second
* **Azione**: Sfrutta i moduli nativi del linguaggio prima di importare dipendenze esterne.
* **Esempi Python**: `hashlib` (sha256/ripemd160), `pathlib` (file/path), `json` (serialization), `subprocess` (shell execution), `asyncio` (concorrenza).

### 3. 📚 Level 3: External Library Third
* **Azione**: Ispirazione ed adattamento dei principi di `karpathy/cryptos` in Python puro a zero dipendenze pesanti.

### 4. ✍️ Level 4: Custom Code Last Resort
* **Azione**: Implementazione dell'aritmetica di curva ellittica Secp256k1 nativa per la firma del contesto.
