---
name: mb-web-dashboard-builder
description: Generatore di Dashboard Web premium, interattive e standalone in Vanilla HTML5, CSS3 avanzato (Dark Mode, Glassmorphism, Neon Glow) e JavaScript Canvas/SVG. Usala quando l'utente richiede di creare interfacce grafiche, pannelli di controllo, visualizzatori di dati o dashboard per i propri progetti.
---

# 🎨 Skill: `mb-web-dashboard-builder`
> **Generazione di Dashboard Web Standalone ad Alto Impatto Visivo**

Questa skill guida l'Agente nella creazione autonoma di **dashboard web moderne, veloci e visivamente spettacolari** (stile `second_brain_dashboard.html`, `ginevra_graphify.html`, `web_dashboard.py`) senza dipendenze esterne pesanti.

---

## 💎 Design System & Regole Estetiche

- **Estetica Dark Mode Premium**: Fondo scuro HSL (es. `#0a0b10`, `#121520`), accenti al neon (Ciano `#00f0ff`, Viola `#9d4edd`, Verde Smeraldo `#00f5d4`).
- **Glassmorphism**: Schede con sfondi semi-trasparenti `backdrop-filter: blur(12px)`, bordi sottili semi-trasparenti `border: 1px solid rgba(255, 255, 255, 0.1)`.
- **Tipografia Moderna**: Google Fonts Inter, Outfit, Fira Code per blocchi di dati.
- **Visualizzazioni Interattive**: Grafici Canvas 2D/SVG nativi per grafi di conoscenza, indicatori di stato, frequenze in tempo reale o log di sistema.

---

## ⚡ Trigger di Attivazione

Attiva questa skill quando:
- L'utente richiede di creare un'interfaccia web, dashboard, pannello di controllo o visualizzazione dati.
- Si lavora su file `.html`, `.css`, `web_dashboard.py` o strumenti di visualizzazione.
- Si rende necessario rappresentare graficamente nodi di conoscenza o metriche di sistema.

---

## 🛠️ Modello Base di Dashboard (Vanilla Stack)

```html
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MB Dashboard</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0a0e17;
      --card-bg: rgba(20, 27, 45, 0.6);
      --accent: #00f0ff;
      --text: #f0f4fc;
    }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', sans-serif;
      margin: 0; padding: 2rem;
    }
    .glass-card {
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 1.5rem;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
    }
  </style>
</head>
<body>
  <div class="glass-card">
    <h1>🚀 MB Control Center</h1>
    <p>Dashboard autonoma attiva.</p>
  </div>
</body>
</html>
```
