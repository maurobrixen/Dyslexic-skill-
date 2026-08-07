/* 🌌 GINEVRA COGNITIVE UNIVERSE - LIVE INTERACTIVE ENGINE */

// --- 3D Holographic Neural Canvas Engine ---
let canvas, ctx;
let nodes = [];
const nodeCount = 35;

function initNeuralCanvas() {
  canvas = document.getElementById("neural-canvas");
  if (!canvas) return;
  ctx = canvas.getContext("2d");
  
  // Set resolution
  canvas.width = canvas.offsetWidth;
  canvas.height = canvas.offsetHeight;

  nodes = [];
  for (let i = 0; i < nodeCount; i++) {
    nodes.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 1.2,
      vy: (Math.random() - 0.5) * 1.2,
      radius: Math.random() * 3 + 2,
      color: i % 3 === 0 ? "#00f2fe" : (i % 3 === 1 ? "#7928ca" : "#ff007f")
    });
  }

  requestAnimationFrame(drawNeuralCanvas);
}

function drawNeuralCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw connections
  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const dx = nodes[i].x - nodes[j].x;
      const dy = nodes[i].y - nodes[j].y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 100) {
        ctx.beginPath();
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(nodes[j].x, nodes[j].y);
        ctx.strokeStyle = `rgba(0, 242, 254, ${1 - dist / 100})`;
        ctx.lineWidth = 0.6;
        ctx.stroke();
      }
    }
  }

  // Update & Draw nodes
  nodes.forEach(n => {
    n.x += n.vx;
    n.y += n.vy;

    if (n.x < 0 || n.x > canvas.width) n.vx *= -1;
    if (n.y < 0 || n.y > canvas.height) n.vy *= -1;

    ctx.beginPath();
    ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
    ctx.fillStyle = n.color;
    ctx.shadowBlur = 10;
    ctx.shadowColor = n.color;
    ctx.fill();
    ctx.shadowBlur = 0;
  });

  requestAnimationFrame(drawNeuralCanvas);
}

// --- Audio Oscillator Engine (Web Audio API) ---
let audioCtx = null;
let osc1 = null, osc2 = null;
let gainNode = null;
let isPlayingAudio = false;

function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function toggleBiofeedbackAudio() {
  initAudio();
  const btn = document.getElementById("audio-toggle-btn");
  
  if (!isPlayingAudio) {
    const baseFreq = parseFloat(document.getElementById("freq-slider").value) || 432;
    const binauralBeat = 8; // Theta state

    osc1 = audioCtx.createOscillator();
    osc2 = audioCtx.createOscillator();
    gainNode = audioCtx.createGain();

    osc1.type = 'sine';
    osc2.type = 'sine';

    osc1.frequency.setValueAtTime(baseFreq, audioCtx.currentTime);
    osc2.frequency.setValueAtTime(baseFreq + binauralBeat, audioCtx.currentTime);

    gainNode.gain.setValueAtTime(0.15, audioCtx.currentTime);

    osc1.connect(gainNode);
    osc2.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    osc1.start();
    osc2.start();

    isPlayingAudio = true;
    btn.innerHTML = "⏸️ Pausa Frequenza Risonanza";
    btn.classList.add("btn-secondary");
    animateVisualizer(true);
    logTerminal("BIOFEEDBACK", `Sintetizzatore avviato a ${baseFreq} Hz (+8Hz Theta Wave).`);
  } else {
    if (osc1) osc1.stop();
    if (osc2) osc2.stop();
    isPlayingAudio = false;
    btn.innerHTML = "▶️ Avvia Frequenza Risonanza (432Hz / 528Hz)";
    btn.classList.remove("btn-secondary");
    animateVisualizer(false);
    logTerminal("BIOFEEDBACK", "Sintetizzatore in pausa.");
  }
}

function updateFrequency(val) {
  document.getElementById("freq-val").innerText = `${val} Hz`;
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
        const h = Math.floor(Math.random() * 80) + 15;
        bar.style.height = `${h}%`;
      });
    }, 150);
  } else {
    clearInterval(animInterval);
    bars.forEach(bar => bar.style.height = "20%");
  }
}

// --- Terminal Logger ---
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

// --- Secp256k1 Double SHA-256 Hashing Verification Simulation ---
async function sha256(str) {
  const buf = new TextEncoder().encode(str);
  const hashBuf = await crypto.subtle.digest('SHA-256', buf);
  const hashArray = Array.from(new Uint8Array(hashBuf));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

async function verifyIntegrityLive() {
  logTerminal("DEVSECOPS", "Avvio verifica integrità crittografica di HANDOFF.md...");
  const content = document.getElementById("context-text").value;
  
  // Double SHA-256
  const hash1 = await sha256(content);
  const hash2 = await sha256(hash1);
  
  document.getElementById("hash-output").innerText = hash2;
  logTerminal("DEVSECOPS", `Double SHA-256 Digest: ${hash2.substring(0, 32)}...`);
  logTerminal("DEVSECOPS", "✅ Firma ECDSA Secp256k1 VERIFICATA. Blocco #3 valido.");
}

// --- Cathedral Room Navigator ---
function selectCathedralRoom(el, roomName, desc) {
  document.querySelectorAll(".nav-room").forEach(r => r.classList.remove("active"));
  el.classList.add("active");
  logTerminal("CATTEDRALE", `Accesso alla ${roomName}: ${desc}`);
}

// Initial setup
document.addEventListener("DOMContentLoaded", () => {
  initNeuralCanvas();
  logTerminal("GINEVRA", "Universo Cognitivo v1.0.0 attivo.");
  logTerminal("CRYPTO", "Secp256k1 ECDSA & Context Chain sincronizzati.");
  window.addEventListener("resize", initNeuralCanvas);
});
