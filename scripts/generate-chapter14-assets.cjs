const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-14"
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
    slug: "01-mappa-operativa-prova-quiz",
    title: "Mappa operativa della prova a quiz",
    subtitle: "Il punteggio nasce da bando, tempo, rischio, distrattori e correzione degli errori.",
    svg: figureMappa()
  },
  {
    slug: "02-banca-dati-albero-decisionale",
    title: "Banca dati o no: albero decisionale",
    subtitle: "La presenza della banca dati cambia il piano: copertura completa o nuclei e tipologie.",
    svg: figureBancaDati()
  },
  {
    slug: "03-scheda-tecnica-prova",
    title: "Scheda tecnica della prova",
    subtitle: "Prima di allenarti devi conoscere tempo medio, soglia, punteggio e penalita.",
    svg: figureSchedaTecnica()
  },
  {
    slug: "04-banca-dati-quattro-passaggi",
    title: "Metodo con banca dati in quattro passaggi",
    subtitle: "Copertura, errori, consolidamento e simulazione trasformano domande in competenza.",
    svg: figureQuattroPassaggi()
  },
  {
    slug: "05-routine-tre-giri",
    title: "Routine dei tre giri in prova",
    subtitle: "Prima proteggi i punti rapidi, poi lavori le domande segnate e chiudi il rischio.",
    svg: figureTreGiri()
  },
  {
    slug: "06-anatomia-del-distrattore",
    title: "Anatomia del distrattore",
    subtitle: "Le opzioni quasi vere si riconoscono da assoluti, inversioni e risposte fuori domanda.",
    svg: figureDistrattori()
  },
  {
    slug: "07-dal-punteggio-al-diario-errori",
    title: "Dal punteggio al diario errori",
    subtitle: "La simulazione vale solo se produce categorie di errore, drill mirato e nuova decisione.",
    svg: figureDiario()
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
  return `# Asset Capitolo 14

Figure generate per \`La prova a quiz\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-operativa-prova-quiz.png\` | Mappa generale: bando, aree, nuclei, diario, output, tempo, rischio e correzione. |
| \`02-banca-dati-albero-decisionale.png\` | Albero decisionale per banca dati ufficiale, assente, promessa o prova mista. |
| \`03-scheda-tecnica-prova.png\` | Cruscotto della prova: domande, tempo, soglia, punteggi, penalita e modalita. |
| \`04-banca-dati-quattro-passaggi.png\` | Metodo di studio con banca dati: copertura, errori, consolidamento, simulazione. |
| \`05-routine-tre-giri.png\` | Gestione della prova con tre giri e soglia di abbandono. |
| \`06-anatomia-del-distrattore.png\` | Segnali dei distrattori ricorrenti nelle risposte multiple. |
| \`07-dal-punteggio-al-diario-errori.png\` | Dalla simulazione al diario errori, con drill e prossima decisione. |

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
      .dash { stroke: ${palette.line}; stroke-width: 3.5; stroke-linecap: round; stroke-dasharray: 9 10; fill: none; }
      .arrowNavy { stroke: ${palette.navy}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowNavy); }
      .arrowBordeaux { stroke: ${palette.bordeaux}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowBordeaux); }
      .arrowGold { stroke: ${palette.gold}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGold); }
      .arrowGreen { stroke: ${palette.green}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowGreen); }
      .arrowTeal { stroke: ${palette.teal}; stroke-width: 5; stroke-linecap: round; fill: none; marker-end: url(#arrowTeal); }
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
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.green}"/>
    </marker>
    <marker id="arrowTeal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${palette.teal}"/>
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
  ${card(575, 170, 450, 125, "Prova a quiz", ["rapidita e precisione", "gestione rischio"], "navy", "card")}
  <path class="line" d="M800 295 L800 365"/>
  <path class="line" d="M210 365 L1390 365"/>
  ${connector(210, 365, 210, 450)}
  ${connector(505, 365, 505, 570)}
  ${connector(800, 365, 800, 450)}
  ${connector(1095, 365, 1095, 570)}
  ${connector(1390, 365, 1390, 450)}
  ${card(75, 450, 270, 130, "Bando", ["quesiti, tempo", "soglia, penalita"], "navy", "softBlue")}
  ${card(370, 570, 270, 130, "Aree", ["materie", "pesi e priorita"], "bordeaux", "softRed")}
  ${card(665, 450, 270, 130, "Nuclei", ["definizioni", "eccezioni, confronti"], "gold", "softGold")}
  ${card(960, 570, 270, 130, "Diario", ["memoria, concetto", "lettura, tempo"], "green", "softGreen")}
  ${card(1255, 450, 270, 130, "Output", ["drill, batterie", "simulazioni"], "teal", "softTeal")}
  ${note(250, 792, 1100, "Non basta fare domande: ogni quiz deve produrre tempo misurato, errore corretto e prossima decisione.")}
`
  return shell(
    "Mappa operativa della prova a quiz",
    "Il punteggio nasce da bando, tempo, rischio, distrattori e correzione degli errori.",
    inner
  )
}

function figureBancaDati() {
  const inner = `
  <rect class="card" x="95" y="165" width="1410" height="630" rx="30"/>
  ${card(565, 205, 470, 105, "Il bando prevede banca dati?", ["controlla avviso, allegati e diario prova"], "navy", "softBlue")}
  <path class="arrowNavy" d="M690 315 C560 365 405 400 305 445"/>
  <path class="arrowBordeaux" d="M795 315 L795 435"/>
  <path class="arrowGold" d="M910 315 C1035 365 1185 400 1295 445"/>
  ${listCard(130, 450, 350, "Si, pubblicata", ["copri tutte le domande", "spiega alternative", "ripeti errori e incerte"], "green", "softGreen")}
  ${listCard(625, 440, 350, "No", ["studia nuclei", "allena tipologie", "simula domande nuove"], "bordeaux", "softRed")}
  ${listCard(1120, 450, 350, "Promessa o mista", ["prepara base comune", "tieni calendario elastico", "separa gli output"], "gold", "softGold")}
  <path class="arrowGreen" d="M305 650 C480 735 1065 735 1295 650"/>
  ${mini(500, 690, 600, "Decisione finale", "scegli copertura, drill o simulazione in base allo scenario", palette.navy)}
  ${note(250, 812, 1100, "Regola: non applicare il metodo banca dati a una prova senza banca dati, e viceversa.")}
`
  return shell(
    "Banca dati o no: albero decisionale",
    "La presenza della banca dati cambia il piano: copertura completa o nuclei e tipologie.",
    inner
  )
}

function figureSchedaTecnica() {
  const cells = [
    ["Domande", "quante e di che tipo", "navy", "softBlue"],
    ["Tempo", "medio e soglia stop", "bordeaux", "softRed"],
    ["Materie", "peso e priorita", "gold", "softGold"],
    ["Punteggi", "corretta, errata, omessa", "green", "softGreen"],
    ["Soglia", "idoneita e graduatoria", "teal", "softTeal"],
    ["Banca dati", "si, no, promessa", "navy", "softBlue"],
    ["Modalita", "digitale o cartacea", "bordeaux", "softRed"],
    ["Ritorno", "si puo tornare indietro?", "gold", "softGold"]
  ]
  const cards = cells
    .map(([title, body, color, box], index) => {
      const col = index % 4
      const row = Math.floor(index / 4)
      return card(115 + col * 365, 255 + row * 190, 320, 130, title, [body], color, box)
    })
    .join("\n")
  const inner = `
  <rect class="card" x="80" y="170" width="1440" height="625" rx="30"/>
  <text class="navy label" x="800" y="225" text-anchor="middle">Compila questi dati prima di fare la prima simulazione</text>
  ${cards}
  ${mini(310, 665, 270, "60 domande", "dato grezzo", palette.navy)}
  ${mini(665, 665, 270, "60 minuti", "vincolo reale", palette.bordeaux)}
  ${mini(1020, 665, 270, "1 minuto", "tempo teorico", palette.green)}
  ${note(250, 812, 1100, "Il tempo medio e' teorico: una domanda facile non deve finanziare una domanda bloccante.")}
`
  return shell(
    "Scheda tecnica della prova",
    "Prima di allenarti devi conoscere tempo medio, soglia, punteggio e penalita.",
    inner
  )
}

function figureQuattroPassaggi() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">La banca dati si studia a giri, non in una sola lettura</text>
  ${stepCard(145, 315, "1", "Copertura", ["vedi tutto", "segna ignoti"], "navy", "softBlue")}
  ${stepCard(470, 315, "2", "Errori", ["capisci perche", "classifica"], "bordeaux", "softRed")}
  ${stepCard(795, 315, "3", "Consolida", ["velocizza corrette", "ripeti incerte"], "gold", "softGold")}
  ${stepCard(1120, 315, "4", "Simula", ["timer reale", "correzione finale"], "green", "softGreen")}
  <path class="arrowNavy" d="M410 405 L455 405"/>
  <path class="arrowBordeaux" d="M735 405 L780 405"/>
  <path class="arrowGold" d="M1060 405 L1105 405"/>
  <path class="dash" d="M1265 540 C1080 690 525 695 290 542"/>
  ${listCard(215, 615, 360, "Da non fare", ["memorizzare posizione", "saltare correzione", "simulare troppo presto"], "bordeaux", "softRed")}
  ${listCard(1025, 615, 360, "Risultato atteso", ["punteggio stabile", "tempi sotto controllo", "errori sempre meno casuali"], "green", "softGreen")}
`
  return shell(
    "Metodo con banca dati in quattro passaggi",
    "Copertura, errori, consolidamento e simulazione trasformano domande in competenza.",
    inner
  )
}

function figureTreGiri() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Ogni giro ha una funzione diversa</text>
  <path class="line" d="M180 445 L1420 445"/>
  ${timelinePoint(275, 445, "1", "Punti rapidi", "rispondi sicure", palette.navy)}
  ${timelinePoint(680, 445, "2", "Lavorabili", "torna sui segnati", palette.gold)}
  ${timelinePoint(1090, 445, "3", "Rischio", "decidi con penalita", palette.bordeaux)}
  ${timelinePoint(1375, 445, "Fine", "controllo", "consegna", palette.green)}
  ${listCard(130, 610, 365, "Salta se", ["non capisci subito", "calcolo non parte", "brano da rileggere troppo"], "navy", "softBlue")}
  ${listCard(615, 610, 365, "Torna se", ["hai due opzioni", "serve solo calcolo", "hai recuperato indizio"], "gold", "softGold")}
  ${listCard(1100, 610, 365, "Rispondi se", ["penalita sostenibile", "plausibilita alta", "tempo residuo sufficiente"], "green", "softGreen")}
  ${note(250, 812, 1100, "Una domanda difficile non deve rubare il tempo a cinque domande facili.")}
`
  return shell(
    "Routine dei tre giri in prova",
    "Prima proteggi i punti rapidi, poi lavori le domande segnate e chiudi il rischio.",
    inner
  )
}

function figureDistrattori() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  ${card(565, 205, 470, 120, "Risposta quasi vera", ["sembra corretta", "ma non risponde esattamente"], "navy", "card")}
  <path class="line" d="M800 325 L800 385"/>
  <path class="line" d="M250 385 L1350 385"/>
  ${connector(250, 385, 250, 465)}
  ${connector(470, 385, 470, 590)}
  ${connector(690, 385, 690, 465)}
  ${connector(910, 385, 910, 590)}
  ${connector(1130, 385, 1130, 465)}
  ${connector(1350, 385, 1350, 590)}
  ${card(115, 465, 270, 115, "Assoluto", ["sempre, mai", "tutti, nessuno"], "bordeaux", "softRed")}
  ${card(335, 590, 270, 115, "Inversione", ["causa effetto", "regola eccezione"], "navy", "softBlue")}
  ${card(555, 465, 270, 115, "Termine simile", ["parola vicina", "istituto diverso"], "gold", "softGold")}
  ${card(775, 590, 270, 115, "Mezza verita", ["corretta in parte", "ma incompleta"], "green", "softGreen")}
  ${card(995, 465, 270, 115, "Fuori domanda", ["vera in se", "non richiesta"], "teal", "softTeal")}
  ${card(1215, 590, 270, 115, "Dato inutile", ["numero presente", "ma irrilevante"], "bordeaux", "softRed")}
  ${note(250, 812, 1100, "Allenati a spiegare perche le alternative sbagliate sono sbagliate.")}
`
  return shell(
    "Anatomia del distrattore",
    "Le opzioni quasi vere si riconoscono da assoluti, inversioni e risposte fuori domanda.",
    inner
  )
}

function figureDiario() {
  const inner = `
  <rect class="card" x="90" y="165" width="1420" height="630" rx="30"/>
  <text class="navy label" x="800" y="228" text-anchor="middle">Il punteggio e' un risultato; il diario spiega il processo</text>
  ${processCard(130, 330, 250, "Simulazione", ["timer", "numero reale"], "navy", "softBlue")}
  ${processCard(420, 330, 250, "Punteggio", ["corrette", "errate, omesse"], "bordeaux", "softRed")}
  ${processCard(710, 330, 250, "Categorie", ["memoria, concetto", "lettura, tempo"], "gold", "softGold")}
  ${processCard(1000, 330, 250, "Drill", ["15-30 minuti", "una causa"], "green", "softGreen")}
  ${processCard(1290, 330, 180, "Prossima", ["regola", "test"], "teal", "softTeal")}
  <path class="arrowNavy" d="M390 410 L410 410"/>
  <path class="arrowBordeaux" d="M680 410 L700 410"/>
  <path class="arrowGold" d="M970 410 L990 410"/>
  <path class="arrowGreen" d="M1260 410 L1280 410"/>
  ${mini(190, 635, 200, "Memoria", "flashcard", palette.navy)}
  ${mini(440, 635, 200, "Concetto", "tabella", palette.bordeaux)}
  ${mini(690, 635, 200, "Lettura", "routine lenta", palette.gold)}
  ${mini(940, 635, 200, "Tempo", "soglia stop", palette.green)}
  ${mini(1190, 635, 200, "Strategia", "tre giri", palette.teal)}
  ${note(250, 812, 1100, "Una simulazione senza correzione e' consumo di domande, non allenamento.")}
`
  return shell(
    "Dal punteggio al diario errori",
    "La simulazione vale solo se produce categorie di errore, drill mirato e nuova decisione.",
    inner
  )
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleFontSize = title.length > 25 ? 18 : title.length > 19 ? 20 : title.length > 14 ? 22 : 25
  const bodyFontSize = lines.some((line) => line.length > 25) ? 16 : 18
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 74 + index * 25}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function listCard(x, y, w, title, lines, colorClass, boxClass) {
  const rowHeight = 31
  const h = 88 + lines.length * rowHeight
  const titleFontSize = title.length > 22 ? 19 : title.length > 16 ? 21 : 24
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 30}" y="${y + 80 + index * rowHeight}" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 24} ${y + 60} L${x + w - 24} ${y + 60}"/>
    ${body}
  </g>`
}

function stepCard(x, y, number, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 145}" y="${y + 92 + index * 27}" text-anchor="middle">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} 290 210 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="290" height="210" rx="24"/>
    <circle cx="${x + 145}" cy="${y + 42}" r="28" fill="${palette[colorClass]}"/>
    <text class="label" x="${x + 145}" y="${y + 51}" text-anchor="middle" fill="#FFFFFF">${esc(number)}</text>
    <text class="${colorClass} label" x="${x + 145}" y="${y + 78}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    ${body}
  </g>`
}

function processCard(x, y, w, title, lines, colorClass, boxClass) {
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 78 + index * 27}" text-anchor="middle" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 160 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="160" rx="22"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 42}" text-anchor="middle" style="font-size:22px">${esc(title)}</text>
    ${body}
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 21 ? 18 : title.length > 15 ? 19 : 21
  const bodyFontSize = body.length > 30 ? 14 : 16

  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 31}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function timelinePoint(x, y, number, title, subtitle, color) {
  return `<g data-safe-box="${x - 120} ${y - 120} 240 215 8">
    <circle cx="${x}" cy="${y}" r="36" fill="${color}"/>
    <text class="label" x="${x}" y="${y + 9}" text-anchor="middle" fill="#FFFFFF" style="font-size:24px">${esc(number)}</text>
    <text class="label" x="${x}" y="${y - 70}" text-anchor="middle" fill="${color}" style="font-size:22px">${esc(title)}</text>
    <text class="muted small" x="${x}" y="${y + 78}" text-anchor="middle" style="font-size:16px">${esc(subtitle)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 102 ? 18 : text.length > 86 ? 19 : 20

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
