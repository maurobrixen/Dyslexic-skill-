# 🛠️ Raccolta Skill Custom per Agenti AI

Benvenuto nella repository delle **Skill Custom** per agenti Antigravity / AI.
Questo repository raccoglie e organizza tutte le skill sviluppate su misura per automatizzare workflow, integrazioni API, analisi dati e sviluppo software.

---

## 📁 Struttura della Repository

```text
.
├── README.md               # Guida generale e indice delle skill
├── .gitignore              # Configurazioni Git Ignore
└── skills/                 # Cartella contenente le varie skill
    ├── _template/          # Template base per creare una nuova skill
    │   └── SKILL.md
    └── (altre skill)
```

---

## 🚀 Come creare una nuova Skill

1. Copia la cartella `skills/_template/` fornendo il nome della nuova skill (es. `skills/mia-nuova-skill/`).
2. Apri il file `SKILL.md` all'interno della nuova cartella.
3. Compila l'intestazione YAML:
   ```yaml
   ---
   name: mia-nuova-skill
   description: Descrizione chiara ed esaustiva di cosa fa questa skill e quando deve essere usata dall'agente.
   ---
   ```
4. Aggiungi le istruzioni dettagliate in formato Markdown. Se la skill richiede script o risorse esterne, organizzale nelle sottocartelle:
   - `scripts/`: Script helper (Python, Bash, Node, ecc.)
   - `resources/`: File statici o configurazioni
   - `references/`: Documentazione di approfondimento

---

## 📚 Indice delle Skill Disponibili

| Nome Skill | Descrizione | Percorso |
| :--- | :--- | :--- |
| `_template` | Template base per la creazione di nuove skill | [`skills/_template/SKILL.md`](./skills/_template/SKILL.md) |
| `mb-chembl-database` | Interrogazione ChEMBL DB (molecole, target, bioattività, SDF/SVG) | [`skills/mb-chembl-database/SKILL.md`](./skills/mb-chembl-database/SKILL.md) |


---

## 💻 Installazione / Utilizzo nell'Agente

Per attivare questa raccolta di skill nel tuo ambiente Antigravity / Agent:
- Puoi copiare la cartella della singola skill in `.agents/skills/<nome-skill>/` o in `C:\Users\<utente>\.gemini\config\skills\<nome-skill>/`.
- Oppure registrare il percorso del repository all'interno del file `skills.json` delle tue configurazioni globali.
