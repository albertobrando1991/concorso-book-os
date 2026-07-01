const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-27"
)

const palette = {
  bg: "#F8FAFC",
  ink: "#0F172A",
  muted: "#526174",
  border: "#CBD5E1",
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
  tealSoft: "#E4F4F5",
  cream: "#FFF7ED"
}

const figures = [
  {
    slug: "01-mappa-bando-concorsi-paralleli",
    title: "Mappa BANDO dei concorsi paralleli",
    subtitle: "Piu bandi entrano nel metodo solo se condividono decisioni, studio e output.",
    description: "Mappa BANDO per trasformare piu procedure aperte in una sola architettura di studio.",
    svg: figureMappaBando()
  },
  {
    slug: "02-portafoglio-concorsi",
    title: "Portafoglio concorsi",
    subtitle: "Non tutti i bandi hanno lo stesso ruolo: guida, satellite o parcheggio.",
    description: "Schema per assegnare a ogni concorso un ruolo operativo nel calendario unico.",
    svg: figurePortafoglio()
  },
  {
    slug: "03-matrice-compatibilita",
    title: "Matrice di compatibilita",
    subtitle: "La scelta diventa visibile quando tutti i bandi stanno nella stessa pagina.",
    description: "Griglia sintetica per confrontare profilo, scadenza, prove, materie e rischio dispersione.",
    svg: figureMatrice()
  },
  {
    slug: "04-regola-70-20-10",
    title: "Regola 70 / 20 / 10",
    subtitle: "Il concorso guida comanda, il satellite aggancia, il controllo impedisce errori.",
    description: "Ripartizione iniziale del tempo tra concorso guida, satellite e monitoraggio logistico.",
    svg: figureRegola()
  },
  {
    slug: "05-calendario-unico-blocchi",
    title: "Calendario unico a blocchi",
    subtitle: "Un solo calendario: comune, specifico, output e controllo.",
    description: "Settimana-tipo con blocchi etichettati per evitare calendari paralleli e dispersione.",
    svg: figureCalendario()
  },
  {
    slug: "06-diario-semaforo-decisionale",
    title: "Diario e semaforo decisionale",
    subtitle: "Gli errori dicono dove intervenire; il colore decide se continuare o parcheggiare.",
    description: "Collegamento tra etichette del diario e revisione settimanale verde, giallo, rosso.",
    svg: figureDiarioSemaforo()
  },
  {
    slug: "07-caso-marta-portafoglio",
    title: "Caso Marta: scegliere senza disperdersi",
    subtitle: "Tre bandi aperti diventano guida, satellite e parcheggio.",
    description: "Caso guidato: Comune come guida, Ministero come satellite, Agenzia fiscale in parcheggio.",
    svg: figureCasoMarta()
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
  const rows = figures
    .map((figure) => `| \`${figure.slug}.png\` | ${figure.description} |`)
    .join("\n")

  return `# Asset Capitolo 27

Figure generate per \`Gestire concorsi paralleli senza disperdersi\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const items = [
    ["B", "Bando", "procedure compatibili", palette.navy, palette.blueSoft],
    ["A", "Aree", "comune e specifico", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "studio una volta", palette.gold, palette.goldSoft],
    ["D", "Diario", "errori condivisi", palette.green, palette.greenSoft],
    ["O", "Output", "prova prioritaria", palette.teal, palette.tealSoft]
  ]
  const boxes = items
    .map(([letter, title, body, color, fill], index) =>
      verticalStep(115 + index * 285, 390, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 285, 513, 392 + index * 285, 513)).join("\n")

  return shell(
    "Mappa BANDO dei concorsi paralleli",
    "Piu bandi entrano nel metodo solo se condividono decisioni, studio e output.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(440, 205, 720, "Portafoglio ordinato", ["guida, satellite, parcheggio", "un solo sistema"], palette.navy, palette.blueSoft)}
    ${boxes}
    ${arrows}
    ${note(250, 812, 1100, "Se due concorsi non condividono nulla, competono per lo stesso tempo.")}
    `
  )
}

function figurePortafoglio() {
  return shell(
    "Portafoglio concorsi",
    "Non tutti i bandi hanno lo stesso ruolo: guida, satellite o parcheggio.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${roleBox(115, 275, "Guida", ["migliori ore", "simulazioni", "tagli"], palette.navy, palette.blueSoft)}
    ${roleBox(620, 275, "Satellite", ["aggancia il core", "usa moduli avviati", "non crea piano autonomo"], palette.gold, palette.goldSoft)}
    ${roleBox(1125, 275, "Parcheggio", ["scheda minima", "scadenze salvate", "nessuno studio quotidiano"], palette.green, palette.greenSoft)}
    ${arrow(490, 455, 620, 455)}
    ${arrow(995, 455, 1125, 455)}
    ${note(250, 812, 1100, "Un bando interessante non deve entrare per forza nel calendario attivo.")}
    `
  )
}

function figureMatrice() {
  const rows = [
    ["Profilo", "alto", "medio", "basso"],
    ["Scadenza", "vicina", "gestibile", "sovrapposta"],
    ["Materie comuni", "molte", "alcune", "poche"],
    ["Materie nuove", "poche", "medie", "molte"],
    ["Prova", "scritta", "quiz", "diversa"],
    ["Decisione", "guida", "satellite", "parcheggio"]
  ]
  const body = rows.map((row, index) => matrixRow(185, 270 + index * 68, row, index)).join("\n")

  return shell(
    "Matrice di compatibilita",
    "La scelta diventa visibile quando tutti i bandi stanno nella stessa pagina.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    <g data-safe-box="185 215 1230 495 4">
      <rect x="185" y="215" width="1230" height="495" rx="22" fill="${palette.white}" stroke="${palette.border}" stroke-width="3"/>
      ${matrixHeader(185, 215)}
      ${body}
    </g>
    ${note(250, 812, 1100, "Non serve precisione matematica: serve una decisione visibile.")}
    `
  )
}

function figureRegola() {
  return shell(
    "Regola 70 / 20 / 10",
    "Il concorso guida comanda, il satellite aggancia, il controllo impedisce errori.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    <g data-safe-box="155 260 1290 360 10">
      ${percentBlock(155, 260, 710, "70%", "Concorso guida", ["priorita", "simulazioni", "tagli"], palette.navy, palette.blueSoft)}
      ${percentBlock(895, 260, 300, "20%", "Satellite", ["aggancio", "differenze"], palette.gold, palette.goldSoft)}
      ${percentBlock(1225, 260, 220, "10%", "Controllo", ["avvisi", "logistica"], palette.green, palette.greenSoft)}
    </g>
    ${wideCard(470, 650, 660, "Il 10% non si sacrifica", ["evita scadenze dimenticate, ricevute non salvate e avvisi non letti"], palette.teal, palette.tealSoft)}
    ${note(250, 812, 1100, "Se il satellite richiede troppo, non aumentare la quota: cambia decisione.")}
    `
  )
}

function figureCalendario() {
  const days = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab"]
  const columns = days.map((day, index) => dayColumn(155 + index * 215, 285, day, index)).join("\n")

  return shell(
    "Calendario unico a blocchi",
    "Un solo calendario: comune, specifico, output e controllo.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    <text class="label navy" x="800" y="225" text-anchor="middle">Ogni blocco deve avere un'etichetta: comune, specifico, output o controllo</text>
    ${columns}
    ${note(250, 812, 1100, "Calendari separati nascondono dispersione; il calendario unico la rende visibile.")}
    `
  )
}

function figureDiarioSemaforo() {
  return shell(
    "Diario e semaforo decisionale",
    "Gli errori dicono dove intervenire; il colore decide se continuare o parcheggiare.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${tagBox(135, 290, "COMUNE", "vale per piu concorsi", "ripasso prioritario", palette.navy, palette.blueSoft)}
    ${tagBox(135, 475, "PROFILO", "modulo specifico", "blocco mirato", palette.bordeaux, palette.redSoft)}
    ${tagBox(135, 660, "LOGISTICA", "scadenze e documenti", "checklist subito", palette.teal, palette.tealSoft)}
    ${arrow(530, 452, 660, 452)}
    ${trafficLight(690, 275)}
    ${note(250, 812, 1100, "Un concorso rosso non e' un fallimento: e' un segnale da trattare.")}
    `
  )
}

function figureCasoMarta() {
  return shell(
    "Caso Marta: scegliere senza disperdersi",
    "Tre bandi aperti diventano guida, satellite e parcheggio.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${caseBox(105, 295, "Comune", ["45 giorni", "prova scritta", "materie avviate"], "GUIDA", palette.navy, palette.blueSoft)}
    ${caseBox(620, 295, "Ministero", ["quiz e orale", "molte materie comuni", "differenze gestibili"], "SATELLITE", palette.gold, palette.goldSoft)}
    ${caseBox(1135, 295, "Agenzia fiscale", ["tributario nuovo", "scadenza sovrapposta", "prova diversa"], "PARCHEGGIO", palette.green, palette.greenSoft)}
    ${arrow(480, 455, 620, 455)}
    ${arrow(995, 455, 1135, 455)}
    <g data-safe-box="430 655 740 72 8">
      <rect x="430" y="655" width="740" height="72" rx="22" fill="${palette.cream}" stroke="#EFC58D" stroke-width="3"/>
      <text class="body strong" x="800" y="700" text-anchor="middle">La scelta non elimina il terzo concorso: lo rende innocuo.</text>
    </g>
    ${note(250, 812, 1100, "Il metodo premia chi trasforma tempo limitato in output ad alta probabilita.")}
    `
  )
}

function shell(title, subtitle, body) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
  <title id="title">${escapeXml(title)}</title>
  <desc id="desc">${escapeXml(subtitle)}</desc>
  <style>
    .bg { fill: ${palette.bg}; }
    .card { fill: ${palette.white}; stroke: ${palette.border}; stroke-width: 3; }
    .title { font: 800 44px Arial, sans-serif; fill: ${palette.ink}; }
    .subtitle { font: 400 22px Arial, sans-serif; fill: ${palette.muted}; }
    .label { font: 800 25px Arial, sans-serif; fill: ${palette.ink}; }
    .body { font: 400 19px Arial, sans-serif; fill: ${palette.ink}; }
    .small { font: 400 16px Arial, sans-serif; fill: ${palette.ink}; }
    .strong { font-weight: 800; }
    .muted { fill: ${palette.muted}; }
    .navy { fill: ${palette.navy}; }
    .whiteText { fill: ${palette.white}; }
    .line { stroke: ${palette.navy}; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; fill: none; }
  </style>
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M2,2 L10,6 L2,10 Z" fill="${palette.navy}"/>
    </marker>
  </defs>
  <rect class="bg" width="1600" height="900"/>
  <g data-safe-box="80 16 1440 118 0">
    <text class="title" x="800" y="68" text-anchor="middle">${escapeXml(title)}</text>
    <text class="subtitle" x="800" y="108" text-anchor="middle">${escapeXml(subtitle)}</text>
  </g>
  ${body}
</svg>
`
}

function wideCard(x, y, w, title, lines, color, fill) {
  const textLines = lines
    .map((line, index) => `<text class="small" x="${x + w / 2}" y="${y + 82 + index * 28}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 150 8">
    <rect x="${x}" y="${y}" width="${w}" height="150" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="${w}" height="12" rx="6" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 52}" text-anchor="middle">${escapeXml(title)}</text>
    ${textLines}
  </g>`
}

function verticalStep(x, y, letter, title, body, color, fill) {
  return `<g data-safe-box="${x} ${y} 240 205 8">
    <rect x="${x}" y="${y}" width="240" height="205" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 120}" cy="${y + 50}" r="32" fill="${color}"/>
    <text class="label whiteText" x="${x + 120}" y="${y + 59}" text-anchor="middle">${escapeXml(letter)}</text>
    <text class="label" x="${x + 120}" y="${y + 112}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 120}" y="${y + 152}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function roleBox(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 175}" y="${y + 146 + index * 34}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 350 360 8">
    <rect x="${x}" y="${y}" width="350" height="360" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="350" height="14" rx="7" fill="${color}"/>
    <text class="label" x="${x + 175}" y="${y + 72}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <line x1="${x + 70}" y1="${y + 100}" x2="${x + 280}" y2="${y + 100}" stroke="${palette.border}" stroke-width="3"/>
    ${rendered}
  </g>`
}

function matrixHeader(x, y) {
  const headers = ["Criterio", "Concorso A", "Concorso B", "Concorso C"]
  return headers
    .map((header, index) => {
      const colX = x + index * 307.5
      return `<rect x="${colX}" y="${y}" width="307.5" height="62" fill="${index === 0 ? palette.navy : palette.blueSoft}" stroke="${palette.border}" stroke-width="2"/>
      <text class="small strong${index === 0 ? " whiteText" : ""}" x="${colX + 153.75}" y="${y + 39}" text-anchor="middle">${escapeXml(header)}</text>`
    })
    .join("\n")
}

function matrixRow(x, y, row, index) {
  return row
    .map((cell, cellIndex) => {
      const colX = x + cellIndex * 307.5
      const fill = index % 2 === 0 ? palette.white : palette.blueSoft
      return `<rect x="${colX}" y="${y}" width="307.5" height="68" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
      <text class="small${cellIndex === 0 ? " strong" : ""}" x="${colX + 153.75}" y="${y + 42}" text-anchor="middle">${escapeXml(cell)}</text>`
    })
    .join("\n")
}

function percentBlock(x, y, w, pct, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + w / 2}" y="${y + 220 + index * 30}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 360 8">
    <rect x="${x}" y="${y}" width="${w}" height="360" rx="30" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="title" x="${x + w / 2}" y="${y + 105}" text-anchor="middle" fill="${color}">${escapeXml(pct)}</text>
    <text class="label" x="${x + w / 2}" y="${y + 160}" text-anchor="middle">${escapeXml(title)}</text>
    ${rendered}
  </g>`
}

function dayColumn(x, y, day, index) {
  const blockSets = [
    [["Comune", palette.navy, palette.blueSoft], ["Output", palette.green, palette.greenSoft]],
    [["Specifico", palette.bordeaux, palette.redSoft], ["Comune", palette.navy, palette.blueSoft]],
    [["Output", palette.green, palette.greenSoft], ["Controllo", palette.teal, palette.tealSoft]],
    [["Comune", palette.navy, palette.blueSoft], ["Specifico", palette.bordeaux, palette.redSoft]],
    [["Controllo", palette.teal, palette.tealSoft], ["Output", palette.green, palette.greenSoft]],
    [["Comune", palette.navy, palette.blueSoft], ["Recupero", palette.gold, palette.goldSoft]]
  ]
  const blocks = blockSets[index]
    .map(([label, color, fill], blockIndex) => `
      <rect x="${x + 18}" y="${y + 92 + blockIndex * 112}" width="150" height="82" rx="16" fill="${fill}" stroke="${color}" stroke-width="3"/>
      <text class="small strong" x="${x + 93}" y="${y + 142 + blockIndex * 112}" text-anchor="middle" fill="${color}">${escapeXml(label)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 185 340 4">
    <rect x="${x}" y="${y}" width="185" height="340" rx="22" fill="${palette.white}" stroke="${palette.border}" stroke-width="3"/>
    <text class="label" x="${x + 92.5}" y="${y + 54}" text-anchor="middle">${escapeXml(day)}</text>
    ${blocks}
  </g>`
}

function tagBox(x, y, title, body, action, color, fill) {
  return `<g data-safe-box="${x} ${y} 360 130 8">
    <rect x="${x}" y="${y}" width="360" height="130" rx="22" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" x="${x + 180}" y="${y + 42}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <text class="small" x="${x + 180}" y="${y + 78}" text-anchor="middle">${escapeXml(body)}</text>
    <text class="small strong" x="${x + 180}" y="${y + 108}" text-anchor="middle">${escapeXml(action)}</text>
  </g>`
}

function trafficLight(x, y) {
  const lights = [
    ["Verde", "compatibile", "resta attivo", palette.green, palette.greenSoft],
    ["Giallo", "sotto pressione", "riduci o proteggi", palette.gold, palette.goldSoft],
    ["Rosso", "rompe il sistema", "parcheggia", palette.bordeaux, palette.redSoft]
  ]
  const rows = lights
    .map(([name, body, action, color, fill], index) => `
      <g data-safe-box="${x + 120} ${y + 55 + index * 150} 560 120 8">
        <rect x="${x + 120}" y="${y + 55 + index * 150}" width="560" height="120" rx="22" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <circle cx="${x + 175}" cy="${y + 115 + index * 150}" r="27" fill="${color}"/>
        <text class="label" x="${x + 300}" y="${y + 104 + index * 150}" text-anchor="middle" fill="${color}">${escapeXml(name)}</text>
        <text class="small" x="${x + 460}" y="${y + 104 + index * 150}" text-anchor="middle">${escapeXml(body)}</text>
        <text class="small strong" x="${x + 460}" y="${y + 136 + index * 150}" text-anchor="middle">${escapeXml(action)}</text>
      </g>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 780 540 4">
    <rect x="${x}" y="${y}" width="780" height="540" rx="28" fill="${palette.white}" stroke="${palette.border}" stroke-width="3"/>
    <text class="label navy" x="${x + 390}" y="${y + 42}" text-anchor="middle">Revisione settimanale</text>
    ${rows}
  </g>`
}

function caseBox(x, y, title, lines, role, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 170}" y="${y + 145 + index * 32}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 340 330 8">
    <rect x="${x}" y="${y}" width="340" height="330" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="340" height="14" rx="7" fill="${color}"/>
    <text class="label" x="${x + 170}" y="${y + 62}" text-anchor="middle" fill="${color}">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 170}" y="${y + 102}" text-anchor="middle">${escapeXml(role)}</text>
    <line x1="${x + 64}" y1="${y + 118}" x2="${x + 276}" y2="${y + 118}" stroke="${palette.border}" stroke-width="3"/>
    ${rendered}
  </g>`
}

function note(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 66 8">
    <rect x="${x}" y="${y}" width="${w}" height="66" rx="22" fill="${palette.cream}" stroke="#EFC58D" stroke-width="3"/>
    <text class="body strong" x="${x + w / 2}" y="${y + 43}" text-anchor="middle">${escapeXml(text)}</text>
  </g>`
}

function arrow(x1, y1, x2, y2) {
  return `<path class="line" marker-end="url(#arrow)" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function escapeXml(value) {
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
