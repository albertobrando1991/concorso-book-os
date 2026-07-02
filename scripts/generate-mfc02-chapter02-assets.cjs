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
  "chapter-02"
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
    slug: "01-mappa-bando-decoder-fiscale",
    title: "Mappa BANDO del Decoder fiscale",
    subtitle: "Dal bando AE, ADM o AdER alla scheda operativa: famiglia, priorita, diario e output.",
    svg: figureMappaBando()
  },
  {
    slug: "02-codice-profilo-famiglia",
    title: "Dal codice profilo alla famiglia M-FC02",
    subtitle: "Ente, sigla e programma vanno letti insieme prima di scegliere materiali e moduli.",
    svg: figureCodiceProfilo()
  },
  {
    slug: "03-prove-output-decoder",
    title: "Prove e output del Decoder fiscale",
    subtitle: "La forma della prova decide se allenare quiz, risposte, casi, orale o checklist.",
    svg: figureProveOutput()
  },
  {
    slug: "04-priorita-studio-fiscale",
    title: "Priorita di studio nel bando fiscale",
    subtitle: "Studio subito, studio dopo, verifico sul bando o rinvio ad altro modulo.",
    svg: figurePriorita()
  },
  {
    slug: "05-caso-tre-decoder-fiscali",
    title: "Caso guidato: tre Decoder fiscali",
    subtitle: "Tre bandi fiscali richiedono tre letture diverse: AE, ADM e AdER.",
    svg: figureCaso()
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
  return `# Asset Capitolo 2 - M-FC02 Bando Decoder fiscale

Figure generate per \`Bando Decoder fiscale\`.

## Analisi stile libro base

Le immagini del libro base usano una grammatica editoriale stabile:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview/PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- font sans serif, titoli brevi, testo interno essenziale e nessuna decorazione fine a se stessa;
- funzioni ricorrenti: mappa BANDO, confronto errore/correzione, matrice decisionale, sequenza operativa, scheda workbook, caso guidato;
- inserimento dopo il blocco testuale che introduce la decisione, non a fine capitolo come ornamento.

Per questo capitolo sono opportune 5 figure: lo stesso numero del capitolo 2 del libro base, con taglio specialistico fiscale.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-decoder-fiscale.png\` | \`01-mappa-bando-decoder-fiscale.svg\` | Mappa BANDO del Decoder fiscale: bando, aree, nuclei, diario e output. |
| \`02-codice-profilo-famiglia.png\` | \`02-codice-profilo-famiglia.svg\` | Lettura di ente, codice profilo, programma e famiglia M-FC02. |
| \`03-prove-output-decoder.png\` | \`03-prove-output-decoder.svg\` | Collegamento tra prova prevista e output di allenamento. |
| \`04-priorita-studio-fiscale.png\` | \`04-priorita-studio-fiscale.svg\` | Griglia studio subito/studio dopo/verifico/rinvio. |
| \`05-caso-tre-decoder-fiscali.png\` | \`05-caso-tre-decoder-fiscali.svg\` | Caso guidato con tre bandi: AE, ADM e AdER. |
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
      .softTeal { fill: ${palette.tealSoft}; stroke: #A3D5D8; stroke-width: 2.5; }
      .note { fill: ${palette.cream}; stroke: #E7C18E; stroke-width: 2.5; }
      .ink { fill: ${palette.ink}; font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; }
      .muted { fill: ${palette.muted}; font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; }
      .title { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 43px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 22px; }
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
      .dash { stroke: ${palette.line}; stroke-width: 3.5; stroke-linecap: round; stroke-dasharray: 9 10; fill: none; }
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
  <text class="ink title" x="800" y="68" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="108" text-anchor="middle">${esc(subtitle)}</text>
${inner}
</svg>
`
}

function figureMappaBando() {
  const inner = `
  ${card(575, 162, 450, 120, "Bando fiscale", ["AE, ADM o AdER", "profilo e prove"], "navy", "card")}
  <path class="line" d="M800 282 L800 348"/>
  <path class="line" d="M210 348 L1390 348"/>
  ${connector(210, 348, 210, 440)}
  ${connector(505, 348, 505, 565)}
  ${connector(800, 348, 800, 440)}
  ${connector(1095, 348, 1095, 565)}
  ${connector(1390, 348, 1390, 440)}
  ${card(70, 440, 280, 130, "Bando", ["ente, codice", "prove e scadenze"], "navy", "softBlue")}
  ${card(365, 565, 280, 130, "Aree", ["comune", "delta fiscale"], "bordeaux", "softRed")}
  ${card(660, 440, 280, 130, "Nuclei", ["tributi, dogane", "riscossione, catasto"], "gold", "softGold")}
  ${card(955, 565, 280, 130, "Diario", ["dubbi ufficiali", "errori e rischi"], "green", "softGreen")}
  ${card(1250, 440, 280, 130, "Output", ["quiz, caso", "orale, checklist"], "teal", "softTeal")}
  ${note(250, 782, 1100, "Il Decoder fiscale non copia il bando: lo trasforma in classificazione, priorita e azione.")}
`
  return shell(
    "Mappa BANDO del Decoder fiscale",
    "Dal bando AE, ADM o AdER alla scheda operativa: famiglia, priorita, diario e output.",
    inner
  )
}

function figureCodiceProfilo() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${flowStep(120, 240, 300, "1", "Ente", ["AE", "ADM", "AdER"], "navy", "softBlue")}
  ${flowStep(470, 240, 300, "2", "Codice", ["TRIB, SPI, FT", "ADM/FAMM, AdER"], "bordeaux", "softRed")}
  ${flowStep(820, 240, 300, "3", "Programma", ["materie comuni", "materie fiscali"], "gold", "softGold")}
  ${flowStep(1170, 240, 300, "4", "Famiglia", ["M-FC02 guida", "o solo supporto"], "green", "softGreen")}
  <path class="arrowNavy" d="M420 340 L462 340"/>
  <path class="arrowBordeaux" d="M770 340 L812 340"/>
  <path class="arrowGold" d="M1120 340 L1162 340"/>
  ${matrixRow(165, 505, "AE", "tributario o territorio/SPI", "tributario, accertamento, catasto", "softBlue", "navy")}
  ${matrixRow(165, 590, "ADM", "dogane, accise, giochi", "glossario e controlli settoriali", "softRed", "bordeaux")}
  ${matrixRow(165, 675, "AdER", "riscossione nazionale", "cartelle, pagamenti, rateizzazioni", "softGreen", "green")}
  ${note(300, 810, 1000, "Il codice profilo e' un indizio: la prova vera e' il programma del bando.")}
`
  return shell(
    "Dal codice profilo alla famiglia M-FC02",
    "Ente, sigla e programma vanno letti insieme prima di scegliere materiali e moduli.",
    inner
  )
}

function figureProveOutput() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${proofCard(125, 235, "Quiz", ["tempo", "differenze secche"], "Diario errori", "navy", "softBlue")}
  ${proofCard(430, 235, "Scritto", ["definizione", "funzione, esempio"], "Schema risposta", "bordeaux", "softRed")}
  ${proofCard(735, 235, "Caso", ["soggetti", "vincoli, decisione"], "Griglia caso", "gold", "softGold")}
  ${proofCard(1040, 235, "Orale", ["lessico fiscale", "collegamenti"], "Risposte 2 min", "green", "softGreen")}
  ${proofCard(430, 545, "Situazionale", ["ruolo", "servizio, legalita"], "Gerarchia scelta", "teal", "softTeal")}
  ${proofCard(735, 545, "Titoli", ["documenti", "ricevute, prove"], "Checklist", "navy", "softBlue")}
  <path class="dash" d="M260 478 C370 520, 480 520, 590 478"/>
  <path class="dash" d="M875 478 C985 520, 1095 520, 1205 478"/>
  ${note(250, 810, 1100, "La stessa materia cambia allenamento: il bando decide quale output produrre.")}
`
  return shell(
    "Prove e output del Decoder fiscale",
    "La forma della prova decide se allenare quiz, risposte, casi, orale o checklist.",
    inner
  )
}

function figurePriorita() {
  const inner = `
  <rect class="card" x="70" y="158" width="1460" height="650" rx="30"/>
  ${priorityColumn(125, "Studio subito", ["definisce il profilo", "compare nella prova", "blocca altri nuclei"], "tributario AE", "navy", "softBlue")}
  ${priorityColumn(465, "Studio dopo", ["completa il profilo", "serve al secondo giro", "non decide subito"], "civile o contabilita", "bordeaux", "softRed")}
  ${priorityColumn(805, "Verifico sul bando", ["sigle profilo", "allegati e soglie", "banca dati o avvisi"], "codice e prova", "gold", "softGold")}
  ${priorityColumn(1145, "Rinvio modulo", ["baricentro non fiscale", "ICT, appalti, tecnico", "M-FC02 solo contesto"], "M-TR01/02/03", "green", "softGreen")}
  ${note(260, 810, 1080, "Se tutto e' urgente, niente e' prioritario: la griglia serve a tagliare dispersione.")}
`
  return shell(
    "Priorita di studio nel bando fiscale",
    "Studio subito, studio dopo, verifico sul bando o rinvio ad altro modulo.",
    inner
  )
}

function figureCaso() {
  const inner = `
  <rect class="card" x="70" y="158" width="1460" height="650" rx="30"/>
  ${caseCard(115, 240, "Decoder AE", "Giuridico-tributario", ["tributario", "accertamento", "adempimenti"], "Rischio: restare generico", "navy", "softBlue")}
  ${caseCard(575, 240, "Decoder ADM", "Assistente o FAMM", ["dogane", "accise", "giochi e monopoli"], "Rischio: copiare il piano AE", "bordeaux", "softRed")}
  ${caseCard(1035, 240, "Decoder AdER", "Addetto riscossione", ["cartelle", "pagamenti", "rateizzazioni"], "Rischio: confondere con accertamento", "green", "softGreen")}
  <path class="arrowGold" d="M360 642 C525 720, 650 720, 800 642"/>
  <path class="arrowGold" d="M1240 642 C1075 720, 950 720, 800 642"/>
  ${centerBadge(615, 670, 370, 80, "Una base comune", ["tre piani specialistici diversi"], "gold")}
  ${note(250, 812, 1100, "Il caso guidato mostra la funzione del Decoder: evitare un unico piano per tre profili diversi.")}
`
  return shell(
    "Caso guidato: tre Decoder fiscali",
    "Tre bandi fiscali richiedono tre letture diverse: AE, ADM e AdER.",
    inner
  )
}

function card(x, y, w, h, title, lines, color, fillClass) {
  const colorValue = palette[color]
  return safe(x, y, w, h, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${colorValue}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 43}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 76, 25, "muted small", 18)}
  `)
}

function flowStep(x, y, w, num, title, lines, color, fillClass) {
  return safe(x, y, w, 205, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="205" rx="24"/>
    <circle cx="${x + 42}" cy="${y + 48}" r="28" fill="${palette[color]}"/>
    <text x="${x + 42}" y="${y + 58}" text-anchor="middle" style="fill:#fff;font-family:'Source Sans 3','Segoe UI',Arial,sans-serif;font-size:27px;font-weight:900;">${num}</text>
    <text class="${color} label" x="${x + 88}" y="${y + 57}" style="font-size:25px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 112, 31, "muted body", 20)}
  `)
}

function matrixRow(x, y, left, mid, right, fillClass, color) {
  return safe(x, y, 1270, 62, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="1270" height="62" rx="16"/>
    <text class="${color} label" x="${x + 45}" y="${y + 39}" style="font-size:19px">${esc(left)}</text>
    <text class="ink body" x="${x + 220}" y="${y + 39}" style="font-weight:800;font-size:18px">${esc(mid)}</text>
    <text class="muted small" x="${x + 735}" y="${y + 39}" style="font-size:17px">${esc(right)}</text>
  `)
}

function proofCard(x, y, title, lines, output, color, fillClass) {
  return safe(x, y, 250, 220, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="250" height="220" rx="24"/>
    <rect x="${x}" y="${y}" width="250" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 125}" y="${y + 48}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    ${textLines(lines, x + 125, y + 88, 27, "muted small", 18)}
    <rect x="${x + 28}" y="${y + 152}" width="194" height="44" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text class="ink small" x="${x + 125}" y="${y + 181}" text-anchor="middle" style="font-weight:800;font-size:17px">${esc(output)}</text>
  `)
}

function priorityColumn(x, title, lines, example, color, fillClass) {
  return safe(x, 238, 290, 450, `
    <rect class="${fillClass}" x="${x}" y="238" width="290" height="450" rx="26"/>
    <rect x="${x}" y="238" width="290" height="12" rx="6" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 145}" y="292" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${bulletLines(lines, x + 38, 350, 38)}
    <rect x="${x + 32}" y="586" width="226" height="64" rx="22" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text class="ink small" x="${x + 145}" y="625" text-anchor="middle" style="font-weight:800;font-size:17px">${esc(example)}</text>
  `)
}

function caseCard(x, y, title, subtitle, nuclei, risk, color, fillClass) {
  return safe(x, y, 370, 405, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="370" height="405" rx="28"/>
    <rect x="${x}" y="${y}" width="370" height="12" rx="6" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 185}" y="${y + 54}" text-anchor="middle" style="font-size:25px">${esc(title)}</text>
    <text class="muted small" x="${x + 185}" y="${y + 88}" text-anchor="middle" style="font-size:18px">${esc(subtitle)}</text>
    ${bulletLines(nuclei, x + 54, y + 145, 42)}
    <rect x="${x + 34}" y="${y + 304}" width="302" height="62" rx="22" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <text class="ink small" x="${x + 185}" y="${y + 342}" text-anchor="middle" style="font-weight:800;font-size:16px">${esc(risk)}</text>
  `)
}

function centerBadge(x, y, w, h, title, lines, color) {
  return safe(x, y, w, h, `
    <rect class="note" x="${x}" y="${y}" width="${w}" height="${h}" rx="28"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 34}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 60, 22, "muted small", 17)}
  `)
}

function note(x, y, w, text) {
  return safe(x, y, w, 64, `
    <rect class="note" x="${x}" y="${y}" width="${w}" height="64" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-weight:800;font-size:20px">${esc(text)}</text>
  `)
}

function connector(x1, y1, x2, y2) {
  return `<path class="line" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function safe(x, y, w, h, inner) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 10">${inner}</g>`
}

function textLines(lines, x, y, gap, className, size) {
  return lines
    .map((line, index) => `<text class="${className}" x="${x}" y="${y + index * gap}" text-anchor="middle" style="font-size:${size}px">${esc(line)}</text>`)
    .join("\n")
}

function bulletLines(lines, x, y, gap) {
  return lines
    .map((line, index) => {
      const cy = y + index * gap - 7
      return `<circle cx="${x}" cy="${cy}" r="7" fill="${palette.gold}"/><text class="ink body" x="${x + 24}" y="${y + index * gap}" style="font-size:18px">${esc(line)}</text>`
    })
    .join("\n")
}

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
}

main().catch((error) => {
  console.error(error)
  process.exit(1)
})
