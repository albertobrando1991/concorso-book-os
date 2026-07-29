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
  "chapter-03"
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
  white: "#FFFFFF",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5"
}

const figures = [
  {
    slug: "01-mappa-bando-organizzazione-fiscale",
    title: "Mappa BANDO dell'organizzazione fiscale",
    subtitle: "Dal bando alla risposta orale su ente, funzione, lessico e rischio.",
    svg: figureMappaBando()
  },
  {
    slug: "02-modello-mef-agenzie-fiscali",
    title: "MEF, agenzie fiscali e riscossione",
    subtitle: "Indirizzo e vigilanza non coincidono con le funzioni tecnico-operative.",
    svg: figureMefAgenzie()
  },
  {
    slug: "03-tre-funzioni-ae-adm-ader",
    title: "Le tre funzioni da non confondere",
    subtitle: "Entrate e servizi fiscali, dogane e monopoli, riscossione nazionale.",
    svg: figureTreFunzioni()
  },
  {
    slug: "04-centro-territorio-canali",
    title: "Organizzazione centrale e rete territoriale",
    subtitle: "Il centro coordina; il territorio incontra contribuenti, operatori e debitori.",
    svg: figureCentroTerritorio()
  },
  {
    slug: "05-accertamento-riscossione",
    title: "Accertamento e riscossione",
    subtitle: "Due fasi collegate ma diverse: pretesa, carico, pagamento e relazione.",
    svg: figureAccertamentoRiscossione()
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
  return `# Asset Capitolo 3 - M-FC02 Ordinamento e organizzazione di AE, ADM e AdER

Figure generate per \`Ordinamento e organizzazione di AE, ADM e AdER\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, schema istituzionale, confronto tra percorsi, sequenza operativa e sintesi anti-errore;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono la mappa BANDO dell'organizzazione, il rapporto MEF/agenzie, le tre funzioni AE/ADM/AdER, il rapporto centro/territorio e la distinzione accertamento/riscossione.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-organizzazione-fiscale.png\` | \`01-mappa-bando-organizzazione-fiscale.svg\` | Mappa BANDO del capitolo: ente, funzione, lessico, diario e risposta. |
| \`02-modello-mef-agenzie-fiscali.png\` | \`02-modello-mef-agenzie-fiscali.svg\` | Rapporto tra MEF, agenzie fiscali e soggetto della riscossione. |
| \`03-tre-funzioni-ae-adm-ader.png\` | \`03-tre-funzioni-ae-adm-ader.svg\` | Distinzione AE/ADM/AdER come tre funzioni operative. |
| \`04-centro-territorio-canali.png\` | \`04-centro-territorio-canali.svg\` | Schema centro, rete territoriale e canali di contatto. |
| \`05-accertamento-riscossione.png\` | \`05-accertamento-riscossione.svg\` | Anti-confusione tra accertamento e riscossione. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${node(585, 205, 430, 118, "Organizzazione fiscale", ["ente, funzione", "lessico da prova"], "navy", "softBlue")}
  <path class="line" d="M800 323 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 455)}
  ${line(505, 370, 505, 580)}
  ${line(800, 370, 800, 455)}
  ${line(1095, 370, 1095, 580)}
  ${line(1395, 370, 1395, 455)}
  ${node(70, 455, 270, 130, "B - Bando", ["ente", "profilo"], "navy", "softBlue")}
  ${node(370, 580, 270, 130, "A - Aree", ["entrate", "dogane, riscossione"], "bordeaux", "softRed")}
  ${node(665, 455, 270, 130, "N - Nuclei", ["MEF", "autonomia, uffici"], "gold", "softGold")}
  ${node(960, 580, 270, 130, "D - Diario", ["AE/ADM", "accert./riscossione"], "green", "softGreen")}
  ${node(1260, 455, 270, 130, "O - Output", ["risposta orale", "scheda funzione/prova"], "teal", "softTeal")}
  ${note(255, 815, 1090, "L'organizzazione serve alla prova quando diventa mappa di funzioni, non elenco di uffici.")}
`
  return shell("Mappa BANDO dell'organizzazione fiscale", "Dal bando alla risposta orale su ente, funzione, lessico e rischio.", inner)
}

function figureMefAgenzie() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${node(585, 205, 430, 120, "MEF", ["indirizzo", "vigilanza, coordinamento"], "navy", "softBlue")}
  <path class="line" d="M800 325 L800 390"/>
  <path class="line" d="M285 390 L1315 390"/>
  ${line(285, 390, 285, 475)}
  ${line(628, 390, 628, 475)}
  ${line(972, 390, 972, 475)}
  ${line(1315, 390, 1315, 475)}
  ${agency(120, 475, "AE", "AE", ["servizi fiscali", "controlli", "accertamento"], "navy", "softBlue")}
  ${agency(462, 475, "ADM", "ADM", ["dogane", "accise", "monopoli"], "bordeaux", "softRed")}
  ${agency(805, 475, "AdER", "AdER", ["riscossione", "pagamenti", "debitore"], "green", "softGreen")}
  ${agency(1148, 475, "P", "Profili", ["lessico", "prove", "output"], "gold", "softGold")}
  ${note(245, 815, 1110, "Collegamento al MEF non significa identita con il Ministero: ogni ente ha funzione propria.")}
`
  return shell("MEF, agenzie fiscali e riscossione", "Indirizzo e vigilanza non coincidono con le funzioni tecnico-operative.", inner)
}

function figureTreFunzioni() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${functionLane(110, 245, "AE", "Agenzia delle Entrate", "Entrate e servizi fiscali", ["contribuente", "adempimento", "controllo", "accertamento", "territorio/SPI"], "navy", "softBlue")}
  ${functionLane(560, 245, "ADM", "ADM", "Dogane, accise e monopoli", ["merce", "operatore", "accisa", "gioco pubblico", "vigilanza"], "bordeaux", "softRed")}
  ${functionLane(1010, 245, "AdER", "AdER", "Riscossione nazionale", ["cartella", "pagamento", "rateizzazione", "sospensione", "debitore"], "green", "softGreen")}
  ${note(230, 815, 1140, "Preparare ADM come AE, o AdER come accertamento, e' l'errore organizzativo piu' costoso.")}
`
  return shell("Le tre funzioni da non confondere", "Entrate e servizi fiscali, dogane e monopoli, riscossione nazionale.", inner)
}

function figureCentroTerritorio() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${centerBox(585, 210, 430, 118, "Strutture centrali", ["indirizzo, coordinamento", "supporto e controllo"])}
  <path class="line" d="M800 328 L800 400"/>
  ${arrow(800, 400, 370, 492, "Navy")}
  ${arrow(800, 400, 800, 492, "Gold")}
  ${arrow(800, 400, 1230, 492, "Teal")}
  ${channel(120, 500, "Territorio AE", ["contribuenti", "professionisti", "servizi e atti"], "navy", "softBlue")}
  ${channel(550, 500, "Presidi ADM", ["operatori", "merci", "settori regolati"], "bordeaux", "softRed")}
  ${channel(980, 500, "Sportelli AdER", ["debitori", "pagamenti", "rate e sospensioni"], "green", "softGreen")}
  ${note(245, 815, 1110, "Gli organigrammi cambiano: la mappa stabile e' centro che coordina, territorio che opera.")}
`
  return shell("Organizzazione centrale e rete territoriale", "Il centro coordina; il territorio incontra contribuenti, operatori e debitori.", inner)
}

function figureAccertamentoRiscossione() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${processBox(130, 240, "Accertamento", ["verifica", "determina o rettifica", "la pretesa"], "AE", "navy", "softBlue")}
  ${arrow(520, 405, 660, 405, "Navy")}
  ${processBox(680, 240, "Credito o carico", ["titolo", "dati", "passaggio operativo"], "ponte", "gold", "softGold")}
  ${arrow(1070, 405, 1210, 405, "Gold")}
  ${processBox(1230, 240, "Riscossione", ["cartella", "pagamento", "rateizzazione"], "AdER", "green", "softGreen")}
  ${warningBox(320, 635, "Da non dire", ["la cartella e' accertamento"], "bordeaux", "softRed")}
  ${warningBox(875, 635, "Da dire", ["accertamento e riscossione", "sono fasi collegate ma diverse"], "teal", "softTeal")}
  ${note(245, 815, 1110, "La domanda-trappola separa pretesa e pagamento: rispondi sempre per fase e funzione.")}
`
  return shell("Accertamento e riscossione", "Due fasi collegate ma diverse: pretesa, carico, pagamento e relazione.", inner)
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
      .softRed { fill: ${palette.redSoft}; stroke: #E2B3BA; stroke-width: 2.5; }
      .softGold { fill: ${palette.goldSoft}; stroke: #E5C85F; stroke-width: 2.5; }
      .softGreen { fill: ${palette.greenSoft}; stroke: #A8D2BC; stroke-width: 2.5; }
      .softTeal { fill: ${palette.tealSoft}; stroke: #A9D7DB; stroke-width: 2.5; }
      .line { fill: none; stroke: ${palette.line}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }
      .title { fill: ${palette.ink}; font: 700 42px Arial, sans-serif; letter-spacing: 0; }
      .subtitle { fill: ${palette.muted}; font: 400 24px Arial, sans-serif; letter-spacing: 0; }
      .label { fill: ${palette.ink}; font: 700 29px Arial, sans-serif; letter-spacing: 0; }
      .small { fill: ${palette.muted}; font: 400 21px Arial, sans-serif; letter-spacing: 0; }
      .tiny { fill: ${palette.muted}; font: 400 19px Arial, sans-serif; letter-spacing: 0; }
      .badgeText { fill: ${palette.white}; font: 700 19px Arial, sans-serif; letter-spacing: 0; }
      .noteText { fill: ${palette.ink}; font: 600 22px Arial, sans-serif; letter-spacing: 0; }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/>
    </marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/>
    </marker>
    <marker id="arrowTeal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.teal}"/>
    </marker>
  </defs>
  <rect class="bg" x="0" y="0" width="1600" height="900"/>
  <g data-safe-box="70 20 1460 112 8" data-safe-name="header">
    <text class="title" x="80" y="70">${esc(title)}</text>
    <text class="subtitle" x="80" y="110">${esc(subtitle)}</text>
  </g>
  ${inner}
</svg>
`
}

function node(x, y, w, h, title, lines, color, softClass) {
  return `
  <g data-safe-box="${x} ${y} ${w} ${h} 6" data-safe-name="${esc(title)}">
    <rect class="${softClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="24"/>
    <rect x="${x + 22}" y="${y + 22}" width="52" height="30" rx="15" fill="${palette[color]}"/>
    <text class="badgeText" x="${x + 48}" y="${y + 44}" text-anchor="middle">M</text>
    <text class="label" x="${x + 92}" y="${y + 45}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 30}" y="${y + 80 + index * 28}">${esc(lineText)}</text>`).join("")}
  </g>`
}

function agency(x, y, badge, title, lines, color, softClass) {
  return `
  <g data-safe-box="${x} ${y} 310 210 18" data-safe-name="${esc(title)}">
    <rect class="${softClass}" x="${x}" y="${y}" width="310" height="210" rx="24"/>
    <circle cx="${x + 50}" cy="${y + 50}" r="28" fill="${palette[color]}"/>
    <text class="badgeText" x="${x + 50}" y="${y + 57}" text-anchor="middle">${esc(badge)}</text>
    <text class="label" x="${x + 96}" y="${y + 58}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 30}" y="${y + 100 + index * 36}">${esc(lineText)}</text>`).join("")}
  </g>`
}

function functionLane(x, y, badge, title, subtitle, lines, color, softClass) {
  return `
  <g data-safe-box="${x} ${y} 380 475 22" data-safe-name="${esc(title)}">
    <rect class="${softClass}" x="${x}" y="${y}" width="380" height="475" rx="28"/>
    <circle cx="${x + 58}" cy="${y + 58}" r="34" fill="${palette[color]}"/>
    <text class="badgeText" x="${x + 58}" y="${y + 65}" text-anchor="middle">${esc(badge)}</text>
    <text class="label" x="${x + 30}" y="${y + 130}">${esc(title)}</text>
    <text class="small" x="${x + 30}" y="${y + 170}">${esc(subtitle)}</text>
    <path class="line" d="M${x + 30} ${y + 205} L${x + 350} ${y + 205}"/>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 42}" y="${y + 260 + index * 38}">- ${esc(lineText)}</text>`).join("")}
  </g>`
}

function centerBox(x, y, w, h, title, lines) {
  return `
  <g data-safe-box="${x} ${y} ${w} ${h} 6" data-safe-name="${esc(title)}">
    <rect class="softBlue" x="${x}" y="${y}" width="${w}" height="${h}" rx="24"/>
    <text class="label" x="${x + 28}" y="${y + 44}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 28}" y="${y + 80 + index * 28}">${esc(lineText)}</text>`).join("")}
  </g>`
}

function channel(x, y, title, lines, color, softClass) {
  return `
  <g data-safe-box="${x} ${y} 380 200 18" data-safe-name="${esc(title)}">
    <rect class="${softClass}" x="${x}" y="${y}" width="380" height="200" rx="24"/>
    <text class="label" x="${x + 30}" y="${y + 50}">${esc(title)}</text>
    <circle cx="${x + 38}" cy="${y + 88}" r="9" fill="${palette[color]}"/>
    <circle cx="${x + 38}" cy="${y + 124}" r="9" fill="${palette[color]}"/>
    <circle cx="${x + 38}" cy="${y + 160}" r="9" fill="${palette[color]}"/>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 62}" y="${y + 95 + index * 36}">${esc(lineText)}</text>`).join("")}
  </g>`
}

function processBox(x, y, title, lines, badge, color, softClass) {
  return `
  <g data-safe-box="${x} ${y} 350 330 22" data-safe-name="${esc(title)}">
    <rect class="${softClass}" x="${x}" y="${y}" width="350" height="330" rx="28"/>
    <rect x="${x + 28}" y="${y + 28}" width="86" height="38" rx="19" fill="${palette[color]}"/>
    <text class="badgeText" x="${x + 71}" y="${y + 53}" text-anchor="middle">${esc(badge)}</text>
    <text class="label" x="${x + 28}" y="${y + 112}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 34}" y="${y + 175 + index * 44}">- ${esc(lineText)}</text>`).join("")}
  </g>`
}

function warningBox(x, y, title, lines, color, softClass) {
  return `
  <g data-safe-box="${x} ${y} 405 110 4" data-safe-name="${esc(title)}">
    <rect class="${softClass}" x="${x}" y="${y}" width="405" height="110" rx="22"/>
    <text class="label" x="${x + 24}" y="${y + 42}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="small" x="${x + 24}" y="${y + 75 + index * 26}">${esc(lineText)}</text>`).join("")}
  </g>`
}

function note(x, y, w, text) {
  return `
  <g data-safe-box="${x} ${y - 34} ${w} 62 14" data-safe-name="nota">
    <rect x="${x}" y="${y - 34}" width="${w}" height="62" rx="22" fill="${palette.white}" stroke="${palette.border}" stroke-width="2"/>
    <text class="noteText" x="${x + 28}" y="${y + 5}">${esc(text)}</text>
  </g>`
}

function line(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function arrow(x1, y1, x2, y2, marker) {
  return `<path d="M${x1} ${y1} L${x2} ${y2}" fill="none" stroke="${marker === "Gold" ? palette.gold : marker === "Teal" ? palette.teal : palette.navy}" stroke-width="5" stroke-linecap="round" marker-end="url(#arrow${marker})"/>`
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
