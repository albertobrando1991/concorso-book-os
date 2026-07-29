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
  "chapter-12"
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
    slug: "01-mappa-bando-civile-commerciale",
    title: "Mappa BANDO civile e commerciale",
    subtitle: "Obbligazioni, contratti, impresa, societa e crisi solo quando servono al caso.",
    svg: figureMappaBando()
  },
  {
    slug: "02-credito-debito-piani-giuridici",
    title: "Credito, debito e piani giuridici",
    subtitle: "Rapporto privato, obbligo tributario e riscossione non sono la stessa cosa.",
    svg: figureCreditoDebito()
  },
  {
    slug: "03-contratto-fattura-pagamento",
    title: "Contratto, fattura e pagamento",
    subtitle: "Tre piani collegati ma distinti: rapporto, documento, flusso monetario.",
    svg: figureContrattoFatturaPagamento()
  },
  {
    slug: "04-impresa-societa-applicazioni-agenzie",
    title: "Impresa e societa nelle Agenzie fiscali",
    subtitle: "Lo stesso soggetto cambia lettura in AE, ADM e AdER.",
    svg: figureImpresaSocietaAgenzie()
  },
  {
    slug: "05-checklist-civile-commerciale-fisco",
    title: "Checklist civile-commerciale M-FC02",
    subtitle: "Prima separa soggetto, rapporto, documento, patrimonio, poteri e piano prevalente.",
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
  return `# Asset Capitolo 12 - M-FC02 Civile e commerciale applicati a fisco, dogane e riscossione

Figure generate per \`Civile e commerciale applicati a fisco, dogane e riscossione\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, schema anti-confusione, sequenza operativa, mappa applicativa e checklist;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO, distinzione credito/debito e piani giuridici, contratto/fattura/pagamento, applicazione AE-ADM-AdER e checklist finale.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-civile-commerciale.png\` | \`01-mappa-bando-civile-commerciale.svg\` | Mappa BANDO del capitolo: bando, aree, nuclei, diario errori e output. |
| \`02-credito-debito-piani-giuridici.png\` | \`02-credito-debito-piani-giuridici.svg\` | Anti-confusione tra rapporto privato, obbligo tributario e riscossione. |
| \`03-contratto-fattura-pagamento.png\` | \`03-contratto-fattura-pagamento.svg\` | Sequenza contratto-documento-pagamento-contabilita-fisco. |
| \`04-impresa-societa-applicazioni-agenzie.png\` | \`04-impresa-societa-applicazioni-agenzie.svg\` | Mappa applicativa dello stesso soggetto in AE, ADM e AdER. |
| \`05-checklist-civile-commerciale-fisco.png\` | \`05-checklist-civile-commerciale-fisco.svg\` | Checklist visuale per casi e orale su civile/commerciale M-FC02. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(520, 198, 560, 145, "Civile/commerciale M-FC02", ["serve al caso fiscale", "non e' un corso autonomo"], "navy", "softBlue")}
  <path class="line" d="M800 343 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 462)}
  ${line(505, 370, 505, 590)}
  ${line(800, 370, 800, 462)}
  ${line(1095, 370, 1095, 590)}
  ${line(1395, 370, 1395, 462)}
  ${box(70, 462, 270, 132, "B - Bando", ["civile", "commerciale"], "navy", "softBlue")}
  ${box(370, 590, 270, 132, "A - Aree", ["obbligazioni", "contratti"], "bordeaux", "softRed")}
  ${box(665, 462, 270, 132, "N - Nuclei", ["impresa", "societa"], "gold", "softGold")}
  ${box(960, 590, 270, 132, "D - Diario", ["piani confusi", "crisi generica"], "green", "softGreen")}
  ${box(1260, 462, 270, 132, "O - Output", ["caso", "checklist"], "teal", "softTeal")}
  ${note(245, 815, 1110, "La materia entra solo dove aiuta a leggere soggetti, rapporti, debiti e documenti.")}`

  return shell("Mappa BANDO civile e commerciale", "Obbligazioni, contratti, impresa, societa e crisi solo quando servono al caso.", inner)
}

function figureCreditoDebito() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(575, 205, 450, 108, "Parola comune", ["credito / debito"], "gold", "softGold")}
  ${arrow(800, 315, 800, 375, "Gold")}
  <path class="line" d="M300 375 L1300 375"/>
  ${line(300, 375, 300, 455)}
  ${line(800, 375, 800, 455)}
  ${line(1300, 375, 1300, 455)}
  ${panel(115, 455, 370, 170, "Rapporto privato", ["contratto", "fornitore/cliente", "adempimento"], "navy", "softBlue")}
  ${panel(615, 455, 370, 170, "Obbligo tributario", ["presupposto", "dichiarazione/versamento", "disciplina pubblica"], "bordeaux", "softRed")}
  ${panel(1115, 455, 370, 170, "Riscossione", ["ente creditore", "cartella/posizione", "pagamento o tutela"], "teal", "softTeal")}
  ${smallBox(365, 675, 870, 88, "Regola anti-trappola", ["stessa parola, fonte diversa, rimedi diversi, competenza diversa"], "green", "softGreen")}
  ${note(245, 815, 1110, "Prima qualifica il piano: civile, tributario o riscossione. Poi rispondi.")}`

  return shell("Credito, debito e piani giuridici", "Rapporto privato, obbligo tributario e riscossione non sono la stessa cosa.", inner)
}

function figureContrattoFatturaPagamento() {
  const y = 305
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(110, y, "1", "Contratto", ["rapporto", "operazione"], "navy", "softBlue")}
  ${step(375, y, "2", "Fattura", ["documento", "fiscale"], "bordeaux", "softRed")}
  ${step(640, y, "3", "Pagamento", ["flusso", "monetario"], "gold", "softGold")}
  ${step(905, y, "4", "Contabilita", ["ricavi/costi", "crediti/debiti"], "green", "softGreen")}
  ${step(1170, y, "5", "Fisco", ["imposte", "controlli"], "teal", "softTeal")}
  ${arrow(300, y + 82, 365, y + 82, "Navy")}
  ${arrow(565, y + 82, 630, y + 82, "Bordeaux")}
  ${arrow(830, y + 82, 895, y + 82, "Gold")}
  ${arrow(1095, y + 82, 1160, y + 82, "Green")}
  ${smallBox(260, 575, 330, 106, "Errore 1", ["fattura =", "contratto completo"], "bordeaux", "softRed")}
  ${smallBox(635, 575, 330, 106, "Errore 2", ["ricavo =", "incasso"], "gold", "softGold")}
  ${smallBox(1010, 575, 330, 106, "Risposta", ["separa i piani", "e poi collega"], "green", "softGreen")}
  ${note(245, 815, 1110, "Un caso fiscale ben risolto distingue rapporto, documento, denaro, scrittura e imposta.")}`

  return shell("Contratto, fattura e pagamento", "Tre piani collegati ma distinti: rapporto, documento, flusso monetario.", inner)
}

function figureImpresaSocietaAgenzie() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(560, 202, 480, 145, "Impresa / societa", ["soggetto, patrimonio", "documenti e poteri"], "navy", "softBlue")}
  ${arrow(800, 347, 800, 390, "Navy")}
  <path class="line" d="M280 390 L1320 390"/>
  ${line(280, 390, 280, 470)}
  ${line(800, 390, 800, 470)}
  ${line(1320, 390, 1320, 470)}
  ${panel(110, 470, 340, 165, "AE", ["dichiarazioni", "bilancio", "controlli"], "bordeaux", "softRed")}
  ${panel(630, 470, 340, 165, "ADM", ["merce", "operatore", "documenti"], "teal", "softTeal")}
  ${panel(1150, 470, 340, 165, "AdER", ["debitore", "posizione", "rateizzazione"], "green", "softGreen")}
  ${smallBox(365, 675, 870, 88, "Domanda guida", ["chi agisce, con quale potere, per quale rapporto e con quale patrimonio?"], "gold", "softGold")}
  ${note(245, 815, 1110, "Lo stesso soggetto va letto in modo diverso a seconda dell'agenzia e del caso.")}`

  return shell("Impresa e societa nelle Agenzie fiscali", "Lo stesso soggetto cambia lettura in AE, ADM e AdER.", inner)
}

function figureChecklist() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${checkItem(130, 220, 430, "1. Soggetto", ["persona, societa, ente"], "navy", "softBlue")}
  ${checkItem(130, 330, 430, "2. Rapporto", ["contratto o obbligo"], "bordeaux", "softRed")}
  ${checkItem(130, 440, 430, "3. Documento", ["fattura, bilancio, cartella"], "gold", "softGold")}
  ${checkItem(130, 550, 430, "4. Patrimonio", ["beni, crediti, debiti"], "green", "softGreen")}
  ${checkItem(1040, 220, 430, "5. Poteri", ["rappresentante o delega"], "teal", "softTeal")}
  ${checkItem(1040, 330, 430, "6. Piano", ["civile, fisco, dogane"], "gold", "softGold")}
  ${checkItem(1040, 440, 430, "7. Crisi", ["alert, non automatismo"], "bordeaux", "softRed")}
  ${checkItem(1040, 550, 430, "8. Output", ["caso, quiz, orale"], "navy", "softBlue")}
  ${center(610, 350, 380, 175, "Risposta solida", ["qualifica", "separa", "collega"], "navy", "softBlue")}
  ${arrow(570, 410, 600, 410, "Green")}
  ${arrow(1000, 410, 1030, 410, "Teal")}
  ${smallBox(615, 575, 370, 82, "Regola d'esame", ["non fondere i piani"], "gold", "softGold")}
  ${note(245, 815, 1110, "La checklist trasforma una domanda privata in una risposta utile per fisco, dogane o riscossione.")}`

  return shell("Checklist civile-commerciale M-FC02", "Prima separa soggetto, rapporto, documento, patrimonio, poteri e piano prevalente.", inner)
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
  return `<g data-safe-box="${x} ${y} ${w} ${h} 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <circle cx="${x + 38}" cy="${y + 38}" r="17" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 66}" y="${y + 45}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 26}" y="${y + 82 + index * 27}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function center(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="26"/>
    <circle cx="${x + 44}" cy="${y + 44}" r="18" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 74}" y="${y + 52}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 34}" y="${y + 92 + index * 28}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function panel(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="24"/>
    <rect x="${x}" y="${y}" width="11" height="${h}" rx="5.5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 32}" y="${y + 45}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 34}" y="${y + 84 + index * 29}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 190 170 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="190" height="170" rx="22"/>
    <circle cx="${x + 36}" cy="${y + 38}" r="21" fill="${palette[color]}"/>
    <text x="${x + 36}" y="${y + 46}" text-anchor="middle" fill="#FFFFFF" style="font: 800 21px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 24}" y="${y + 82}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 24}" y="${y + 116 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function smallBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="20"/>
    <rect x="${x}" y="${y}" width="10" height="${h}" rx="5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 24}" y="${y + 36}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 24}" y="${y + 68 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function checkItem(x, y, w, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} 88 0" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="88" rx="20"/>
    <rect x="${x}" y="${y}" width="10" height="88" rx="5" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 26}" y="${y + 35}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 28}" y="${y + 64 + index * 22}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function note(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 54 0" data-safe-name="nota">
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
