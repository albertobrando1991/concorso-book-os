const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-21"
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
    slug: "01-mappa-bando-moduli-integrativi",
    title: "Mappa BANDO dei moduli integrativi",
    subtitle: "Il modulo parte dal bando, passa dal diario e deve produrre output verificabile.",
    svg: figureMappaBando()
  },
  {
    slug: "02-core-modulo-approfondimento",
    title: "Core, modulo e approfondimento",
    subtitle: "Non tutto cio che e' interessante deve entrare nel piano di preparazione.",
    svg: figureCoreModulo()
  },
  {
    slug: "03-quattro-requisiti-del-modulo",
    title: "Quattro requisiti del modulo",
    subtitle: "Un modulo utile nasce da un bisogno, chiude una lacuna, produce output e ha limiti.",
    svg: figureQuattroRequisiti()
  },
  {
    slug: "04-cinque-filtri-di-scelta",
    title: "I cinque filtri di scelta",
    subtitle: "Prima di aprire materiali integrativi, passa da bando, profilo, prova, rischio e output.",
    svg: figureCinqueFiltri()
  },
  {
    slug: "05-matrice-decisione-moduli",
    title: "Matrice di decisione dei moduli",
    subtitle: "La scelta corretta non e' aprire tutto: e' assegnare profondita e limite.",
    svg: figureMatriceDecisione()
  },
  {
    slug: "06-atlante-moduli-integrativi",
    title: "Atlante operativo dei moduli",
    subtitle: "Ogni modulo deve collegare profilo, materia, prova e prodotto finale.",
    svg: figureAtlanteModuli()
  },
  {
    slug: "07-scheda-modulo-e-caso-sara",
    title: "Scheda modulo e caso Sara",
    subtitle: "Una decisione buona isola il modulo senza duplicare il nucleo comune.",
    svg: figureSchedaCaso()
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
  return `# Asset Capitolo 21

Figure generate per \`Come scegliere i moduli integrativi\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-moduli-integrativi.png\` | Mappa BANDO per decidere quando un modulo entra nel piano. |
| \`02-core-modulo-approfondimento.png\` | Distinzione tra nucleo comune, modulo necessario e approfondimento da lasciare fuori. |
| \`03-quattro-requisiti-del-modulo.png\` | Le quattro condizioni minime per considerare utile un modulo integrativo. |
| \`04-cinque-filtri-di-scelta.png\` | Filtri bando, profilo, prova, rischio e output prima di aprire materiali. |
| \`05-matrice-decisione-moduli.png\` | Matrice visuale per scegliere tra modulo completo, essenziale, mini-modulo, drill o taglio. |
| \`06-atlante-moduli-integrativi.png\` | Atlante sintetico dei principali moduli integrativi del Metodo BANDO. |
| \`07-scheda-modulo-e-caso-sara.png\` | Scheda operativa e caso Sara per combinare core comune e moduli separati. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${wideCard(490, 205, 620, "Modulo integrativo", ["un blocco mirato", "non un manuale in piu"], "navy", "softBlue")}
  <path class="line" d="M800 332 L800 388"/>
  <path class="line" d="M210 388 L1390 388"/>
  ${connector(210, 388, 210, 462)}
  ${connector(505, 388, 505, 575)}
  ${connector(800, 388, 800, 462)}
  ${connector(1095, 388, 1095, 575)}
  ${connector(1390, 388, 1390, 462)}
  ${stepBox(80, 462, 260, "Bando", ["lista differenze", "dal core"], "navy", "softBlue")}
  ${stepBox(375, 575, 260, "Aree", ["famiglia", "specialistica"], "bordeaux", "softRed")}
  ${stepBox(670, 462, 260, "Nuclei", ["contenuti", "ad alta resa"], "gold", "softGold")}
  ${stepBox(965, 575, 260, "Diario", ["errori", "tempo e limiti"], "green", "softGreen")}
  ${stepBox(1260, 462, 260, "Output", ["quiz", "caso", "orale"], "teal", "softTeal")}
  ${note(250, 812, 1100, "Il modulo nasce dal bando, ma viene confermato dal diario e dagli output.")}`

  return shell(
    "Mappa BANDO dei moduli integrativi",
    "Il modulo parte dal bando, passa dal diario e deve produrre output verificabile.",
    inner
  )
}

function figureCoreModulo() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${columnBox(130, 270, 360, "Nucleo comune", ["si riusa", "tra piu concorsi", "non si abbandona"], "navy", "softBlue")}
  ${columnBox(620, 270, 360, "Modulo necessario", ["entra se il bando", "cambia profilo", "o prova"], "bordeaux", "softRed")}
  ${columnBox(1110, 270, 360, "Approfondimento", ["resta fuori", "se non produce", "punteggio"], "gold", "softGold")}
  <path class="arrowNavy" d="M498 455 L608 455"/>
  <path class="arrowGold" d="M988 455 L1098 455"/>
  ${wideCard(395, 690, 810, "Regola pratica", ["prima garantisci il core minimo", "poi dai profondita al modulo decisivo"], "green", "softGreen")}`

  return shell(
    "Core, modulo e approfondimento",
    "Non tutto cio che e' interessante deve entrare nel piano di preparazione.",
    inner
  )
}

function figureQuattroRequisiti() {
  const items = [
    ["1", "Esigenza del bando", "materia, prova o competenza richiesta", "navy", "softBlue"],
    ["2", "Lacuna del core", "il libro base non basta per quel profilo", "bordeaux", "softRed"],
    ["3", "Output verificabile", "quiz, caso, orale, schema o prova", "gold", "softGold"],
    ["4", "Limite di profondita", "tempo massimo e cosa non studiare", "green", "softGreen"]
  ]

  const cards = items
    .map(([n, title, body, color, box], index) => numberedTile(150 + index * 370, 300, 300, n, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="230" text-anchor="middle">Senza questi quattro elementi il modulo diventa dispersione</text>
  ${cards}
  <path class="arrowNavy" d="M455 420 L510 420"/>
  <path class="arrowNavy" d="M825 420 L880 420"/>
  <path class="arrowNavy" d="M1195 420 L1250 420"/>
  ${note(250, 705, 1100, "La risposta non valida e': aver letto il modulo. Serve un prodotto osservabile.")}`

  return shell(
    "Quattro requisiti del modulo",
    "Un modulo utile nasce da un bisogno, chiude una lacuna, produce output e ha limiti.",
    inner
  )
}

function figureCinqueFiltri() {
  const filters = [
    ["Bando", "e' scritto o implicito?", "navy", "softBlue"],
    ["Profilo", "serve alla funzione?", "bordeaux", "softRed"],
    ["Prova", "in quale forma esce?", "gold", "softGold"],
    ["Rischio", "che cosa perdo se lo ignoro?", "green", "softGreen"],
    ["Output", "che cosa so fare dopo?", "teal", "softTeal"]
  ]

  const cards = filters
    .map(([title, body, color, box], index) => filterCard(100 + index * 295, 345, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="235" text-anchor="middle">Il materiale si apre solo dopo la decisione</text>
  ${cards}
  <path class="arrowNavy" d="M310 435 L390 435"/>
  <path class="arrowNavy" d="M605 435 L685 435"/>
  <path class="arrowNavy" d="M900 435 L980 435"/>
  <path class="arrowNavy" d="M1195 435 L1275 435"/>
  ${note(250, 705, 1100, "Se un filtro non passa, il modulo resta in lista: non entra nel calendario.")}`

  return shell(
    "I cinque filtri di scelta",
    "Prima di aprire materiali integrativi, passa da bando, profilo, prova, rischio e output.",
    inner
  )
}

function figureMatriceDecisione() {
  const rows = [
    ["Esplicita + centrale", "Modulo completo", "tributario in agenzia fiscale"],
    ["Esplicita ma marginale", "Modulo essenziale", "inglese solo idoneita"],
    ["Core con taglio specialistico", "Mini-modulo", "contratti per PNRR"],
    ["Errore ricorrente ad alta resa", "Drill modulo", "accesso, termini, competenze"],
    ["Interessante ma fuori prova", "Non attivare", "approfondimento universitario"]
  ]

  const body = rows.map((row, index) => decisionRow(145, 275 + index * 82, 1310, row, index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="230" text-anchor="middle">Segnale del bando -> profondita del modulo -> limite operativo</text>
  <g data-safe-box="145 275 1310 410 8">
    ${body}
  </g>
  ${note(250, 725, 1100, "La matrice serve a scegliere profondita: completo, essenziale, mini, drill o taglio.")}`

  return shell(
    "Matrice di decisione dei moduli",
    "La scelta corretta non e' aprire tutto: e' assegnare profondita e limite.",
    inner
  )
}

function figureAtlanteModuli() {
  const modules = [
    ["Ente locale", "organi, atti, servizi", "navy", "softBlue"],
    ["Amm.-contabile", "bilancio, entrata, spesa", "bordeaux", "softRed"],
    ["Tributario", "accertamento, riscossione", "gold", "softGold"],
    ["Giustizia", "uffici, funzioni, lessico", "green", "softGreen"],
    ["Lavoro e vigilanza", "previdenza, controlli", "teal", "softTeal"],
    ["Tecnico PA", "procedimento + settore", "navy", "softBlue"],
    ["ICT e digitale", "dati, sicurezza, servizi", "bordeaux", "softRed"],
    ["Situazionale", "ruolo, legalita, servizio", "green", "softGreen"]
  ]

  const cards = modules
    .map(([title, body, color, box], index) =>
      moduleCell(110 + (index % 4) * 365, 255 + Math.floor(index / 4) * 225, title, body, color, box)
    )
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Ogni modulo deve finire in quiz, caso, orale, schema o simulazione</text>
  ${cards}
  ${note(250, 812, 1100, "Il modulo non dice: studia tutto. Dice: studia questo per produrre questo.")}`

  return shell(
    "Atlante operativo dei moduli",
    "Ogni modulo deve collegare profilo, materia, prova e prodotto finale.",
    inner
  )
}

function figureSchedaCaso() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Sara ha due concorsi: isola i moduli, non duplica il core</text>
  ${caseBlock(115, 290, 380, "Core comune", ["amministrativo", "pubblico impiego", "privacy e trasparenza", "informatica, inglese", "quiz settimanali"], "navy", "softBlue")}
  ${caseBlock(610, 290, 380, "Modulo Comune", ["TUEL", "atti locali", "contabilita locale", "caso su liquidazione", "limite: 18 sessioni"], "bordeaux", "softRed")}
  ${caseBlock(1105, 290, 380, "Modulo Ministero", ["organizzazione settore", "funzioni centrali", "risposta orale", "quiz su procedimento", "limite: 10 sessioni"], "green", "softGreen")}
  <path class="arrowNavy" d="M505 455 L595 455"/>
  <path class="arrowNavy" d="M1000 455 L1090 455"/>
  ${wideCard(355, 700, 890, "Scheda modulo", ["fonte nel bando, prova collegata, output, tempo massimo", "criterio di sufficienza e cosa non studiare"], "gold", "softGold")}`

  return shell(
    "Scheda modulo e caso Sara",
    "Una decisione buona isola il modulo senza duplicare il nucleo comune.",
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
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/></marker>
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

function columnBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 120 + index * 45}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 350 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="350" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    <path class="thin" d="M${x + 38} ${y + 82} L${x + w - 38} ${y + 82}"/>
    ${rows}
  </g>`
}

function numberedTile(x, y, w, number, title, body, colorClass, boxClass) {
  const titleSize = title.length > 22 ? 18 : 20
  const bodySize = body.length > 38 ? 14 : 15
  return `<g data-safe-box="${x} ${y} ${w} 250 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="250" rx="26"/>
    <circle cx="${x + w / 2}" cy="${y + 55}" r="34" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + w / 2}" y="${y + 66}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 120}" text-anchor="middle" style="font-size:${titleSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + w / 2}" y="${y + 178}" text-anchor="middle" style="font-size:${bodySize}px">${esc(body)}</text>
  </g>`
}

function filterCard(x, y, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 205 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="190" rx="24"/>
    <rect x="${x}" y="${y}" width="205" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 54}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    <path class="thin" d="M${x + 28} ${y + 76} L${x + 177} ${y + 76}"/>
    <text class="muted small" x="${x + 102.5}" y="${y + 122}" text-anchor="middle" style="font-size:15px">${esc(body)}</text>
  </g>`
}

function decisionRow(x, y, w, row, index) {
  const [signal, decision, example] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  const colors = [palette.navy, palette.bordeaux, palette.gold, palette.green, palette.teal]

  return `<g>
    <rect x="${x}" y="${y}" width="${w}" height="68" rx="16" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <circle cx="${x + 38}" cy="${y + 34}" r="14" fill="${colors[index]}"/>
    <text class="navy label" x="${x + 74}" y="${y + 42}" style="font-size:18px">${esc(signal)}</text>
    <text class="bordeaux label" x="${x + 515}" y="${y + 42}" style="font-size:18px">${esc(decision)}</text>
    <text class="muted small" x="${x + 865}" y="${y + 42}" style="font-size:17px">${esc(example)}</text>
  </g>`
}

function moduleCell(x, y, title, body, colorClass, boxClass) {
  const titleSize = title.length > 18 ? 18 : 20
  return `<g data-safe-box="${x} ${y} 300 150 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="300" height="150" rx="23"/>
    <rect x="${x}" y="${y}" width="300" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 150}" y="${y + 47}" text-anchor="middle" style="font-size:${titleSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 30} ${y + 69} L${x + 270} ${y + 69}"/>
    <text class="muted small" x="${x + 150}" y="${y + 109}" text-anchor="middle" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function caseBlock(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 107 + index * 38}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 320 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="320" rx="26"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 55}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    <path class="thin" d="M${x + 35} ${y + 78} L${x + w - 35} ${y + 78}"/>
    ${rows}
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
