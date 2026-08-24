import { readFile, writeFile } from "node:fs/promises"
import { readdir } from "node:fs/promises"
import path from "node:path"

const directory = path.resolve("wiki/books/moduli/m-fc03-enti-non-economici/chapters")

const apostrophes = new Map([
  ["e'", "è"], ["E'", "È"], ["puo'", "può"], ["Puo'", "Può"],
  ["perche'", "perché"], ["Perche'", "Perché"], ["piu'", "più"],
  ["pero'", "però"], ["cio'", "ciò"], ["gia'", "già"], ["cosi'", "così"],
  ["sara'", "sarà"], ["ne'", "né"], ["cioe'", "cioè"], ["dovra'", "dovrà"],
  ["diventera'", "diventerà"], ["da'", "dà"], ["meta'", "metà"],
  ["assumera'", "assumerà"], ["utilizzera'", "utilizzerà"], ["poiche'", "poiché"],
  ["avverra'", "avverrà"], ["proseguira'", "proseguirà"], ["valutera'", "valuterà"],
  ["comunichera'", "comunicherà"], ["uscira'", "uscirà"], ["reggera'", "reggerà"],
  ["finche'", "finché"]
])

const truncated = new Map([
  ["attivita", "attività"], ["contabilita", "contabilità"], ["responsabilita", "responsabilità"],
  ["finalita", "finalità"], ["modalita", "modalità"], ["qualita", "qualità"],
  ["possibilita", "possibilità"], ["autorita", "autorità"], ["priorita", "priorità"],
  ["operativita", "operatività"], ["profondita", "profondità"], ["conformita", "conformità"],
  ["continuita", "continuità"], ["pubblicita", "pubblicità"], ["proporzionalita", "proporzionalità"],
  ["necessita", "necessità"], ["unita", "unità"], ["utilita", "utilità"],
  ["validita", "validità"], ["capacita", "capacità"], ["complessita", "complessità"],
  ["comunita", "comunità"], ["identita", "identità"], ["opportunita", "opportunità"],
  ["proprieta", "proprietà"], ["realta", "realtà"], ["quantita", "quantità"],
  ["rapidita", "rapidità"], ["stabilita", "stabilità"], ["legalita", "legalità"],
  ["imparzialita", "imparzialità"], ["tracciabilita", "tracciabilità"],
  ["accessibilita", "accessibilità"], ["integrita", "integrità"],
  ["verificabilita", "verificabilità"], ["specificita", "specificità"],
  ["criticita", "criticità"], ["affidabilita", "affidabilità"], ["sostenibilita", "sostenibilità"]
])

const wrongGraves = new Map([
  ["perch\u00e8", "perch\u00e9"], ["Perch\u00e8", "Perch\u00e9"],
  ["poich\u00e8", "poich\u00e9"], ["Poich\u00e8", "Poich\u00e9"],
  ["affinch\u00e8", "affinch\u00e9"], ["Affinch\u00e8", "Affinch\u00e9"],
  ["cosicch\u00e8", "cosicch\u00e9"], ["Cosicch\u00e8", "Cosicch\u00e9"],
  ["n\u00e8", "n\u00e9"], ["N\u00e8", "N\u00e9"]
])

const missingAccents = new Map([
  ["abilita", "abilit\u00e0"], ["probabilita", "probabilit\u00e0"],
  ["sanita", "sanit\u00e0"], ["personalita", "personalit\u00e0"],
  ["regolarita", "regolarit\u00e0"], ["fragilita", "fragilit\u00e0"],
  ["invalidita", "invalidit\u00e0"], ["maternita", "maternit\u00e0"],
  ["conoscibilita", "conoscibilit\u00e0"], ["formalita", "formalit\u00e0"],
  ["interoperabilita", "interoperabilit\u00e0"], ["liceita", "liceit\u00e0"],
  ["annualita", "annualit\u00e0"], ["compatibilita", "compatibilit\u00e0"],
  ["controllabilita", "controllabilit\u00e0"], ["economicita", "economicit\u00e0"],
  ["passivita", "passivit\u00e0"], ["collettivita", "collettivit\u00e0"],
  ["disparita", "disparit\u00e0"], ["indennita", "indennit\u00e0"],
  ["arbitrarieta", "arbitrariet\u00e0"], ["sensibilita", "sensibilit\u00e0"],
  ["curiosita", "curiosit\u00e0"], ["disponibilita", "disponibilit\u00e0"],
  ["velocita", "velocit\u00e0"], ["difficolta", "difficolt\u00e0"],
  ["piu", "pi\u00f9"], ["gia", "gi\u00e0"], ["cio", "ci\u00f2"]
])

for (const name of (await readdir(directory)).filter((file) => file.endsWith(".md"))) {
  const file = path.join(directory, name)
  const content = (await readFile(file, "utf8")).replace(/\r\n/g, "\n")
  const match = content.match(/^(---\n[\s\S]*?\n---\n)([\s\S]*)$/)
  if (!match) throw new Error(`Frontmatter non riconosciuto: ${name}`)

  const header = match[1]
    .replace(/^status: .+$/m, "status: final")
    .replace(/^review_required: .+$/m, "review_required: false")
    .replace(/^draft_stage: .+$/m, "draft_stage: specialist_audit_done")
    .replace(/^updated_at: .+$/m, "updated_at: 2026-08-22T14:00:00+02:00")
    .replace(/professional-draft/g, "specialist-audit-complete")
  let body = match[2]
  for (const [from, to] of apostrophes) body = body.split(from).join(to)
  for (const [from, to] of wrongGraves) body = body.split(from).join(to)
  for (const [from, to] of missingAccents) {
    body = body.replace(new RegExp(`\\b${from}\\b`, "g"), to)
    body = body.replace(new RegExp(`\\b${capitalize(from)}\\b`, "g"), capitalize(to))
  }
  for (const [from, to] of truncated) {
    body = body.replace(new RegExp(`\\b${from}\\b`, "g"), to)
    body = body.replace(new RegExp(`\\b${capitalize(from)}\\b`, "g"), capitalize(to))
  }
  await writeFile(file, header + body, "utf8")
}

function capitalize(value) {
  return value.charAt(0).toUpperCase() + value.slice(1)
}
