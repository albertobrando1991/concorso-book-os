const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-15"
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
    slug: "01-mappa-operativa-scritto",
    title: "Mappa operativa dello scritto",
    subtitle: "La prova scritta trasforma traccia, nuclei e tempo in una risposta pertinente.",
    svg: figureMappa()
  },
  {
    slug: "02-formati-prova-scritta",
    title: "Formati da riconoscere",
    subtitle: "Quesito sintetico, elaborato, caso e prova mista richiedono output diversi.",
    svg: figureFormati()
  },
  {
    slug: "03-lettura-traccia",
    title: "Lettura della traccia",
    subtitle: "Prima di scrivere, isola verbo, materia, soggetti, vincoli e output richiesto.",
    svg: figureTraccia()
  },
  {
    slug: "04-schema-risposta-concorsuale",
    title: "Schema della risposta concorsuale",
    subtitle: "Definizione, riferimento, funzione, applicazione e conclusione danno ordine.",
    svg: figureSchemaRisposta()
  },
  {
    slug: "05-risposte-10-20-30-righe",
    title: "Risposte in 10, 20 e 30 righe",
    subtitle: "La lunghezza cambia selezione, sviluppo e chiusura della risposta.",
    svg: figureLunghezze()
  },
  {
    slug: "06-caso-teorico-pratico",
    title: "Caso teorico-pratico",
    subtitle: "Dal fatto alla soluzione: soggetti, problema, regola, applicazione e cautele.",
    svg: figureCaso()
  },
  {
    slug: "07-tempo-diario-scritto",
    title: "Tempo, revisione e diario dello scritto",
    subtitle: "La simulazione vale se corregge pertinenza, struttura, lessico e gestione tempo.",
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
  return `# Asset Capitolo 15

Figure generate per \`La prova scritta e teorico-pratica\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-operativa-scritto.png\` | Mappa generale: bando, formati, traccia, schema risposta, diario e output. |
| \`02-formati-prova-scritta.png\` | Distinzione tra risposta sintetica, domanda teorica, elaborato, caso e prova mista. |
| \`03-lettura-traccia.png\` | Checklist visiva per leggere la traccia prima di scrivere. |
| \`04-schema-risposta-concorsuale.png\` | Sequenza definizione, riferimento, funzione, applicazione e conclusione. |
| \`05-risposte-10-20-30-righe.png\` | Strategia diversa per risposte brevi, medie e sviluppate. |
| \`06-caso-teorico-pratico.png\` | Metodo per trasformare un caso in soluzione ordinata. |
| \`07-tempo-diario-scritto.png\` | Distribuzione del tempo e diario di correzione dello scritto. |

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
  ${card(570, 170, 460, 125, "Risposta scritta", ["pertinenza e ordine", "tempo e revisione"], "navy", "card")}
  <path class="line" d="M800 295 L800 365"/>
  <path class="line" d="M210 365 L1390 365"/>
  ${connector(210, 365, 210, 450)}
  ${connector(505, 365, 505, 570)}
  ${connector(800, 365, 800, 450)}
  ${connector(1095, 365, 1095, 570)}
  ${connector(1390, 365, 1390, 450)}
  ${card(75, 450, 270, 130, "Bando", ["formato, durata", "criteri, strumenti"], "navy", "softBlue")}
  ${card(370, 570, 270, 130, "Formati", ["sintetica", "elaborato, caso"], "bordeaux", "softRed")}
  ${card(665, 450, 270, 130, "Traccia", ["verbo, materia", "vincoli e output"], "gold", "softGold")}
  ${card(960, 570, 270, 130, "Diario", ["pertinenza", "struttura, lessico"], "green", "softGreen")}
  ${card(1255, 450, 270, 130, "Output", ["scaletta", "risposta corretta"], "teal", "softTeal")}
  ${note(250, 792, 1100, "Lo scritto non premia chi scrive tutto: premia chi risponde alla traccia con ordine.")}
`
  return shell(
    "Mappa operativa dello scritto",
    "La prova scritta trasforma traccia, nuclei e tempo in una risposta pertinente.",
    inner
  )
}

function figureFormati() {
  const inner = `
  <rect class="card" x="85" y="165" width="1430" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Ogni formato misura un output diverso</text>
  ${listCard(115, 305, 300, "Risposta sintetica", ["nozione precisa", "punti essenziali", "spazio stretto"], "navy", "softBlue")}
  ${listCard(465, 305, 300, "Domanda teorica", ["istituto", "principi", "conseguenze"], "bordeaux", "softRed")}
  ${listCard(815, 305, 300, "Elaborato breve", ["scaletta", "paragrafi", "chiusura"], "gold", "softGold")}
  ${listCard(1165, 305, 300, "Caso pratico", ["fatti", "regola", "soluzione"], "green", "softGreen")}
  ${mini(300, 640, 330, "Teorico-pratica", "spiega la regola e usala", palette.teal)}
  ${mini(760, 640, 330, "Prova mista", "separa tempi e parti", palette.navy)}
  ${note(250, 812, 1100, "Errore da evitare: preparare un caso pratico come se fosse una domanda solo teorica.")}
`
  return shell(
    "Formati da riconoscere",
    "Quesito sintetico, elaborato, caso e prova mista richiedono output diversi.",
    inner
  )
}

function figureTraccia() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">La traccia e' un bando in miniatura</text>
  <rect class="note" x="260" y="295" width="1080" height="120" rx="24"/>
  <text class="ink body" x="800" y="345" text-anchor="middle" style="font-size:24px;font-weight:800">"Indicare come dovrebbe comportarsi l'amministrazione..."</text>
  <text class="muted small" x="800" y="382" text-anchor="middle">Prima leggi i vincoli, poi costruisci la risposta.</text>
  ${smallTag(145, 505, 185, "Verbo", "che cosa fare", palette.navy)}
  ${smallTag(360, 505, 185, "Materia", "ambito", palette.bordeaux)}
  ${smallTag(575, 505, 185, "Istituto", "nucleo", palette.gold)}
  ${smallTag(790, 505, 185, "Soggetti", "chi agisce", palette.green)}
  ${smallTag(1005, 505, 185, "Vincoli", "righe e tempo", palette.teal)}
  ${smallTag(1220, 505, 185, "Output", "risposta attesa", palette.navy)}
  <path class="arrowNavy" d="M237 505 L250 430"/>
  <path class="arrowBordeaux" d="M452 505 L500 430"/>
  <path class="arrowGold" d="M667 505 L705 430"/>
  <path class="arrowGreen" d="M882 505 L900 430"/>
  <path class="arrowTeal" d="M1097 505 L1095 430"/>
  <path class="arrowNavy" d="M1312 505 L1240 430"/>
  ${note(250, 812, 1100, "Se il verbo e' confrontare, una definizione lunga non basta; se e' applicare, serve soluzione.")}
`
  return shell(
    "Lettura della traccia",
    "Prima di scrivere, isola verbo, materia, soggetti, vincoli e output richiesto.",
    inner
  )
}

function figureSchemaRisposta() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Una risposta concorsuale ha una sequenza riconoscibile</text>
  ${stepCard(130, 330, "1", "Definizione", ["che cos'e", "nucleo"], "navy", "softBlue")}
  ${stepCard(420, 330, "2", "Riferimento", ["fonte sicura", "principio"], "bordeaux", "softRed")}
  ${stepCard(710, 330, "3", "Funzione", ["a cosa serve", "perche conta"], "gold", "softGold")}
  ${stepCard(1000, 330, "4", "Applicazione", ["esempio", "caso"], "green", "softGreen")}
  ${stepCard(1290, 330, "5", "Conclusione", ["torna alla", "traccia"], "teal", "softTeal")}
  <path class="arrowNavy" d="M380 425 L410 425"/>
  <path class="arrowBordeaux" d="M670 425 L700 425"/>
  <path class="arrowGold" d="M960 425 L990 425"/>
  <path class="arrowGreen" d="M1250 425 L1280 425"/>
  ${mini(455, 640, 300, "No articoli incerti", "meglio principio sicuro", palette.bordeaux)}
  ${mini(845, 640, 300, "No riassunto", "rispondi alla domanda", palette.green)}
  ${note(250, 812, 1100, "La risposta non deve dire tutto: deve dire cio che serve, nell'ordine giusto.")}
`
  return shell(
    "Schema della risposta concorsuale",
    "Definizione, riferimento, funzione, applicazione e conclusione danno ordine.",
    inner
  )
}

function figureLunghezze() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Lo spazio disponibile decide quanta selezione serve</text>
  ${columnCard(170, 310, 330, 315, "10 righe", ["definizione", "due punti chiave", "chiusura secca"], "navy", "softBlue")}
  ${columnCard(635, 270, 330, 395, "20 righe", ["definizione", "funzione", "elementi", "esempio breve"], "gold", "softGold")}
  ${columnCard(1100, 230, 330, 475, "30 righe", ["inquadramento", "sviluppo", "confronto o caso", "conclusione"], "green", "softGreen")}
  <path class="dash" d="M230 720 L1370 720"/>
  ${note(250, 812, 1100, "Se non sai scriverla in 10 righe, non hai ancora isolato il nucleo della risposta.")}
`
  return shell(
    "Risposte in 10, 20 e 30 righe",
    "La lunghezza cambia selezione, sviluppo e chiusura della risposta.",
    inner
  )
}

function figureCaso() {
  const inner = `
  <rect class="card" x="80" y="165" width="1440" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Il caso chiede comportamento motivato, non teoria riversata</text>
  ${processCard(110, 330, 190, "Fatti", ["che cosa", "accade"], "navy", "softBlue")}
  ${processCard(335, 330, 190, "Problema", ["punto da", "risolvere"], "bordeaux", "softRed")}
  ${processCard(560, 330, 190, "Soggetti", ["chi agisce", "chi riceve"], "gold", "softGold")}
  ${processCard(785, 330, 190, "Regola", ["principio", "sicuro"], "green", "softGreen")}
  ${processCard(1010, 330, 190, "Applica", ["regola al", "caso"], "teal", "softTeal")}
  ${processCard(1235, 330, 230, "Soluzione", ["esito", "cautele"], "navy", "softBlue")}
  <path class="arrowNavy" d="M310 410 L325 410"/>
  <path class="arrowBordeaux" d="M535 410 L550 410"/>
  <path class="arrowGold" d="M760 410 L775 410"/>
  <path class="arrowGreen" d="M985 410 L1000 410"/>
  <path class="arrowTeal" d="M1210 410 L1225 410"/>
  ${listCard(230, 620, 460, "Prima di scrivere", ["non aprire tutto il manuale", "leggi soggetti e problema", "decidi l'output"], "bordeaux", "softRed")}
  ${listCard(910, 620, 460, "Risposta attesa", ["comportamento dell'ufficio", "motivazione sintetica", "conclusione operativa"], "green", "softGreen")}
`
  return shell(
    "Caso teorico-pratico",
    "Dal fatto alla soluzione: soggetti, problema, regola, applicazione e cautele.",
    inner
  )
}

function figureDiario() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Una prova scritta si migliora correggendo il processo</text>
  ${timeBlock(145, 330, 245, "5-10%", "Lettura", "tracce e vincoli", "navy", "softBlue")}
  ${timeBlock(440, 330, 245, "10%", "Scaletta", "ordine prima", "bordeaux", "softRed")}
  ${timeBlock(735, 330, 245, "70-75%", "Scrittura", "risposta proporzionata", "gold", "softGold")}
  ${timeBlock(1030, 330, 245, "10%", "Revisione", "forma e pertinenza", "green", "softGreen")}
  <path class="arrowNavy" d="M405 410 L430 410"/>
  <path class="arrowBordeaux" d="M700 410 L725 410"/>
  <path class="arrowGold" d="M995 410 L1020 410"/>
  ${mini(205, 635, 200, "Pertinenza", "traccia", palette.navy)}
  ${mini(455, 635, 200, "Struttura", "inizio-sviluppo", palette.bordeaux)}
  ${mini(705, 635, 200, "Completezza", "essenziali", palette.gold)}
  ${mini(955, 635, 200, "Lessico", "termini corretti", palette.green)}
  ${mini(1205, 635, 200, "Tempo", "limite", palette.teal)}
  ${note(250, 812, 1100, "Non correggere solo cosa sai: correggi come costruisci la risposta.")}
`
  return shell(
    "Tempo, revisione e diario dello scritto",
    "La simulazione vale se corregge pertinenza, struttura, lessico e gestione tempo.",
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
    .map((line, index) => `<text class="muted small" x="${x + 125}" y="${y + 92 + index * 27}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 250 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="250" height="190" rx="24"/>
    <circle cx="${x + 125}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 125}" y="${y + 51}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 125}" y="${y + 78}" text-anchor="middle" style="font-size:20px">${esc(title)}</text>
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

function columnCard(x, y, w, h, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 120 + index * 44}" text-anchor="middle" style="font-size:20px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="12" rx="6" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" style="font-size:31px">${esc(title)}</text>
    <path class="thin" d="M${x + 36} ${y + 85} L${x + w - 36} ${y + 85}"/>
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
