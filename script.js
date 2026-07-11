// =====================================================
// MOBILE NAV
// =====================================================

const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");

if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
        navLinks.classList.toggle("open");
    });

    navLinks.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => navLinks.classList.remove("open"));
    });
}

// =====================================================
// SCROLL REVEAL
// =====================================================

const revealEls = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window && revealEls.length) {
    const io = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                io.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });

    revealEls.forEach(el => io.observe(el));
} else {
    revealEls.forEach(el => el.classList.add("is-visible"));
}

// =====================================================
// TERMINAL TYPING EFFECT (hero signature element)
// =====================================================

const typedLineEl = document.getElementById("typedLine");
const historyEl = document.getElementById("consoleHistory");

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const consoleLines = [
    { cmd: "whoami", out: "maycon — full stack dev" },
    { cmd: "cat stack.txt", out: "python · html · css · js" },
    { cmd: "python jogo.py", out: "carregando cassino... 🎲" },
    { cmd: "echo $MOOD", out: "café + código = 💚" }
];

let lineIndex = 0;

function typeLine(text, onDone) {
    let i = 0;
    typedLineEl.textContent = "";
    const speed = 45;

    function step() {
        if (i <= text.length) {
            typedLineEl.textContent = text.slice(0, i);
            i++;
            setTimeout(step, speed);
        } else if (onDone) {
            setTimeout(onDone, 500);
        }
    }
    step();
}

function pushHistory(cmd, out) {
    if (!historyEl) return;
    const row = document.createElement("div");
    row.className = "console-line";
    row.innerHTML = `<span class="prompt">$</span> ${cmd}<br><span class="out">${out}</span>`;
    historyEl.appendChild(row);

    // keep only the last 2 entries so the console doesn't overflow
    while (historyEl.children.length > 2) {
        historyEl.removeChild(historyEl.firstChild);
    }
}

function runConsoleLoop() {
    if (!typedLineEl) return;
    const current = consoleLines[lineIndex % consoleLines.length];

    typeLine(current.cmd, () => {
        pushHistory(current.cmd, current.out);
        typedLineEl.textContent = "";
        lineIndex++;
        setTimeout(runConsoleLoop, 900);
    });
}

if (typedLineEl) {
    if (prefersReducedMotion) {
        typedLineEl.textContent = consoleLines[0].cmd;
        pushHistory(consoleLines[0].cmd, consoleLines[0].out);
    } else {
        runConsoleLoop();
    }
}

// little blink for the cat mascot sitting on the console
const catEyeL = document.getElementById("catEyeL");
const catEyeR = document.getElementById("catEyeR");

if (catEyeL && catEyeR && !prefersReducedMotion) {
    setInterval(() => {
        [catEyeL, catEyeR].forEach(eye => eye.setAttribute("ry", "0.4"));
        setTimeout(() => {
            [catEyeL, catEyeR].forEach(eye => eye.removeAttribute("ry"));
        }, 150);
    }, 3200);
}

// =====================================================
// GITHUB STATS (live, public API — falls back silently)
// =====================================================

async function loadGithubStats() {
    const repoStat = document.querySelector('[data-stat="repos"]');
    const followerStat = document.querySelector('[data-stat="followers"]');
    if (!repoStat && !followerStat) return;

    try {
        const res = await fetch("https://api.github.com/users/Maycondev07");
        if (!res.ok) throw new Error("github api error");
        const data = await res.json();

        if (repoStat) repoStat.textContent = data.public_repos ?? "—";
        if (followerStat) followerStat.textContent = data.followers ?? "—";
    } catch (err) {
        // fallback: keep placeholders tidy instead of a stuck em-dash
        if (repoStat) repoStat.textContent = "—";
        if (followerStat) followerStat.textContent = "—";
    }
}

loadGithubStats();

// =====================================================
// FILTRO DE PROJETOS (grid da home)
// =====================================================

function filtrar(categoria) {
    const cards = document.querySelectorAll("#projetos .card");
    const buttons = document.querySelectorAll(".filtros button");

    buttons.forEach(btn => btn.classList.remove("active"));
    const activeBtn = Array.from(buttons).find(b => b.getAttribute("onclick") === `filtrar('${categoria}')`);
    if (activeBtn) activeBtn.classList.add("active");

    cards.forEach(card => {
        if (categoria === "todos" || card.classList.contains(categoria)) {
            card.style.display = "flex";
        } else {
            card.style.display = "none";
        }
    });
}
