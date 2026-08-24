const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require("playwright")

const moduleRoot = path.join(process.cwd(), "wiki", "books", "moduli", "m-fc05-authority-indipendenti")
const p = {
  bg: "#F8FAFC", white: "#FFFFFF", ink: "#0F172A", muted: "#526174", border: "#CBD5E1", line: "#94A3B8",
  navy: "#10233F", bordeaux: "#7A2430", gold: "#D4AF37", green: "#2F7D5A", teal: "#1F6F78",
  blueSoft: "#EAF2FB", redSoft: "#F8E8EA", goldSoft: "#FFF4CC", greenSoft: "#E7F3ED", tealSoft: "#E4F4F5", cream: "#FFF7ED"
}

const chapters = [
  ["02", "indipendenza-governance-accountability-personale", "Indipendenza, governance e personale", ["fonte e mandato", "organi e decisioni", "accountability", "personale e incompatibilità", "output di prova"], ["indipendenza", "governance", "accountability", "personale"], ["garanzia", "istruttoria", "decisione", "controllo"], ["autonomia non è isolamento", "ruolo non è potere", "controllo non è interferenza"], ["fonte", "garanzia", "decisione", "responsabilità"]],
  ["03", "regolazione-europea-reti", "Regolazione europea e reti", ["fonte UE", "competenza nazionale", "rete europea", "caso transfrontaliero", "decisione motivata"], ["regolamento e direttiva", "autorità nazionale", "rete europea", "cooperazione"], ["problema", "coordinamento", "istruttoria", "esito"], ["rete non è gerarchia", "cooperare non elimina competenze", "UE non sostituisce il caso concreto"], ["fonte", "livello", "rete", "decisione"]],
  ["04", "ciclo-regolatorio-air-vir", "Ciclo regolatorio, AIR e VIR", ["problema", "consultazione", "AIR", "decisione", "monitoraggio e VIR"], ["regolazione", "consultazione", "AIR", "VIR"], ["evidenze", "opzioni", "atto", "valutazione"], ["consultare non è negoziare", "AIR non è mera premessa", "VIR non è controllo formale"], ["problema", "evidenze", "decisione", "verifica"]],
  ["05", "vigilanza-istruttoria-prova", "Vigilanza, istruttoria e prova", ["segnalazione", "piano istruttorio", "ispezione", "contraddittorio", "provvedimento"], ["vigilanza", "istruttoria", "ispezione", "dato e documento"], ["notizia", "raccolta", "valutazione", "decisione"], ["dato non è prova", "ispezione non è sanzione", "anomalia non è violazione"], ["fatto", "evidenza", "garanzia", "esito"]],
  ["06", "sanzioni-impegni-rimedi", "Sanzioni, impegni e rimedi", ["fatto", "contestazione", "contraddittorio", "rimedio o sanzione", "tutela"], ["sanzione", "impegni", "misura correttiva", "giudice"], ["accertamento", "difesa", "decisione", "controllo"], ["impegno non è sanzione", "rimedio non è premio", "ricorso non riscrive il fatto"], ["violazione", "garanzie", "proporzionalità", "tutela"]],
  ["07", "economia-regolazione-dati", "Economia della regolazione", ["mercato", "fallimento", "strumento", "dati", "tariffa e qualità"], ["concorrenza", "potere di mercato", "incentivi", "contabilità regolatoria"], ["problema", "ipotesi", "evidenze", "decisione"], ["costo non è prezzo", "correlazione non è causalità", "tariffa non è numero isolato"], ["mercato", "incentivo", "dato", "scelta"]],
  ["08", "agcm-concorrenza-consumatore", "AGCM: concorrenza e consumatore", ["mercato", "condotta", "istruttoria", "impegni o sanzione", "tutela"], ["intese", "abuso", "concentrazioni", "pratiche scorrette"], ["segnalazione", "accertamento", "decisione", "rimedio"], ["concorrenza non è pubblicità", "consumatore non è concorrente", "impegno non è assoluzione"], ["fatto", "mercato", "potere", "rimedio"]],
  ["09", "arera-servizi-tariffe", "ARERA: servizi e tariffe", ["servizio", "costi e dati", "tariffa", "qualità", "tutela utente"], ["energia e gas", "acqua", "rifiuti", "qualità"], ["dati", "consultazione", "regolazione", "monitoraggio"], ["tariffa non è prezzo libero", "qualità non è sola cortesia", "utente non è semplice cliente"], ["servizio", "costo", "qualità", "utente"]],
  ["10", "agcom-media-piattaforme", "AGCOM: comunicazioni e piattaforme", ["rete", "media", "utenti", "piattaforme", "cooperazione"], ["comunicazioni elettroniche", "audiovisivo", "pluralismo", "diritti utenti"], ["segnalazione", "regola", "vigilanza", "tutela"], ["rete non è media", "piattaforma non è editore", "Corecom non è AGCOM"], ["servizio", "utente", "regola", "garanzia"]],
  ["11", "consob-mercati-investitore", "CONSOB: mercati e investitore", ["emittente", "intermediario", "mercato", "investitore", "vigilanza"], ["trasparenza", "correttezza", "abusi di mercato", "tutela"], ["informazione", "condotta", "controllo", "sanzione"], ["rischio non è illecito", "informazione non è consulenza", "tutela non è rendimento"], ["dato", "correttezza", "mercato", "investitore"]],
  ["12", "banca-italia-ivass", "Banca d'Italia e IVASS", ["intermediario", "rischio", "vigilanza prudenziale", "condotta", "stabilità e tutela"], ["Banca d'Italia", "IVASS", "prudenziale", "clientela e assicurati"], ["segnale", "valutazione", "misura", "cooperazione"], ["stabilità non è servizio clienti", "prudenziale non è condotta", "banca non è assicurazione"], ["rischio", "governance", "vigilanza", "tutela"]],
  ["13", "garante-privacy-cooperazione", "Garante privacy e cooperazione", ["trattamento", "rischio", "reclamo o segnalazione", "istruttoria", "misura e cooperazione"], ["titolare", "interessato", "Garante", "EDPB"], ["criticità", "indagine", "misura", "controllo"], ["Garante non è titolare", "reclamo non è segnalazione", "privacy non annulla trasparenza"], ["trattamento", "responsabilità", "misura", "cooperazione"]],
  ["14", "anac-prevenzione-whistleblowing", "ANAC: prevenzione e whistleblowing", ["rischio", "PNA e RPCT", "misure", "segnalazione", "vigilanza e rimedio"], ["prevenzione", "trasparenza", "contratti", "whistleblowing"], ["rischio", "canale", "istruttoria", "protezione"], ["segnalazione non prova il fatto", "RPCT non sostituisce ANAC", "prevenzione non è adempimento"], ["rischio", "misura", "segnalazione", "integrità"]],
  ["15", "laboratorio-prove-authority", "Laboratorio delle prove authority", ["traccia", "decoder", "risposta", "correzione", "diario e piano"], ["quiz", "orale", "memo", "caso pratico"], ["leggi", "ordina", "scrivi", "correggi"], ["sapere non è esporre", "correggere non è rileggere", "simulare non è improvvisare"], ["traccia", "metodo", "feedback", "ripasso"]]
]

async function main() {
  const browser = await launchBrowser()
  try {
    for (const config of chapters) await buildChapter(config, browser)
  } finally { await browser.close() }
}

async function launchBrowser() {
  try { return await chromium.launch({ channel: "msedge", headless: true }) }
  catch {
    try { return await chromium.launch({ channel: "chrome", headless: true }) }
    catch { return chromium.launch({ headless: true }) }
  }
}

async function buildChapter([number, slug, title, bando, cards, flow, distinctions, synthesis], browser) {
  const assetDir = path.join(moduleRoot, "assets", `chapter-${number}`)
  const chapterFile = (await fs.readdir(path.join(moduleRoot, "chapters"))).find((file) => file.startsWith(`${number}-`) && file.endsWith(".md"))
  if (!chapterFile) throw new Error(`Capitolo ${number} non trovato nella cartella del modulo`)
  const chapterPath = path.join(moduleRoot, "chapters", chapterFile)
  const figures = [
    [`01-mappa-bando-${slug}`, `Mappa BANDO: ${title}`, bandoFigure(title, bando)],
    [`02-architettura-${slug}`, `Architettura: ${title}`, gridFigure(title, cards)],
    [`03-flusso-${slug}`, `Sequenza operativa: ${title}`, flowFigure(title, flow)],
    [`04-distinzioni-${slug}`, `Distinzioni essenziali: ${title}`, distinctionsFigure(title, distinctions)],
    [`05-sintesi-${slug}`, `Sintesi operativa: ${title}`, synthesisFigure(title, synthesis)]
  ]
  await fs.mkdir(assetDir, { recursive: true })
  for (const [file, , svg] of figures) await fs.writeFile(path.join(assetDir, `${file}.svg`), svg, "utf8")
  for (const [file, , svg] of figures) await rasterize(browser, svg, path.join(assetDir, `${file}.png`))
  await fs.writeFile(path.join(assetDir, "README.md"), readme(number, title, figures), "utf8")
  await injectMarkdown(chapterPath, number, figures)
}

async function rasterize(browser, svg, target) {
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 }, deviceScaleFactor: 1 })
  const data = Buffer.from(svg, "utf8").toString("base64")
  await page.setContent(`<body style="margin:0;background:${p.bg}"><img src="data:image/svg+xml;base64,${data}" width="1600" height="1000"></body>`, { waitUntil: "load" })
  await page.locator("img").screenshot({ path: target })
  await page.close()
}

async function injectMarkdown(chapterPath, number, figures) {
  let content = await fs.readFile(chapterPath, "utf8")
  if (content.includes(`../assets/chapter-${number}/`)) return
  const refs = figures.map(([file]) => `  - "books/moduli/m-fc05-authority-indipendenti/assets/chapter-${number}/${file}.png"`).join("\n")
  content = content.replace(/\n---\n/, `\nasset_refs:\n${refs}\n---\n`)
  content = content.replace(/updated_at: .+/, "updated_at: 2026-07-27")
  const headings = Array.from(content.matchAll(/^### .+$/gm)).map((match) => match[0])
  const contentHeadings = headings.filter((heading) => !/Apertura editoriale|Obiettivo operativo|Mappa BANDO|Caso guidato|Domanda|Risposta orale|Errore tipico|Mini-esercizio|Riferimenti|Note di review/.test(heading))
  const anchors = [contentHeadings[0], contentHeadings[1], contentHeadings[2], contentHeadings[3], headings.find((heading) => heading === "### Mappa BANDO")]
  for (const [index, anchor] of anchors.entries()) {
    if (!anchor) continue
    const [file, title] = figures[index]
    const block = `![Figura ${Number(number)}.${index + 1} — ${title}.](../assets/chapter-${number}/${file}.png)\n\n*Figura ${Number(number)}.${index + 1} — Schema di ripasso: usa la mappa per collegare regola, funzione e output di prova.*\n`
    content = content.replace(anchor, `${block}\n${anchor}`)
  }
  await fs.writeFile(chapterPath, content, "utf8")
}

function bandoFigure(title, items) {
  const colors = ["navy", "bordeaux", "gold", "green", "teal"]
  return shell(`Mappa BANDO: ${title}`, "Dal bando alla risposta: cinque domande per scegliere la priorità giusta.", `
  ${card(520, 180, 560, 145, "Bando e prova", ["profilo, programma, criteri e output"], "navy", "softBlue")}
  <path class="line" d="M800 325 L800 405"/><path class="line" d="M210 405 L1390 405"/>
  ${items.map((item, i) => { const x = 80 + i * 304; return `<path class="line" d="M${x + 130} 405 L${x + 130} 485"/>${card(x, 500, 260, 145, ["Bando","Aree","Nuclei","Diario","Output"][i], [item], colors[i], ["softBlue","softRed","softGold","softGreen","softTeal"][i])}` }).join("\n")}
  ${note("Obiettivo: leggere la materia come funzione, procedura e prestazione concorsuale.")}`)
}

function gridFigure(title, items) {
  return shell(`Architettura: ${title}`, "Quattro snodi da distinguere prima di affrontare il caso pratico.", `
  <rect class="card" x="85" y="175" width="1430" height="595" rx="30"/>
  ${items.map((item, i) => { const x = 150 + (i % 2) * 735; const y = 285 + Math.floor(i / 2) * 235; return card(x, y, 565, 150, item, ["definizione, funzione e limite"], ["navy","bordeaux","green","teal"][i], ["softBlue","softRed","softGreen","softTeal"][i]) }).join("\n")}
  ${note("La domanda d'esame valuta soprattutto le differenze: evita di usare le parole come sinonimi.")}`)
}

function flowFigure(title, items) {
  return shell(`Sequenza operativa: ${title}`, "Ricostruisci la catena dei passaggi prima di scegliere il rimedio o la risposta.", `
  <rect class="card" x="85" y="230" width="1430" height="465" rx="30"/>
  ${items.map((item, i) => { const x = 125 + i * 370; const color = ["navy","bordeaux","gold","green"][i]; const box = ["softBlue","softRed","softGold","softGreen"][i]; return `${card(x, 405, 280, 150, `${i + 1}. ${item}`, ["fatto, criterio, azione"], color, box)}${i < 3 ? `<path class="arrowNavy" d="M${x + 295} 480 L${x + 355} 480"/>` : ""}` }).join("\n")}
  ${note("Una risposta ordinata segue i passaggi; non salta dal fatto iniziale alla conclusione.")}`)
}

function distinctionsFigure(title, items) {
  return shell(`Distinzioni essenziali: ${title}`, "Tre confronti che impediscono errori di qualificazione e di metodo.", `
  ${items.map((item, i) => { const x = 150 + i * 475; const fontSize = item.length > 30 ? 16 : item.length > 25 ? 18 : 21; return `<g data-safe-box="${x} 270 350 350 8"><rect class="card" x="${x}" y="270" width="350" height="350" rx="28"/><circle cx="${x + 175}" cy="345" r="42" fill="${[p.navy,p.bordeaux,p.green][i]}"/><text class="label" x="${x + 175}" y="354" text-anchor="middle" fill="#FFFFFF">${i + 1}</text><text class="${["navy","bordeaux","green"][i]} label" x="${x + 175}" y="445" text-anchor="middle" style="font-size:${fontSize}px">${esc(item)}</text><path class="thin" d="M${x + 42} 485 L${x + 308} 485"/><text class="muted small" x="${x + 175}" y="530" text-anchor="middle">definisci, distingui, applica</text></g>` }).join("\n")}
  ${note("Se non sai spiegare la differenza, non puoi ancora scegliere il potere, il procedimento o l'output corretto.")}`)
}

function synthesisFigure(title, items) {
  return shell(`Sintesi operativa: ${title}`, "Dalla conoscenza alla prestazione: una mappa breve da usare prima di quiz, orale o memo.", `
  <rect class="softGold" x="330" y="185" width="940" height="108" rx="26"/><text class="gold label" x="800" y="230" text-anchor="middle">Ripasso in quattro mosse</text><text class="muted small" x="800" y="262" text-anchor="middle">metti in relazione fonte, funzione, fatto e risposta</text>
  ${items.map((item, i) => { const x = 130 + i * 365; return `${card(x, 420, 300, 150, `${i + 1}. ${item}`, ["parola chiave e controllo"], ["navy","bordeaux","green","teal"][i], ["softBlue","softRed","softGreen","softTeal"][i])}${i < 3 ? `<path class="arrowNavy" d="M${x + 315} 495 L${x + 350} 495"/>` : ""}` }).join("\n")}
  ${note("Prima della prova, ripeti la catena in voce: definizione, funzione, passaggi, esempio e limite.")}`)
}

function shell(title, subtitle, inside) {
  return `<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000" role="img" aria-labelledby="title desc"><title id="title">${esc(title)}</title><desc id="desc">${esc(subtitle)}</desc><defs><style>.bg{fill:${p.bg}}.card{fill:${p.white};stroke:${p.border};stroke-width:3}.softBlue{fill:${p.blueSoft};stroke:#B9CBE0;stroke-width:2.5}.softRed{fill:${p.redSoft};stroke:#E3B9BF;stroke-width:2.5}.softGold{fill:${p.goldSoft};stroke:#E8D080;stroke-width:2.5}.softGreen{fill:${p.greenSoft};stroke:#A8D1BD;stroke-width:2.5}.softTeal{fill:${p.tealSoft};stroke:#A3D5D8;stroke-width:2.5}.note{fill:${p.cream};stroke:#E7C18E;stroke-width:2.5}.ink{fill:${p.ink};font-family:Arial,Helvetica,sans-serif}.muted{fill:${p.muted};font-family:Arial,Helvetica,sans-serif}.title{font-size:43px;font-weight:700}.subtitle{font-size:22px}.label{font-family:Arial,Helvetica,sans-serif;font-size:25px;font-weight:700}.body{font-family:Arial,Helvetica,sans-serif;font-size:20px}.small{font-family:Arial,Helvetica,sans-serif;font-size:18px}.navy{fill:${p.navy}}.bordeaux{fill:${p.bordeaux}}.gold{fill:${p.gold}}.green{fill:${p.green}}.teal{fill:${p.teal}}.line{stroke:${p.line};stroke-width:4;stroke-linecap:round;fill:none}.thin{stroke:${p.border};stroke-width:2.5;stroke-linecap:round;fill:none}.arrowNavy{stroke:${p.navy};stroke-width:5;stroke-linecap:round;fill:none;marker-end:url(#arrowNavy)}</style><marker id="arrowNavy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="${p.navy}"/></marker></defs><rect class="bg" width="1600" height="1000"/><text class="ink title" x="800" y="70" text-anchor="middle">${esc(title)}</text><text class="muted subtitle" x="800" y="112" text-anchor="middle">${esc(subtitle)}</text>${inside}</svg>`
}

function card(x, y, w, h, title, lines, color, box) {
  return `<g data-safe-box="${x} ${y} ${w} ${h} 8"><rect class="${box}" x="${x}" y="${y}" width="${w}" height="${h}" rx="22"/><rect x="${x}" y="${y}" width="${w}" height="10" rx="5" fill="${p[color]}"/><text class="${color} label" x="${x + w / 2}" y="${y + 48}" text-anchor="middle" style="font-size:${title.length > 25 ? 18 : title.length > 18 ? 20 : 23}px">${esc(title)}</text>${lines.map((line, i) => `<text class="muted small" x="${x + w / 2}" y="${y + 92 + i * 27}" text-anchor="middle" style="font-size:${line.length > 28 ? 16 : 18}px">${esc(line)}</text>`).join("")}</g>`
}

function note(text) { return `<g data-safe-box="220 850 1160 70 8"><rect class="note" x="220" y="850" width="1160" height="70" rx="24"/><text class="ink body" x="800" y="894" text-anchor="middle" style="font-weight:700;font-size:18px">${esc(text)}</text></g>` }
function readme(number, title, figures) { return `# Asset M-FC05 — Capitolo ${Number(number)}\n\nFigure per **${title}**. I master SVG sono editabili; i PNG sono usati nella preview Markdown e nell'export.\n\n${figures.map(([file, label], i) => `- \`${file}.png\` — Figura ${Number(number)}.${i + 1}: ${label}.`).join("\n")}\n\nPalette e gabbia: 1600 × 1000 px, Arial, Navy/Bordeaux/Muted Gold/Green/Teal, coerenti con Il Metodo BANDO e M-FC02.\n` }
function esc(value) { return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;") }

main().catch((error) => { console.error(error); process.exit(1) })
