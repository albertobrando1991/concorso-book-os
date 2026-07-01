const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-23"
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
    slug: "01-mappa-bando-diario-errori",
    title: "Mappa BANDO del diario degli errori",
    subtitle: "L'errore diventa utile quando collega bando, area, nucleo, causa e output.",
    svg: figureMappaBando()
  },
  {
    slug: "02-sei-categorie-errore",
    title: "Le sei categorie di errore",
    subtitle: "La categoria non etichetta il candidato: decide il rimedio operativo.",
    svg: figureCategorie()
  },
  {
    slug: "03-protocollo-sei-passaggi",
    title: "Protocollo in sei passaggi",
    subtitle: "Il diario si chiude solo quando il secondo tentativo conferma il miglioramento.",
    svg: figureProtocollo()
  },
  {
    slug: "04-scheda-diario-errori",
    title: "Scheda professionale del diario",
    subtitle: "Pochi campi, ma tutti orientati a una prossima azione verificabile.",
    svg: figureScheda()
  },
  {
    slug: "05-diario-per-prove",
    title: "Usare il diario nelle diverse prove",
    subtitle: "Quiz, scritto, orale e casi pratici richiedono errori letti in modo diverso.",
    svg: figureProve()
  },
  {
    slug: "06-flashcard-ripasso-materia-peggiora",
    title: "Dall'errore al ripasso mirato",
    subtitle: "Flashcard, segnali di peggioramento e rimedi devono stare nello stesso ciclo.",
    svg: figureRipasso()
  },
  {
    slug: "07-caso-marta-pattern-errori",
    title: "Caso Marta: leggere i pattern",
    subtitle: "Quattordici errori non chiedono piu studio generico, ma decisioni selettive.",
    svg: figureMarta()
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
  return `# Asset Capitolo 23

Figure generate per \`Il diario degli errori\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-diario-errori.png\` | Collegamento BANDO tra errore, causa e output successivo. |
| \`02-sei-categorie-errore.png\` | Le sei categorie che determinano il rimedio. |
| \`03-protocollo-sei-passaggi.png\` | Flusso completo: registrare, classificare, correggere, trasformare, programmare, verificare. |
| \`04-scheda-diario-errori.png\` | Scheda compilabile con i campi minimi del diario. |
| \`05-diario-per-prove.png\` | Uso differenziato del diario in quiz, scritto, orale e casi pratici. |
| \`06-flashcard-ripasso-materia-peggiora.png\` | Ciclo errore-flashcard-ripasso e segnali di materia in peggioramento. |
| \`07-caso-marta-pattern-errori.png\` | Caso guidato Marta: lettura dei pattern e decisioni selettive. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${wideCard(500, 205, 600, "Errore come dato", ["non colpa", "ma segnale di piano"], "navy", "softBlue")}
  <path class="line" d="M800 332 L800 388"/>
  <path class="line" d="M210 388 L1390 388"/>
  ${connector(210, 388, 210, 462)}
  ${connector(505, 388, 505, 575)}
  ${connector(800, 388, 800, 462)}
  ${connector(1095, 388, 1095, 575)}
  ${connector(1390, 388, 1390, 462)}
  ${stepBox(80, 462, 260, "Bando", ["materia", "prova"], "navy", "softBlue")}
  ${stepBox(375, 575, 260, "Aree", ["raggruppa", "priorita"], "bordeaux", "softRed")}
  ${stepBox(670, 462, 260, "Nuclei", ["concetto", "regola"], "gold", "softGold")}
  ${stepBox(965, 575, 260, "Diario", ["causa", "ripasso"], "green", "softGreen")}
  ${stepBox(1260, 462, 260, "Output", ["quiz", "orale", "caso"], "teal", "softTeal")}
  ${note(250, 812, 1100, "Senza diario il piano vede il punteggio, ma non vede la causa dell'errore.")}`

  return shell(
    "Mappa BANDO del diario degli errori",
    "L'errore diventa utile quando collega bando, area, nucleo, causa e output.",
    inner
  )
}

function figureCategorie() {
  const cards = [
    ["Memoria", "dato o definizione non recuperati", "flashcard", "navy", "softBlue"],
    ["Concetto", "istituti confusi tra loro", "schema comparativo", "bordeaux", "softRed"],
    ["Lettura", "negazione o eccezione saltata", "drill parole-spia", "gold", "softGold"],
    ["Tempo", "risposta veloce o incompleta", "timer e doppio giro", "green", "softGreen"],
    ["Strategia", "energia spesa nel punto sbagliato", "regola di salto", "teal", "softTeal"],
    ["Ansia", "ordine e lucidita perduti", "simulazione progressiva", "navy", "softBlue"]
  ]

  const body = cards
    .map(([title, signal, action, color, box], index) => {
      const col = index % 3
      const row = Math.floor(index / 3)
      return categoryCard(155 + col * 450, 265 + row * 245, title, signal, action, color, box)
    })
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Scrivere solo "sbagliato" non basta: serve una diagnosi</text>
  ${body}
  ${note(250, 812, 1100, "La categoria decide il rimedio: stesso punteggio, azioni completamente diverse.")}`

  return shell(
    "Le sei categorie di errore",
    "La categoria non etichetta il candidato: decide il rimedio operativo.",
    inner
  )
}

function figureProtocollo() {
  const steps = [
    ["1", "Registra", "subito dopo la prova", "navy", "softBlue"],
    ["2", "Classifica", "causa prevalente", "bordeaux", "softRed"],
    ["3", "Regola", "scritta con parole tue", "gold", "softGold"],
    ["4", "Output", "quiz, orale, caso", "green", "softGreen"],
    ["5", "Ripasso", "data e controllo", "teal", "softTeal"],
    ["6", "Verifica", "secondo tentativo", "navy", "softBlue"]
  ]

  const top = steps
    .slice(0, 3)
    .map(([num, title, body, color, box], index) => flowCard(155 + index * 450, 275, num, title, body, color, box))
    .join("\n")
  const bottom = steps
    .slice(3)
    .map(([num, title, body, color, box], index) => flowCard(1055 - index * 450, 535, num, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Un errore registrato senza scadenza resta archivio</text>
  ${top}
  <path class="arrowNavy" d="M505 390 L585 390"/>
  <path class="arrowNavy" d="M955 390 L1035 390"/>
  <path class="arrowNavy" d="M1225 480 L1225 520"/>
  ${bottom}
  <path class="arrowNavy" d="M1035 650 L955 650"/>
  <path class="arrowNavy" d="M585 650 L505 650"/>
  ${note(250, 812, 1100, "Il diario si chiude quando l'errore non si ripete, non quando la risposta sembra capita.")}`

  return shell(
    "Protocollo in sei passaggi",
    "Il diario si chiude solo quando il secondo tentativo conferma il miglioramento.",
    inner
  )
}

function figureScheda() {
  const rows = [
    ["Fonte", "quiz / scritto / orale / caso"],
    ["Materia", "area e modulo interessato"],
    ["Categoria", "memoria, concetto, lettura, tempo"],
    ["Regola", "versione corretta in parole proprie"],
    ["Azione", "flashcard, schema, drill, simulazione"],
    ["Ripasso", "data, esito, secondo tentativo"]
  ]

  const body = rows.map((row, index) => sheetRow(170, 265 + index * 78, 1260, row, index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">La scheda deve portare a una decisione, non a una raccolta passiva</text>
  <g data-safe-box="170 265 1260 468 8">
    ${body}
  </g>
  ${note(250, 765, 1100, "La colonna piu importante e' Prossima azione: senza azione il diario diventa archivio.")}`

  return shell(
    "Scheda professionale del diario",
    "Pochi campi, ma tutti orientati a una prossima azione verificabile.",
    inner
  )
}

function figureProve() {
  const cards = [
    ["Quiz", ["errori ripetuti", "lettura e tempo", "risposte incerte"], "navy", "softBlue"],
    ["Scritto", ["traccia centrata", "struttura", "linguaggio"], "bordeaux", "softRed"],
    ["Orale", ["definizione", "ordine", "collegamenti"], "gold", "softGold"],
    ["Casi pratici", ["problema", "competenza", "decisione"], "green", "softGreen"]
  ]

  const body = cards
    .map(([title, lines, color, box], index) => {
      const col = index % 2
      const row = Math.floor(index / 2)
      return proofCard(190 + col * 640, 270 + row * 250, title, lines, color, box)
    })
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Ogni prova produce un tipo diverso di errore utile</text>
  ${body}
  ${note(250, 812, 1100, "Il diario non misura solo contenuti: misura anche forma, procedura e gestione della prova.")}`

  return shell(
    "Usare il diario nelle diverse prove",
    "Quiz, scritto, orale e casi pratici richiedono errori letti in modo diverso.",
    inner
  )
}

function figureRipasso() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Le flashcard migliori nascono dagli errori ad alta resa</text>
  ${pipeCard(110, 315, "Errore", "confusione o lacuna", "bordeaux", "softRed")}
  <path class="arrowNavy" d="M355 420 L445 420"/>
  ${pipeCard(470, 315, "Flashcard", "una domanda precisa", "navy", "softBlue")}
  <path class="arrowNavy" d="M715 420 L805 420"/>
  ${pipeCard(830, 315, "Ripasso", "24-48 ore e 5-7 giorni", "green", "softGreen")}
  <path class="arrowNavy" d="M1075 420 L1165 420"/>
  ${pipeCard(1190, 315, "Esito", "secondo tentativo", "teal", "softTeal")}
  ${signalBox(170, 590, 540, "Materia che peggiora", ["errori aumentano", "istituti simili confusi", "quiz corretti solo subito dopo"], "bordeaux", "softRed")}
  ${signalBox(890, 590, 540, "Rimedio minimo", ["sospendi pagine nuove", "schema comparativo", "20 domande mirate"], "green", "softGreen")}
  <path class="arrowNavy" d="M735 665 L865 665"/>
  ${note(250, 812, 1100, "Se una materia peggiora, non aggiungere teoria: blocca, confronta, prova e misura di nuovo.")}`

  return shell(
    "Dall'errore al ripasso mirato",
    "Flashcard, segnali di peggioramento e rimedi devono stare nello stesso ciclo.",
    inner
  )
}

function figureMarta() {
  const bars = [
    ["Accesso", 5, "schema comparativo", "navy", "softBlue"],
    ["Silenzio", 3, "flashcard + 10 quiz", "bordeaux", "softRed"],
    ["Negazioni", 2, "parole-spia", "gold", "softGold"],
    ["Tempo", 2, "due giri", "green", "softGreen"],
    ["Dettagli", 2, "non priorita", "teal", "softTeal"]
  ]

  const body = bars.map((row, index) => martaRow(185, 265 + index * 92, 1230, row)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">50 quiz, 14 errori: il punteggio non basta a decidere</text>
  <g data-safe-box="185 265 1230 460 8">
    ${body}
  </g>
  ${note(250, 765, 1100, "Marta non deve studiare tutto di piu: deve correggere i pattern che si ripetono.")}`

  return shell(
    "Caso Marta: leggere i pattern",
    "Quattordici errori non chiedono piu studio generico, ma decisioni selettive.",
    inner
  )
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
      .title { font-size: 43px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-size: 22px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 25px; font-weight: 800; letter-spacing: 0; }
      .body { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 20px; }
      .small { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 18px; }
      .navy { fill: ${palette.navy}; }
      .bordeaux { fill: ${palette.bordeaux}; }
      .gold { fill: ${palette.gold}; }
      .green { fill: ${palette.green}; }
      .teal { fill: ${palette.teal}; }
      .line { stroke: ${palette.line}; stroke-width: 4; stroke-linecap: round; fill: none; }
      .thin { stroke: ${palette.border}; stroke-width: 2.5; stroke-linecap: round; fill: none; }
      .arrowNavy { stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowNavy); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="108" text-anchor="middle">${esc(subtitle)}</text>
${inner}
</svg>
`
}

function wideCard(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 77 + index * 27}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 128 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="128" rx="25"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 44}" text-anchor="middle">${esc(title)}</text>
    ${body}
  </g>`
}

function stepBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 27}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 158 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="158" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    ${rows}
  </g>`
}

function categoryCard(x, y, title, signal, action, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 390 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="390" height="190" rx="24"/>
    <rect x="${x}" y="${y}" width="390" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 195}" y="${y + 47}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    <text class="muted small" x="${x + 195}" y="${y + 94}" text-anchor="middle" style="font-size:17px">${esc(signal)}</text>
    <path class="thin" d="M${x + 55} ${y + 115} L${x + 335} ${y + 115}"/>
    <text class="ink label" x="${x + 195}" y="${y + 152}" text-anchor="middle" style="font-size:18px">${esc(action)}</text>
  </g>`
}

function flowCard(x, y, number, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 335 170 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="335" height="170" rx="24"/>
    <circle cx="${x + 58}" cy="${y + 64}" r="32" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 58}" y="${y + 75}" text-anchor="middle" fill="#FFFFFF" style="font-size:23px">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 190}" y="${y + 57}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <text class="muted small" x="${x + 190}" y="${y + 106}" text-anchor="middle" style="font-size:17px">${esc(body)}</text>
  </g>`
}

function sheetRow(x, y, w, row, index) {
  const [field, content] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  return `<g>
    <rect x="${x}" y="${y}" width="${w}" height="64" rx="12" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <rect x="${x}" y="${y}" width="245" height="64" rx="12" fill="${palette.navy}" opacity="0.96"/>
    <text class="label" x="${x + 122}" y="${y + 41}" text-anchor="middle" fill="#FFFFFF" style="font-size:18px">${esc(field)}</text>
    <text class="muted small" x="${x + 300}" y="${y + 41}" style="font-size:18px">${esc(content)}</text>
  </g>`
}

function proofCard(x, y, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + 300}" y="${y + 112 + index * 34}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 580 205 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="580" height="205" rx="24"/>
    <rect x="${x}" y="${y}" width="580" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 300}" y="${y + 52}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    <path class="thin" d="M${x + 75} ${y + 74} L${x + 505} ${y + 74}"/>
    ${rows}
  </g>`
}

function pipeCard(x, y, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 245 210 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="245" height="210" rx="24"/>
    <circle cx="${x + 122.5}" cy="${y + 55}" r="34" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 122.5}" y="${y + 132}" text-anchor="middle" style="font-size:22px;fill:${palette[colorClass]}">${esc(title)}</text>
    <text class="muted small" x="${x + 122.5}" y="${y + 170}" text-anchor="middle" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function signalBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 90 + index * 27}" text-anchor="middle" style="font-size:15px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 180 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="180" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    ${rows}
  </g>`
}

function martaRow(x, y, w, row) {
  const [label, count, action, colorClass, boxClass] = row
  const max = 5
  const barWidth = Math.round((count / max) * 420)
  return `<g data-safe-box="${x} ${y} ${w} 72 8">
    <rect x="${x}" y="${y}" width="${w}" height="72" rx="16" fill="${palette.white}" stroke="${palette.border}" stroke-width="2"/>
    <text class="${colorClass} label" x="${x + 110}" y="${y + 45}" text-anchor="middle" style="font-size:19px">${esc(label)}</text>
    <rect class="${boxClass}" x="${x + 235}" y="${y + 22}" width="420" height="28" rx="14"/>
    <rect x="${x + 235}" y="${y + 22}" width="${barWidth}" height="28" rx="14" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 705}" y="${y + 45}" text-anchor="middle" style="font-size:20px;fill:${palette.ink}">${count}</text>
    <text class="muted small" x="${x + 950}" y="${y + 45}" text-anchor="middle" style="font-size:17px">${esc(action)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 112 ? 18 : text.length > 94 ? 19 : 20
  return `<g data-safe-box="${x} ${y} ${w} 64 8">
    <rect class="note" x="${x}" y="${y}" width="${w}" height="64" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-weight:800;font-size:${fontSize}px">${esc(text)}</text>
  </g>`
}

function connector(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
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
