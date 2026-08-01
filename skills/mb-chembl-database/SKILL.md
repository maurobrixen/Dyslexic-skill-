---
name: mb-chembl-database
description: >
  Skill MB per interrogare il database ChEMBL: ricerca molecole bioattive, target terapeutici,
  dati di bioattività (IC50, Ki), farmaci approvati e ricerche di struttura chimica.
  Da attivare anche tramite /chembl-database o per richieste su composti chimici e farmacologia.
---

# 🧪 MB Skill - ChEMBL Database Query

Questa skill (della suite **MB Skill**) fornisce l'integrazione completa per interrogare il database **ChEMBL**, accedere ai dati farmacologici, target biologici, strutture molecolari (SDF/MOL/SVG) e misurazioni di bioattività.

---

## 📋 Prerequisiti

1. **`uv`**: Assicurati che `uv` sia installato ed eseguibile nell'ambiente.
2. **Licenza ChEMBL**: Tutti i dati provengono dal database ChEMBL. Verificare le condizioni di licenza su [ChEMBL Documentation](https://chembl.gitbook.io/chembl-interface-documentation/about).

---

## ⚙️ Regole Principali

- **Usa lo Script dedicato**: Esegui sempre le interrogazioni tramite lo script `scripts/chembl_api.py`.
- **Output su File (--output)**: Ogni comando richiede il parametro `--output <percorso_file.json>` per salvare i risultati strutturati.
- **Normalizzazione Unità**: Per i dati di bioattività (`IC50`, `Ki`, `EC50`), usa la flag `--normalize` per convertire tutti i valori in `nM`.

---

## 🚀 Esempi di Comandi Utili

### 1. Controllo dello Stato dell'API
```bash
uv run scripts/chembl_api.py status --output /tmp/status.json
```

### 2. Ricerca Molecole e Farmaci
```bash
# Ricerca molecola per nome (es. Aspirina)
uv run scripts/chembl_api.py molecule --search "aspirin" --limit 3 --output /tmp/aspirin.json

# Download del file di struttura 3D (SDF)
uv run scripts/chembl_api.py molecule --id CHEMBL25 --dl_format sdf --output /tmp/aspirin.sdf
```

### 3. Ricerca Target Biologici e Bioattività
```bash
# Ricerca per target (es. EGFR)
uv run scripts/chembl_api.py target --search "EGFR" --limit 5 --output /tmp/egfr_targets.json

# Filtra bioattività IC50 normalizzate in nM
uv run scripts/chembl_api.py activity --filter target_chembl_id=CHEMBL203 standard_type=IC50 --normalize --limit 10 --output /tmp/egfr_ic50.json
```

### 4. Ricerca per Similitudine Molecolare (SMILES)
```bash
uv run scripts/chembl_api.py similarity --smiles "CC(=O)Oc1ccccc1C(=O)O" --similarity 85 --limit 5 --output /tmp/similar.json
```

---

## 📚 Riferimenti

- Documentazione dettagliata degli endpoint: [`references/api_endpoints.md`](./references/api_endpoints.md)
- Citazioni scientifiche: [`references/citation.bib`](./references/citation.bib)
