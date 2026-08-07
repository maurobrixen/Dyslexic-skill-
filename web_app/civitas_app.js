/* 🌌 SECOND CHANGE SIMULATOR - LIVE KPI & SOCIETY VISUALIZER */

let civitasCanvas, civitasCtx;
let citizens = [];
let simRunning = false;
let isPrimeDirective = true;

class VisualCitizen {
  constructor(id, x, y) {
    this.id = id;
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 2;
    this.vy = (Math.random() - 0.5) * 2;
    this.freedom = 0.95;
    this.trust = 0.99;
    this.compliance = 1.0;
    this.friction = 0.01;
    this.synergy = 1.0;
    this.resonance = 0.95;
  }

  update(width, height, primeActive) {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < 10 || this.x > width - 10) this.vx *= -1;
    if (this.y < 10 || this.y > height - 10) this.vy *= -1;

    if (primeActive) {
      this.compliance = Math.min(1.0, this.compliance + 0.002);
      this.friction = Math.max(0.005, this.friction * 0.98);
      this.resonance = Math.min(1.0, this.resonance + 0.002);
      this.synergy += 0.006;
    } else {
      this.compliance = Math.max(0.2, this.compliance - 0.005);
      this.friction += 0.005;
      this.resonance = Math.max(0.1, this.resonance * 0.99);
      this.synergy = Math.max(0.2, this.synergy * 0.995);
    }
  }

  draw(ctx, primeActive) {
    ctx.beginPath();
    ctx.arc(this.x, this.y, 5, 0, Math.PI * 2);
    ctx.fillStyle = primeActive ? "#00ff87" : "#ff007f";
    ctx.shadowBlur = 10;
    ctx.shadowColor = primeActive ? "#00ff87" : "#ff007f";
    ctx.fill();
    ctx.shadowBlur = 0;
  }
}

function initCivitasSimulation() {
  civitasCanvas = document.getElementById("civitas-canvas");
  if (!civitasCanvas) return;
  civitasCtx = civitasCanvas.getContext("2d");

  civitasCanvas.width = civitasCanvas.offsetWidth;
  civitasCanvas.height = civitasCanvas.offsetHeight;

  const count = parseInt(document.getElementById("pop-slider") ? document.getElementById("pop-slider").value : 80) || 80;
  citizens = [];
  for (let i = 0; i < count; i++) {
    citizens.push(new VisualCitizen(i, Math.random() * civitasCanvas.width, Math.random() * civitasCanvas.height));
  }

  simRunning = true;
  requestAnimationFrame(loopCivitasSimulation);
}

function loopCivitasSimulation() {
  if (!simRunning || !civitasCtx) return;

  civitasCtx.clearRect(0, 0, civitasCanvas.width, civitasCanvas.height);

  for (let i = 0; i < citizens.length; i++) {
    for (let j = i + 1; j < citizens.length; j++) {
      const dx = citizens[i].x - citizens[j].x;
      const dy = citizens[i].y - citizens[j].y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 90) {
        civitasCtx.beginPath();
        civitasCtx.moveTo(citizens[i].x, citizens[i].y);
        civitasCtx.lineTo(citizens[j].x, citizens[j].y);
        civitasCtx.strokeStyle = isPrimeDirective ? `rgba(0, 242, 254, ${1 - dist/90})` : `rgba(255, 0, 127, ${1 - dist/90})`;
        civitasCtx.lineWidth = 0.8;
        civitasCtx.stroke();
      }
    }
  }

  let totalSynergy = 0, totalFriction = 0, totalCompliance = 0, totalResonance = 0;
  citizens.forEach(c => {
    c.update(civitasCanvas.width, civitasCanvas.height, isPrimeDirective);
    c.draw(civitasCtx, isPrimeDirective);
    totalSynergy += c.synergy;
    totalFriction += c.friction;
    totalCompliance += c.compliance;
    totalResonance += c.resonance;
  });

  const avgSyn = (totalSynergy / citizens.length).toFixed(2);
  const avgFric = (totalFriction / citizens.length).toFixed(3);
  const avgComp = ((totalCompliance / citizens.length) * 100).toFixed(1);
  const avgRes = ((totalResonance / citizens.length) * 100).toFixed(1);

  if (document.getElementById("stat-synergy")) document.getElementById("stat-synergy").innerText = `${avgSyn}x`;
  if (document.getElementById("stat-friction")) document.getElementById("stat-friction").innerText = avgFric;
  if (document.getElementById("kpi-compliance")) {
    document.getElementById("kpi-compliance").innerText = `${avgComp}%`;
    document.getElementById("kpi-compliance-bar").style.width = `${avgComp}%`;
  }
  if (document.getElementById("kpi-resonance")) {
    document.getElementById("kpi-resonance").innerText = `${avgRes}%`;
    document.getElementById("kpi-resonance-bar").style.width = `${avgRes}%`;
  }

  requestAnimationFrame(loopCivitasSimulation);
}

function toggleDirectiveMode() {
  isPrimeDirective = !isPrimeDirective;
  const btn = document.getElementById("mode-toggle-btn");
  const modeTitle = document.getElementById("sim-mode-title");
  
  if (isPrimeDirective) {
    if (btn) btn.innerText = "🔄 Passa a Burocrazia Tradizionale";
    if (btn) btn.classList.remove("btn-secondary");
    if (modeTitle) {
      modeTitle.innerText = "Second Change: Il Secondo Cambiamento (Società di Libertà e Rispetto Reciproco)";
      modeTitle.style.color = "var(--accent-green)";
    }
  } else {
    if (btn) btn.innerText = "🔄 Attiva Legge Suprema di Libertà";
    if (btn) btn.classList.add("btn-secondary");
    if (modeTitle) {
      modeTitle.innerText = "Società Burocratica Tradizionale (Alto Attrito & Controllo Forzato)";
      modeTitle.style.color = "var(--accent-magenta)";
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initCivitasSimulation();
});
