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
  "chapter-09"
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
    slug: "01-mappa-bando-accise-giochi-monopoli",
    title: "Mappa BANDO accise e monopoli",
    subtitle: "Prodotti regolati, giochi pubblici, controlli, legalita e output da concorso.",
    svg: figureMappaBando()
  },
  {
    slug: "02-filiera-accise-regime-sospensivo",
    title: "Accise come filiera regolata",
    subtitle: "Prodotto, deposito, regime, circolazione e consumo vanno letti come sequenza.",
    svg: figureFilieraAccise()
  },
  {
    slug: "03-prodotti-giochi-monopoli-adm",
    title: "Prodotti, giochi e monopoli",
    subtitle: "Le aree ADM da riconoscere: energia, alcole, tabacchi, giochi e rete autorizzata.",
    svg: figureAree()
  },
  {
    slug: "04-controlli-adm-filiere-regolate",
    title: "Controlli ADM nelle filiere",
    subtitle: "Prodotto, luogo, soggetto, dati e rischio costruiscono la verifica.",
    svg: figureControlli()
  },
  {
    slug: "05-checklist-accise-giochi-monopoli",
    title: "Checklist accise, giochi e monopoli",
    subtitle: "Materia, prodotto, titolo, documenti, controllo e cautela sulle sanzioni.",
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
  return `# Asset Capitolo 9 - M-FC02 Accise, giochi e monopoli

Figure generate per \`Accise, giochi e monopoli\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, sequenza operativa, confronto concettuale, schema di controllo e checklist applicativa;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO, filiera accise, aree ADM regolamentate, controlli nelle filiere e checklist finale.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-accise-giochi-monopoli.png\` | \`01-mappa-bando-accise-giochi-monopoli.svg\` | Mappa BANDO del capitolo: prodotti regolati, giochi, controlli e legalita. |
| \`02-filiera-accise-regime-sospensivo.png\` | \`02-filiera-accise-regime-sospensivo.svg\` | Sequenza operativa delle accise come filiera regolata. |
| \`03-prodotti-giochi-monopoli-adm.png\` | \`03-prodotti-giochi-monopoli-adm.svg\` | Schema delle aree ADM: energia, alcole, energia/gas, tabacchi e giochi. |
| \`04-controlli-adm-filiere-regolate.png\` | \`04-controlli-adm-filiere-regolate.svg\` | Sintesi dei controlli ADM su prodotto, luogo, soggetto, dati e rischio. |
| \`05-checklist-accise-giochi-monopoli.png\` | \`05-checklist-accise-giochi-monopoli.svg\` | Checklist visuale per impostare una risposta su accise, giochi e monopoli. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(555, 205, 490, 122, "ADM filiere regolate", ["accise, giochi", "monopoli e controlli"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${box(70, 460, 270, 130, "B - Bando", ["profili ADM", "accise giochi"], "navy", "softBlue")}
  ${box(370, 585, 270, 130, "A - Aree", ["prodotti", "giochi monopoli"], "bordeaux", "softRed")}
  ${box(665, 460, 270, 130, "N - Nuclei", ["deposito", "regime controllo"], "gold", "softGold")}
  ${box(960, 585, 270, 130, "D - Diario", ["IVA/accisa", "gioco legale"], "green", "softGreen")}
  ${box(1260, 460, 270, 130, "O - Output", ["glossario ADM", "caso guidato"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Il capitolo si studia come mappa di filiere, titoli, controlli e legalita.")}
`
  return shell("Mappa BANDO accise e monopoli", "Prodotti regolati, giochi pubblici, controlli, legalita e output da concorso.", inner)
}

function figureFilieraAccise() {
  const y = 305
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(115, y, "1", "Prodotto", ["energia", "alcole tabacchi"], "navy", "softBlue")}
  ${step(355, y, "2", "Deposito", ["luogo", "autorizzato"], "bordeaux", "softRed")}
  ${step(595, y, "3", "Regime", ["sospensivo", "o consumo"], "gold", "softGold")}
  ${step(835, y, "4", "Movimento", ["dati", "documenti"], "green", "softGreen")}
  ${step(1075, y, "5", "Esigibilita", ["imposta", "effetti"], "teal", "softTeal")}
  ${step(1315, y, "6", "Controllo", ["rischio", "sanzioni"], "navy", "softBlue")}
  ${arrow(285, y + 82, 345, y + 82, "Navy")}
  ${arrow(525, y + 82, 585, y + 82, "Bordeaux")}
  ${arrow(765, y + 82, 825, y + 82, "Gold")}
  ${arrow(1005, y + 82, 1065, y + 82, "Green")}
  ${arrow(1245, y + 82, 1305, y + 82, "Teal")}
  ${smallBox(255, 595, 330, 106, "Nodo luogo", ["non e' magazzino generico"], "bordeaux", "softRed")}
  ${smallBox(635, 595, 330, 106, "Nodo regime", ["sospensione non e' esenzione"], "gold", "softGold")}
  ${smallBox(1015, 595, 330, 106, "Nodo rischio", ["filiera tracciata e controllata"], "green", "softGreen")}
  ${note(245, 815, 1110, "Nelle accise il tributo segue prodotto, filiera, soggetto e titolo autorizzativo.")}
`
  return shell("Accise come filiera regolata", "Prodotto, deposito, regime, circolazione e consumo vanno letti come sequenza.", inner)
}

function figureAree() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(560, 215, 480, 142, "ADM presidio regolato", ["tributo, concessione", "legalita e controllo"], "navy", "softBlue")}
  <path class="line" d="M800 357 L800 408"/>
  <path class="line" d="M280 408 L1320 408"/>
  ${line(280, 408, 280, 500)}
  ${line(540, 408, 540, 500)}
  ${line(800, 408, 800, 500)}
  ${line(1060, 408, 1060, 500)}
  ${line(1320, 408, 1320, 500)}
  ${tile(120, 500, 320, "Prodotti energetici", ["deposito", "circolazione"], "navy", "softBlue")}
  ${tile(480, 500, 320, "Alcole e bevande", ["filiera", "imposta"], "bordeaux", "softRed")}
  ${tile(840, 500, 320, "Energia e gas", ["fornitura", "consumo"], "gold", "softGold")}
  ${tile(1200, 500, 320, "Tabacchi e giochi", ["rete legale", "concessioni"], "teal", "softTeal")}
  ${smallBox(520, 690, 560, 86, "Idea comune", ["settori sensibili, titoli pubblici, dati e controlli ADM"], "green", "softGreen")}
  ${note(245, 815, 1110, "Non memorizzare aliquote: riconosci area, soggetto, obbligo e controllo.")}
`
  return shell("Prodotti, giochi e monopoli", "Le aree ADM da riconoscere: energia, alcole, tabacchi, giochi e rete autorizzata.", inner)
}

function figureControlli() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(555, 225, 490, 142, "Controllo ADM", ["legalita, gettito", "mercato regolato"], "navy", "softBlue")}
  ${arrow(800, 370, 800, 455, "Navy")}
  ${option(105, 475, "Prodotto", ["natura", "quantita"], "teal", "softTeal")}
  ${option(450, 475, "Luogo", ["deposito", "punto vendita"], "bordeaux", "softRed")}
  ${option(795, 475, "Soggetto", ["titolo", "affidabilita"], "gold", "softGold")}
  ${option(1140, 475, "Dati e rischio", ["tracciati", "anomalie"], "green", "softGreen")}
  ${arrow(350, 555, 440, 555, "Teal")}
  ${arrow(695, 555, 785, 555, "Bordeaux")}
  ${arrow(1040, 555, 1130, 555, "Gold")}
  ${smallBox(520, 690, 560, 86, "Esito concorsuale", ["spiegare controllo prima della sanzione"], "navy", "softBlue")}
  ${note(245, 815, 1110, "Il controllo moderno combina prodotto reale, titolo autorizzativo, dati e rischio.")}
`
  return shell("Controlli ADM nelle filiere", "Prodotto, luogo, soggetto, dati e rischio costruiscono la verifica.", inner)
}

function figureChecklist() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${checkItem(130, 225, 415, "1. Materia", ["accisa gioco monopolio"], "navy", "softBlue")}
  ${checkItem(130, 335, 415, "2. Prodotto", ["energia alcole tabacchi"], "bordeaux", "softRed")}
  ${checkItem(130, 445, 415, "3. Luogo", ["deposito rete canale"], "gold", "softGold")}
  ${checkItem(130, 555, 415, "4. Soggetto", ["operatore e titolo"], "green", "softGreen")}
  ${checkItem(1055, 225, 415, "5. Regime", ["sospensione consumo"], "gold", "softGold")}
  ${checkItem(1055, 335, 415, "6. Documenti", ["dati e tracciati"], "green", "softGreen")}
  ${checkItem(1055, 445, 415, "7. Controllo", ["rischio legalita"], "teal", "softTeal")}
  ${checkItem(1055, 555, 415, "8. Sanzioni", ["solo testo vigente"], "bordeaux", "softRed")}
  ${center(595, 335, 410, 205, "Risposta ADM", ["filiera", "titolo", "controllo", "cautela"], "navy", "softBlue")}
  ${arrow(555, 410, 585, 410, "Green")}
  ${arrow(1015, 410, 1045, 410, "Teal")}
  ${smallBox(600, 585, 400, 86, "Regola d'esame", ["prima funzione, poi norma puntuale"], "gold", "softGold")}
  ${note(245, 815, 1110, "La checklist evita risposte vaghe su giochi, tabacchi, accise e monopoli.")}
`
  return shell("Checklist accise, giochi e monopoli", "Materia, prodotto, titolo, documenti, controllo e cautela sulle sanzioni.", inner)
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
