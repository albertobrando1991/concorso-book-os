const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-26"
)

const palette = {
  bg: "#F8FAFC",
  ink: "#0F172A",
  muted: "#526174",
  border: "#CBD5E1",
  navy: "#10233F",
  bordeaux: "#7A2430",
  gold: "#D4AF37",
  green: "#2F7D5A",
  teal: "#1F6F78",
  red: "#A33A3A",
  white: "#FFFFFF",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5",
  cream: "#FFF7ED"
}

const figures = [
  {
    slug: "01-mappa-bando-capitale",
    title: "Mappa BANDO del capitale di studio",
    subtitle: "Ogni concorso lascia capitale solo se produce strumenti riusabili.",
    description: "Mappa in cinque passaggi: bando, aree, nuclei, diario e output diventano prodotti da conservare.",
    svg: figureMappaBandoCapitale()
  },
  {
    slug: "02-deposito-vs-capitale",
    title: "Deposito o capitale?",
    subtitle: "Conservare tutto non crea vantaggio: crea solo peso da gestire.",
    description: "Confronto tra accumulo disordinato e materiale verificato, sintetico e riusabile.",
    svg: figureDepositoVsCapitale()
  },
  {
    slug: "03-regola-3c",
    title: "Regola 3C piu taglio",
    subtitle: "Conserva, correggi, converti; poi elimina cio che non produce output.",
    description: "Griglia decisionale per decidere cosa fare con appunti, schemi, errori e simulazioni.",
    svg: figureRegola3C()
  },
  {
    slug: "04-archivio-minimo-cinque-cartelle",
    title: "Archivio minimo in cinque cartelle",
    subtitle: "Lo strumento puo cambiare; la struttura deve restare stabile.",
    description: "Cinque contenitori operativi: bandi, nucleo comune, moduli, output e diario.",
    svg: figureArchivioMinimo()
  },
  {
    slug: "05-protocollo-trenta-minuti",
    title: "Protocollo dei 30 minuti",
    subtitle: "Entro 48 ore dalla prova trasforma memoria fresca in dati utili.",
    description: "Timeline post-prova per registrare formato reale, errori, materiali utili, tagli e prossimo uso.",
    svg: figureProtocollo30()
  },
  {
    slug: "06-core-moduli-trasferibilita",
    title: "Core, moduli e trasferibilita",
    subtitle: "Il capitale comune accelera; il nuovo bando decide cosa adattare.",
    description: "Schema per separare nucleo comune, moduli di profilo e output quando cambia il concorso.",
    svg: figureCoreModuli()
  },
  {
    slug: "07-caso-elena-capitale-riuso",
    title: "Caso Elena: non ripartire da zero",
    subtitle: "Una prova non vinta puo diventare base operativa per il bando successivo.",
    description: "Flusso dal concorso comunale al concorso in unione di comuni attraverso capitale salvato.",
    svg: figureCasoElena()
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
  const rows = figures
    .map((figure) => `| \`${figure.slug}.png\` | ${figure.description} |`)
    .join("\n")

  return `# Asset Capitolo 26

Figure generate per \`Trasformare ogni concorso in capitale di studio\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBandoCapitale() {
  const items = [
    ["B", "Bando", "Decoder compilato", palette.navy, palette.blueSoft],
    ["A", "Aree", "core e moduli", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "schemi e domande", palette.gold, palette.goldSoft],
    ["D", "Diario", "errori e ripassi", palette.green, palette.greenSoft],
    ["O", "Output", "quiz, casi, orale", palette.teal, palette.tealSoft]
  ]
  const boxes = items
    .map(([letter, title, body, color, fill], index) =>
      verticalStep(115 + index * 285, 385, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 285, 505, 390 + index * 285, 505)).join("\n")

  return shell(
    "Mappa BANDO del capitale di studio",
    "Ogni concorso lascia capitale solo se produce strumenti riusabili.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(460, 195, 680, "Concorso concluso", ["non archiviare emozioni", "trasforma in prodotti riusabili"], palette.navy, palette.blueSoft)}
    ${boxes}
    ${arrows}
    ${wideCard(500, 640, 600, "Sistema trasferibile", ["base migliore per il prossimo bando"], palette.green, palette.greenSoft)}
    ${note(250, 812, 1100, "Se manca una parte della catena BANDO, il materiale resta fragile.")}
    `
  )
}

function figureDepositoVsCapitale() {
  return shell(
    "Deposito o capitale?",
    "Conservare tutto non crea vantaggio: crea solo peso da gestire.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${comparisonPanel(135, 240, "Deposito", ["PDF mai letti", "screenshot senza contesto", "appunti duplicati", "flashcard mai ripetute", "riassunti non verificati"], palette.bordeaux, palette.redSoft)}
    ${filterBox(650, 312)}
    ${comparisonPanel(985, 240, "Capitale", ["schemi corretti", "domande riusabili", "errori classificati", "casi svolti", "output datati e corretti"], palette.green, palette.greenSoft)}
    ${arrow(590, 450, 650, 450)}
    ${arrow(950, 450, 985, 450)}
    ${note(250, 812, 1100, "Il capitale di studio non e' cio che hai letto: e' cio che puoi riusare.")}
    `
  )
}

function figureRegola3C() {
  const cards = [
    ["Conserva", "corretto", "sintetico", "riusabile", palette.navy, palette.blueSoft],
    ["Correggi", "utile", "incompleto", "da chiarire", palette.bordeaux, palette.redSoft],
    ["Converti", "passivo", "in domanda", "o caso", palette.gold, palette.goldSoft],
    ["Elimina", "duplicato", "superato", "senza output", palette.green, palette.greenSoft]
  ]
  const columns = cards
    .map(([title, a, b, c, color, fill], index) => decisionColumn(130 + index * 350, 290, title, [a, b, c], color, fill))
    .join("\n")

  return shell(
    "Regola 3C piu taglio",
    "Conserva, correggi, converti; poi elimina cio che non produce output.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    <text class="label navy" x="800" y="225" text-anchor="middle">Ogni materiale deve ricevere una decisione, non solo una cartella</text>
    ${columns}
    ${note(250, 812, 1100, "Studiare meglio significa anche buttare via meglio.")}
    `
  )
}

function figureArchivioMinimo() {
  const folders = [
    ["1", "Bandi", "decoder, avvisi, date", palette.navy, palette.blueSoft],
    ["2", "Nucleo comune", "schemi ricorrenti", palette.bordeaux, palette.redSoft],
    ["3", "Moduli", "profili attivati", palette.gold, palette.goldSoft],
    ["4", "Output", "quiz, casi, orale", palette.green, palette.greenSoft],
    ["5", "Diario", "errori e azioni", palette.teal, palette.tealSoft]
  ]
  const cards = folders
    .map(([num, title, body, color, fill], index) => folderCard(135 + index * 270, 300, num, title, body, color, fill))
    .join("\n")

  return shell(
    "Archivio minimo in cinque cartelle",
    "Lo strumento puo cambiare; la struttura deve restare stabile.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    <text class="label navy" x="800" y="225" text-anchor="middle">Carta, cloud o app: conta la struttura, non lo strumento</text>
    ${cards}
    <g data-safe-box="340 590 920 110 10">
      <rect x="340" y="590" width="920" height="110" rx="22" fill="${palette.cream}" stroke="#EFC58D" stroke-width="3"/>
      <text class="body strong" x="800" y="635" text-anchor="middle">Tre etichette rapide: core, modulo, solo questo bando</text>
      <text class="small muted" x="800" y="675" text-anchor="middle">Servono a non trattare tutto come se fosse trasferibile</text>
    </g>
    ${note(250, 812, 1100, "Un archivio utile alleggerisce le decisioni del concorso successivo.")}
    `
  )
}

function figureProtocollo30() {
  const steps = [
    ["0-5", "Formato reale", "scrivi a memoria"],
    ["5-10", "Mappa prova", "materie e domande"],
    ["10-15", "Tre errori", "diario operativo"],
    ["15-20", "Tre materiali", "core o modulo"],
    ["20-25", "Taglio", "pulizia mirata"],
    ["25-30", "Prossimo uso", "piano successivo"]
  ]
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.bordeaux, palette.redSoft],
    [palette.gold, palette.goldSoft],
    [palette.green, palette.greenSoft],
    [palette.teal, palette.tealSoft],
    [palette.navy, palette.blueSoft]
  ]
  const cards = steps
    .map(([time, title, body], index) => timeStep(145 + index * 220, 430, time, title, body, colors[index][0], colors[index][1]))
    .join("\n")
  const arrows = [0, 1, 2, 3, 4].map((index) => arrow(330 + index * 220, 545, 365 + index * 220, 545)).join("\n")

  return shell(
    "Protocollo dei 30 minuti",
    "Entro 48 ore dalla prova trasforma memoria fresca in dati utili.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(480, 210, 640, "Dopo la prova", ["prima che restino solo emozioni"], palette.navy, palette.blueSoft)}
    ${cards}
    ${arrows}
    ${note(250, 812, 1100, "Una prova analizzata bene puo evitare settimane di errori nel concorso successivo.")}
    `
  )
}

function figureCoreModuli() {
  return shell(
    "Core, moduli e trasferibilita",
    "Il capitale comune accelera; il nuovo bando decide cosa adattare.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${comparisonPanel(120, 260, "Core comune", ["Metodo BANDO", "amministrativo essenziale", "pubblico impiego", "trasparenza e privacy", "logica, inglese, prove"], palette.navy, palette.blueSoft)}
    ${wideCard(585, 355, 430, "Nuovo bando", ["verifica profilo", "prova e materie", "decide cosa adattare"], palette.gold, palette.goldSoft)}
    ${comparisonPanel(1060, 260, "Moduli profilo", ["enti locali", "contabilita", "tributario", "ICT, sanita, scuola", "vigilanza, tecnico, appalti"], palette.teal, palette.tealSoft)}
    ${arrow(535, 450, 585, 450)}
    ${arrow(1015, 450, 1060, 450)}
    ${note(250, 812, 1100, "Il capitale fa partire avanti, ma non sostituisce la lettura del bando.")}
    `
  )
}

function figureCasoElena() {
  return shell(
    "Caso Elena: non ripartire da zero",
    "Una prova non vinta puo diventare base operativa per il bando successivo.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${caseBox(120, 300, "Concorso comunale", ["decoder completo", "enti locali", "quiz corretti"], palette.bordeaux, palette.redSoft)}
    ${caseBox(620, 245, "Capitale salvato", ["schemi accesso", "25 errori", "6 orali", "3 casi"], palette.navy, palette.blueSoft)}
    ${caseBox(1080, 300, "Unione di comuni", ["riusa core", "riapre modulo", "simula entro 7 giorni"], palette.green, palette.greenSoft)}
    ${arrow(500, 450, 620, 450)}
    ${arrow(990, 450, 1080, 450)}
    <g data-safe-box="430 625 740 90 10">
      <rect x="430" y="625" width="740" height="90" rx="22" fill="${palette.cream}" stroke="#EFC58D" stroke-width="3"/>
      <text class="body strong" x="800" y="675" text-anchor="middle">Non ha gia vinto. Ma non riparte da zero.</text>
    </g>
    ${note(250, 812, 1100, "La differenza tra accumulare e crescere e' trasformare l'esperienza in metodo.")}
    `
  )
}

function shell(title, subtitle, body) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">${escapeXml(title)}</title>
  <desc id="desc">${escapeXml(subtitle)}</desc>
  <style>
    .bg { fill: ${palette.bg}; }
    .card { fill: ${palette.white}; stroke: ${palette.border}; stroke-width: 3; }
    .title { font: 800 44px Arial, sans-serif; fill: ${palette.ink}; }
    .subtitle { font: 400 22px Arial, sans-serif; fill: ${palette.muted}; }
    .label { font: 800 25px Arial, sans-serif; fill: ${palette.ink}; }
    .body { font: 400 19px Arial, sans-serif; fill: ${palette.ink}; }
    .small { font: 400 16px Arial, sans-serif; fill: ${palette.ink}; }
    .strong { font-weight: 800; }
    .muted { fill: ${palette.muted}; }
    .navy { fill: ${palette.navy}; }
    .line { stroke: ${palette.navy}; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; fill: none; }
  </style>
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M2,2 L10,6 L2,10 Z" fill="${palette.navy}"/>
    </marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <g data-safe-box="80 16 1440 118 0">
    <text class="title" x="800" y="68" text-anchor="middle">${escapeXml(title)}</text>
    <text class="subtitle" x="800" y="108" text-anchor="middle">${escapeXml(subtitle)}</text>
  </g>
  ${body}
</svg>
`
}

function wideCard(x, y, w, title, lines, color, fill) {
  const textLines = lines
    .map((line, index) => `<text class="small" x="${x + w / 2}" y="${y + 82 + index * 28}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 150 8">
    <rect x="${x}" y="${y}" width="${w}" height="150" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="${w}" height="12" rx="6" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 52}" text-anchor="middle">${escapeXml(title)}</text>
    ${textLines}
  </g>`
}

function verticalStep(x, y, letter, title, body, color, fill) {
  return `<g data-safe-box="${x} ${y} 240 205 14">
    <rect x="${x}" y="${y}" width="240" height="205" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 120}" cy="${y + 50}" r="32" fill="${color}"/>
    <text class="label" x="${x + 120}" y="${y + 59}" text-anchor="middle" fill="${palette.white}">${escapeXml(letter)}</text>
    <text class="label" x="${x + 120}" y="${y + 112}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 120}" y="${y + 152}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function comparisonPanel(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 200}" y="${y + 130 + index * 34}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 400 380 20">
    <rect x="${x}" y="${y}" width="400" height="380" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="400" height="14" rx="7" fill="${color}"/>
    <text class="label" x="${x + 200}" y="${y + 68}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <line x1="${x + 70}" y1="${y + 95}" x2="${x + 330}" y2="${y + 95}" stroke="${palette.border}" stroke-width="3"/>
    ${rendered}
  </g>`
}

function filterBox(x, y) {
  return `<g data-safe-box="${x} ${y} 300 275 18">
    <rect x="${x}" y="${y}" width="300" height="275" rx="28" fill="${palette.cream}" stroke="#EFC58D" stroke-width="3"/>
    <text class="label" x="${x + 150}" y="${y + 62}" text-anchor="middle">Filtro</text>
    <text class="small" x="${x + 150}" y="${y + 118}" text-anchor="middle">corretto?</text>
    <text class="small" x="${x + 150}" y="${y + 154}" text-anchor="middle">sintetico?</text>
    <text class="small" x="${x + 150}" y="${y + 190}" text-anchor="middle">collegato al bando?</text>
    <text class="small" x="${x + 150}" y="${y + 226}" text-anchor="middle">produce output?</text>
  </g>`
}

function decisionColumn(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 145}" y="${y + 188 + index * 38}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 290 340 18">
    <rect x="${x}" y="${y}" width="290" height="340" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 145}" cy="${y + 68}" r="42" fill="${color}"/>
    <text class="label" x="${x + 145}" y="${y + 76}" text-anchor="middle" fill="${palette.white}">${escapeXml(title[0])}</text>
    <text class="label" x="${x + 145}" y="${y + 142}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    ${rendered}
  </g>`
}

function folderCard(x, y, num, title, body, color, fill) {
  return `<g data-safe-box="${x} ${y} 230 235 4">
    <path d="M${x} ${y + 45} Q${x} ${y + 22} ${x + 24} ${y + 22} L${x + 92} ${y + 22} Q${x + 110} ${y + 22} ${x + 124} ${y + 45} L${x + 206} ${y + 45} Q${x + 230} ${y + 45} ${x + 230} ${y + 69} L${x + 230} ${y + 210} Q${x + 230} ${y + 235} ${x + 205} ${y + 235} L${x + 25} ${y + 235} Q${x} ${y + 235} ${x} ${y + 210} Z" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 54}" cy="${y + 86}" r="28" fill="${color}"/>
    <text class="small strong" x="${x + 54}" y="${y + 93}" text-anchor="middle" fill="${palette.white}">${escapeXml(num)}</text>
    <text class="label" x="${x + 115}" y="${y + 140}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <text class="small" x="${x + 115}" y="${y + 184}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function timeStep(x, y, time, title, body, color, fill) {
  return `<g data-safe-box="${x - 18} ${y - 40} 216 270 0">
    <rect x="${x}" y="${y}" width="180" height="230" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x + 30}" y="${y - 34}" width="120" height="68" rx="34" fill="${color}"/>
    <text class="small strong" x="${x + 90}" y="${y + 8}" text-anchor="middle" fill="${palette.white}">${escapeXml(time)}</text>
    <text class="body strong" x="${x + 90}" y="${y + 92}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <text class="small" x="${x + 90}" y="${y + 144}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function caseBox(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 180}" y="${y + 135 + index * 34}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 360 300 18">
    <rect x="${x}" y="${y}" width="360" height="300" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="360" height="14" rx="7" fill="${color}"/>
    <text class="label" x="${x + 180}" y="${y + 68}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <line x1="${x + 58}" y1="${y + 96}" x2="${x + 302}" y2="${y + 96}" stroke="${palette.border}" stroke-width="3"/>
    ${rendered}
  </g>`
}

function note(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 66 12">
    <rect x="${x}" y="${y}" width="${w}" height="66" rx="22" fill="${palette.cream}" stroke="#EFC58D" stroke-width="3"/>
    <text class="body strong" x="${x + w / 2}" y="${y + 43}" text-anchor="middle">${escapeXml(text)}</text>
  </g>`
}

function arrow(x1, y1, x2, y2) {
  return `<path class="line" marker-end="url(#arrow)" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function escapeXml(value) {
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
