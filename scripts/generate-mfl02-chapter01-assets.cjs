const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "moduli",
  "m-fl02-regioni-province-citta-metropolitane",
  "assets",
  "chapter-01"
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
  white: "#FFFFFF",
  cream: "#FFF7ED",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5"
}

const figures = [
  {
    slug: "01-mappa-bando-sistema-multilivello",
    title: "Mappa BANDO del sistema multilivello",
    subtitle: "Dal bando al livello competente, fino ad atto, controllo e output.",
    svg: figureMappaBando()
  },
  {
    slug: "02-architettura-stato-regione-area-vasta-comune",
    title: "Architettura territoriale multilivello",
    subtitle: "Stato, Regione, area vasta e Comune non sono una gerarchia semplice.",
    svg: figureArchitettura()
  },
  {
    slug: "03-sussidiarieta-differenziazione-adeguatezza",
    title: "Tre principi per allocare le funzioni",
    subtitle: "Sussidiarieta, differenziazione e adeguatezza decidono la scala.",
    svg: figurePrincipi()
  },
  {
    slug: "04-catena-avviso-regionale-comuni",
    title: "Catena di un avviso regionale",
    subtitle: "Programma, avviso, beneficiario, attuazione, rendicontazione e monitoraggio.",
    svg: figureCatenaAvviso()
  },
  {
    slug: "05-area-vasta-funzione-atto",
    title: "Area vasta: funzione, ente e atto",
    subtitle: "Province e Citta metropolitane governano funzioni sovracomunali.",
    svg: figureAreaVasta()
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
      const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1 })
      const encoded = Buffer.from(figure.svg, "utf8").toString("base64")
      await page.setContent(
        `<html><body style="margin:0;background:${palette.bg}"><img src="data:image/svg+xml;base64,${encoded}" width="1600" height="900"></body></html>`,
        { waitUntil: "load" }
      )
      await page.locator("img").screenshot({ path: path.join(OUTPUT_DIR, `${figure.slug}.png`) })
      await page.close()
    }
  } finally {
    await browser.close()
  }

  await fs.writeFile(path.join(OUTPUT_DIR, "README.md"), renderReadme(), "utf8")
}

function renderReadme() {
  return `# Asset Capitolo 1 - M-FL02 Sistema territoriale multilivello

Figure generate per \`Il sistema territoriale multilivello\`.

## Analisi stile libro base

La ricognizione delle immagini gia presenti nei capitoli del libro base e nei moduli illustrati mostra una grammatica editoriale costante:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview, dashboard e PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- immagini didattiche, non decorative: mappe BANDO, flussi, confronti, matrici e sintesi anti-errore;
- testi interni brevi, card a raggio contenuto, frecce leggere, nessuna fotografia stock e nessuna ornamentazione autonoma;
- inserimento subito dopo il blocco di testo che l'immagine traduce in schema.

Per questo capitolo sono opportune 5 figure: coprono apertura BANDO, architettura territoriale, principi di allocazione, catena Regione-Comuni e funzione di area vasta.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-sistema-multilivello.png\` | \`01-mappa-bando-sistema-multilivello.svg\` | Mappa BANDO di apertura: ente, area, nucleo, diario e output del sistema multilivello. |
| \`02-architettura-stato-regione-area-vasta-comune.png\` | \`02-architettura-stato-regione-area-vasta-comune.svg\` | Schema dei livelli Stato, Regione, area vasta e Comune senza gerarchia impropria. |
| \`03-sussidiarieta-differenziazione-adeguatezza.png\` | \`03-sussidiarieta-differenziazione-adeguatezza.svg\` | Tavola dei tre principi come criterio di allocazione delle funzioni. |
| \`04-catena-avviso-regionale-comuni.png\` | \`04-catena-avviso-regionale-comuni.svg\` | Flusso di un avviso regionale rivolto ai Comuni, da programma a monitoraggio. |
| \`05-area-vasta-funzione-atto.png\` | \`05-area-vasta-funzione-atto.svg\` | Anti-confusione su Province e Citta metropolitane come enti di area vasta. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${node(585, 205, 430, 116, "Bando territoriale", ["ente, profilo", "materie e prova"], "navy", "softBlue")}
  <path class="line" d="M800 321 L800 372"/>
  <path class="line" d="M205 372 L1395 372"/>
  ${line(205, 372, 205, 455)}
  ${line(505, 372, 505, 580)}
  ${line(800, 372, 800, 455)}
  ${line(1095, 372, 1095, 580)}
  ${line(1395, 372, 1395, 455)}
  ${node(70, 455, 270, 130, "B - Bando", ["Regione", "Provincia, Citta metro"], "navy", "softBlue")}
  ${node(370, 580, 270, 130, "A - Aree", ["ordinamento", "fondi, territorio"], "bordeaux", "softRed")}
  ${node(665, 455, 270, 130, "N - Nuclei", ["competenza", "funzione, atto"], "gold", "softGold")}
  ${node(960, 580, 270, 130, "D - Diario", ["livelli confusi", "Province abolite"], "green", "softGreen")}
  ${node(1260, 455, 270, 130, "O - Output", ["mappa livello", "caso e orale"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Prima domanda: quale livello istituzionale rende corretta la risposta?")}
`

  return shell(
    "Mappa BANDO del sistema multilivello",
    "Dal bando al livello competente, fino ad atto, controllo e output.",
    inner
  )
}

function figureArchitettura() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${tier(155, 230, 1290, "Stato", ["unita dell'ordinamento", "principi, livelli essenziali, cornice nazionale"], "navy", "softBlue")}
  ${tier(210, 350, 1180, "Regione", ["legislazione, programmazione, coordinamento", "finanziamenti, atti, controlli"], "bordeaux", "softRed")}
  ${tier(265, 470, 1070, "Area vasta", ["Province e Citta metropolitane", "viabilita, scuole, pianificazione, rete territoriale"], "gold", "softGold")}
  ${tier(320, 590, 960, "Comune", ["prossimita, sportello, servizi", "attuazione locale e rapporto con cittadini e imprese"], "green", "softGreen")}
  ${note(260, 815, 1080, "Autonomia e coordinamento: il rapporto istituzionale non e una scala gerarchica lineare.")}
`

  return shell(
    "Architettura territoriale multilivello",
    "Stato, Regione, area vasta e Comune non sono una gerarchia semplice.",
    inner
  )
}

function figurePrincipi() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${principle(120, 245, "Sussidiarieta", "Vicino, se efficace", ["livello piu prossimo", "servizio al cittadino", "ma senza automatismi"], "navy", "softBlue")}
  ${principle(555, 245, "Differenziazione", "Territori diversi", ["piccoli Comuni", "aree metropolitane", "zone interne"], "bordeaux", "softRed")}
  ${principle(990, 245, "Adeguatezza", "Scala e mezzi", ["competenze", "risorse", "coordinamento"], "green", "softGreen")}
  <path class="arrowGold" d="M800 585 L800 665"/>
  ${wide(410, 665, 780, "Funzione allocata al livello coerente", ["Comune, Regione, Provincia o Citta metropolitana", "in base a problema, territorio e capacita amministrativa"], "gold", "softGold")}
  ${note(245, 815, 1110, "In prova non basta definire i principi: devi usarli per scegliere la scala della funzione.")}
`

  return shell(
    "Tre principi per allocare le funzioni",
    "Sussidiarieta, differenziazione e adeguatezza decidono la scala.",
    inner
  )
}

function figureCatenaAvviso() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(100, 255, "1", "Programma", ["obiettivi", "risorse"], "navy", "softBlue")}
  ${arrow(285, 335, 365, 335, "Navy")}
  ${step(390, 255, "2", "Avviso", ["requisiti", "criteri"], "bordeaux", "softRed")}
  ${arrow(575, 335, 655, 335, "Bordeaux")}
  ${step(680, 255, "3", "Domanda", ["Comune", "progetto"], "gold", "softGold")}
  ${arrow(865, 335, 945, 335, "Gold")}
  ${step(970, 255, "4", "Istruttoria", ["ammissibile", "graduatoria"], "green", "softGreen")}
  ${arrow(1155, 335, 1235, 335, "Green")}
  ${step(1260, 255, "5", "Concessione", ["atto", "obblighi"], "teal", "softTeal")}
  <path class="line" d="M1360 455 C1360 540 240 540 240 625"/>
  ${step(100, 625, "6", "Attuazione", ["affidamenti", "spesa"], "navy", "softBlue")}
  ${arrow(285, 705, 420, 705, "Navy")}
  ${wide(445, 625, 710, "Rendicontazione e controllo", ["documenti, pagamenti, tracciabilita", "revoca o recupero se emergono irregolarita"], "bordeaux", "softRed")}
  ${arrow(1180, 705, 1315, 705, "Bordeaux")}
  ${step(1340, 625, "7", "Monitoraggio", ["dati", "indicatori"], "green", "softGreen")}
`

  return shell(
    "Catena di un avviso regionale",
    "Programma, avviso, beneficiario, attuazione, rendicontazione e monitoraggio.",
    inner
  )
}

function figureAreaVasta() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${areaCard(115, 245, "Provincia", ["viabilita", "edilizia scolastica", "pianificazione", "assistenza ai Comuni"], "navy", "softBlue")}
  ${areaCard(610, 245, "Citta metropolitana", ["piano strategico", "mobilita", "infrastrutture", "servizi di scala urbana"], "bordeaux", "softRed")}
  ${areaCard(1105, 245, "Comune", ["prossimita", "sportello", "servizi locali", "attuazione sul territorio"], "green", "softGreen")}
  ${wide(315, 650, 970, "Anti-errore", ["Provincia e Citta metropolitana non sono uffici residuali", "e la Citta metropolitana non coincide con il solo Comune capoluogo"], "gold", "softGold")}
  ${note(245, 815, 1110, "La parola chiave e area vasta: funzione sovracomunale, scala territoriale, atto coerente.")}
`

  return shell(
    "Area vasta: funzione, ente e atto",
    "Province e Citta metropolitane governano funzioni sovracomunali.",
    inner
  )
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
      .title { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 43px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 22px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: 0; }
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
      .arrowTeal { stroke: ${palette.teal}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowTeal); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
    <marker id="arrowBordeaux" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.bordeaux}"/></marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/></marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.green}"/></marker>
    <marker id="arrowTeal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.teal}"/></marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="108" text-anchor="middle">${esc(subtitle)}</text>
${inner}
</svg>
`
}

function node(x, y, w, h, title, lines, color, fillClass) {
  return safe(x, y, w, h, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 73, 25, "muted small", 18)}
  `)
}

function tier(x, y, w, title, lines, color, fillClass) {
  return safe(x, y, w, 94, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="94" rx="24"/>
    <rect x="${x}" y="${y}" width="12" height="94" rx="6" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 46}" y="${y + 39}" text-anchor="start" style="font-size:24px">${esc(title)}</text>
    <text class="ink body" x="${x + 255}" y="${y + 36}" text-anchor="start" style="font-weight:800;font-size:19px">${esc(lines[0])}</text>
    <text class="muted small" x="${x + 255}" y="${y + 65}" text-anchor="start" style="font-size:18px">${esc(lines[1])}</text>
  `)
}

function principle(x, y, title, subtitle, lines, color, fillClass) {
  return safe(x, y, 365, 330, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="365" height="330" rx="28"/>
    <rect x="${x}" y="${y}" width="365" height="12" rx="6" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 182.5}" y="${y + 57}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    <text class="ink small" x="${x + 182.5}" y="${y + 96}" text-anchor="middle" style="font-weight:800;font-size:18px">${esc(subtitle)}</text>
    <path class="thin" d="M${x + 55} ${y + 126} L${x + 310} ${y + 126}"/>
    ${bulletLines(lines, x + 70, y + 175, 43)}
  `)
}

function step(x, y, num, title, lines, color, fillClass) {
  return safe(x, y, 185, 160, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="185" height="160" rx="24"/>
    <circle cx="${x + 42}" cy="${y + 44}" r="25" fill="${palette[color]}"/>
    <text x="${x + 42}" y="${y + 53}" text-anchor="middle" style="fill:#fff;font-family:'Source Sans 3','Segoe UI',Arial,sans-serif;font-size:24px;font-weight:900">${esc(num)}</text>
    <text class="${color} label" x="${x + 92}" y="${y + 48}" text-anchor="middle" style="font-size:17px">${esc(title)}</text>
    ${textLines(lines, x + 92, y + 92, 28, "muted small", 17)}
  `)
}

function areaCard(x, y, title, lines, color, fillClass) {
  return safe(x, y, 380, 330, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="380" height="330" rx="28"/>
    <rect x="${x}" y="${y}" width="380" height="12" rx="6" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 190}" y="${y + 60}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    <path class="thin" d="M${x + 62} ${y + 92} L${x + 318} ${y + 92}"/>
    ${bulletLines(lines, x + 70, y + 140, 42)}
  `)
}

function wide(x, y, w, title, lines, color, fillClass) {
  return safe(x, y, w, 110, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="110" rx="26"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 72, 24, "muted small", 17)}
  `)
}

function note(x, y, w, text) {
  return safe(x, y, w, 62, `
    <rect class="note" x="${x}" y="${y}" width="${w}" height="62" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 39}" text-anchor="middle" style="font-weight:800;font-size:20px">${esc(text)}</text>
  `)
}

function arrow(x1, y1, x2, y2, color) {
  return `<path class="arrow${color}" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function line(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function safe(x, y, w, h, inner) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 10">${inner}</g>`
}

function textLines(lines, x, y, gap, className, size) {
  return lines
    .map((line, index) => `<text class="${className}" x="${x}" y="${y + index * gap}" text-anchor="middle" style="font-size:${size}px">${esc(line)}</text>`)
    .join("\n")
}

function bulletLines(lines, x, y, gap) {
  return lines
    .map((text, index) => {
      const lineY = y + index * gap
      return `<circle cx="${x}" cy="${lineY - 7}" r="6" fill="${palette.gold}"/><text class="ink body" x="${x + 22}" y="${lineY}" style="font-size:18px">${esc(text)}</text>`
    })
    .join("\n")
}

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
