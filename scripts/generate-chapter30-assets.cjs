const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-30"
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
  violet: "#5B3B82",
  white: "#FFFFFF",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5",
  violetSoft: "#EFEAF7",
  cream: "#FFF7ED"
}

const figures = [
  {
    slug: "01-mappa-bando-dopo-prova",
    title: "Mappa BANDO dopo la prova",
    subtitle: "Chiudi il ciclo: fonti, diagnosi, Diario e prossima decisione.",
    description: "Mappa per trasformare esito, errori e fonti ufficiali nella prossima decisione.",
    svg: figureMappaBando()
  },
  {
    slug: "02-prime-24-ore",
    title: "Prime 24 ore: non decidere sul rumore",
    subtitle: "Subito dopo la prova servono conservazione, memoria a caldo e fonti ufficiali.",
    description: "Procedura minima delle prime 24 ore dopo la prova, senza decisioni emotive.",
    svg: figurePrimeOre()
  },
  {
    slug: "03-tre-livelli-esito",
    title: "Tre livelli di esito",
    subtitle: "Impressione, atto ufficiale e conseguenza procedurale non sono la stessa cosa.",
    description: "Schema per distinguere percezione personale, esito ufficiale e passo procedurale.",
    svg: figureTreLivelli()
  },
  {
    slug: "04-cartella-dopo-prova",
    title: "Cartella dopo-prova",
    subtitle: "Ogni documento deve essere recuperabile quando serve una decisione.",
    description: "Archivio minimo di bando, ricevute, avvisi, esiti, graduatoria e schede personali.",
    svg: figureCartella()
  },
  {
    slug: "05-graduatoria-accesso-atti",
    title: "Graduatoria e accesso agli atti",
    subtitle: "Punteggi e parole procedurali vanno letti sugli atti, non sulle ipotesi.",
    description: "Mappa di prudenza documentale per punteggio, idoneita, graduatoria e accesso agli atti.",
    svg: figureGraduatoriaAccesso()
  },
  {
    slug: "06-scheda-diario-capitale",
    title: "Scheda, Diario e capitale",
    subtitle: "La prova diventa utile quando produce dati, errori corretti e materiali riusabili.",
    description: "Flusso dalla scheda post-prova al Diario degli errori e al capitale di studio.",
    svg: figureSchedaDiario()
  },
  {
    slug: "07-matrice-prossima-mossa",
    title: "Matrice della prossima mossa",
    subtitle: "Dopo l'esito scegli un passo coerente, non una reazione impulsiva.",
    description: "Matrice operativa per decidere tra fase successiva, monitoraggio, correzione e recupero.",
    svg: figureMatrice()
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

  return `# Asset Capitolo 30

Figure generate per \`Dopo la prova: esiti, graduatoria e prossima mossa\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const items = [
    ["B", "Bando", "esiti, soglie, avvisi", palette.navy, palette.blueSoft],
    ["A", "Aree", "forti, deboli, cedute", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "temi da riusare", palette.gold, palette.goldSoft],
    ["D", "Diario", "causa e azione", palette.green, palette.greenSoft],
    ["O", "Output", "prossima mossa", palette.teal, palette.tealSoft]
  ]
  const steps = items
    .map(([letter, title, body, color, fill], index) =>
      stepBox(105 + index * 290, 370, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 290, 485, 395 + index * 290, 485)).join("\n")

  return shell(
    "Mappa BANDO dopo la prova",
    "Chiudi il ciclo: fonti, diagnosi, Diario e prossima decisione.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(430, 215, 740, "Fase di conversione", ["dall'emozione ai dati", "dal risultato alla decisione"], palette.navy, palette.blueSoft)}
    ${steps}
    ${arrows}
    ${note(245, 810, 1110, "La prova finisce quando hai capito, archiviato e deciso il passo successivo.")}
    `
  )
}

function figurePrimeOre() {
  const cards = [
    ["Conserva", ["convocazione", "ricevute", "avvisi e codici"], palette.navy, palette.blueSoft],
    ["Scrivi", ["memoria a caldo", "domande ricordate", "tempo e difficolta"], palette.green, palette.greenSoft],
    ["Controlla", ["una fonte ufficiale", "bando e avvisi", "niente chat come prova"], palette.teal, palette.tealSoft]
  ]
  const rendered = cards.map((card, index) => listPanel(120 + index * 485, 300, 390, 315, card)).join("\n")

  return shell(
    "Prime 24 ore: non decidere sul rumore",
    "Subito dopo la prova servono conservazione, memoria a caldo e fonti ufficiali.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${rendered}
    ${arrow(510, 455, 605, 455)}
    ${arrow(995, 455, 1090, 455)}
    ${wideCard(485, 675, 630, "Decisioni pesanti", ["rimandale dopo l'atto ufficiale", "o dopo una lettura piu fredda"], palette.bordeaux, palette.redSoft)}
    ${note(245, 810, 1110, "Nelle prime ore il candidato registra dati; non riscrive tutto il metodo.")}
    `
  )
}

function figureTreLivelli() {
  const cards = [
    ["Impressione", ["sensazione personale", "memoria selettiva", "confronto con altri"], palette.bordeaux, palette.redSoft],
    ["Esito ufficiale", ["punteggio o elenco", "atto dell'ente", "bando e avvisi"], palette.navy, palette.blueSoft],
    ["Conseguenza", ["orale o titoli", "graduatoria", "archiviazione"], palette.green, palette.greenSoft]
  ]

  return shell(
    "Tre livelli di esito",
    "Impressione, atto ufficiale e conseguenza procedurale non sono la stessa cosa.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${cards.map((card, index) => listPanel(120 + index * 485, 285, 390, 355, card)).join("\n")}
    ${arrow(510, 465, 605, 465)}
    ${arrow(995, 465, 1090, 465)}
    ${wideCard(480, 675, 640, "Regola", ["prima identifichi il livello", "poi scegli l'azione corretta"], palette.gold, palette.goldSoft)}
    ${note(245, 810, 1110, "Un'impressione negativa non e' esclusione; un buon punteggio non e' automaticamente assunzione.")}
    `
  )
}

function figureCartella() {
  const left = [
    ["Bando", "2026-ente-profilo-bando.pdf"],
    ["Convocazione", "convocazione-scritto.pdf"],
    ["Ricevute", "invio-pagamento.pdf"],
    ["Avvisi", "diario-sede-istruzioni.pdf"]
  ]
  const right = [
    ["Esito", "esito-scritto.pdf"],
    ["Graduatoria", "graduatoria.pdf"],
    ["Scheda tua", "scheda-post-prova.md"],
    ["Diario", "errori-e-azioni.md"]
  ]

  return shell(
    "Cartella dopo-prova",
    "Ogni documento deve essere recuperabile quando serve una decisione.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${folderPanel(150, 240, "Fonti e prove", left, palette.navy, palette.blueSoft)}
    ${folderPanel(880, 240, "Esiti e lavoro tuo", right, palette.green, palette.greenSoft)}
    ${wideCard(520, 615, 560, "Nome file semplice", ["data, ente, profilo, tipo documento", "non screenshot sparsi nei download"], palette.teal, palette.tealSoft)}
    ${note(245, 810, 1110, "Il giorno in cui serve un documento non devi cercarlo tra messaggi e cartelle casuali.")}
    `
  )
}

function figureGraduatoriaAccesso() {
  const chips = [
    ["Punteggio", "soglie e criteri"],
    ["Idoneita", "non sempre vincitore"],
    ["Graduatoria", "ordine, titoli, riserve"],
    ["Scorrimento", "atti e decisioni"],
    ["Accesso atti", "canali e motivi concreti"]
  ]

  return shell(
    "Graduatoria e accesso agli atti",
    "Punteggi e parole procedurali vanno letti sugli atti, non sulle ipotesi.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(455, 220, 690, "Lettura prudente", ["non fare equivalenze automatiche", "rileggi bando, avvisi e atto pubblicato"], palette.navy, palette.blueSoft)}
    ${chips.map((chip, index) => chipBox(135 + index * 270, 405, chip, index)).join("\n")}
    ${wideCard(235, 650, 500, "Se il dubbio e' fondato", ["definisci quale atto vuoi vedere", "usa modalita e canali ufficiali"], palette.green, palette.greenSoft)}
    ${wideCard(865, 650, 500, "Se e' solo impulso", ["aspetta una lettura fredda", "non trasformare sfogo in procedura"], palette.bordeaux, palette.redSoft)}
    ${note(245, 810, 1110, "Per ricorsi, termini e scelte specifiche serve supporto qualificato.")}
    `
  )
}

function figureSchedaDiario() {
  const steps = [
    ["Scheda", ["dati prova", "materie forti", "punti deboli"], palette.navy, palette.blueSoft],
    ["Diario", ["errore", "causa", "una azione"], palette.bordeaux, palette.redSoft],
    ["Capitale", ["nuclei", "flashcard", "routine utile"], palette.green, palette.greenSoft]
  ]

  return shell(
    "Scheda, Diario e capitale",
    "La prova diventa utile quando produce dati, errori corretti e materiali riusabili.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${steps.map((step, index) => listPanel(120 + index * 485, 285, 390, 355, step)).join("\n")}
    ${arrow(510, 465, 605, 465)}
    ${arrow(995, 465, 1090, 465)}
    ${wideCard(470, 675, 660, "Regola di trasformazione", ["ogni errore produce una sola azione verificabile"], palette.gold, palette.goldSoft)}
    ${note(245, 810, 1110, "Il candidato metodico archivia la prova come capitale, non solo come bene o male.")}
    `
  )
}

function figureMatrice() {
  const rows = [
    ["Superata", "prepara fase successiva", palette.green, palette.greenSoft],
    ["Idoneita", "monitora atti ufficiali", palette.navy, palette.blueSoft],
    ["Negativa", "correggi lacune o metodo", palette.bordeaux, palette.redSoft],
    ["Dubbio", "valuta accesso documentale", palette.gold, palette.goldSoft],
    ["Nuovo bando", "trasferisci capitale", palette.teal, palette.tealSoft],
    ["Stanchezza", "recupero e revisione fredda", palette.violet, palette.violetSoft]
  ]

  return shell(
    "Matrice della prossima mossa",
    "Dopo l'esito scegli un passo coerente, non una reazione impulsiva.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${matrixRows(190, 230, rows)}
    ${sideRule(1030, 305, "Criterio", ["la mossa non deve", "essere eroica", "deve essere coerente"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "La prossima decisione nasce da situazione, atti disponibili, energia e capitale riusabile.")}
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
    .title { font: 800 43px Arial, sans-serif; fill: ${palette.ink}; }
    .subtitle { font: 400 21px Arial, sans-serif; fill: ${palette.muted}; }
    .label { font: 800 25px Arial, sans-serif; fill: ${palette.ink}; }
    .body { font: 400 19px Arial, sans-serif; fill: ${palette.ink}; }
    .small { font: 400 16px Arial, sans-serif; fill: ${palette.ink}; }
    .strong { font-weight: 800; }
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

function stepBox(x, y, letter, title, body, color, fill) {
  return `<g data-safe-box="${x} ${y} 245 210 8">
    <rect x="${x}" y="${y}" width="245" height="210" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 122.5}" cy="${y + 52}" r="32" fill="${color}"/>
    <text class="label whiteText" x="${x + 122.5}" y="${y + 61}" text-anchor="middle">${escapeXml(letter)}</text>
    <text class="label" x="${x + 122.5}" y="${y + 116}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 122.5}" y="${y + 158}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function listPanel(x, y, w, h, [title, items, color, fill]) {
  const lines = items
    .map((item, index) => `<text class="small" x="${x + w / 2}" y="${y + 130 + index * 42}" text-anchor="middle">${escapeXml(item)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="${w}" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + w / 2}" y="${y + 72}" text-anchor="middle">${escapeXml(title)}</text>
    ${lines}
  </g>`
}

function folderPanel(x, y, title, items, color, fill) {
  const rows = items
    .map(([label, name], index) => {
      const rowY = y + 94 + index * 66
      return `<g data-safe-box="${x + 35} ${rowY} 580 48 4">
        <rect x="${x + 35}" y="${rowY}" width="580" height="48" rx="14" fill="${palette.white}" stroke="${palette.border}" stroke-width="2"/>
        <text class="small strong" x="${x + 130}" y="${rowY + 31}" text-anchor="middle">${escapeXml(label)}</text>
        <text class="small" x="${x + 380}" y="${rowY + 31}" text-anchor="middle">${escapeXml(name)}</text>
      </g>`
    })
    .join("\n")

  return `<g data-safe-box="${x} ${y} 650 350 8">
    <rect x="${x}" y="${y}" width="650" height="350" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="650" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 325}" y="${y + 58}" text-anchor="middle">${escapeXml(title)}</text>
    ${rows}
  </g>`
}

function chipBox(x, y, [title, body], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.green, palette.greenSoft],
    [palette.gold, palette.goldSoft],
    [palette.teal, palette.tealSoft],
    [palette.bordeaux, palette.redSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 250 165 8">
    <rect x="${x}" y="${y}" width="250" height="165" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 125}" y="${y + 58}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 125}" y="${y + 108}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function matrixRows(x, y, rows) {
  return rows
    .map(([situation, action, color, fill], index) => {
      const rowY = y + index * 88
      return `<g data-safe-box="${x} ${rowY} 760 70 6">
        <rect x="${x}" y="${rowY}" width="760" height="70" rx="20" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <circle cx="${x + 44}" cy="${rowY + 35}" r="20" fill="${color}"/>
        <text class="small strong" style="fill:${color}" x="${x + 170}" y="${rowY + 43}" text-anchor="middle">${escapeXml(situation)}</text>
        <text class="small" x="${x + 500}" y="${rowY + 43}" text-anchor="middle">${escapeXml(action)}</text>
      </g>`
    })
    .join("\n")
}

function sideRule(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 190}" y="${y + 100 + index * 32}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 380 250 8">
    <rect x="${x}" y="${y}" width="380" height="250" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 190}" y="${y + 56}" text-anchor="middle">${escapeXml(title)}</text>
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
