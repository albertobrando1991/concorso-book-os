const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const outputDir = path.join(
  process.cwd(),
  "wiki",
  "books",
  "moduli",
  "m-fc05-authority-indipendenti",
  "assets",
  "chapter-01"
)

const palette = {
  bg: "#F8FAFC",
  white: "#FFFFFF",
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
  tealSoft: "#E4F4F5"
}

const figures = [
  {
    slug: "01-mappa-bando-authority",
    title: "Mappa BANDO delle authority",
    subtitle: "Dal bando al percorso di studio, fino all'output richiesto in prova.",
    svg: figureMappaBando()
  },
  {
    slug: "02-authority-settori-poteri",
    title: "Authority, settori e poteri",
    subtitle: "La sigla non basta: ogni ente va letto da interesse protetto, settore e funzione.",
    svg: figureSettoriPoteri()
  },
  {
    slug: "03-percorsi-g-e-p",
    title: "Tre percorsi, una base comune",
    subtitle: "G, E e P cambiano priorità, linguaggio e tipo di allenamento.",
    svg: figurePercorsi()
  },
  {
    slug: "04-nucleo-comune-delta-authority",
    title: "Nucleo comune e delta authority",
    subtitle: "La preparazione efficace collega categorie generali, settore e prova concreta.",
    svg: figureNucleoDelta()
  },
  {
    slug: "05-bando-decoder-authority",
    title: "Bando Decoder M-FC05",
    subtitle: "La scheda minima per scegliere contenuti, priorità e output prima di studiare.",
    svg: figureDecoder()
  }
]

async function main() {
  await fs.mkdir(outputDir, { recursive: true })

  for (const figure of figures) {
    await fs.writeFile(path.join(outputDir, `${figure.slug}.svg`), figure.svg, "utf8")
  }

  const browser = await chromium.launch({ headless: true })
  try {
    for (const figure of figures) {
      const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 })
      const encoded = Buffer.from(figure.svg, "utf8").toString("base64")
      await page.setContent(
        `<html><body style="margin:0;background:${palette.bg}"><img src="data:image/svg+xml;base64,${encoded}" width="1600" height="1000"></body></html>`,
        { waitUntil: "load" }
      )
      await page.locator("img").screenshot({ path: path.join(outputDir, `${figure.slug}.png`) })
      await page.close()
    }
  } finally {
    await browser.close()
  }

  await fs.writeFile(path.join(outputDir, "README.md"), renderReadme(), "utf8")
}

function figureMappaBando() {
  const items = [
    [105, "B — Bando", ["ente, profilo, prove", "programma e criteri"], "navy", "softBlue"],
    [395, "A — Aree", ["base VOL-01", "delta M-FC05"], "bordeaux", "softRed"],
    [685, "N — Nuclei", ["fonte, interesse", "potere e procedura"], "gold", "softGold"],
    [975, "D — Diario", ["errori, rinvii", "priorità e dubbi"], "green", "softGreen"],
    [1265, "O — Output", ["quiz, memo, caso", "risposta orale"], "teal", "softTeal"]
  ]
  const cards = items.map(([x, title, lines, color, box]) => card(x, 500, 230, 150, title, lines, color, box)).join("\n")
  const connectors = items.map(([x]) => `<path class="line" d="M800 405 L${Number(x) + 115} 405 L${Number(x) + 115} 485"/>`).join("\n")

  return shell("Mappa BANDO delle authority", "Dal bando al percorso di studio, fino all'output richiesto in prova.", `
  ${card(520, 190, 560, 160, "Bando per authority", ["ente, profilo, materie e formato della prova", "prima leggi il programma, poi scegli il percorso"], "navy", "softBlue")}
  <path class="line" d="M800 350 L800 405"/>
  ${connectors}
  ${cards}
  ${note(230, 835, 1140, "Obiettivo: trasformare la sigla dell'ente in una preparazione verificabile e non dispersiva.")}
`)
}

function figureSettoriPoteri() {
  const top = [
    [95, "AGCM", ["concorrenza", "consumatore"], "navy", "softBlue"],
    [475, "ARERA", ["energia, acqua", "tariffe, qualità"], "green", "softGreen"],
    [855, "AGCOM", ["comunicazioni", "media, utenti"], "teal", "softTeal"],
    [1235, "CONSOB", ["mercati", "investitore"], "bordeaux", "softRed"]
  ]
  const bottom = [
    [95, "Banca d'Italia", ["stabilità", "vigilanza"], "gold", "softGold"],
    [475, "IVASS", ["assicurazioni", "condotta"], "gold", "softGold"],
    [855, "Garante", ["dati personali", "cooperazione UE"], "green", "softGreen"],
    [1235, "ANAC", ["integrità", "prevenzione"], "bordeaux", "softRed"]
  ]

  return shell("Authority, settori e poteri", "La sigla non basta: ogni ente va letto da interesse protetto, settore e funzione.", `
  <rect class="card" x="65" y="175" width="1470" height="605" rx="30"/>
  <text class="navy label" x="800" y="235" text-anchor="middle">Domanda guida: quale interesse è protetto e con quale potere?</text>
  ${top.map(([x, title, lines, color, box]) => card(x, 305, 270, 150, title, lines, color, box)).join("\n")}
  ${bottom.map(([x, title, lines, color, box]) => card(x, 545, 270, 150, title, lines, color, box)).join("\n")}
  ${note(230, 850, 1140, "Regolazione, vigilanza, istruttoria e sanzione non sono etichette equivalenti: dipendono da fonte e settore.")}
`)
}

function figurePercorsi() {
  const columns = [
    [100, "G — Giuridico", "navy", "softBlue", ["fonti e poteri", "procedimento", "garanzie e rimedi"], "Rischio: elenco di norme senza sequenza."],
    [555, "E — Economico-regolatorio", "green", "softGreen", ["mercati e incentivi", "tariffe e qualità", "dati e consultazione"], "Rischio: formule senza problema regolatorio."],
    [1010, "P — Giuridico-economico", "bordeaux", "softRed", ["norma e mercato", "dato e decisione", "memo tecnico"], "Rischio: accumulare tutti i settori." ]
  ]
  return shell("Tre percorsi, una base comune", "G, E e P cambiano priorità, linguaggio e tipo di allenamento.", `
  <rect class="softGold" x="315" y="175" width="970" height="105" rx="26"/>
  <text class="gold label" x="800" y="220" text-anchor="middle">Base comune: bando, fonti, procedimento, dati, prova e diario degli errori</text>
  <text class="muted small" x="800" y="254" text-anchor="middle">Il profilo ordina le priorità: non autorizza a ignorare le garanzie comuni.</text>
  ${columns.map(([x, title, color, box, lines, warning]) => profileColumn(x, title, color, box, lines, warning)).join("\n")}
  ${note(230, 850, 1140, "Scegli il percorso dal programma e dall'output di prova, non dal nome più attraente dell'ente.")}
`)
}

function figureNucleoDelta() {
  return shell("Nucleo comune e delta authority", "La preparazione efficace collega categorie generali, settore e prova concreta.", `
  ${card(95, 255, 370, 245, "Nucleo comune VOL-01", ["fonti e principi", "procedimento e provvedimento", "trasparenza, privacy, anticorruzione"], "navy", "softBlue")}
  <path class="arrowNavy" d="M485 378 L620 378"/>
  ${card(630, 255, 340, 245, "Delta M-FC05", ["interesse protetto", "poteri e reti", "dati, mercato, settore"], "bordeaux", "softRed")}
  <path class="arrowBordeaux" d="M990 378 L1125 378"/>
  ${card(1135, 255, 370, 245, "Prova reale", ["quiz: differenze", "orale: catena logica", "caso: fatti, potere, esito"], "green", "softGreen")}
  <rect class="card" x="190" y="610" width="1220" height="125" rx="26"/>
  <text class="navy label" x="800" y="662" text-anchor="middle">Formula operativa</text>
  <text class="muted body" x="800" y="705" text-anchor="middle">categoria generale + applicazione settoriale + output richiesto = risposta concorsuale utilizzabile</text>
  ${note(230, 850, 1140, "La base non va duplicata; va richiamata quando serve a comprendere una scelta regolatoria concreta.")}
`)
}

function figureDecoder() {
  const fields = [
    [105, 290, "Ente e settore", "AGCM, ARERA, privacy...", "navy", "softBlue"],
    [420, 290, "Profilo", "G, E, P o denominazione", "bordeaux", "softRed"],
    [735, 290, "Prove", "quiz, scritto, orale, memo", "gold", "softGold"],
    [1050, 290, "Nuclei", "fonte, potere, garanzia", "green", "softGreen"],
    [1295, 290, "Rischio", "confusione, fonte, tempo", "teal", "softTeal"],
    [260, 555, "Materie base", "rinvio puntuale a VOL-01", "navy", "softBlue"],
    [660, 555, "Delta specialistico", "capitolo M-FC05 prioritario", "bordeaux", "softRed"],
    [1060, 555, "Output", "risposta, schema, esercizio", "green", "softGreen"]
  ]
  return shell("Bando Decoder M-FC05", "La scheda minima per scegliere contenuti, priorità e output prima di studiare.", `
  <rect class="card" x="65" y="175" width="1470" height="610" rx="30"/>
  <text class="navy label" x="800" y="235" text-anchor="middle">Compila i campi prima di acquistare materiali o distribuire le ore di studio</text>
  ${fields.map(([x, y, title, text, color, box], index) => decoderField(x, y, title, text, color, box, index < 5 ? 240 : 310)).join("\n")}
  ${note(230, 850, 1140, "Il bando guida il materiale: ogni campo vuoto segnala una verifica da fare prima di programmare lo studio.")}
`)
}

function shell(title, subtitle, content) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000" role="img" aria-labelledby="title desc">
  <title id="title">${esc(title)}</title>
  <desc id="desc">${esc(subtitle)}</desc>
  <defs>
    <style>
      .bg { fill: ${palette.bg}; } .card { fill: ${palette.white}; stroke: ${palette.border}; stroke-width: 3; }
      .softBlue { fill: ${palette.blueSoft}; stroke: #B9CBE0; stroke-width: 2.5; } .softRed { fill: ${palette.redSoft}; stroke: #E3B9BF; stroke-width: 2.5; }
      .softGold { fill: ${palette.goldSoft}; stroke: #E8D080; stroke-width: 2.5; } .softGreen { fill: ${palette.greenSoft}; stroke: #A8D1BD; stroke-width: 2.5; }
      .softTeal { fill: ${palette.tealSoft}; stroke: #A3D5D8; stroke-width: 2.5; } .note { fill: ${palette.cream}; stroke: #E7C18E; stroke-width: 2.5; }
      .ink { fill: ${palette.ink}; font-family: Arial, Helvetica, sans-serif; } .muted { fill: ${palette.muted}; font-family: Arial, Helvetica, sans-serif; }
      .title { font-size: 43px; font-weight: 700; } .subtitle { font-size: 22px; } .label { font-family: Arial, Helvetica, sans-serif; font-size: 25px; font-weight: 700; }
      .body { font-family: Arial, Helvetica, sans-serif; font-size: 20px; } .small { font-family: Arial, Helvetica, sans-serif; font-size: 18px; }
      .navy { fill: ${palette.navy}; } .bordeaux { fill: ${palette.bordeaux}; } .gold { fill: ${palette.gold}; } .green { fill: ${palette.green}; } .teal { fill: ${palette.teal}; }
      .line { stroke: ${palette.line}; stroke-width: 4; stroke-linecap: round; fill: none; } .thin { stroke: ${palette.border}; stroke-width: 2.5; stroke-linecap: round; fill: none; }
      .arrowNavy { stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowNavy); } .arrowBordeaux { stroke: ${palette.bordeaux}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowBordeaux); }
    </style>
    <marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="${palette.navy}"/></marker>
    <marker id="arrowBordeaux" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="${palette.bordeaux}"/></marker>
  </defs>
  <rect class="bg" width="1600" height="1000"/>
  <text class="ink title" x="800" y="70" text-anchor="middle">${esc(title)}</text>
  <text class="muted subtitle" x="800" y="112" text-anchor="middle">${esc(subtitle)}</text>
  ${content}
</svg>`
}

function card(x, y, w, h, title, lines, color, box) {
  const titleSize = title.length > 24 ? 19 : title.length > 18 ? 21 : 23
  const body = lines.map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 88 + index * 27}" text-anchor="middle" style="font-size:${line.length > 27 ? 16 : 18}px">${esc(line)}</text>`).join("\n")
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8"><rect class="${box}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/><rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[color]}"/><text class="${color} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:${titleSize}px">${esc(title)}</text>${body}</g>`
}

function profileColumn(x, title, color, box, lines, warning) {
  return `<g data-safe-box="${x} 335 390 420 8"><rect class="card" x="${x}" y="335" width="390" height="420" rx="28"/><rect x="${x}" y="335" width="390" height="14" rx="7" fill="${palette[color]}"/><text class="${color} label" x="${x + 195}" y="398" text-anchor="middle">${esc(title)}</text>${lines.map((line, index) => `<rect class="${box}" x="${x + 38}" y="${y = 450 + index * 75}" width="314" height="54" rx="16"/><text class="muted small" x="${x + 195}" y="${y + 34}" text-anchor="middle">${esc(line)}</text>`).join("")}<path class="thin" d="M${x + 35} 684 L${x + 355} 684"/><text class="muted small" x="${x + 195}" y="720" text-anchor="middle" style="font-size:16px">${esc(warning)}</text></g>`
}

function decoderField(x, y, title, text, color, box, width) {
  return `<g data-safe-box="${x} ${y} ${width} 145 8"><rect class="${box}" x="${x}" y="${y}" width="${width}" height="145" rx="22"/><rect x="${x}" y="${y}" width="${width}" height="10" rx="5" fill="${palette[color]}"/><text class="${color} label" x="${x + width / 2}" y="${y + 50}" text-anchor="middle" style="font-size:${title.length > 17 ? 19 : 22}px">${esc(title)}</text><path class="thin" d="M${x + 22} ${y + 72} L${x + width - 22} ${y + 72}"/><text class="muted small" x="${x + width / 2}" y="${y + 108}" text-anchor="middle" style="font-size:16px">${esc(text)}</text><path class="thin" d="M${x + 28} ${y + 123} L${x + width - 28} ${y + 123}"/></g>`
}

function note(x, y, w, text) {
  return `<g data-safe-box="${x} ${y} ${w} 70 8"><rect class="note" x="${x}" y="${y}" width="${w}" height="70" rx="24"/><text class="ink body" x="${x + w / 2}" y="${y + 44}" text-anchor="middle" style="font-weight:700;font-size:${text.length > 105 ? 18 : 20}px">${esc(text)}</text></g>`
}

function renderReadme() {
  return `# Asset M-FC05 — Capitolo 1

Figure per **Le authority viste dal candidato**, prodotte come master SVG editabili e PNG per la preview Markdown e l'export.

| File | Funzione didattica | Collocazione nel capitolo |
|---|---|---|
| \`01-mappa-bando-authority.png\` | Mappa BANDO: dal bando all'output di prova. | Dopo l'obiettivo operativo. |
| \`02-authority-settori-poteri.png\` | Panorama comparativo di enti, interessi e settori. | Dopo la mappa degli enti. |
| \`03-percorsi-g-e-p.png\` | Distinzione dei percorsi giuridico, economico-regolatorio e integrato. | Dopo la sezione sui profili. |
| \`04-nucleo-comune-delta-authority.png\` | Collegamento fra base VOL-01, delta specialistico e prova. | Dopo materie comuni e contenuti specialistici. |
| \`05-bando-decoder-authority.png\` | Scheda di lettura da compilare prima del piano di studio. | Dopo la Mappa BANDO. |

Tutti gli asset usano la gabbia 1600 × 1000 px, palette Navy/Bordeaux/Muted Gold/Green/Teal e testo Arial, in coerenza con Il Metodo BANDO e M-FC02.
`
}

function esc(value) {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;")
}

main().catch((error) => { console.error(error); process.exit(1) })
