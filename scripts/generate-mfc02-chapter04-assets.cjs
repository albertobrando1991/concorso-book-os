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
  "chapter-04"
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
    slug: "01-mappa-bando-diritto-tributario",
    title: "Mappa BANDO del diritto tributario",
    subtitle: "Dal programma fiscale alla mappa minima per quiz, orale e casi.",
    svg: figureMappaBando()
  },
  {
    slug: "02-sequenza-nascita-tributo",
    title: "Come nasce e si sviluppa il tributo",
    subtitle: "Una sequenza per leggere definizioni, adempimenti, controlli e riscossione.",
    svg: figureSequenzaTributo()
  },
  {
    slug: "03-categorie-del-tributo",
    title: "Tributo, imposta, tassa e contributo",
    subtitle: "La classificazione minima per non usare come sinonimi parole diverse.",
    svg: figureCategorieTributo()
  },
  {
    slug: "04-presupposto-base-aliquota",
    title: "Presupposto, base imponibile e aliquota",
    subtitle: "Tre domande diverse: perche nasce, su cosa si calcola, come si misura.",
    svg: figureFormula()
  },
  {
    slug: "05-tuir-iva-accertamento-riscossione",
    title: "Dalla teoria alle fonti operative",
    subtitle: "TUIR, IVA, accertamento e riscossione come mappe diverse dello stesso rapporto.",
    svg: figureFontiOperative()
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
  return `# Asset Capitolo 4 - M-FC02 Diritto tributario e teoria dell'imposta

Figure generate per \`Diritto tributario e teoria dell'imposta\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 o 1600 x 1000 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card arrotondate, linee leggere e nessun elemento decorativo senza funzione;
- funzioni ricorrenti: mappa BANDO, sequenza operativa, confronto concettuale, formula/matrice e sintesi pre-epilogativa;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono la mappa del capitolo, la sequenza del rapporto tributario, le categorie del tributo, la formula presupposto/base/aliquota e il ponte verso TUIR, IVA, accertamento e riscossione.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-diritto-tributario.png\` | \`01-mappa-bando-diritto-tributario.svg\` | Mappa BANDO del capitolo: programma, aree, nuclei, diario e output. |
| \`02-sequenza-nascita-tributo.png\` | \`02-sequenza-nascita-tributo.svg\` | Sequenza dal fatto rilevante ad accertamento e riscossione. |
| \`03-categorie-del-tributo.png\` | \`03-categorie-del-tributo.svg\` | Distinzione tributo, imposta, tassa e contributo. |
| \`04-presupposto-base-aliquota.png\` | \`04-presupposto-base-aliquota.svg\` | Formula operativa per distinguere presupposto, base imponibile e aliquota. |
| \`05-tuir-iva-accertamento-riscossione.png\` | \`05-tuir-iva-accertamento-riscossione.svg\` | Ponte pre-epilogativo tra teoria, fonti operative e capitoli successivi. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${node(585, 205, 430, 122, "Diritto tributario", ["teoria minima", "per prove fiscali"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${node(70, 460, 270, 130, "B - Bando", ["TUIR, IVA", "accertamento"], "navy", "softBlue")}
  ${node(370, 585, 270, 130, "A - Aree", ["teoria", "redditi, IVA"], "bordeaux", "softRed")}
  ${node(665, 460, 270, 130, "N - Nuclei", ["presupposto", "soggetto, base"], "gold", "softGold")}
  ${node(960, 585, 270, 130, "D - Diario", ["tassa/imposta", "accertamento/riscossione"], "green", "softGreen")}
  ${node(1260, 460, 270, 130, "O - Output", ["risposta orale", "quiz e casi"], "teal", "softTeal")}
  ${note(255, 815, 1090, "Il capitolo seleziona il minimo stabile: concetti, sequenza e uso in prova.")}
`
  return shell("Mappa BANDO del diritto tributario", "Dal programma fiscale alla mappa minima per quiz, orale e casi.", inner)
}

function figureSequenzaTributo() {
  const y1 = 260
  const y2 = 520
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(105, y1, "1", "Fatto rilevante", ["reddito", "operazione", "situazione"], "navy", "softBlue")}
  ${step(415, y1, "2", "Presupposto", ["perche nasce", "la rilevanza"], "bordeaux", "softRed")}
  ${step(725, y1, "3", "Soggetto", ["chi e' tenuto", "all'obbligo"], "gold", "softGold")}
  ${step(1035, y1, "4", "Base imponibile", ["su quale", "grandezza"], "green", "softGreen")}
  ${arrow(365, y1 + 82, 405, y1 + 82, "Navy")}
  ${arrow(675, y1 + 82, 715, y1 + 82, "Bordeaux")}
  ${arrow(985, y1 + 82, 1025, y1 + 82, "Gold")}
  ${step(260, y2, "5", "Calcolo", ["aliquota", "imposta dovuta"], "teal", "softTeal")}
  ${step(570, y2, "6", "Adempimento", ["dichiarazione", "versamento"], "navy", "softBlue")}
  ${step(880, y2, "7", "Controllo", ["verifica", "accertamento"], "bordeaux", "softRed")}
  ${step(1190, y2, "8", "Riscossione", ["credito", "pagamento"], "green", "softGreen")}
  ${arrow(520, y2 + 82, 560, y2 + 82, "Teal")}
  ${arrow(830, y2 + 82, 870, y2 + 82, "Navy")}
  ${arrow(1140, y2 + 82, 1180, y2 + 82, "Bordeaux")}
  <path class="arrowGold" d="M1170 425 C1060 485, 510 485, 382 520"/>
  ${note(255, 815, 1090, "Se perdi un passaggio, confondi definizioni, procedimenti e atti.")}
`
  return shell("Come nasce e si sviluppa il tributo", "Una sequenza per leggere definizioni, adempimenti, controlli e riscossione.", inner)
}

function figureCategorieTributo() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${node(585, 220, 430, 125, "Tributo", ["categoria generale", "prelievo pubblico previsto dalla legge"], "navy", "softBlue")}
  <path class="line" d="M800 345 L800 415"/>
  <path class="line" d="M280 415 L1320 415"/>
  ${line(280, 415, 280, 475)}
  ${line(800, 415, 800, 475)}
  ${line(1320, 415, 1320, 475)}
  ${category(120, 475, "Imposta", ["capacita contributiva", "senza servizio individuale", "finanziamento generale"], "bordeaux", "softRed")}
  ${category(640, 475, "Tassa", ["servizio pubblico", "attivita amministrativa", "non prezzo privato"], "gold", "softGold")}
  ${category(1160, 475, "Contributo", ["posizione specifica", "vantaggio o funzione", "collegamento particolare"], "green", "softGreen")}
  ${note(250, 815, 1100, "Nel linguaggio comune tutto diventa tassa; nel concorso la distinzione va mantenuta.")}
`
  return shell("Tributo, imposta, tassa e contributo", "La classificazione minima per non usare come sinonimi parole diverse.", inner)
}

function figureFormula() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${formulaBox(120, 245, "Presupposto", "Perche il tributo puo' nascere?", ["fatto, atto o situazione", "previsti dalla legge"], "navy", "softBlue")}
  ${bigPlus(480, 420)}
  ${formulaBox(560, 245, "Soggetto", "Chi e' tenuto all'obbligo?", ["contribuente", "sostituto o responsabile"], "bordeaux", "softRed")}
  ${bigPlus(920, 420)}
  ${formulaBox(1000, 245, "Base imponibile", "Su quale grandezza calcolo?", ["reddito, valore", "corrispettivo o misura"], "gold", "softGold")}
  <path class="arrowGreen" d="M800 610 L800 670"/>
  ${resultBox(465, 670, 670, "Aliquota e disciplina applicabile", ["portano alla determinazione dell'imposta dovuta", "e agli adempimenti successivi"], "green", "softGreen")}
  ${note(245, 815, 1110, "Errore da evitare: chiamare base imponibile la somma finale da pagare.")}
`
  return shell("Presupposto, base imponibile e aliquota", "Tre domande diverse: perche nasce, su cosa si calcola, come si misura.", inner)
}

function figureFontiOperative() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(575, 208, 450, 96, "Teoria dell'imposta", ["concetti stabili per leggere fonti e procedure"], "navy", "softBlue")}
  <path class="line" d="M800 304 L800 365"/>
  <path class="line" d="M285 365 L1315 365"/>
  ${line(285, 365, 285, 445)}
  ${line(628, 365, 628, 445)}
  ${line(972, 365, 972, 445)}
  ${line(1315, 365, 1315, 445)}
  ${sourceCard(120, 445, "TUIR", ["soggetti", "redditi", "categorie"], "cap. 6", "navy", "softBlue")}
  ${sourceCard(462, 445, "IVA", ["operazioni", "rivalsa", "detrazione"], "cap. 6", "bordeaux", "softRed")}
  ${sourceCard(805, 445, "Accertamento", ["controllo", "poteri", "atti"], "cap. 5", "gold", "softGold")}
  ${sourceCard(1148, 445, "Riscossione", ["cartella", "pagamento", "rateizzazione"], "cap. 7", "green", "softGreen")}
  ${note(245, 815, 1110, "La teoria non chiude l'argomento: prepara la lettura dei capitoli operativi successivi.")}
`
  return shell("Dalla teoria alle fonti operative", "TUIR, IVA, accertamento e riscossione come mappe diverse dello stesso rapporto.", inner)
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
      .subtitle { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 22px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: 0; }
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

function node(x, y, w, h, title, lines, color, fillClass) {
  return safe(x, y, w, h, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 41}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 74, 26, "muted small", 18)}
  `)
}

function step(x, y, num, title, lines, color, fillClass) {
  return safe(x, y, 260, 165, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="260" height="165" rx="24"/>
    <circle cx="${x + 43}" cy="${y + 47}" r="27" fill="${palette[color]}"/>
    <text x="${x + 43}" y="${y + 57}" text-anchor="middle" style="fill:#fff;font-family:'Source Sans 3','Segoe UI',Arial,sans-serif;font-size:25px;font-weight:900">${esc(num)}</text>
    <text class="${color} label" x="${x + 88}" y="${y + 47}" text-anchor="start" style="font-size:18px">${esc(title)}</text>
    ${textLines(lines, x + 130, y + 89, 25, "muted small", 17)}
  `)
}

function category(x, y, title, lines, color, fillClass) {
  return safe(x, y, 320, 250, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="320" height="250" rx="26"/>
    <rect x="${x}" y="${y}" width="320" height="11" rx="5.5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 160}" y="${y + 52}" text-anchor="middle">${esc(title)}</text>
    <path class="thin" d="M${x + 42} ${y + 82} L${x + 278} ${y + 82}"/>
    ${bulletLines(lines, x + 55, y + 126, 38)}
  `)
}

function formulaBox(x, y, title, question, lines, color, fillClass) {
  return safe(x, y, 340, 300, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="340" height="300" rx="28"/>
    <rect x="${x}" y="${y}" width="340" height="11" rx="5.5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 170}" y="${y + 56}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    <text class="ink small" x="${x + 170}" y="${y + 98}" text-anchor="middle" style="font-weight:800;font-size:17px">${esc(question)}</text>
    <path class="thin" d="M${x + 45} ${y + 124} L${x + 295} ${y + 124}"/>
    ${textLines(lines, x + 170, y + 166, 36, "muted small", 18)}
  `)
}

function resultBox(x, y, w, title, lines, color, fillClass) {
  return safe(x, y, w, 112, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="112" rx="26"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 74, 24, "muted small", 17)}
  `)
}

function center(x, y, w, h, title, lines, color, fillClass) {
  return safe(x, y, w, h, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 39}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 70, 22, "muted small", 17)}
  `)
}

function sourceCard(x, y, title, lines, chapter, color, fillClass) {
  return safe(x, y, 285, 255, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="285" height="255" rx="26"/>
    <rect x="${x}" y="${y}" width="285" height="11" rx="5.5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 142.5}" y="${y + 52}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    ${bulletLines(lines, x + 45, y + 107, 38)}
    <rect x="${x + 66}" y="${y + 195}" width="153" height="42" rx="17" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text class="ink small" x="${x + 142.5}" y="${y + 222}" text-anchor="middle" style="font-weight:800;font-size:17px">${esc(chapter)}</text>
  `)
}

function note(x, y, w, text) {
  return safe(x, y, w, 62, `
    <rect class="note" x="${x}" y="${y}" width="${w}" height="62" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 39}" text-anchor="middle" style="font-weight:800;font-size:20px">${esc(text)}</text>
  `)
}

function bigPlus(x, y) {
  return `<g data-safe-box="${x - 35} ${y - 38} 70 76 0">
    <circle cx="${x}" cy="${y}" r="29" fill="${palette.gold}"/>
    <text x="${x}" y="${y + 10}" text-anchor="middle" style="fill:#fff;font-family:'Source Sans 3','Segoe UI',Arial,sans-serif;font-size:34px;font-weight:900">+</text>
  </g>`
}

function arrow(x1, y1, x2, y2, color) {
  return `<path class="arrow${color}" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function line(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function safe(x, y, w, h, inner) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 10">${inner}</g>`
}

function textLines(lines, x, y, gap, className, size) {
  return lines
    .map((line, index) => `<text class="${className}" x="${x}" y="${y + index * gap}" text-anchor="middle" style="font-size:${size}px">${esc(line)}</text>`)
    .join("\n")
}

function bulletLines(lines, x, y, gap) {
  return lines
    .map((text, index) => {
      const lineY = y + index * gap
      return `<circle cx="${x}" cy="${lineY - 7}" r="6" fill="${palette.gold}"/><text class="ink body" x="${x + 22}" y="${lineY}" style="font-size:17px">${esc(text)}</text>`
    })
    .join("\n")
}

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
