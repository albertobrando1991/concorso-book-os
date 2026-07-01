const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-31"
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
    slug: "01-mappa-bando-presa-servizio",
    title: "Mappa BANDO della presa di servizio",
    subtitle: "Il metodo non finisce con la graduatoria: cambia output.",
    description: "Mappa BANDO per trasformare concorso, comunicazioni e primi giorni in comportamento professionale.",
    svg: figureMappaBando()
  },
  {
    slug: "02-dal-concorso-al-ruolo",
    title: "Dal concorso al ruolo",
    subtitle: "Graduatoria, chiamata, accettazione, documenti, contratto e presa di servizio sono passaggi diversi.",
    description: "Sequenza prudente dei passaggi dal risultato concorsuale all'ingresso operativo nell'ufficio.",
    svg: figureSequenzaRuolo()
  },
  {
    slug: "03-cartella-ingresso",
    title: "Cartella di ingresso",
    subtitle: "L'ordine documentale e' gia un comportamento professionale.",
    description: "Archivio minimo per comunicazioni, riscontri, documenti, sede, CCNL, codice e appunti di ingresso.",
    svg: figureCartellaIngresso()
  },
  {
    slug: "04-quattro-livelli-ruolo",
    title: "Quattro livelli del nuovo ruolo",
    subtitle: "Profilo, area, comparto e ufficio non dicono la stessa cosa.",
    description: "Schema per leggere profilo, area o famiglia professionale, comparto/CCNL e ufficio concreto.",
    svg: figureQuattroLivelli()
  },
  {
    slug: "05-codice-comportamento-bussola",
    title: "Codice di comportamento come bussola",
    subtitle: "Prima di agire chiediti se l'azione e' compatibile con servizio, imparzialita e fiducia.",
    description: "Bussola pratica per riservatezza, conflitti, uso strumenti, rapporti col pubblico e dubbio operativo.",
    svg: figureCodiceBussola()
  },
  {
    slug: "06-primi-30-giorni-pa",
    title: "Primi 30 giorni in PA",
    subtitle: "Il primo obiettivo non e' sembrare esperto: e' diventare affidabile.",
    description: "Timeline dei primi 30 giorni: orientamento, flussi, attivita controllate e autonomia progressiva.",
    svg: figurePrimiTrenta()
  },
  {
    slug: "07-capitale-studio-professionale",
    title: "Da capitale di studio a capitale professionale",
    subtitle: "Le nozioni diventano lavoro quando aiutano a leggere atti, dati, ruoli, rischi e risultati.",
    description: "Conversione del capitale di studio in competenze operative per l'ufficio pubblico.",
    svg: figureCapitaleProfessionale()
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

  return `# Asset Capitolo 31

Figure generate per \`Prendere servizio nella PA: dal concorso al ruolo\`.

| File | Funzione didattica |
|---|---|
${rows}

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const items = [
    ["B", "Bando", "profilo e comunicazioni", palette.navy, palette.blueSoft],
    ["A", "Aree", "area, comparto, ufficio", palette.bordeaux, palette.redSoft],
    ["N", "Nuclei", "doveri, dati, procedimenti", palette.gold, palette.goldSoft],
    ["D", "Diario", "dubbi e risposte verificate", palette.green, palette.greenSoft],
    ["O", "Output", "comportamento affidabile", palette.teal, palette.tealSoft]
  ]
  const steps = items
    .map(([letter, title, body, color, fill], index) =>
      stepBox(105 + index * 290, 370, letter, title, body, color, fill)
    )
    .join("\n")
  const arrows = [0, 1, 2, 3].map((index) => arrow(365 + index * 290, 485, 395 + index * 290, 485)).join("\n")

  return shell(
    "Mappa BANDO della presa di servizio",
    "Il metodo non finisce con la graduatoria: cambia output.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(430, 215, 740, "Dal candidato al dipendente", ["prima producevi risposte corrette", "ora produci comportamento professionale"], palette.navy, palette.blueSoft)}
    ${steps}
    ${arrows}
    ${note(245, 810, 1110, "La stessa catena usata per studiare serve per entrare in servizio con ordine.")}
    `
  )
}

function figureSequenzaRuolo() {
  const items = [
    ["Graduatoria", "ordine e posizione"],
    ["Chiamata", "atto o comunicazione"],
    ["Accettazione", "riscontro nei canali"],
    ["Documenti", "copie e ricevute"],
    ["Contratto", "riferimenti ufficiali"],
    ["Servizio", "sede, data, ufficio"]
  ]

  return shell(
    "Dal concorso al ruolo",
    "Graduatoria, chiamata, accettazione, documenti, contratto e presa di servizio sono passaggi diversi.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${items.map((item, index) => processStep(105 + index * 240, 355, item, index)).join("\n")}
    ${[0, 1, 2, 3, 4].map((index) => arrow(310 + index * 240, 455, 345 + index * 240, 455)).join("\n")}
    ${wideCard(420, 635, 760, "Domanda corretta", ["quale atto ufficiale mi dice il prossimo passo?", "entro quale termine e con quali documenti?"], palette.green, palette.greenSoft)}
    ${note(245, 810, 1110, "Non usare una parola sola per tutto: ogni passaggio ha fonte, scadenza e prova documentale.")}
    `
  )
}

function figureCartellaIngresso() {
  const left = [
    ["Bando", "bando e rettifiche"],
    ["Graduatoria", "esito utile"],
    ["Comunicazioni", "atto dell'ente"],
    ["Riscontro", "accettazione o risposta"]
  ]
  const right = [
    ["Documenti", "allegati richiesti"],
    ["Sede", "data, orario, referente"],
    ["Regole", "CCNL e codice"],
    ["Appunti", "diario ingresso"]
  ]

  return shell(
    "Cartella di ingresso",
    "L'ordine documentale e' gia un comportamento professionale.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${folderPanel(150, 240, "Fonti e riscontri", left, palette.navy, palette.blueSoft)}
    ${folderPanel(880, 240, "Ingresso operativo", right, palette.green, palette.greenSoft)}
    ${wideCard(520, 615, 560, "Nome file utile", ["data, ente, profilo, documento", "copie e ricevute sempre insieme"], palette.teal, palette.tealSoft)}
    ${note(245, 810, 1110, "Quando l'ente chiede un riscontro, non devi cercare tra posta, download e chat.")}
    `
  )
}

function figureQuattroLivelli() {
  const levels = [
    ["Profilo", ["ruolo selezionato"], palette.navy, palette.blueSoft],
    ["Area", ["competenza attesa", "responsabilita"], palette.green, palette.greenSoft],
    ["Comparto", ["CCNL da verificare"], palette.gold, palette.goldSoft],
    ["Ufficio", ["attivita concrete", "della struttura"], palette.teal, palette.tealSoft]
  ]

  return shell(
    "Quattro livelli del nuovo ruolo",
    "Profilo, area, comparto e ufficio non dicono la stessa cosa.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${levels.map((level, index) => levelCard(130 + index * 360, 285, level)).join("\n")}
    ${wideCard(455, 665, 690, "Verifica sempre", ["comunicazioni dell'ente", "CCNL applicabile, regolamenti e ufficio personale"], palette.bordeaux, palette.redSoft)}
    ${note(245, 810, 1110, "Il bando dice per cosa hai concorso; l'ufficio mostra il lavoro reale.")}
    `
  )
}

function figureCodiceBussola() {
  const items = [
    ["Riservatezza", "dati e pratiche"],
    ["Imparzialita", "conflitti e regali"],
    ["Strumenti", "email, PC, banche dati"],
    ["Pubblico", "correttezza e fiducia"],
    ["Dubbio", "chiedere prima di agire"]
  ]

  return shell(
    "Codice di comportamento come bussola",
    "Prima di agire chiediti se l'azione e' compatibile con servizio, imparzialita e fiducia.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${wideCard(430, 220, 740, "Domanda guida", ["questa azione e' compatibile con il servizio?", "protegge fiducia e imparzialita?"], palette.navy, palette.blueSoft)}
    ${items.map((item, index) => compassChip(135 + index * 270, 430, item, index)).join("\n")}
    ${wideCard(485, 660, 630, "Valore del neoassunto", ["non fare tutto subito", "evitare errori evitabili"], palette.green, palette.greenSoft)}
    ${note(245, 810, 1110, "Il criterio non e' se puoi tecnicamente farlo, ma se hai titolo e ragione di servizio.")}
    `
  )
}

function figurePrimiTrenta() {
  const blocks = [
    ["1-3", "orientamento", "sede, orari, strumenti"],
    ["4-10", "osservazione", "flussi, documenti, scadenze"],
    ["11-20", "prime attivita", "compiti controllati"],
    ["21-30", "autonomia", "checklist personale"]
  ]

  return shell(
    "Primi 30 giorni in PA",
    "Il primo obiettivo non e' sembrare esperto: e' diventare affidabile.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${blocks.map((block, index) => monthBlock(140 + index * 345, 315, block, index)).join("\n")}
    ${[0, 1, 2].map((index) => arrow(420 + index * 345, 455, 485 + index * 345, 455)).join("\n")}
    ${wideCard(455, 660, 690, "Affidabile significa", ["leggere prima di chiedere", "chiedere prima di improvvisare"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "La scheda ufficio trasforma ordini isolati in mappa dell'organizzazione.")}
    `
  )
}

function figureCapitaleProfessionale() {
  const rows = [
    ["Diritto amm.", "atti e procedimenti", palette.navy, palette.blueSoft],
    ["Pubblico impiego", "ruoli e doveri", palette.green, palette.greenSoft],
    ["Privacy e trasparenza", "dati e pubblicazioni", palette.gold, palette.goldSoft],
    ["PA digitale", "PEC, protocollo, firme", palette.teal, palette.tealSoft],
    ["Contratti e contabilita", "vincoli e responsabilita", palette.bordeaux, palette.redSoft]
  ]

  return shell(
    "Da capitale di studio a capitale professionale",
    "Le nozioni diventano lavoro quando aiutano a leggere atti, dati, ruoli, rischi e risultati.",
    `
    <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
    ${conversionRows(180, 245, rows)}
    ${sideRule(1040, 325, "Ogni procedura", ["quale fonte?", "chi e' responsabile?", "quale rischio evito?", "quale output produce?"], palette.navy, palette.blueSoft)}
    ${note(245, 810, 1110, "La logica dei casi pratici diventa metodo di lavoro dentro l'ufficio.")}
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

function processStep(x, y, [title, body], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.green, palette.greenSoft],
    [palette.gold, palette.goldSoft],
    [palette.teal, palette.tealSoft],
    [palette.bordeaux, palette.redSoft],
    [palette.violet, palette.violetSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 205 210 8">
    <rect x="${x}" y="${y}" width="205" height="210" rx="24" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 102.5}" cy="${y + 55}" r="30" fill="${color}"/>
    <text class="label whiteText" x="${x + 102.5}" y="${y + 64}" text-anchor="middle">${index + 1}</text>
    <text class="small strong" style="fill:${color}" x="${x + 102.5}" y="${y + 118}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small" x="${x + 102.5}" y="${y + 160}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function folderPanel(x, y, title, items, color, fill) {
  const rows = items
    .map(([label, name], index) => {
      const rowY = y + 94 + index * 66
      return `<g data-safe-box="${x + 35} ${rowY} 580 48 4">
        <rect x="${x + 35}" y="${rowY}" width="580" height="48" rx="14" fill="${palette.white}" stroke="${palette.border}" stroke-width="2"/>
        <text class="small strong" x="${x + 140}" y="${rowY + 31}" text-anchor="middle">${escapeXml(label)}</text>
        <text class="small" x="${x + 405}" y="${rowY + 31}" text-anchor="middle">${escapeXml(name)}</text>
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

function levelCard(x, y, [title, lines, color, fill]) {
  const renderedLines = lines
    .map((line, index) => `<text class="small strong" x="${x + 150}" y="${y + 176 + index * 38}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 300 345 8">
    <rect x="${x}" y="${y}" width="300" height="345" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <rect x="${x}" y="${y}" width="300" height="14" rx="7" fill="${color}"/>
    <text class="label" style="fill:${color}" x="${x + 150}" y="${y + 72}" text-anchor="middle">${escapeXml(title)}</text>
    <line x1="${x + 55}" y1="${y + 115}" x2="${x + 245}" y2="${y + 115}" stroke="${palette.border}" stroke-width="3"/>
    ${renderedLines}
  </g>`
}

function compassChip(x, y, [title, body], index) {
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

function monthBlock(x, y, [days, title, body], index) {
  const colors = [
    [palette.navy, palette.blueSoft],
    [palette.green, palette.greenSoft],
    [palette.gold, palette.goldSoft],
    [palette.teal, palette.tealSoft]
  ]
  const [color, fill] = colors[index % colors.length]

  return `<g data-safe-box="${x} ${y} 280 290 8">
    <rect x="${x}" y="${y}" width="280" height="290" rx="28" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <circle cx="${x + 140}" cy="${y + 62}" r="42" fill="${color}"/>
    <text class="label whiteText" x="${x + 140}" y="${y + 71}" text-anchor="middle">${escapeXml(days)}</text>
    <text class="label" style="fill:${color}" x="${x + 140}" y="${y + 142}" text-anchor="middle">${escapeXml(title)}</text>
    <text class="small strong" x="${x + 140}" y="${y + 205}" text-anchor="middle">${escapeXml(body)}</text>
  </g>`
}

function conversionRows(x, y, rows) {
  return rows
    .map(([source, target, color, fill], index) => {
      const rowY = y + index * 92
      return `<g data-safe-box="${x} ${rowY} 760 74 6">
        <rect x="${x}" y="${rowY}" width="760" height="74" rx="20" fill="${fill}" stroke="${color}" stroke-width="3"/>
        <text class="small strong" style="fill:${color}" x="${x + 180}" y="${rowY + 45}" text-anchor="middle">${escapeXml(source)}</text>
        <path class="line" marker-end="url(#arrow)" d="M${x + 310} ${rowY + 37} L${x + 410} ${rowY + 37}"/>
        <text class="small" x="${x + 580}" y="${rowY + 45}" text-anchor="middle">${escapeXml(target)}</text>
      </g>`
    })
    .join("\n")
}

function sideRule(x, y, title, lines, color, fill) {
  const rendered = lines
    .map((line, index) => `<text class="small" x="${x + 190}" y="${y + 88 + index * 32}" text-anchor="middle">${escapeXml(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 380 285 8">
    <rect x="${x}" y="${y}" width="380" height="285" rx="26" fill="${fill}" stroke="${color}" stroke-width="3"/>
    <text class="label" style="fill:${color}" x="${x + 190}" y="${y + 52}" text-anchor="middle">${escapeXml(title)}</text>
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
