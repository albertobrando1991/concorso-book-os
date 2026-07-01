const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-29"
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
    slug: "01-mappa-bando-sostenibilita",
    title: "Mappa BANDO della sostenibilita",
    subtitle: "Quando la pressione sale, non moltiplicare lo studio: torna alla catena BANDO.",
    description: "Mappa per leggere energia, ansia e continuita dentro le cinque fasi del Metodo BANDO.",
    svg: figureMappaBando()
  },
  {
    slug: "02-scala-energia-studio",
    title: "Energia alta, media, bassa, minima",
    subtitle: "Le ore non valgono tutte uguale: assegna il compito giusto all'energia reale.",
    description: "Scala operativa per decidere quali attivita fare in base al livello di energia disponibile.",
    svg: figureScalaEnergia()
  },
  {
    slug: "03-minimo-efficace",
    title: "Il minimo efficace",
    subtitle: "Nei giorni difficili basta mantenere vivo il filo del metodo.",
    description: "Schema dei micro-output che impediscono al piano di uscire dal sistema nei giorni difficili.",
    svg: figureMinimoEfficace()
  },
  {
    slug: "04-recuperare-senza-distruggere-piano",
    title: "Recuperare senza distruggere il piano",
    subtitle: "Il recupero corretto taglia, protegge output e aggiorna la settimana.",
    description: "Tre domande operative per recuperare ritardi senza moltiplicare ore irrealistiche.",
    svg: figureRecupero()
  },
  {
    slug: "05-ansia-in-procedura",
    title: "Ansia da prova: trasformarla in procedura",
    subtitle: "Il Diario distingue lacuna, fretta, disordine e routine mancante.",
    description: "Flusso per trasformare l'ansia in cause osservabili e azioni allenabili.",
    svg: figureAnsiaProcedura()
  },
  {
    slug: "06-semaforo-sovraccarico",
    title: "Semaforo del sovraccarico",
    subtitle: "Verde mantiene, giallo riduce, rosso taglia e protegge il sistema.",
    description: "Semaforo settimanale per decidere se mantenere, ridurre o ristrutturare il piano.",
    svg: figureSemaforo()
  },
  {
    slug: "07-caso-sara-piano-sostenibile",
    title: "Caso Sara: recuperare cio che conta",
    subtitle: "Una settimana difficile non deve distruggere l'intero piano.",
    description: "Caso guidato: dagli errori ricorrenti alla revisione sostenibile del piano.",
    svg: figureCasoSara()
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

  return `# Asset Capitolo 29

Figure generate per \`Reggere la preparazione: energia, ansia e continuita\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const items = [
    ["B", "Bando", "decoder e priorita", palette.navy, palette.blueSoft],
    ["A", "Aree", "una area alla volta", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "richiamo breve", palette.gold, palette.goldSoft],
    ["D", "Diario", "causa e azione", palette.green, palette.greenSoft],
    ["O", "Output", "prova minima", palette.teal, palette.tealSoft]
  ]
  const steps = items
    .map(([letter, title, body, color, fill], index) =>
      stepBox(105 + index * 290, 375, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 290, 490, 395 + index * 290, 490)).join("\n")

  return shell(
    "Mappa BANDO della sostenibilita",
    "Quando la pressione sale, non moltiplicare lo studio: torna alla catena BANDO.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(420, 215, 760, "Tenuta del sistema", ["energia, ansia e imprevisti non cambiano il metodo", "cambiano la dose e la priorita"], palette.navy, palette.blueSoft)}
    ${steps}
    ${arrows}
    ${note(250, 812, 1100, "La continuita nasce dal non perdere il filo, non dallo studiare sempre tanto.")}
    `
  )
}

function figureScalaEnergia() {
  const levels = [
    ["Alta", "simulazioni e casi", "non riordinare file", palette.navy, palette.blueSoft],
    ["Media", "quiz e ripasso", "non aprire tre materie", palette.green, palette.greenSoft],
    ["Bassa", "correzione errori", "non forzare studio profondo", palette.gold, palette.goldSoft],
    ["Minima", "una azione piccola", "non recuperare tutto", palette.bordeaux, palette.redSoft]
  ]
  const cards = levels.map((level, index) => energyCard(130 + index * 360, 285, level)).join("\n")

  return shell(
    "Energia alta, media, bassa, minima",
    "Le ore non valgono tutte uguale: assegna il compito giusto all'energia reale.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${cards}
    ${wideCard(455, 660, 690, "Regola pratica", ["ore migliori agli output difficili", "ore peggiori alla manutenzione del sistema"], palette.teal, palette.tealSoft)}
    ${note(250, 812, 1100, "Un calendario sostenibile prevede anche giornate basse.")}
    `
  )
}

function figureMinimoEfficace() {
  const items = [
    ["10 minuti", "Diario errori"],
    ["5 schede", "flashcard mirate"],
    ["1 risposta", "orale registrato"],
    ["10 quiz", "domande brevi"],
    ["1 scelta", "priorita domani"]
  ]
  const boxes = items.map((item, index) => miniBox(125 + index * 285, 375, item)).join("\n")

  return shell(
    "Il minimo efficace",
    "Nei giorni difficili basta mantenere vivo il filo del metodo.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(455, 220, 690, "Domanda giusta", ["qual e' il minimo che mantiene vivo il metodo?"], palette.navy, palette.blueSoft)}
    ${boxes}
    ${note(250, 812, 1100, "Il minimo efficace non sostituisce lo studio pieno: impedisce l'uscita dal sistema.")}
    `
  )
}

function figureRecupero() {
  const questions = [
    ["Essenziale?", "recupero solo il nucleo ad alta resa", palette.navy, palette.blueSoft],
    ["Tagliare?", "elimino duplicati e letture passive", palette.gold, palette.goldSoft],
    ["Proteggere?", "salvo quiz, caso, orale o simulazione", palette.green, palette.greenSoft]
  ]
  const cards = questions.map((item, index) => decisionCard(135 + index * 485, 305, item)).join("\n")

  return shell(
    "Recuperare senza distruggere il piano",
    "Il recupero corretto taglia, protegge output e aggiorna la settimana.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${cards}
    ${arrow(520, 465, 620, 465)}
    ${arrow(1005, 465, 1105, 465)}
    ${wideCard(485, 645, 630, "No al recupero punitivo", ["non trasformare tre ore perse in sei ore impossibili"], palette.bordeaux, palette.redSoft)}
    ${note(250, 812, 1100, "Se perdi due giorni, non fingi che nulla sia accaduto: aggiorni il piano.")}
    `
  )
}

function figureAnsiaProcedura() {
  return shell(
    "Ansia da prova: trasformarla in procedura",
    "Il Diario distingue lacuna, fretta, disordine e routine mancante.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(115, 340, 360, "Segnale", ["errore sotto pressione", "blocco o fretta"], palette.bordeaux, palette.redSoft)}
    ${wideCard(620, 250, 360, "Diario", ["non sapevo?", "ho letto male?", "ho perso ordine?"], palette.navy, palette.blueSoft)}
    ${wideCard(1125, 340, 360, "Azione", ["simulazione breve", "timer realistico", "routine consegne"], palette.green, palette.greenSoft)}
    ${arrow(475, 415, 620, 360)}
    ${arrow(980, 360, 1125, 415)}
    ${note(250, 812, 1100, "Se il disagio e' intenso o persistente, serve supporto qualificato.")}
    `
  )
}

function figureSemaforo() {
  const lights = [
    ["Verde", "studio e output procedono", "mantieni", palette.green, palette.greenSoft],
    ["Giallo", "ritardi ed errori aumentano", "riduci e proteggi", palette.gold, palette.goldSoft],
    ["Rosso", "piano irrealistico", "taglia e chiedi supporto", palette.bordeaux, palette.redSoft]
  ]
  const rows = lights.map((light, index) => trafficRow(240, 250 + index * 155, light)).join("\n")

  return shell(
    "Semaforo del sovraccarico",
    "Verde mantiene, giallo riduce, rosso taglia e protegge il sistema.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${rows}
    ${sideRule(1010, 330, "Decisione", ["il colore non giudica", "serve a scegliere il prossimo passo"], palette.navy, palette.blueSoft)}
    ${note(250, 812, 1100, "Il rosso non e' fallimento: e' un piano non piu sostenibile.")}
    `
  )
}

function figureCasoSara() {
  return shell(
    "Caso Sara: recuperare cio che conta",
    "Una settimana difficile non deve distruggere l'intero piano.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${listPanel(105, 285, "Problema", ["due sere saltate", "simulazione debole", "ansia sul tempo"], palette.bordeaux, palette.redSoft)}
    ${listPanel(590, 285, "Diario", ["lettura frettolosa", "fasi della spesa", "gestione tempo"], palette.navy, palette.blueSoft)}
    ${listPanel(1075, 285, "Revisione", ["taglia lettura passiva", "blocco errori", "routine tre giri"], palette.green, palette.greenSoft)}
    ${arrow(500, 455, 590, 455)}
    ${arrow(985, 455, 1075, 455)}
    ${note(250, 812, 1100, "Sara non recupera tutto: recupera cio che incide sulla prova.")}
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

function energyCard(x, y, [title, action, avoid, color, fill]) {
  return `<g data-safe-box="${x} ${y} 300 345 8">
    <rect x="${x}" y="${y}" width="300" height="345" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="300" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 150}" y="${y + 70}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 150}" y="${y + 142}" text-anchor="middle">Usa per</text>
    <text class="small" x="${x + 150}" y="${y + 176}" text-anchor="middle">${escapeXml(action)}</text>
    <text class="small strong" x="${x + 150}" y="${y + 245}" text-anchor="middle">Evita</text>
    <text class="small" x="${x + 150}" y="${y + 279}" text-anchor="middle">${escapeXml(avoid)}</text>
  </g>`
}

function miniBox(x, y, [top, bottom]) {
  return `<g data-safe-box="${x} ${y} 240 205 8">
    <rect x="${x}" y="${y}" width="240" height="205" rx="24" fill="${palette.greenSoft}" stroke="${palette.green}" stroke-width="3"/>
    <text class="label" style="fill:${palette.green}" x="${x + 120}" y="${y + 78}" text-anchor="middle">${escapeXml(top)}</text>
    <text class="small strong" x="${x + 120}" y="${y + 130}" text-anchor="middle">${escapeXml(bottom)}</text>
  </g>`
}

function decisionCard(x, y, [title, body, color, fill]) {
  return `<g data-safe-box="${x} ${y} 390 310 8">
    <rect x="${x}" y="${y}" width="390" height="310" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 195}" y="${y + 78}" text-anchor="middle">${escapeXml(title)}</text>
    <line x1="${x + 70}" y1="${y + 112}" x2="${x + 320}" y2="${y + 112}" stroke="${palette.border}" stroke-width="3"/>
    <text class="small strong" x="${x + 195}" y="${y + 175}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function trafficRow(x, y, [name, signal, decision, color, fill]) {
  return `<g data-safe-box="${x} ${y} 710 125 8">
    <rect x="${x}" y="${y}" width="710" height="125" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 70}" cy="${y + 62.5}" r="34" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 180}" y="${y + 54}" text-anchor="middle">${escapeXml(name)}</text>
    <text class="small" x="${x + 420}" y="${y + 48}" text-anchor="middle">${escapeXml(signal)}</text>
    <text class="small strong" x="${x + 420}" y="${y + 84}" text-anchor="middle">${escapeXml(decision)}</text>
  </g>`
}

function sideRule(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 190}" y="${y + 100 + index * 32}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 380 230 8">
    <rect x="${x}" y="${y}" width="380" height="230" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 190}" y="${y + 56}" text-anchor="middle">${escapeXml(title)}</text>
    ${rendered}
  </g>`
}

function listPanel(x, y, title, items, color, fill) {
  const lines = items
    .map((item, index) => `<text class="small" x="${x + 195}" y="${y + 130 + index * 42}" text-anchor="middle">${escapeXml(item)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 390 360 8">
    <rect x="${x}" y="${y}" width="390" height="360" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="390" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 195}" y="${y + 72}" text-anchor="middle">${escapeXml(title)}</text>
    ${lines}
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
