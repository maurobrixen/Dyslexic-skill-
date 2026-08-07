---
name: mb-biofeedback-frequency-engine
description: Engine per l'analisi di segnali biofeedback (HRV, EEG, biometrici, tono vocale) e modulazione di frequenze acustiche/visive di risonanza. Usa questa skill quando lavori su elaborazione di segnali fisiologici, sintetizzatori di frequenze, algoritmi di biofeedback o stati emotivi/cognitivi dell'utente.
---

# 🔊 Skill: `mb-biofeedback-frequency-engine`
> **Elaborazione Biofeedback & Modulazione di Frequenze di Risonanza**

Questa skill fornisce all'Agente le istruzioni e la logica per interagire con i moduli di **biofeedback**, calcolare metriche biometriche (HRV, ritmi EEG Alpha/Theta/Beta, tono emotivo vocale) e sintetizzare frequenze audio/visive armoniche (`frequency_engine.py`, `biofeedback.py`).

---

## 👁️ Principi Operativi

1. **Riconoscimento Segnali Biometrici**: Mappa i dati in ingresso da sensori (pulsossimetri, EEG, analisi vocale) in stati di attivazione fisiologica (Relax, Focus, Stress, Trance).
2. **Generazione di Frequenze Armoniche**: Calcola frequenze binaurali, toni iso-cronici e risonanze (es. Solfeggio, Onda Schumann 7.83Hz, Frequenze Focus 40Hz Beta/Gamma).
3. **Feedback Loop Terapeutico**: Modula dinamicamente le uscite acustiche e visive in base alla risposta in tempo reale del soggetto.

---

## ⚡ Trigger di Attivazione

Attiva questa skill quando:
- Si lavora sui moduli `biofeedback.py`, `frequency_engine.py`, `voice_speaker.py` o simili.
- L'utente richiede di generare toni, frequenze binaurali o pattern di sincronizzazione cerebrale.
- Occorre analizzare dati biometrici o frequenziali.

---

## 📊 Matrice di Frequenza e Stati Cognitivi

| Banda EEG / Frequenza | Gamma (Hz) | Stato Associato | Applicazione Biofeedback |
| :--- | :--- | :--- | :--- |
| **Delta** | 0.5 - 4 Hz | Sonno profondo, rigenerazione | Rilassamento muscolare totale, recupero |
| **Theta** | 4 - 8 Hz | Meditazione, creatività visiva | Pensiero per immagini, stato IPNAGOGICO |
| **Alpha** | 8 - 13 Hz | Calma vigile, riduzione stress | Stato di Flow, apprendimento accelerato |
| **Beta** | 13 - 30 Hz | Attenzione attiva, problem solving | Focus analitico, elaborazione dati |
| **Gamma** | 30 - 100 Hz | Integrazione cognitiva superiore | Insight creativi, sintesi multi-modale |

---

## ⚙️ Esempio di Codice / Logica Modulazione

```python
# Sintesi Frequenza Binaurale Focus (40Hz Gamma over 432Hz Carrier)
def generate_binaural_beat(carrier_freq=432.0, beat_freq=40.0, duration_sec=10):
    left_channel = carrier_freq - (beat_freq / 2.0)
    right_channel = carrier_freq + (beat_freq / 2.0)
    return {
        "left_hz": left_channel,  # 412.0 Hz
        "right_hz": right_channel, # 452.0 Hz
        "target_state": "FOCUS_GAMMA"
    }
```
