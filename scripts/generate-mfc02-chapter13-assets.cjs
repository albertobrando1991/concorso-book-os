const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "moduli",
  "m-fc02-agenzie-fiscali",
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
    slug: "01-mappa-bando-performance-finale",
    title: "Mappa BANDO della prestazione finale",
    subtitle: "Dal bando agli output: quiz, caso, orale, diario errori e piano.",
    svg: figureMappaBando()
  },
  {
    slug: "02-quiz-quattro-mosse-parole-spia",
    title: "Quiz M-FC02: quattro mosse",
    subtitle: "Lettura, esclusione, scelta e controllo delle parole-spia.",
    svg: figureQuiz()
  },
  {
    slug: "03-casi-ae-adm-ader-griglia",
    title: "Casi pratici AE, ADM e AdER",
    subtitle: "La griglia unica separa fatto, soggetti, materia, sequenza e output.",
    svg: figureCasi()
  },
  {
    slug: "04-orale-90-secondi-domande-trappola",
    title: "Risposta orale da 90 secondi",
    subtitle: "Definizione, funzione, soggetti, sequenza, esempio e limite.",
    svg: figureOrale()
  },
  {
    slug: "05-simulazione-diario-piano-30-60-90",
    title: "Simulazione, diario e piano 30/60/90",
    subtitle: "La prova finale produce dati, correzioni e priorita di studio.",
    svg: figureSimulazione()
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
  return `# Asset Capitolo 13 - M-FC02 Casi pratici, quiz e orale nelle Agenzie fiscali

Figure generate per \`Casi pratici, quiz e orale nelle Agenzie fiscali\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, flusso procedurale, schema anti-confusione, mappa applicativa e checklist/simulazione;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO della prestazione finale, procedura per quiz, griglia casi AE-ADM-AdER, schema orale da 90 secondi e simulazione finale con diario e piano 30/60/90.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-performance-finale.png\` | \`01-mappa-bando-performance-finale.svg\` | Sintesi del capitolo: prova, materie, distinzioni, errori e output. |
| \`02-quiz-quattro-mosse-parole-spia.png\` | \`02-quiz-quattro-mosse-parole-spia.svg\` | Procedura visiva per affrontare quiz e parole-spia. |
| \`03-casi-ae-adm-ader-griglia.png\` | \`03-casi-ae-adm-ader-griglia.svg\` | Griglia unica per leggere casi AE, ADM e AdER senza confondere competenze. |
| \`04-orale-90-secondi-domande-trappola.png\` | \`04-orale-90-secondi-domande-trappola.svg\` | Schema della risposta orale e gestione delle domande-trappola. |
| \`05-simulazione-diario-piano-30-60-90.png\` | \`05-simulazione-diario-piano-30-60-90.svg\` | Chiusura operativa: simulazione, diario errori e piano 30/60/90. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(510, 205, 580, 142, "Prestazione M-FC02", ["quiz, caso, orale", "diario e piano finale"], "navy", "softBlue")}
  ${arrow(800, 348, 800, 380, "Navy")}
  <path class="line" d="M205 380 L1395 380"/>
  ${line(205, 380, 205, 470)}
  ${line(505, 380, 505, 590)}
  ${line(800, 380, 800, 470)}
  ${line(1095, 380, 1095, 590)}
  ${line(1395, 380, 1395, 470)}
  ${box(70, 470, 270, 132, "B - Prova", ["format, soglie", "tempo e avvisi"], "navy", "softBlue")}
  ${box(370, 590, 270, 132, "A - Materie", ["tributario", "dogane, AdER"], "bordeaux", "softRed")}
  ${box(665, 470, 270, 132, "N - Nuclei", ["enti, atti", "sequenze"], "gold", "softGold")}
  ${box(960, 590, 270, 132, "D - Errori", ["memoria, lettura", "piani confusi"], "green", "softGreen")}
  ${box(1260, 470, 270, 132, "O - Output", ["simulazione", "piano 30/60/90"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Il capitolo trasforma programma e studio in prestazioni misurabili.")}`

  return shell("Mappa BANDO della prestazione finale", "Dal bando agli output: quiz, caso, orale, diario errori e piano.", inner)
}

function figureQuiz() {
  const y = 270
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(150, y, "1", "Lettura", ["richiesta", "parola-spia"], "navy", "softBlue")}
  ${step(455, y, "2", "Esclusione", ["soggetto", "fase"], "bordeaux", "softRed")}
  ${step(760, y, "3", "Scelta", ["opzione", "perimetro"], "gold", "softGold")}
  ${step(1065, y, "4", "Controllo", ["negazioni", "assoluti"], "green", "softGreen")}
  ${arrow(365, y + 84, 445, y + 84, "Navy")}
  ${arrow(670, y + 84, 750, y + 84, "Bordeaux")}
  ${arrow(975, y + 84, 1055, y + 84, "Gold")}
  ${smallBox(185, 555, 305, 112, "Banca dati", ["versione", "tag errori"], "teal", "softTeal")}
  ${smallBox(520, 555, 305, 112, "Senza banca", ["nuclei bando", "quiz mirati"], "navy", "softBlue")}
  ${smallBox(855, 555, 305, 112, "Parole-spia", ["non, sempre", "ente, cartella"], "bordeaux", "softRed")}
  ${smallBox(1190, 555, 225, 112, "Diario", ["causa", "azione"], "green", "softGreen")}
  ${note(245, 815, 1110, "Il quiz premia precisione: prima capisci il piano, poi scegli la risposta.")}`

  return shell("Quiz M-FC02: quattro mosse", "Lettura, esclusione, scelta e controllo delle parole-spia.", inner)
}

function figureCasi() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${panel(100, 225, 360, 188, "AE", ["dichiarazioni", "controlli", "compliance"], "bordeaux", "softRed")}
  ${panel(620, 225, 360, 188, "ADM", ["merce", "origine/valore", "controlli"], "teal", "softTeal")}
  ${panel(1140, 225, 360, 188, "AdER", ["cartella", "rateizzazione", "sportello"], "green", "softGreen")}
  ${arrow(460, 320, 610, 320, "Bordeaux")}
  ${arrow(980, 320, 1130, 320, "Teal")}
  ${center(540, 492, 520, 140, "Griglia unica", ["fatto, soggetti, materia", "istituto, sequenza, output"], "navy", "softBlue")}
  ${smallBox(165, 555, 300, 102, "Domanda 1", ["chi e' competente?"], "navy", "softBlue")}
  ${smallBox(1135, 555, 300, 102, "Domanda 2", ["quale fase?"], "gold", "softGold")}
  ${note(245, 815, 1110, "Il caso non chiede piu' teoria: chiede di applicare il piano corretto al fatto.")}`

  return shell("Casi pratici AE, ADM e AdER", "La griglia unica separa fatto, soggetti, materia, sequenza e output.", inner)
}

function figureOrale() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(590, 315, 420, 170, "Risposta 90 secondi", ["ordine, lessico", "e chiusura prudente"], "navy", "softBlue")}
  ${oralNode(155, 225, "1. Definizione", ["che cos'e'"], "navy", "softBlue")}
  ${oralNode(570, 205, "2. Funzione", ["a cosa serve"], "bordeaux", "softRed")}
  ${oralNode(985, 225, "3. Soggetti", ["chi interviene"], "gold", "softGold")}
  ${oralNode(155, 545, "4. Sequenza", ["prima / dopo"], "green", "softGreen")}
  ${oralNode(570, 565, "5. Esempio", ["profilo fiscale"], "teal", "softTeal")}
  ${oralNode(985, 545, "6. Limite", ["non confondere"], "bordeaux", "softRed")}
  ${line(430, 292, 580, 360)}
  ${line(790, 290, 950, 360)}
  ${line(430, 610, 580, 450)}
  ${line(790, 610, 950, 450)}
  ${smallBox(510, 690, 580, 92, "Domanda-trappola", ["correggi la premessa, poi spiega il criterio"], "gold", "softGold")}
  ${note(245, 815, 1110, "Una risposta forte non dice tutto: definisce, collega e sa fermarsi.")}`

  return shell("Risposta orale da 90 secondi", "Definizione, funzione, soggetti, sequenza, esempio e limite.", inner)
}

function figureSimulazione() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${simBlock(100, 238, "Quiz", "35 min", ["punteggio", "domande lente"], "navy", "softBlue")}
  ${simBlock(410, 238, "Caso", "25 min", ["griglia", "conclusione"], "bordeaux", "softRed")}
  ${simBlock(720, 238, "Orale", "20 min", ["3 risposte", "90 secondi"], "gold", "softGold")}
  ${simBlock(1030, 238, "Diario", "10 min", ["cause", "azioni"], "green", "softGreen")}
  ${arrow(330, 330, 400, 330, "Navy")}
  ${arrow(640, 330, 710, 330, "Bordeaux")}
  ${arrow(950, 330, 1020, 330, "Gold")}
  ${arrow(1180, 440, 1180, 500, "Green")}
  ${center(520, 520, 560, 144, "Piano 30/60/90", ["30: fondamenta  |  60: casi", "90: simulazioni e rifinitura"], "teal", "softTeal")}
  ${smallBox(120, 555, 320, 112, "Dati utili", ["errori ricorrenti", "materie lente"], "gold", "softGold")}
  ${smallBox(1160, 555, 320, 112, "Priorita", ["ripasso mirato", "verifica"], "navy", "softBlue")}
  ${note(245, 815, 1110, "La simulazione vale solo se produce correzioni e una prossima azione verificabile.")}`

  return shell("Simulazione, diario e piano 30/60/90", "La prova finale produce dati, correzioni e priorita di studio.", inner)
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
      .title { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 43px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 22px; letter-spacing: 0; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: 0; }
      .body { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 20px; letter-spacing: 0; }
      .small { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 18px; letter-spacing: 0; }
      .line { stroke: ${palette.line}; stroke-width: 4; stroke-linecap: round; fill: none; }
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
  <g data-safe-box="120 14 1360 116 0" data-safe-name="header">
    <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
    <text class="muted subtitle" x="800" y="106" text-anchor="middle">${esc(subtitle)}</text>
  </g>
  ${inner}
</svg>
`
}

function box(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <circle cx="${x + 38}" cy="${y + 38}" r="17" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 66}" y="${y + 45}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 26}" y="${y + 82 + index * 27}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function center(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="26"/>
    <circle cx="${x + 44}" cy="${y + 44}" r="18" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 74}" y="${y + 52}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 34}" y="${y + 92 + index * 28}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function panel(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="24"/>
    <rect x="${x}" y="${y}" width="11" height="${h}" rx="5.5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 32}" y="${y + 45}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 34}" y="${y + 84 + index * 29}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 215 170 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="215" height="170" rx="22"/>
    <circle cx="${x + 38}" cy="${y + 38}" r="21" fill="${palette[color]}"/>
    <text x="${x + 38}" y="${y + 46}" text-anchor="middle" fill="#FFFFFF" style="font: 800 21px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 26}" y="${y + 82}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 26}" y="${y + 116 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function smallBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="20"/>
    <rect x="${x}" y="${y}" width="10" height="${h}" rx="5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 24}" y="${y + 36}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 24}" y="${y + 68 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function oralNode(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 360 118 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="360" height="118" rx="22"/>
    <rect x="${x}" y="${y}" width="10" height="118" rx="5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 28}" y="${y + 42}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 30}" y="${y + 80 + index * 26}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function simBlock(x, y, title, time, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 240 190 10" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="240" height="190" rx="24"/>
    <text class="ink label" x="${x + 28}" y="${y + 44}">${esc(title)}</text>
    <text class="muted body" x="${x + 28}" y="${y + 78}">${esc(time)}</text>
    <rect x="${x + 28}" y="${y + 96}" width="184" height="5" rx="2.5" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 30}" y="${y + 135 + index * 24}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function note(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 54 14" data-safe-name="nota">
    <rect class="note" x="${x}" y="${y}" width="${w}" height="54" rx="18"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 35}" text-anchor="middle">${esc(text)}</text>
  </g>`
}

function arrow(x1, y1, x2, y2, color) {
  return `<path class="arrow${color}" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function line(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error)
    process.exit(1)
  })
