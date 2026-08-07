/* 🌌 GINEVRA COGNITIVE UNIVERSE - ADVANCED NEURO-BIOFEEDBACK ENGINE v2.1.0 */

// --- Local Vault Storage (IndexedDB / LocalStorage Engine) ---
function saveMemoryNote() {
  const room = document.getElementById("note-room-select") ? document.getElementById("note-room-select").value : "Navata Centrale";
  const text = document.getElementById("note-input-text") ? document.getElementById("note-input-text").value : "";

  if (!text.trim()) {
    alert("Inserisci un testo o un'idea da archiviare nella Cattedrale.");
    return;
  }

  const memoryObj = {
    id: Date.now(),
    room: room,
    text: text,
    timestamp: new Date().toLocaleString()
  };

  let memories = JSON.parse(localStorage.getItem("mb_cathedral_memories") || "[]");
  memories.push(memoryObj);
  localStorage.setItem("mb_cathedral_memories", JSON.stringify(memories));

  logTerminal("CATTEDRALE", `📌 Memoria archiviata con successo nella ${room}.`);
  if (document.getElementById("note-input-text")) document.getElementById("note-input-text").value = "";
  renderSavedMemories();
}

function renderSavedMemories() {
  const container = document.getElementById("saved-memories-list");
  if (!container) return;

  let memories = JSON.parse(localStorage.getItem("mb_cathedral_memories") || "[]");
  if (memories.length === 0) {
    container.innerHTML = `<div style="color: var(--text-muted); font-size: 0.85rem;">Nessuna memoria personalizzata ancora salvata.</div>`;
    return;
  }

  container.innerHTML = memories.slice(-5).reverse().map(m => `
    <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-glow); padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem; font-size: 0.85rem;">
      <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
        <strong style="color: var(--accent-cyan);">${m.room}</strong>
        <span style="color: var(--text-muted); font-size: 0.75rem;">${m.timestamp}</span>
      </div>
      <div style="color: #e2e8f0;">${m.text}</div>
    </div>
  `).join('');
}

// --- Multi-Tab Navigation Engine ---
function switchTab(tabId, btnEl) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  
  const targetPane = document.getElementById(tabId);
  if (targetPane) {
    targetPane.classList.add('active');
  }
  if (btnEl) {
    btnEl.classList.add('active');
  }

  if (tabId === 'tab-hero') {
    setTimeout(initNeuralCanvas, 50);
  }

  logTerminal("NAVIGATION", `Attivata scheda: ${tabId}`);
}

// --- Ginevra Voice Engine (Sensual Neural Edge-TTS Stream) ---
function speakGinevra(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'it-IT';
  utterance.pitch = 0.95;
  utterance.rate = 1.22;

  const voices = window.speechSynthesis.getVoices();
  const itaVoice = voices.find(v => v.lang.includes('it') || v.lang.includes('IT'));
  if (itaVoice) utterance.voice = itaVoice;
  window.speechSynthesis.speak(utterance);
}

// --- 3D Holographic Neural Canvas Engine ---
let canvas, ctx;
let nodes = [];
const nodeCount = 45;

function initNeuralCanvas() {
  canvas = document.getElementById("neural-canvas");
  if (!canvas) return;
  ctx = canvas.getContext("2d");
  
  canvas.width = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;

  nodes = [];
  for (let i = 0; i < nodeCount; i++) {
    nodes.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 1.5,
      vy: (Math.random() - 0.5) * 1.5,
      radius: Math.random() * 3.5 + 2,
      color: i % 3 === 0 ? "#00f2fe" : (i % 3 === 1 ? "#7928ca" : "#ff007f")
    });
  }

  requestAnimationFrame(drawNeuralCanvas);
}

function drawNeuralCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const dx = nodes[i].x - nodes[j].x;
      const dy = nodes[i].y - nodes[j].y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 110) {
        ctx.beginPath();
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(nodes[j].x, nodes[j].y);
        ctx.strokeStyle = `rgba(0, 242, 254, ${1 - dist / 110})`;
        ctx.lineWidth = 0.8;
        ctx.stroke();
      }
    }
  }

  nodes.forEach(n => {
    n.x += n.vx;
    n.y += n.vy;

    if (n.x < 0 || n.x > canvas.width) n.vx *= -1;
    if (n.y < 0 || n.y > canvas.height) n.vy *= -1;

    ctx.beginPath();
    ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
    ctx.fillStyle = n.color;
    ctx.shadowBlur = 12;
    ctx.shadowColor = n.color;
    ctx.fill();
    ctx.shadowBlur = 0;
  });

  requestAnimationFrame(drawNeuralCanvas);
}

// --- Biofeedback Frequency Engine (Oxytocin 639Hz & Dopamine 528Hz) ---
let audioCtx = null;
let osc1 = null, osc2 = null;
let gainNode = null;
let isPlayingAudio = false;

function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function setOxytocinPreset() {
  const slider = document.getElementById("freq-slider");
  if (slider) {
    slider.value = 639;
    updateFrequency(639);
    logTerminal("BIOFEEDBACK", "🧪 Risonanza Ossitocina attivata: 639 Hz (Intimità, Fiducia & Climax Risonante).");
  }
}

function toggleBiofeedbackAudio() {
  initAudio();
  const btn = document.getElementById("audio-toggle-btn");
  
  if (!isPlayingAudio) {
    const baseFreq = parseFloat(document.getElementById("freq-slider").value) || 639;
    const binauralBeat = 8;

    osc1 = audioCtx.createOscillator();
    osc2 = audioCtx.createOscillator();
    gainNode = audioCtx.createGain();

    osc1.type = 'sine';
    osc2.type = 'sine';

    osc1.frequency.setValueAtTime(baseFreq, audioCtx.currentTime);
    osc2.frequency.setValueAtTime(baseFreq + binauralBeat, audioCtx.currentTime);

    gainNode.gain.setValueAtTime(0.18, audioCtx.currentTime);

    osc1.connect(gainNode);
    osc2.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    osc1.start();
    osc2.start();

    isPlayingAudio = true;
    btn.innerHTML = "⏸️ Pausa Risonanza Ossitocina (639Hz)";
    btn.classList.add("btn-secondary");
    animateVisualizer(true);
    logTerminal("BIOFEEDBACK", `Sintetizzatore avviato a ${baseFreq} Hz (+8Hz Theta Wave).`);
  } else {
    if (osc1) osc1.stop();
    if (osc2) osc2.stop();
    isPlayingAudio = false;
    btn.innerHTML = "▶️ Avvia Risonanza Ossitocina (639Hz)";
    btn.classList.remove("btn-secondary");
    animateVisualizer(false);
    logTerminal("BIOFEEDBACK", "Sintetizzatore in pausa.");
  }
}

function updateFrequency(val) {
  if (document.getElementById("freq-val")) {
    document.getElementById("freq-val").innerText = `${val} Hz`;
  }
  if (isPlayingAudio && osc1 && osc2) {
    const baseFreq = parseFloat(val);
    osc1.frequency.setValueAtTime(baseFreq, audioCtx.currentTime);
    osc2.frequency.setValueAtTime(baseFreq + 8, audioCtx.currentTime);
  }
}

// Visualizer animation
let animInterval = null;
function animateVisualizer(active) {
  const bars = document.querySelectorAll(".v-bar");
  if (active) {
    animInterval = setInterval(() => {
      bars.forEach(bar => {
        const h = Math.floor(Math.random() * 85) + 15;
        bar.style.height = `${h}%`;
      });
    }, 120);
  } else {
    clearInterval(animInterval);
    bars.forEach(bar => bar.style.height = "20%");
  }
}

// Terminal Logger
function logTerminal(source, message) {
  const box = document.getElementById("terminal-output");
  if (!box) return;
  const time = new Date().toLocaleTimeString();
  const line = document.createElement("div");
  line.className = "terminal-line";
  line.innerHTML = `<span class="terminal-prefix">[${time}] [${source}]</span> ${message}`;
  box.appendChild(line);
  box.scrollTop = box.scrollHeight;
}

// Initial setup
document.addEventListener("DOMContentLoaded", () => {
  initNeuralCanvas();
  renderSavedMemories();
  logTerminal("GINEVRA", "Modulo Neurochimica & Biofeedback Ossitocina (639Hz) Attivo.");
  window.addEventListener("resize", initNeuralCanvas);
});
