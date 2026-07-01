const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const OUTPUT_DIR = path.join(
  process.cwd(),
  "wiki",
  "books",
  "il-metodo-bando",
  "assets",
  "chapter-12"
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
    slug: "01-mappa-logica-comprensione-ragionamento",
    title: "Logica, comprensione e ragionamento",
    subtitle: "La prova premia lettura precisa, classificazione rapida e controllo dell'errore.",
    svg: figureMappa()
  },
  {
    slug: "02-classifica-prima-di-risolvere",
    title: "Classifica prima di risolvere",
    subtitle: "Ogni famiglia di quesiti richiede uno strumento diverso.",
    svg: figureClassifica()
  },
  {
    slug: "03-parole-logiche-decisive",
    title: "Le parole logiche decisive",
    subtitle: "Negazioni, quantificatori e condizioni cambiano la risposta corretta.",
    svg: figureParoleLogiche()
  },
  {
    slug: "04-vincoli-serie-pattern",
    title: "Vincoli, serie e pattern",
    subtitle: "Trasforma informazioni sparse in blocchi, griglie e regole controllabili.",
    svg: figureVincoliSerie()
  },
  {
    slug: "05-testo-argomento-evidenza",
    title: "Testo e argomento: cercare evidenza",
    subtitle: "La risposta deve essere supportata dal brano o dalle premesse, non solo plausibile.",
    svg: figureTestoArgomento()
  },
  {
    slug: "06-ragionamento-numerico-rapido",
    title: "Ragionamento numerico rapido",
    subtitle: "Percentuali, proporzioni e tabelle richiedono base corretta e controllo di scala.",
    svg: figureNumerico()
  },
  {
    slug: "07-tempo-esclusione-diario-errori",
    title: "Tempo, esclusione e diario errori",
    subtitle: "Il punteggio cresce quando sai saltare, tornare e correggere per categoria.",
    svg: figureTempoDiario()
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
  return `# Asset Capitolo 12

Figure generate per \`Logica, comprensione del testo e ragionamento\`.

| File | Funzione didattica |
|---|---|
| \`01-mappa-logica-comprensione-ragionamento.png\` | Mappa generale: brani, deduzioni, vincoli, serie, calcoli, argomenti, tempo e diario errori. |
| \`02-classifica-prima-di-risolvere.png\` | Routine di classificazione del quesito e scelta dello strumento. |
| \`03-parole-logiche-decisive.png\` | Connettivi, quantificatori e condizioni necessarie/sufficienti. |
| \`04-vincoli-serie-pattern.png\` | Metodo per vincoli, ordinamenti, griglie e pattern numerici/alfabetici. |
| \`05-testo-argomento-evidenza.png\` | Comprensione del testo e ragionamento critico basati su evidenza, premesse e assunzioni. |
| \`06-ragionamento-numerico-rapido.png\` | Percentuali, proporzioni, tabelle e controllo di plausibilita. |
| \`07-tempo-esclusione-diario-errori.png\` | Gestione a piu giri, esclusione razionale e diario degli errori. |

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
      .title { font-size: 44px; font-weight: 800; letter-spacing: 0; }
      .subtitle { font-size: 23px; }
      .label { font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; font-size: 25px; font-weight: 800; }
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
  ${card(555, 180, 490, 145, "Prova attitudinale", ["tempo stretto", "opzioni simili"], "navy", "card")}
  <path class="line" d="M800 325 L800 388"/>
  <path class="line" d="M245 388 L1355 388"/>
  ${connector(245, 388, 245, 450)}
  ${connector(467, 388, 467, 575)}
  ${connector(689, 388, 689, 450)}
  ${connector(911, 388, 911, 575)}
  ${connector(1133, 388, 1133, 450)}
  ${connector(1355, 388, 1355, 575)}
  ${card(105, 450, 280, 130, "Brano", ["evidenza", "non impressione"], "navy", "softBlue")}
  ${card(327, 575, 280, 130, "Deduzione", ["se, solo se", "tutti, alcuni"], "bordeaux", "softRed")}
  ${card(549, 450, 280, 130, "Vincoli", ["griglia", "casi possibili"], "gold", "softGold")}
  ${card(771, 575, 280, 130, "Serie", ["regola semplice", "alternanza"], "green", "softGreen")}
  ${card(993, 450, 280, 130, "Numerico", ["base corretta", "scala"], "teal", "softTeal")}
  ${card(1215, 575, 280, 130, "Argomento", ["premesse", "assunzione"], "bordeaux", "softRed")}
  ${note(250, 795, 1100, "Routine unica: classifica, scegli lo strumento, risolvi, controlla, registra l'errore.")}
`
  return shell("Logica, comprensione e ragionamento", "La prova premia lettura precisa, classificazione rapida e controllo dell'errore.", inner)
}

function figureClassifica() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Prima domanda mentale: che tipo di quesito ho davanti?</text>
  ${flowCard(135, 310, 250, "Brano", ["cerca prova nel testo", "segna parole assolute"], "navy", "softBlue")}
  ${flowCard(430, 310, 250, "Premesse", ["traduci in regole", "controlla necessita"], "bordeaux", "softRed")}
  ${flowCard(725, 310, 250, "Vincoli", ["disegna griglia", "parti dai certi"], "gold", "softGold")}
  ${flowCard(1020, 310, 250, "Calcolo", ["trova base", "stima il risultato"], "green", "softGreen")}
  ${flowCard(1315, 310, 150, "Serie", ["regola", "salta"], "teal", "softTeal")}
  <path class="arrowNavy" d="M390 382 L415 382"/>
  <path class="arrowBordeaux" d="M685 382 L710 382"/>
  <path class="arrowGold" d="M980 382 L1005 382"/>
  <path class="arrowGreen" d="M1275 382 L1300 382"/>
  ${stepCard(150, 560, ["1", "Capisco", "domanda reale"], 230)}
  ${stepCard(430, 560, ["2", "Separo", "dati e distrattori"], 230)}
  ${stepCard(710, 560, ["3", "Applico", "schema o calcolo"], 230)}
  ${stepCard(990, 560, ["4", "Controllo", "tutti i vincoli"], 230)}
  ${stepCard(1270, 560, ["5", "Decido", "rispondo o salto"], 230)}
  ${note(250, 805, 1100, "Le opzioni servono per controllare: non devono guidare la prima lettura.")}
`
  return shell("Classifica prima di risolvere", "Ogni famiglia di quesiti richiede uno strumento diverso.", inner)
}

function figureParoleLogiche() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Piccole parole, grande differenza di risposta</text>
  ${listCard(135, 300, 300, "Connettivi", ["non A = A escluso", "A e B = entrambi", "A o B = almeno uno", "o A o B = uno solo"], "navy", "softBlue")}
  ${listCard(485, 300, 300, "Condizioni", ["se A allora B", "A sufficiente per B", "solo se B: B necessario", "non invertire la freccia"], "bordeaux", "softRed")}
  ${listCard(835, 300, 300, "Quantificatori", ["tutti = ogni caso", "nessuno = zero casi", "alcuni = almeno uno", "non tutti = almeno uno no"], "gold", "softGold")}
  ${listCard(1185, 300, 300, "Negazioni", ["tutti -> almeno uno no", "nessuno -> almeno uno si", "alcuni -> nessuno", "esattamente uno -> zero o piu"], "green", "softGreen")}
  ${mini(245, 650, 330, "A -> B", "se A, allora B", palette.navy)}
  ${mini(635, 650, 330, "non B -> non A", "contrapposizione", palette.bordeaux)}
  ${mini(1025, 650, 330, "B -> A?", "inversione non valida", palette.green)}
  ${note(250, 805, 1100, "Quando leggi 'solo se', fermati: indica una condizione necessaria, non sempre sufficiente.")}
`
  return shell("Le parole logiche decisive", "Negazioni, quantificatori e condizioni cambiano la risposta corretta.", inner)
}

function figureVincoliSerie() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Dalla frase alla struttura controllabile</text>
  ${card(135, 315, 275, 120, "Elementi", ["persone, uffici", "giorni, ruoli"], "navy", "softBlue")}
  ${card(475, 315, 275, 120, "Vincoli certi", ["non prima", "subito dopo"], "bordeaux", "softRed")}
  ${card(815, 315, 275, 120, "Struttura", ["linea", "tabella, griglia"], "gold", "softGold")}
  ${card(1155, 315, 275, 120, "Casi", ["prova e scarta", "controlla tutto"], "green", "softGreen")}
  <path class="arrowNavy" d="M420 375 L460 375"/>
  <path class="arrowBordeaux" d="M760 375 L800 375"/>
  <path class="arrowGold" d="M1100 375 L1140 375"/>
  ${mini(160, 555, 260, "B-C", "blocca subito prima", palette.bordeaux)}
  ${mini(480, 555, 260, "1 2 3 4", "linea posizioni", palette.navy)}
  ${mini(800, 555, 260, "+4 +8 +16", "serie numerica", palette.gold)}
  ${mini(1120, 555, 260, "+2 +3 +4", "serie alfabetica", palette.green)}
  <path class="dash" d="M290 520 C430 485 545 495 610 545"/>
  <path class="dash" d="M930 520 C1020 490 1125 495 1245 545"/>
  ${note(250, 805, 1100, "Se la griglia non parte entro pochi secondi, segna la domanda e proteggi il tempo.")}
`
  return shell("Vincoli, serie e pattern", "Trasforma informazioni sparse in blocchi, griglie e regole controllabili.", inner)
}

function figureTestoArgomento() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Non basta che una risposta sembri ragionevole</text>
  ${card(135, 315, 300, 130, "Dato esplicito", ["parole presenti", "riga o frase"], "navy", "softBlue")}
  ${card(485, 315, 300, 130, "Inferenza", ["supportata", "senza ipotesi esterne"], "bordeaux", "softRed")}
  ${card(835, 315, 300, 130, "Argomento", ["premessa", "conclusione"], "gold", "softGold")}
  ${card(1185, 315, 300, 130, "Assunzione", ["ponte nascosto", "causa alternativa"], "green", "softGreen")}
  <path class="arrowNavy" d="M445 380 L470 380"/>
  <path class="arrowBordeaux" d="M795 380 L820 380"/>
  <path class="arrowGold" d="M1145 380 L1170 380"/>
  ${listCard(165, 555, 390, "Opzioni sospette", ["tutti, sempre, solo, mai", "affermazione troppo ampia", "dettaglio vero ma irrilevante"], "bordeaux", "softRed")}
  ${listCard(620, 555, 390, "Controllo", ["dove lo dice il testo?", "segue necessariamente?", "serve una ipotesi esterna?"], "navy", "softBlue")}
  ${listCard(1075, 555, 390, "Critico", ["rafforza = sostiene", "indebolisce = causa alternativa", "assunzione = ponte"], "green", "softGreen")}
  ${note(250, 805, 1100, "Formula da usare: vero nel mondo non significa dimostrato nel quesito.")}
`
  return shell("Testo e argomento: cercare evidenza", "La risposta deve essere supportata dal brano o dalle premesse, non solo plausibile.", inner)
}

function figureNumerico() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">Il calcolo corretto nasce dalla base corretta</text>
  ${card(130, 315, 300, 130, "Percentuale", ["di quale base?", "aumento o calo?"], "navy", "softBlue")}
  ${card(480, 315, 300, 130, "Proporzione", ["diretta", "oppure inversa"], "bordeaux", "softRed")}
  ${card(830, 315, 300, 130, "Tabella", ["riga, colonna", "grandezza chiesta"], "gold", "softGold")}
  ${card(1180, 315, 300, 130, "Stima", ["ordine di grandezza", "risultato plausibile"], "green", "softGreen")}
  <path class="arrowNavy" d="M440 380 L465 380"/>
  <path class="arrowBordeaux" d="M790 380 L815 380"/>
  <path class="arrowGold" d="M1140 380 L1165 380"/>
  ${mini(175, 560, 280, "20 / 80 = 25%", "base iniziale", palette.navy)}
  ${mini(500, 560, 280, "5 addetti", "piu lavoro se tempo uguale", palette.bordeaux)}
  ${mini(825, 560, 280, "64 / 80 = 80%", "quota, non valore assoluto", palette.gold)}
  ${mini(1150, 560, 280, "scala", "scarta valori impossibili", palette.green)}
  ${note(250, 805, 1100, "Prima di calcolare scrivi cosa stai cercando: valore finale, differenza o percentuale.")}
`
  return shell("Ragionamento numerico rapido", "Percentuali, proporzioni e tabelle richiedono base corretta e controllo di scala.", inner)
}

function figureTempoDiario() {
  const inner = `
  <rect class="card" x="90" y="175" width="1420" height="610" rx="30"/>
  <text class="navy label" x="800" y="232" text-anchor="middle">La gestione conta quanto la soluzione</text>
  ${card(135, 315, 280, 125, "Primo giro", ["quesiti riconoscibili", "risposte rapide"], "navy", "softBlue")}
  ${card(485, 315, 280, 125, "Secondo giro", ["schemi e calcoli", "domande segnate"], "bordeaux", "softRed")}
  ${card(835, 315, 280, 125, "Terzo giro", ["dubbi residui", "scelta controllata"], "gold", "softGold")}
  ${card(1185, 315, 280, 125, "Chiusura", ["nessun blocco", "tempo protetto"], "green", "softGreen")}
  <path class="arrowNavy" d="M425 375 L470 375"/>
  <path class="arrowBordeaux" d="M775 375 L820 375"/>
  <path class="arrowGold" d="M1125 375 L1170 375"/>
  ${listCard(175, 555, 360, "Esclusione", ["contraddice un dato", "troppo assoluta", "relazione invertita"], "navy", "softBlue")}
  ${listCard(620, 555, 360, "Soglie", ["serie: 30-45 sec", "vincoli: schema rapido", "brano: evidenza"], "bordeaux", "softRed")}
  ${listCard(1065, 555, 360, "Diario errori", ["lettura", "condizionale", "calcolo, tempo"], "green", "softGreen")}
  ${note(250, 805, 1100, "Correggere significa classificare l'errore: solo cosi il ripasso diventa mirato.")}
`
  return shell("Tempo, esclusione e diario errori", "Il punteggio cresce quando sai saltare, tornare e correggere per categoria.", inner)
}

function card(x, y, w, h, title, lines, colorClass, boxClass) {
  const titleY = y + 42
  const titleFontSize = title.length > 24 ? 18 : title.length > 19 ? 20 : title.length > 14 ? 22 : 25
  const bodyFontSize = lines.some((line) => line.length > 25) ? 16 : 18
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 25}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${titleY}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function flowCard(x, y, w, title, lines, colorClass, boxClass) {
  const titleFontSize = title.length > 12 ? 20 : 23
  const bodyFontSize = lines.some((line) => line.length > 20) ? 15 : 16
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + w / 2}" y="${y + 76 + index * 24}" text-anchor="middle" style="font-size:${bodyFontSize}px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} 135 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="135" rx="20"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 43}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    ${body}
  </g>`
}

function listCard(x, y, w, title, lines, colorClass, boxClass) {
  const rowHeight = 33
  const h = 92 + lines.length * rowHeight
  const titleFontSize = title.length > 22 ? 19 : title.length > 16 ? 21 : 24
  const body = lines
    .map((line, index) => `<text class="muted small" x="${x + 30}" y="${y + 82 + index * rowHeight}" style="font-size:17px">${esc(line)}</text>`)
    .join("\n")

  return `<g data-safe-box="${x} ${y} ${w} ${h} 8">
    <rect class="${boxClass}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/>
    <rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${palette[colorClass]}"/>
    <text class="${colorClass} label" x="${x + w / 2}" y="${y + 44}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <path class="thin" d="M${x + 24} ${y + 64} L${x + w - 24} ${y + 64}"/>
    ${body}
  </g>`
}

function mini(x, y, w, title, body, color) {
  const titleFontSize = title.length > 21 ? 18 : title.length > 15 ? 19 : 21
  const bodyFontSize = body.length > 26 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 78 8">
    <rect x="${x}" y="${y}" width="${w}" height="78" rx="20" fill="${color}"/>
    <text class="label" x="${x + w / 2}" y="${y + 32}" text-anchor="middle" fill="#FFFFFF" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="small" x="${x + w / 2}" y="${y + 58}" text-anchor="middle" fill="#FFFFFF" style="font-size:${bodyFontSize}px">${esc(body)}</text>
  </g>`
}

function stepCard(x, y, [number, title, subtitle], w) {
  const center = x + w / 2
  const titleFontSize = title.length > 15 ? 17 : 19
  const subtitleFontSize = subtitle.length > 20 ? 15 : 16

  return `<g data-safe-box="${x} ${y} ${w} 145 8">
    <rect class="card" x="${x}" y="${y}" width="${w}" height="145" rx="20"/>
    <circle cx="${center}" cy="${y + 34}" r="23" fill="${palette.gold}"/>
    <text class="ink label" x="${center}" y="${y + 43}" text-anchor="middle" style="font-size:22px">${esc(number)}</text>
    <text class="navy label" x="${center}" y="${y + 84}" text-anchor="middle" style="font-size:${titleFontSize}px">${esc(title)}</text>
    <text class="muted small" x="${center}" y="${y + 116}" text-anchor="middle" style="font-size:${subtitleFontSize}px">${esc(subtitle)}</text>
  </g>`
}

function note(x, y, w, text) {
  const fontSize = text.length > 98 ? 18 : text.length > 82 ? 19 : 20

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
