import fs from "node:fs"
import path from "node:path"

const cp1252Special = new Map([
  [0x20ac, 0x80], [0x201a, 0x82], [0x0192, 0x83], [0x201e, 0x84],
  [0x2026, 0x85], [0x2020, 0x86], [0x2021, 0x87], [0x02c6, 0x88],
  [0x2030, 0x89], [0x0160, 0x8a], [0x2039, 0x8b], [0x0152, 0x8c],
  [0x017d, 0x8e], [0x2018, 0x91], [0x2019, 0x92], [0x201c, 0x93],
  [0x201d, 0x94], [0x2022, 0x95], [0x2013, 0x96], [0x2014, 0x97],
  [0x02dc, 0x98], [0x2122, 0x99], [0x0161, 0x9a], [0x203a, 0x9b],
  [0x0153, 0x9c], [0x017e, 0x9e], [0x0178, 0x9f]
])

const decoder = new TextDecoder("utf-8", { fatal: true })

function cp1252Bytes(value) {
  const bytes = []
  for (const char of value) {
    const code = char.codePointAt(0)
    if (code <= 0xff) {
      bytes.push(code)
      continue
    }
    const mapped = cp1252Special.get(code)
    if (mapped === undefined) return null
    bytes.push(mapped)
  }
  return Uint8Array.from(bytes)
}

function mojibakeScore(value) {
  return [...value].filter((char) => "ÃÂâƒÆ¢€šœ¬".includes(char)).length
}

function repairRun(value) {
  let current = value
  for (let pass = 0; pass < 5; pass += 1) {
    const bytes = cp1252Bytes(current)
    if (!bytes) break
    let decoded
    try {
      decoded = decoder.decode(bytes)
    } catch {
      break
    }
    if (decoded === current || mojibakeScore(decoded) >= mojibakeScore(current)) break
    current = decoded
  }
  return current
}

const italianWords = new Map([
  ["accessibilita", "accessibilità"], ["ammissibilita", "ammissibilità"],
  ["attivita", "attività"], ["autorita", "autorità"], ["capacita", "capacità"],
  ["cio", "ciò"], ["cioe", "cioè"], ["comunita", "comunità"],
  ["compatibilita", "compatibilità"], ["continuita", "continuità"],
  ["contabilita", "contabilità"], ["criticita", "criticità"], ["densita", "densità"],
  ["disponibilita", "disponibilità"],
  ["eleggibilita", "eleggibilità"], ["finalita", "finalità"], ["gia", "già"],
  ["identita", "identità"], ["imparzialita", "imparzialità"],
  ["informalita", "informalità"], ["integrita", "integrità"], ["legalita", "legalità"],
  ["liberta", "libertà"], ["mobilita", "mobilità"],
  ["modalita", "modalità"], ["necessita", "necessità"], ["opportunita", "opportunità"],
  ["possibilita", "possibilità"], ["priorita", "priorità"], ["professionalita", "professionalità"],
  ["ammissibilita", "ammissibilità"], ["pero", "però"], ["proprieta", "proprietà"],
  ["qualita", "qualità"], ["realta", "realtà"],
  ["responsabilita", "responsabilità"], ["societa", "società"], ["specificita", "specificità"],
  ["tracciabilita", "tracciabilità"],
  ["sara", "sarà"], ["universita", "università"], ["utilita", "utilità"], ["varieta", "varietà"]
])

function normalizeItalian(value) {
  let result = value.replace(/[^\x00-\x7F]+/gu, repairRun)
  result = result.replace(/\bE'(?=\s|[.,;:!?])/g, "È")
  result = result.replace(/\be'(?=\s|[.,;:!?])/g, "è")
  result = result.replace(/\bpuo'?(?=\s|[.,;:!?])/gi, (word) => word[0] === "P" ? "Può" : "può")
  result = result.replace(/\bperche'?(?=\s|[.,;:!?])/gi, (word) => word[0] === "P" ? "Perché" : "perché")
  result = result.replace(/\bpiu'?(?=\s|[.,;:!?])/gi, (word) => word[0] === "P" ? "Più" : "più")
  result = result.replace(/\bne'(?=\s|[.,;:!?])/gi, (word) => word[0] === "N" ? "Né" : "né")
  result = result.replace(/\bcosi'?(?=\s|[.,;:!?])/gi, (word) => word[0] === "C" ? "Così" : "così")
  for (const [plain, accented] of italianWords) {
    result = result.replace(new RegExp(`\\b${plain}(?:'(?=\\s|[.,;:!?])|\\b)`, "gi"), (word) =>
      word[0] === word[0].toUpperCase()
        ? accented[0].toUpperCase() + accented.slice(1)
        : accented
    )
  }
  result = result.replace(/([àèéìòù])'(?=\s|[.,;:!?])/g, "$1")
  result = result.replace(/\bdell azione\b/gi, (word) => word[0] === "D" ? "Dell'azione" : "dell'azione")
  result = result.replaceAll("Se la prova e teorico-pratica", "Se la prova è teorico-pratica")
  result = result.replaceAll("La biblioteca universitaria e un servizio", "La biblioteca universitaria è un servizio")
  result = result.replaceAll("Se una risorsa e disponibile", "Se una risorsa è disponibile")
  result = result.replaceAll("Se il problema e catalografico", "Se il problema è catalografico")
  result = result.replaceAll("Nel profilo AFAM e importante", "Nel profilo AFAM è importante")
  result = result.replaceAll("quando una regola e comune", "quando una regola è comune")
  result = result.replaceAll("La risposta da concorso non e ", "La risposta da concorso non è ")
  result = result.replaceAll(". E una nota istruttoria", ". È una nota istruttoria")
  result = result.replaceAll("non e documentato", "non è documentato")
  result = result.replaceAll("La prima operazione e riconoscere", "La prima operazione è riconoscere")
  result = result.replaceAll("La seconda operazione e leggere", "La seconda operazione è leggere")
  result = result.replaceAll("Questa e una risposta", "Questa è una risposta")
  result = result.replaceAll("Il profilo amministrativo/studenti e quello", "Il profilo amministrativo/studenti è quello")
  result = result.replaceAll("riconoscimento dei crediti e automatico", "riconoscimento dei crediti è automatico")
  result = result.replaceAll("qual e ", "qual è ")
  result = result.replaceAll("Il rischio maggiore e confondere", "Il rischio maggiore è confondere")
  result = result.replaceAll("Se una spesa e presente", "Se una spesa è presente")
  result = result.replaceAll("allora e sempre", "allora è sempre")
  result = result.replaceAll("La previsione di budget e necessaria", "La previsione di budget è necessaria")
  result = result.replaceAll("Il primo e il catalogo", "Il primo è il catalogo")
  result = result.replaceAll("non e un semplice elenco", "non è un semplice elenco")
  result = result.replaceAll("Il secondo e il servizio", "Il secondo è il servizio")
  result = result.replaceAll("Il terzo e il limite", "Il terzo è il limite")
  result = result.replaceAll("Se una risorsa e open access", "Se una risorsa è open access")
  result = result.replaceAll("Che differenza c'e", "Che differenza c'è")
  result = result.replaceAll("La biblioteca e anche amministrazione", "La biblioteca è anche amministrazione")
  result = result.replaceAll("il centro della prova e il servizio", "il centro della prova è il servizio")
  result = result.replaceAll("Il punto chiave e distinguere", "Il punto chiave è distinguere")
  result = result.replaceAll("Questa formula non e cautela vuota: e metodo professionale", "Questa formula non è cautela vuota: è metodo professionale")
  result = result.replaceAll("La richiesta e stata acquisita", "La richiesta è stata acquisita")
  result = result.replaceAll("formative e necessaria", "formative è necessaria")
  result = result.replaceAll("chiedera di produrre", "chiederà di produrre")
  result = result.replaceAll("riconoscimento crediti e una domanda", "riconoscimento crediti è una domanda")
  result = result.replace(/^(A|B|C|D)\. e(?=\s+(?:un|una|sempre)\b)/gm, "$1. è")
  result = result.replace(/\bil primo elemento da decodificare e:/gi, (value) =>
    value[0] === "I" ? "Il primo elemento da decodificare è:" : "il primo elemento da decodificare è:"
  )
  return result
}

function fixCanonicalSlugs(value) {
  return value
    .replaceAll("m-ir02-università-afam", "m-ir02-universita-afam")
    .replaceAll("vol-06-scuola-università-ricerca-cultura", "vol-06-scuola-universita-ricerca-cultura")
    .replaceAll("fonti-ufficiali-m-ir02-università-afam", "fonti-ufficiali-m-ir02-universita-afam")
    .replaceAll("bandi-rappresentativi-m-ir02-università-afam", "bandi-rappresentativi-m-ir02-universita-afam")
    .replaceAll("03-piano-capitolo-04-amministrazione-contabilità-controlli", "03-piano-capitolo-04-amministrazione-contabilita-controlli")
}

function normalizeDocument(value) {
  const frontmatter = value.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/)
  if (!frontmatter) return fixCanonicalSlugs(normalizeItalian(value))

  const head = fixCanonicalSlugs(frontmatter[0].replace(/[^\x00-\x7F]+/gu, repairRun))
  const body = normalizeItalian(value.slice(frontmatter[0].length))
  return head + fixCanonicalSlugs(body)
}

const write = process.argv.includes("--write")
const targets = process.argv.slice(2).filter((arg) => arg !== "--write")
if (targets.length === 0) {
  throw new Error("Indicare almeno un file da normalizzare.")
}

let changed = 0
for (const target of targets) {
  const absolute = path.resolve(target)
  const before = fs.readFileSync(absolute, "utf8")
  const after = normalizeDocument(before)
  if (after === before) {
    console.log(`UNCHANGED ${target}`)
    continue
  }
  changed += 1
  const beforeMojibake = mojibakeScore(before)
  const afterMojibake = mojibakeScore(after)
  console.log(`${write ? "UPDATED" : "WOULD_UPDATE"} ${target} mojibake=${beforeMojibake}->${afterMojibake}`)
  if (write) fs.writeFileSync(absolute, after, "utf8")
}

console.log(JSON.stringify({ write, targets: targets.length, changed }))
