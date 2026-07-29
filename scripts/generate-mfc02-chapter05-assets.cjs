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
  "chapter-05"
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
    slug: "01-mappa-bando-accertamento-compliance",
    title: "Mappa BANDO dell'accertamento fiscale",
    subtitle: "Dal bando alla sequenza controllo, istruttoria, atto, garanzie e compliance.",
    svg: figureMappaBando()
  },
  {
    slug: "02-sequenza-controllo-accertamento",
    title: "Dal dato all'atto motivato",
    subtitle: "La sequenza operativa per non confondere controllo, accertamento e riscossione.",
    svg: figureSequenza()
  },
  {
    slug: "03-poteri-garanzie-atto",
    title: "Poteri istruttori e garanzie",
    subtitle: "Il potere pubblico acquista senso solo insieme a limiti, motivazione e tutela.",
    svg: figurePoteriGaranzie()
  },
  {
    slug: "04-compliance-rischio-fiscale",
    title: "Compliance fiscale e rischio",
    subtitle: "Prevenire, orientare e selezionare prima che l'anomalia diventi contenzioso.",
    svg: figureCompliance()
  },
  {
    slug: "05-adempimento-collaborativo-tcf",
    title: "Adempimento collaborativo e TCF",
    subtitle: "Il tax control framework collega rischio fiscale, controlli interni e dialogo preventivo.",
    svg: figureAdempimentoCollaborativo()
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
  return `# Asset Capitolo 5 - M-FC02 Accertamento, controlli e compliance fiscale

Figure generate per \`Accertamento, controlli e compliance fiscale\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, sequenza operativa, confronto concettuale, matrice rischio/azione e sintesi anti-errore;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono la mappa del capitolo, la sequenza dato-controllo-atto, il rapporto poteri/garanzie, la compliance come gestione del rischio e l'adempimento collaborativo con tax control framework.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-accertamento-compliance.png\` | \`01-mappa-bando-accertamento-compliance.svg\` | Mappa BANDO del capitolo: controllo, istruttoria, atto, garanzie e compliance. |
| \`02-sequenza-controllo-accertamento.png\` | \`02-sequenza-controllo-accertamento.svg\` | Sequenza dal dato all'atto motivato e alla fase distinta di riscossione. |
| \`03-poteri-garanzie-atto.png\` | \`03-poteri-garanzie-atto.svg\` | Equilibrio tra poteri istruttori, limiti, motivazione, contraddittorio e autotutela. |
| \`04-compliance-rischio-fiscale.png\` | \`04-compliance-rischio-fiscale.svg\` | Compliance come prevenzione, dialogo e selezione del rischio fiscale. |
| \`05-adempimento-collaborativo-tcf.png\` | \`05-adempimento-collaborativo-tcf.svg\` | Tax control framework e adempimento collaborativo nei profili avanzati. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(585, 205, 430, 122, "Accertamento", ["controlli, atto", "garanzie, compliance"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${box(70, 460, 270, 130, "B - Bando", ["accertamento", "compliance"], "navy", "softBlue")}
  ${box(370, 585, 270, 130, "A - Aree", ["controlli", "istruttoria"], "bordeaux", "softRed")}
  ${box(665, 460, 270, 130, "N - Nuclei", ["atto", "motivazione"], "gold", "softGold")}
  ${box(960, 585, 270, 130, "D - Diario", ["riscossione", "contraddittorio"], "green", "softGreen")}
  ${box(1260, 460, 270, 130, "O - Output", ["caso fiscale", "checklist atto"], "teal", "softTeal")}
  ${note(245, 815, 1110, "L'accertamento si studia come sequenza amministrativa, non come elenco di articoli.")}
`
  return shell("Mappa BANDO dell'accertamento fiscale", "Dal bando alla sequenza controllo, istruttoria, atto, garanzie e compliance.", inner)
}

function figureSequenza() {
  const y = 285
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(95, y, "1", "Dato", ["dichiarazione", "versamento", "segnale"], "navy", "softBlue")}
  ${step(355, y, "2", "Controllo", ["coerenza", "documenti", "sostanza"], "bordeaux", "softRed")}
  ${step(615, y, "3", "Istruttoria", ["richieste", "analisi", "elementi"], "gold", "softGold")}
  ${step(875, y, "4", "Confronto", ["garanzie", "chiarimenti"], "green", "softGreen")}
  ${step(1135, y, "5", "Atto", ["motivazione", "pretesa"], "teal", "softTeal")}
  ${arrow(315, y + 82, 345, y + 82, "Navy")}
  ${arrow(575, y + 82, 605, y + 82, "Bordeaux")}
  ${arrow(835, y + 82, 865, y + 82, "Gold")}
  ${arrow(1095, y + 82, 1125, y + 82, "Green")}
  ${smallBox(215, 590, 280, 116, "Esito possibile", ["chiarimento", "archiviazione"], "green", "softGreen")}
  ${smallBox(655, 590, 290, 116, "Atto motivato", ["fatti e regola", "pretesa"], "navy", "softBlue")}
  ${smallBox(1095, 590, 290, 116, "Fase distinta", ["tutela", "riscossione"], "bordeaux", "softRed")}
  ${arrow(495, 648, 635, 648, "Green")}
  ${arrow(945, 648, 1075, 648, "Navy")}
  ${note(245, 815, 1110, "Non ogni controllo produce un atto; non ogni atto coincide con riscossione.")}
`
  return shell("Dal dato all'atto motivato", "La sequenza operativa per non confondere controllo, accertamento e riscossione.", inner)
}

function figurePoteriGaranzie() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${pillar(120, 245, "Poteri", ["richieste", "documenti", "banche dati", "analisi"], "navy", "softBlue")}
  ${arrow(460, 405, 575, 405, "Navy")}
  ${centerBox(590, 285, 420, 240, "Istruttoria", ["trasforma dati e anomalie", "in elementi valutabili"], "gold", "softGold")}
  ${arrow(1025, 405, 1140, 405, "Gold")}
  ${pillar(1160, 245, "Atto", ["motivazione", "destinatario", "pretesa", "rimedi"], "teal", "softTeal")}
  ${guardBox(250, 610, "Limiti", ["base legale", "pertinenza"], "bordeaux", "softRed")}
  ${guardBox(585, 610, "Confronto", ["contraddittorio", "chiarimenti"], "green", "softGreen")}
  ${guardBox(920, 610, "Riesame", ["autotutela", "tutela"], "navy", "softBlue")}
  ${note(245, 815, 1110, "Il potere istruttorio e' efficace solo se resta dentro legalita, motivazione e garanzie.")}
`
  return shell("Poteri istruttori e garanzie", "Il potere pubblico acquista senso solo insieme a limiti, motivazione e tutela.", inner)
}

function figureCompliance() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(575, 205, 450, 145, "Rischio fiscale", ["anomalia, incertezza", "comportamento da presidiare"], "bordeaux", "softRed")}
  <path class="line" d="M800 350 L800 390"/>
  <path class="line" d="M285 390 L1315 390"/>
  ${line(285, 390, 285, 470)}
  ${line(628, 390, 628, 470)}
  ${line(972, 390, 972, 470)}
  ${line(1315, 390, 1315, 470)}
  ${riskCard(120, 470, "Prevenire", ["comunicazioni", "servizi"], "green", "softGreen")}
  ${riskCard(462, 470, "Orientare", ["adempimento", "correzione"], "navy", "softBlue")}
  ${riskCard(805, 470, "Selezionare", ["rischi", "controlli mirati"], "gold", "softGold")}
  ${riskCard(1148, 470, "Accertare", ["se resta", "irregolarita"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Compliance non significa rinuncia al controllo: significa governare prima il rischio.")}
`
  return shell("Compliance fiscale e rischio", "Prevenire, orientare e selezionare prima che l'anomalia diventi contenzioso.", inner)
}

function figureAdempimentoCollaborativo() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${largeBox(110, 255, 370, 300, "Contribuente complesso", ["operazioni articolate", "rischio fiscale elevato", "organizzazione interna"], "navy", "softBlue")}
  ${arrow(500, 405, 610, 405, "Navy")}
  ${largeBox(630, 230, 340, 350, "Tax control framework", ["rileva rischi", "misura e presidia", "assegna responsabilita", "documenta controlli"], "gold", "softGold")}
  ${arrow(990, 405, 1100, 405, "Gold")}
  ${largeBox(1120, 255, 370, 300, "Dialogo preventivo", ["trasparenza", "cooperazione", "minore conflitto"], "green", "softGreen")}
  ${smallBox(450, 640, 700, 92, "Da verificare sempre sul testo vigente", ["requisiti, soglie, procedure e profili ACFI"], "bordeaux", "softRed")}
  ${note(245, 815, 1110, "Nei profili avanzati la parola chiave e' rischio: interno al contribuente, valutato dall'amministrazione.")}
`
  return shell("Adempimento collaborativo e TCF", "Il tax control framework collega rischio fiscale, controlli interni e dialogo preventivo.", inner)
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
      .navy { fill: ${palette.navy}; }
      .bordeaux { fill: ${palette.bordeaux}; }
      .gold { fill: ${palette.gold}; }
      .green { fill: ${palette.green}; }
      .teal { fill: ${palette.teal}; }
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
  <g data-safe-box="120 14 1360 110 0" data-safe-name="header">
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

function smallBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="20"/>
    <text class="ink label" x="${x + 24}" y="${y + 38}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 24}" y="${y + 72 + index * 25}">${esc(lineText)}</text>`).join("\n")}
    <rect x="${x}" y="${y}" width="10" height="${h}" rx="5" fill="${palette[color]}"/>
  </g>`
}

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 220 164 16" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="220" height="164" rx="22"/>
    <circle cx="${x + 40}" cy="${y + 42}" r="22" fill="${palette[color]}"/>
    <text x="${x + 40}" y="${y + 50}" text-anchor="middle" fill="#FFFFFF" style="font: 800 22px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 76}" y="${y + 50}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 26}" y="${y + 92 + index * 25}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function pillar(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 320 310 20" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="320" height="310" rx="26"/>
    <text class="ink label" x="${x + 30}" y="${y + 48}">${esc(title)}</text>
    <rect x="${x + 30}" y="${y + 72}" width="260" height="4" rx="2" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 36}" y="${y + 118 + index * 43}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function centerBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 22" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="28"/>
    <text class="ink label" x="${x + w / 2}" y="${y + 54}" text-anchor="middle">${esc(title)}</text>
    <circle cx="${x + w / 2}" cy="${y + 105}" r="24" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + w / 2}" y="${y + 156 + index * 31}" text-anchor="middle">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function guardBox(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 280 120 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="280" height="120" rx="20"/>
    <text class="ink label" x="${x + 24}" y="${y + 38}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 24}" y="${y + 72 + index * 25}">${esc(lineText)}</text>`).join("\n")}
    <circle cx="${x + 240}" cy="${y + 42}" r="14" fill="${palette[color]}"/>
  </g>`
}

function riskCard(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 305 180 18" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="305" height="180" rx="24"/>
    <circle cx="${x + 45}" cy="${y + 46}" r="18" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 76}" y="${y + 54}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 30}" y="${y + 104 + index * 29}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function largeBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 24" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="28"/>
    <text class="ink label" x="${x + 30}" y="${y + 50}">${esc(title)}</text>
    <rect x="${x + 30}" y="${y + 75}" width="${w - 60}" height="4" rx="2" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 34}" y="${y + 122 + index * 38}">${esc(lineText)}</text>`).join("\n")}
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
