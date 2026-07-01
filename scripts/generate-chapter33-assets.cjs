const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-33"
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
  violet: "#5B3B82",
  white: "#FFFFFF",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5",
  violetSoft: "#EFEAF7",
  cream: "#FFF7ED"
}

const figures = [
  {
    slug: "01-mappa-bando-materiali",
    title: "Mappa BANDO dei materiali",
    subtitle: "Ogni materiale deve servire bando, piano, errori e output.",
    description: "Mappa BANDO per collocare manuali, corsi, banche dati e strumenti nel metodo.",
    svg: figureMappaBando()
  },
  {
    slug: "02-prima-bando-poi-materiale",
    title: "Prima il bando, poi il materiale",
    subtitle: "Se parti dal manuale, il materiale comanda il piano.",
    description: "Sequenza corretta: bando, Decoder, priorita, materiali, piano e output.",
    svg: figureBandoPoiMateriale()
  },
  {
    slug: "03-pila-minima-studio",
    title: "La pila minima di studio",
    subtitle: "Non serve una biblioteca: serve una pila governabile.",
    description: "Strati essenziali: fonti ufficiali, base ordinata, allenamento, modulo specialistico, Diario e capitale.",
    svg: figurePilaMinima()
  },
  {
    slug: "04-scorecard-materiali",
    title: "Scorecard dei materiali",
    subtitle: "Prima di acquistare o mantenere, verifica i criteri centrali.",
    description: "Scorecard per valutare allineamento, aggiornamento, tracciabilita, formato, correzione e riuso.",
    svg: figureScorecard()
  },
  {
    slug: "05-funzione-rischio-materiali",
    title: "Materiali: funzione e rischio",
    subtitle: "Manuale, corso, quiz, dispense e AI servono solo se producono output.",
    description: "Schema funzione-rischio per manuali, corsi, banche dati, dispense e AI.",
    svg: figureFunzioneRischio()
  },
  {
    slug: "06-banca-dati-ufficiale-non-ufficiale",
    title: "Banca dati ufficiale o allenamento",
    subtitle: "Una banca dati ufficiale cambia il piano; una non ufficiale allena.",
    description: "Distinzione operativa tra banca dati ufficiale e banca dati non ufficiale.",
    svg: figureBancaDati()
  },
  {
    slug: "07-decisione-materiali",
    title: "Decisione finale sui materiali",
    subtitle: "Tieni, integra o archivia in base a bando, output ed errori.",
    description: "Flusso per decidere se tenere, integrare o archiviare un materiale.",
    svg: figureDecisioneMateriali()
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

  return `# Asset Capitolo 33

Figure generate per \`Manuali, corsi e banche dati: scegliere senza disperdersi\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const items = [
    ["B", "Bando", "elimina rumore", palette.navy, palette.blueSoft],
    ["A", "Aree", "comune e profilo", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "priorita", palette.gold, palette.goldSoft],
    ["D", "Diario", "errori reali", palette.green, palette.greenSoft],
    ["O", "Output", "quiz, casi, orale", palette.teal, palette.tealSoft]
  ]
  const steps = items
    .map(([letter, title, body, color, fill], index) =>
      stepBox(105 + index * 290, 370, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 290, 485, 395 + index * 290, 485)).join("\n")

  return shell(
    "Mappa BANDO dei materiali",
    "Ogni materiale deve servire bando, piano, errori e output.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(430, 215, 740, "Materiale governato", ["entra nel metodo solo se ha una funzione", "e produce un output verificabile"], palette.navy, palette.blueSoft)}
    ${steps}
    ${arrows}
    ${note(245, 810, 1110, "Un materiale che non sai collocare nella catena BANDO non e' ancora pronto per il piano.")}
    `
  )
}

function figureBandoPoiMateriale() {
  const steps = [
    ["Bando", "materie e prove"],
    ["Decoder", "dati reali"],
    ["Priorita", "cosa conta"],
    ["Materiali", "solo dove serve"],
    ["Piano", "tempo e output"],
    ["Prova", "risultato allenato"]
  ]

  return shell(
    "Prima il bando, poi il materiale",
    "Se parti dal manuale, il materiale comanda il piano.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${steps.map((step, index) => processStep(110 + index * 240, 350, step, index)).join("\n")}
    ${[0, 1, 2, 3, 4].map((index) => arrow(315 + index * 240, 455, 350 + index * 240, 455)).join("\n")}
    ${wideCard(430, 640, 740, "Regola pratica", ["il piano comanda il materiale", "non il contrario"], palette.green, palette.greenSoft)}
    ${note(245, 810, 1110, "Prima del Decoder fai solo ricognizione leggera: la scelta arriva dopo i dati del bando.")}
    `
  )
}

function figurePilaMinima() {
  const layers = [
    ["Fonti ufficiali", "bando, avvisi, norme"],
    ["Base ordinata", "manuale principale"],
    ["Allenamento", "quiz, casi, orale"],
    ["Modulo profilo", "cio che cambia"],
    ["Diario e capitale", "errori e riuso"]
  ]

  return shell(
    "La pila minima di studio",
    "Non serve una biblioteca: serve una pila governabile.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${stackLayers(340, 240, layers)}
    ${sideRule(1020, 315, "Aggiungi solo se", ["copre una lacuna", "produce output", "entra nel piano"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "Una pila minima ben usata batte una libreria parallela che non sai governare.")}
    `
  )
}

function figureScorecard() {
  const criteria = [
    ["Allineamento", "bando"],
    ["Aggiornamento", "data"],
    ["Tracciabilita", "fonti"],
    ["Formato", "prova"],
    ["Correzione", "errori"],
    ["Riuso", "capitale"]
  ]

  return shell(
    "Scorecard dei materiali",
    "Prima di acquistare o mantenere, verifica i criteri centrali.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${scoreGrid(165, 250, criteria)}
    ${wideCard(455, 645, 690, "Segnale di stop", ["se fallisce due o tre criteri centrali", "non e' un affare: e' distrazione"], palette.bordeaux, palette.redSoft)}
    ${note(245, 810, 1110, "La scorecard trasforma l'acquisto emotivo in decisione di metodo.")}
    `
  )
}

function figureFunzioneRischio() {
  const rows = [
    ["Manuale", "struttura", "quattro paralleli"],
    ["Corso", "percorso", "dipendenza passiva"],
    ["Quiz", "allenamento", "senza ragionamento"],
    ["Dispense", "ripasso", "origine incerta"],
    ["AI", "trasforma", "fonte autonoma"]
  ]

  return shell(
    "Materiali: funzione e rischio",
    "Manuale, corso, quiz, dispense e AI servono solo se producono output.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${riskRows(185, 245, rows)}
    ${sideRule(1040, 325, "Filtro", ["serve al bando?", "corregge errori?", "produce output?"], palette.green, palette.greenSoft)}
    ${note(245, 810, 1110, "Ogni strumento utile ha anche un rischio: il metodo decide quando usarlo.")}
    `
  )
}

function figureBancaDati() {
  return shell(
    "Banca dati ufficiale o allenamento",
    "Una banca dati ufficiale cambia il piano; una non ufficiale allena.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${listPanel(145, 285, "Ufficiale", ["procedura", "copertura completa", "errori e ritorno", "simulazione finale"], palette.navy, palette.blueSoft)}
    ${listPanel(835, 285, "Non ufficiale", ["allenamento", "distrattori", "tempo", "richiamo"], palette.teal, palette.tealSoft)}
    ${arrow(600, 455, 735, 455)}
    ${wideCard(455, 655, 690, "Decisione", ["se e' ufficiale, entra nel piano", "se non lo e', resta strumento di allenamento"], palette.gold, palette.goldSoft)}
    ${note(245, 810, 1110, "Il programma lo decide il bando, non una banca dati non ufficiale.")}
    `
  )
}

function figureDecisioneMateriali() {
  const cards = [
    ["Tieni", ["allineato", "aggiornato", "produce output"], palette.green, palette.greenSoft],
    ["Integra", ["utile", "manca un pezzo", "entra nel piano"], palette.gold, palette.goldSoft],
    ["Archivia", ["duplica", "non produce", "distrae"], palette.bordeaux, palette.redSoft]
  ]

  return shell(
    "Decisione finale sui materiali",
    "Tieni, integra o archivia in base a bando, output ed errori.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${cards.map((card, index) => decisionCard(145 + index * 485, 305, card)).join("\n")}
    ${arrow(525, 465, 625, 465)}
    ${arrow(1010, 465, 1110, 465)}
    ${wideCard(455, 660, 690, "Domanda finale", ["quale decisione del piano rende possibile?", "se nessuna, aspetta o archivia"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "Il candidato forte non possiede piu materiali: sa quali comandano la prossima settimana.")}
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
    .title { font: 800 43px Arial, sans-serif; fill: ${palette.ink}; }
    .subtitle { font: 400 21px Arial, sans-serif; fill: ${palette.muted}; }
    .label { font: 800 25px Arial, sans-serif; fill: ${palette.ink}; }
    .body { font: 400 19px Arial, sans-serif; fill: ${palette.ink}; }
    .small { font: 400 16px Arial, sans-serif; fill: ${palette.ink}; }
    .strong { font-weight: 800; }
    .whiteText { fill: ${palette.white}; }
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

function stepBox(x, y, letter, title, body, color, fill) {
  return `<g data-safe-box="${x} ${y} 245 210 8">
    <rect x="${x}" y="${y}" width="245" height="210" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 122.5}" cy="${y + 52}" r="32" fill="${color}"/>
    <text class="label whiteText" x="${x + 122.5}" y="${y + 61}" text-anchor="middle">${escapeXml(letter)}</text>
    <text class="label" x="${x + 122.5}" y="${y + 116}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 122.5}" y="${y + 158}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function processStep(x, y, [title, body], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.green, palette.greenSoft],
    [palette.gold, palette.goldSoft],
    [palette.teal, palette.tealSoft],
    [palette.bordeaux, palette.redSoft],
    [palette.violet, palette.violetSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 205 210 8">
    <rect x="${x}" y="${y}" width="205" height="210" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 102.5}" cy="${y + 55}" r="30" fill="${color}"/>
    <text class="label whiteText" x="${x + 102.5}" y="${y + 64}" text-anchor="middle">${index + 1}</text>
    <text class="small strong" style="fill:${color}" x="${x + 102.5}" y="${y + 118}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 102.5}" y="${y + 160}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function stackLayers(x, y, layers) {
  return layers
    .map(([title, body], index) => {
      const width = 680 - index * 62
      const layerX = x + index * 31
      const layerY = y + index * 82
      const colors = [
        [palette.navy, palette.blueSoft],
        [palette.green, palette.greenSoft],
        [palette.gold, palette.goldSoft],
        [palette.teal, palette.tealSoft],
        [palette.bordeaux, palette.redSoft]
      ]
      const [color, fill] = colors[index]

      return `<g data-safe-box="${layerX} ${layerY} ${width} 70 6">
        <rect x="${layerX}" y="${layerY}" width="${width}" height="70" rx="20" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <text class="small strong" style="fill:${color}" x="${layerX + width / 2 - 130}" y="${layerY + 43}" text-anchor="middle">${escapeXml(title)}</text>
        <text class="small" x="${layerX + width / 2 + 140}" y="${layerY + 43}" text-anchor="middle">${escapeXml(body)}</text>
      </g>`
    })
    .join("\n")
}

function scoreGrid(x, y, criteria) {
  return criteria
    .map(([title, body], index) => {
      const col = index % 3
      const row = Math.floor(index / 3)
      const cardX = x + col * 420
      const cardY = y + row * 160
      const colors = [
        [palette.navy, palette.blueSoft],
        [palette.green, palette.greenSoft],
        [palette.gold, palette.goldSoft],
        [palette.teal, palette.tealSoft],
        [palette.bordeaux, palette.redSoft],
        [palette.violet, palette.violetSoft]
      ]
      const [color, fill] = colors[index]

      return `<g data-safe-box="${cardX} ${cardY} 360 130 8">
        <rect x="${cardX}" y="${cardY}" width="360" height="130" rx="22" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <text class="label" style="fill:${color}" x="${cardX + 180}" y="${cardY + 52}" text-anchor="middle">${escapeXml(title)}</text>
        <text class="small strong" x="${cardX + 180}" y="${cardY + 92}" text-anchor="middle">${escapeXml(body)}</text>
      </g>`
    })
    .join("\n")
}

function riskRows(x, y, rows) {
  return rows
    .map(([tool, functionText, risk], index) => {
      const rowY = y + index * 88
      const colors = [
        [palette.navy, palette.blueSoft],
        [palette.green, palette.greenSoft],
        [palette.gold, palette.goldSoft],
        [palette.teal, palette.tealSoft],
        [palette.bordeaux, palette.redSoft]
      ]
      const [color, fill] = colors[index]

      return `<g data-safe-box="${x} ${rowY} 760 70 6">
        <rect x="${x}" y="${rowY}" width="760" height="70" rx="20" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <text class="small strong" style="fill:${color}" x="${x + 130}" y="${rowY + 43}" text-anchor="middle">${escapeXml(tool)}</text>
        <text class="small" x="${x + 370}" y="${rowY + 43}" text-anchor="middle">${escapeXml(functionText)}</text>
        <text class="small strong" x="${x + 620}" y="${rowY + 43}" text-anchor="middle">${escapeXml(risk)}</text>
      </g>`
    })
    .join("\n")
}

function listPanel(x, y, title, items, color, fill) {
  const lines = items
    .map((item, index) => `<text class="small strong" x="${x + 240}" y="${y + 132 + index * 42}" text-anchor="middle">${escapeXml(item)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 480 340 8">
    <rect x="${x}" y="${y}" width="480" height="340" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="480" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 240}" y="${y + 72}" text-anchor="middle">${escapeXml(title)}</text>
    ${lines}
  </g>`
}

function decisionCard(x, y, [title, lines, color, fill]) {
  const rendered = lines
    .map((line, index) => `<text class="small strong" x="${x + 195}" y="${y + 150 + index * 42}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 390 310 8">
    <rect x="${x}" y="${y}" width="390" height="310" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="390" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 195}" y="${y + 78}" text-anchor="middle">${escapeXml(title)}</text>
    ${rendered}
  </g>`
}

function sideRule(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 190}" y="${y + 98 + index * 34}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 380 250 8">
    <rect x="${x}" y="${y}" width="380" height="250" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 190}" y="${y + 56}" text-anchor="middle">${escapeXml(title)}</text>
    ${rendered}
  </g>`
}

function note(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 66 8">
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
