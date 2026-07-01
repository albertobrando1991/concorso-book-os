const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
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
  cream: "#FFF7ED",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  green: "#2F7D5A",
  greenSoft: "#E7F3ED",
  white: "#FFFFFF"
}

const figures = [
  {
    slug: "01-contratti-pubblici-mappa",
    title: "Contratti pubblici essenziali",
    subtitle: "Il contratto pubblico come ciclo: bisogno, scelta, esecuzione, dati e controllo.",
    svg: figureMappa()
  },
  {
    slug: "02-ciclo-fabbisogno-esecuzione",
    title: "Dal fabbisogno all'esecuzione",
    subtitle: "La sequenza che impedisce di ridurre il contratto pubblico alla sola gara.",
    svg: figureCiclo()
  },
  {
    slug: "03-procedure-affidamento-concorrenza",
    title: "Procedure e intensita delle regole",
    subtitle: "Importo, complessita e impatto sul mercato aumentano formalita, pubblicita e controlli.",
    svg: figureProcedure()
  },
  {
    slug: "04-documenti-gara-offerte-stipula",
    title: "Documenti, requisiti e stipula",
    subtitle: "Dalla procedura conoscibile al vincolo contrattuale: ogni parola ha una funzione diversa.",
    svg: figureDocumenti()
  },
  {
    slug: "05-ecosistema-digitale-contratti",
    title: "Ecosistema digitale dei contratti",
    subtitle: "BDNCP, PCP, FVOE, CIG e piattaforme non sono sinonimi: presidiano passaggi diversi.",
    svg: figureDigitale()
  },
  {
    slug: "06-acquisti-controlli-responsabilita",
    title: "Dal portale al controllo",
    subtitle: "Consip, MEPA e strumenti digitali restano dentro responsabilita, tracciabilita e risultato.",
    svg: figureControlli()
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
      const page = await browser.newPage({
        viewport: { width: 1600, height: 900 },
        deviceScaleFactor: 1
      })
      const encoded = Buffer.from(figure.svg, "utf8").toString("base64")
      await page.setContent(
        `<html><body style="margin:0;background:${palette.bg}"><img src="data:image/svg+xml;base64,${encoded}" width="1600" height="900"></body></html>`,
        { waitUntil: "load" }
      )
      await page.locator("img").screenshot({
        path: path.join(OUTPUT_DIR, `${figure.slug}.png`)
      })
      await page.close()
    }
  } finally {
    await browser.close()
  }

  await fs.writeFile(path.join(OUTPUT_DIR, "README.md"), renderReadme(), "utf8")
}

function renderReadme() {
  return `# Asset Capitolo 9

Figure generate per \`Contratti pubblici essenziali\`.

| File | Funzione didattica |
|---|---|
| \`01-contratti-pubblici-mappa.png\` | Mappa generale del contratto pubblico come ciclo: fabbisogno, procedura, operatore, esecuzione e controllo. |
| \`02-ciclo-fabbisogno-esecuzione.png\` | Sequenza operativa dal bisogno pubblico alla trasparenza finale. |
| \`03-procedure-affidamento-concorrenza.png\` | Scala didattica delle procedure e dell'intensita di concorrenza, formalita e controlli. |
| \`04-documenti-gara-offerte-stipula.png\` | Distinzione tra bando, disciplinare, capitolato, requisiti, offerte, aggiudicazione e stipula. |
| \`05-ecosistema-digitale-contratti.png\` | Ecosistema digitale: BDNCP, PCP, FVOE, CIG e piattaforme di approvvigionamento. |
| \`06-acquisti-controlli-responsabilita.png\` | Sintesi pre-epilogativa su Consip, MEPA, ANAC, tracciabilita, controlli e responsabilita. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
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
      .note { fill: ${palette.cream}; stroke: #E7C18E; stroke-width: 2.5; }
      .ink { fill: ${palette.ink}; font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; }
      .muted { fill: ${palette.muted}; font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; }
      .title { font-size: 44px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-size: 23px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 25px; font-weight: 800; }
      .body { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 20px; }
      .small { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 18px; }
      .tiny { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 16px; }
      .navy { fill: ${palette.navy}; }
      .bordeaux { fill: ${palette.bordeaux}; }
      .gold { fill: ${palette.gold}; }
      .green { fill: ${palette.green}; }
      .line { stroke: ${palette.line}; stroke-width: 4; stroke-linecap: round; fill: none; }
      .thin { stroke: ${palette.border}; stroke-width: 2.5; stroke-linecap: round; fill: none; }
      .arrowNavy { stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowNavy); }
      .arrowBordeaux { stroke: ${palette.bordeaux}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowBordeaux); }
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/>
    </marker>
    <marker id="arrowBordeaux" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.bordeaux}"/>
    </marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/>
    </marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="108" text-anchor="middle">${esc(subtitle)}</text>
${inner}
</svg>
`
}

function figureMappa() {
  const inner = `
  ${card(565, 190, 470, 150, "Contratto pubblico", ["risorse pubbliche", "mercato", "interesse pubblico"], "navy", "card")}
  <path class="line" d="M800 340 L800 410"/>
  <path class="line" d="M250 410 L1350 410"/>
  <path class="line" d="M250 410 L250 455"/>
  <path class="line" d="M525 410 L525 455"/>
  <path class="line" d="M800 410 L800 455"/>
  <path class="line" d="M1075 410 L1075 455"/>
  <path class="line" d="M1350 410 L1350 455"/>
  ${card(105, 455, 290, 130, "Fabbisogno", ["che cosa serve", "e per quale fine"], "navy", "softBlue")}
  ${card(380, 605, 290, 130, "Procedura", ["come si sceglie", "l'operatore"], "bordeaux", "softRed")}
  ${card(655, 455, 290, 130, "Operatore", ["requisiti", "offerta e ruolo"], "gold", "softGold")}
  ${card(930, 605, 290, 130, "Esecuzione", ["prestazione", "tempi e qualita"], "green", "softGreen")}
  ${card(1205, 455, 290, 130, "Controllo", ["dati, tracciabilita", "responsabilita"], "navy", "softBlue")}
  ${note(260, 790, 1080, "Domanda guida: la PA ha trasformato un bisogno reale in una prestazione controllata?")}
`
  return shell("Contratti pubblici essenziali", "Il contratto pubblico come ciclo: bisogno, scelta, esecuzione, dati e controllo.", inner)
}

function figureCiclo() {
  const steps = [
    ["1", "Fabbisogno", "bisogno pubblico"],
    ["2", "Programmazione", "priorita e risorse"],
    ["3", "Progettazione", "oggetto e qualita"],
    ["4", "Decisione", "atto e copertura"],
    ["5", "Procedura", "modello di scelta"],
    ["6", "Offerte", "documenti e requisiti"],
    ["7", "Valutazione", "criteri e controlli"],
    ["8", "Aggiudicazione", "operatore scelto"],
    ["9", "Stipula", "vincolo contrattuale"],
    ["10", "Esecuzione", "prestazione reale"],
    ["11", "Verifica e dati", "pagamento, BDNCP"]
  ]
  const top = steps.slice(0, 6)
  const bottom = steps.slice(6)
  const topX = [70, 315, 560, 805, 1050, 1295]
  const bottomX = [160, 445, 730, 1015, 1300]
  const cardWidth = 200
  const topCards = top.map((item, index) => stepCard(topX[index], 210, item, cardWidth)).join("\n")
  const bottomCards = bottom.map((item, index) => stepCard(bottomX[index], 535, item, cardWidth)).join("\n")
  const topArrows = topX
    .slice(0, -1)
    .map((x, index) => `<path class="arrowNavy" d="M${x + cardWidth + 12} 292 L${topX[index + 1] - 18} 292"/>`)
    .join("\n")
  const bottomArrows = bottomX
    .slice(0, -1)
    .map((x, index) => `<path class="arrowBordeaux" d="M${x + cardWidth + 12} 617 L${bottomX[index + 1] - 18} 617"/>`)
    .join("\n")
  const inner = `
  ${topCards}
  ${topArrows}
  <path class="arrowGold" d="M1395 340 C1445 410 1340 480 1280 525"/>
  ${bottomCards}
  ${bottomArrows}
  ${note(260, 800, 1080, "Regola da concorso: non saltare dalla gara al pagamento; esecuzione e controlli chiudono il ciclo.")}
`
  return shell("Dal fabbisogno all'esecuzione", "La sequenza che impedisce di ridurre il contratto pubblico alla sola gara.", inner)
}

function figureProcedure() {
  const inner = `
  <rect class="card" x="105" y="190" width="510" height="560" rx="26"/>
  <text class="navy label" x="360" y="245" text-anchor="middle">Scala operativa</text>
  ${bar(170, 305, 330, "Affidamento diretto", "semplificato, non arbitrario", palette.green)}
  ${bar(170, 410, 370, "Procedura negoziata", "consultazione di operatori", palette.gold)}
  ${bar(170, 515, 410, "Procedura ristretta", "candidati selezionati, poi offerta", palette.bordeaux)}
  ${bar(170, 620, 450, "Procedura aperta", "partecipazione piu ampia", palette.navy)}
  <path class="arrowNavy" d="M705 665 L705 285"/>
  <text class="ink label" x="760" y="320">Aumentano</text>
  <text class="muted body" x="760" y="360">formalita</text>
  <text class="muted body" x="760" y="392">pubblicita</text>
  <text class="muted body" x="760" y="424">concorrenza</text>
  <text class="muted body" x="760" y="456">controlli</text>
  ${card(930, 235, 470, 150, "Criterio pratico", ["piu importo, complessita", "o impatto sul mercato", "piu procedura strutturata"], "bordeaux", "softRed")}
  ${card(930, 445, 470, 150, "Errore da evitare", ["sotto soglia non significa", "scelta fiduciaria libera", "o assenza di motivazione"], "gold", "softGold")}
  ${note(780, 675, 760, "Prima qualifica oggetto e importo; poi scegli la procedura coerente.")}
`
  return shell("Procedure e intensita delle regole", "Importo, complessita e impatto sul mercato aumentano formalita, pubblicita e controlli.", inner)
}

function figureDocumenti() {
  const inner = `
  ${card(80, 210, 300, 150, "Bando", ["rende conoscibile", "la procedura"], "navy", "softBlue")}
  ${card(460, 210, 300, 150, "Disciplinare", ["regola partecipazione", "documenti e termini"], "bordeaux", "softRed")}
  ${card(840, 210, 300, 150, "Capitolato", ["descrive prestazioni", "condizioni tecniche"], "gold", "softGold")}
  ${card(1220, 210, 300, 150, "Requisiti", ["chi puo partecipare", "e con quali prove"], "green", "softGreen")}
  <path class="arrowNavy" d="M385 285 L445 285"/>
  <path class="arrowNavy" d="M765 285 L825 285"/>
  <path class="arrowNavy" d="M1145 285 L1205 285"/>
  <path class="line" d="M800 395 L800 455"/>
  ${card(190, 500, 330, 145, "Offerta", ["tecnica ed economica", "secondo criteri noti"], "navy", "card")}
  ${card(635, 500, 330, 145, "Aggiudicazione", ["individua", "l'operatore scelto"], "bordeaux", "card")}
  ${card(1080, 500, 330, 145, "Stipula", ["perfeziona", "il vincolo contrattuale"], "gold", "card")}
  <path class="arrowBordeaux" d="M525 572 L620 572"/>
  <path class="arrowBordeaux" d="M970 572 L1065 572"/>
  ${note(250, 780, 1100, "Formula da ricordare: documenti chiari, offerta valutabile, aggiudicazione distinta dalla stipula.")}
`
  return shell("Documenti, requisiti e stipula", "Dalla procedura conoscibile al vincolo contrattuale: ogni parola ha una funzione diversa.", inner)
}

function figureDigitale() {
  const inner = `
  ${card(575, 205, 450, 165, "ANAC", ["ecosistema dati", "vigilanza e tracciabilita"], "navy", "card")}
  <path class="line" d="M800 370 L800 425"/>
  <path class="line" d="M250 425 L1350 425"/>
  <path class="line" d="M250 425 L250 470"/>
  <path class="line" d="M525 425 L525 470"/>
  <path class="line" d="M800 425 L800 470"/>
  <path class="line" d="M1075 425 L1075 470"/>
  <path class="line" d="M1350 425 L1350 470"/>
  ${card(105, 470, 290, 135, "BDNCP", ["banca dati nazionale", "dei contratti"], "navy", "softBlue")}
  ${card(380, 620, 290, 135, "PCP", ["piattaforma contratti", "pubblici"], "bordeaux", "softRed")}
  ${card(655, 470, 290, 135, "FVOE", ["verifica requisiti", "operatore economico"], "gold", "softGold")}
  ${card(930, 620, 290, 135, "CIG", ["identificazione", "e tracciabilita"], "green", "softGreen")}
  ${card(1205, 470, 290, 135, "Piattaforme", ["procedure, dati", "comunicazioni"], "navy", "softBlue")}
  ${note(250, 800, 1100, "Digitalizzazione non significa solo gara online: collega atti, dati, requisiti, pubblicita e controlli.")}
`
  return shell("Ecosistema digitale dei contratti", "BDNCP, PCP, FVOE, CIG e piattaforme non sono sinonimi: presidiano passaggi diversi.", inner)
}

function figureControlli() {
  const inner = `
  <rect class="card" x="80" y="190" width="1440" height="540" rx="30"/>
  <text class="navy label" x="800" y="245" text-anchor="middle">La scelta digitale resta dentro il ciclo pubblico</text>
  ${card(135, 315, 260, 125, "Consip", ["programma", "razionalizzazione"], "navy", "softBlue")}
  ${card(425, 315, 260, 125, "Acquisti in Rete", ["portale", "amministrazioni-imprese"], "bordeaux", "softRed")}
  ${card(715, 315, 260, 125, "MEPA", ["mercato elettronico", "sotto soglia"], "gold", "softGold")}
  ${card(1005, 315, 260, 125, "Convenzioni", ["condizioni", "gia definite"], "green", "softGreen")}
  ${card(1295, 315, 180, 125, "SDAPA", ["sistema", "dinamico"], "navy", "softBlue")}
  <path class="line" d="M800 475 L800 525"/>
  <path class="line" d="M265 525 L1335 525"/>
  <path class="line" d="M265 525 L265 560"/>
  <path class="line" d="M535 525 L535 560"/>
  <path class="line" d="M800 525 L800 560"/>
  <path class="line" d="M1065 525 L1065 560"/>
  <path class="line" d="M1335 525 L1335 560"/>
  ${pill(150, 575, 230, "Motivazione", palette.navy)}
  ${pill(420, 575, 230, "CIG e dati", palette.bordeaux)}
  ${pill(685, 575, 230, "Controlli", palette.gold)}
  ${pill(950, 575, 230, "Esecuzione", palette.green)}
  ${pill(1220, 575, 230, "Responsabilita", palette.navy)}
  ${note(250, 790, 1100, "Il portale aiuta la procedura, ma non sostituisce Codice, copertura, tracciabilita e verifica della prestazione.")}
`
  return shell("Dal portale al controllo", "Consip, MEPA e strumenti digitali restano dentro responsabilita, tracciabilita e risultato.", inner)
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleY = y + 42
  const titleFontSize = title.length > 18 ? 22 : title.length > 14 ? 24 : 25
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 25}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${titleY}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function stepCard(x, y, [number, title, subtitle], w = 200) {
  const center = x + w / 2
  const titleFontSize = title.length > 13 ? 18 : 20
  const subtitleFontSize = subtitle.length > 18 ? 17 : 18
  return `<g data-safe-box="${x} ${y} ${w} 165 8">
    <rect class="card" x="${x}" y="${y}" width="${w}" height="165" rx="20"/>
    <circle cx="${center}" cy="${y + 39}" r="25" fill="${palette.gold}"/>
    <text class="ink label" x="${center}" y="${y + 48}" text-anchor="middle">${esc(number)}</text>
    <text class="navy label" x="${center}" y="${y + 93}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${center}" y="${y + 125}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function bar(x, y, width, title, subtitle, color) {
  return `<g data-safe-box="${x} ${y} ${width} 72 8">
    <rect x="${x}" y="${y}" width="${width}" height="72" rx="18" fill="${color}"/>
    <text class="label" x="${x + width / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:21px">${esc(title)}</text>
    <text class="small" x="${x + width / 2}" y="${y + 56}" text-anchor="middle" fill="#FFFFFF" style="font-size:17px">${esc(subtitle)}</text>
  </g>`
}

function pill(x, y, w, text, color) {
  const fontSize = text.length > 13 ? 20 : 21
  return `<g data-safe-box="${x} ${y} ${w} 58 8">
    <rect x="${x}" y="${y}" width="${w}" height="58" rx="29" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 38}" text-anchor="middle" fill="#FFFFFF" style="font-size:${fontSize}px">${esc(text)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 95 ? 18 : text.length > 80 ? 19 : 20
  return `<g data-safe-box="${x} ${y} ${w} 64 8">
    <rect class="note" x="${x}" y="${y}" width="${w}" height="64" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-weight:800;font-size:${fontSize}px">${esc(text)}</text>
  </g>`
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
