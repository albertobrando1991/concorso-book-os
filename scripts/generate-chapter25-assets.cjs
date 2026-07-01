const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-25"
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
    slug: "01-mappa-bando-aggiornamento",
    title: "Mappa BANDO dell'aggiornamento",
    subtitle: "Una novita conta solo se cambia bando, materia, diario o output.",
    svg: figureMappaBando()
  },
  {
    slug: "02-gerarchia-fonti",
    title: "Gerarchia delle fonti",
    subtitle: "Quando le informazioni divergono, decide la fonte piu vicina alla procedura.",
    svg: figureGerarchia()
  },
  {
    slug: "03-fonti-da-controllare",
    title: "Fonti da controllare davvero",
    subtitle: "Ogni fonte ha una funzione: cercare, verificare, interpretare o aggiornare.",
    svg: figureFonti()
  },
  {
    slug: "04-protocollo-venti-minuti",
    title: "Protocollo dei 20 minuti",
    subtitle: "Un controllo breve chiude il ciclo: fonte, impatto, decisione e data.",
    svg: figureProtocollo()
  },
  {
    slug: "05-scheda-aggiornamento",
    title: "Scheda aggiornamento",
    subtitle: "Ogni cambiamento utile deve diventare una decisione entro 48 ore.",
    svg: figureScheda()
  },
  {
    slug: "06-cambiare-o-non-cambiare-piano",
    title: "Cambiare o non cambiare il piano",
    subtitle: "Il calendario cambia solo quando l'informazione modifica un'azione.",
    svg: figureDecisione()
  },
  {
    slug: "07-caso-davide-rumore-fonte-decisione",
    title: "Caso Davide: dal rumore alla decisione",
    subtitle: "Una voce non ufficiale diventa utile solo dopo verifica e impatto BANDO.",
    svg: figureDavide()
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
  return `# Asset Capitolo 25

Figure generate per \`Aggiornare il metodo dopo il libro\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-aggiornamento.png\` | Mappa BANDO applicata agli aggiornamenti. |
| \`02-gerarchia-fonti.png\` | Gerarchia delle fonti ufficiali e di supporto. |
| \`03-fonti-da-controllare.png\` | Fonti da controllare e funzione operativa di ciascuna. |
| \`04-protocollo-venti-minuti.png\` | Sequenza settimanale del protocollo dei 20 minuti. |
| \`05-scheda-aggiornamento.png\` | Scheda per trasformare un aggiornamento in decisione. |
| \`06-cambiare-o-non-cambiare-piano.png\` | Griglia decisionale per modificare o non modificare il piano. |
| \`07-caso-davide-rumore-fonte-decisione.png\` | Caso Davide: da voce non ufficiale a decisione BANDO. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${wideCard(500, 205, 600, "Aggiornamento utile", ["non notizia nuova", "ma decisione nuova"], "navy", "softBlue")}
  <path class="line" d="M800 332 L800 388"/>
  <path class="line" d="M210 388 L1390 388"/>
  ${connector(210, 388, 210, 462)}
  ${connector(505, 388, 505, 575)}
  ${connector(800, 388, 800, 462)}
  ${connector(1095, 388, 1095, 575)}
  ${connector(1390, 388, 1390, 462)}
  ${stepBox(80, 462, 260, "Bando", ["avvisi", "date", "prove"], "navy", "softBlue")}
  ${stepBox(375, 575, 260, "Aree", ["core", "moduli"], "bordeaux", "softRed")}
  ${stepBox(670, 462, 260, "Nuclei", ["alta resa", "fondamento"], "gold", "softGold")}
  ${stepBox(965, 575, 260, "Diario", ["fonte", "decisione"], "green", "softGreen")}
  ${stepBox(1260, 462, 260, "Output", ["quiz", "caso", "orale"], "teal", "softTeal")}
  ${note(250, 812, 1100, "Se non cambia un'azione, non deve far saltare il calendario.")}`

  return shell(
    "Mappa BANDO dell'aggiornamento",
    "Una novita conta solo se cambia bando, materia, diario o output.",
    inner
  )
}

function figureGerarchia() {
  const levels = [
    ["1", "Bando e avvisi", "requisiti, scadenze, prove", "navy", "softBlue"],
    ["2", "inPA e sito ente", "candidature e comunicazioni", "bordeaux", "softRed"],
    ["3", "Gazzetta Ufficiale", "pubblicazioni e avvisi", "gold", "softGold"],
    ["4", "Normattiva", "testo vigente", "green", "softGreen"],
    ["5", "Autorita settore", "ANAC, AgID, Garante, DFP", "teal", "softTeal"],
    ["6", "Manuali e gruppi", "spiegazione, mai comando", "navy", "softBlue"]
  ]

  const rows = levels.map((row, index) => hierarchyRow(190, 230 + index * 92, 1220, row, index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="215" text-anchor="middle">La domanda non e' cosa mi piace, ma quale fonte comanda</text>
  <g data-safe-box="190 230 1220 552 8">
    ${rows}
  </g>
  ${note(250, 812, 1100, "Il piano parte dal bando; le fonti di supporto spiegano, non sostituiscono.")}`

  return shell(
    "Gerarchia delle fonti",
    "Quando le informazioni divergono, decide la fonte piu vicina alla procedura.",
    inner
  )
}

function figureFonti() {
  const cards = [
    ["inPA", "bandi e candidature", "navy", "softBlue"],
    ["Sito ente", "diario prove e avvisi", "bordeaux", "softRed"],
    ["Gazzetta", "pubblicazioni ufficiali", "gold", "softGold"],
    ["Normattiva", "norma vigente", "green", "softGreen"],
    ["DFP / SNA", "competenze PA", "teal", "softTeal"],
    ["ANAC AgID Garante", "settori specifici", "navy", "softBlue"]
  ]

  const body = cards
    .map(([title, text, color, box], index) => {
      const col = index % 3
      const row = Math.floor(index / 3)
      return sourceCard(155 + col * 450, 270 + row * 245, title, text, color, box)
    })
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Non controllare tutto: controlla la fonte giusta per la domanda giusta</text>
  ${body}
  ${note(250, 812, 1100, "La fonte serve solo se cambia il modo in cui studi, rispondi o ti presenti alla prova.")}`

  return shell(
    "Fonti da controllare davvero",
    "Ogni fonte ha una funzione: cercare, verificare, interpretare o aggiornare.",
    inner
  )
}

function figureProtocollo() {
  const steps = [
    ["0-4", "inPA", "procedura e avvisi", "navy", "softBlue"],
    ["4-8", "Sito ente", "diario e sede", "bordeaux", "softRed"],
    ["8-11", "Bando", "allegati e regole", "gold", "softGold"],
    ["11-15", "Fonte mirata", "norma o settore", "green", "softGreen"],
    ["15-18", "Decoder", "cosa cambia", "teal", "softTeal"],
    ["18-20", "Diario", "decisione e data", "navy", "softBlue"]
  ]

  const top = steps
    .slice(0, 3)
    .map(([time, title, body, color, box], index) => timeCard(155 + index * 450, 275, time, title, body, color, box))
    .join("\n")
  const bottom = steps
    .slice(3)
    .map(([time, title, body, color, box], index) => timeCard(1055 - index * 450, 535, time, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Il controllo settimanale evita dieci ricontrolli mentali</text>
  ${top}
  <path class="arrowNavy" d="M505 390 L585 390"/>
  <path class="arrowNavy" d="M955 390 L1035 390"/>
  <path class="arrowNavy" d="M1225 480 L1225 520"/>
  ${bottom}
  <path class="arrowNavy" d="M1035 650 L955 650"/>
  <path class="arrowNavy" d="M585 650 L505 650"/>
  ${note(250, 812, 1100, "Se non trovi cambiamenti operativi, scrivi: nessun cambio operativo, proseguo piano.")}`

  return shell(
    "Protocollo dei 20 minuti",
    "Un controllo breve chiude il ciclo: fonte, impatto, decisione e data.",
    inner
  )
}

function figureScheda() {
  const rows = [
    ["Data", "giorno del controllo"],
    ["Fonte", "bando, inPA, ente, norma"],
    ["Cambio", "sintesi in una riga"],
    ["Area BANDO", "bando, aree, nuclei, diario, output"],
    ["Impatto", "scadenza, prova, materia, documento"],
    ["Decisione", "cosa fai entro 48 ore"],
    ["Prossimo", "data del nuovo controllo"]
  ]

  const body = rows.map((row, index) => sheetRow(170, 250 + index * 66, 1260, row, index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Non salvare messaggi a caso: chiudi il ciclo in una scheda</text>
  <g data-safe-box="170 250 1260 462 8">
    ${body}
  </g>
  ${note(250, 765, 1100, "La scheda costringe a passare da sapere a decidere.")}`

  return shell(
    "Scheda aggiornamento",
    "Ogni cambiamento utile deve diventare una decisione entro 48 ore.",
    inner
  )
}

function figureDecisione() {
  const yes = [
    ["Nuova data prova", "ricalcola calendario"],
    ["Rettifica materie", "aggiorna matrice"],
    ["Cambio formato", "modifica output"],
    ["Documento richiesto", "verifica domanda"]
  ]
  const no = [
    ["Articolo generico", "solo spiegazione"],
    ["Discussione gruppo", "verifica prima"],
    ["Corso aggiunge lezione", "non cambia bando"],
    ["Norma interessante", "attesa se irrilevante"]
  ]

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">La domanda decisiva: cambia un'azione gia pianificata?</text>
  ${decisionPanel(145, 300, 590, "Cambia il piano", yes, "green", "softGreen")}
  ${decisionPanel(865, 300, 590, "Non cambia il piano", no, "bordeaux", "softRed")}
  <path class="arrowNavy" d="M755 500 L845 500"/>
  ${mini(320, 690, 330, "Si", "aggiorna calendario o output", palette.green)}
  ${mini(930, 690, 330, "No", "scrivi e torna al piano", palette.bordeaux)}
  ${note(250, 812, 1100, "Una novita ufficiale puo essere importante in generale ma irrilevante per il tuo concorso.")}`

  return shell(
    "Cambiare o non cambiare il piano",
    "Il calendario cambia solo quando l'informazione modifica un'azione.",
    inner
  )
}

function figureDavide() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Privacy nel gruppo: Davide verifica prima di aprire un modulo avanzato</text>
  ${caseBox(120, 305, 320, "Rumore", ["voce in gruppo", "piu privacy"], "bordeaux", "softRed")}
  <path class="arrowNavy" d="M455 405 L535 405"/>
  ${caseBox(560, 305, 320, "Fonti", ["bando", "sito ente", "nucleo comune"], "navy", "softBlue")}
  <path class="arrowNavy" d="M895 405 L975 405"/>
  ${caseBox(1000, 305, 360, "Impatto", ["privacy essenziale", "nessuna rettifica", "nessun manuale nuovo"], "gold", "softGold")}
  ${caseBox(330, 560, 360, "Decisione", ["bilanciamento", "2 casi pratici", "simulazione mantenuta"], "green", "softGreen")}
  <path class="arrowNavy" d="M1180 500 L710 560"/>
  ${caseBox(820, 560, 360, "Diario", ["ansia da fonte", "non ufficiale", "prossimo controllo"], "teal", "softTeal")}
  <path class="arrowNavy" d="M700 650 L805 650"/>
  ${note(250, 812, 1100, "Davide non ignora la privacy: la studia al livello richiesto dal bando.")}`

  return shell(
    "Caso Davide: dal rumore alla decisione",
    "Una voce non ufficiale diventa utile solo dopo verifica e impatto BANDO.",
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
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 77 + index * 27}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 128 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="128" rx="25"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 44}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
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

function hierarchyRow(x, y, w, row, index) {
  const [level, title, body, colorClass, boxClass] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  return `<g data-safe-box="${x} ${y} ${w} 70 8">
    <rect x="${x}" y="${y}" width="${w}" height="70" rx="16" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <circle cx="${x + 52}" cy="${y + 35}" r="25" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 52}" y="${y + 44}" text-anchor="middle" fill="#FFFFFF" style="font-size:19px">${esc(level)}</text>
    <text class="${colorClass} label" x="${x + 250}" y="${y + 43}" text-anchor="middle" style="font-size:18px">${esc(title)}</text>
    <text class="muted small" x="${x + 760}" y="${y + 43}" text-anchor="middle" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function sourceCard(x, y, title, text, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 390 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="390" height="190" rx="24"/>
    <rect x="${x}" y="${y}" width="390" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 195}" y="${y + 58}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <path class="thin" d="M${x + 55} ${y + 82} L${x + 335} ${y + 82}"/>
    <text class="muted small" x="${x + 195}" y="${y + 128}" text-anchor="middle" style="font-size:17px">${esc(text)}</text>
  </g>`
}

function timeCard(x, y, time, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 335 170 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="335" height="170" rx="24"/>
    <circle cx="${x + 62}" cy="${y + 64}" r="34" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 62}" y="${y + 73}" text-anchor="middle" fill="#FFFFFF" style="font-size:18px">${esc(time)}</text>
    <text class="${colorClass} label" x="${x + 202}" y="${y + 58}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <text class="muted small" x="${x + 202}" y="${y + 106}" text-anchor="middle" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function sheetRow(x, y, w, row, index) {
  const [field, content] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  return `<g>
    <rect x="${x}" y="${y}" width="${w}" height="56" rx="12" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <rect x="${x}" y="${y}" width="245" height="56" rx="12" fill="${palette.navy}" opacity="0.96"/>
    <text class="label" x="${x + 122}" y="${y + 36}" text-anchor="middle" fill="#FFFFFF" style="font-size:17px">${esc(field)}</text>
    <text class="muted small" x="${x + 300}" y="${y + 36}" style="font-size:17px">${esc(content)}</text>
  </g>`
}

function decisionPanel(x, y, w, title, rows, colorClass, boxClass) {
  const body = rows
    .map(([label, value], index) => {
      const yy = y + 95 + index * 55
      return `<g>
        <text class="${colorClass} label" x="${x + 155}" y="${yy}" text-anchor="middle" style="font-size:16px">${esc(label)}</text>
        <text class="muted small" x="${x + 410}" y="${yy}" text-anchor="middle" style="font-size:16px">${esc(value)}</text>
      </g>`
    })
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 355 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="355" rx="26"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${body}
  </g>`
}

function caseBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 100 + index * 30}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 190 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="190" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <path class="thin" d="M${x + 45} ${y + 70} L${x + w - 45} ${y + 70}"/>
    ${rows}
  </g>`
}

function mini(x, y, w, title, body, color) {
  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:20px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:16px">${esc(body)}</text>
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
