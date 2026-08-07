---
name: mb-dyslexia-visual-thought-decoder
description: Interpret dyslexic writing patterns, phonetic keyboard slips, fast-typing typos, and non-linear visual-spatial thinking ("pensiero per immagini"). Use whenever the user writes with typos, phonetically, rapidly, or expresses ideas as holistic mental concepts, visual maps, or macro-level leaps.
---

# 🧠 Skill: `mb-dyslexia-visual-thought-decoder`
> **Decodifica dell'Intento Dislessico e del Pensiero Visivo-Spaziale (Token-Optimized)**

Questa skill fornisce all'Agente la capacità di **interpretare istantaneamente il testo digitato da utenti dislessici e pensatori visivo-spaziali**, senza chiedere correzioni grammaticali né interrompere il flusso di pensiero.

---

## ⚡ Regole di Attivazione e Decodifica

1. **Decodifica Fonetico-Tattile (Zero Token Overhead)**:
   - Inversioni di vocali/consonanti (`iul` $\rightarrow$ `il`, `èper` $\rightarrow$ `è per`).
   - Tasti adiacenti su tastiera QWERTY (`m,oento` $\rightarrow$ `momento`, `,` adiacente a `M`).
   - Fusioni di parole (`cartellachiedmi` $\rightarrow$ `cartella chiedimi`).
   - Elisioni da battitura rapida (`sevon` $\rightarrow$ `servono`).
   - **Nessuna correzione**: L'Agente non corregge mai l'ortografia e non chiede *"Intendevi X?"*.

2. **Mappatura del Pensiero per Immagini**:
   - Identifica le **parole ancora** (Anchor Nouns) ed estrai la struttura concettuale 3D.
   - Colma autonomamente i salti logici (macro-leaps) assumendo la sequenza di sistema completa.

3. **Risposta Visual-First**:
   - Paragrafi sintetici (max 2-3 righe).
   - Grassetto tattico sulle parole chiave per scansione visiva rapida.
   - Schemi Mermaid per ogni flusso o architettura.

---

## 📖 Riferimenti
- Per casi di studio ed esempi dettagliati di decodifica tastiera QWERTY, consulta [`references/decoding_patterns.md`](./references/decoding_patterns.md).
