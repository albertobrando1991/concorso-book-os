const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-32"
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
    slug: "01-mappa-bando-sistema-personale",
    title: "Mappa BANDO del sistema personale",
    subtitle: "Il metodo funziona quando lo ripeti davanti a ogni nuovo bando.",
    description: "Mappa BANDO del sistema personale: Decoder, matrice, nuclei, Diario e output.",
    svg: figureMappaBando()
  },
  {
    slug: "02-cinque-pagine-vive",
    title: "Le cinque pagine vive",
    subtitle: "Non devi mantenere vivo tutto il libro: devi mantenere vivo il sistema.",
    description: "Schema delle cinque pagine vive: Decoder, matrice, piano, Diario e archivio capitale.",
    svg: figurePagineVive()
  },
  {
    slug: "03-protocollo-15-30-60",
    title: "Protocollo 15/30/60",
    subtitle: "La manutenzione deve essere breve, altrimenti diventa un lavoro parallelo.",
    description: "Protocollo di revisione settimanale, post-evento e strategica in 15, 30 e 60 minuti.",
    svg: figureProtocollo()
  },
  {
    slug: "04-cruscotto-personale",
    title: "Cruscotto BANDO personale",
    subtitle: "Il cruscotto toglie decisioni dalla testa e le mette in dati visibili.",
    description: "Cruscotto personale per bandi, prove, output, errori, fonti, capitale ed energia.",
    svg: figureCruscotto()
  },
  {
    slug: "05-mantieni-aggiorna-archivia",
    title: "Mantieni, aggiorna, archivia",
    subtitle: "Ogni materiale deve avere un destino operativo.",
    description: "Regola per decidere se mantenere, aggiornare o archiviare materiali e appunti.",
    svg: figureDestini()
  },
  {
    slug: "06-chiusura-dopo-prova",
    title: "Chiudere il sistema dopo una prova",
    subtitle: "Il risultato senza revisione produce memoria emotiva; con revisione produce capitale.",
    description: "Quattro passaggi per chiudere ogni prova: salva documenti, scheda, Diario/capitale, prossima mossa.",
    svg: figureDopoProva()
  },
  {
    slug: "07-nuovo-bando-apri-metodo",
    title: "Nuovo bando: apri prima il metodo",
    subtitle: "Il bando viene prima di manuali, corsi, quiz e strumenti.",
    description: "Sequenza per aprire un nuovo bando senza ricominciare da zero.",
    svg: figureNuovoBando()
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

  return `# Asset Capitolo 32

Figure generate per \`Il tuo sistema BANDO personale\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const items = [
    ["B", "Bando", "Decoder", palette.navy, palette.blueSoft],
    ["A", "Aree", "matrice", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "capitale", palette.gold, palette.goldSoft],
    ["D", "Diario", "errori", palette.green, palette.greenSoft],
    ["O", "Output", "prove reali", palette.teal, palette.tealSoft]
  ]
  const steps = items
    .map(([letter, title, body, color, fill], index) =>
      stepBox(105 + index * 290, 370, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 290, 485, 395 + index * 290, 485)).join("\n")

  return shell(
    "Mappa BANDO del sistema personale",
    "Il metodo funziona quando lo ripeti davanti a ogni nuovo bando.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(430, 215, 740, "Sistema ripetibile", ["non ricominciare da zero", "riapri la catena BANDO"], palette.navy, palette.blueSoft)}
    ${steps}
    ${arrows}
    ${note(245, 810, 1110, "Quando ti senti perso, non cercare un nuovo metodo: torna alla catena.")}
    `
  )
}

function figurePagineVive() {
  const pages = [
    ["Decoder", "ogni nuovo bando"],
    ["Matrice", "confronto concorsi"],
    ["Piano", "ogni settimana"],
    ["Diario", "quiz e prove"],
    ["Archivio", "chiusura concorso"]
  ]

  return shell(
    "Le cinque pagine vive",
    "Non devi mantenere vivo tutto il libro: devi mantenere vivo il sistema.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${pages.map((page, index) => livePage(125 + index * 285, 340, page, index)).join("\n")}
    ${wideCard(455, 640, 690, "Segnale di controllo", ["se queste pagine sono ferme", "il sistema sta perdendo controllo"], palette.bordeaux, palette.redSoft)}
    ${note(245, 810, 1110, "Cinque pagine vive valgono piu di cento file accumulati e mai riaperti.")}
    `
  )
}

function figureProtocollo() {
  const cards = [
    ["15", "fine settimana", ["piano", "output", "priorita"], palette.green, palette.greenSoft],
    ["30", "dopo evento", ["Decoder", "Diario", "decisione"], palette.navy, palette.blueSoft],
    ["60", "fine mese", ["portafoglio", "materiali", "sostenibilita"], palette.gold, palette.goldSoft]
  ]

  return shell(
    "Protocollo 15/30/60",
    "La manutenzione deve essere breve, altrimenti diventa un lavoro parallelo.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${cards.map((card, index) => protocolCard(140 + index * 465, 285, card)).join("\n")}
    ${arrow(505, 455, 605, 455)}
    ${arrow(970, 455, 1070, 455)}
    ${note(245, 810, 1110, "Non usare 60 minuti per ogni quiz sbagliato, ne' 15 minuti per un nuovo bando importante.")}
    `
  )
}

function figureCruscotto() {
  const cells = [
    ["Bandi", "aperti"],
    ["Prove", "calendario"],
    ["Output", "prodotti"],
    ["Errori", "ricorrenti"],
    ["Fonti", "da controllare"],
    ["Capitale", "riutilizzabile"],
    ["Energia", "sostenibilita"],
    ["Decisione", "settimana"]
  ]

  return shell(
    "Cruscotto BANDO personale",
    "Il cruscotto toglie decisioni dalla testa e le mette in dati visibili.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${dashboardGrid(215, 245, cells)}
    ${wideCard(455, 655, 690, "Regola", ["se il cruscotto e' vuoto", "mancano dati, non motivazione"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "Quando non sai cosa fare, leggi il cruscotto e scegli la prossima azione verificabile.")}
    `
  )
}

function figureDestini() {
  const cards = [
    ["Mantieni", ["corretto", "breve", "riusabile"], palette.green, palette.greenSoft],
    ["Aggiorna", ["utile", "incompleto", "superato"], palette.gold, palette.goldSoft],
    ["Archivia", ["duplicato", "passivo", "senza output"], palette.bordeaux, palette.redSoft]
  ]

  return shell(
    "Mantieni, aggiorna, archivia",
    "Ogni materiale deve avere un destino operativo.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${cards.map((card, index) => destinyCard(145 + index * 485, 305, card)).join("\n")}
    ${arrow(525, 465, 625, 465)}
    ${arrow(1010, 465, 1110, 465)}
    ${wideCard(455, 660, 690, "Capitale vero", ["puoi riaprirlo tra un mese", "e usarlo senza ricostruire tutto"], palette.teal, palette.tealSoft)}
    ${note(245, 810, 1110, "La cartella piena non e' capitale: il capitale e' cio che torna utile alla prova.")}
    `
  )
}

function figureDopoProva() {
  const items = [
    ["1", "Salva", "esiti e documenti"],
    ["2", "Scheda", "post-prova"],
    ["3", "Aggiorna", "Diario e capitale"],
    ["4", "Decidi", "prossima mossa"]
  ]

  return shell(
    "Chiudere il sistema dopo una prova",
    "Il risultato senza revisione produce memoria emotiva; con revisione produce capitale.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${items.map((item, index) => closureStep(145 + index * 345, 340, item, index)).join("\n")}
    ${[0, 1, 2].map((index) => arrow(425 + index * 345, 455, 490 + index * 345, 455)).join("\n")}
    ${wideCard(455, 655, 690, "Chiusura vera", ["ogni prova termina con dati", "non solo con una sensazione"], palette.green, palette.greenSoft)}
    ${note(245, 810, 1110, "Non importa se e' andata bene o male: se non estrai capitale, perdi informazione.")}
    `
  )
}

function figureNuovoBando() {
  const steps = [
    ["Leggi", "requisiti"],
    ["Decoder", "bando"],
    ["Matrice", "confronto"],
    ["Capitale", "riuso"],
    ["Moduli", "mancanti"],
    ["Piano", "settimana"],
    ["Output", "prova"]
  ]

  return shell(
    "Nuovo bando: apri prima il metodo",
    "Il bando viene prima di manuali, corsi, quiz e strumenti.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${steps.map((step, index) => smallStep(95 + index * 205, 365, step, index)).join("\n")}
    ${[0, 1, 2, 3, 4, 5].map((index) => arrow(265 + index * 205, 455, 300 + index * 205, 455)).join("\n")}
    ${wideCard(455, 635, 690, "Solo dopo", ["scegli libri, corsi, quiz e strumenti", "il materiale segue il bando"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "Il sistema non elimina la lettura del bando: la rende piu veloce e piu precisa.")}
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

function livePage(x, y, [title, when], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.bordeaux, palette.redSoft],
    [palette.gold, palette.goldSoft],
    [palette.green, palette.greenSoft],
    [palette.teal, palette.tealSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 240 230 8">
    <rect x="${x}" y="${y}" width="240" height="230" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <path d="M${x + 52} ${y + 38} H${x + 188} V${y + 150} H${x + 52} Z" fill="${palette.white}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 120}" y="${y + 92}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 120}" y="${y + 185}" text-anchor="middle">${escapeXml(when)}</text>
  </g>`
}

function protocolCard(x, y, [minutes, when, lines, color, fill]) {
  const rendered = lines
    .map((line, index) => `<text class="small strong" x="${x + 180}" y="${y + 190 + index * 36}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 360 350 8">
    <rect x="${x}" y="${y}" width="360" height="350" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 180}" cy="${y + 74}" r="48" fill="${color}"/>
    <text class="label whiteText" x="${x + 180}" y="${y + 84}" text-anchor="middle">${escapeXml(minutes)}</text>
    <text class="label" style="fill:${color}" x="${x + 180}" y="${y + 150}" text-anchor="middle">${escapeXml(when)}</text>
    ${rendered}
  </g>`
}

function dashboardGrid(x, y, cells) {
  return cells
    .map(([title, body], index) => {
      const col = index % 4
      const row = Math.floor(index / 4)
      const cardX = x + col * 295
      const cardY = y + row * 160
      const colors = [
        [palette.navy, palette.blueSoft],
        [palette.green, palette.greenSoft],
        [palette.gold, palette.goldSoft],
        [palette.teal, palette.tealSoft],
        [palette.bordeaux, palette.redSoft],
        [palette.violet, palette.violetSoft]
      ]
      const [color, fill] = colors[index % colors.length]

      return `<g data-safe-box="${cardX} ${cardY} 260 130 8">
        <rect x="${cardX}" y="${cardY}" width="260" height="130" rx="22" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <text class="label" style="fill:${color}" x="${cardX + 130}" y="${cardY + 52}" text-anchor="middle">${escapeXml(title)}</text>
        <text class="small strong" x="${cardX + 130}" y="${cardY + 92}" text-anchor="middle">${escapeXml(body)}</text>
      </g>`
    })
    .join("\n")
}

function destinyCard(x, y, [title, lines, color, fill]) {
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

function closureStep(x, y, [number, title, body], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.green, palette.greenSoft],
    [palette.gold, palette.goldSoft],
    [palette.teal, palette.tealSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 280 250 8">
    <rect x="${x}" y="${y}" width="280" height="250" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 140}" cy="${y + 58}" r="36" fill="${color}"/>
    <text class="label whiteText" x="${x + 140}" y="${y + 67}" text-anchor="middle">${escapeXml(number)}</text>
    <text class="label" style="fill:${color}" x="${x + 140}" y="${y + 130}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 140}" y="${y + 182}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function smallStep(x, y, [title, body], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.green, palette.greenSoft],
    [palette.gold, palette.goldSoft],
    [palette.teal, palette.tealSoft],
    [palette.bordeaux, palette.redSoft],
    [palette.violet, palette.violetSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 170 185 8">
    <rect x="${x}" y="${y}" width="170" height="185" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 85}" cy="${y + 48}" r="27" fill="${color}"/>
    <text class="small strong whiteText" x="${x + 85}" y="${y + 55}" text-anchor="middle">${index + 1}</text>
    <text class="small strong" style="fill:${color}" x="${x + 85}" y="${y + 105}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 85}" y="${y + 145}" text-anchor="middle">${escapeXml(body)}</text>
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
