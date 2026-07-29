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
  "chapter-08"
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
    slug: "01-mappa-bando-dogane-adm",
    title: "Mappa BANDO delle dogane ADM",
    subtitle: "Diritto UE, merci, dichiarazione, controlli e operatore economico come mappa da concorso.",
    svg: figureMappaBando()
  },
  {
    slug: "02-flusso-procedura-doganale",
    title: "Procedura doganale come sequenza",
    subtitle: "Dal movimento della merce allo svincolo, passando per dati, regime e controlli.",
    svg: figureFlusso()
  },
  {
    slug: "03-triade-classificazione-origine-valore",
    title: "Classificazione, origine e valore",
    subtitle: "La triade tecnica che collega la merce a tariffa, misure, controlli e base economica.",
    svg: figureTriade()
  },
  {
    slug: "04-controlli-doganali-rischio-aeo",
    title: "Controlli doganali e rischio",
    subtitle: "Dati, documenti, controlli fisici e AEO servono a proteggere il commercio legittimo.",
    svg: figureControlli()
  },
  {
    slug: "05-checklist-dichiarazione-doganale",
    title: "Checklist della dichiarazione doganale",
    subtitle: "Soggetto, merce, triade tecnica, regime, documenti e rischio prima della risposta.",
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
  return `# Asset Capitolo 8 - M-FC02 Dogane e procedure doganali ADM

Figure generate per \`Dogane e procedure doganali ADM\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, sequenza operativa, confronto concettuale, schema anti-confusione e checklist applicativa;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO dogane ADM, flusso procedurale, triade classificazione-origine-valore, controlli/rischio/AEO e checklist dichiarazione doganale.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-dogane-adm.png\` | \`01-mappa-bando-dogane-adm.svg\` | Mappa BANDO del capitolo: diritto UE, merci, dichiarazione, controlli e operatore economico. |
| \`02-flusso-procedura-doganale.png\` | \`02-flusso-procedura-doganale.svg\` | Sequenza operativa dal movimento della merce allo svincolo. |
| \`03-triade-classificazione-origine-valore.png\` | \`03-triade-classificazione-origine-valore.svg\` | Schema della triade tecnica che regge il caso doganale. |
| \`04-controlli-doganali-rischio-aeo.png\` | \`04-controlli-doganali-rischio-aeo.svg\` | Sintesi di controlli documentali, fisici, rischio e AEO. |
| \`05-checklist-dichiarazione-doganale.png\` | \`05-checklist-dichiarazione-doganale.svg\` | Checklist visuale per impostare una dichiarazione doganale. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${box(555, 205, 490, 122, "Dogane ADM", ["merci, dati e regime", "controlli e operatore"], "navy", "softBlue")}
  <path class="line" d="M800 327 L800 370"/>
  <path class="line" d="M205 370 L1395 370"/>
  ${line(205, 370, 205, 460)}
  ${line(505, 370, 505, 585)}
  ${line(800, 370, 800, 460)}
  ${line(1095, 370, 1095, 585)}
  ${line(1395, 370, 1395, 460)}
  ${box(70, 460, 270, 130, "B - Bando", ["ADM, dogane", "import/export"], "navy", "softBlue")}
  ${box(370, 585, 270, 130, "A - Aree", ["UE, regime", "controlli"], "bordeaux", "softRed")}
  ${box(665, 460, 270, 130, "N - Nuclei", ["dichiarazione", "triade tecnica"], "gold", "softGold")}
  ${box(960, 585, 270, 130, "D - Diario", ["origine/spedizione", "valore/fattura"], "green", "softGreen")}
  ${box(1260, 460, 270, 130, "O - Output", ["mappa merce", "caso guidato"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Il capitolo si studia come flusso di merci, dati, regime e controllo.")}
`
  return shell("Mappa BANDO delle dogane ADM", "Diritto UE, merci, dichiarazione, controlli e operatore economico come mappa da concorso.", inner)
}

function figureFlusso() {
  const y = 305
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(94, y, "1", "Operatore", ["ruolo e", "titolo"], "navy", "softBlue")}
  ${step(299, y, "2", "Merce", ["descrizione", "tecnica"], "bordeaux", "softRed")}
  ${step(504, y, "3", "Triade", ["classifica", "origine valore"], "gold", "softGold")}
  ${step(709, y, "4", "Regime", ["import", "export transito"], "green", "softGreen")}
  ${step(914, y, "5", "Dati", ["documenti", "e sistemi"], "teal", "softTeal")}
  ${step(1119, y, "6", "Controllo", ["rischio", "verifiche"], "navy", "softBlue")}
  ${step(1324, y, "7", "Svincolo", ["o esito", "successivo"], "bordeaux", "softRed")}
  ${arrow(264, y + 82, 289, y + 82, "Navy")}
  ${arrow(469, y + 82, 494, y + 82, "Bordeaux")}
  ${arrow(674, y + 82, 699, y + 82, "Gold")}
  ${arrow(879, y + 82, 904, y + 82, "Green")}
  ${arrow(1084, y + 82, 1109, y + 82, "Teal")}
  ${arrow(1289, y + 82, 1314, y + 82, "Navy")}
  ${smallBox(250, 595, 330, 106, "Nodo dati", ["merce reale e documenti"], "bordeaux", "softRed")}
  ${smallBox(635, 595, 330, 106, "Nodo regime", ["effetti e formalita"], "gold", "softGold")}
  ${smallBox(1020, 595, 330, 106, "Nodo rischio", ["controllo proporzionato"], "green", "softGreen")}
  ${note(245, 815, 1110, "La procedura doganale non e' solo pagamento: e' qualificazione, regime e controllo.")}
`
  return shell("Procedura doganale come sequenza", "Dal movimento della merce allo svincolo, passando per dati, regime e controlli.", inner)
}

function figureTriade() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(560, 220, 480, 145, "Merce da qualificare", ["descrizione tecnica", "documenti e funzione"], "navy", "softBlue")}
  <path class="line" d="M800 365 L800 405"/>
  <path class="line" d="M310 405 L1290 405"/>
  ${line(310, 405, 310, 485)}
  ${line(800, 405, 800, 485)}
  ${line(1290, 405, 1290, 485)}
  ${option(130, 485, "Classificazione", ["voce corretta", "misure applicabili"], "gold", "softGold")}
  ${option(620, 485, "Origine", ["nazionalita", "economica"], "green", "softGreen")}
  ${option(1110, 485, "Valore", ["base economica", "regole doganali"], "teal", "softTeal")}
  ${smallBox(510, 690, 580, 82, "Effetto comune", ["tariffa, controlli, preferenze, divieti e responsabilita"], "bordeaux", "softRed")}
  ${note(245, 815, 1110, "Nome commerciale, Paese di spedizione e fattura non bastano: serve qualificazione doganale.")}
`
  return shell("Classificazione, origine e valore", "La triade tecnica che collega la merce a tariffa, misure, controlli e base economica.", inner)
}

function figureControlli() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(555, 235, 490, 142, "Analisi del rischio", ["seleziona l'intensita", "senza bloccare il lecito"], "navy", "softBlue")}
  ${arrow(800, 380, 800, 450, "Navy")}
  ${option(105, 475, "Dati anticipati", ["arrivo, uscita", "e tracciati"], "teal", "softTeal")}
  ${option(450, 475, "Documenti", ["fatture, trasporto", "autorizzazioni"], "bordeaux", "softRed")}
  ${option(795, 475, "Controllo fisico", ["merce reale", "quantita natura"], "gold", "softGold")}
  ${option(1140, 475, "AEO", ["affidabilita", "regolata"], "green", "softGreen")}
  ${arrow(350, 555, 440, 555, "Teal")}
  ${arrow(695, 555, 785, 555, "Bordeaux")}
  ${arrow(1040, 555, 1130, 555, "Gold")}
  ${smallBox(520, 690, 560, 86, "Obiettivo ADM", ["proteggere mercato, entrate, sicurezza e commercio legittimo"], "navy", "softBlue")}
  ${note(245, 815, 1110, "AEO riduce attriti dove ricorrono requisiti, ma non elimina il potere di controllo.")}
`
  return shell("Controlli doganali e rischio", "Dati, documenti, controlli fisici e AEO servono a proteggere il commercio legittimo.", inner)
}

function figureChecklist() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${checkItem(130, 225, 415, "1. Soggetto", ["operatore e ruolo"], "navy", "softBlue")}
  ${checkItem(130, 335, 415, "2. Merce", ["descrizione tecnica"], "bordeaux", "softRed")}
  ${checkItem(130, 445, 415, "3. Regime", ["import, export, transito"], "gold", "softGold")}
  ${checkItem(130, 555, 415, "4. Documenti", ["prove e autorizzazioni"], "green", "softGreen")}
  ${checkItem(1055, 225, 415, "5. Classificazione", ["voce e misure"], "gold", "softGold")}
  ${checkItem(1055, 335, 415, "6. Origine", ["non solo spedizione"], "green", "softGreen")}
  ${checkItem(1055, 445, 415, "7. Valore", ["regole doganali"], "teal", "softTeal")}
  ${checkItem(1055, 555, 415, "8. Rischio", ["controllo coerente"], "bordeaux", "softRed")}
  ${center(595, 335, 410, 205, "Risposta concorsuale", ["merce", "triade tecnica", "regime", "controllo"], "navy", "softBlue")}
  ${arrow(555, 410, 585, 410, "Green")}
  ${arrow(1015, 410, 1045, 410, "Teal")}
  ${smallBox(600, 585, 400, 86, "Non partire dal dazio", ["prima dati, regime e competenza"], "gold", "softGold")}
  ${note(245, 815, 1110, "La checklist impedisce risposte generiche su importazione, dazio e documenti.")}
`
  return shell("Checklist della dichiarazione doganale", "Soggetto, merce, triade tecnica, regime, documenti e rischio prima della risposta.", inner)
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
