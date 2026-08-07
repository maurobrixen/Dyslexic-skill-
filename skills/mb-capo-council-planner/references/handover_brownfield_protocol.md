# 🔄 Protocollo Handover e Gestione Progetti Esistenti (Brownfield)

Questo protocollo stabilisce come la Skill `mb-capo-council-planner` analizza, comprende e riprende in mano progetti gia avviati, garantendo continuity cognitiva e riscrittura dinamica del Piano Maestro.

---

## 🔍 Fase 1: Scansione Completa e Diagnosi dello Stato

Quando il comando `/capo-resume` o un'analisi di progetto esistente viene invocata, l'Agente esegue la scansione sequenziale di:

1. **`HANDOFF.md`**: Per comprendere lo stato dell'ultima sessione, le attivita completate, i blocchi riscontrati e le raccomandazioni aperte.
2. **`SESSION_STATE.md`**: Per verificare variabili di stato attive, contesto corrente e obiettivi immediati.
3. **`README.md` & Documentazione**: Per comprendere la visione originaria del progetto.
4. **Codebase & Graphify**: Esegue l'analisi delle directory per identificare i file esistenti, le librerie installate e generare il grafo delle dipendenze reali.

---

## 📊 Fase 2: Matrice di Avanzamento (Cosa e Fatto vs Cosa Manca)

L'Agente genera una tabella riassuntiva di diagnosi:

| Modulo / Componente | Stato Attuale | Completamento (%) | Note / Blocchi Evidenziati dal Consiglio |
| :--- | :--- | :--- | :--- |
| **Core Architecture** | ✅ Completato | 100% | Architettura di base solida. |
| **API Integration** | 🟡 In Corso | 50% | Mancano gestire rate limit e retry policy. |
| **UI / Dashboard** | 🔴 Non Iniziato | 0% | Da progettare con standard premium e dark mode. |

---

## 📝 Fase 3: Riscrittura Dinamica del Piano Maestro

Il Consiglio dei Saggi e **IL CAPO** riesaminano il progetto alla luce dello stato reale:
- **Senior Architect**: Identifica debito tecnico accumulato nelle parti gia sviluppate.
- **IL CAPO**: Riformula il **Piano Maestro Aggiornato**, eliminando i task gia completati e ridefinendo le priorita per il completamento con la massima chiarezza e rispetto della Legge di Liberta.
