const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-22"
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
    slug: "01-cinque-dati-obbligatori",
    title: "Cinque dati obbligatori prima del piano",
    subtitle: "Senza tempo, prove, ore realistiche, priorita e moduli il calendario e' fantasia.",
    svg: figureDati()
  },
  {
    slug: "02-mappa-bando-del-piano",
    title: "Mappa BANDO del piano 30/60/90",
    subtitle: "La pianificazione parte dalla prova e torna indietro fino alla settimana corrente.",
    svg: figureMappaBando()
  },
  {
    slug: "03-struttura-base-ogni-piano",
    title: "Struttura base di ogni piano",
    subtitle: "Studio, richiamo, ripasso, output e correzione devono comparire ogni settimana.",
    svg: figureStruttura()
  },
  {
    slug: "04-confronto-30-60-90-giorni",
    title: "Confronto operativo 30 / 60 / 90 giorni",
    subtitle: "La durata cambia profondita, margine di correzione e ruolo delle simulazioni.",
    svg: figureConfronto()
  },
  {
    slug: "05-piano-15-giorni-e-tagli",
    title: "Piano 15 giorni e tagli",
    subtitle: "Quando il tempo e' minimo, non si aggiunge materiale: si toglie rumore.",
    svg: figureQuindici()
  },
  {
    slug: "06-settimana-tipo-output",
    title: "Settimana tipo orientata agli output",
    subtitle: "Core, modulo, ripasso, simulazione e diario devono restare nello stesso ciclo.",
    svg: figureSettimana()
  },
  {
    slug: "07-caso-luca-ciclo-controllo",
    title: "Caso Luca: ciclo di controllo",
    subtitle: "Un piano funziona se ogni settimana produce dati, correzioni e decisioni.",
    svg: figureCaso()
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
  return `# Asset Capitolo 22

Figure generate per \`Piano 30/60/90 giorni\`.

| File | Funzione didattica |
|---|---|
| \`01-cinque-dati-obbligatori.png\` | I cinque dati minimi prima di costruire il piano. |
| \`02-mappa-bando-del-piano.png\` | Mappa BANDO del piano: bando, aree, nuclei, diario, output. |
| \`03-struttura-base-ogni-piano.png\` | I cinque blocchi ricorrenti di ogni calendario efficace. |
| \`04-confronto-30-60-90-giorni.png\` | Confronto tra preparazione breve, intermedia e solida. |
| \`05-piano-15-giorni-e-tagli.png\` | Protocollo di emergenza e tagli da fare quando restano 15 giorni. |
| \`06-settimana-tipo-output.png\` | Settimana tipo con core, modulo, prova, ripasso e diario. |
| \`07-caso-luca-ciclo-controllo.png\` | Caso guidato Luca e ciclo settimanale di correzione del piano. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureDati() {
  const items = [
    ["Giorni", "profondita e tagli", "navy", "softBlue"],
    ["Ore reali", "calendario sostenibile", "bordeaux", "softRed"],
    ["Prove", "tipo di output", "gold", "softGold"],
    ["Alta resa", "priorita settimanali", "green", "softGreen"],
    ["Moduli", "cosa aggiungere al core", "teal", "softTeal"]
  ]

  const cards = items
    .map(([title, body, color, box], index) => filterCard(100 + index * 295, 335, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="235" text-anchor="middle">Prima estrai i dati, poi costruisci la settimana</text>
  ${cards}
  <path class="arrowNavy" d="M310 425 L390 425"/>
  <path class="arrowNavy" d="M605 425 L685 425"/>
  <path class="arrowNavy" d="M900 425 L980 425"/>
  <path class="arrowNavy" d="M1195 425 L1275 425"/>
  ${note(250, 705, 1100, "Se manca un dato, il piano torna al bando e alla mappa profilo.")}`

  return shell(
    "Cinque dati obbligatori prima del piano",
    "Senza tempo, prove, ore realistiche, priorita e moduli il calendario e' fantasia.",
    inner
  )
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${wideCard(500, 205, 600, "Piano di controllo", ["non promessa", "ma revisione settimanale"], "navy", "softBlue")}
  <path class="line" d="M800 332 L800 388"/>
  <path class="line" d="M210 388 L1390 388"/>
  ${connector(210, 388, 210, 462)}
  ${connector(505, 388, 505, 575)}
  ${connector(800, 388, 800, 462)}
  ${connector(1095, 388, 1095, 575)}
  ${connector(1390, 388, 1390, 462)}
  ${stepBox(80, 462, 260, "Bando", ["tempo", "prova"], "navy", "softBlue")}
  ${stepBox(375, 575, 260, "Aree", ["core", "moduli"], "bordeaux", "softRed")}
  ${stepBox(670, 462, 260, "Nuclei", ["alta resa", "priorita"], "gold", "softGold")}
  ${stepBox(965, 575, 260, "Diario", ["errori", "ritardi"], "green", "softGreen")}
  ${stepBox(1260, 462, 260, "Output", ["quiz", "simulazione"], "teal", "softTeal")}
  ${note(250, 812, 1100, "Il piano parte dalla prova e torna indietro: non dal lunedi.")}`

  return shell(
    "Mappa BANDO del piano 30/60/90",
    "La pianificazione parte dalla prova e torna indietro fino alla settimana corrente.",
    inner
  )
}

function figureStruttura() {
  const blocks = [
    ["Studio nuovo", "contenuti essenziali", "navy", "softBlue"],
    ["Richiamo attivo", "rispondere senza testo", "bordeaux", "softRed"],
    ["Ripasso", "tornare prima di dimenticare", "gold", "softGold"],
    ["Output", "quiz, caso, orale, simulazione", "green", "softGreen"],
    ["Correzione", "errori e passo successivo", "teal", "softTeal"]
  ]

  const cards = blocks
    .map(([title, body, color, box], index) => stepCard(105 + index * 295, 330, index + 1, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="230" text-anchor="middle">Un calendario con sola lettura non e' ancora un piano</text>
  ${cards}
  <path class="arrowNavy" d="M315 435 L390 435"/>
  <path class="arrowNavy" d="M610 435 L685 435"/>
  <path class="arrowNavy" d="M905 435 L980 435"/>
  <path class="arrowNavy" d="M1200 435 L1275 435"/>
  ${note(250, 705, 1100, "Ogni settimana deve dire: studio, richiamo, ripasso, produco e correggo.")}`

  return shell(
    "Struttura base di ogni piano",
    "Studio, richiamo, ripasso, output e correzione devono comparire ogni settimana.",
    inner
  )
}

function figureConfronto() {
  const columns = [
    ["30 giorni", "selezione", ["core minimo", "un modulo killer", "simulazioni presto"], "bordeaux", "softRed"],
    ["60 giorni", "copertura", ["core stabile", "modulo profilo", "simulazioni con margine"], "navy", "softBlue"],
    ["90 giorni", "correzione", ["fondazione", "applicazione", "stabilizzazione"], "green", "softGreen"]
  ]

  const cards = columns
    .map(([title, label, rows, color, box], index) => bigColumn(135 + index * 465, 260, 400, title, label, rows, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Piu tempo non significa studiare tutto: significa correggere meglio</text>
  ${cards}
  ${note(250, 812, 1100, "La durata decide profondita, numero di moduli e spazio per errori e simulazioni.")}`

  return shell(
    "Confronto operativo 30 / 60 / 90 giorni",
    "La durata cambia profondita, margine di correzione e ruolo delle simulazioni.",
    inner
  )
}

function figureQuindici() {
  const steps = [
    ["1-2", "Bando e diagnosi", "prova breve", "navy", "softBlue"],
    ["3-8", "Core minimo", "quiz + errori", "bordeaux", "softRed"],
    ["9-12", "Modulo killer", "simulazioni", "gold", "softGold"],
    ["13-15", "Rifinitura", "schede + logistica", "green", "softGreen"]
  ]

  const cards = steps
    .map(([day, title, body, color, box], index) => emergencyCard(150 + index * 370, 290, day, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Emergenza vera: scegli, riduci, verifica</text>
  ${cards}
  <path class="arrowNavy" d="M455 405 L510 405"/>
  <path class="arrowNavy" d="M825 405 L880 405"/>
  <path class="arrowNavy" d="M1195 405 L1250 405"/>
  ${mini(245, 640, 330, "Taglia", "dettagli rari e lettura passiva", palette.bordeaux)}
  ${mini(635, 640, 330, "Proteggi", "simulazioni e correzione", palette.navy)}
  ${mini(1025, 640, 330, "Chiudi", "documenti e routine prova", palette.green)}
  ${note(250, 812, 1100, "Negli ultimi 15 giorni non vinci aggiungendo materiale: vinci togliendo rumore.")}`

  return shell(
    "Piano 15 giorni e tagli",
    "Quando il tempo e' minimo, non si aggiunge materiale: si toglie rumore.",
    inner
  )
}

function figureSettimana() {
  const rows = [
    ["Lun", "core", "richiamo", "10 domande"],
    ["Mar", "modulo", "quiz", "diario errori"],
    ["Mer", "ripasso", "caso/orale", "risposta breve"],
    ["Gio", "core", "drill errori", "flashcard"],
    ["Ven", "modulo", "simulazione", "correzione"],
    ["Sab", "simulazione", "revisione", "tagli"],
    ["Dom", "ripasso leggero", "pianifica", "settimana nuova"]
  ]

  const body = rows.map((row, index) => weekRow(165, 260 + index * 62, 1270, row, index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Dimezza i blocchi se hai poco tempo, ma non eliminare output e diario</text>
  <g data-safe-box="165 260 1270 434 8">
    ${body}
  </g>
  ${note(250, 735, 1100, "La settimana tipo alterna teoria, richiamo, modulo, prova e correzione.")}`

  return shell(
    "Settimana tipo orientata agli output",
    "Core, modulo, ripasso, simulazione e diario devono restare nello stesso ciclo.",
    inner
  )
}

function figureCaso() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Luca ha 60 giorni: il piano funziona perche produce prova</text>
  ${caseBox(120, 295, 360, "Giorni 1-10", ["bando", "core", "diagnosi"], "navy", "softBlue")}
  ${caseBox(510, 295, 360, "Giorni 11-25", ["amministrativo", "accesso", "pubblico impiego"], "bordeaux", "softRed")}
  ${caseBox(900, 295, 360, "Giorni 26-40", ["TUEL", "atti", "contabilita"], "gold", "softGold")}
  ${caseBox(330, 550, 360, "Giorni 41-52", ["quiz", "casi", "correzione"], "green", "softGreen")}
  ${caseBox(850, 550, 360, "Giorni 53-60", ["simulazioni", "orale", "logistica"], "teal", "softTeal")}
  <path class="arrowNavy" d="M490 405 L500 405"/>
  <path class="arrowNavy" d="M880 405 L890 405"/>
  <path class="arrowNavy" d="M1070 500 L935 540"/>
  <path class="arrowNavy" d="M690 630 L835 630"/>
  ${note(250, 812, 1100, "Ogni settimana: risultati, errori, tagli e decisione per la settimana successiva.")}`

  return shell(
    "Caso Luca: ciclo di controllo",
    "Un piano funziona se ogni settimana produce dati, correzioni e decisioni.",
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
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="108" text-anchor="middle">${esc(subtitle)}</text>
${inner}
</svg>
`
}

function wideCard(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 77 + index * 27}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 128 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="128" rx="25"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 44}" text-anchor="middle">${esc(title)}</text>
    ${body}
  </g>`
}

function stepBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 27}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 142 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="142" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    ${rows}
  </g>`
}

function filterCard(x, y, title, body, colorClass, boxClass) {
  const titleSize = title.length > 10 ? 20 : 22
  return `<g data-safe-box="${x} ${y} 205 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="190" rx="24"/>
    <rect x="${x}" y="${y}" width="205" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 54}" text-anchor="middle" style="font-size:${titleSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 28} ${y + 76} L${x + 177} ${y + 76}"/>
    <text class="muted small" x="${x + 102.5}" y="${y + 122}" text-anchor="middle" style="font-size:15px">${esc(body)}</text>
  </g>`
}

function stepCard(x, y, number, title, body, colorClass, boxClass) {
  const titleSize = title.length > 15 ? 17 : 19
  const bodySize = body.length > 28 ? 14 : 15
  return `<g data-safe-box="${x} ${y} 205 205 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="205" rx="24"/>
    <circle cx="${x + 102.5}" cy="${y + 43}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 102.5}" y="${y + 52}" text-anchor="middle" fill="#FFFFFF">${number}</text>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 94}" text-anchor="middle" style="font-size:${titleSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + 102.5}" y="${y + 142}" text-anchor="middle" style="font-size:${bodySize}px">${esc(body)}</text>
  </g>`
}

function bigColumn(x, y, w, title, label, rows, colorClass, boxClass) {
  const body = rows
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 150 + index * 48}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 430 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="430" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 55}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    <text class="ink label" x="${x + w / 2}" y="${y + 100}" text-anchor="middle" style="font-size:21px">${esc(label)}</text>
    <path class="thin" d="M${x + 40} ${y + 120} L${x + w - 40} ${y + 120}"/>
    ${body}
  </g>`
}

function emergencyCard(x, y, day, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 300 250 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="300" height="250" rx="26"/>
    <circle cx="${x + 150}" cy="${y + 55}" r="36" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 150}" y="${y + 66}" text-anchor="middle" fill="#FFFFFF" style="font-size:22px">${esc(day)}</text>
    <text class="${colorClass} label" x="${x + 150}" y="${y + 122}" text-anchor="middle" style="font-size:20px">${esc(title)}</text>
    <text class="muted small" x="${x + 150}" y="${y + 178}" text-anchor="middle" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function weekRow(x, y, w, row, index) {
  const [day, block1, block2, output] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  return `<g>
    <rect x="${x}" y="${y}" width="${w}" height="54" rx="12" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <text class="navy label" x="${x + 34}" y="${y + 36}" style="font-size:18px">${esc(day)}</text>
    <text class="muted small" x="${x + 230}" y="${y + 36}" style="font-size:17px">${esc(block1)}</text>
    <text class="muted small" x="${x + 570}" y="${y + 36}" style="font-size:17px">${esc(block2)}</text>
    <text class="bordeaux label" x="${x + 920}" y="${y + 36}" style="font-size:17px">${esc(output)}</text>
  </g>`
}

function caseBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 105 + index * 36}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="190" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <path class="thin" d="M${x + 35} ${y + 70} L${x + w - 35} ${y + 70}"/>
    ${rows}
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 17 ? 17 : 20
  const bodyFontSize = body.length > 31 ? 14 : 16
  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 112 ? 18 : text.length > 94 ? 19 : 20
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
