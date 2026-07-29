const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "moduli",
  "m-fl03-camere-commercio",
  "assets",
  "chapter-01"
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
  white: "#FFFFFF",
  cream: "#FFF7ED",
  blueSoft: "#EAF2FB",
  redSoft: "#F8E8EA",
  goldSoft: "#FFF4CC",
  greenSoft: "#E7F3ED",
  tealSoft: "#E4F4F5"
}

const figures = [
  {
    slug: "01-mappa-bando-sistema-camerale",
    title: "Mappa BANDO del sistema camerale",
    subtitle: "Dal bando camerale a ente, funzione, servizio e output di prova.",
    svg: figureMappaBando()
  },
  {
    slug: "02-autonomia-funzionale-camera-commercio",
    title: "Camera di commercio: autonomia funzionale",
    subtitle: "Ente pubblico, sistema delle imprese, mercato e territorio economico.",
    svg: figureAutonomiaFunzionale()
  },
  {
    slug: "03-sistema-camerale-unioncamere",
    title: "Sistema camerale e Unioncamere",
    subtitle: "Camere, unioni regionali, Unioncamere e strumenti comuni.",
    svg: figureSistemaUnioncamere()
  },
  {
    slug: "04-funzioni-camerali-servizi-mercato",
    title: "Funzioni camerali: dal concetto al servizio",
    subtitle: "Registro imprese, semplificazione, mercato, servizi e organizzazione.",
    svg: figureFunzioniCamerali()
  },
  {
    slug: "05-catena-impresa-camera-suap",
    title: "Catena operativa impresa-Camera-SUAP",
    subtitle: "Domanda dell'utente, servizio camerale, competenza SUAP e output.",
    svg: figureCatenaImpresaCameraSuap()
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
      await page.locator("img").screenshot({ path: path.join(OUTPUT_DIR, `${figure.slug}.png`) })
      await page.close()
    }
  } finally {
    await browser.close()
  }

  await fs.writeFile(path.join(OUTPUT_DIR, "README.md"), renderReadme(), "utf8")
}

function renderReadme() {
  return `# Asset Capitolo 1 - M-FL03 Camere di commercio

Figure generate per \`Camere di commercio, sistema camerale e Unioncamere\`.

## Analisi stile libro base

La ricognizione delle immagini gia presenti nel libro base e nei moduli illustrati conferma una grammatica editoriale costante:

- master vettoriale \`.svg\` e versione \`.png\` 1600 x 900 per preview, dashboard e PDF;
- palette istituzionale con Navy, Bordeaux, Muted Gold, Green, Teal, grigi chiari e fondo Off-White;
- immagini didattiche, non decorative: mappe BANDO, flussi, confronti, matrici e sintesi anti-errore;
- testi interni brevi, card a raggio contenuto, frecce leggere, nessuna fotografia stock e nessuna ornamentazione autonoma;
- inserimento subito dopo il blocco di testo che l'immagine traduce in schema.

Per questo capitolo sono opportune 5 figure: coprono mappa BANDO, identita funzionale della Camera, sistema camerale, funzioni trasformate in servizi e catena operativa impresa-Camera-SUAP.

| File | Master vettoriale | Funzione didattica |
|---|---|---|
| \`01-mappa-bando-sistema-camerale.png\` | \`01-mappa-bando-sistema-camerale.svg\` | Mappa BANDO di apertura: ente, aree, nuclei, diario errori e output del concorso camerale. |
| \`02-autonomia-funzionale-camera-commercio.png\` | \`02-autonomia-funzionale-camera-commercio.svg\` | Schema anti-confusione sulla Camera come ente pubblico ad autonomia funzionale. |
| \`03-sistema-camerale-unioncamere.png\` | \`03-sistema-camerale-unioncamere.svg\` | Rete del sistema camerale: Camere, unioni regionali, Unioncamere e strumenti comuni. |
| \`04-funzioni-camerali-servizi-mercato.png\` | \`04-funzioni-camerali-servizi-mercato.svg\` | Conversione delle funzioni camerali in servizi e output di prova. |
| \`05-catena-impresa-camera-suap.png\` | \`05-catena-impresa-camera-suap.svg\` | Flusso operativo per distinguere Registro imprese, servizio camerale e profilo SUAP. |
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${node(585, 205, 430, 116, "Bando camerale", ["ente, profilo", "servizio e prove"], "navy", "softBlue")}
  <path class="line" d="M800 321 L800 372"/>
  <path class="line" d="M205 372 L1395 372"/>
  ${line(205, 372, 205, 455)}
  ${line(505, 372, 505, 580)}
  ${line(800, 372, 800, 455)}
  ${line(1095, 372, 1095, 580)}
  ${line(1395, 372, 1395, 455)}
  ${node(70, 455, 270, 130, "B - Bando", ["Camera", "Unioncamere"], "navy", "softBlue")}
  ${node(370, 580, 270, 130, "A - Aree", ["ordinamento", "servizi, mercato"], "bordeaux", "softRed")}
  ${node(665, 455, 270, 130, "N - Nuclei", ["autonomia", "Registro, REA"], "gold", "softGold")}
  ${node(960, 580, 270, 130, "D - Diario", ["no Comune", "no archivio"], "green", "softGreen")}
  ${node(1260, 455, 270, 130, "O - Output", ["risposta orale", "caso e checklist"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Prima domanda: quale funzione camerale rende corretta la risposta?")}
`

  return shell(
    "Mappa BANDO del sistema camerale",
    "Dal bando camerale a ente, funzione, servizio e output di prova.",
    inner
  )
}

function figureAutonomiaFunzionale() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${wide(525, 245, 550, "Camera di commercio", ["ente pubblico ad autonomia funzionale", "funzioni di interesse generale per imprese e mercato"], "navy", "softBlue")}
  ${line(800, 355, 800, 430)}
  ${line(370, 430, 1230, 430)}
  ${line(370, 430, 370, 510)}
  ${line(660, 430, 660, 510)}
  ${line(940, 430, 940, 510)}
  ${line(1230, 430, 1230, 510)}
  ${pillar(190, 510, "Natura pubblica", ["legalita", "procedimento", "trasparenza"], "navy", "softBlue")}
  ${pillar(480, 510, "Funzione propria", ["imprese", "mercato", "pubblicita"], "bordeaux", "softRed")}
  ${pillar(760, 510, "Territorio economico", ["unita locali", "filiere", "servizi"], "gold", "softGold")}
  ${pillar(1050, 510, "Sistema camerale", ["rete", "strumenti", "supporto"], "green", "softGreen")}
  ${note(270, 815, 1060, "Anti-errore: non e Comune, non e ufficio periferico statale, non e sola rappresentanza di imprese.")}
`

  return shell(
    "Camera di commercio: autonomia funzionale",
    "Ente pubblico, sistema delle imprese, mercato e territorio economico.",
    inner
  )
}

function figureSistemaUnioncamere() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${wide(525, 210, 550, "Unioncamere", ["rappresentanza, coordinamento e supporto", "strumenti comuni del sistema camerale"], "navy", "softBlue")}
  ${arrow(610, 338, 360, 455, "Navy")}
  ${arrow(800, 338, 800, 455, "Navy")}
  ${arrow(990, 338, 1240, 455, "Navy")}
  ${networkNode(150, 455, "Unioni regionali", ["raccordo territoriale", "supporto alle Camere"], "bordeaux", "softRed")}
  ${networkNode(590, 455, "Camere di commercio", ["ente operativo", "servizi e procedimenti"], "gold", "softGold")}
  ${networkNode(1030, 455, "Organismi e strumenti", ["InfoCamere", "piattaforme digitali"], "green", "softGreen")}
  ${arrow(342, 615, 590, 680, "Bordeaux")}
  ${arrow(800, 615, 800, 680, "Gold")}
  ${arrow(1258, 615, 1010, 680, "Green")}
  ${wide(445, 680, 710, "Imprese, professionisti, PA e utenti", ["servizi condivisi, dati pubblici, pratiche telematiche", "visure, certificati, ComUnica, SUAP e strumenti informativi"], "teal", "softTeal")}
  ${note(235, 815, 1130, "La rete non va descritta come comando gerarchico semplice: conta il raccordo operativo.")}
`

  return shell(
    "Sistema camerale e Unioncamere",
    "Camere, unioni regionali, Unioncamere e strumenti comuni.",
    inner
  )
}

function figureFunzioniCamerali() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${functionCard(100, 255, "Registro e REA", ["iscrizioni", "visure", "certificati"], "navy", "softBlue")}
  ${arrow(360, 335, 410, 335, "Navy")}
  ${functionCard(430, 255, "Semplificazione", ["ComUnica", "SUAP digitale", "pratiche online"], "bordeaux", "softRed")}
  ${arrow(690, 335, 740, 335, "Bordeaux")}
  ${functionCard(760, 255, "Regolazione", ["mercato", "fede pubblica", "controlli"], "gold", "softGold")}
  ${arrow(1020, 335, 1070, 335, "Gold")}
  ${functionCard(1090, 255, "Servizi imprese", ["supporto", "promozione", "digitale"], "green", "softGreen")}
  ${line(1230, 485, 1230, 585)}
  ${wide(430, 585, 740, "Organizzazione e comunicazione", ["uffici, sportello, procedimento, trasparenza e relazione con l'utenza", "la materia diventa mansione, caso pratico e risposta orale"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Il valore concorsuale e trasformare ogni funzione in servizio, procedimento, utente e output.")}
`

  return shell(
    "Funzioni camerali: dal concetto al servizio",
    "Registro imprese, semplificazione, mercato, servizi e organizzazione.",
    inner
  )
}

function figureCatenaImpresaCameraSuap() {
  const inner = `
  <rect class="card" x="70" y="160" width="1460" height="640" rx="30"/>
  ${wide(155, 245, 380, "Impresa o professionista", ["richiede iscrizione, dato, documento", "oppure avvio/modifica attivita"], "navy", "softBlue")}
  ${arrow(540, 300, 700, 300, "Navy")}
  ${wide(700, 245, 380, "Domanda da classificare", ["dato camerale, documento", "titolo, SCIA o autorizzazione"], "gold", "softGold")}
  ${arrow(885, 360, 600, 500, "Gold")}
  ${arrow(895, 360, 1180, 500, "Gold")}
  ${wide(325, 500, 470, "Camera di commercio", ["Registro imprese, REA, visure, certificati", "servizi camerali e controlli di competenza"], "bordeaux", "softRed")}
  ${wide(805, 500, 470, "Comune e SUAP", ["titoli per attivita produttive", "SCIA, autorizzazioni e canale amministrativo"], "green", "softGreen")}
  ${line(560, 610, 560, 690)}
  ${line(1040, 610, 1040, 690)}
  ${wide(445, 690, 710, "Output corretto", ["orientare l'utente senza confondere competenze", "separare dato camerale, profilo SUAP e strumenti digitali"], "teal", "softTeal")}
  ${note(245, 815, 1110, "Nel caso pratico non accentrare tutto: classifica la richiesta e indica il canale competente.")}
`

  return shell(
    "Catena operativa impresa-Camera-SUAP",
    "Domanda dell'utente, servizio camerale, competenza SUAP e output.",
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
      .title { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 43px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 22px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: 0; }
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

function node(x, y, w, h, title, lines, color, fillClass) {
  return safe(x, y, w, h, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 73, 25, "muted small", 18)}
  `)
}

function wide(x, y, w, title, lines, color, fillClass) {
  return safe(x, y, w, 110, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="${w}" height="110" rx="26"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + w / 2}" y="${y + 40}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    ${textLines(lines, x + w / 2, y + 72, 24, "muted small", 17)}
  `)
}

function pillar(x, y, title, lines, color, fillClass) {
  return safe(x, y, 260, 160, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="260" height="160" rx="24"/>
    <rect x="${x}" y="${y}" width="260" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 130}" y="${y + 42}" text-anchor="middle" style="font-size:20px">${esc(title)}</text>
    <path class="thin" d="M${x + 42} ${y + 68} L${x + 218} ${y + 68}"/>
    ${textLines(lines, x + 130, y + 98, 25, "muted small", 17)}
  `)
}

function networkNode(x, y, title, lines, color, fillClass) {
  return safe(x, y, 360, 160, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="360" height="160" rx="26"/>
    <rect x="${x}" y="${y}" width="360" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 180}" y="${y + 43}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    <path class="thin" d="M${x + 58} ${y + 70} L${x + 302} ${y + 70}"/>
    ${textLines(lines, x + 180, y + 100, 28, "muted small", 17)}
  `)
}

function functionCard(x, y, title, lines, color, fillClass) {
  return safe(x, y, 260, 230, `
    <rect class="${fillClass}" x="${x}" y="${y}" width="260" height="230" rx="26"/>
    <rect x="${x}" y="${y}" width="260" height="10" rx="5" fill="${palette[color]}"/>
    <text class="${color} label" x="${x + 130}" y="${y + 48}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    <path class="thin" d="M${x + 45} ${y + 78} L${x + 215} ${y + 78}"/>
    ${bulletLines(lines, x + 56, y + 122, 38)}
  `)
}

function note(x, y, w, text) {
  return safe(x, y, w, 62, `
    <rect class="note" x="${x}" y="${y}" width="${w}" height="62" rx="24"/>
    <text class="ink body" x="${x + w / 2}" y="${y + 39}" text-anchor="middle" style="font-weight:800;font-size:20px">${esc(text)}</text>
  `)
}

function arrow(x1, y1, x2, y2, color) {
  return `<path class="arrow${color}" d="M${x1} ${y1} L${x2} ${y2}"/>`
}

function line(x1, y1, x2, y2) {
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
    .map((text, index) => {
      const lineY = y + index * gap
      return `<circle cx="${x}" cy="${lineY - 7}" r="6" fill="${palette.gold}"/><text class="ink body" x="${x + 22}" y="${lineY}" style="font-size:18px">${esc(text)}</text>`
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
