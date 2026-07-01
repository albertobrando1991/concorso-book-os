const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-11"
)

const palette = {
  bg: "#F8FAFC",
  ink: "#0F172A",
  muted: "#526174",
  border: "#CBD5E1",
  line: "#94A3B8",
  navy: "#10233F",
  bordeaux: "#7A2430",
  gold: "#D4AF37",
  green: "#2F7D5A",
  teal: "#1F6F78",
  cream: "#FFF7ED",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5",
  white: "#FFFFFF"
}

const figures = [
  {
    slug: "01-mappa-inglese-concorsuale",
    title: "Inglese concorsuale essenziale",
    subtitle: "Dalla lettura del bando alle risposte brevi, corrette e verificabili.",
    svg: figureMappa()
  },
  {
    slug: "02-metodo-cloze",
    title: "Cloze: risolvere la frase prima delle opzioni",
    subtitle: "Il completamento premia segnali grammaticali, collocazioni e scarto dei distrattori.",
    svg: figureCloze()
  },
  {
    slug: "03-tempi-verbali-segnali",
    title: "Tempi verbali e segnali",
    subtitle: "Nei quiz la scelta corretta nasce dal tempo indicato dalla frase.",
    svg: figureTempi()
  },
  {
    slug: "04-ausiliari-modali",
    title: "Be, do, have e modali",
    subtitle: "Domande, negazioni, tempi composti e obblighi dipendono dall'ausiliare.",
    svg: figureAusiliari()
  },
  {
    slug: "05-preposizioni-lessico-false-friends",
    title: "Preposizioni, lessico PA e false friends",
    subtitle: "Nei cloze contano collocazioni, contesto amministrativo e falsi amici.",
    svg: figureLessico()
  },
  {
    slug: "06-reading-email-orale",
    title: "Reading, email e orale",
    subtitle: "La prova valuta comprensione essenziale e comunicazione breve, ordinata, cortese.",
    svg: figureComunicazione()
  },
  {
    slug: "07-ripasso-diario-errori",
    title: "Piano di ripasso e diario errori",
    subtitle: "Pochi giorni richiedono priorita, simulazione e correzione per categoria.",
    svg: figureRipasso()
  }
]

async function main() {
  await fs.mkdir(OUTPUT_DIR, { recursive: true })

  for (const figure of figures) {
    await fs.writeFile(path.join(OUTPUT_DIR, `${figure.slug}.svg`), figure.svg, "utf8")
  }

  const browser = await chromium.launch({ headless: true })
  try {
    for (const figure of figures) {
      const page = await browser.newPage({
        viewport: { width: 1600, height: 900 },
        deviceScaleFactor: 1
      })
      const encoded = Buffer.from(figure.svg, "utf8").toString("base64")
      await page.setContent(
        `<html><body style="margin:0;background:${palette.bg}"><img src="data:image/svg+xml;base64,${encoded}" width="1600" height="900"></body></html>`,
        { waitUntil: "load" }
      )
      await page.locator("img").screenshot({
        path: path.join(OUTPUT_DIR, `${figure.slug}.png`)
      })
      await page.close()
    }
  } finally {
    await browser.close()
  }

  await fs.writeFile(path.join(OUTPUT_DIR, "README.md"), renderReadme(), "utf8")
}

function renderReadme() {
  return `# Asset Capitolo 11

Figure generate per \`Inglese concorsuale essenziale\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-inglese-concorsuale.png\` | Mappa generale: bando, cloze, grammatica, lessico, reading e output. |
| \`02-metodo-cloze.png\` | Metodo operativo per risolvere completamenti di frase. |
| \`03-tempi-verbali-segnali.png\` | Tempi verbali essenziali collegati ai segnali ricorrenti. |
| \`04-ausiliari-modali.png\` | Be, do, have, modali e risposte brevi. |
| \`05-preposizioni-lessico-false-friends.png\` | Preposizioni, collocazioni, lessico PA e falsi amici. |
| \`06-reading-email-orale.png\` | Metodo per reading, email formale e risposta orale breve. |
| \`07-ripasso-diario-errori.png\` | Piano di ripasso e diario degli errori per la materia inglese. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function shell(title, subtitle, inner) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">${esc(title)}</title>
  <desc id="desc">${esc(subtitle)}</desc>
  <defs>
    <style>
      .bg { fill: ${palette.bg}; }
      .card { fill: ${palette.white}; stroke: ${palette.border}; stroke-width: 3; }
      .softBlue { fill: ${palette.blueSoft}; stroke: #B9CBE0; stroke-width: 2.5; }
      .softRed { fill: ${palette.redSoft}; stroke: #E3B9BF; stroke-width: 2.5; }
      .softGold { fill: ${palette.goldSoft}; stroke: #E8D080; stroke-width: 2.5; }
      .softGreen { fill: ${palette.greenSoft}; stroke: #A8D1BD; stroke-width: 2.5; }
      .softTeal { fill: ${palette.tealSoft}; stroke: #A3D5D8; stroke-width: 2.5; }
      .note { fill: ${palette.cream}; stroke: #E7C18E; stroke-width: 2.5; }
      .ink { fill: ${palette.ink}; font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; }
      .muted { fill: ${palette.muted}; font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; }
      .title { font-size: 44px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-size: 23px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 25px; font-weight: 800; }
      .body { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 20px; }
      .small { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 18px; }
      .navy { fill: ${palette.navy}; }
      .bordeaux { fill: ${palette.bordeaux}; }
      .gold { fill: ${palette.gold}; }
      .green { fill: ${palette.green}; }
      .teal { fill: ${palette.teal}; }
      .line { stroke: ${palette.line}; stroke-width: 4; stroke-linecap: round; fill: none; }
      .thin { stroke: ${palette.border}; stroke-width: 2.5; stroke-linecap: round; fill: none; }
      .arrowNavy { stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowNavy); }
      .arrowBordeaux { stroke: ${palette.bordeaux}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowBordeaux); }
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
      .arrowGreen { stroke: ${palette.green}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGreen); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/>
    </marker>
    <marker id="arrowBordeaux" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.bordeaux}"/>
    </marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.green}"/>
    </marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="108" text-anchor="middle">${esc(subtitle)}</text>
${inner}
</svg>
`
}

function figureMappa() {
  const inner = `
  ${card(555, 180, 490, 145, "Prova di inglese", ["formato + livello", "peso nel bando"], "navy", "card")}
  <path class="line" d="M800 325 L800 388"/>
  <path class="line" d="M245 388 L1355 388"/>
  ${connector(245, 388, 245, 450)}
  ${connector(467, 388, 467, 575)}
  ${connector(689, 388, 689, 450)}
  ${connector(911, 388, 911, 575)}
  ${connector(1133, 388, 1133, 450)}
  ${connector(1355, 388, 1355, 575)}
  ${card(105, 450, 280, 130, "Bando", ["idoneita o punteggio", "A2, B1, B2"], "navy", "softBlue")}
  ${card(327, 575, 280, 130, "Cloze", ["frase, segnale", "scelta corretta"], "bordeaux", "softRed")}
  ${card(549, 450, 280, 130, "Grammatica", ["tempi, modali", "articoli, pronomi"], "gold", "softGold")}
  ${card(771, 575, 280, 130, "Lessico", ["PA, scadenze", "false friends"], "green", "softGreen")}
  ${card(993, 450, 280, 130, "Reading", ["testi brevi", "date e dettagli"], "teal", "softTeal")}
  ${card(1215, 575, 280, 130, "Output", ["email, orale", "diario errori"], "bordeaux", "softRed")}
  ${note(250, 795, 1100, "Obiettivo: scegliere forme corrette e comunicare senza errori evitabili.")}
`
  return shell("Inglese concorsuale essenziale", "Dalla lettura del bando alle risposte brevi, corrette e verificabili.", inner)
}

function figureCloze() {
  const inner = `
  <rect class="card" x="95" y="175" width="1410" height="220" rx="30"/>
  <text class="navy label" x="800" y="230" text-anchor="middle">Esempio guida</text>
  ${phraseBox(175, 275, 520, "She ___ here since 2021.", palette.navy)}
  ${mini(765, 275, 220, "since", "segnale di durata", palette.bordeaux)}
  ${phraseBox(1060, 275, 330, "has worked", palette.green)}
  <path class="arrowBordeaux" d="M705 315 L750 315"/>
  <path class="arrowGreen" d="M995 315 L1045 315"/>
  <rect class="card" x="95" y="455" width="1410" height="270" rx="30"/>
  ${stepCard(130, 510, ["1", "Leggi tutto", "non solo il vuoto"], 205)}
  ${stepCard(365, 510, ["2", "Trova soggetto", "chi compie l'azione"], 205)}
  ${stepCard(600, 510, ["3", "Cerca segnali", "since, yesterday"], 205)}
  ${stepCard(835, 510, ["4", "Classifica", "tempo o lessico"], 205)}
  ${stepCard(1070, 510, ["5", "Scarta", "opzioni impossibili"], 205)}
  ${stepCard(1305, 510, ["6", "Rileggi", "frase completa"], 205)}
  ${note(250, 795, 1100, "Regola pratica: prima il contesto, poi la grammatica, infine le opzioni.")}
`
  return shell("Cloze: risolvere la frase prima delle opzioni", "Il completamento premia segnali grammaticali, collocazioni e scarto dei distrattori.", inner)
}

function figureTempi() {
  const inner = `
  <rect class="card" x="95" y="180" width="1410" height="560" rx="30"/>
  <text class="navy label" x="800" y="238" text-anchor="middle">Scegli il tempo dal segnale, non dalla traduzione italiana</text>
  ${card(145, 305, 360, 125, "Present simple", ["routine, regole", "every day, usually"], "navy", "softBlue")}
  ${card(620, 305, 360, 125, "Past simple", ["passato concluso", "yesterday, last year"], "bordeaux", "softRed")}
  ${card(1095, 305, 360, 125, "Present perfect", ["passato + presente", "since, for, already"], "green", "softGreen")}
  ${card(145, 530, 360, 125, "Future forms", ["will, going to", "tomorrow, soon"], "gold", "softGold")}
  ${card(620, 530, 360, 125, "Passive voice", ["be + participio", "document focus"], "teal", "softTeal")}
  ${card(1095, 530, 360, 125, "Conditionals", ["if + forma", "ipotesi e conseguenze"], "navy", "softBlue")}
  ${note(240, 795, 1120, "Controllo finale: soggetto, tempo, ausiliare e forma del verbo devono combaciare.")}
`
  return shell("Tempi verbali e segnali", "Nei quiz la scelta corretta nasce dal tempo indicato dalla frase.", inner)
}

function figureAusiliari() {
  const inner = `
  <rect class="card" x="95" y="185" width="1410" height="555" rx="30"/>
  <text class="navy label" x="800" y="240" text-anchor="middle">L'ausiliare regge la struttura della frase</text>
  ${card(150, 315, 295, 130, "Be", ["stato", "progressivo, passivo"], "navy", "softBlue")}
  ${card(500, 315, 295, 130, "Do", ["domande", "negazioni semplici"], "bordeaux", "softRed")}
  ${card(850, 315, 295, 130, "Have", ["tempi perfetti", "azione collegata"], "green", "softGreen")}
  ${card(1200, 315, 295, 130, "Modali", ["can, must, should", "verbo base"], "gold", "softGold")}
  <path class="arrowNavy" d="M455 380 L485 380"/>
  <path class="arrowBordeaux" d="M805 380 L835 380"/>
  <path class="arrowGreen" d="M1155 380 L1185 380"/>
  ${mini(225, 570, 300, "Is she available?", "Yes, she is.", palette.navy)}
  ${mini(650, 570, 300, "Does she work?", "Yes, she does.", palette.bordeaux)}
  ${mini(1075, 570, 300, "Must send", "non must to send", palette.green)}
  ${note(245, 795, 1110, "Trappola classica: con does il verbo principale torna alla forma base.")}
`
  return shell("Be, do, have e modali", "Domande, negazioni, tempi composti e obblighi dipendono dall'ausiliare.", inner)
}

function figureLessico() {
  const inner = `
  <rect class="card" x="85" y="185" width="1430" height="565" rx="30"/>
  <text class="navy label" x="800" y="240" text-anchor="middle">Studia parole e preposizioni in coppie operative</text>
  ${listCard(130, 310, 310, "Tempo e luogo", ["at 9 a.m.", "on Monday", "in 2026", "by 30 June"], "navy", "softBlue")}
  ${listCard(470, 310, 310, "Collocazioni", ["apply for", "interested in", "responsible for", "according to"], "bordeaux", "softRed")}
  ${listCard(810, 310, 310, "Lessico PA", ["application", "deadline", "receipt", "public office"], "green", "softGreen")}
  ${listCard(1150, 310, 310, "False friends", ["actual = reale", "library = biblioteca", "eventually = alla fine", "sensible = ragionevole"], "gold", "softGold")}
  ${note(250, 795, 1100, "Nel dubbio, scegli il significato coerente con ufficio, procedura, scadenza o servizio.")}
`
  return shell("Preposizioni, lessico PA e false friends", "Nei cloze contano collocazioni, contesto amministrativo e falsi amici.", inner)
}

function figureComunicazione() {
  const inner = `
  <rect class="card" x="90" y="185" width="1420" height="565" rx="30"/>
  <text class="navy label" x="800" y="240" text-anchor="middle">Comprendere e rispondere: tre output ricorrenti</text>
  ${card(145, 320, 370, 145, "Reading", ["leggi domanda", "cerca date e keyword", "rispondi dal testo"], "navy", "softBlue")}
  ${card(615, 320, 370, 145, "Email", ["saluto", "motivo e richiesta", "thanks + regards"], "bordeaux", "softRed")}
  ${card(1085, 320, 370, 145, "Orale", ["frase semplice", "chiedi di ripetere", "risposta breve"], "green", "softGreen")}
  <path class="arrowNavy" d="M525 392 L600 392"/>
  <path class="arrowBordeaux" d="M995 392 L1070 392"/>
  ${phraseBox(160, 570, 360, "From Tuesday morning.", palette.navy)}
  ${phraseBox(620, 570, 360, "Could you confirm...?", palette.bordeaux)}
  ${phraseBox(1080, 570, 360, "I would like to...", palette.green)}
  ${note(250, 795, 1100, "Meglio una frase breve e corretta che una frase lunga con errori strutturali.")}
`
  return shell("Reading, email e orale", "La prova valuta comprensione essenziale e comunicazione breve, ordinata, cortese.", inner)
}

function figureRipasso() {
  const inner = `
  <rect class="card" x="90" y="185" width="1420" height="600" rx="30"/>
  <text class="navy label" x="800" y="240" text-anchor="middle">Da priorita a simulazione: non ripassare tutto allo stesso modo</text>
  ${card(135, 315, 280, 130, "3 giorni", ["tempi + cloze", "preposizioni + reading"], "bordeaux", "softRed")}
  ${card(490, 315, 280, 130, "7 giorni", ["bando, grammatica", "lessico e simulazione"], "navy", "softBlue")}
  ${card(845, 315, 280, 130, "30 giorni", ["alternanza settimanale", "quiz e correzione"], "green", "softGreen")}
  ${card(1200, 315, 280, 130, "Output", ["30 quiz", "2 reading, 10 frasi"], "gold", "softGold")}
  <path class="arrowBordeaux" d="M425 380 L475 380"/>
  <path class="arrowNavy" d="M780 380 L830 380"/>
  <path class="arrowGreen" d="M1135 380 L1185 380"/>
  ${listCard(230, 555, 500, "Diario errori", ["tempo verbale", "preposizione", "articolo o pronome", "lessico o distrazione"], "navy", "softBlue")}
  ${listCard(870, 555, 500, "Correzione utile", ["categoria", "frase corretta", "regola breve", "ripasso mirato"], "green", "softGreen")}
  ${note(250, 795, 1100, "Scrivere solo 'inglese sbagliato' non basta: serve la categoria dell'errore.")}
`
  return shell("Piano di ripasso e diario errori", "Pochi giorni richiedono priorita, simulazione e correzione per categoria.", inner)
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleY = y + 42
  const titleFontSize = title.length > 22 ? 19 : title.length > 17 ? 21 : title.length > 13 ? 23 : 25
  const bodyFontSize = lines.some((line) => line.length > 25) ? 17 : 18
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 25}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${titleY}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function listCard(x, y, w, title, lines, colorClass, boxClass) {
  const rowHeight = 34
  const h = 92 + lines.length * rowHeight
  const titleFontSize = title.length > 22 ? 19 : title.length > 16 ? 21 : 24
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 32}" y="${y + 82 + index * rowHeight}" style="font-size:18px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 44}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 24} ${y + 64} L${x + w - 24} ${y + 64}"/>
    ${body}
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 20 ? 18 : title.length > 15 ? 19 : 21
  const bodyFontSize = body.length > 22 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 32}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function phraseBox(x, y, w, text, color) {
  const fontSize = text.length > 28 ? 22 : text.length > 22 ? 24 : 27

  return `<g data-safe-box="${x} ${y} ${w} 84 8">
    <rect x="${x}" y="${y}" width="${w}" height="84" rx="22" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 53}" text-anchor="middle" fill="#FFFFFF" style="font-size:${fontSize}px">${esc(text)}</text>
  </g>`
}

function stepCard(x, y, [number, title, subtitle], w) {
  const center = x + w / 2
  const titleFontSize = title.length > 15 ? 17 : 19
  const subtitleFontSize = subtitle.length > 20 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 150 8">
    <rect class="card" x="${x}" y="${y}" width="${w}" height="150" rx="20"/>
    <circle cx="${center}" cy="${y + 35}" r="23" fill="${palette.gold}"/>
    <text class="ink label" x="${center}" y="${y + 44}" text-anchor="middle" style="font-size:22px">${esc(number)}</text>
    <text class="navy label" x="${center}" y="${y + 87}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${center}" y="${y + 119}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 94 ? 18 : text.length > 80 ? 19 : 20

  return `<g data-safe-box="${x} ${y} ${w} 64 8">
    <rect class="note" x="${x}" y="${y}" width="${w}" height="64" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-weight:800;font-size:${fontSize}px">${esc(text)}</text>
  </g>`
}

function connector(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
