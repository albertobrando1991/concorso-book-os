const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-16"
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
    slug: "01-mappa-operativa-prova-orale",
    title: "Mappa operativa della prova orale",
    subtitle: "L'orale trasforma studio, esempi e simulazioni in esposizione stabile.",
    svg: figureMappa()
  },
  {
    slug: "02-scheda-orale-bando",
    title: "Scheda orale del bando",
    subtitle: "Prima di parlare, delimita materie, prove accessorie, criteri e vincoli.",
    svg: figureScheda()
  },
  {
    slug: "03-struttura-universale-risposta-orale",
    title: "Struttura universale della risposta orale",
    subtitle: "Apertura, definizione, funzione, riferimento, esempio e chiusura danno ordine.",
    svg: figureStruttura()
  },
  {
    slug: "04-risposta-due-minuti",
    title: "Risposta orale in due minuti",
    subtitle: "Il timer obbliga a selezionare il nucleo e a chiudere senza dispersione.",
    svg: figureDueMinuti()
  },
  {
    slug: "05-collegamenti-domande-incrociate",
    title: "Collegamenti e domande incrociate",
    subtitle: "La commissione puo spostare il fuoco: rispondi al punto e apri un ponte breve.",
    svg: figureCollegamenti()
  },
  {
    slug: "06-domande-simulazioni-progressive",
    title: "Domande e simulazioni progressive",
    subtitle: "Ogni nucleo diventa domanda base, confronto, applicazione e colloquio misto.",
    svg: figureSimulazioni()
  },
  {
    slug: "07-diario-ultimi-sette-giorni",
    title: "Diario orale e ultimi sette giorni",
    subtitle: "Correggi durata, chiarezza, esempi e logistica prima della prova.",
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
  return `# Asset Capitolo 16

Figure generate per \`La prova orale\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-operativa-prova-orale.png\` | Mappa generale della preparazione orale secondo BANDO. |
| \`02-scheda-orale-bando.png\` | Checklist visiva per estrarre dal bando materie, prove accessorie e criteri. |
| \`03-struttura-universale-risposta-orale.png\` | Sequenza di risposta: apertura, definizione, funzione, riferimento, esempio e chiusura. |
| \`04-risposta-due-minuti.png\` | Distribuzione temporale della risposta orale da 120 secondi. |
| \`05-collegamenti-domande-incrociate.png\` | Gestione di collegamenti, esempi, distinzioni e follow-up della commissione. |
| \`06-domande-simulazioni-progressive.png\` | Trasformazione dei nuclei in domande e simulazioni progressive. |
| \`07-diario-ultimi-sette-giorni.png\` | Ciclo diario-correzione e programma finale dell'ultima settimana. |

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
  ${card(570, 170, 460, 125, "Esposizione orale", ["ordine, ritmo", "esempi e recupero"], "navy", "card")}
  <path class="line" d="M800 295 L800 365"/>
  <path class="line" d="M210 365 L1390 365"/>
  ${connector(210, 365, 210, 450)}
  ${connector(505, 365, 505, 570)}
  ${connector(800, 365, 800, 450)}
  ${connector(1095, 365, 1095, 570)}
  ${connector(1390, 365, 1390, 450)}
  ${card(75, 450, 270, 130, "Bando", ["materie, lingua", "criteri e soglie"], "navy", "softBlue")}
  ${card(370, 570, 270, 130, "Aree", ["comuni e", "specifiche"], "bordeaux", "softRed")}
  ${card(665, 450, 270, 130, "Nuclei", ["definizioni", "confronti, casi"], "gold", "softGold")}
  ${card(960, 570, 270, 130, "Diario", ["esitazioni", "lessico, durata"], "green", "softGreen")}
  ${card(1255, 450, 270, 130, "Output", ["risposte a voce", "simulazioni"], "teal", "softTeal")}
  ${note(250, 792, 1100, "L'orale non premia il discorso lungo: premia risposta, collegamento e chiusura.")}
`
  return shell(
    "Mappa operativa della prova orale",
    "L'orale trasforma studio, esempi e simulazioni in esposizione stabile.",
    inner
  )
}

function figureScheda() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">La scheda orale delimita il colloquio prima dello studio</text>
  ${listCard(135, 310, 310, "Perimetro", ["materie orali", "profilo specifico", "durata indicativa"], "navy", "softBlue")}
  ${listCard(495, 310, 310, "Prove accessorie", ["inglese", "informatica", "documenti"], "bordeaux", "softRed")}
  ${listCard(855, 310, 310, "Valutazione", ["criteri", "soglia minima", "commissione"], "gold", "softGold")}
  ${listCard(1215, 310, 250, "Rischi", ["materie deboli", "lacune", "logistica"], "green", "softGreen")}
  <path class="dash" d="M170 610 L1430 610"/>
  ${mini(250, 660, 300, "Da verificare", "non affidarti alla memoria", palette.bordeaux)}
  ${mini(650, 660, 300, "Da allenare", "domande e simulazioni", palette.green)}
  ${mini(1050, 660, 300, "Da portare", "documenti e avvisi", palette.teal)}
  ${note(250, 812, 1100, "Il bando decide il perimetro: lingua, informatica, materie e criteri non sono dettagli.")}
`
  return shell(
    "Scheda orale del bando",
    "Prima di parlare, delimita materie, prove accessorie, criteri e vincoli.",
    inner
  )
}

function figureStruttura() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Una risposta orale efficace segue una sequenza flessibile</text>
  ${stepCard(110, 330, "1", "Apertura", ["inquadra", "la domanda"], "navy", "softBlue")}
  ${stepCard(345, 330, "2", "Definizione", ["spiega", "il concetto"], "bordeaux", "softRed")}
  ${stepCard(580, 330, "3", "Funzione", ["a cosa serve", "perche conta"], "gold", "softGold")}
  ${stepCard(815, 330, "4", "Riferimento", ["solo se", "sicuro"], "green", "softGreen")}
  ${stepCard(1050, 330, "5", "Esempio", ["applica", "o collega"], "teal", "softTeal")}
  ${stepCard(1285, 330, "6", "Chiusura", ["torna alla", "domanda"], "navy", "softBlue")}
  <path class="arrowNavy" d="M315 425 L335 425"/>
  <path class="arrowBordeaux" d="M550 425 L570 425"/>
  <path class="arrowGold" d="M785 425 L805 425"/>
  <path class="arrowGreen" d="M1020 425 L1040 425"/>
  <path class="arrowTeal" d="M1255 425 L1275 425"/>
  ${mini(410, 650, 320, "No discorso imparato", "struttura flessibile", palette.bordeaux)}
  ${mini(870, 650, 320, "No citazioni incerte", "principio prima del numero", palette.green)}
  ${note(250, 812, 1100, "La risposta orale deve partire dalla domanda, non dal capitolo studiato.")}
`
  return shell(
    "Struttura universale della risposta orale",
    "Apertura, definizione, funzione, riferimento, esempio e chiusura danno ordine.",
    inner
  )
}

function figureDueMinuti() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Centoventi secondi bastano per una risposta completa e proporzionata</text>
  ${timeBlock(145, 320, 260, "0-20 s", "Inquadra", "domanda e definizione", "navy", "softBlue")}
  ${timeBlock(455, 320, 260, "20-60 s", "Sviluppa", "elementi principali", "bordeaux", "softRed")}
  ${timeBlock(765, 320, 260, "60-100 s", "Collega", "esempio o ponte", "gold", "softGold")}
  ${timeBlock(1075, 320, 260, "100-120 s", "Chiudi", "risposta al punto", "green", "softGreen")}
  <path class="arrowNavy" d="M420 400 L445 400"/>
  <path class="arrowBordeaux" d="M730 400 L755 400"/>
  <path class="arrowGold" d="M1040 400 L1065 400"/>
  ${listCard(245, 610, 430, "Partenze utili", ["Il tema si inquadra...", "La distinzione principale e...", "Nel caso occorre considerare..."], "navy", "softBlue")}
  ${listCard(925, 610, 430, "Partenze da evitare", ["E' una cosa importante...", "Non ricordo bene...", "Dipende... senza spiegare"], "bordeaux", "softRed")}
  ${note(250, 812, 1100, "Se non riesci a chiudere in due minuti, non hai ancora isolato il nucleo.")}
`
  return shell(
    "Risposta orale in due minuti",
    "Il timer obbliga a selezionare il nucleo e a chiudere senza dispersione.",
    inner
  )
}

function figureCollegamenti() {
  const inner = `
  <rect class="card" x="80" y="165" width="1440" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Il follow-up non rompe la risposta: cambia il punto da servire</text>
  ${card(625, 315, 350, 150, "Domanda principale", ["rispondi prima", "poi apri un ponte"], "navy", "softBlue")}
  ${smallTag(165, 305, 230, "Esempio", "caso semplice", palette.green)}
  ${smallTag(285, 560, 250, "Differenza", "oggetto, funzione, effetti", palette.bordeaux)}
  ${smallTag(675, 610, 250, "Collegamento", "ponte breve", palette.gold)}
  ${smallTag(1065, 560, 250, "Caso nuovo", "applica la regola", palette.teal)}
  ${smallTag(1205, 305, 230, "Precisione", "stringi il punto", palette.navy)}
  <path class="arrowGreen" d="M395 350 L615 370"/>
  <path class="arrowBordeaux" d="M535 600 L650 465"/>
  <path class="arrowGold" d="M800 610 L800 475"/>
  <path class="arrowTeal" d="M1065 600 L950 465"/>
  <path class="arrowNavy" d="M1205 350 L985 370"/>
  ${mini(165, 705, 340, "Formula ponte", "Si collega a..., perche...", palette.teal)}
  ${mini(1085, 705, 340, "Regola di tenuta", "ascolta, rispondi, torna al punto", palette.green)}
  ${note(250, 812, 1100, "Il collegamento non deve diventare fuga: una frase basta se la domanda principale e' servita.")}
`
  return shell(
    "Collegamenti e domande incrociate",
    "La commissione puo spostare il fuoco: rispondi al punto e apri un ponte breve.",
    inner
  )
}

function figureSimulazioni() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Ogni nucleo va trasformato in domande e poi in prestazione</text>
  ${processCard(140, 325, 250, "Domanda base", ["che cos'e", "funzione"], "navy", "softBlue")}
  ${processCard(470, 325, 250, "Confronto", ["differenza", "confini"], "bordeaux", "softRed")}
  ${processCard(800, 325, 250, "Applicazione", ["caso", "soluzione"], "gold", "softGold")}
  ${processCard(1130, 325, 250, "Simulazione", ["materie miste", "follow-up"], "green", "softGreen")}
  <path class="arrowNavy" d="M405 405 L460 405"/>
  <path class="arrowBordeaux" d="M735 405 L790 405"/>
  <path class="arrowGold" d="M1065 405 L1120 405"/>
  <path class="dash" d="M190 590 L1410 590"/>
  ${smallTag(185, 645, 220, "60 secondi", "definizione", palette.navy)}
  ${smallTag(500, 645, 220, "2 minuti", "esempio", palette.bordeaux)}
  ${smallTag(815, 645, 220, "Follow-up", "domanda nuova", palette.gold)}
  ${smallTag(1130, 645, 220, "20-30 min", "colloquio misto", palette.green)}
  ${note(250, 812, 1100, "La prima simulazione deve arrivare presto: parlare rivela lacune che la lettura nasconde.")}
`
  return shell(
    "Domande e simulazioni progressive",
    "Ogni nucleo diventa domanda base, confronto, applicazione e colloquio misto.",
    inner
  )
}

function figureDiario() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Il diario orale trasforma ogni simulazione in correzione mirata</text>
  ${processCard(140, 305, 230, "Simula", ["domanda", "timer"], "navy", "softBlue")}
  ${processCard(445, 305, 230, "Registra", ["durata", "chiarezza"], "bordeaux", "softRed")}
  ${processCard(750, 305, 230, "Classifica", ["problema", "categoria"], "gold", "softGold")}
  ${processCard(1055, 305, 230, "Correggi", ["prossima", "azione"], "green", "softGreen")}
  <path class="arrowNavy" d="M385 385 L435 385"/>
  <path class="arrowBordeaux" d="M690 385 L740 385"/>
  <path class="arrowGold" d="M995 385 L1045 385"/>
  <path class="arrowGreen" d="M1170 465 C1040 570 520 570 255 465"/>
  ${dayCard(155, 630, "-7/-6", "mappa nuclei")}
  ${dayCard(325, 630, "-5", "simulazione")}
  ${dayCard(495, 630, "-4", "definizioni")}
  ${dayCard(665, 630, "-3", "casi e ponti")}
  ${dayCard(835, 630, "-2", "lingua e digitale")}
  ${dayCard(1005, 630, "-1", "logistica")}
  ${dayCard(1175, 630, "prova", "ascolto e calma")}
  ${note(250, 812, 1100, "Negli ultimi sette giorni non aprire nuovi mondi: consolida, simula e arriva lucido.")}
`
  return shell(
    "Diario orale e ultimi sette giorni",
    "Correggi durata, chiarezza, esempi e logistica prima della prova.",
    inner
  )
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleFontSize = title.length > 25 ? 18 : title.length > 19 ? 20 : title.length > 14 ? 22 : 25
  const bodyFontSize = lines.some((line) => line.length > 25) ? 16 : 18
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

function stepCard(x, y, number, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 102}" y="${y + 92 + index * 27}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 205 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="190" rx="24"/>
    <circle cx="${x + 102.5}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 102.5}" y="${y + 51}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 78}" text-anchor="middle" style="font-size:19px">${esc(title)}</text>
    ${body}
  </g>`
}

function processCard(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 78 + index * 27}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 160 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="160" rx="22"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    ${body}
  </g>`
}

function timeBlock(x, y, w, time, title, subtitle, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y - 8} ${w} 153 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="145" rx="20"/>
    <rect x="${x}" y="${y}" width="${w}" height="38" rx="18" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + w / 2}" y="${y + 28}" text-anchor="middle" fill="#FFFFFF" style="font-size:21px">${esc(time)}</text>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 82}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    <text class="muted small" x="${x + w / 2}" y="${y + 113}" text-anchor="middle" style="font-size:16px">${esc(subtitle)}</text>
  </g>`
}

function smallTag(x, y, w, title, body, color) {
  return `<g data-safe-box="${x} ${y} ${w} 98 8">
    <rect x="${x}" y="${y}" width="${w}" height="98" rx="22" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 38}" text-anchor="middle" fill="#FFFFFF" style="font-size:22px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 68}" text-anchor="middle" fill="#FFFFFF" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 21 ? 18 : title.length > 15 ? 19 : 21
  const bodyFontSize = body.length > 30 ? 14 : 16

  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function dayCard(x, y, title, body) {
  return `<g data-safe-box="${x} ${y} 140 78 8">
    <rect class="softTeal" x="${x}" y="${y}" width="140" height="78" rx="18"/>
    <text class="teal label" x="${x + 70}" y="${y + 31}" text-anchor="middle" style="font-size:20px">${esc(title)}</text>
    <text class="muted small" x="${x + 70}" y="${y + 57}" text-anchor="middle" style="font-size:14px">${esc(body)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 102 ? 18 : text.length > 86 ? 19 : 20

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
