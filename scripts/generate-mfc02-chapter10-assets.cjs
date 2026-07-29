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
  "chapter-10"
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
    slug: "01-mappa-bando-territorio-spi",
    title: "Mappa BANDO Territorio e SPI",
    subtitle: "Catasto, cartografia, estimo, OMI e pubblicita immobiliare come mappa da concorso.",
    svg: figureMappaBando()
  },
  {
    slug: "02-sistema-catasto-cartografia-estimo-spi",
    title: "Sistema Territorio Agenzia Entrate",
    subtitle: "Identificare, rappresentare, valutare e rendere conoscibili le vicende immobiliari.",
    svg: figureSistemaTerritorio()
  },
  {
    slug: "03-identificativo-classamento-rendita",
    title: "Identificativo, classamento e rendita",
    subtitle: "Dal Comune al subalterno, poi categoria, classe, consistenza e rendita catastale.",
    svg: figureIdentificativo()
  },
  {
    slug: "04-servizi-procedure-territorio",
    title: "Servizi e procedure del Territorio",
    subtitle: "Visura, planimetria, voltura, rettifica, cartografia, ispezione e OMI.",
    svg: figureServizi()
  },
  {
    slug: "05-checklist-catasto-pubblicita-immobiliare",
    title: "Checklist Catasto e pubblicita immobiliare",
    subtitle: "Dato, mappa, valore e formalita vanno separati prima di rispondere.",
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
  return `# Asset Capitolo 10 - M-FC02 Catasto, cartografia, estimo e pubblicita immobiliare

Figure generate per \`Catasto, cartografia, estimo e pubblicita immobiliare\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, sequenza operativa, confronto concettuale, schema anti-confusione e checklist applicativa;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO, sistema Territorio/SPI, identificativo-classamento-rendita, servizi/procedure e checklist finale.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-territorio-spi.png\` | \`01-mappa-bando-territorio-spi.svg\` | Mappa BANDO del capitolo: profili AE Territorio e SPI, nuclei, errori e output. |
| \`02-sistema-catasto-cartografia-estimo-spi.png\` | \`02-sistema-catasto-cartografia-estimo-spi.svg\` | Schema dei quattro piani: catasto, cartografia, estimo/OMI e pubblicita immobiliare. |
| \`03-identificativo-classamento-rendita.png\` | \`03-identificativo-classamento-rendita.svg\` | Sequenza per leggere un immobile: Comune, foglio, particella, subalterno, classamento e rendita. |
| \`04-servizi-procedure-territorio.png\` | \`04-servizi-procedure-territorio.svg\` | Mappa dei servizi: visura, planimetria, voltura, rettifica, cartografia, ispezione e OMI. |
| \`05-checklist-catasto-pubblicita-immobiliare.png\` | \`05-checklist-catasto-pubblicita-immobiliare.svg\` | Checklist visuale per separare dato catastale, mappa, valore e formalita. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(555, 205, 490, 122, "AE Territorio / SPI", ["catasto, mappe", "estimo e registri"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${box(70, 460, 270, 130, "B - Bando", ["profili SPI", "tecnici territorio"], "navy", "softBlue")}
  ${box(370, 585, 270, 130, "A - Aree", ["catasto OMI", "registri"], "bordeaux", "softRed")}
  ${box(665, 460, 270, 130, "N - Nuclei", ["dato, mappa", "valore formalita"], "gold", "softGold")}
  ${box(960, 585, 270, 130, "D - Diario", ["visura/proprieta", "rendita/mercato"], "green", "softGreen")}
  ${box(1260, 460, 270, 130, "O - Output", ["glossario", "caso e checklist"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Il capitolo si studia separando dato catastale, mappa, valore e formalita.")}
`
  return shell("Mappa BANDO Territorio e SPI", "Catasto, cartografia, estimo, OMI e pubblicita immobiliare come mappa da concorso.", inner)
}

function figureSistemaTerritorio() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(555, 218, 490, 138, "Sistema Territorio AE", ["banche dati, servizi", "utenti e professionisti"], "navy", "softBlue")}
  <path class="line" d="M800 356 L800 408"/>
  <path class="line" d="M280 408 L1320 408"/>
  ${line(280, 408, 280, 500)}
  ${line(540, 408, 540, 500)}
  ${line(800, 408, 800, 500)}
  ${line(1060, 408, 1060, 500)}
  ${line(1320, 408, 1320, 500)}
  ${tile(110, 500, 290, "Catasto", ["identifica", "classifica"], "navy", "softBlue")}
  ${tile(455, 500, 290, "Cartografia", ["rappresenta", "particelle"], "bordeaux", "softRed")}
  ${tile(800, 500, 290, "Estimo / OMI", ["valuta", "osserva mercato"], "gold", "softGold")}
  ${tile(1145, 500, 290, "Pubblicita", ["registri", "formalita"], "teal", "softTeal")}
  ${smallBox(520, 695, 560, 82, "Regola anti-confusione", ["i quattro piani dialogano, ma non coincidono"], "green", "softGreen")}
  ${note(245, 815, 1110, "Il candidato deve classificare la domanda prima di scegliere servizio o banca dati.")}
`
  return shell("Sistema Territorio Agenzia Entrate", "Identificare, rappresentare, valutare e rendere conoscibili le vicende immobiliari.", inner)
}

function figureIdentificativo() {
  const y = 305
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(110, y, "1", "Comune", ["base", "territoriale"], "navy", "softBlue")}
  ${step(340, y, "2", "Foglio", ["porzione", "di mappa"], "bordeaux", "softRed")}
  ${step(570, y, "3", "Particella", ["area o", "mappale"], "gold", "softGold")}
  ${step(800, y, "4", "Subalterno", ["unita", "distinta"], "green", "softGreen")}
  ${step(1030, y, "5", "Classam.", ["categoria", "classe"], "teal", "softTeal")}
  ${step(1260, y, "6", "Rendita", ["dato", "catastale"], "navy", "softBlue")}
  ${arrow(280, y + 82, 330, y + 82, "Navy")}
  ${arrow(510, y + 82, 560, y + 82, "Bordeaux")}
  ${arrow(740, y + 82, 790, y + 82, "Gold")}
  ${arrow(970, y + 82, 1020, y + 82, "Green")}
  ${arrow(1200, y + 82, 1250, y + 82, "Teal")}
  ${smallBox(260, 595, 330, 106, "Identificazione", ["prima localizzo il bene"], "bordeaux", "softRed")}
  ${smallBox(635, 595, 330, 106, "Classamento", ["poi qualifico l'unita"], "gold", "softGold")}
  ${smallBox(1010, 595, 330, 106, "Cautela", ["non prova da sola proprieta"], "green", "softGreen")}
  ${note(245, 815, 1110, "La sequenza evita di confondere identificativo, classamento, rendita e titolo giuridico.")}
`
  return shell("Identificativo, classamento e rendita", "Dal Comune al subalterno, poi categoria, classe, consistenza e rendita catastale.", inner)
}

function figureServizi() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(560, 220, 480, 138, "Domanda dell'utente", ["consultare, aggiornare", "verificare o stimare"], "navy", "softBlue")}
  ${arrow(800, 358, 800, 420, "Navy")}
  ${option(105, 460, "Visura", ["dati catastali", "immobile o soggetto"], "navy", "softBlue")}
  ${option(450, 460, "Planimetria", ["unita urbana", "rappresentazione"], "bordeaux", "softRed")}
  ${option(795, 460, "Voltura", ["intestazioni", "catastali"], "gold", "softGold")}
  ${option(1140, 460, "Ispezione", ["registri", "formalita"], "teal", "softTeal")}
  ${smallBox(280, 660, 315, 92, "Rettifica", ["corregge dati non coerenti"], "green", "softGreen")}
  ${smallBox(645, 660, 315, 92, "Cartografia", ["mappe e particelle"], "bordeaux", "softRed")}
  ${smallBox(1010, 660, 315, 92, "OMI", ["quotazioni di supporto"], "gold", "softGold")}
  ${note(245, 815, 1110, "Ogni servizio risponde a una domanda diversa: dato, disegno, intestazione, registri o mercato.")}
`
  return shell("Servizi e procedure del Territorio", "Visura, planimetria, voltura, rettifica, cartografia, ispezione e OMI.", inner)
}

function figureChecklist() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${checkItem(130, 225, 415, "1. Blocco", ["catasto, OMI o SPI"], "navy", "softBlue")}
  ${checkItem(130, 335, 415, "2. Identificativo", ["Comune foglio particella"], "bordeaux", "softRed")}
  ${checkItem(130, 445, 415, "3. Dato", ["categoria classe rendita"], "gold", "softGold")}
  ${checkItem(130, 555, 415, "4. Servizio", ["visura voltura ispezione"], "green", "softGreen")}
  ${checkItem(1055, 225, 415, "5. Mappa", ["cartografia o planimetria"], "teal", "softTeal")}
  ${checkItem(1055, 335, 415, "6. Valore", ["stima e OMI"], "gold", "softGold")}
  ${checkItem(1055, 445, 415, "7. Formalita", ["trascrizione iscrizione"], "bordeaux", "softRed")}
  ${checkItem(1055, 555, 415, "8. Cautela", ["fonti tecniche vigenti"], "navy", "softBlue")}
  ${center(595, 335, 410, 205, "Risposta Territorio", ["dato", "mappa", "valore", "formalita"], "navy", "softBlue")}
  ${arrow(555, 410, 585, 410, "Green")}
  ${arrow(1015, 410, 1045, 410, "Teal")}
  ${smallBox(600, 585, 400, 86, "Regola d'esame", ["non confondere visura e prova"], "gold", "softGold")}
  ${note(245, 815, 1110, "Prima separa il piano della domanda, poi cita servizio, limite e fonte da verificare.")}
`
  return shell("Checklist Catasto e pubblicita immobiliare", "Dato, mappa, valore e formalita vanno separati prima di rispondere.", inner)
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

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 170 164 6" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="170" height="164" rx="22"/>
    <circle cx="${x + 34}" cy="${y + 38}" r="21" fill="${palette[color]}"/>
    <text x="${x + 34}" y="${y + 46}" text-anchor="middle" fill="#FFFFFF" style="font: 800 21px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 28}" y="${y + 82}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 28}" y="${y + 116 + index * 23}">${esc(lineText)}</text>`).join("\n")}
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

function option(x, y, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 360 155 12" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="360" height="155" rx="24"/>
    <text class="ink label" x="${x + 30}" y="${y + 46}">${esc(title)}</text>
    <rect x="${x + 30}" y="${y + 68}" width="300" height="4" rx="2" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 32}" y="${y + 105 + index * 27}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function tile(x, y, w, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} 150 12" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="150" rx="24"/>
    <text class="ink label" x="${x + 30}" y="${y + 46}">${esc(title)}</text>
    <rect x="${x + 30}" y="${y + 68}" width="${w - 60}" height="4" rx="2" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 32}" y="${y + 105 + index * 27}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function smallBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
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
