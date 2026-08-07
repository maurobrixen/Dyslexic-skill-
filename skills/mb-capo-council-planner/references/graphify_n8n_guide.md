# 🕸️ Guida all'Integrazione: Graphify & Agenti n8n

Questo documento stabilisce le linee guida per integrare **Graphify (Grafo della Conoscenza)** e gli **Workflow n8n** all'interno dei piani prodotti dalla Skill `mb-capo-council-planner`.

---

## 🕸️ 1. Integrazione Graphify (Mappe Concettuali 3D)

### Cos'e Graphify nel contesto della Skill
Graphify trasforma la struttura di un progetto o di una codebase in una rete di nodi e relazioni (Knowledge Graph), riducendo il consumo di token e permettendo all'Agente e al CAPO di navigare l'architettura a colpo d'occhio.

### Come applicarlo durante la pianificazione
1. **Per Progetti Nuovi (Greenfield)**:
   - Genera una mappa concettuale Graphify delle entita chiave, delle risorse e dei flussi logici prima di scrivere il codice.
   - Esprimi il grafo in formato Mermaid per la visualizzazione immediata in chat.

2. **Per Progetti Esistenti (Brownfield)**:
   - Analizza la cartella di progetto per estrarre le relazioni tra i file e i moduli esistenti.
   - Identifica visivamente i componenti isolati (orphaned code) o ad alto accoppiamento.

---

## ⚡ 2. Integrazione Agenti e Workflow n8n

### Quando raccomandare Workflow n8n
L'Agente deve proporre la creazione o l'integrazione di workflow n8n per:
- Automazione di task di backend e cron-job schedulati.
- Integrazione di API di terze parti (Telegram, Slack, Email, Webhooks, CRM).
- Orchestrazione di pipeline di dati e agenti AI secondari.

### Struttura di un Nodo n8n nel Piano
Per ogni automazione identificata nel piano maestro, definire:
- **Trigger**: Webhook, Schedule, Evento HTTP o Cambio Stato.
- **Nodi di Elaborazione**: Code node (JS/Python), AI Agent node, HTTP Request node.
- **Output / Azione**: Salvataggio DB, notifica, aggiornamento stato.
