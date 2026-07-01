const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-24"
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
    slug: "01-mappa-bando-checklist",
    title: "Mappa BANDO delle checklist",
    subtitle: "Ogni controllo collega bando, priorita, nuclei, diario e output di prova.",
    svg: figureMappaBando()
  },
  {
    slug: "02-tre-regole-checklist",
    title: "Tre regole per usare le checklist",
    subtitle: "La spunta vale solo se nasce da una verifica reale e da una decisione.",
    svg: figureRegole()
  },
  {
    slug: "03-percorso-domanda-comunicazioni",
    title: "Percorso domanda e comunicazioni",
    subtitle: "Prima scelta, invio, ricevuta e avvisi ufficiali formano un unico controllo.",
    svg: figureDomanda()
  },
  {
    slug: "04-checklist-preparazione-prove",
    title: "Preparazione delle prove",
    subtitle: "Quiz, scritto, orale e casi richiedono controlli diversi prima dell'output.",
    svg: figureProve()
  },
  {
    slug: "05-ultimi-sette-giorni-ventiquattro-ore",
    title: "Ultimi 7 giorni e ultime 24 ore",
    subtitle: "La fase finale serve a stabilizzare, non ad aprire nuovo materiale.",
    svg: figureFinale()
  },
  {
    slug: "06-logistica-ansia-tenuta",
    title: "Logistica, ansia e tenuta",
    subtitle: "Il rischio pratico si riduce con procedure, margini e istruzioni concrete.",
    svg: figureLogistica()
  },
  {
    slug: "07-checklist-unica-bando-caso-giulia",
    title: "Checklist unica BANDO: caso Giulia",
    subtitle: "Le righe non completate diventano il piano delle prossime 48 ore.",
    svg: figureGiulia()
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
  return `# Asset Capitolo 24

Figure generate per \`Checklist operative\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-bando-checklist.png\` | Mappa BANDO delle checklist come sistema di controllo. |
| \`02-tre-regole-checklist.png\` | Le tre regole d'uso: verifica, nota dubbio, criterio di stop. |
| \`03-percorso-domanda-comunicazioni.png\` | Percorso operativo da scelta concorso a piano aggiornato. |
| \`04-checklist-preparazione-prove.png\` | Controlli differenziati per quiz, scritto, orale e casi. |
| \`05-ultimi-sette-giorni-ventiquattro-ore.png\` | Timeline finale e regola delle ultime 24 ore. |
| \`06-logistica-ansia-tenuta.png\` | Rischi pratici e procedure anti-ansia da applicare. |
| \`07-checklist-unica-bando-caso-giulia.png\` | Checklist unica BANDO applicata al caso Giulia. |

I file \`.svg\` sono master vettoriali modificabili; i file \`.png\` sono le versioni inserite nel capitolo per preview Markdown ed export.
`
}

function figureMappaBando() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  ${wideCard(500, 205, 600, "Checklist come metodo", ["non memoria", "ma controllo ripetibile"], "navy", "softBlue")}
  <path class="line" d="M800 332 L800 388"/>
  <path class="line" d="M210 388 L1390 388"/>
  ${connector(210, 388, 210, 462)}
  ${connector(505, 388, 505, 575)}
  ${connector(800, 388, 800, 462)}
  ${connector(1095, 388, 1095, 575)}
  ${connector(1390, 388, 1390, 462)}
  ${stepBox(80, 462, 260, "Bando", ["requisiti", "scadenze"], "navy", "softBlue")}
  ${stepBox(375, 575, 260, "Aree", ["core", "moduli"], "bordeaux", "softRed")}
  ${stepBox(670, 462, 260, "Nuclei", ["alta resa", "ultimi giorni"], "gold", "softGold")}
  ${stepBox(965, 575, 260, "Diario", ["errori", "ansia"], "green", "softGreen")}
  ${stepBox(1260, 462, 260, "Output", ["quiz", "scritto", "orale"], "teal", "softTeal")}
  ${note(250, 812, 1100, "Se un punto e' decisivo, deve essere controllabile prima della prova.")}`

  return shell(
    "Mappa BANDO delle checklist",
    "Ogni controllo collega bando, priorita, nuclei, diario e output di prova.",
    inner
  )
}

function figureRegole() {
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Una checklist utile non tranquillizza: impedisce dimenticanze evitabili</text>
  ${ruleCard(140, 315, "1", "Spunta verificata", ["fonte affidabile", "bando, avviso, ricevuta"], "navy", "softBlue")}
  <path class="arrowNavy" d="M475 420 L565 420"/>
  ${ruleCard(615, 315, "2", "Nota il dubbio", ["scrivi fonte", "e scadenza di controllo"], "bordeaux", "softRed")}
  <path class="arrowNavy" d="M950 420 L1040 420"/>
  ${ruleCard(1090, 315, "3", "Criterio stop", ["se e' essenziale", "fermati e verifica"], "green", "softGreen")}
  ${mini(250, 640, 330, "Non spuntare", "per memoria o fiducia", palette.bordeaux)}
  ${mini(635, 640, 330, "Scrivi", "dubbio, fonte, entro quando", palette.navy)}
  ${mini(1020, 640, 330, "Procedi", "solo dopo verifica", palette.green)}
  ${note(250, 812, 1100, "La spunta e' una decisione documentata, non un gesto automatico.")}`

  return shell(
    "Tre regole per usare le checklist",
    "La spunta vale solo se nasce da una verifica reale e da una decisione.",
    inner
  )
}

function figureDomanda() {
  const steps = [
    ["1", "Scegli", "requisiti e prove", "navy", "softBlue"],
    ["2", "Invia", "dati e allegati", "bordeaux", "softRed"],
    ["3", "Salva", "ricevuta e protocollo", "gold", "softGold"],
    ["4", "Controlla", "avvisi ufficiali", "green", "softGreen"],
    ["5", "Aggiorna", "piano e diario", "teal", "softTeal"]
  ]

  const cards = steps
    .map(([num, title, body, color, box], index) => flowCard(110 + index * 295, 335, num, title, body, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">La domanda e' una fase amministrativa: non una formalita</text>
  ${cards}
  <path class="arrowNavy" d="M320 435 L395 435"/>
  <path class="arrowNavy" d="M615 435 L690 435"/>
  <path class="arrowNavy" d="M910 435 L985 435"/>
  <path class="arrowNavy" d="M1205 435 L1280 435"/>
  ${wideCard(310, 635, 980, "Criterio di stop", ["non inviare senza scadenza, requisiti, dati, allegati, pagamento e ricevuta"], "bordeaux", "softRed")}
  ${note(250, 812, 1100, "Dopo l'invio non si aspetta soltanto: si controllano comunicazioni e calendario.")}`

  return shell(
    "Percorso domanda e comunicazioni",
    "Prima scelta, invio, ricevuta e avvisi ufficiali formano un unico controllo.",
    inner
  )
}

function figureProve() {
  const cards = [
    ["Quiz", ["timer", "penalita", "regola salto"], "navy", "softBlue"],
    ["Scritto", ["scaletta", "tempo", "struttura"], "bordeaux", "softRed"],
    ["Orale", ["2 minuti", "definizione", "collegamenti"], "gold", "softGold"],
    ["Casi", ["fatti", "competenza", "decisione"], "green", "softGreen"]
  ]

  const body = cards
    .map(([title, lines, color, box], index) => proofCard(170 + index * 315, 300, title, lines, color, box))
    .join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">La preparazione finale deve assomigliare alla prova reale</text>
  ${body}
  ${wideCard(290, 590, 460, "Controlli comuni", ["formato, durata, soglie", "strumenti ammessi"], "navy", "softBlue")}
  ${wideCard(850, 590, 460, "Correzione", ["errori ad alta resa", "diario aggiornato"], "green", "softGreen")}
  <path class="arrowNavy" d="M760 660 L840 660"/>
  ${note(250, 812, 1100, "Senza simulazione, la checklist misura intenzioni: con simulazione misura dati.")}`

  return shell(
    "Preparazione delle prove",
    "Quiz, scritto, orale e casi richiedono controlli diversi prima dell'output.",
    inner
  )
}

function figureFinale() {
  const days = [
    ["-7", "simulazione", "correzione"],
    ["-6", "errori", "flashcard"],
    ["-5", "core", "domande brevi"],
    ["-4", "prova parziale", "timer"],
    ["-3", "documenti", "logistica"],
    ["-2", "routine", "ripasso leggero"],
    ["-1", "sonno", "materiale"]
  ]

  const rows = days.map((row, index) => dayRow(165, 270 + index * 54, 690, row, index)).join("\n")

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Gli ultimi giorni servono a ridurre rischio e rumore</text>
  <g data-safe-box="165 270 690 378 8">
    ${rows}
  </g>
  ${finalBox(965, 285, "Ultime 24 ore", ["documento", "convocazione", "percorso", "sveglie", "schede brevi"], "bordeaux", "softRed")}
  ${finalBox(965, 560, "Non fare", ["manuale nuovo", "metodo nuovo", "studio pesante", "chat al posto fonti"], "green", "softGreen")}
  ${note(250, 812, 1100, "Nella fase finale vinci stabilizzando: non aumentando volume all'ultimo minuto.")}`

  return shell(
    "Ultimi 7 giorni e ultime 24 ore",
    "La fase finale serve a stabilizzare, non ad aprire nuovo materiale.",
    inner
  )
}

function figureLogistica() {
  const left = [
    ["Identita", "documento valido"],
    ["Convocazione", "data, ora, sede"],
    ["Accesso", "percorso e margine"],
    ["Materiali", "solo ammessi"],
    ["Divieti", "telefono, testi, strumenti"]
  ]
  const right = [
    ["Prima prova", "arriva con margine"],
    ["Inizio", "leggi istruzioni"],
    ["Difficile", "segna e salta"],
    ["Vuoto orale", "definizione e funzione"],
    ["Tempo", "priorita e punti probabili"]
  ]

  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">L'ansia si gestisce con procedure, non con frasi vaghe</text>
  ${listPanel(145, 290, 590, "Rischi pratici", left, "navy", "softBlue")}
  ${listPanel(865, 290, 590, "Procedure di tenuta", right, "bordeaux", "softRed")}
  <path class="arrowNavy" d="M755 500 L845 500"/>
  ${mini(275, 700, 330, "Verifica", "bando e avviso decidono", palette.navy)}
  ${mini(635, 700, 330, "Riduci", "margini, percorso, materiali", palette.green)}
  ${mini(995, 700, 330, "Esegui", "istruzioni concrete", palette.bordeaux)}
  ${note(250, 812, 1100, "Se un oggetto non e' chiaramente ammesso, non darlo per ammesso.")}`

  return shell(
    "Logistica, ansia e tenuta",
    "Il rischio pratico si riduce con procedure, margini e istruzioni concrete.",
    inner
  )
}

function figureGiulia() {
  const rows = [
    ["B", "Bando", "sede non verificata", "controlla percorso"],
    ["A", "Aree", "core e modulo ok", "mantieni priorita"],
    ["N", "Nuclei", "accesso e Comune", "ripasso mirato"],
    ["D", "Diario", "negazioni nei quiz", "drill parole-spia"],
    ["O", "Output", "orale troppo lungo", "3 risposte da 2 min"]
  ]

  const body = rows.map((row, index) => bandoRow(180, 270 + index * 82, 1240, row, index)).join("\n")
  const inner = `
  <rect class="card" x="70" y="165" width="1460" height="630" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Caso Giulia: ogni riga incompleta genera una prossima azione</text>
  <g data-safe-box="180 270 1240 410 8">
    ${body}
  </g>
  ${note(250, 765, 1100, "Se una riga BANDO resta vuota, quella e' la prossima azione entro 48 ore.")}`

  return shell(
    "Checklist unica BANDO: caso Giulia",
    "Le righe non completate diventano il piano delle prossime 48 ore.",
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

function ruleCard(x, y, number, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 175}" y="${y + 112 + index * 30}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 350 210 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="350" height="210" rx="26"/>
    <circle cx="${x + 175}" cy="${y + 52}" r="33" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 175}" y="${y + 63}" text-anchor="middle" fill="#FFFFFF" style="font-size:23px">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 175}" y="${y + 88}" text-anchor="middle" style="font-size:21px">${esc(title)}</text>
    ${body}
  </g>`
}

function flowCard(x, y, number, title, body, colorClass, boxClass) {
  return `<g data-safe-box="${x} ${y} 205 205 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="205" height="205" rx="24"/>
    <circle cx="${x + 102.5}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 102.5}" y="${y + 52}" text-anchor="middle" fill="#FFFFFF" style="font-size:20px">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 102.5}" y="${y + 94}" text-anchor="middle" style="font-size:20px">${esc(title)}</text>
    <text class="muted small" x="${x + 102.5}" y="${y + 145}" text-anchor="middle" style="font-size:15px">${esc(body)}</text>
  </g>`
}

function proofCard(x, y, title, lines, colorClass, boxClass) {
  const rows = lines
    .map((line, index) => `<text class="muted small" x="${x + 135}" y="${y + 112 + index * 34}" text-anchor="middle" style="font-size:16px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 270 225 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="270" height="225" rx="24"/>
    <rect x="${x}" y="${y}" width="270" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 135}" y="${y + 54}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    <path class="thin" d="M${x + 45} ${y + 76} L${x + 225} ${y + 76}"/>
    ${rows}
  </g>`
}

function dayRow(x, y, w, row, index) {
  const [day, action, focus] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  return `<g>
    <rect x="${x}" y="${y}" width="${w}" height="46" rx="12" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <text class="navy label" x="${x + 45}" y="${y + 31}" text-anchor="middle" style="font-size:18px">${esc(day)}</text>
    <text class="muted small" x="${x + 225}" y="${y + 31}" text-anchor="middle" style="font-size:16px">${esc(action)}</text>
    <text class="bordeaux label" x="${x + 515}" y="${y + 31}" text-anchor="middle" style="font-size:16px">${esc(focus)}</text>
  </g>`
}

function finalBox(x, y, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 235}" y="${y + 92 + index * 27}" text-anchor="middle" style="font-size:15px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 470 220 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="470" height="220" rx="26"/>
    <rect x="${x}" y="${y}" width="470" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + 235}" y="${y + 52}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${body}
  </g>`
}

function listPanel(x, y, w, title, rows, colorClass, boxClass) {
  const body = rows
    .map(([label, value], index) => {
      const yy = y + 88 + index * 48
      return `<g>
        <text class="${colorClass} label" x="${x + 115}" y="${yy}" text-anchor="middle" style="font-size:16px">${esc(label)}</text>
        <text class="muted small" x="${x + 355}" y="${yy}" text-anchor="middle" style="font-size:16px">${esc(value)}</text>
      </g>`
    })
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 355 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="355" rx="26"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 47}" text-anchor="middle" style="font-size:23px">${esc(title)}</text>
    ${body}
  </g>`
}

function bandoRow(x, y, w, row, index) {
  const [letter, label, gap, action] = row
  const fill = index % 2 === 0 ? palette.blueSoft : palette.white
  const colors = [palette.navy, palette.bordeaux, palette.gold, palette.green, palette.teal]
  return `<g data-safe-box="${x} ${y} ${w} 70 8">
    <rect x="${x}" y="${y}" width="${w}" height="70" rx="16" fill="${fill}" stroke="${palette.border}" stroke-width="2"/>
    <circle cx="${x + 55}" cy="${y + 35}" r="25" fill="${colors[index]}"/>
    <text class="label" x="${x + 55}" y="${y + 44}" text-anchor="middle" fill="#FFFFFF" style="font-size:20px">${esc(letter)}</text>
    <text class="navy label" x="${x + 175}" y="${y + 43}" text-anchor="middle" style="font-size:18px">${esc(label)}</text>
    <text class="muted small" x="${x + 510}" y="${y + 43}" text-anchor="middle" style="font-size:16px">${esc(gap)}</text>
    <text class="green label" x="${x + 925}" y="${y + 43}" text-anchor="middle" style="font-size:16px">${esc(action)}</text>
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 17 ? 17 : 20
  const bodyFontSize = body.length > 31 ? 14 : 16
  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
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
