const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-19"
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
    slug: "01-mappa-bando-famiglie-concorsuali",
    title: "Mappa BANDO delle famiglie concorsuali",
    subtitle: "La famiglia aiuta a leggere il bando: cosa riuso, cosa aggiungo, cosa alleno.",
    svg: figureMappa()
  },
  {
    slug: "02-due-errori-da-evitare",
    title: "Due errori opposti da evitare",
    subtitle: "Tutto uguale disperde il profilo; tutto diverso spreca capitale di studio.",
    svg: figureErrori()
  },
  {
    slug: "03-quattro-domande-famiglia",
    title: "Quattro domande per riconoscere la famiglia",
    subtitle: "Amministrazione, profilo, funzione e prova orientano tutto il piano.",
    svg: figureDomande()
  },
  {
    slug: "04-atlante-famiglie-concorsuali",
    title: "Atlante operativo delle famiglie",
    subtitle: "Le famiglie sono categorie di lavoro: non etichette ufficiali rigide.",
    svg: figureAtlante()
  },
  {
    slug: "05-nucleo-comune-modulo-profilo",
    title: "Nucleo comune e modulo profilo",
    subtitle: "La base riutilizzabile non sostituisce il modulo che decide il punteggio.",
    svg: figureCoreModulo()
  },
  {
    slug: "06-caso-guidato-tre-bandi",
    title: "Caso guidato: tre bandi aperti",
    subtitle: "Stesso nucleo comune, tre moduli diversi e tre rischi da pesare.",
    svg: figureCaso()
  },
  {
    slug: "07-sequenza-famiglia-piano",
    title: "Sequenza operativa: dalla famiglia al piano",
    subtitle: "Prima famiglia e profilo, poi programma, materiali e simulazioni coerenti.",
    svg: figureSequenza()
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
  return `# Asset Capitolo 19

Figure generate per \`Le famiglie dei concorsi pubblici\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-famiglie-concorsuali.png\` | Mappa BANDO per leggere le famiglie concorsuali dentro bando, aree, nuclei, diario e output. |
| \`02-due-errori-da-evitare.png\` | Confronto tra i due errori opposti: tutti i concorsi uguali o tutti completamente diversi. |
| \`03-quattro-domande-famiglia.png\` | Le quattro domande iniziali per riconoscere famiglia, profilo e prova selettiva. |
| \`04-atlante-famiglie-concorsuali.png\` | Atlante sintetico delle principali famiglie operative del Metodo BANDO. |
| \`05-nucleo-comune-modulo-profilo.png\` | Distinzione tra nucleo comune riutilizzabile, modulo profilo e output di prova. |
| \`06-caso-guidato-tre-bandi.png\` | Caso guidato con tre bandi: comune contabile, agenzia fiscale e universita. |
| \`07-sequenza-famiglia-piano.png\` | Sequenza operativa per trasformare famiglia e profilo in piano di studio. |

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
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
    <marker id="arrowBordeaux" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.bordeaux}"/></marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/></marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.green}"/></marker>
    <marker id="arrowTeal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.teal}"/></marker>
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
  ${card(575, 168, 450, 125, "Famiglia concorsuale", ["leggere il terreno", "prima dei materiali"], "navy", "card")}
  <path class="line" d="M800 293 L800 363"/>
  <path class="line" d="M210 363 L1390 363"/>
  ${connector(210, 363, 210, 450)}
  ${connector(505, 363, 505, 570)}
  ${connector(800, 363, 800, 450)}
  ${connector(1095, 363, 1095, 570)}
  ${connector(1390, 363, 1390, 450)}
  ${card(75, 450, 270, 130, "Bando", ["amministrazione", "profilo e prove"], "navy", "softBlue")}
  ${card(370, 570, 270, 130, "Aree", ["comune", "specialistico"], "bordeaux", "softRed")}
  ${card(665, 450, 270, 130, "Nuclei", ["argomenti", "ad alto rendimento"], "gold", "softGold")}
  ${card(960, 570, 270, 130, "Diario", ["ore investite", "errori per famiglia"], "green", "softGreen")}
  ${card(1255, 450, 270, 130, "Output", ["quiz, scritto", "caso, orale"], "teal", "softTeal")}
  ${note(250, 792, 1100, "La famiglia non sostituisce il bando: lo rende piu leggibile e meno dispersivo.")}
`
  return shell(
    "Mappa BANDO delle famiglie concorsuali",
    "La famiglia aiuta a leggere il bando: cosa riuso, cosa aggiungo, cosa alleno.",
    inner
  )
}

function figureErrori() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${comparisonPanel(135, 245, 560, "Tutti uguali", ["preparazione generica", "profilo ignorato", "materia killer scoperta tardi"], "bordeaux", "softRed")}
  ${centerBadge(650, 360, 300, 150, "Equilibrio", ["nucleo comune", "+ modulo profilo"], "navy")}
  ${comparisonPanel(905, 245, 560, "Tutti diversi", ["si ricomincia da zero", "materiali moltiplicati", "capitale gia studiato disperso"], "gold", "softGold")}
  <path class="arrowBordeaux" d="M705 420 L640 420"/>
  <path class="arrowGold" d="M895 420 L960 420"/>
  ${mini(205, 675, 330, "Errore", "stesso piano per ogni bando", palette.bordeaux)}
  ${mini(1035, 675, 330, "Errore", "nessun riuso strategico", palette.gold)}
  ${note(250, 812, 1100, "La risposta corretta sta in mezzo: riusa la base, ma cambia priorita, linguaggio e prova.")}
`
  return shell(
    "Due errori opposti da evitare",
    "Tutto uguale disperde il profilo; tutto diverso spreca capitale di studio.",
    inner
  )
}

function figureDomande() {
  const items = [
    ["1", "Chi assume?", "ente, settore e lessico", "navy", "softBlue"],
    ["2", "Per quale profilo?", "assistente, istruttore, funzionario, tecnico", "bordeaux", "softRed"],
    ["3", "Quale funzione?", "sportello, istruttoria, controllo, bilancio", "gold", "softGold"],
    ["4", "Quale prova seleziona?", "quiz, scritto, orale, pratica, situazione", "green", "softGreen"]
  ]
  const tiles = items
    .map(([n, title, body, color, box], index) => questionTile(150 + index * 370, 300, 300, n, title, body, color, box))
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="230" text-anchor="middle">Prima il contesto, poi l'elenco delle materie</text>
  ${tiles}
  <path class="arrowNavy" d="M455 400 L510 400"/>
  <path class="arrowBordeaux" d="M825 400 L880 400"/>
  <path class="arrowGold" d="M1195 400 L1250 400"/>
  ${note(250, 690, 1100, "Solo dopo queste quattro risposte il programma del bando diventa davvero leggibile.")}
`
  return shell(
    "Quattro domande per riconoscere la famiglia",
    "Amministrazione, profilo, funzione e prova orientano tutto il piano.",
    inner
  )
}

function figureAtlante() {
  const groups = [
    ["Base amministrativa", "amm. generale, contabile, enti locali", "navy", "softBlue"],
    ["Centrale e giustizia", "ministeri, funzioni centrali, giustizia", "bordeaux", "softRed"],
    ["Specialistiche forti", "fiscale, lavoro, previdenza, vigilanza", "gold", "softGold"],
    ["Tecniche e digitali", "tecnici PA, ICT, digitale, cybersecurity", "green", "softGreen"],
    ["Servizi territoriali", "polizia locale, sanita, scuola, universita", "teal", "softTeal"],
    ["Progetti e carriere", "PNRR, appalti, UE, dirigenza, speciali", "navy", "softBlue"]
  ]
  const cells = groups
    .map(([title, body, color, box], index) => familyCell(115 + (index % 3) * 485, 260 + Math.floor(index / 3) * 225, 405, title, body, color, box))
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Raggruppa per contesto, rischio e modulo da aggiungere</text>
  ${cells}
  ${note(250, 812, 1100, "Le famiglie sono mappe operative: il bando resta la fonte che decide dettaglio e priorita.")}
`
  return shell(
    "Atlante operativo delle famiglie",
    "Le famiglie sono categorie di lavoro: non etichette ufficiali rigide.",
    inner
  )
}

function figureCoreModulo() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${stackBox(135, 260, 430, "Nucleo comune", ["amministrativo", "pubblico impiego", "trasparenza, privacy", "informatica, inglese", "quiz, scritto, orale"], "navy", "softBlue")}
  ${stackBox(600, 260, 430, "Modulo profilo", ["tributario", "bilancio", "codice strada", "sanita, scuola", "tecnico o ICT"], "bordeaux", "softRed")}
  ${stackBox(1065, 260, 430, "Output di prova", ["quiz a tempo", "risposta breve", "caso pratico", "orale", "prova pratica"], "green", "softGreen")}
  <path class="arrowNavy" d="M575 445 L590 445"/>
  <path class="arrowBordeaux" d="M1040 445 L1055 445"/>
  ${note(250, 812, 1100, "Il nucleo comune riduce dispersione; il modulo profilo impedisce di arrivare generici.")}
`
  return shell(
    "Nucleo comune e modulo profilo",
    "La base riutilizzabile non sostituisce il modulo che decide il punteggio.",
    inner
  )
}

function figureCaso() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Tre bandi, una base comune, moduli separati</text>
  ${caseCard(120, 300, 405, "Comune contabile", ["enti locali", "bilancio, atti", "rischio: contabilita tardi"], "navy", "softBlue")}
  ${caseCard(575, 300, 405, "Agenzia fiscale", ["organizzazione agenzia", "tributario", "rischio: modulo killer"], "bordeaux", "softRed")}
  ${caseCard(1030, 300, 405, "Universita", ["segreterie e studenti", "ordinamento settore", "rischio: contesto ignorato"], "green", "softGreen")}
  <path class="dash" d="M180 615 L1420 615"/>
  ${mini(270, 665, 290, "Base comune", "amministrativo, impiego", palette.navy)}
  ${mini(635, 665, 290, "Pesatura", "prove e punteggi", palette.gold)}
  ${mini(1000, 665, 290, "Blocchi separati", "moduli etichettati", palette.green)}
`
  return shell(
    "Caso guidato: tre bandi aperti",
    "Stesso nucleo comune, tre moduli diversi e tre rischi da pesare.",
    inner
  )
}

function figureSequenza() {
  const steps = [
    ["1", "Famiglia", "riconosci il terreno", "navy", "softBlue"],
    ["2", "Profilo", "capisci il ruolo", "bordeaux", "softRed"],
    ["3", "Programma", "separa comune e modulo", "gold", "softGold"],
    ["4", "Materiali", "scegli solo cio che serve", "green", "softGreen"],
    ["5", "Piano", "tempo, diario, output", "teal", "softTeal"]
  ]
  const cards = steps
    .map(([n, title, body, color, box], index) => stepCard(105 + index * 295, 335, n, title, [body], color, box))
    .join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Non scegliere il manuale prima della famiglia</text>
  ${cards}
  <path class="arrowNavy" d="M315 430 L390 430"/>
  <path class="arrowBordeaux" d="M610 430 L685 430"/>
  <path class="arrowGold" d="M905 430 L980 430"/>
  <path class="arrowGreen" d="M1200 430 L1275 430"/>
  ${note(250, 690, 1100, "Ordine corretto: prima famiglia, poi profilo, programma, materiali e simulazioni coerenti.")}
`
  return shell(
    "Sequenza operativa: dalla famiglia al piano",
    "Prima famiglia e profilo, poi programma, materiali e simulazioni coerenti.",
    inner
  )
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleFontSize = title.length > 28 ? 17 : title.length > 22 ? 19 : title.length > 15 ? 22 : 25
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

function comparisonPanel(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 100 + index * 34}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")
  return `<g data-safe-box="${x} ${y} ${w} 315 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="315" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 52}" text-anchor="middle">${esc(title)}</text>
    <path class="thin" d="M${x + 40} ${y + 70} L${x + w - 40} ${y + 70}"/>
    ${body}
  </g>`
}

function centerBadge(x, y, w, h, title, lines, colorClass) {
  const body = lines
    .map((line, index) => `<text class="small" x="${x + w / 2}" y="${y + 88 + index * 28}" text-anchor="middle" fill="#FFFFFF">${esc(line)}</text>`)
    .join("\n")
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="32" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + w / 2}" y="${y + 52}" text-anchor="middle" fill="#FFFFFF">${esc(title)}</text>
    ${body}
  </g>`
}

function questionTile(x, y, w, number, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} ${w} 245 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="245" rx="26"/>
    <circle cx="${x + w / 2}" cy="${y + 55}" r="34" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + w / 2}" y="${y + 66}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 118}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <text class="muted small" x="${x + w / 2}" y="${y + 170}" text-anchor="middle" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function familyCell(x, y, w, title, body, colorClass, boxClass) {
  const titleFontSize = title.length > 24 ? 18 : 21
  const bodyFontSize = body.length > 44 ? 15 : 16
  return `<g data-safe-box="${x} ${y} ${w} 155 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="155" rx="23"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 45}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 30} ${y + 68} L${x + w - 30} ${y + 68}"/>
    <text class="muted small" x="${x + w / 2}" y="${y + 108}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function stackBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 110 + index * 42}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")
  return `<g data-safe-box="${x} ${y} ${w} 455 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="455" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 55}" text-anchor="middle">${esc(title)}</text>
    <path class="thin" d="M${x + 38} ${y + 78} L${x + w - 38} ${y + 78}"/>
    ${rows}
  </g>`
}

function caseCard(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 100 + index * 36}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")
  return `<g data-safe-box="${x} ${y} ${w} 250 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="250" rx="25"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 50}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    <path class="thin" d="M${x + 35} ${y + 72} L${x + w - 35} ${y + 72}"/>
    ${rows}
  </g>`
}

function stepCard(x, y, number, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 102}" y="${y + 98 + index * 27}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")
  return `<g data-safe-box="${x} ${y} 205 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="190" rx="24"/>
    <circle cx="${x + 102.5}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 102.5}" y="${y + 51}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 78}" text-anchor="middle" style="font-size:18px">${esc(title)}</text>
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
  const fontSize = text.length > 108 ? 18 : text.length > 90 ? 19 : 20
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
