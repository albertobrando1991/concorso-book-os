const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-20"
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
    slug: "01-mappa-bando-mappe-profilo",
    title: "Mappa BANDO delle mappe profilo",
    subtitle: "Dal profilo alla strategia: cosa resta comune, cosa cambia, cosa va allenato.",
    svg: figureMappaBando()
  },
  {
    slug: "02-core-modulo-prova-reale",
    title: "Formula core + modulo + prova reale",
    subtitle: "La preparazione resta continua, ma cambia peso in base al bando.",
    svg: figureCoreModulo()
  },
  {
    slug: "03-scheda-unica-profilo",
    title: "Scheda unica di mappa profilo",
    subtitle: "Una pagina per decidere priorita, rischio e prima azione di studio.",
    svg: figureScheda()
  },
  {
    slug: "04-profili-amministrativi-e-centrali",
    title: "Profili amministrativi e centrali",
    subtitle: "Le prime mappe distinguono base comune, ente e modulo giuridico-contabile.",
    svg: figureProfiliBase()
  },
  {
    slug: "05-profili-specialistici-e-servizi",
    title: "Profili specialistici e servizi",
    subtitle: "Quando il modulo pesa molto, il piano deve cambiare fin dal primo giorno.",
    svg: figureProfiliSpecialistici()
  },
  {
    slug: "06-semaforo-e-pesatura-tempo",
    title: "Semaforo e pesatura del tempo",
    subtitle: "Colori e percentuali impediscono di studiare in base alla sola abitudine.",
    svg: figureSemaforoTempo()
  },
  {
    slug: "07-caso-guidato-conversione-profilo",
    title: "Caso guidato: convertire una preparazione",
    subtitle: "Da istruttore amministrativo a funzionario tecnico senza buttare la base.",
    svg: figureCasoGuidato()
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
  return `# Asset Capitolo 20

Figure generate per \`Mappe profilo: cosa resta comune e cosa cambia\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-mappe-profilo.png\` | Mappa BANDO per trasformare profilo, aree, nuclei, diario e output in una strategia di studio. |
| \`02-core-modulo-prova-reale.png\` | Formula operativa nucleo comune + modulo profilo + prova reale. |
| \`03-scheda-unica-profilo.png\` | Scheda compilabile sintetica con core, modulo, prova, rischio e prima azione. |
| \`04-profili-amministrativi-e-centrali.png\` | Sintesi visuale delle mappe amministrative, contabili, enti locali, ministeri, giustizia e agenzie fiscali. |
| \`05-profili-specialistici-e-servizi.png\` | Sintesi visuale dei profili lavoro/previdenza, tecnici, ICT, polizia locale, sanita, scuola e appalti/fondi. |
| \`06-semaforo-e-pesatura-tempo.png\` | Griglia semaforo e distribuzione prudente del tempo tra core, modulo e output. |
| \`07-caso-guidato-conversione-profilo.png\` | Caso guidato di conversione da concorso amministrativo comunale a profilo tecnico. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${wideCard(510, 205, 580, "Mappa profilo", ["decide cosa riusare", "e cosa cambiare"], "navy", "softBlue")}
  <path class="line" d="M800 332 L800 388"/>
  <path class="line" d="M210 388 L1390 388"/>
  ${connector(210, 388, 210, 462)}
  ${connector(505, 388, 505, 575)}
  ${connector(800, 388, 800, 462)}
  ${connector(1095, 388, 1095, 575)}
  ${connector(1390, 388, 1390, 462)}
  ${stepBox(80, 462, 260, "Bando", ["profilo", "prove", "peso"], "navy", "softBlue")}
  ${stepBox(375, 575, 260, "Aree", ["core", "modulo", "eventuali"], "bordeaux", "softRed")}
  ${stepBox(670, 462, 260, "Nuclei", ["alto rendimento", "materia killer"], "gold", "softGold")}
  ${stepBox(965, 575, 260, "Diario", ["ore", "errori", "rinvii"], "green", "softGreen")}
  ${stepBox(1260, 462, 260, "Output", ["quiz", "caso", "orale"], "teal", "softTeal")}
  ${note(250, 812, 1100, "La mappa profilo non prevede tutto: riduce le decisioni sbagliate.")}`

  return shell(
    "Mappa BANDO delle mappe profilo",
    "Dal profilo alla strategia: cosa resta comune, cosa cambia, cosa va allenato.",
    inner
  )
}

function figureCoreModulo() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${formulaBox(130, 275, 360, "Nucleo comune", ["amministrativo", "pubblico impiego", "trasparenza e privacy", "digitale, inglese", "metodo di prova"], "navy", "softBlue")}
  ${plus(520, 450)}
  ${formulaBox(620, 275, 360, "Modulo profilo", ["enti locali", "contabilita", "tributario", "tecnico, ICT", "sanita, scuola"], "bordeaux", "softRed")}
  ${plus(1010, 450)}
  ${formulaBox(1110, 275, 360, "Prova reale", ["quiz a tempo", "risposta breve", "caso pratico", "orale", "prova pratica"], "green", "softGreen")}
  <path class="arrowNavy" d="M800 650 L800 705"/>
  ${wideCard(455, 705, 690, "Preparazione utile", ["continuita senza rigidita", "adattamento senza ripartenza da zero"], "gold", "softGold")}`

  return shell(
    "Formula core + modulo + prova reale",
    "La preparazione resta continua, ma cambia peso in base al bando.",
    inner
  )
}

function figureScheda() {
  const rows = [
    ["Profilo", "titolo, mansioni, amministrazione"],
    ["Famiglia", "area concorsuale operativa"],
    ["Core", "materie riutilizzabili"],
    ["Modulo", "materie che distinguono il profilo"],
    ["Prove", "formato, tempo, soglia, penalita"],
    ["Rischio", "punto in cui si perde punteggio"],
    ["Prima cosa", "sessione da fare subito"]
  ]
  const body = rows.map((row, index) => tableRow(200, 260 + index * 62, 1200, row[0], row[1], index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Compila la scheda prima di aprire nuovi materiali</text>
  <g data-safe-box="200 260 1200 434 8">
    ${body}
  </g>
  ${mini(235, 725, 320, "Decisione", "cosa studio oggi", palette.navy)}
  ${mini(640, 725, 320, "Rinvio", "cosa taglio o posticipo", palette.bordeaux)}
  ${mini(1045, 725, 320, "Output", "cosa produco entro 7 giorni", palette.green)}`

  return shell(
    "Scheda unica di mappa profilo",
    "Una pagina per decidere priorita, rischio e prima azione di studio.",
    inner
  )
}

function figureProfiliBase() {
  const profiles = [
    ["Amm. generale", "core forte", "rischio: genericita", "navy", "softBlue"],
    ["Amm.-contabile", "bilancio + atti", "rischio: rinvio contabile", "bordeaux", "softRed"],
    ["Enti locali", "organi + competenze", "rischio: ruoli confusi", "gold", "softGold"],
    ["Ministeri", "Stato + funzione", "rischio: ente ignorato", "green", "softGreen"],
    ["Giustizia", "ufficio + procedura", "rischio: peso sbagliato", "teal", "softTeal"],
    ["Agenzie fiscali", "tributario o catasto", "rischio: modulo killer", "navy", "softBlue"]
  ]
  const cells = profiles
    .map(([title, focus, risk, color, box], index) =>
      profileCell(115 + (index % 3) * 485, 255 + Math.floor(index / 3) * 235, title, focus, risk, color, box)
    )
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Prime schede: cambia il contesto, non sparisce il nucleo comune</text>
  ${cells}
  ${note(250, 812, 1100, "Qui la priorita e' bilanciare base amministrativa, amministrazione specifica e prova.")}`

  return shell(
    "Profili amministrativi e centrali",
    "Le prime mappe distinguono base comune, ente e modulo giuridico-contabile.",
    inner
  )
}

function figureProfiliSpecialistici() {
  const profiles = [
    ["Lavoro e previdenza", "glossario specialistico", "modulo presto", "bordeaux", "softRed"],
    ["Tecnico PA", "disciplina + procedimento", "casi e atti", "green", "softGreen"],
    ["ICT e digitale", "sistemi, dati, sicurezza", "PA digitale", "teal", "softTeal"],
    ["Polizia locale", "codice strada + casi", "non concorso generico", "navy", "softBlue"],
    ["Sanita amm.", "privacy + servizio", "dati e utenza", "gold", "softGold"],
    ["Scuola e universita", "segreterie + ordinamento", "processi reali", "bordeaux", "softRed"],
    ["Appalti e fondi", "ciclo progetto-controllo", "rendicontazione", "green", "softGreen"]
  ]
  const firstSix = profiles
    .slice(0, 6)
    .map(([title, focus, risk, color, box], index) =>
      compactProfile(115 + (index % 3) * 485, 245 + Math.floor(index / 3) * 202, title, focus, risk, color, box)
    )
    .join("\n")
  const [title, focus, risk, color, box] = profiles[6]
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="220" text-anchor="middle">Nei profili verticali il modulo puo decidere la graduatoria</text>
  ${firstSix}
  ${wideProfile(390, 660, 820, title, focus, risk, color, box)}
  ${note(250, 812, 1100, "Se il modulo e' rosso, va avviato in parallelo al core: non negli ultimi giorni.")}`

  return shell(
    "Profili specialistici e servizi",
    "Quando il modulo pesa molto, il piano deve cambiare fin dal primo giorno.",
    inner
  )
}

function figureSemaforoTempo() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="445" y="235" text-anchor="middle">Griglia semaforo</text>
  ${trafficRow(145, 285, palette.green, "Verde", "gia studiata", "ripasso e quiz")}
  ${trafficRow(145, 380, palette.gold, "Giallo", "da adattare", "collegamenti e casi")}
  ${trafficRow(145, 475, palette.bordeaux, "Rosso", "nuova o killer", "blocchi dedicati")}
  ${trafficRow(145, 570, palette.line, "Grigio", "marginale", "studio minimo")}
  <path class="thin" d="M795 255 L795 680"/>
  <text class="navy label" x="1160" y="235" text-anchor="middle">Pesatura prudente</text>
  ${bar(910, 305, 500, 44, 0.55, "Profilo amm. generale", "55 / 20 / 25")}
  ${bar(910, 385, 500, 44, 0.40, "Amm.-contabile", "40 / 35 / 25")}
  ${bar(910, 465, 500, 44, 0.30, "Specialistico", "30 / 45 / 25")}
  ${bar(910, 545, 500, 44, 0.30, "Prova pratica", "30 / 35 / 35")}
  ${legend(930, 640)}
  ${note(250, 812, 1100, "Il rosso non va lasciato alla fine; il grigio non deve rubare tempo al rosso.")}`

  return shell(
    "Semaforo e pesatura del tempo",
    "Colori e percentuali impediscono di studiare in base alla sola abitudine.",
    inner
  )
}

function figureCasoGuidato() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${caseColumn(115, 270, "Base gia pronta", ["amministrativo", "pubblico impiego", "trasparenza", "privacy"], "navy", "softBlue")}
  ${caseColumn(605, 270, "Da convertire", ["contratti pubblici", "procedimento tecnico", "responsabilita", "linguaggio dell'ente"], "gold", "softGold")}
  ${caseColumn(1095, 270, "Nuovo rosso", ["urbanistica", "edilizia", "lavori pubblici", "casi tecnico-pratici"], "bordeaux", "softRed")}
  <path class="arrowNavy" d="M505 445 L590 445"/>
  <path class="arrowGold" d="M995 445 L1080 445"/>
  ${wideCard(355, 672, 890, "Decisione corretta", ["la base non si butta: si mantiene in verde", "il modulo tecnico entra subito nel calendario"], "green", "softGreen")}`

  return shell(
    "Caso guidato: convertire una preparazione",
    "Da istruttore amministrativo a funzionario tecnico senza buttare la base.",
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
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.navy}"/></marker>
    <marker id="arrowGold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.gold}"/></marker>
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

  return `<g data-safe-box="${x} ${y} ${w} 142 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="142" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    ${rows}
  </g>`
}

function formulaBox(x, y, w, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 112 + index * 43}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 350 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="350" rx="28"/>
    <rect x="${x}" y="${y}" width="${w}" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 55}" text-anchor="middle" style="font-size:24px">${esc(title)}</text>
    <path class="thin" d="M${x + 38} ${y + 78} L${x + w - 38} ${y + 78}"/>
    ${rows}
  </g>`
}

function tableRow(x, y, w, left, right, index) {
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  return `<g>
    <rect x="${x}" y="${y}" width="${w}" height="54" rx="12" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <text class="navy label" x="${x + 36}" y="${y + 36}" style="font-size:19px">${esc(left)}</text>
    <text class="muted small" x="${x + 350}" y="${y + 36}" style="font-size:18px">${esc(right)}</text>
  </g>`
}

function profileCell(x, y, title, focus, risk, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 405 170 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="405" height="170" rx="24"/>
    <rect x="${x}" y="${y}" width="405" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 202.5}" y="${y + 45}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    <path class="thin" d="M${x + 35} ${y + 66} L${x + 370} ${y + 66}"/>
    <text class="muted small" x="${x + 202.5}" y="${y + 104}" text-anchor="middle" style="font-size:17px">${esc(focus)}</text>
    <text class="muted small" x="${x + 202.5}" y="${y + 137}" text-anchor="middle" style="font-size:16px">${esc(risk)}</text>
  </g>`
}

function compactProfile(x, y, title, focus, risk, colorClass, boxClass) {
  const titleSize = title.length > 18 ? 18 : 20
  return `<g data-safe-box="${x} ${y} 405 146 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="405" height="146" rx="22"/>
    <rect x="${x}" y="${y}" width="405" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 202.5}" y="${y + 42}" text-anchor="middle" style="font-size:${titleSize}px">${esc(title)}</text>
    <text class="muted small" x="${x + 202.5}" y="${y + 84}" text-anchor="middle" style="font-size:16px">${esc(focus)}</text>
    <text class="muted small" x="${x + 202.5}" y="${y + 116}" text-anchor="middle" style="font-size:15px">${esc(risk)}</text>
  </g>`
}

function wideProfile(x, y, w, title, focus, risk, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} ${w} 92 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="92" rx="24"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 165}" y="${y + 57}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    <text class="muted small" x="${x + 480}" y="${y + 57}" text-anchor="middle" style="font-size:17px">${esc(focus)}</text>
    <text class="muted small" x="${x + 690}" y="${y + 57}" text-anchor="middle" style="font-size:16px">${esc(risk)}</text>
  </g>`
}

function trafficRow(x, y, color, title, meaning, action) {
  return `<g data-safe-box="${x} ${y} 600 70 8">
    <rect class="card" x="${x}" y="${y}" width="600" height="70" rx="20"/>
    <circle cx="${x + 45}" cy="${y + 35}" r="18" fill="${color}"/>
    <text class="navy label" x="${x + 90}" y="${y + 43}" style="font-size:20px">${esc(title)}</text>
    <text class="muted small" x="${x + 245}" y="${y + 43}" style="font-size:17px">${esc(meaning)}</text>
    <text class="muted small" x="${x + 425}" y="${y + 43}" style="font-size:17px">${esc(action)}</text>
  </g>`
}

function bar(x, y, w, h, firstShare, label, values) {
  const coreW = Math.round(w * firstShare)
  const moduleW = Math.round(w * 0.28)
  const outputW = w - coreW - moduleW
  return `<g data-safe-box="${x - 95} ${y - 28} ${w + 215} ${h + 40} 4">
    <text class="muted small" x="${x}" y="${y - 9}" style="font-size:15px">${esc(label)}</text>
    <rect x="${x}" y="${y}" width="${coreW}" height="${h}" rx="12" fill="${palette.navy}"/>
    <rect x="${x + coreW}" y="${y}" width="${moduleW}" height="${h}" fill="${palette.bordeaux}"/>
    <rect x="${x + coreW + moduleW}" y="${y}" width="${outputW}" height="${h}" rx="12" fill="${palette.green}"/>
    <text class="small" x="${x + w + 22}" y="${y + 29}" fill="${palette.ink}" style="font-size:15px">${esc(values)}</text>
  </g>`
}

function legend(x, y) {
  return `<g data-safe-box="${x} ${y - 8} 460 50 4">
    <rect x="${x}" y="${y}" width="20" height="20" rx="5" fill="${palette.navy}"/>
    <text class="muted small" x="${x + 30}" y="${y + 17}" style="font-size:15px">core</text>
    <rect x="${x + 120}" y="${y}" width="20" height="20" rx="5" fill="${palette.bordeaux}"/>
    <text class="muted small" x="${x + 150}" y="${y + 17}" style="font-size:15px">modulo</text>
    <rect x="${x + 260}" y="${y}" width="20" height="20" rx="5" fill="${palette.green}"/>
    <text class="muted small" x="${x + 290}" y="${y + 17}" style="font-size:15px">output</text>
  </g>`
}

function caseColumn(x, y, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + 172.5}" y="${y + 112 + index * 42}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 345 330 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="345" height="330" rx="26"/>
    <rect x="${x}" y="${y}" width="345" height="11" rx="5.5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 172.5}" y="${y + 55}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    <path class="thin" d="M${x + 35} ${y + 78} L${x + 310} ${y + 78}"/>
    ${rows}
  </g>`
}

function plus(x, y) {
  return `<g data-safe-box="${x - 35} ${y - 35} 70 70 2">
    <circle cx="${x}" cy="${y}" r="34" fill="${palette.gold}"/>
    <text class="label" x="${x}" y="${y + 10}" text-anchor="middle" fill="#FFFFFF" style="font-size:34px">+</text>
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 17 ? 17 : 20
  const bodyFontSize = body.length > 30 ? 14 : 16
  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 108 ? 18 : text.length > 90 ? 19 : 20
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
