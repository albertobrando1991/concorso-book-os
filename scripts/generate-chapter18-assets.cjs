const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-18"
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
    slug: "01-mappa-bando-quesiti-situazionali",
    title: "Mappa BANDO dei quesiti situazionali",
    subtitle: "Dal bando alla scelta motivata: ogni scenario misura comportamento pubblico.",
    svg: figureMappa()
  },
  {
    slug: "02-competenze-trasversali-pa",
    title: "Competenze trasversali nella PA",
    subtitle: "Le soft skills diventano comportamenti osservabili dentro regole e servizio.",
    svg: figureCompetenze()
  },
  {
    slug: "03-anatomia-quesito-situazionale",
    title: "Anatomia del quesito situazionale",
    subtitle: "Scenario, ruolo, tensione, opzioni e richiesta vanno letti separatamente.",
    svg: figureAnatomia()
  },
  {
    slug: "04-gerarchia-di-scelta",
    title: "Gerarchia di scelta",
    subtitle: "Prima si scartano le opzioni illegittime, poi si cerca il miglior equilibrio.",
    svg: figureGerarchia()
  },
  {
    slug: "05-quattro-risposte-deboli",
    title: "Le quattro risposte deboli",
    subtitle: "Buonismo, rigidita, passivita e iniziativa fuori ruolo sono trappole ricorrenti.",
    svg: figureDeboli()
  },
  {
    slug: "06-lettura-guidata-opzioni",
    title: "Lettura guidata delle opzioni",
    subtitle: "Ogni alternativa va qualificata: scorretta, debole, accettabile o efficace.",
    svg: figureOpzioni()
  },
  {
    slug: "07-routine-diario-errori-situazionali",
    title: "Routine e diario degli errori",
    subtitle: "L'allenamento corregge il criterio di scelta, non solo il singolo quesito.",
    svg: figureRoutine()
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
  return `# Asset Capitolo 18

Figure generate per \`Quesiti situazionali e soft skills\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-quesiti-situazionali.png\` | Mappa BANDO dei quesiti situazionali: bando, aree, nuclei, diario e output. |
| \`02-competenze-trasversali-pa.png\` | Collegamento tra competenze trasversali, valori pubblici e comportamento osservabile. |
| \`03-anatomia-quesito-situazionale.png\` | Struttura del quesito: scenario, ruolo, tensione, opzioni e richiesta. |
| \`04-gerarchia-di-scelta.png\` | Gerarchia dei criteri per scartare e scegliere l'opzione migliore. |
| \`05-quattro-risposte-deboli.png\` | Trappole frequenti: buonismo, rigidita, passivita e iniziativa fuori ruolo. |
| \`06-lettura-guidata-opzioni.png\` | Metodo per classificare le alternative e motivare la scelta. |
| \`07-routine-diario-errori-situazionali.png\` | Routine di allenamento e diario degli errori situazionali. |

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
      .dash { stroke: ${palette.line}; stroke-width: 3.5; stroke-linecap: round; stroke-dasharray: 9 10; fill: none; }
      .arrowNavy { stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowNavy); }
      .arrowBordeaux { stroke: ${palette.bordeaux}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowBordeaux); }
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
      .arrowGreen { stroke: ${palette.green}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGreen); }
      .arrowTeal { stroke: ${palette.teal}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowTeal); }
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
    <marker id="arrowTeal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.teal}"/>
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
  ${card(590, 168, 420, 125, "Comportamento pubblico", ["scegliere l'azione", "piu coerente"], "navy", "card")}
  <path class="line" d="M800 293 L800 363"/>
  <path class="line" d="M210 363 L1390 363"/>
  ${connector(210, 363, 210, 450)}
  ${connector(505, 363, 505, 570)}
  ${connector(800, 363, 800, 450)}
  ${connector(1095, 363, 1095, 570)}
  ${connector(1390, 363, 1390, 450)}
  ${card(75, 450, 270, 130, "Bando", ["quesiti, lingua", "punteggio"], "navy", "softBlue")}
  ${card(370, 570, 270, 130, "Aree", ["cittadino, colleghi", "dati, conflitti"], "bordeaux", "softRed")}
  ${card(665, 450, 270, 130, "Nuclei", ["legalita", "servizio, privacy"], "gold", "softGold")}
  ${card(960, 570, 270, 130, "Diario", ["errore ricorrente", "criterio da correggere"], "green", "softGreen")}
  ${card(1255, 450, 270, 130, "Output", ["opzione scelta", "motivazione"], "teal", "softTeal")}
  ${note(250, 792, 1100, "Il quesito situazionale non premia la risposta piu gentile: premia il ruolo pubblico piu corretto.")}
`
  return shell(
    "Mappa BANDO dei quesiti situazionali",
    "Dal bando alla scelta motivata: ogni scenario misura comportamento pubblico.",
    inner
  )
}

function figureCompetenze() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${centerBadge(620, 330, 360, 170, "Comportamento", ["pubblico osservabile"], "navy")}
  ${wideTile(125, 235, 420, "Capire il contesto", ["ruolo, regole, dati", "problema e cambiamento"], "navy", "softBlue")}
  ${wideTile(1055, 235, 420, "Interagire", ["comunicare", "collaborare, servire"], "bordeaux", "softRed")}
  ${wideTile(125, 550, 420, "Realizzare valore", ["affidabilita", "accuratezza, risultato"], "green", "softGreen")}
  ${wideTile(1055, 550, 420, "Gestire risorse", ["processi, strumenti", "persone e responsabilita"], "teal", "softTeal")}
  <path class="arrowNavy" d="M555 315 L610 365"/>
  <path class="arrowBordeaux" d="M1045 315 L990 365"/>
  <path class="arrowGreen" d="M555 630 L610 505"/>
  <path class="arrowTeal" d="M1045 630 L990 505"/>
  ${mini(425, 725, 220, "Integrita", "niente scorciatoie", palette.bordeaux)}
  ${mini(690, 725, 220, "Inclusione", "servizio corretto", palette.green)}
  ${mini(955, 725, 220, "Sostenibilita", "risorse responsabili", palette.teal)}
`
  return shell(
    "Competenze trasversali nella PA",
    "Le soft skills diventano comportamenti osservabili dentro regole e servizio.",
    inner
  )
}

function figureAnatomia() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Leggi il quesito in cinque parti, non come una storia unica</text>
  ${stepCard(105, 345, "1", "Scenario", ["che cosa", "sta accadendo"], "navy", "softBlue")}
  ${stepCard(380, 345, "2", "Ruolo", ["che cosa puoi", "davvero fare"], "bordeaux", "softRed")}
  ${stepCard(655, 345, "3", "Tensione", ["rischio", "o conflitto"], "gold", "softGold")}
  ${stepCard(930, 345, "4", "Opzioni", ["alternative", "da classificare"], "green", "softGreen")}
  ${stepCard(1205, 345, "5", "Richiesta", ["piu efficace", "o meno efficace"], "teal", "softTeal")}
  <path class="arrowNavy" d="M315 440 L370 440"/>
  <path class="arrowBordeaux" d="M590 440 L645 440"/>
  <path class="arrowGold" d="M865 440 L920 440"/>
  <path class="arrowGreen" d="M1140 440 L1195 440"/>
  ${note(250, 672, 1100, "Prima di scegliere, chiediti sempre quale competenza la traccia sta misurando.")}
`
  return shell(
    "Anatomia del quesito situazionale",
    "Scenario, ruolo, tensione, opzioni e richiesta vanno letti separatamente.",
    inner
  )
}

function figureGerarchia() {
  const items = [
    ["1", "Legalita e competenza", "scarta cio che aggira regole o ruolo", "navy", "softBlue"],
    ["2", "Imparzialita e integrita", "scarta favoritismi e interessi personali", "bordeaux", "softRed"],
    ["3", "Riservatezza", "protegge dati e informazioni d'ufficio", "gold", "softGold"],
    ["4", "Orientamento al servizio", "aiuta senza promettere esiti impropri", "green", "softGreen"],
    ["5", "Collaborazione", "coinvolge la persona giusta quando serve", "teal", "softTeal"],
    ["6", "Tracciabilita", "lascia passaggi controllabili", "navy", "softBlue"]
  ]
  const rows = items
    .map(([num, title, body, color, box], index) => ladderRow(210, 205 + index * 88, 1180, num, title, body, color, box))
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${rows}
  ${note(250, 812, 1100, "Una risposta puo essere gentile e sbagliata, o prudente e incompleta: scegli l'equilibrio pubblico.")}
`
  return shell(
    "Gerarchia di scelta",
    "Prima si scartano le opzioni illegittime, poi si cerca il miglior equilibrio.",
    inner
  )
}

function figureDeboli() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${trapTile(140, 240, 580, "Risposta buonista", ["aiuta violando canali", "o dati personali"], "bordeaux", "softRed")}
  ${trapTile(880, 240, 580, "Risposta autoritaria", ["applica la regola", "senza orientare"], "navy", "softBlue")}
  ${trapTile(140, 520, 580, "Risposta passiva", ["evita il rischio", "ma non gestisce"], "gold", "softGold")}
  ${trapTile(880, 520, 580, "Risposta solitaria", ["mostra iniziativa", "ma supera il ruolo"], "green", "softGreen")}
  <path class="dash" d="M800 220 L800 720"/>
  <path class="dash" d="M110 485 L1490 485"/>
  ${note(250, 812, 1100, "La trappola ha sempre un lato seducente: servizio, regola, prudenza o iniziativa usati male.")}
`
  return shell(
    "Le quattro risposte deboli",
    "Buonismo, rigidita, passivita e iniziativa fuori ruolo sono trappole ricorrenti.",
    inner
  )
}

function figureOpzioni() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Classifica ogni alternativa prima di scegliere</text>
  ${optionBand(135, 285, "Scorretta", "viola regole, dati, ruolo o imparzialita", "scarta subito", "bordeaux", "softRed")}
  ${optionBand(135, 405, "Debole", "e' passiva, brusca, sproporzionata o non tracciata", "elimina dopo", "gold", "softGold")}
  ${optionBand(135, 525, "Accettabile", "rispetta le regole ma manca servizio o precisione", "tieni in riserva", "teal", "softTeal")}
  ${optionBand(135, 645, "Efficace", "combina regola, servizio, competenza e traccia", "scegli e motiva", "green", "softGreen")}
  ${note(250, 812, 1100, "La motivazione in una riga controlla se la scelta e' davvero tua o solo intuitiva.")}
`
  return shell(
    "Lettura guidata delle opzioni",
    "Ogni alternativa va qualificata: scorretta, debole, accettabile o efficace.",
    inner
  )
}

function figureRoutine() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${listPanel(120, 225, 610, "Routine in 7 mosse", [
    "1. leggi scenario e ruolo",
    "2. individua rischio principale",
    "3. scarta opzioni illegittime",
    "4. scarta passivita e sproporzione",
    "5. scegli equilibrio pubblico",
    "6. scrivi una motivazione",
    "7. registra l'errore"
  ], "navy", "softBlue")}
  ${listPanel(870, 225, 610, "Diario degli errori", [
    "troppa empatia",
    "troppa rigidita",
    "passivita",
    "invasione di competenza",
    "privacy o conflitto",
    "comunicazione vaga",
    "scelta da stress"
  ], "bordeaux", "softRed")}
  <path class="arrowGreen" d="M745 445 L855 445"/>
  <path class="arrowTeal" d="M855 590 C720 690 520 690 385 590"/>
  ${mini(610, 690, 380, "Correzione", "allena il criterio piu fragile", palette.green)}
`
  return shell(
    "Routine e diario degli errori",
    "L'allenamento corregge il criterio di scelta, non solo il singolo quesito.",
    inner
  )
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleFontSize = title.length > 28 ? 17 : title.length > 21 ? 19 : title.length > 14 ? 22 : 25
  const bodyFontSize = lines.some((line) => line.length > 25) ? 15 : 18
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 74 + index * 25}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function wideTile(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 83 + index * 30}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 165 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="165" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 45}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    ${body}
  </g>`
}

function centerBadge(x, y, w, h, title, lines, colorClass) {
  const body = lines
    .map((line, index) => `<text class="small" x="${x + w / 2}" y="${y + 98 + index * 28}" text-anchor="middle" fill="#FFFFFF">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="34" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + w / 2}" y="${y + 62}" text-anchor="middle" fill="#FFFFFF">${esc(title)}</text>
    ${body}
  </g>`
}

function stepCard(x, y, number, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 102}" y="${y + 94 + index * 27}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 205 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="190" rx="24"/>
    <circle cx="${x + 102.5}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 102.5}" y="${y + 51}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 78}" text-anchor="middle" style="font-size:18px">${esc(title)}</text>
    ${body}
  </g>`
}

function ladderRow(x, y, w, number, title, body, colorClass, boxClass) {
  const titleFontSize = title.length > 24 ? 19 : 22
  const bodyFontSize = body.length > 48 ? 16 : 18

  return `<g data-safe-box="${x} ${y} ${w} 68 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="68" rx="20"/>
    <circle cx="${x + 44}" cy="${y + 34}" r="24" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 44}" y="${y + 43}" text-anchor="middle" fill="#FFFFFF" style="font-size:22px">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 315}" y="${y + 43}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + 790}" y="${y + 42}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function trapTile(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 90 + index * 31}" text-anchor="middle" style="font-size:18px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 195 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="195" rx="25"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 47}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    <path class="thin" d="M${x + 40} ${y + 65} L${x + w - 40} ${y + 65}"/>
    ${body}
  </g>`
}

function optionBand(x, y, label, signal, action, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 1330 88 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="1330" height="88" rx="22"/>
    <rect x="${x}" y="${y}" width="13" height="88" rx="6.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 160}" y="${y + 55}" text-anchor="middle" style="font-size:24px">${esc(label)}</text>
    <text class="muted small" x="${x + 680}" y="${y + 54}" text-anchor="middle">${esc(signal)}</text>
    <text class="${colorClass} label" x="${x + 1160}" y="${y + 55}" text-anchor="middle" style="font-size:21px">${esc(action)}</text>
  </g>`
}

function listPanel(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + 34}" y="${y + 95 + index * 39}" style="font-size:18px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 405 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="405" rx="25"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    <path class="thin" d="M${x + 30} ${y + 65} L${x + w - 30} ${y + 65}"/>
    ${rows}
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 17 ? 17 : 20
  const bodyFontSize = body.length > 28 ? 14 : 16

  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 106 ? 18 : text.length > 90 ? 19 : 20

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
