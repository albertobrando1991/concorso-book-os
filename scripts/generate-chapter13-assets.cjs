const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-13"
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
    slug: "01-mappa-metodo-studio-bando",
    title: "Metodo di studio per concorsi",
    subtitle: "Il Metodo BANDO trasforma ore, materiali ed errori in una settimana governata.",
    svg: figureMappa()
  },
  {
    slug: "02-dal-bando-alla-scheda-concorso",
    title: "Dal bando alla scheda concorso",
    subtitle: "Prima di pianificare devi estrarre prove, materie, vincoli, tempi e output.",
    svg: figureBandoScheda()
  },
  {
    slug: "03-calendario-inverso",
    title: "Calendario inverso",
    subtitle: "Parti dalla prova e risali a setup, apprendimento, consolidamento e rifinitura.",
    svg: figureCalendario()
  },
  {
    slug: "04-sq3r-nuclei-alta-resa",
    title: "SQ3R per i nuclei ad alta resa",
    subtitle: "La lettura diventa domanda, richiamo e verifica su argomenti che sbloccano il programma.",
    svg: figureSq3r()
  },
  {
    slug: "05-active-recall-ripasso-distribuito",
    title: "Active recall e ripasso distribuito",
    subtitle: "Testarsi presto e tornare sugli errori batte rilettura e sottolineatura passiva.",
    svg: figureRecall()
  },
  {
    slug: "06-blocco-studio-50-minuti",
    title: "Blocco di studio da 50 minuti",
    subtitle: "Ogni sessione deve chiudersi con un output e una decisione per il prossimo passo.",
    svg: figureBlocco()
  },
  {
    slug: "07-diario-output-recupero",
    title: "Diario, output e recupero",
    subtitle: "Gli errori diventano dati: classificazione, drill mirato e scelta di cosa tagliare.",
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
  return `# Asset Capitolo 13

Figure generate per \`Metodo di studio per concorsi\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-metodo-studio-bando.png\` | Mappa generale: bando, aree, nuclei, diario, output e settimana governata. |
| \`02-dal-bando-alla-scheda-concorso.png\` | Routine di estrazione dal bando prima del calendario. |
| \`03-calendario-inverso.png\` | Distribuzione delle fasi dalla data prova verso il setup iniziale. |
| \`04-sq3r-nuclei-alta-resa.png\` | Metodo SQ3R applicato ai nuclei ad alta resa. |
| \`05-active-recall-ripasso-distribuito.png\` | Ciclo richiamo attivo, flashcard e ripassi programmati. |
| \`06-blocco-studio-50-minuti.png\` | Sessione tipo: obiettivo, teoria, richiamo, quiz e diario. |
| \`07-diario-output-recupero.png\` | Uso di errori e output per decidere recupero, drill e tagli. |

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
      .title { font-size: 44px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-size: 23px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 25px; font-weight: 800; }
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
  ${card(565, 175, 470, 135, "Settimana governata", ["tempo reale", "prove e dati"], "navy", "card")}
  <path class="line" d="M800 310 L800 380"/>
  <path class="line" d="M250 380 L1350 380"/>
  ${connector(250, 380, 250, 455)}
  ${connector(525, 380, 525, 575)}
  ${connector(800, 380, 800, 455)}
  ${connector(1075, 380, 1075, 575)}
  ${connector(1350, 380, 1350, 455)}
  ${card(115, 455, 270, 130, "Bando", ["prove, soglie", "materie e tempi"], "navy", "softBlue")}
  ${card(390, 575, 270, 130, "Aree", ["blocchi", "peso e priorita"], "bordeaux", "softRed")}
  ${card(665, 455, 270, 130, "Nuclei", ["alta resa", "domande guida"], "gold", "softGold")}
  ${card(940, 575, 270, 130, "Diario", ["errori", "ripassi"], "green", "softGreen")}
  ${card(1215, 455, 270, 130, "Output", ["quiz, orale", "risposta, caso"], "teal", "softTeal")}
  ${note(250, 795, 1100, "Il piano non misura solo ore: misura output prodotti e errori corretti.")}
`
  return shell("Metodo di studio per concorsi", "Il Metodo BANDO trasforma ore, materiali ed errori in una settimana governata.", inner)
}

function figureBandoScheda() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Prima estrai il perimetro, poi apri manuali e calendari</text>
  ${listCard(125, 310, 300, "Dal bando", ["prove previste", "materie richieste", "punteggi e soglie", "scadenze"], "navy", "softBlue")}
  ${listCard(470, 310, 300, "Vincoli", ["giorni disponibili", "ore reali", "banca dati", "penalita"], "bordeaux", "softRed")}
  ${listCard(815, 310, 300, "Decisioni", ["priorita aree", "fonti minime", "cosa tagliare", "output iniziale"], "gold", "softGold")}
  ${listCard(1160, 310, 300, "Scheda", ["concorso in 1 pagina", "rischi aperti", "prossimo passo", "review bando"], "green", "softGreen")}
  <path class="arrowNavy" d="M435 440 L460 440"/>
  <path class="arrowBordeaux" d="M780 440 L805 440"/>
  <path class="arrowGold" d="M1125 440 L1150 440"/>
  ${mini(220, 675, 330, "Non compilata", "non pianificare", palette.bordeaux)}
  ${mini(615, 675, 330, "Compilata", "inizia il calendario", palette.navy)}
  ${mini(1010, 675, 330, "Da verificare", "segnalo nel diario", palette.green)}
  ${note(250, 805, 1100, "Se una riga della scheda resta vuota, quello e' il primo compito di studio.")}
`
  return shell("Dal bando alla scheda concorso", "Prima di pianificare devi estrarre prove, materie, vincoli, tempi e output.", inner)
}

function figureCalendario() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">La data prova decide il ritmo delle fasi</text>
  <path class="line" d="M190 405 L1410 405"/>
  ${timelinePoint(230, 405, "Setup", "bando, fonti", palette.navy)}
  ${timelinePoint(520, 405, "Base", "lettura attiva", palette.bordeaux)}
  ${timelinePoint(815, 405, "Consolida", "quiz e recall", palette.gold)}
  ${timelinePoint(1110, 405, "Rifinisci", "simulazioni", palette.green)}
  ${timelinePoint(1390, 405, "Prova", "output reale", palette.teal)}
  ${card(130, 560, 290, 125, "10-15%", ["setup", "perimetro e materiali"], "navy", "softBlue")}
  ${card(455, 560, 290, 125, "40-45%", ["apprendimento", "nuclei base"], "bordeaux", "softRed")}
  ${card(780, 560, 290, 125, "25-30%", ["consolidamento", "test e ripasso"], "gold", "softGold")}
  ${card(1105, 560, 290, 125, "15-20%", ["rifinitura", "simulazioni e tagli"], "green", "softGreen")}
  ${note(250, 805, 1100, "Errore da evitare: leggere fino all'ultimo giorno e simulare troppo tardi.")}
`
  return shell("Calendario inverso", "Parti dalla prova e risali a setup, apprendimento, consolidamento e rifinitura.", inner)
}

function figureSq3r() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Ogni nucleo deve diventare domanda e verifica</text>
  ${stepCard(140, 315, ["1", "Survey", "scorri titoli"], 240, "navy")}
  ${stepCard(420, 315, ["2", "Question", "trasforma in domande"], 240, "bordeaux")}
  ${stepCard(700, 315, ["3", "Read", "cerca risposte"], 240, "gold")}
  ${stepCard(980, 315, ["4", "Recite", "spiega senza testo"], 240, "green")}
  ${stepCard(1260, 315, ["5", "Review", "quiz e correzione"], 240, "teal")}
  <path class="arrowNavy" d="M385 395 L410 395"/>
  <path class="arrowBordeaux" d="M665 395 L690 395"/>
  <path class="arrowGold" d="M945 395 L970 395"/>
  <path class="arrowGreen" d="M1225 395 L1250 395"/>
  ${listCard(190, 600, 430, "Nucleo ad alta resa", ["ritorna nei quiz", "collega piu materie", "serve all'orale"], "navy", "softBlue")}
  ${listCard(790, 600, 430, "Output minimo", ["5 domande", "risposta breve", "errore classificato"], "green", "softGreen")}
  ${note(250, 805, 1100, "Capire mentre leggi non basta: devi recuperare e spiegare senza guardare.")}
`
  return shell("SQ3R per i nuclei ad alta resa", "La lettura diventa domanda, richiamo e verifica su argomenti che sbloccano il programma.", inner)
}

function figureRecall() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Il test costruisce apprendimento, non misura soltanto</text>
  ${circleStep(300, 390, "1", "Leggi", "blocco breve", palette.navy)}
  ${circleStep(570, 390, "2", "Richiama", "senza testo", palette.bordeaux)}
  ${circleStep(840, 390, "3", "Controlla", "correggi", palette.gold)}
  ${circleStep(1110, 390, "4", "Flashcard", "domanda utile", palette.green)}
  ${circleStep(1370, 390, "5", "Ripassa", "prima che sfugga", palette.teal)}
  <path class="arrowNavy" d="M400 390 L500 390"/>
  <path class="arrowBordeaux" d="M670 390 L770 390"/>
  <path class="arrowGold" d="M940 390 L1040 390"/>
  <path class="arrowGreen" d="M1210 390 L1300 390"/>
  <path class="dash" d="M1370 500 C1210 650 520 660 300 505"/>
  ${mini(230, 640, 180, "D0", "subito", palette.navy)}
  ${mini(455, 640, 180, "D1", "domani", palette.bordeaux)}
  ${mini(680, 640, 180, "D3", "breve", palette.gold)}
  ${mini(905, 640, 180, "D7", "settimana", palette.green)}
  ${mini(1130, 640, 180, "D14", "stabile", palette.teal)}
  ${note(250, 805, 1100, "Rilettura e sottolineatura aiutano solo se diventano domande recuperabili.")}
`
  return shell("Active recall e ripasso distribuito", "Testarsi presto e tornare sugli errori batte rilettura e sottolineatura passiva.", inner)
}

function figureBlocco() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Una sessione efficace alterna comprensione, prova e correzione</text>
  ${timeBlock(140, 320, 205, "0-5", "Obiettivo", "cosa devo produrre", "navy", "softBlue")}
  ${timeBlock(390, 320, 255, "5-25", "Teoria breve", "nucleo ad alta resa", "bordeaux", "softRed")}
  ${timeBlock(690, 320, 255, "25-35", "Richiamo", "senza manuale", "gold", "softGold")}
  ${timeBlock(990, 320, 255, "35-45", "Quiz/output", "5-10 domande", "green", "softGreen")}
  ${timeBlock(1290, 320, 205, "45-50", "Diario", "errore e passo", "teal", "softTeal")}
  <path class="arrowNavy" d="M355 405 L380 405"/>
  <path class="arrowBordeaux" d="M655 405 L680 405"/>
  <path class="arrowGold" d="M955 405 L980 405"/>
  <path class="arrowGreen" d="M1255 405 L1280 405"/>
  ${listCard(250, 590, 410, "Se hai poca energia", ["blocco da 25 minuti", "un solo nucleo", "un output piccolo"], "navy", "softBlue")}
  ${listCard(760, 590, 410, "Se hai piu tempo", ["due blocchi", "pausa reale", "correzione finale"], "green", "softGreen")}
  ${note(250, 805, 1100, "Il timer serve a evitare studio passivo interminabile, non a riempire ore.")}
`
  return shell("Blocco di studio da 50 minuti", "Ogni sessione deve chiudersi con un output e una decisione per il prossimo passo.", inner)
}

function figureDiario() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Dal dato al recupero: ogni errore indica una mossa</text>
  ${listCard(125, 310, 305, "Errore", ["lacuna", "confusione", "lettura", "memoria", "tempo"], "bordeaux", "softRed")}
  ${listCard(470, 310, 305, "Output", ["quiz svolti", "risposta orale", "caso breve", "simulazione"], "navy", "softBlue")}
  ${listCard(815, 310, 305, "Decisione", ["recupero immediato", "ripasso breve", "drill mirato", "taglio"], "gold", "softGold")}
  ${listCard(1160, 310, 305, "Piano", ["prossima sessione", "flashcard", "simulazione", "review bando"], "green", "softGreen")}
  <path class="arrowBordeaux" d="M440 440 L460 440"/>
  <path class="arrowNavy" d="M785 440 L805 440"/>
  <path class="arrowGold" d="M1130 440 L1150 440"/>
  ${mini(220, 680, 300, "Centrale e debole", "recupero subito", palette.bordeaux)}
  ${mini(620, 680, 300, "Centrale sufficiente", "ripasso + quiz", palette.navy)}
  ${mini(1020, 680, 300, "Accessorio debole", "trattazione minima", palette.green)}
  ${note(250, 805, 1100, "Il candidato maturo non recupera tutto: recupera cio che cambia il risultato.")}
`
  return shell("Diario, output e recupero", "Gli errori diventano dati: classificazione, drill mirato e scelta di cosa tagliare.", inner)
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleY = y + 42
  const titleFontSize = title.length > 24 ? 18 : title.length > 19 ? 20 : title.length > 14 ? 22 : 25
  const bodyFontSize = lines.some((line) => line.length > 25) ? 16 : 18
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 25}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${titleY}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function listCard(x, y, w, title, lines, colorClass, boxClass) {
  const rowHeight = 33
  const h = 92 + lines.length * rowHeight
  const titleFontSize = title.length > 22 ? 19 : title.length > 16 ? 21 : 24
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 30}" y="${y + 82 + index * rowHeight}" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 44}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 24} ${y + 64} L${x + w - 24} ${y + 64}"/>
    ${body}
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 21 ? 18 : title.length > 15 ? 19 : 21
  const bodyFontSize = body.length > 26 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 32}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function stepCard(x, y, [number, title, subtitle], w, colorClass = "navy") {
  const center = x + w / 2
  const titleFontSize = title.length > 15 ? 17 : 19
  const subtitleFontSize = subtitle.length > 22 ? 14 : 16

  return `<g data-safe-box="${x} ${y} ${w} 155 8">
    <rect class="card" x="${x}" y="${y}" width="${w}" height="155" rx="20"/>
    <circle cx="${center}" cy="${y + 35}" r="23" fill="${palette[colorClass]}"/>
    <text class="label" x="${center}" y="${y + 44}" text-anchor="middle" fill="#FFFFFF" style="font-size:22px">${esc(number)}</text>
    <text class="${colorClass} label" x="${center}" y="${y + 88}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${center}" y="${y + 121}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function timeBlock(x, y, w, time, title, subtitle, colorClass, boxClass) {
  const titleFontSize = title.length > 15 ? 18 : 20
  const subtitleFontSize = subtitle.length > 21 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 145 0">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="145" rx="20"/>
    <rect x="${x}" y="${y}" width="${w}" height="38" rx="18" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + w / 2}" y="${y + 28}" text-anchor="middle" fill="#FFFFFF" style="font-size:21px">${esc(time)}</text>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 82}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + w / 2}" y="${y + 113}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function timelinePoint(x, y, title, subtitle, color) {
  const titleFontSize = title.length > 9 ? 18 : 20
  const subtitleFontSize = subtitle.length > 16 ? 15 : 16

  return `<g data-safe-box="${x - 95} ${y - 108} 190 190 8">
    <circle cx="${x}" cy="${y}" r="28" fill="${color}"/>
    <text class="label" x="${x}" y="${y - 56}" text-anchor="middle" fill="${color}" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${x}" y="${y + 72}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function circleStep(x, y, number, title, subtitle, color) {
  const titleFontSize = title.length > 13 ? 18 : 20
  const subtitleFontSize = subtitle.length > 16 ? 15 : 16

  return `<g data-safe-box="${x - 90} ${y - 100} 180 200 8">
    <circle cx="${x}" cy="${y}" r="78" fill="${color}"/>
    <text class="label" x="${x}" y="${y - 28}" text-anchor="middle" fill="#FFFFFF" style="font-size:24px">${esc(number)}</text>
    <text class="label" x="${x}" y="${y + 6}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x}" y="${y + 38}" text-anchor="middle" fill="#FFFFFF" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 98 ? 18 : text.length > 82 ? 19 : 20

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
