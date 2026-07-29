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
  "chapter-06"
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
    slug: "01-mappa-bando-adempimenti-fiscali",
    title: "Mappa BANDO degli adempimenti fiscali",
    subtitle: "Redditi, IVA, dichiarazioni, versamenti, compensazioni e servizi come sequenza da concorso.",
    svg: figureMappaBando()
  },
  {
    slug: "02-redditi-iva-due-logiche",
    title: "Redditi e IVA: due logiche diverse",
    subtitle: "Il reddito guarda al soggetto e al periodo; l'IVA guarda alle operazioni.",
    svg: figureRedditiIva()
  },
  {
    slug: "03-flusso-dichiarazione-versamento-controllo",
    title: "Dal fatto fiscale al controllo",
    subtitle: "Dichiarazione, liquidazione, versamento e verifica sono fasi collegate ma distinte.",
    svg: figureFlusso()
  },
  {
    slug: "04-credito-rimborso-compensazione",
    title: "Credito, rimborso e compensazione",
    subtitle: "Tre parole vicine, tre funzioni diverse dentro regole e controlli.",
    svg: figureCredito()
  },
  {
    slug: "05-servizi-compliance-controllo",
    title: "Servizi fiscali, compliance e controllo",
    subtitle: "L'Agenzia assiste, orienta e verifica per migliorare qualita del dato e legalita fiscale.",
    svg: figureServizi()
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
  return `# Asset Capitolo 6 - M-FC02 Adempimenti fiscali: redditi, IVA, dichiarazioni

Figure generate per \`Adempimenti fiscali: redditi, IVA, dichiarazioni\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, confronto concettuale, sequenza operativa, schema anti-confusione e sintesi servizi/controllo;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO degli adempimenti, confronto redditi/IVA, flusso dichiarazione-versamento-controllo, distinzione credito/rimborso/compensazione e rapporto tra servizi fiscali, compliance e controllo.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-adempimenti-fiscali.png\` | \`01-mappa-bando-adempimenti-fiscali.svg\` | Mappa BANDO del capitolo: redditi, IVA, dichiarazioni, versamenti, compensazioni e servizi. |
| \`02-redditi-iva-due-logiche.png\` | \`02-redditi-iva-due-logiche.svg\` | Confronto anti-confusione tra logica dei redditi e logica IVA. |
| \`03-flusso-dichiarazione-versamento-controllo.png\` | \`03-flusso-dichiarazione-versamento-controllo.svg\` | Sequenza dal fatto fiscale alla dichiarazione, al versamento e al controllo. |
| \`04-credito-rimborso-compensazione.png\` | \`04-credito-rimborso-compensazione.svg\` | Distinzione tra credito, rimborso e compensazione. |
| \`05-servizi-compliance-controllo.png\` | \`05-servizi-compliance-controllo.svg\` | Ruolo dei servizi fiscali nel rapporto contribuente, compliance e controllo. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(555, 205, 490, 122, "Adempimenti fiscali", ["redditi, IVA, dichiarazioni", "versamenti e servizi"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${box(70, 460, 270, 130, "B - Bando", ["redditi, IVA", "adempimenti"], "navy", "softBlue")}
  ${box(370, 585, 270, 130, "A - Aree", ["dichiarare", "pagare"], "bordeaux", "softRed")}
  ${box(665, 460, 270, 130, "N - Nuclei", ["debito, credito", "controllo"], "gold", "softGold")}
  ${box(960, 585, 270, 130, "D - Diario", ["scambio fasi", "IVA = utile"], "green", "softGreen")}
  ${box(1260, 460, 270, 130, "O - Output", ["mappa", "flusso"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Gli adempimenti si studiano come sequenza, non come calendario di sigle.")}
`
  return shell("Mappa BANDO degli adempimenti fiscali", "Redditi, IVA, dichiarazioni, versamenti, compensazioni e servizi come sequenza da concorso.", inner)
}

function figureRedditiIva() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${panel(135, 235, 580, 420, "Imposte sui redditi", ["soggetto", "periodo d'imposta", "reddito", "base imponibile", "dichiarazione"], "navy", "softBlue")}
  ${panel(885, 235, 580, 420, "IVA", ["operazione", "soggetto in attivita", "rivalsa e detrazione", "liquidazione", "dichiarazione"], "bordeaux", "softRed")}
  ${arrow(725, 430, 875, 430, "Gold")}
  ${badge(635, 695, 330, "non trasferire la stessa logica")}
  ${note(245, 815, 1110, "Redditi: ricchezza del soggetto. IVA: operazioni e meccanismo rivalsa/detrazione.")}
`
  return shell("Redditi e IVA: due logiche diverse", "Il reddito guarda al soggetto e al periodo; l'IVA guarda alle operazioni.", inner)
}

function figureFlusso() {
  const y = 305
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(94, y, "1", "Fatto", ["rilevante"], "navy", "softBlue")}
  ${step(299, y, "2", "Dati", ["documenti"], "bordeaux", "softRed")}
  ${step(504, y, "3", "Dichiarare", ["esporre"], "gold", "softGold")}
  ${step(709, y, "4", "Liquidare", ["debito o", "credito"], "green", "softGreen")}
  ${step(914, y, "5", "Versare", ["o usare", "credito"], "teal", "softTeal")}
  ${step(1119, y, "6", "Servizi", ["assistenza"], "navy", "softBlue")}
  ${step(1324, y, "7", "Controllo", ["coerenza"], "bordeaux", "softRed")}
  ${arrow(264, y + 82, 289, y + 82, "Navy")}
  ${arrow(469, y + 82, 494, y + 82, "Bordeaux")}
  ${arrow(674, y + 82, 699, y + 82, "Gold")}
  ${arrow(879, y + 82, 904, y + 82, "Green")}
  ${arrow(1084, y + 82, 1109, y + 82, "Teal")}
  ${arrow(1289, y + 82, 1314, y + 82, "Navy")}
  ${smallBox(250, 595, 330, 106, "Atti diversi", ["dichiarare non e' pagare"], "bordeaux", "softRed")}
  ${smallBox(635, 595, 330, 106, "Posizione finale", ["debito, credito o verifica"], "gold", "softGold")}
  ${smallBox(1020, 595, 330, 106, "Esito possibile", ["compliance o accertamento"], "green", "softGreen")}
  ${note(245, 815, 1110, "La dichiarazione alimenta il sistema informativo; il versamento estingue il debito nei modi previsti.")}
`
  return shell("Dal fatto fiscale al controllo", "Dichiarazione, liquidazione, versamento e verifica sono fasi collegate ma distinte.", inner)
}

function figureCredito() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(565, 215, 470, 130, "Credito fiscale", ["posizione favorevole da verificare"], "gold", "softGold")}
  <path class="line" d="M800 345 L800 400"/>
  <path class="line" d="M310 400 L1290 400"/>
  ${line(310, 400, 310, 475)}
  ${line(800, 400, 800, 475)}
  ${line(1290, 400, 1290, 475)}
  ${option(130, 475, "Rimborso", ["restituzione", "quando spettante"], "green", "softGreen")}
  ${option(620, 475, "Compensazione", ["usa il credito", "contro debiti"], "teal", "softTeal")}
  ${option(1110, 475, "Riporto", ["eccedenza", "secondo regole"], "navy", "softBlue")}
  ${smallBox(510, 670, 580, 92, "Regole e controlli", ["limiti, procedure e istruzioni vanno verificati sul testo vigente"], "bordeaux", "softRed")}
  ${note(245, 815, 1110, "Il credito non e' denaro liberamente spendibile: va usato nei modi previsti.")}
`
  return shell("Credito, rimborso e compensazione", "Tre parole vicine, tre funzioni diverse dentro regole e controlli.", inner)
}

function figureServizi() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(545, 255, 510, 170, "Rapporto contribuente - Agenzia", ["dati, assistenza, adempimento", "e tutela dell'interesse fiscale"], "navy", "softBlue")}
  ${option(110, 520, "Servizi fiscali", ["accesso ai dati", "canali digitali"], "teal", "softTeal")}
  ${option(620, 520, "Compliance", ["correzione", "adempimento spontaneo"], "green", "softGreen")}
  ${option(1130, 520, "Controllo", ["coerenza", "legalita"], "bordeaux", "softRed")}
  ${arrow(365, 555, 610, 555, "Teal")}
  ${arrow(875, 555, 1120, 555, "Green")}
  ${arrow(800, 425, 800, 510, "Navy")}
  ${note(245, 815, 1110, "Il servizio non sostituisce il controllo: rende piu' semplice adempiere correttamente.")}
`
  return shell("Servizi fiscali, compliance e controllo", "L'Agenzia assiste, orienta e verifica per migliorare qualita del dato e legalita fiscale.", inner)
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

function panel(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 18" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="30"/>
    <rect x="${x + 28}" y="${y + 28}" width="${w - 56}" height="7" rx="4" fill="${palette[color]}"/>
    <text class="ink label" x="${x + w / 2}" y="${y + 80}" text-anchor="middle">${esc(title)}</text>
    ${lines.map((lineText, index) => `<circle cx="${x + 95}" cy="${y + 135 + index * 50}" r="8" fill="${palette.gold}"/><text class="muted body" x="${x + 125}" y="${y + 142 + index * 50}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 170 164 12" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="170" height="164" rx="22"/>
    <circle cx="${x + 34}" cy="${y + 38}" r="21" fill="${palette[color]}"/>
    <text x="${x + 34}" y="${y + 46}" text-anchor="middle" fill="#FFFFFF" style="font: 800 21px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 28}" y="${y + 82}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 28}" y="${y + 116 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function center(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 16" data-safe-name="${esc(title)}">
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

function smallBox(x, y, w, h, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="20"/>
    <text class="ink label" x="${x + 24}" y="${y + 36}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 24}" y="${y + 68 + index * 23}">${esc(lineText)}</text>`).join("\n")}
    <rect x="${x}" y="${y}" width="10" height="${h}" rx="5" fill="${palette[color]}"/>
  </g>`
}

function badge(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 58 10" data-safe-name="badge">
    <rect class="note" x="${x}" y="${y}" width="${w}" height="58" rx="18"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 37}" text-anchor="middle">${esc(text)}</text>
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
