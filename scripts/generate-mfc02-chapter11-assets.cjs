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
  "chapter-11"
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
    slug: "01-mappa-bando-bilancio-fisco",
    title: "Mappa BANDO Bilancio e fisco",
    subtitle: "Dal bando alla risposta su bilancio, scritture, errori e mini-casi.",
    svg: figureMappaBando()
  },
  {
    slug: "02-bilancio-quattro-documenti",
    title: "Bilancio d'esercizio in quattro documenti",
    subtitle: "Stato patrimoniale, conto economico, rendiconto e nota integrativa.",
    svg: figureBilancioDocumenti()
  },
  {
    slug: "03-ricavi-costi-incassi-pagamenti",
    title: "Ricavi, costi, incassi e pagamenti",
    subtitle: "Competenza economica e flussi monetari non coincidono sempre.",
    svg: figureRicaviCosti()
  },
  {
    slug: "04-utile-reddito-imposta",
    title: "Utile, reddito fiscale e imposta",
    subtitle: "Tre piani collegati ma distinti: bilancio, regole tributarie, dichiarazione.",
    svg: figureUtileRedditoImposta()
  },
  {
    slug: "05-checklist-bilancio-fisco",
    title: "Checklist Bilancio-Fisco",
    subtitle: "Prima separa documento, grandezza, piano fiscale, errore e output.",
    svg: figureChecklist()
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
  return `# Asset Capitolo 11 - M-FC02 Contabilita aziendale ed economia d'impresa per il fisco

Figure generate per \`Contabilita aziendale ed economia d'impresa per il fisco\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, schema concettuale, sequenza operativa, schema anti-confusione e checklist applicativa;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO, documenti del bilancio, differenza ricavi/costi e incassi/pagamenti, raccordo utile/reddito/imposta e checklist finale.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-bilancio-fisco.png\` | \`01-mappa-bando-bilancio-fisco.svg\` | Mappa BANDO del capitolo: bilancio, scritture, nuclei, errori e output. |
| \`02-bilancio-quattro-documenti.png\` | \`02-bilancio-quattro-documenti.svg\` | Schema dei quattro documenti del bilancio e delle domande da concorso. |
| \`03-ricavi-costi-incassi-pagamenti.png\` | \`03-ricavi-costi-incassi-pagamenti.svg\` | Anti-confusione tra competenza economica e flussi monetari. |
| \`04-utile-reddito-imposta.png\` | \`04-utile-reddito-imposta.svg\` | Sequenza dal risultato civilistico alla dichiarazione e al controllo. |
| \`05-checklist-bilancio-fisco.png\` | \`05-checklist-bilancio-fisco.svg\` | Checklist visuale per impostare mini-casi e risposta orale. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(555, 205, 490, 122, "Bilancio e fisco", ["impresa come contribuente", "dati, documenti, controlli"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${box(70, 460, 270, 130, "B - Bando", ["contabilita", "economia impresa"], "navy", "softBlue")}
  ${box(370, 585, 270, 130, "A - Aree", ["bilancio", "scritture e fisco"], "bordeaux", "softRed")}
  ${box(665, 460, 270, 130, "N - Nuclei", ["ricavi, costi", "patrimonio"], "gold", "softGold")}
  ${box(960, 585, 270, 130, "D - Diario", ["utile/reddito", "ricavo/incasso"], "green", "softGreen")}
  ${box(1260, 460, 270, 130, "O - Output", ["mini-caso", "risposta orale"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Il capitolo trasforma il bilancio in mappa operativa per dichiarazioni e controlli.")}`

  return shell("Mappa BANDO Bilancio e fisco", "Dal bando alla risposta su bilancio, scritture, errori e mini-casi.", inner)
}

function figureBilancioDocumenti() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(530, 215, 540, 132, "Bilancio d'esercizio", ["rappresentazione patrimoniale", "finanziaria ed economica"], "navy", "softBlue")}
  ${arrow(800, 347, 800, 410, "Navy")}
  <path class="line" d="M260 410 L1340 410"/>
  ${line(260, 410, 260, 490)}
  ${line(620, 410, 620, 490)}
  ${line(980, 410, 980, 490)}
  ${line(1340, 410, 1340, 490)}
  ${docCard(100, 490, "Stato patr.", ["attivita", "passivita", "patrimonio"], "navy", "softBlue")}
  ${docCard(460, 490, "Conto econ.", ["ricavi", "costi", "risultato"], "bordeaux", "softRed")}
  ${docCard(820, 490, "Rendiconto", ["flussi", "liquidita", "incassi/pag."], "gold", "softGold")}
  ${docCard(1180, 490, "Nota integr.", ["criteri", "dettagli", "chiarimenti"], "teal", "softTeal")}
  ${smallBox(320, 705, 960, 72, "Domanda guida", ["che cosa racconta il documento e quale dato puo' interessare al fisco?"], "green", "softGreen")}
  ${note(245, 815, 1110, "La prova non chiede tutto il bilancio: chiede di non confondere funzione e documento.")}`

  return shell("Bilancio d'esercizio in quattro documenti", "Stato patrimoniale, conto economico, rendiconto e nota integrativa.", inner)
}

function figureRicaviCosti() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${lane(125, 250, "Piano economico", ["ricavo", "costo", "utile/perdita"], "navy", "softBlue")}
  ${lane(1085, 250, "Piano monetario", ["incasso", "pagamento", "liquidita"], "green", "softGreen")}
  ${arrow(535, 345, 690, 345, "Navy")}
  ${bridge(650, 270, "Competenza", ["a quale esercizio", "si riferisce?"], "gold", "softGold")}
  ${arrow(910, 345, 1065, 345, "Green")}
  ${exampleBox(220, 560, "Esempio 1", ["vendo a dicembre", "incasso a gennaio"], "bordeaux", "softRed")}
  ${exampleBox(610, 560, "Esempio 2", ["pago oggi", "costo su piu esercizi"], "gold", "softGold")}
  ${exampleBox(1000, 560, "Regola", ["dato economico", "non sempre flusso"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Ricavo non significa incasso; costo non significa pagamento: prima individua il piano.")}`

  return shell("Ricavi, costi, incassi e pagamenti", "Competenza economica e flussi monetari non coincidono sempre.", inner)
}

function figureUtileRedditoImposta() {
  const y = 290
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(95, y, "1", "Operazione", ["vendita", "acquisto"], "navy", "softBlue")}
  ${step(330, y, "2", "Scrittura", ["dato contabile", "documento"], "bordeaux", "softRed")}
  ${step(565, y, "3", "Bilancio", ["utile o", "perdita"], "gold", "softGold")}
  ${step(800, y, "4", "Regole fisc.", ["variazioni", "limiti"], "green", "softGreen")}
  ${step(1035, y, "5", "Dichiaraz.", ["base", "posizione"], "teal", "softTeal")}
  ${step(1270, y, "6", "Controllo", ["coerenza", "documenti"], "navy", "softBlue")}
  ${arrow(275, y + 82, 320, y + 82, "Navy")}
  ${arrow(510, y + 82, 555, y + 82, "Bordeaux")}
  ${arrow(745, y + 82, 790, y + 82, "Gold")}
  ${arrow(980, y + 82, 1025, y + 82, "Green")}
  ${arrow(1215, y + 82, 1260, y + 82, "Teal")}
  ${smallBox(270, 575, 340, 104, "Da evitare", ["utile = imponibile", "imposta = risultato"], "bordeaux", "softRed")}
  ${smallBox(635, 575, 340, 104, "Da dire", ["civilistico, fiscale", "e imposta sono piani"], "green", "softGreen")}
  ${smallBox(1000, 575, 340, 104, "Uso in prova", ["spiega sequenza", "non fare consulenza"], "gold", "softGold")}
  ${note(245, 815, 1110, "Il bilancio alimenta il fisco, ma la base imponibile segue le regole tributarie.")}`

  return shell("Utile, reddito fiscale e imposta", "Tre piani collegati ma distinti: bilancio, regole tributarie, dichiarazione.", inner)
}

function figureChecklist() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${checkItem(130, 225, 415, "1. Profilo", ["AE, ADM o AdER"], "navy", "softBlue")}
  ${checkItem(130, 335, 415, "2. Documento", ["bilancio, fattura, debito"], "bordeaux", "softRed")}
  ${checkItem(130, 445, 415, "3. Grandezza", ["ricavi, costi, crediti"], "gold", "softGold")}
  ${checkItem(130, 555, 415, "4. Piano", ["economico o monetario"], "green", "softGreen")}
  ${checkItem(1055, 225, 415, "5. Fisco", ["redditi, IVA, controlli"], "teal", "softTeal")}
  ${checkItem(1055, 335, 415, "6. Rischio", ["utile/reddito/imposta"], "gold", "softGold")}
  ${checkItem(1055, 445, 415, "7. Output", ["caso, quiz, orale"], "bordeaux", "softRed")}
  ${checkItem(1055, 555, 415, "8. Review", ["fonti e periodo"], "navy", "softBlue")}
  ${center(595, 335, 410, 205, "Risposta bilancio-fisco", ["dato", "regola", "cautela", "controllo"], "navy", "softBlue")}
  ${arrow(555, 410, 585, 410, "Green")}
  ${arrow(1015, 410, 1045, 410, "Teal")}
  ${smallBox(600, 585, 400, 86, "Regola d'esame", ["mai fondere i piani"], "gold", "softGold")}
  ${note(245, 815, 1110, "La checklist serve a impostare mini-casi contabili senza perdere il collegamento fiscale.")}`

  return shell("Checklist Bilancio-Fisco", "Prima separa documento, grandezza, piano fiscale, errore e output.", inner)
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

function docCard(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 320 170 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="320" height="170" rx="24"/>
    <text class="ink label" x="${x + 28}" y="${y + 46}">${esc(title)}</text>
    <rect x="${x + 28}" y="${y + 68}" width="264" height="4" rx="2" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 30}" y="${y + 105 + index * 27}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function lane(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 410 235 16" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="410" height="235" rx="28"/>
    <text class="ink label" x="${x + 34}" y="${y + 50}">${esc(title)}</text>
    <rect x="${x + 34}" y="${y + 76}" width="342" height="5" rx="2.5" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 42}" y="${y + 125 + index * 38}">- ${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function bridge(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 300 150 12" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="300" height="150" rx="75"/>
    <text class="ink label" x="${x + 150}" y="${y + 55}" text-anchor="middle">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 150}" y="${y + 92 + index * 24}" text-anchor="middle">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function exampleBox(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 360 130 10" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="360" height="130" rx="24"/>
    <rect x="${x}" y="${y}" width="10" height="130" rx="5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 30}" y="${y + 42}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 32}" y="${y + 80 + index * 28}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 180 164 6" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="180" height="164" rx="22"/>
    <circle cx="${x + 34}" cy="${y + 38}" r="21" fill="${palette[color]}"/>
    <text x="${x + 34}" y="${y + 46}" text-anchor="middle" fill="#FFFFFF" style="font: 800 21px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 24}" y="${y + 82}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 24}" y="${y + 116 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function smallBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="20"/>
    <text class="ink label" x="${x + 24}" y="${y + 36}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 24}" y="${y + 68 + index * 23}">${esc(lineText)}</text>`).join("\n")}
    <rect x="${x}" y="${y}" width="10" height="${h}" rx="5" fill="${palette[color]}"/>
  </g>`
}

function checkItem(x, y, w, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} 88 10" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="88" rx="20"/>
    <rect x="${x}" y="${y}" width="10" height="88" rx="5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 26}" y="${y + 35}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 28}" y="${y + 64 + index * 22}">${esc(lineText)}</text>`).join("\n")}
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
