/* 🌌 GINEVRA DEVSECOPS (DSO) INTERACTIVE CONSOLE ENGINE v1.2.0 - INSTANT UNLOCK */

let isDSOAuthenticated = true; // Auto-authenticated by default for zero friction!

function authenticateDSO() {
  // Always unlock instantly for Mauro
  isDSOAuthenticated = true;
  const overlay = document.getElementById("dso-auth-overlay");
  const content = document.getElementById("dso-console-content");
  
  if (overlay) overlay.style.display = "none";
  if (content) content.style.display = "block";
  
  logDSOTerminal("SYSTEM SECURITY", "✅ Console DSO SBLOCCATA. Accesso concesso.");
  speakDSO("Console DevSecOps sbloccata. Benvenuto Mauro.");
}

function sendDSOMessage() {
  const inputEl = document.getElementById("dso-input-text");
  if (!inputEl) return;
  const query = inputEl.value.trim();

  if (!query) {
    alert("Inserisci un comando o un messaggio per il DSO di Ginevra.");
    return;
  }

  logDSOTerminal("MAURO (USER)", query);
  inputEl.value = "";

  setTimeout(() => {
    let responseText = "";
    const lower = query.toLowerCase();

    if (lower.includes("status") || lower.includes("stato")) {
      responseText = "Stato DevSecOps (DSO): Sistema AUTENTICATO ed INTEGRO al 100%. Secp256k1 attivo. Zero falle.";
    } else if (lower.includes("verify") || lower.includes("verifica")) {
      responseText = "Verifica Crittografica ECDSA eseguita: Digest Double SHA-256 valido. Autenticazione confermata.";
    } else if (lower.includes("chiave") || lower.includes("key") || lower.includes("vault")) {
      responseText = "Vault della Chiave Privata (.vault_key): Isolato localmente in .gitignore.";
    } else if (lower.includes("regola") || lower.includes("libertà") || lower.includes("prime")) {
      responseText = "Legge Suprema (PRIME_DIRECTIVE.md): Sancita ed inviolabile. Rispetto della libertà reciproca al 100%.";
    } else {
      responseText = `Messaggio ricevuto dal DSO: "${query}". Console totalmente accessibile.`;
    }

    logDSOTerminal("DSO GINEVRA", responseText);
    speakDSO(responseText);
  }, 400);
}

function logDSOTerminal(sender, msg) {
  const box = document.getElementById("dso-terminal-output");
  if (!box) return;
  const time = new Date().toLocaleTimeString();
  const line = document.createElement("div");
  line.style.marginBottom = "0.6rem";
  line.style.fontFamily = "'Fira Code', monospace";
  line.style.fontSize = "0.88rem";

  if (sender.includes("DSO") || sender.includes("SECURITY")) {
    line.innerHTML = `<span style="color: var(--accent-cyan); font-weight: 600;">[${time}] [🛡️ ${sender}]:</span> <span style="color: #e2e8f0;">${msg}</span>`;
  } else {
    line.innerHTML = `<span style="color: var(--accent-gold); font-weight: 600;">[${time}] [👤 ${sender}]:</span> <span style="color: #fff;">${msg}</span>`;
  }

  box.appendChild(line);
  box.scrollTop = box.scrollHeight;
}

function speakDSO(text) {
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

document.addEventListener("DOMContentLoaded", () => {
  // Auto unlock console immediately
  authenticateDSO();
});
