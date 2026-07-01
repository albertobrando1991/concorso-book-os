const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-28"
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
    slug: "01-mappa-bando-digitale",
    title: "Mappa BANDO del digitale",
    subtitle: "Lo strumento serve solo se accelera bando, aree, nuclei, diario o output.",
    description: "Mappa per collegare ogni strumento digitale a una funzione reale del Metodo BANDO.",
    svg: figureMappaBandoDigitale()
  },
  {
    slug: "02-regola-1-3-5",
    title: "Regola 1-3-5",
    subtitle: "Una fonte, tre strumenti, cinque output: meno app, piu decisioni.",
    description: "Schema operativo per limitare strumenti e mantenere il digitale al servizio dello studio.",
    svg: figureRegola135()
  },
  {
    slug: "03-cartella-minima-candidato",
    title: "Cartella minima del candidato",
    subtitle: "Cinque cartelle numerate separano fonti, piano, nuclei, output e diario.",
    description: "Architettura minima dell'archivio digitale del candidato, leggibile anche dopo settimane.",
    svg: figureCartellaMinima()
  },
  {
    slug: "04-ai-assistente-non-fonte",
    title: "AI: assistente, non fonte",
    subtitle: "L'AI trasforma materiale verificato; non decide requisiti, prove o scadenze.",
    description: "Confronto tra usi controllabili dell'AI e domande che richiedono fonte ufficiale.",
    svg: figureAiAssistente()
  },
  {
    slug: "05-protocollo-ai-sicuro",
    title: "Protocollo AI sicuro",
    subtitle: "Contesto, output verificabile, verifica e archiviazione.",
    description: "Sequenza in quattro passaggi per usare un assistente digitale senza perdere affidabilita.",
    svg: figureProtocolloAi()
  },
  {
    slug: "06-digitale-carta-output",
    title: "Digitale e carta devono parlarsi",
    subtitle: "Ogni contenuto essenziale deve essere ritrovabile, esportabile e allenabile.",
    description: "Flusso che collega strumento digitale, export, workbook, output e diario degli errori.",
    svg: figureDigitaleCarta()
  },
  {
    slug: "07-caso-luca-riordino-digitale",
    title: "Caso Luca: riordino digitale",
    subtitle: "Da strumenti dispersi a sistema unico in cinque cartelle.",
    description: "Caso guidato per trasformare app, chat e file sparsi in una struttura BANDO governabile.",
    svg: figureCasoLuca()
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

  return `# Asset Capitolo 28

Figure generate per \`Usare il digitale senza perdere il metodo\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBandoDigitale() {
  const items = [
    ["B", "Bando", "fonti e ricevute", palette.navy, palette.blueSoft],
    ["A", "Aree", "tabella profilo", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "schemi e flashcard", palette.gold, palette.goldSoft],
    ["D", "Diario", "errori e ripassi", palette.green, palette.greenSoft],
    ["O", "Output", "quiz, casi, orale", palette.teal, palette.tealSoft]
  ]
  const steps = items
    .map(([letter, title, body, color, fill], index) =>
      stepBox(105 + index * 290, 370, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 290, 485, 395 + index * 290, 485)).join("\n")

  return shell(
    "Mappa BANDO del digitale",
    "Lo strumento serve solo se accelera bando, aree, nuclei, diario o output.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(430, 210, 740, "Decisione prima dello strumento", ["prima scegli cosa devi produrre", "poi scegli app, foglio o archivio"], palette.navy, palette.blueSoft)}
    ${steps}
    ${arrows}
    ${note(250, 812, 1100, "Se uno strumento non produce una decisione o un output, e' rumore.")}
    `
  )
}

function figureRegola135() {
  return shell(
    "Regola 1-3-5",
    "Una fonte, tre strumenti, cinque output: meno app, piu decisioni.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${numberCard(130, 265, "1", "Fonte ufficiale", ["bando", "avvisi", "ricevute"], palette.navy, palette.blueSoft)}
    ${numberCard(605, 265, "3", "Strumenti stabili", ["archivio", "calendario", "foglio"], palette.gold, palette.goldSoft)}
    ${numberCard(1080, 265, "5", "Output da produrre", ["quiz", "risposte", "casi", "orale", "diario"], palette.green, palette.greenSoft)}
    ${arrow(500, 445, 605, 445)}
    ${arrow(975, 445, 1080, 445)}
    ${note(250, 812, 1100, "La qualita del sistema si misura dagli output, non dal numero di strumenti.")}
    `
  )
}

function figureCartellaMinima() {
  const folders = [
    ["01", "bando-fonti", "bando, avvisi, allegati, ricevute"],
    ["02", "decoder-piano", "decoder, calendario, priorita"],
    ["03", "materie-nuclei", "schemi, mappe, domande"],
    ["04", "output", "quiz, casi, risposte, simulazioni"],
    ["05", "diario-errori", "errore, causa, azione, verifica"]
  ]
  const rows = folders.map((folder, index) => folderRow(130, 220 + index * 105, folder)).join("\n")

  return shell(
    "Cartella minima del candidato",
    "Cinque cartelle numerate separano fonti, piano, nuclei, output e diario.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${rows}
    ${sideRule(930, 245, "Regola 1", "nessun riassunto senza fonte", palette.navy, palette.blueSoft)}
    ${sideRule(930, 400, "Regola 2", "una sola versione aggiornata", palette.gold, palette.goldSoft)}
    ${sideRule(930, 555, "Regola 3", "ogni output ha una data", palette.green, palette.greenSoft)}
    ${note(250, 812, 1100, "La numerazione impedisce alla cartella Concorso di diventare ingestibile.")}
    `
  )
}

function figureAiAssistente() {
  return shell(
    "AI: assistente, non fonte",
    "L'AI trasforma materiale verificato; non decide requisiti, prove o scadenze.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${listPanel(130, 255, "Uso controllabile", ["domande di ripasso", "schema da verificare", "simulazione orale", "categorie del diario"], palette.green, palette.greenSoft)}
    ${listPanel(1050, 255, "Da non delegare", ["requisiti", "scadenze", "prove", "documenti allegati"], palette.bordeaux, palette.redSoft)}
    ${wideCard(555, 300, 490, "Verifica obbligatoria", ["bando, avvisi, portale", "source notes consolidate"], palette.navy, palette.blueSoft)}
    ${arrow(495, 455, 555, 455)}
    ${arrow(1045, 455, 1050, 455)}
    ${note(250, 812, 1100, "L'AI puo organizzare la domanda; non puo firmare la risposta al posto tuo.")}
    `
  )
}

function figureProtocolloAi() {
  const steps = [
    ["1", "Contesto", "blocca la fonte"],
    ["2", "Output", "tabella o schema"],
    ["3", "Verifica", "controllo riga per riga"],
    ["4", "Archivia", "salva solo il corretto"]
  ]
  const boxes = steps
    .map(([num, title, body], index) => protocolBox(150 + index * 335, 330, num, title, body))
    .join("\n")
  const arrows = [0, 1, 2].map((index) => arrow(415 + index * 335, 455, 485 + index * 335, 455)).join("\n")

  return shell(
    "Protocollo AI sicuro",
    "Contesto, output verificabile, verifica e archiviazione.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${boxes}
    ${arrows}
    ${wideCard(480, 645, 640, "Condizione di ingresso", ["se non puoi verificarlo, non entra nel sistema"], palette.bordeaux, palette.redSoft)}
    ${note(250, 812, 1100, "Uno spunto puo restare spunto; capitale di studio diventa solo cio che hai controllato.")}
    `
  )
}

function figureDigitaleCarta() {
  return shell(
    "Digitale e carta devono parlarsi",
    "Ogni contenuto essenziale deve essere ritrovabile, esportabile e allenabile.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${flowCard(115, 330, "Digitale", ["cartella", "foglio", "AI"], palette.navy, palette.blueSoft)}
    ${flowCard(425, 330, "Export", ["PDF", "stampa", "backup"], palette.gold, palette.goldSoft)}
    ${flowCard(735, 330, "Workbook", ["scheda", "settimana", "20 errori"], palette.green, palette.greenSoft)}
    ${flowCard(1045, 330, "Output", ["quiz", "caso", "orale"], palette.teal, palette.tealSoft)}
    ${arrow(355, 455, 425, 455)}
    ${arrow(665, 455, 735, 455)}
    ${arrow(975, 455, 1045, 455)}
    ${wideCard(455, 645, 690, "Tre controlli", ["ritrovare", "verificare", "esportare"], palette.bordeaux, palette.redSoft)}
    ${note(250, 812, 1100, "Se non puoi recuperarlo nei giorni pieni, non affidargli una parte essenziale.")}
    `
  )
}

function figureCasoLuca() {
  return shell(
    "Caso Luca: riordino digitale",
    "Da strumenti dispersi a sistema unico in cinque cartelle.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${listPanel(115, 265, "Prima", ["desktop", "cloud", "tabella telefono", "app piano", "chat AI"], palette.bordeaux, palette.redSoft)}
    ${wideCard(560, 345, 480, "Un'ora di riordino", ["sposta, rinomina, elimina", "salva solo versioni utili"], palette.navy, palette.blueSoft)}
    ${listPanel(1085, 265, "Dopo", ["01 fonti", "02 piano", "03 nuclei", "04 output", "05 diario"], palette.green, palette.greenSoft)}
    ${arrow(505, 455, 560, 455)}
    ${arrow(1040, 455, 1085, 455)}
    ${note(250, 812, 1100, "Luca non ha studiato nuove pagine, ma il giorno dopo studia meglio.")}
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

function numberCard(x, y, number, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 175}" y="${y + 215 + index * 31}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 350 375 8">
    <rect x="${x}" y="${y}" width="350" height="375" rx="30" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="title" style="fill:${color}" x="${x + 175}" y="${y + 106}" text-anchor="middle">${escapeXml(number)}</text>
    <text class="label" x="${x + 175}" y="${y + 160}" text-anchor="middle">${escapeXml(title)}</text>
    ${rendered}
  </g>`
}

function folderRow(x, y, [num, title, body]) {
  return `<g data-safe-box="${x} ${y} 690 78 8">
    <rect x="${x}" y="${y}" width="690" height="78" rx="18" fill="${palette.blueSoft}" stroke="${palette.navy}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="106" height="78" rx="18" fill="${palette.navy}"/>
    <text class="label whiteText" x="${x + 53}" y="${y + 49}" text-anchor="middle">${escapeXml(num)}</text>
    <text class="label" x="${x + 250}" y="${y + 34}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 410}" y="${y + 60}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function sideRule(x, y, title, body, color, fill) {
  return `<g data-safe-box="${x} ${y} 470 118 8">
    <rect x="${x}" y="${y}" width="470" height="118" rx="22" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 235}" y="${y + 43}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 235}" y="${y + 80}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function listPanel(x, y, title, items, color, fill) {
  const lines = items
    .map((item, index) => `<text class="small" x="${x + 210}" y="${y + 125 + index * 42}" text-anchor="middle">${escapeXml(item)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 420 375 8">
    <rect x="${x}" y="${y}" width="420" height="375" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="420" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 210}" y="${y + 70}" text-anchor="middle">${escapeXml(title)}</text>
    ${lines}
  </g>`
}

function protocolBox(x, y, num, title, body) {
  return `<g data-safe-box="${x} ${y} 265 250 8">
    <rect x="${x}" y="${y}" width="265" height="250" rx="26" fill="${palette.blueSoft}" stroke="${palette.navy}" stroke-width="3"/>
    <circle cx="${x + 132.5}" cy="${y + 56}" r="34" fill="${palette.navy}"/>
    <text class="label whiteText" x="${x + 132.5}" y="${y + 65}" text-anchor="middle">${escapeXml(num)}</text>
    <text class="label" x="${x + 132.5}" y="${y + 130}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 132.5}" y="${y + 178}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function flowCard(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 120}" y="${y + 130 + index * 31}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 240 245 8">
    <rect x="${x}" y="${y}" width="240" height="245" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 120}" y="${y + 62}" text-anchor="middle">${escapeXml(title)}</text>
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
