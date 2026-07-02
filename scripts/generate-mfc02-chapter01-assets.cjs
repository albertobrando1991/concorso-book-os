const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "moduli",
  "m-fc02-agenzie-fiscali",
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
    slug: "01-mappa-bando-agenzie-fiscali",
    title: "Mappa BANDO delle Agenzie fiscali",
    subtitle: "Dal bando al sottopercorso: ente, profilo, materie e prova reale.",
    svg: figureMappaBando()
  },
  {
    slug: "02-perimetro-mfc02-dentro-fuori",
    title: "Perimetro M-FC02: dentro, fuori, con cautela",
    subtitle: "Il modulo guida solo quando il baricentro del bando e fiscale.",
    svg: figurePerimetro()
  },
  {
    slug: "03-tre-porte-ae-adm-ader",
    title: "Le tre porte di ingresso: AE, ADM, AdER",
    subtitle: "Stesso mondo fiscale, funzioni concorsuali diverse.",
    svg: figureTrePorte()
  },
  {
    slug: "04-nucleo-comune-delta-fiscale",
    title: "Nucleo comune + delta fiscale",
    subtitle: "La base generale diventa utile solo quando incontra la funzione fiscale.",
    svg: figureCoreDelta()
  },
  {
    slug: "05-bando-decoder-fiscale",
    title: "Bando Decoder fiscale",
    subtitle: "Una scheda prima del piano: classificare, pesare, decidere.",
    svg: figureDecoder()
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
      const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 })
      const encoded = Buffer.from(figure.svg, "utf8").toString("base64")
      await page.setContent(
        `<html><body style="margin:0;background:${palette.bg}"><img src="data:image/svg+xml;base64,${encoded}" width="1600" height="1000"></body></html>`,
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
  return `# Asset M-FC02 Capitolo 1

Figure generate per \`Mappa delle Agenzie fiscali e dei profili concorsuali\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-agenzie-fiscali.png\` | Mappa BANDO di apertura per leggere ente, profilo, nuclei fiscali, rischi e output. |
| \`02-perimetro-mfc02-dentro-fuori.png\` | Tavola di perimetro per distinguere dentro, fuori e casi con cautela. |
| \`03-tre-porte-ae-adm-ader.png\` | Confronto tra Agenzia delle Entrate, ADM e AdER. |
| \`04-nucleo-comune-delta-fiscale.png\` | Formula operativa: nucleo comune + delta fiscale + prova. |
| \`05-bando-decoder-fiscale.png\` | Scheda minima del Bando Decoder fiscale prima del piano di studio. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="690" rx="30"/>
  ${wideCard(505, 205, 590, "Bando fiscale", ["ente, codice profilo, prove", "materie comuni e specialistiche"], "navy", "softBlue")}
  <path class="line" d="M800 340 L800 405"/>
  <path class="line" d="M205 405 L1395 405"/>
  ${connector(205, 405, 205, 500)}
  ${connector(505, 405, 505, 620)}
  ${connector(800, 405, 800, 500)}
  ${connector(1095, 405, 1095, 620)}
  ${connector(1395, 405, 1395, 500)}
  ${stepBox(70, 500, 270, "B - Bando", ["AE, ADM, AdER", "profilo concreto"], "navy", "softBlue")}
  ${stepBox(370, 620, 270, "A - Aree", ["nucleo comune", "delta fiscale"], "bordeaux", "softRed")}
  ${stepBox(665, 500, 270, "N - Nuclei", ["tributi, dogane", "riscossione"], "gold", "softGold")}
  ${stepBox(960, 620, 270, "D - Diario", ["rischi di perimetro", "errori ricorrenti"], "green", "softGreen")}
  ${stepBox(1260, 500, 270, "O - Output", ["piano, quiz", "casi e orale"], "teal", "softTeal")}
  ${note(250, 805, 1100, "Obiettivo: scegliere il sottopercorso giusto prima di accumulare materiali.")}`

  return shell(
    "Mappa BANDO delle Agenzie fiscali",
    "Dal bando al sottopercorso: ente, profilo, materie e prova reale.",
    inner
  )
}

function figurePerimetro() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="690" rx="30"/>
  ${column(120, 250, 380, "Dentro M-FC02", ["AE tributario", "AE territorio / SPI", "ADM dogane, accise", "ADM giochi, monopoli", "AdER riscossione"], "green", "softGreen")}
  ${column(610, 250, 380, "Con cautela", ["gestionale o RU AE", "materia fiscale secondaria", "profilo misto", "contesto fiscale", "programma da pesare"], "gold", "softGold")}
  ${column(1100, 250, 380, "Fuori perimetro", ["ICT, AI, cybersecurity", "gare e appalti", "tecnico puro", "EPNE non fiscali", "ministeriale generale"], "bordeaux", "softRed")}
  <path class="arrowGreen" d="M500 510 L595 510"/>
  <path class="arrowGold" d="M990 510 L1085 510"/>
  ${note(255, 790, 1090, "La domanda decisiva non e il nome dell'ente, ma la funzione richiesta dal profilo.")}`

  return shell(
    "Perimetro M-FC02: dentro, fuori, con cautela",
    "Il modulo guida solo quando il baricentro del bando e fiscale.",
    inner
  )
}

function figureTrePorte() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="690" rx="30"/>
  ${doorCard(125, 245, "AE", "Agenzia delle Entrate", ["tributi", "servizi fiscali", "accertamento", "catasto e SPI"], "navy", "softBlue")}
  ${doorCard(610, 245, "ADM", "Dogane e Monopoli", ["dogane", "accise", "giochi", "controlli su flussi"], "bordeaux", "softRed")}
  ${doorCard(1095, 245, "AdER", "Entrate-Riscossione", ["cartelle", "pagamenti", "rateizzazioni", "front-office"], "teal", "softTeal")}
  <path class="thin" d="M220 690 L1380 690"/>
  ${miniTag(210, 735, "linguaggio")}
  ${miniTag(470, 735, "procedura")}
  ${miniTag(730, 735, "utente")}
  ${miniTag(990, 735, "controllo")}
  ${miniTag(1250, 735, "output")}
  ${note(295, 820, 1010, "Le tre porte condividono il nucleo pubblico, ma non le stesse priorita di studio.")}`

  return shell(
    "Le tre porte di ingresso: AE, ADM, AdER",
    "Stesso mondo fiscale, funzioni concorsuali diverse.",
    inner
  )
}

function figureCoreDelta() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="690" rx="30"/>
  ${formulaBox(130, 275, 360, "Nucleo comune", ["amministrativo", "pubblico impiego", "trasparenza", "privacy", "inglese e digitale"], "navy", "softBlue")}
  ${plus(555, 455)}
  ${formulaBox(620, 275, 360, "Delta fiscale", ["tributi", "accertamento", "dogane", "riscossione", "catasto"], "bordeaux", "softRed")}
  ${plus(1045, 455)}
  ${formulaBox(1110, 275, 360, "Prova reale", ["quiz", "orale", "caso", "front-office", "simulazione"], "green", "softGreen")}
  <path class="arrowNavy" d="M800 650 L800 710"/>
  ${wideCard(455, 710, 690, "Preparazione utilizzabile", ["risposta meno generica", "priorita coerenti con il profilo"], "gold", "softGold")}`

  return shell(
    "Nucleo comune + delta fiscale",
    "La base generale diventa utile solo quando incontra la funzione fiscale.",
    inner
  )
}

function figureDecoder() {
  const rows = [
    ["Ente", "AE / ADM / AdER"],
    ["Profilo", "codice e famiglia"],
    ["Prove", "quiz, scritto, orale, caso"],
    ["Materie", "comuni + M-FC02"],
    ["Rinvii", "digitale, appalti, tecnico"],
    ["Rischio", "perimetro o materia killer"],
    ["Output", "piano, diario, simulazione"]
  ]
  const body = rows.map((row, index) => tableRow(180, 265 + index * 64, 1240, row[0], row[1], index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="690" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Compila la scheda prima di scegliere materiali e calendario</text>
  <rect class="softBlue" x="180" y="250" width="1240" height="470" rx="24"/>
  ${body}
  ${note(260, 790, 1080, "Se non sai compilare il Decoder, non sei ancora pronto a costruire il piano.")}`

  return shell(
    "Bando Decoder fiscale",
    "Una scheda prima del piano: classificare, pesare, decidere.",
    inner
  )
}

function shell(title, subtitle, inner) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000" role="img" aria-labelledby="title desc">
  <title id="title">${escapeXml(title)}</title>
  <desc id="desc">${escapeXml(subtitle)}</desc>
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
      .title { font-size: 43px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-size: 22px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 25px; font-weight: 800; letter-spacing: 0; }
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
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
      .arrowGreen { stroke: ${palette.green}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGreen); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/></marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.green}"/></marker>
  </defs>
  <rect class="bg" width="1600" height="1000"/>
  <text class="ink title" x="800" y="72" text-anchor="middle">${escapeXml(title)}</text>
  <text class="muted subtitle" x="800" y="114" text-anchor="middle">${escapeXml(subtitle)}</text>
${inner}
</svg>
`
}

function wideCard(x, y, w, title, lines, color, fill) {
  return `
  <g data-safe-box="${x} ${y} ${w} 135 8">
    <rect class="${fill}" x="${x}" y="${y}" width="${w}" height="135" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 45}" text-anchor="middle">${escapeXml(title)}</text>
    ${textLines(x + w / 2, y + 78, lines, "muted small", "middle", 27)}
  </g>`
}

function stepBox(x, y, w, title, lines, color, fill) {
  return `
  <g data-safe-box="${x} ${y} ${w} 135 8">
    <rect class="${fill}" x="${x}" y="${y}" width="${w}" height="135" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 43}" text-anchor="middle" style="font-size:23px">${escapeXml(title)}</text>
    ${textLines(x + w / 2, y + 76, lines, "muted small", "middle", 25)}
  </g>`
}

function column(x, y, w, title, lines, color, fill) {
  return `
  <g data-safe-box="${x} ${y} ${w} 460 8">
    <rect class="${fill}" x="${x}" y="${y}" width="${w}" height="460" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="12" rx="6" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 56}" text-anchor="middle">${escapeXml(title)}</text>
    <path class="thin" d="M${x + 42} ${y + 86} L${x + w - 42} ${y + 86}"/>
    ${lines.map((line, index) => bulletLine(x + 62, y + 135 + index * 55, line)).join("\n")}
  </g>`
}

function doorCard(x, y, code, title, lines, color, fill) {
  return `
  <g data-safe-box="${x} ${y} 380 410 8">
    <rect class="${fill}" x="${x}" y="${y}" width="380" height="410" rx="30"/>
    <rect x="${x}" y="${y}" width="380" height="12" rx="6" fill="${palette[color]}"/>
    <circle cx="${x + 190}" cy="${y + 85}" r="52" fill="${palette[color]}"/>
    <text class="label" x="${x + 190}" y="${y + 96}" text-anchor="middle" fill="#FFFFFF" style="font-size:34px">${escapeXml(code)}</text>
    <text class="${color} label" x="${x + 190}" y="${y + 166}" text-anchor="middle" style="font-size:22px">${escapeXml(title)}</text>
    <path class="thin" d="M${x + 50} ${y + 192} L${x + 330} ${y + 192}"/>
    ${lines.map((line, index) => bulletLine(x + 72, y + 238 + index * 42, line)).join("\n")}
  </g>`
}

function formulaBox(x, y, w, title, lines, color, fill) {
  return `
  <g data-safe-box="${x} ${y} ${w} 360 8">
    <rect class="${fill}" x="${x}" y="${y}" width="${w}" height="360" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" style="font-size:24px">${escapeXml(title)}</text>
    <path class="thin" d="M${x + 38} ${y + 86} L${x + w - 38} ${y + 86}"/>
    ${textLines(x + w / 2, y + 125, lines, "muted small", "middle", 43)}
  </g>`
}

function tableRow(x, y, w, left, right, index) {
  const fill = index % 2 === 0 ? "#FFFFFF" : "#F8FAFC"
  return `
  <g data-safe-box="${x} ${y} ${w} 52 4">
    <rect x="${x}" y="${y}" width="${w}" height="52" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <text class="navy label" x="${x + 42}" y="${y + 34}" style="font-size:20px">${escapeXml(left)}</text>
    <text class="muted body" x="${x + 330}" y="${y + 34}" style="font-size:20px">${escapeXml(right)}</text>
  </g>`
}

function note(x, y, w, text) {
  return `
  <g data-safe-box="${x} ${y} ${w} 66 8">
    <rect class="note" x="${x}" y="${y}" width="${w}" height="66" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 41}" text-anchor="middle" style="font-weight:800;font-size:20px">${escapeXml(text)}</text>
  </g>`
}

function miniTag(x, y, text) {
  return `
  <g data-safe-box="${x - 78} ${y - 26} 156 52 4">
    <rect class="softGold" x="${x - 78}" y="${y - 26}" width="156" height="52" rx="22"/>
    <text class="gold label" x="${x}" y="${y + 8}" text-anchor="middle" style="font-size:19px">${escapeXml(text)}</text>
  </g>`
}

function plus(x, y) {
  return `
  <g data-safe-box="${x - 30} ${y - 30} 60 60 2">
    <circle cx="${x}" cy="${y}" r="28" fill="${palette.gold}"/>
    <text class="label" x="${x}" y="${y + 9}" text-anchor="middle" fill="#FFFFFF" style="font-size:32px">+</text>
  </g>`
}

function connector(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function bulletLine(x, y, text) {
  return `<circle cx="${x}" cy="${y - 6}" r="5" fill="${palette.gold}"/><text class="muted small" x="${x + 20}" y="${y}" style="font-size:19px">${escapeXml(text)}</text>`
}

function textLines(x, y, lines, cls, anchor = "middle", step = 26) {
  return lines.map((line, index) =>
    `<text class="${cls}" x="${x}" y="${y + index * step}" text-anchor="${anchor}">${escapeXml(line)}</text>`
  ).join("\n")
}

function escapeXml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exitCode = 1
})
