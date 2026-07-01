const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-17"
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
    slug: "01-mappa-bando-caso-pratico",
    title: "Mappa BANDO del caso pratico",
    subtitle: "Dal bando alla soluzione: il caso va trasformato in output amministrativo.",
    svg: figureMappa()
  },
  {
    slug: "02-caso-come-fascicolo-amministrativo",
    title: "Il caso non e' una storia",
    subtitle: "Leggi la traccia come un fascicolo: fatti, soggetti, competenza e vincoli.",
    svg: figureFascicolo()
  },
  {
    slug: "03-griglia-otto-domande",
    title: "Griglia in otto domande",
    subtitle: "Una sequenza stabile impedisce risposte generiche e salti logici.",
    svg: figureGriglia()
  },
  {
    slug: "04-schema-risposta-caso-pratico",
    title: "Schema di risposta al caso pratico",
    subtitle: "Fatti, problema, regola, applicazione, soluzione e cautele chiudono il ragionamento.",
    svg: figureSchema()
  },
  {
    slug: "05-nuclei-alto-rendimento",
    title: "Nuclei ad alto rendimento",
    subtitle: "Alcuni snodi sbloccano molti casi: competenza, termini, accesso, dati e tracciabilita.",
    svg: figureNuclei()
  },
  {
    slug: "06-matrice-casi-ricorrenti",
    title: "Matrice dei casi ricorrenti",
    subtitle: "Ogni scenario va letto per problema, vincolo e output operativo.",
    svg: figureMatrice()
  },
  {
    slug: "07-output-diario-casi",
    title: "Output e diario dei casi",
    subtitle: "Quiz, scritto e orale cambiano forma; il diario corregge il modo di decidere.",
    svg: figureDiario()
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
  return `# Asset Capitolo 17

Figure generate per \`Casi pratici e problem solving amministrativo\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-caso-pratico.png\` | Mappa BANDO del caso pratico: bando, aree, nuclei, diario e output. |
| \`02-caso-come-fascicolo-amministrativo.png\` | Trasformazione della traccia narrativa in fascicolo amministrativo ridotto. |
| \`03-griglia-otto-domande.png\` | Griglia di lettura in otto domande per non saltare passaggi. |
| \`04-schema-risposta-caso-pratico.png\` | Sequenza stabile per costruire la risposta al caso. |
| \`05-nuclei-alto-rendimento.png\` | Nuclei ricorrenti che sbloccano molti casi pratici. |
| \`06-matrice-casi-ricorrenti.png\` | Matrice degli scenari tipici e degli output attesi. |
| \`07-output-diario-casi.png\` | Adattamento a quiz, scritto e orale piu ciclo del diario errori. |

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
  ${card(590, 168, 420, 125, "Caso pratico", ["decidere il prossimo", "passo corretto"], "navy", "card")}
  <path class="line" d="M800 293 L800 363"/>
  <path class="line" d="M210 363 L1390 363"/>
  ${connector(210, 363, 210, 450)}
  ${connector(505, 363, 505, 570)}
  ${connector(800, 363, 800, 450)}
  ${connector(1095, 363, 1095, 570)}
  ${connector(1390, 363, 1390, 450)}
  ${card(75, 450, 270, 130, "Bando", ["formato prova", "scenario atteso"], "navy", "softBlue")}
  ${card(370, 570, 270, 130, "Aree", ["procedimento", "accesso, dati"], "bordeaux", "softRed")}
  ${card(665, 450, 270, 130, "Nuclei", ["competenza", "vincoli, termini"], "gold", "softGold")}
  ${card(960, 570, 270, 130, "Diario", ["errore tipo", "correzione"], "green", "softGreen")}
  ${card(1255, 450, 270, 130, "Output", ["soluzione", "atto o risposta"], "teal", "softTeal")}
  ${note(250, 792, 1100, "Il caso pratico non chiede tutta la teoria: chiede un'azione corretta, motivata e tracciabile.")}
`
  return shell(
    "Mappa BANDO del caso pratico",
    "Dal bando alla soluzione: il caso va trasformato in output amministrativo.",
    inner
  )
}

function figureFascicolo() {
  const inner = `
  <rect class="card" x="80" y="165" width="1440" height="630" rx="30"/>
  ${listCard(145, 255, 390, "Traccia narrativa", ["dettagli descrittivi", "richieste implicite", "emozioni del caso", "dati secondari"], "bordeaux", "softRed")}
  ${card(620, 340, 360, 155, "Separare", ["cio che serve", "da cio che distrae"], "gold", "softGold")}
  ${listCard(1065, 255, 390, "Fascicolo operativo", ["fatti essenziali", "soggetti e ufficio", "procedimento", "regola, vincoli, output"], "green", "softGreen")}
  <path class="arrowBordeaux" d="M545 350 L610 390"/>
  <path class="arrowGold" d="M990 390 L1055 350"/>
  ${mini(205, 650, 260, "Rischio", "frasi generiche", palette.bordeaux)}
  ${mini(670, 650, 260, "Metodo", "griglia stabile", palette.navy)}
  ${mini(1135, 650, 260, "Risultato", "prossimo passo", palette.green)}
  ${note(250, 812, 1100, "Se non estrai i dati del fascicolo, finisci per raccontare il caso invece di risolverlo.")}
`
  return shell(
    "Il caso non e' una storia",
    "Leggi la traccia come un fascicolo: fatti, soggetti, competenza e vincoli.",
    inner
  )
}

function figureGriglia() {
  const items = [
    ["1", "Richiesta", "che cosa vuole la traccia?", "navy", "softBlue"],
    ["2", "Fatti", "quali dati sono essenziali?", "bordeaux", "softRed"],
    ["3", "Soggetti", "chi chiede e chi decide?", "gold", "softGold"],
    ["4", "Competenza", "qual e' l'ufficio giusto?", "green", "softGreen"],
    ["5", "Nucleo", "quale materia sblocca?", "teal", "softTeal"],
    ["6", "Vincoli", "termini, dati, risorse?", "navy", "softBlue"],
    ["7", "Soluzione", "azione legittima e possibile", "bordeaux", "softRed"],
    ["8", "Output", "comunicazione o atto finale", "green", "softGreen"]
  ]
  const tiles = items
    .map(([num, title, body, color, box], index) => {
      const col = index % 4
      const row = Math.floor(index / 4)
      return numberTile(110 + col * 370, 220 + row * 245, 320, num, title, body, color, box)
    })
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${tiles}
  ${note(250, 812, 1100, "La griglia vale per scritto, orale e quiz: cambia solo la forma dell'output.")}
`
  return shell(
    "Griglia in otto domande",
    "Una sequenza stabile impedisce risposte generiche e salti logici.",
    inner
  )
}

function figureSchema() {
  const inner = `
  <rect class="card" x="80" y="165" width="1440" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Dalla traccia alla soluzione motivata</text>
  ${stepCard(115, 330, "1", "Fatti", ["riassumi", "senza divagare"], "navy", "softBlue")}
  ${stepCard(350, 330, "2", "Problema", ["individua", "il nodo"], "bordeaux", "softRed")}
  ${stepCard(585, 330, "3", "Regola", ["principio", "pertinente"], "gold", "softGold")}
  ${stepCard(820, 330, "4", "Applicazione", ["porta la regola", "nel caso"], "green", "softGreen")}
  ${stepCard(1055, 330, "5", "Soluzione", ["azione", "concreta"], "teal", "softTeal")}
  ${stepCard(1290, 330, "6", "Cautele", ["termini, dati", "traccia"], "navy", "softBlue")}
  <path class="arrowNavy" d="M320 425 L340 425"/>
  <path class="arrowBordeaux" d="M555 425 L575 425"/>
  <path class="arrowGold" d="M790 425 L810 425"/>
  <path class="arrowGreen" d="M1025 425 L1045 425"/>
  <path class="arrowTeal" d="M1260 425 L1280 425"/>
  ${mini(310, 650, 330, "Apertura forte", "il caso riguarda...", palette.green)}
  ${mini(960, 650, 330, "Apertura debole", "la PA deve rispettare la legge", palette.bordeaux)}
  ${note(250, 812, 1100, "Una risposta forte applica poca teoria pertinente, non molta teoria scollegata.")}
`
  return shell(
    "Schema di risposta al caso pratico",
    "Fatti, problema, regola, applicazione, soluzione e cautele chiudono il ragionamento.",
    inner
  )
}

function figureNuclei() {
  const items = [
    ["Competenza", "chi deve agire", "navy", "softBlue"],
    ["Responsabile", "istruttoria e tempi", "bordeaux", "softRed"],
    ["Termini", "gestione del tempo", "gold", "softGold"],
    ["Motivazione", "perche si decide", "green", "softGreen"],
    ["Accesso", "documenti e terzi", "teal", "softTeal"],
    ["Privacy", "dati e limiti", "navy", "softBlue"],
    ["Trasparenza", "pubblicita non totale", "bordeaux", "softRed"],
    ["Comportamento", "doveri e rischi", "gold", "softGold"],
    ["Contratti", "RUP e tracciabilita", "green", "softGreen"],
    ["Riesame", "errore e autotutela", "teal", "softTeal"]
  ]
  const cells = items
    .map(([title, body, color, box], index) => {
      const col = index % 5
      const row = Math.floor(index / 5)
      return compactCell(95 + col * 292, 285 + row * 180, 238, title, body, color, box)
    })
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="230" text-anchor="middle">Studia prima gli snodi che tornano in scenari diversi</text>
  ${cells}
  ${note(250, 812, 1100, "Il nucleo giusto trasforma una traccia confusa in una sequenza amministrativa leggibile.")}
`
  return shell(
    "Nuclei ad alto rendimento",
    "Alcuni snodi sbloccano molti casi: competenza, termini, accesso, dati e tracciabilita.",
    inner
  )
}

function figureMatrice() {
  const items = [
    ["Istanza incompleta", "integrazione e traccia", "navy", "softBlue"],
    ["Accesso con dati", "bilancia e oscura", "bordeaux", "softRed"],
    ["Ritardo pratica", "verifica e comunica", "gold", "softGold"],
    ["Sportello sbagliato", "orienta al canale", "green", "softGreen"],
    ["Graduatoria", "canali tracciati", "teal", "softTeal"],
    ["Ufficio non competente", "inoltra senza inerzia", "navy", "softBlue"],
    ["Acquisto urgente", "procedura proporzionata", "bordeaux", "softRed"],
    ["Riesame", "qualifica la richiesta", "green", "softGreen"]
  ]
  const cells = items
    .map(([title, body, color, box], index) => {
      const col = index % 4
      const row = Math.floor(index / 4)
      return caseCell(115 + col * 370, 260 + row * 225, 315, title, body, color, box)
    })
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Scenario tipico, vincolo dominante, output atteso</text>
  ${cells}
  ${note(250, 812, 1100, "Il caso cambia superficie, ma la domanda vera resta: quale passaggio corretto deve compiere la PA?")}
`
  return shell(
    "Matrice dei casi ricorrenti",
    "Ogni scenario va letto per problema, vincolo e output operativo.",
    inner
  )
}

function figureDiario() {
  const inner = `
  <rect class="card" x="80" y="165" width="1440" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Stesso ragionamento, tre forme di prova</text>
  ${processCard(145, 310, 300, "Quiz", ["scegli opzione", "escludi scorciatoie"], "navy", "softBlue")}
  ${processCard(650, 310, 300, "Scritto", ["argomenta", "in 12-15 righe"], "bordeaux", "softRed")}
  ${processCard(1155, 310, 300, "Orale", ["spiega", "ragionamento"], "gold", "softGold")}
  <path class="arrowNavy" d="M460 390 L635 390"/>
  <path class="arrowBordeaux" d="M965 390 L1140 390"/>
  <path class="dash" d="M170 555 L1430 555"/>
  ${mini(165, 620, 230, "Fatti", "ho capito il caso?", palette.navy)}
  ${mini(425, 620, 230, "Competenza", "chi agisce?", palette.bordeaux)}
  ${mini(685, 620, 230, "Regola", "principio giusto?", palette.gold)}
  ${mini(945, 620, 230, "Output", "azione concreta?", palette.green)}
  ${mini(1205, 620, 230, "Tempo", "partenza rapida?", palette.teal)}
  ${note(250, 812, 1100, "Nel diario non scrivere solo 'sbagliato': classifica l'errore e correggi il passaggio.")}
`
  return shell(
    "Output e diario dei casi",
    "Quiz, scritto e orale cambiano forma; il diario corregge il modo di decidere.",
    inner
  )
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleFontSize = title.length > 26 ? 18 : title.length > 19 ? 20 : title.length > 14 ? 22 : 25
  const bodyFontSize = lines.some((line) => line.length > 24) ? 16 : 18
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

function listCard(x, y, w, title, lines, colorClass, boxClass) {
  const rowHeight = 31
  const h = 88 + lines.length * rowHeight
  const titleFontSize = title.length > 22 ? 19 : title.length > 16 ? 21 : 24
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 30}" y="${y + 80 + index * rowHeight}" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 24} ${y + 60} L${x + w - 24} ${y + 60}"/>
    ${body}
  </g>`
}

function numberTile(x, y, w, number, title, body, colorClass, boxClass) {
  const titleFontSize = title.length > 16 ? 18 : 21
  const bodyFontSize = body.length > 30 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 150 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="150" rx="22"/>
    <circle cx="${x + 42}" cy="${y + 45}" r="27" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 42}" y="${y + 54}" text-anchor="middle" fill="#FFFFFF" style="font-size:24px">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 180}" y="${y + 46}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + 180}" y="${y + 88}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function stepCard(x, y, number, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 102}" y="${y + 92 + index * 27}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 205 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="190" rx="24"/>
    <circle cx="${x + 102.5}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 102.5}" y="${y + 51}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 78}" text-anchor="middle" style="font-size:18px">${esc(title)}</text>
    ${body}
  </g>`
}

function compactCell(x, y, w, title, body, colorClass, boxClass) {
  const titleFontSize = title.length > 16 ? 17 : title.length > 12 ? 18 : 20
  const bodyFontSize = body.length > 24 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 124 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="124" rx="20"/>
    <rect x="${x}" y="${y}" width="${w}" height="9" rx="4.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 43}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + w / 2}" y="${y + 78}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function caseCell(x, y, w, title, body, colorClass, boxClass) {
  const titleFontSize = title.length > 21 ? 16 : title.length > 16 ? 18 : 20
  const bodyFontSize = body.length > 24 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 155 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="155" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 45}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 28} ${y + 72} L${x + w - 28} ${y + 72}"/>
    <text class="muted small" x="${x + w / 2}" y="${y + 112}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function processCard(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 82 + index * 28}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 170 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="170" rx="22"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 45}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    ${body}
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
  const fontSize = text.length > 104 ? 18 : text.length > 88 ? 19 : 20

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
