const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const ROOT = process.cwd()
const ASSET_ROOT = path.join(ROOT, "wiki", "books", "il-metodo-bando", "assets")
const CHAPTERS = Array.from({ length: 14 }, (_, index) => index + 34)
const WIDTH = 1536
const HEIGHT = 1024

const palette = {
  ivory: "#F7F3EA",
  paper: "#FFFDF8",
  navy: "#102A43",
  navySoft: "#E7EEF5",
  bordeaux: "#7A263A",
  bordeauxSoft: "#F5E7EA",
  gold: "#C99A2E",
  goldSoft: "#F8EFCF",
  teal: "#23757A",
  tealSoft: "#E2F1F0",
  green: "#32705B",
  greenSoft: "#E5F0EA",
  ink: "#182536",
  muted: "#667281",
  line: "#AEB8C3",
  white: "#FFFFFF"
}

const accents = [
  [palette.navy, palette.navySoft],
  [palette.bordeaux, palette.bordeauxSoft],
  [palette.gold, palette.goldSoft],
  [palette.teal, palette.tealSoft],
  [palette.green, palette.greenSoft]
]

const exactTitles = {
  "01-ciclo-simulazione": "Ciclo della simulazione",
  "02-diagnosi-errori": "Diagnosi degli errori",
  "03-setup-simulazione": "Assetto della simulazione",
  "04-matrice-tempo-risposta": "Tempo e risposta",
  "05-protocollo-correzione": "Protocollo di correzione",
  "06-registro-simulazioni": "Registro delle simulazioni",
  "07-caso-decisione": "Caso e decisione",
  "01-mappa-scheda-operativa": "Mappa della scheda operativa",
  "02-struttura-minima-scheda": "Struttura minima della scheda",
  "03-regola-uno-uno-uno": "Regola uno–uno–uno",
  "04-scheda-concetto": "Scheda concetto",
  "05-scheda-procedimento": "Scheda procedimento",
  "06-scheda-errore": "Scheda errore",
  "07-ciclo-aggiornamento": "Ciclo di aggiornamento",
  "01-mappa-priorita-studio": "Mappa delle priorità",
  "02-triage-tre-colonne": "Triage in tre colonne",
  "03-semaforo-programma": "Semaforo del programma",
  "04-regola-prova-materia-nucleo-output": "Prova, materia, nucleo, output",
  "05-matrice-resa-rischio-tempo-riuso": "Resa, rischio, tempo, riuso",
  "06-taglio-materiali": "Taglio dei materiali",
  "07-scheda-decisione-taglio": "Decisione di taglio",
  "01-mappa-strategia-punteggio": "Mappa della strategia",
  "02-soglia-rischio": "Soglia e rischio",
  "03-scheda-tempo": "Scheda del tempo",
  "04-tre-giri-quiz": "Tre giri del quiz",
  "05-matrice-certezza-rischio-tempo": "Certezza, rischio, tempo",
  "06-simulare-punteggio": "Simulare il punteggio",
  "07-caso-strategia-prova": "Strategia di prova",
  "01-mappa-routine-prova": "Mappa della routine",
  "02-linea-tempo-24-ore": "Le ventiquattro ore",
  "03-checklist-logistica": "Checklist logistica",
  "04-routine-mattino": "Routine del mattino",
  "05-lettura-istruzioni": "Lettura delle istruzioni",
  "06-protocollo-imprevisti": "Protocollo imprevisti",
  "07-caso-giorno-prova": "Il giorno della prova",
  "01-mappa-tra-prove": "Transizione tra prove",
  "02-prime-24-ore": "Le prime ventiquattro ore",
  "03-conversione-piano": "Dal riscontro al piano",
  "04-bivio-scritto-orale": "Bivio scritto–orale",
  "05-calendario-riallineamento": "Calendario di riallineamento",
  "06-esito-incerto": "Gestire un esito incerto",
  "07-caso-ripianificazione": "Caso di ripianificazione",
  "01-mappa-ripasso-finale": "Mappa del ripasso finale",
  "02-quattro-attivita-ripasso": "Quattro attività di ripasso",
  "03-fascicolo-finale": "Fascicolo finale",
  "04-matrice-tengo-recupero-lascio": "Tengo, recupero, lascio",
  "05-protocollo-sette-tre-uno": "Protocollo sette–tre–uno",
  "06-ripasso-attivo": "Ripasso attivo",
  "07-caso-ripasso": "Caso di ripasso",
  "01-mappa-caso-completo": "Mappa del caso completo",
  "02-estrazione-dati-bando": "Estrazione dei dati",
  "03-aree-nuclei": "Dalle aree ai nuclei",
  "04-diario-decisioni": "Diario delle decisioni",
  "05-output-settimanale": "Output settimanali",
  "06-piano-trenta-giorni": "Piano a trenta giorni",
  "07-caso-marta": "Caso completo",
  "01-mappa-banca-dati": "Mappa della banca dati",
  "02-verifica-ufficialita": "Verifica dell’ufficialità",
  "03-protocollo-quattro-fasi": "Protocollo in quattro fasi",
  "04-domanda-spiegazione": "Dalla domanda alla spiegazione",
  "05-diario-errori-banca-dati": "Diario errori della banca dati",
  "06-piano-banca-dati": "Piano della banca dati",
  "07-caso-banca-dati": "Caso banca dati",
  "01-mappa-risposta-sintetica": "Mappa della risposta sintetica",
  "02-lettura-traccia": "Lettura della traccia",
  "03-schema-base-risposta": "Schema della risposta",
  "04-micro-scaletta": "Micro-scaletta",
  "05-parole-chiave": "Parole chiave",
  "06-griglia-revisione": "Griglia di revisione",
  "07-caso-risposta": "Caso di risposta",
  "01-mappa-confronto": "Mappa del confronto",
  "02-criteri-distinzione": "Criteri di distinzione",
  "03-formula-confronto": "Formula del confronto",
  "04-tabella-confronto": "Tabella di confronto",
  "05-confusioni-tipiche": "Confusioni tipiche",
  "06-diario-differenze": "Diario delle differenze",
  "07-caso-confronto": "Caso di confronto",
  "01-mappa-collegamenti": "Mappa dei collegamenti",
  "02-sette-ponti": "Sette ponti",
  "03-centro-ponte-ritorno": "Centro, ponte, ritorno",
  "04-collegare-scritto": "Collegare nello scritto",
  "05-collegare-orale": "Collegare nell’orale",
  "06-scheda-ponti-utili": "Scheda dei ponti utili",
  "07-caso-collegamento": "Caso di collegamento",
  "01-mappa-domanda-imprevista": "Mappa della domanda imprevista",
  "02-perimetro-nucleo-sviluppo": "Perimetro, nucleo, sviluppo",
  "03-tipi-domande-impreviste": "Tipi di domande impreviste",
  "04-risposta-orale-imprevista": "Risposta orale imprevista",
  "05-quiz-non-so": "Il quiz quando non so",
  "06-diario-incertezza": "Diario dell’incertezza",
  "07-caso-imprevisto": "Caso imprevisto",
  "01-mappa-revisione-finale": "Mappa della revisione finale",
  "02-formula-cinque-passaggi": "Formula in cinque passaggi",
  "03-checklist-rapida": "Checklist rapida",
  "04-risposte-lunghezza": "Risposte e lunghezza",
  "05-revisione-caso-pratico": "Revisione del caso pratico",
  "06-correggere-senza-peggiorare": "Correggere senza peggiorare",
  "07-caso-consegna": "Caso e consegna"
}

async function main() {
  const browser = await chromium.launch({ headless: true })
  const results = []

  try {
    for (const chapter of CHAPTERS) {
      const chapterName = `chapter-${String(chapter).padStart(2, "0")}`
      const dir = path.join(ASSET_ROOT, chapterName)
      const files = (await fs.readdir(dir))
        .filter((file) => file.endsWith(".png"))
        .sort()

      if (files.length !== 7) {
        throw new Error(`${chapterName}: attesi 7 PNG, trovati ${files.length}`)
      }

      for (const file of files) {
        const base = file.replace(/\.png$/i, "")
        const number = Number.parseInt(base.slice(0, 2), 10)
        const module = `R${chapter - 24}`
        const title = exactTitles[base] || humanize(base.replace(/^\d+-/, ""))
        const [accent, soft] = accents[(chapter + number) % accents.length]
        const svg = renderFigure({
          title,
          module,
          number,
          accent,
          soft,
          variantSeed: chapter + number
        })
        const page = await browser.newPage({
          viewport: { width: WIDTH, height: HEIGHT },
          deviceScaleFactor: 1
        })

        try {
          await page.setContent(svg, { waitUntil: "load" })
          const root = page.locator("svg")
          await root.screenshot({ path: path.join(dir, file) })
          const geometry = await auditGeometry(page)
          if (geometry.length > 0) {
            throw new Error(`${chapterName}/${file}: ${JSON.stringify(geometry)}`)
          }
          results.push({ chapter, module, file, title })
        } finally {
          await page.close()
        }
      }
    }
  } finally {
    await browser.close()
  }

  console.log(JSON.stringify({ generated: results.length, results }, null, 2))
}

function renderFigure({ title, module, number, accent, soft, variantSeed }) {
  const content = [
    renderMap,
    renderPipeline,
    renderColumns,
    renderDecision,
    renderMatrix,
    renderLedger,
    renderCase
  ][number - 1]({ accent, soft, seed: variantSeed })
  const titleLines = wrapTitle(title)
  const titleMarkup = titleLines
    .map(
      (line, index) =>
        `<text class="title" x="112" y="${118 + index * 46}">${escapeXml(line)}</text>`
    )
    .join("")
  const contentOffset = titleLines.length > 1 ? 32 : 0

  return `<!doctype html>
  <html>
    <head><meta charset="utf-8"></head>
    <body style="margin:0">
      <svg xmlns="http://www.w3.org/2000/svg" width="${WIDTH}" height="${HEIGHT}" viewBox="0 0 ${WIDTH} ${HEIGHT}">
        <defs>
          <filter id="shadow" x="-10%" y="-10%" width="120%" height="125%">
            <feDropShadow dx="0" dy="10" stdDeviation="13" flood-color="#102A43" flood-opacity=".08"/>
          </filter>
          <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/>
          </marker>
        </defs>
        <style>
          text { font-family: Arial, Helvetica, sans-serif; fill: ${palette.ink}; }
          .eyebrow { font-size: 22px; font-weight: 700; letter-spacing: 3px; fill: ${accent}; }
          .title { font-size: 42px; font-weight: 700; letter-spacing: -.5px; }
          .label { font-size: 24px; font-weight: 700; }
          .small { font-size: 19px; font-weight: 700; letter-spacing: 1.2px; }
          .micro { font-size: 17px; font-weight: 700; letter-spacing: 1px; }
          .muted { fill: ${palette.muted}; }
          .line { fill: none; stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }
          .hairline { fill: none; stroke: ${palette.line}; stroke-width: 3; stroke-linecap: round; }
        </style>
        <rect width="${WIDTH}" height="${HEIGHT}" fill="${palette.ivory}"/>
        <path d="M48 108 V48 H108 M1428 48 H1488 V108 M48 916 V976 H108 M1428 976 H1488 V916"
              fill="none" stroke="${accent}" stroke-width="5"/>
        <circle cx="1456" cy="74" r="10" fill="${palette.gold}"/>
        <text class="eyebrow" x="112" y="62">RICETTARIO · ${module} / ${String(number).padStart(2, "0")}</text>
        ${titleMarkup}
        <g transform="translate(0 ${contentOffset})">
          <rect x="84" y="214" width="1368" height="682" rx="34" fill="${palette.paper}" stroke="${palette.line}" stroke-width="3" filter="url(#shadow)"/>
          ${content}
        </g>
        <line x1="112" y1="944" x2="642" y2="944" stroke="${palette.line}" stroke-width="3"/>
        <circle cx="682" cy="944" r="7" fill="${accent}"/>
        <circle cx="710" cy="944" r="7" fill="${palette.gold}"/>
        <circle cx="738" cy="944" r="7" fill="${palette.navy}"/>
        <line x1="778" y1="944" x2="1424" y2="944" stroke="${palette.line}" stroke-width="3"/>
      </svg>
    </body>
  </html>`
}

function renderMap({ accent, soft, seed }) {
  const nodes = [
    [400, 400, "OSSERVA"],
    [1136, 400, "SELEZIONA"],
    [1136, 720, "VERIFICA"],
    [400, 720, "REGISTRA"]
  ]
  const links = nodes
    .map(([x, y]) => `<line class="hairline" x1="768" y1="560" x2="${x}" y2="${y}"/>`)
    .join("")
  const cards = nodes
    .map(
      ([x, y, label], index) => `
        <g data-audit-box>
          <rect x="${x - 138}" y="${y - 70}" width="276" height="140" rx="24" fill="${index % 2 ? soft : palette.white}" stroke="${index % 2 ? accent : palette.navy}" stroke-width="4"/>
          <circle cx="${x - 96}" cy="${y}" r="22" fill="${index % 2 ? accent : palette.navy}"/>
          <text class="small" x="${x + 6}" y="${y + 8}" text-anchor="middle">${label}</text>
        </g>`
    )
    .join("")

  return `
    ${links}
    ${cards}
    <circle cx="768" cy="560" r="126" fill="${soft}" stroke="${accent}" stroke-width="6"/>
    <circle cx="768" cy="560" r="86" fill="${palette.paper}" stroke="${palette.navy}" stroke-width="4"/>
    <text class="label" x="768" y="553" text-anchor="middle">NUCLEO</text>
    <text class="micro muted" x="768" y="587" text-anchor="middle">DA GOVERNARE</text>
    <circle cx="${680 + (seed % 3) * 44}" cy="318" r="8" fill="${palette.gold}"/>
    <circle cx="${816 + (seed % 4) * 34}" cy="806" r="8" fill="${accent}"/>`
}

function renderPipeline({ accent, soft }) {
  const items = ["DATO", "FILTRO", "SCELTA", "OUTPUT"]
  return items
    .map((label, index) => {
      const x = 132 + index * 330
      const arrow =
        index < items.length - 1
          ? `<line class="line" x1="${x + 272}" y1="560" x2="${x + 320}" y2="560" marker-end="url(#arrow)"/>`
          : ""
      return `
        <g data-audit-box>
          <rect x="${x}" y="420" width="272" height="280" rx="28" fill="${index % 2 ? soft : palette.white}" stroke="${index % 2 ? accent : palette.navy}" stroke-width="4"/>
          <circle cx="${x + 136}" cy="488" r="30" fill="${index % 2 ? accent : palette.navy}"/>
          <text x="${x + 136}" y="497" text-anchor="middle" font-size="25" font-weight="700" fill="${palette.white}">${index + 1}</text>
          <text class="label" x="${x + 136}" y="566" text-anchor="middle">${label}</text>
          <line x1="${x + 64}" y1="612" x2="${x + 208}" y2="612" stroke="${palette.line}" stroke-width="4"/>
          <line x1="${x + 82}" y1="642" x2="${x + 190}" y2="642" stroke="${palette.line}" stroke-width="4"/>
        </g>
        ${arrow}`
    })
    .join("")
}

function renderColumns({ accent, soft }) {
  const items = [
    ["ATTIVO", palette.green, palette.greenSoft],
    ["DA TRATTARE", accent, soft],
    ["DA LASCIARE", palette.bordeaux, palette.bordeauxSoft]
  ]
  return items
    .map(([label, color, fill], index) => {
      const x = 150 + index * 428
      const rows = [0, 1, 2]
        .map(
          (row) => `
            <rect x="${x + 48}" y="${470 + row * 86}" width="236" height="58" rx="14" fill="${palette.white}" stroke="${palette.line}" stroke-width="3"/>
            <circle cx="${x + 78}" cy="${499 + row * 86}" r="9" fill="${color}"/>
            <line x1="${x + 102}" y1="${499 + row * 86}" x2="${x + 248}" y2="${499 + row * 86}" stroke="${palette.line}" stroke-width="4"/>`
        )
        .join("")
      return `
        <g data-audit-box>
          <rect x="${x}" y="342" width="332" height="474" rx="28" fill="${fill}" stroke="${color}" stroke-width="4"/>
          <rect x="${x + 34}" y="380" width="264" height="68" rx="18" fill="${color}"/>
          <text class="small" x="${x + 166}" y="423" text-anchor="middle" fill="${palette.white}">${label}</text>
          ${rows}
        </g>`
    })
    .join("")
}

function renderDecision({ accent, soft }) {
  const targets = [
    [1060, 350, "PROCEDI", palette.green, palette.greenSoft],
    [1060, 528, "RINVIA", palette.gold, palette.goldSoft],
    [1060, 706, "CORREGGI", palette.bordeaux, palette.bordeauxSoft]
  ]
  const branches = targets
    .map(
      ([x, y, label, color, fill]) => `
        <path class="hairline" d="M820 560 C900 560 912 ${y} ${x - 34} ${y}"/>
        <g data-audit-box>
          <rect x="${x}" y="${y - 60}" width="250" height="120" rx="24" fill="${fill}" stroke="${color}" stroke-width="4"/>
          <circle cx="${x + 48}" cy="${y}" r="17" fill="${color}"/>
          <text class="small" x="${x + 146}" y="${y + 8}" text-anchor="middle">${label}</text>
        </g>`
    )
    .join("")
  return `
    <g data-audit-box>
      <rect x="170" y="440" width="278" height="240" rx="28" fill="${palette.navySoft}" stroke="${palette.navy}" stroke-width="4"/>
      <text class="label" x="309" y="534" text-anchor="middle">PERIMETRO</text>
      <line x1="226" y1="582" x2="392" y2="582" stroke="${palette.line}" stroke-width="4"/>
      <line x1="246" y1="618" x2="372" y2="618" stroke="${palette.line}" stroke-width="4"/>
    </g>
    <line class="line" x1="448" y1="560" x2="552" y2="560" marker-end="url(#arrow)"/>
    <path d="M690 410 L828 560 L690 710 L552 560 Z" fill="${soft}" stroke="${accent}" stroke-width="6"/>
    <text class="label" x="690" y="551" text-anchor="middle">DECIDI</text>
    <text class="micro muted" x="690" y="587" text-anchor="middle">CON CRITERIO</text>
    ${branches}`
}

function renderMatrix({ accent, soft, seed }) {
  const cells = [
    [404, 388, "ALTA", palette.greenSoft, palette.green],
    [806, 388, "MIRATA", soft, accent],
    [404, 618, "RECUPERO", palette.goldSoft, palette.gold],
    [806, 618, "SCARTO", palette.bordeauxSoft, palette.bordeaux]
  ]
  const blocks = cells
    .map(
      ([x, y, label, fill, color], index) => `
        <g data-audit-box>
          <rect x="${x}" y="${y}" width="330" height="188" rx="24" fill="${fill}" stroke="${color}" stroke-width="${(seed + index) % 4 === 0 ? 7 : 4}"/>
          <circle cx="${x + 54}" cy="${y + 54}" r="20" fill="${color}"/>
          <text class="label" x="${x + 190}" y="${y + 64}" text-anchor="middle">${label}</text>
          <line x1="${x + 68}" y1="${y + 118}" x2="${x + 262}" y2="${y + 118}" stroke="${palette.line}" stroke-width="4"/>
          <line x1="${x + 92}" y1="${y + 148}" x2="${x + 238}" y2="${y + 148}" stroke="${palette.line}" stroke-width="4"/>
        </g>`
    )
    .join("")
  return `
    <text class="small muted" x="228" y="605" text-anchor="middle" transform="rotate(-90 228 605)">COSTO</text>
    <text class="small muted" x="782" y="344" text-anchor="middle">RESA</text>
    <line class="line" x1="302" y1="842" x2="302" y2="334" marker-end="url(#arrow)"/>
    <line class="line" x1="302" y1="842" x2="1234" y2="842" marker-end="url(#arrow)"/>
    ${blocks}`
}

function renderLedger({ accent, soft }) {
  const rows = ["RILEVA", "CLASSIFICA", "CORREGGI", "RIPROVA", "ARCHIVIA"]
    .map(
      (label, index) => `
        <g data-audit-box>
          <rect x="550" y="${330 + index * 94}" width="470" height="68" rx="16" fill="${index % 2 ? soft : palette.white}" stroke="${index % 2 ? accent : palette.line}" stroke-width="3"/>
          <circle cx="590" cy="${364 + index * 94}" r="14" fill="${index % 2 ? accent : palette.navy}"/>
          <text class="small" x="760" y="${372 + index * 94}" text-anchor="middle">${label}</text>
        </g>`
    )
    .join("")
  return `
    <g data-audit-box>
      <rect x="156" y="350" width="270" height="420" rx="30" fill="${palette.navySoft}" stroke="${palette.navy}" stroke-width="4"/>
      <rect x="212" y="414" width="158" height="206" rx="18" fill="${palette.white}" stroke="${palette.navy}" stroke-width="4"/>
      <line x1="244" y1="468" x2="338" y2="468" stroke="${palette.line}" stroke-width="5"/>
      <line x1="244" y1="516" x2="338" y2="516" stroke="${palette.line}" stroke-width="5"/>
      <line x1="244" y1="564" x2="320" y2="564" stroke="${palette.line}" stroke-width="5"/>
      <text class="small" x="291" y="692" text-anchor="middle">INPUT</text>
    </g>
    <line class="line" x1="426" y1="560" x2="516" y2="560" marker-end="url(#arrow)"/>
    ${rows}
    <line class="line" x1="1020" y1="560" x2="1108" y2="560" marker-end="url(#arrow)"/>
    <g data-audit-box>
      <circle cx="1242" cy="560" r="126" fill="${palette.greenSoft}" stroke="${palette.green}" stroke-width="6"/>
      <path d="M1180 560 L1224 604 L1312 504" fill="none" stroke="${palette.green}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <text class="small" x="1242" y="736" text-anchor="middle">VERIFICATO</text>
    </g>`
}

function renderCase({ accent, soft }) {
  const labels = ["SITUAZIONE", "ANALISI", "SCELTA", "AZIONE", "VERIFICA"]
  const nodes = labels
    .map((label, index) => {
      const x = 190 + index * 286
      const connector =
        index < labels.length - 1
          ? `<line class="line" x1="${x + 76}" y1="560" x2="${x + 202}" y2="560" marker-end="url(#arrow)"/>`
          : ""
      return `
        <g data-audit-box>
          <circle cx="${x}" cy="560" r="76" fill="${index % 2 ? soft : palette.navySoft}" stroke="${index % 2 ? accent : palette.navy}" stroke-width="5"/>
          <circle cx="${x}" cy="560" r="31" fill="${index % 2 ? accent : palette.navy}"/>
          <text x="${x}" y="569" text-anchor="middle" font-size="25" font-weight="700" fill="${palette.white}">${index + 1}</text>
          <text class="micro" x="${x}" y="680" text-anchor="middle">${label}</text>
        </g>
        ${connector}`
    })
    .join("")
  return `
    <path d="M190 560 H1334" fill="none" stroke="${palette.line}" stroke-width="4" stroke-dasharray="10 13"/>
    ${nodes}
    <rect x="314" y="760" width="908" height="70" rx="20" fill="${palette.paper}" stroke="${palette.line}" stroke-width="3"/>
    <text class="small muted" x="768" y="804" text-anchor="middle">IL PERCORSO RESTA CONTROLLABILE IN OGNI PASSAGGIO</text>`
}

async function auditGeometry(page) {
  return page.evaluate(() => {
    const svg = document.querySelector("svg")
    const root = svg.getBoundingClientRect()
    const issues = []
    const fuzz = 2
    const nodes = Array.from(svg.querySelectorAll("text, [data-audit-box]"))

    for (const node of nodes) {
      const box = node.getBoundingClientRect()
      if (
        box.left < root.left - fuzz ||
        box.top < root.top - fuzz ||
        box.right > root.right + fuzz ||
        box.bottom > root.bottom + fuzz
      ) {
        issues.push({
          type: "outside-canvas",
          node: node.tagName,
          text: (node.textContent || "").trim()
        })
      }
    }

    const texts = Array.from(svg.querySelectorAll("text")).map((node) => ({
      node,
      box: node.getBoundingClientRect(),
      text: (node.textContent || "").trim()
    }))

    for (let left = 0; left < texts.length; left += 1) {
      for (let right = left + 1; right < texts.length; right += 1) {
        const a = texts[left]
        const b = texts[right]
        const overlapX = Math.min(a.box.right, b.box.right) - Math.max(a.box.left, b.box.left)
        const overlapY = Math.min(a.box.bottom, b.box.bottom) - Math.max(a.box.top, b.box.top)
        if (overlapX > fuzz && overlapY > fuzz) {
          issues.push({ type: "text-overlap", text: `${a.text} <> ${b.text}` })
        }
      }
    }

    return issues
  })
}

function wrapTitle(title) {
  if (title.length <= 38) return [title]
  const words = title.split(/\s+/)
  const lines = [""]
  for (const word of words) {
    const current = lines[lines.length - 1]
    if (`${current} ${word}`.trim().length <= 38 || lines.length === 2) {
      lines[lines.length - 1] = `${current} ${word}`.trim()
    } else {
      lines.push(word)
    }
  }
  return lines
}

function humanize(value) {
  return value
    .replaceAll("-", " ")
    .replace(/\bpriorita\b/g, "priorità")
    .replace(/\battivita\b/g, "attività")
    .replace(/\bufficialita\b/g, "ufficialità")
    .replace(/\bcertezza\b/g, "certezza")
    .replace(/\b\w/g, (letter) => letter.toUpperCase())
}

function escapeXml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
