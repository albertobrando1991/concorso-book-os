const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-10"
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
    slug: "01-mappa-informatica-pa-digitale",
    title: "Informatica e PA digitale",
    subtitle: "La materia unisce lessico tecnico, uso operativo e istituti digitali della PA.",
    svg: figureMappa()
  },
  {
    slug: "02-hardware-software-dati",
    title: "Hardware, software e dati",
    subtitle: "Il candidato deve distinguere componenti fisiche, programmi, memoria e informazioni.",
    svg: figureHardware()
  },
  {
    slug: "03-file-office-dati",
    title: "File, Office e dati strutturati",
    subtitle: "File system, produttivita e tabelle non sono la stessa cosa: cambia la funzione.",
    svg: figureFileOffice()
  },
  {
    slug: "04-internet-reti-protocolli",
    title: "Internet, Web e protocolli",
    subtitle: "Browser, DNS, HTTP, posta e cloud usano la rete, ma presidiano livelli diversi.",
    svg: figureInternet()
  },
  {
    slug: "05-sicurezza-informatica-pa",
    title: "Sicurezza informatica nella PA",
    subtitle: "Riservatezza, integrita e disponibilita richiedono misure tecniche e organizzative.",
    svg: figureSicurezza()
  },
  {
    slug: "06-ecosistema-pa-digitale",
    title: "Ecosistema della PA digitale",
    subtitle: "CAD, identita, documenti, comunicazioni, pagamenti e dati formano un sistema.",
    svg: figurePaDigitale()
  },
  {
    slug: "07-istanza-online-conservazione",
    title: "Dall'istanza online alla conservazione",
    subtitle: "Ogni passaggio digitale deve restare tracciabile, sicuro, accessibile e conservabile.",
    svg: figureIstanza()
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
  return `# Asset Capitolo 10

Figure generate per \`Informatica, PA digitale e competenze digitali\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-informatica-pa-digitale.png\` | Mappa generale dei blocchi: base tecnica, sistemi e file, produttivita, reti, sicurezza, PA digitale. |
| \`02-hardware-software-dati.png\` | Distinzione tra hardware, sistema operativo, applicazioni, memoria e dati/informazioni. |
| \`03-file-office-dati.png\` | File system, Office e differenza tra foglio elettronico e database. |
| \`04-internet-reti-protocolli.png\` | Relazioni tra Internet, Web, DNS, HTTP/HTTPS, posta e cloud. |
| \`05-sicurezza-informatica-pa.png\` | Triade sicurezza, minacce, controlli e risposta agli incidenti nella PA. |
| \`06-ecosistema-pa-digitale.png\` | Mappa CAD degli strumenti PA digitale: identita, documenti, PEC, pagamenti, dati, cloud/accessibilita/privacy. |
| \`07-istanza-online-conservazione.png\` | Flusso operativo da accesso al servizio a protocollo, fascicolo, comunicazione e conservazione. |

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
  ${card(555, 185, 490, 145, "Competenza digitale", ["tecnica", "operativa", "amministrativa"], "navy", "card")}
  <path class="line" d="M800 330 L800 390"/>
  <path class="line" d="M245 390 L1355 390"/>
  ${connector(245, 390, 245, 455)}
  ${connector(467, 390, 467, 575)}
  ${connector(689, 390, 689, 455)}
  ${connector(911, 390, 911, 575)}
  ${connector(1133, 390, 1133, 455)}
  ${connector(1355, 390, 1355, 575)}
  ${card(105, 455, 280, 130, "Base tecnica", ["hardware", "software e dati"], "navy", "softBlue")}
  ${card(327, 575, 280, 130, "Sistema e file", ["cartelle", "percorsi, estensioni"], "bordeaux", "softRed")}
  ${card(549, 455, 280, 130, "Produttivita", ["documenti", "fogli e database"], "gold", "softGold")}
  ${card(771, 575, 280, 130, "Reti e web", ["browser, DNS", "protocolli"], "green", "softGreen")}
  ${card(993, 455, 280, 130, "Sicurezza", ["accessi, backup", "phishing, incidenti"], "navy", "softBlue")}
  ${card(1215, 575, 280, 130, "PA digitale", ["CAD, SPID, PEC", "dati e servizi"], "bordeaux", "softRed")}
  ${note(230, 795, 1140, "Obiettivo: riconoscere differenze operative e collegarle al lavoro pubblico.")}
`
  return shell("Informatica e PA digitale", "La materia unisce lessico tecnico, uso operativo e istituti digitali della PA.", inner)
}

function figureHardware() {
  const inner = `
  <rect class="card" x="105" y="190" width="1390" height="560" rx="30"/>
  <text class="navy label" x="800" y="245" text-anchor="middle">Dal componente fisico all'informazione utile</text>
  ${card(165, 315, 255, 135, "Hardware", ["CPU, RAM, disco", "monitor, rete"], "navy", "softBlue")}
  ${card(500, 315, 255, 135, "Sistema operativo", ["gestisce risorse", "file e periferiche"], "bordeaux", "softRed")}
  ${card(835, 315, 255, 135, "Applicazioni", ["browser, Office", "antivirus, gestionali"], "gold", "softGold")}
  ${card(1170, 315, 255, 135, "Dati", ["file, record", "codici e misure"], "green", "softGreen")}
  <path class="arrowNavy" d="M430 382 L485 382"/>
  <path class="arrowBordeaux" d="M765 382 L820 382"/>
  <path class="arrowGold" d="M1100 382 L1155 382"/>
  ${mini(230, 565, 230, "CPU", "elabora istruzioni", palette.navy)}
  ${mini(500, 565, 230, "RAM", "memoria volatile", palette.bordeaux)}
  ${mini(770, 565, 230, "SSD/HDD", "archiviazione stabile", palette.gold)}
  ${mini(1040, 565, 230, "Informazione", "dato interpretato", palette.green)}
  ${note(250, 795, 1100, "Errore da evitare: RAM, ROM e memoria di massa non svolgono la stessa funzione.")}
`
  return shell("Hardware, software e dati", "Il candidato deve distinguere componenti fisiche, programmi, memoria e informazioni.", inner)
}

function figureFileOffice() {
  const inner = `
  <rect class="card" x="90" y="190" width="600" height="555" rx="28"/>
  <text class="navy label" x="390" y="245" text-anchor="middle">File system</text>
  ${mini(150, 310, 180, "Unita", "C: o disco", palette.navy)}
  ${mini(405, 310, 220, "Cartelle", "contenitori logici", palette.bordeaux)}
  ${mini(150, 445, 180, "File", "dati + nome", palette.gold)}
  ${mini(405, 445, 220, "Estensione", ".pdf, .xlsx, .zip", palette.green)}
  ${mini(255, 595, 270, "Percorso", "posizione completa", palette.navy)}
  <path class="arrowNavy" d="M332 340 L390 340"/>
  <path class="arrowBordeaux" d="M515 445 L515 405"/>
  <path class="arrowGold" d="M330 595 L255 515"/>
  <rect class="card" x="805" y="190" width="705" height="555" rx="28"/>
  <text class="navy label" x="1158" y="245" text-anchor="middle">Produttivita e dati</text>
  ${card(855, 305, 275, 120, "Word / Writer", ["testi, stili", "PDF e stampa"], "navy", "softBlue")}
  ${card(1180, 305, 275, 120, "Excel / Calc", ["celle, formule", "funzioni e grafici"], "gold", "softGold")}
  ${card(855, 505, 275, 120, "PowerPoint", ["slide, layout", "transizioni"], "bordeaux", "softRed")}
  ${card(1180, 505, 275, 120, "Database", ["tabelle, query", "relazioni"], "green", "softGreen")}
  ${note(260, 800, 1080, "Domanda guida: sto gestendo un file, facendo calcoli o interrogando dati strutturati?")}
`
  return shell("File, Office e dati strutturati", "File system, produttivita e tabelle non sono la stessa cosa: cambia la funzione.", inner)
}

function figureInternet() {
  const inner = `
  <rect class="card" x="90" y="185" width="1420" height="565" rx="30"/>
  <text class="navy label" x="800" y="240" text-anchor="middle">Internet e' l'infrastruttura; Web, posta e cloud sono servizi</text>
  ${card(135, 330, 255, 130, "Utente", ["browser", "app o client"], "navy", "softBlue")}
  ${card(475, 330, 255, 130, "DNS", ["nome dominio", "indirizzo IP"], "bordeaux", "softRed")}
  ${card(815, 330, 255, 130, "Server web", ["risorse", "pagine e API"], "gold", "softGold")}
  ${card(1155, 330, 255, 130, "Servizi", ["web, email", "cloud"], "green", "softGreen")}
  <path class="arrowNavy" d="M400 392 L460 392"/>
  <path class="arrowBordeaux" d="M740 392 L800 392"/>
  <path class="arrowGold" d="M1080 392 L1140 392"/>
  ${mini(215, 575, 230, "HTTP/HTTPS", "pagine web", palette.navy)}
  ${mini(505, 575, 230, "SMTP/IMAP", "posta elettronica", palette.bordeaux)}
  ${mini(795, 575, 230, "TCP/IP", "rete e trasporto", palette.gold)}
  ${mini(1085, 575, 230, "URL", "risorsa sul Web", palette.green)}
  ${note(260, 800, 1080, "Trappola ricorrente: browser, motore di ricerca, Web e Internet non sono sinonimi.")}
`
  return shell("Internet, Web e protocolli", "Browser, DNS, HTTP, posta e cloud usano la rete, ma presidiano livelli diversi.", inner)
}

function figureSicurezza() {
  const inner = `
  ${pill(280, 190, 260, "Riservatezza", palette.navy)}
  ${pill(670, 190, 260, "Integrita", palette.bordeaux)}
  ${pill(1060, 190, 260, "Disponibilita", palette.green)}
  <path class="line" d="M800 275 L800 330"/>
  <rect class="card" x="95" y="330" width="1410" height="390" rx="30"/>
  ${card(150, 405, 330, 135, "Minacce", ["phishing, malware", "errore umano"], "bordeaux", "softRed")}
  ${card(635, 405, 330, 135, "Controlli", ["MFA, firewall", "backup e patch"], "navy", "softBlue")}
  ${card(1120, 405, 330, 135, "Risposta", ["rileva, contiene", "ripristina e segnala"], "green", "softGreen")}
  <path class="arrowBordeaux" d="M495 472 L620 472"/>
  <path class="arrowNavy" d="M980 472 L1105 472"/>
  ${mini(230, 610, 250, "Accessi", "autenticazione + permessi", palette.navy)}
  ${mini(535, 610, 250, "Dati", "cifratura e minimizzazione", palette.bordeaux)}
  ${mini(840, 610, 250, "Servizi", "continuita operativa", palette.gold)}
  ${mini(1145, 610, 250, "Incidenti", "log, notifica, correzione", palette.green)}
  ${note(245, 795, 1110, "Risposta da concorso: sicurezza = tecnica, organizzazione, formazione e responsabilita.")}
`
  return shell("Sicurezza informatica nella PA", "Riservatezza, integrita e disponibilita richiedono misure tecniche e organizzative.", inner)
}

function figurePaDigitale() {
  const inner = `
  ${card(555, 185, 490, 145, "CAD", ["diritti digitali", "processi e servizi"], "navy", "card")}
  <path class="line" d="M800 330 L800 390"/>
  <path class="line" d="M245 390 L1355 390"/>
  ${connector(245, 390, 245, 455)}
  ${connector(467, 390, 467, 575)}
  ${connector(689, 390, 689, 455)}
  ${connector(911, 390, 911, 575)}
  ${connector(1133, 390, 1133, 455)}
  ${connector(1355, 390, 1355, 575)}
  ${card(105, 455, 280, 130, "Identita", ["SPID, CIE, CNS", "accesso ai servizi"], "navy", "softBlue")}
  ${card(327, 575, 280, 130, "Documenti", ["firma digitale", "protocollo"], "bordeaux", "softRed")}
  ${card(549, 455, 280, 130, "Comunicazioni", ["PEC, domicilio", "SEND e App IO"], "gold", "softGold")}
  ${card(771, 575, 280, 130, "Pagamenti", ["pagoPA", "tracciabilita"], "green", "softGreen")}
  ${card(993, 455, 280, 130, "Dati", ["PDND, API", "open data"], "navy", "softBlue")}
  ${card(1215, 575, 280, 130, "Qualita", ["cloud, privacy", "accessibilita"], "bordeaux", "softRed")}
  ${note(235, 795, 1130, "La PA digitale non e' un elenco di sigle: ogni strumento presidia una funzione.")}
`
  return shell("Ecosistema della PA digitale", "CAD, identita, documenti, comunicazioni, pagamenti e dati formano un sistema.", inner)
}

function figureIstanza() {
  const steps = [
    ["1", "Accesso", "SPID, CIE, CNS"],
    ["2", "Modulo", "dati necessari"],
    ["3", "Allegati", "formati leggibili"],
    ["4", "Pagamento", "pagoPA"],
    ["5", "Protocollo", "registrazione"],
    ["6", "Fascicolo", "documenti e metadati"],
    ["7", "Istruttoria", "database e permessi"],
    ["8", "Comunicazione", "PEC, IO, SEND"],
    ["9", "Sicurezza", "privacy e log"],
    ["10", "Conservazione", "integrita nel tempo"]
  ]
  const topX = [95, 385, 675, 965, 1255]
  const bottomX = [95, 385, 675, 965, 1255]
  const topCards = steps.slice(0, 5).map((item, index) => stepCard(topX[index], 215, item, 220)).join("\n")
  const bottomCards = steps.slice(5).map((item, index) => stepCard(bottomX[index], 545, item, 220)).join("\n")
  const topArrows = topX
    .slice(0, -1)
    .map((x, index) => `<path class="arrowNavy" d="M${x + 232} 297 L${topX[index + 1] - 18} 297"/>`)
    .join("\n")
  const bottomArrows = bottomX
    .slice(0, -1)
    .map((x, index) => `<path class="arrowBordeaux" d="M${x + 232} 627 L${bottomX[index + 1] - 18} 627"/>`)
    .join("\n")
  const inner = `
  ${topCards}
  ${topArrows}
  <path class="arrowGold" d="M1365 380 C1435 430 1415 492 1365 530"/>
  ${bottomCards}
  ${bottomArrows}
  ${note(250, 800, 1100, "Controllo finale: identificare, tracciare, proteggere, comunicare e conservare.")}
`
  return shell("Dall'istanza online alla conservazione", "Ogni passaggio digitale deve restare tracciabile, sicuro, accessibile e conservabile.", inner)
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleY = y + 42
  const titleFontSize = title.length > 18 ? 21 : title.length > 14 ? 23 : 25
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

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 18 ? 19 : title.length > 14 ? 20 : 21

  return `<g data-safe-box="${x} ${y} ${w} 74 8">
    <rect x="${x}" y="${y}" width="${w}" height="74" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 56}" text-anchor="middle" fill="#FFFFFF" style="font-size:16px">${esc(body)}</text>
  </g>`
}

function pill(x, y, w, text, color) {
  const fontSize = text.length > 14 ? 20 : 22

  return `<g data-safe-box="${x} ${y} ${w} 62 8">
    <rect x="${x}" y="${y}" width="${w}" height="62" rx="31" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 41}" text-anchor="middle" fill="#FFFFFF" style="font-size:${fontSize}px">${esc(text)}</text>
  </g>`
}

function stepCard(x, y, [number, title, subtitle], w) {
  const center = x + w / 2
  const titleFontSize = title.length > 13 ? 18 : 20
  const subtitleFontSize = subtitle.length > 18 ? 16 : 17

  return `<g data-safe-box="${x} ${y} ${w} 160 8">
    <rect class="card" x="${x}" y="${y}" width="${w}" height="160" rx="20"/>
    <circle cx="${center}" cy="${y + 37}" r="24" fill="${palette.gold}"/>
    <text class="ink label" x="${center}" y="${y + 46}" text-anchor="middle" style="font-size:23px">${esc(number)}</text>
    <text class="navy label" x="${center}" y="${y + 92}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${center}" y="${y + 124}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 95 ? 18 : text.length > 80 ? 19 : 20

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
