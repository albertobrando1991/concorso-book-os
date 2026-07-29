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
  "chapter-14"
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
    slug: "01-mappa-bando-appendici-operative",
    title: "Mappa BANDO delle appendici operative",
    subtitle: "Dal bando alle appendici da attivare, fino a glossario, diario errori e output.",
    svg: figureMappaAppendici()
  },
  {
    slug: "02-reati-sanzioni-condotte-rischio",
    title: "Reati, sanzioni e condotte a rischio",
    subtitle: "Classificare il piano prima di usare parole come reato, illecito o responsabilita.",
    svg: figureReatiSanzioni()
  },
  {
    slug: "03-diritto-ue-doganale-mappa-operativa",
    title: "Diritto UE doganale: mappa operativa",
    subtitle: "Cornice UE, Codice doganale, ADM, merce, triade tecnica e controlli.",
    svg: figureUeDoganale()
  },
  {
    slug: "04-front-office-privacy-protocollo",
    title: "Front-office e protezione dati",
    subtitle: "Sette passaggi per orientare senza promettere e trattare solo dati necessari.",
    svg: figureFrontOffice()
  },
  {
    slug: "05-allerta-bando-glossario-output",
    title: "Schede allerta, glossario e output",
    subtitle: "Parole-spia del bando, appendice corretta, priorita e azione entro 7 giorni.",
    svg: figureAllertaGlossario()
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
  return `# Asset Capitolo 14 - M-FC02 Appendici operative

Figure generate per \`Appendici operative\`.

## Analisi stile libro base

Le immagini del libro base e dei capitoli M-FC02 gia illustrati usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- titoli brevi, testo interno essenziale, card con raggio contenuto, frecce leggere e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, flusso procedurale, schema anti-confusione, protocollo operativo e checklist/allerta;
- inserimento subito dopo il blocco testuale che l'immagine sintetizza.

Per questo capitolo sono opportune 5 figure: coprono mappa generale delle appendici, classificazione reati/sanzioni/condotte, diritto UE doganale, protocollo front-office/privacy e uso coordinato di schede allerta e glossario.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-appendici-operative.png\` | \`01-mappa-bando-appendici-operative.svg\` | Sintesi del capitolo: quale appendice attivare, con quale domanda guida e quale output. |
| \`02-reati-sanzioni-condotte-rischio.png\` | \`02-reati-sanzioni-condotte-rischio.svg\` | Schema anti-confusione tra illecito amministrativo, tributario, penale e integrita pubblica. |
| \`03-diritto-ue-doganale-mappa-operativa.png\` | \`03-diritto-ue-doganale-mappa-operativa.svg\` | Mappa operativa per collegare diritto UE, CDU, ADM e caso doganale. |
| \`04-front-office-privacy-protocollo.png\` | \`04-front-office-privacy-protocollo.svg\` | Protocollo visuale in 7 passaggi per sportello, legittimazione e protezione dati. |
| \`05-allerta-bando-glossario-output.png\` | \`05-allerta-bando-glossario-output.svg\` | Chiusura operativa: parole-spia, glossario, appendice corretta, priorita e output entro 7 giorni. |
`
}

function figureMappaAppendici() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(500, 205, 600, 138, "Appendici operative M-FC02", ["confini, rischi, glossario", "decisioni di bando e output"], "navy", "softBlue")}
  ${arrow(800, 345, 800, 382, "Navy")}
  <path class="line" d="M205 382 L1395 382"/>
  ${line(205, 382, 205, 475)}
  ${line(505, 382, 505, 595)}
  ${line(800, 382, 800, 475)}
  ${line(1095, 382, 1095, 595)}
  ${line(1395, 382, 1395, 475)}
  ${box(70, 475, 270, 132, "B - Bando", ["parole-spia", "peso e prova"], "navy", "softBlue")}
  ${box(370, 595, 270, 132, "A - Appendici", ["A reati/sanzioni", "B UE, C privacy"], "bordeaux", "softRed")}
  ${box(665, 475, 270, 132, "N - Nuclei", ["glossario", "distinzioni"], "gold", "softGold")}
  ${box(960, 595, 270, 132, "D - Diario", ["errori ricorrenti", "fonti da verificare"], "green", "softGreen")}
  ${box(1260, 475, 270, 132, "O - Output", ["scheda allerta", "risposta o caso"], "teal", "softTeal")}
  ${note(245, 815, 1110, "L'appendice giusta riduce rumore: attiva solo cio' che cambia la risposta.")}
`
  return shell("Mappa BANDO delle appendici operative", "Dal bando alle appendici da attivare, fino a glossario, diario errori e output.", inner)
}

function figureReatiSanzioni() {
  const y = 292
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(105, y, "1", "Condotta", ["fatto e soggetto", "documento/atto"], "navy", "softBlue")}
  ${step(380, y, "2", "Piano", ["amministrativo", "tributario/penale"], "bordeaux", "softRed")}
  ${step(655, y, "3", "Fonte", ["norma vigente", "review se serve"], "gold", "softGold")}
  ${step(930, y, "4", "Risposta", ["nucleo prudente", "senza soglie inventate"], "green", "softGreen")}
  ${step(1205, y, "5", "Errore", ["reato generico", "sanzione sinonimo"], "teal", "softTeal")}
  ${arrow(315, y + 84, 370, y + 84, "Navy")}
  ${arrow(590, y + 84, 645, y + 84, "Bordeaux")}
  ${arrow(865, y + 84, 920, y + 84, "Gold")}
  ${arrow(1140, y + 84, 1195, y + 84, "Green")}
  ${smallBox(180, 555, 330, 118, "Non tutto e' reato", ["prima individua procedimento", "autorita e sanzione"], "bordeaux", "softRed")}
  ${smallBox(635, 555, 330, 118, "Non tutto e' forma", ["frode, documento, credito", "possono cambiare piano"], "gold", "softGold")}
  ${smallBox(1090, 555, 330, 118, "Integrita pubblica", ["imparzialita, conflitto", "riservatezza e ruolo"], "green", "softGreen")}
  ${note(245, 815, 1110, "La risposta forte separa illecito, tributo, reato e dovere di comportamento.")}
`
  return shell("Reati, sanzioni e condotte a rischio", "Classificare il piano prima di usare parole come reato, illecito o responsabilita.", inner)
}

function figureUeDoganale() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${center(135, 255, 300, 138, "Unione europea", ["cornice comune", "regole doganali"], "navy", "softBlue")}
  ${center(500, 255, 300, 138, "CDU", ["regimi", "dichiarazione"], "bordeaux", "softRed")}
  ${center(865, 255, 300, 138, "ADM", ["applica", "controlla"], "green", "softGreen")}
  ${center(1230, 255, 235, 138, "Caso", ["merce", "operatore"], "teal", "softTeal")}
  ${arrow(445, 324, 490, 324, "Navy")}
  ${arrow(810, 324, 855, 324, "Bordeaux")}
  ${arrow(1175, 324, 1220, 324, "Green")}
  ${smallBox(155, 505, 300, 118, "Dichiarazione", ["regime e dati", "documenti"], "navy", "softBlue")}
  ${smallBox(520, 505, 300, 118, "Triade tecnica", ["classificazione", "origine, valore"], "gold", "softGold")}
  ${smallBox(885, 505, 300, 118, "Controlli", ["rischio", "documenti/merce"], "bordeaux", "softRed")}
  ${smallBox(1250, 505, 235, 118, "AEO/EORI", ["operatore", "affidabilita"], "teal", "softTeal")}
  ${line(800, 395, 800, 452)}
  <path class="line" d="M305 452 L1370 452"/>
  ${line(305, 452, 305, 505)}
  ${line(670, 452, 670, 505)}
  ${line(1035, 452, 1035, 505)}
  ${line(1370, 452, 1370, 505)}
  ${note(245, 815, 1110, "Nel profilo ADM il diritto UE non e' teoria generale: serve a qualificare la merce e il controllo.")}
`
  return shell("Diritto UE doganale: mappa operativa", "Cornice UE, Codice doganale, ADM, merce, triade tecnica e controlli.", inner)
}

function figureFrontOffice() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${miniStep(110, 235, "1", "Ascolta", ["richiesta", "urgenza"], "navy", "softBlue")}
  ${miniStep(455, 235, "2", "Identifica", ["soggetto", "legittimazione"], "bordeaux", "softRed")}
  ${miniStep(800, 235, "3", "Qualifica", ["AE, ADM", "AdER o altro"], "gold", "softGold")}
  ${miniStep(1145, 235, "4", "Verifica atto", ["documento", "canale"], "green", "softGreen")}
  ${arrow(375, 305, 445, 305, "Navy")}
  ${arrow(720, 305, 790, 305, "Bordeaux")}
  ${arrow(1065, 305, 1135, 305, "Gold")}
  ${miniStep(270, 525, "5", "Proteggi dati", ["base, canale", "minimizzazione"], "teal", "softTeal")}
  ${miniStep(655, 525, "6", "Orienta", ["termini", "documenti"], "navy", "softBlue")}
  ${miniStep(1040, 525, "7", "Chiudi", ["azione", "cautela"], "bordeaux", "softRed")}
  ${arrow(535, 595, 645, 595, "Teal")}
  ${arrow(920, 595, 1030, 595, "Navy")}
  ${smallBox(485, 415, 630, 108, "Regola privacy", ["informazioni necessarie e soggetti legittimati", "canale previsto e dati minimi"], "green", "softGreen")}
  ${note(245, 815, 1110, "Professionalita allo sportello significa orientare bene, senza promettere un esito non verificato.")}
`
  return shell("Front-office e protezione dati", "Sette passaggi per orientare senza promettere e trattare solo dati necessari.", inner)
}

function figureAllertaGlossario() {
  const y = 310
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${step(105, y, "1", "Nuovo bando", ["ente, profilo", "programma"], "navy", "softBlue")}
  ${step(380, y, "2", "Parole-spia", ["reati, UE", "privacy, ICT"], "bordeaux", "softRed")}
  ${step(655, y, "3", "Appendice", ["A, B, C", "D o E"], "gold", "softGold")}
  ${step(930, y, "4", "Priorita", ["subito, dopo", "taglio"], "green", "softGreen")}
  ${step(1205, y, "5", "Output", ["7 giorni", "scheda/prova"], "teal", "softTeal")}
  ${arrow(315, y + 84, 370, y + 84, "Navy")}
  ${arrow(590, y + 84, 645, y + 84, "Bordeaux")}
  ${arrow(865, y + 84, 920, y + 84, "Gold")}
  ${arrow(1140, y + 84, 1195, y + 84, "Green")}
  ${smallBox(195, 560, 360, 118, "Glossario", ["stabilizza parole", "prima del quiz"], "navy", "softBlue")}
  ${smallBox(620, 560, 360, 118, "Scheda allerta", ["peso, modulo", "fonte da verificare"], "bordeaux", "softRed")}
  ${smallBox(1045, 560, 360, 118, "Decisione", ["cosa studiare", "e cosa non studiare"], "green", "softGreen")}
  ${note(245, 815, 1110, "Il glossario non e' elenco: e' una macchina per decidere come studiare il bando.")}
`
  return shell("Schede allerta, glossario e output", "Parole-spia del bando, appendice corretta, priorita e azione entro 7 giorni.", inner)
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
  return `<g data-safe-box="${x} ${y} ${w} ${h} 12" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="${w}" height="${h}" rx="26"/>
    <circle cx="${x + 44}" cy="${y + 44}" r="18" fill="${palette[color]}"/>
    <text class="ink label" x="${x + 74}" y="${y + 52}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted body" x="${x + 34}" y="${y + 92 + index * 28}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function step(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 210 170 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="210" height="170" rx="22"/>
    <circle cx="${x + 38}" cy="${y + 38}" r="21" fill="${palette[color]}"/>
    <text x="${x + 38}" y="${y + 46}" text-anchor="middle" fill="#FFFFFF" style="font: 800 21px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 26}" y="${y + 82}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 26}" y="${y + 116 + index * 23}">${esc(lineText)}</text>`).join("\n")}
  </g>`
}

function miniStep(x, y, number, title, lines, color, soft) {
  return `<g data-safe-box="${x} ${y} 265 138 8" data-safe-name="${esc(title)}">
    <rect class="${soft}" x="${x}" y="${y}" width="265" height="138" rx="22"/>
    <circle cx="${x + 36}" cy="${y + 36}" r="20" fill="${palette[color]}"/>
    <text x="${x + 36}" y="${y + 44}" text-anchor="middle" fill="#FFFFFF" style="font: 800 20px 'Segoe UI', Arial, sans-serif">${number}</text>
    <text class="ink label" x="${x + 68}" y="${y + 44}">${esc(title)}</text>
    ${lines.map((lineText, index) => `<text class="muted small" x="${x + 28}" y="${y + 84 + index * 23}">${esc(lineText)}</text>`).join("\n")}
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
