/* 🌌 GINEVRA CIVITAS SIMULATOR - INTERACTIVE SOCIETY SIMULATION ENGINE */

let civitasCanvas, civitasCtx;
let citizens = [];
let simRunning = false;
let isPrimeDirective = true;
let animReq;

class VisualCitizen {
  constructor(id, x, y) {
    self = this;
    this.id = id;
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 2;
    this.vy = (Math.random() - 0.5) * 2;
    this.freedom = 0.9;
    this.trust = 0.95;
    this.friction = 0.05;
    this.synergy = 1.0;
  }

  update(width, height, primeActive) {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < 10 || this.x > width - 10) this.vx *= -1;
    if (this.y < 10 || this.y > height - 10) this.vy *= -1;

    if (primeActive) {
      this.friction = Math.max(0.01, this.friction * 0.98);
      this.synergy += 0.005;
    } else {
      this.friction += 0.005;
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

  const count = parseInt(document.getElementById("pop-slider").value) || 80;
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

  // Draw interactions between citizens
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

  // Update & Draw citizens
  let totalSynergy = 0, totalFriction = 0;
  citizens.forEach(c => {
    c.update(civitasCanvas.width, civitasCanvas.height, isPrimeDirective);
    c.draw(civitasCtx, isPrimeDirective);
    totalSynergy += c.synergy;
    totalFriction += c.friction;
  });

  // Update stats
  const avgSyn = (totalSynergy / citizens.length).toFixed(2);
  const avgFric = (totalFriction / citizens.length).toFixed(3);
  document.getElementById("stat-synergy").innerText = `${avgSyn}x`;
  document.getElementById("stat-friction").innerText = avgFric;

  requestAnimationFrame(loopCivitasSimulation);
}

function toggleDirectiveMode() {
  isPrimeDirective = !isPrimeDirective;
  const btn = document.getElementById("mode-toggle-btn");
  const modeTitle = document.getElementById("sim-mode-title");
  
  if (isPrimeDirective) {
    btn.innerText = "🔄 Passa a Burocrazia Tradizionale";
    btn.classList.remove("btn-secondary");
    modeTitle.innerText = "Società di Libertà e Rispetto Reciproco (Ginevra Prime Directive)";
    modeTitle.style.color = "var(--accent-green)";
  } else {
    btn.innerText = "🔄 Attiva Legge Suprema di Libertà";
    btn.classList.add("btn-secondary");
    modeTitle.innerText = "Società Burocratica Tradizionale (Alto Attrito & Controllo)";
    modeTitle.style.color = "var(--accent-magenta)";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initCivitasSimulation();
});
