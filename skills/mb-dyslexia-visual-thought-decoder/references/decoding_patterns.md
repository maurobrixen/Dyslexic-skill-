# 📖 Guida dei Pattern di Decodifica: Dislessia & Pensiero per Immagini

Questo documento fornisce esempi pratici per aiutare l'Agente AI a comprendere la casistica reale di frasi, refusi e strutture non lineari tipiche dei pensatori visivo-spaziali.

---

## 1. Mappatura Tastiera QWERTY & Refusi Adiacenti

Quando si digita rapidamente per "inseguire" un'immagine mentale rapida, la mano scivola sui tasti vicini.

| Carattere Digitato | Carattere Inteso | Motivazione Posizionale |
| :--- | :--- | :--- |
| `,` | `m` / `k` / `l` | La virgola è subito sotto `K` e a destra di `M`. |
| `w` | `e` / `q` / `s` | La `W` è adiacente a `E` e `Q`. |
| `u` | `i` / `y` / `j` | La `U` è adiacente a `I` e `Y`. |
| `o` | `i` / `p` / `l` | La `O` è adiacente a `I` e `P`. |

### Esempio Reale:
> **Input Utente**: `usa èper iul m,oento q uesta cartellachiedmi i permessi che sevon`
>
> **Fasi di Decodifica dell'Agente**:
> 1. `èper` $\rightarrow$ `è per` (spazio saltato tra verbo/preposizione).
> 2. `iul` $\rightarrow$ `il` (inversione vocale `u/i`).
> 3. `m,oento` $\rightarrow$ `momento` (tasto `,` premuto al posto di `m`).
> 4. `q uesta` $\rightarrow$ `questa` (spazio inserito involontariamente).
> 5. `cartellachiedmi` $\rightarrow$ `cartella chiedimi` (agglutinazione di due termini).
> 6. `sevon` $\rightarrow$ `servono` (elisione di consonante interna `r`).
>
> **Risultato Decodificato**: *"Usa per il momento questa cartella, chiedimi i permessi che servono."*

---

## 2. Decodifica dei Salti Logici (Macro-Leaps)

I pensatori visivi elaborano il sistema in modo olistico. Invece di descrivere la sequenza A $\rightarrow$ B $\rightarrow$ C $\rightarrow$ D, pronunciano A e D perché vedono già l'intera figura.

### Esempio Reale:
> **Input Utente**: `voglio dashboard grafici sqlite`
>
> **Interpretazione Agente**:
> - **Nodo A**: Creazione UI / Dashboard.
> - **Nodo B (Invisibile ma implicito)**: Server backend o connessione DB.
> - **Nodo C (Invisibile ma implicito)**: Query SQL / estrazione metriche.
> - **Nodo D**: Database SQLite locale.
>
> **Azione Agente**: Non chiedere *"Quale backend vuoi usare per collegare SQLite ai grafici?"*. Costruisci direttamente la struttura (es. Python/Streamlit o HTML/JS con SQLite) mostrando l'architettura completa nel diagramma Mermaid.

---

## 3. Guida allo Stile di Risposta Visual-First

Per garantire che la risposta sia leggibile al 100% per un utente dislessico:

- **Contrasto e Scannabilità**: Usa il grassetto per le prime 2-3 parole di ogni riga principale.
- **Icone Visive**: Usa emoji coerenti come marker visivi (es. 🎯 per obiettivi, ⚙️ per impostazioni, 🚀 per azioni).
- **Diagrammi Sintetici**: Non superare i 5-6 nodi nei diagrammi Mermaid per mantenere immediata la percezione della mappa.
