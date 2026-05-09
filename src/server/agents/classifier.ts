import { createId, slugify } from "../wiki/slug"
import type { ClassifiedSource, SourceInput } from "../wiki/types"

const TOPIC_KEYWORDS: Array<[string, string[]]> = [
  ["metodo bando", ["metodo bando", "bando decoder", "diario", "output", "nuclei concettuali"]],
  ["anatomia del bando", ["anatomia del bando", "leggere un bando", "requisiti", "prove", "punteggi", "graduatorie"]],
  ["bando decoder", ["bando decoder", "griglia compilabile", "tabella operativa", "decodificare il tuo concorso"]],
  ["moduli profilo", ["moduli profilo", "mappe profilo", "profilo amministrativo", "profilo contabile"]],
  ["piano 30 60 90 giorni", ["piano 30/60/90", "30 giorni", "60 giorni", "90 giorni", "calendario realistico"]],
  ["diario errori", ["diario errori", "foglio errori", "tracciare gli errori", "classificazione errore"]],
  ["diritto costituzionale", ["costituzione", "parlamento", "governo", "regioni", "fonti del diritto"]],
  ["diritto amministrativo", ["amministrativo", "provvedimento", "procedimento", "accesso", "discrezionalita"]],
  ["enti locali", ["comune", "provincia", "sindaco", "giunta", "consiglio comunale", "ente locale"]],
  ["pubblico impiego", ["dipendente pubblico", "pubblico impiego", "contratto collettivo", "responsabilita disciplinare"]],
  ["contabilita pubblica", ["bilancio", "spesa", "entrata", "rendiconto", "contabilita"]],
  ["anticorruzione e trasparenza", ["anticorruzione", "trasparenza", "accesso civico", "anac", "prevenzione"]],
  ["procedimento amministrativo", ["legge 241", "procedimento amministrativo", "responsabile del procedimento", "silenzio"]],
  ["contratti pubblici", ["appalto", "contratti pubblici", "codice dei contratti", "affidamento", "rup"]]
]

const ENTITY_KEYWORDS: Array<[string, string[]]> = [
  ["Metodo BANDO", ["metodo bando"]],
  ["Bando Decoder", ["bando decoder"]],
  ["Moduli Profilo", ["moduli profilo", "mappe profilo"]],
  ["Diario degli errori", ["diario errori", "foglio errori"]],
  ["Piano 30/60/90 giorni", ["piano 30/60/90", "30 giorni", "60 giorni", "90 giorni"]],
  ["inPA", ["inpa", "portale inpa"]],
  ["Costituzione della Repubblica Italiana", ["costituzione"]],
  ["Legge 241/1990", ["legge 241", "241/1990", "procedimento amministrativo"]],
  ["ANAC", ["anac", "anticorruzione"]],
  ["RUP", ["rup", "responsabile unico del progetto", "responsabile unico del procedimento"]],
  ["Comune", ["comune", "consiglio comunale", "giunta", "sindaco"]],
  ["Codice dei contratti pubblici", ["codice dei contratti", "d.lgs. 36", "contratti pubblici"]],
  ["Piano integrato di attivita e organizzazione", ["piao", "piano integrato"]]
]

export function classifySource(input: SourceInput): ClassifiedSource {
  const haystack = `${input.title}\n${input.content}`.toLowerCase()
  const topics = TOPIC_KEYWORDS
    .filter(([, keywords]) => keywords.some((keyword) => haystack.includes(keyword)))
    .map(([topic]) => topic)

  const entities = ENTITY_KEYWORDS
    .filter(([, keywords]) => keywords.some((keyword) => haystack.includes(keyword)))
    .map(([entity]) => entity)

  const fallbackTopic = input.sourceType === "law" ? "diritto amministrativo" : "concorsi pubblici"
  const normalizedTopics = topics.length > 0 ? topics : [fallbackTopic]
  const normalizedEntities = entities.length > 0 ? entities : ["Pubblica amministrazione"]
  const authorityLevel = input.authorityLevel || inferAuthorityLevel(input.sourceType)
  const slug = slugify(input.title)

  return {
    id: createId("source", input.title),
    title: input.title,
    slug,
    topics: normalizedTopics,
    entities: normalizedEntities,
    summary: summarize(input.content),
    authorityLevel,
    sourceType: input.sourceType
  }
}

function inferAuthorityLevel(sourceType: SourceInput["sourceType"]) {
  if (sourceType === "law" || sourceType === "decree") return "alta"
  if (sourceType === "manual") return "media"
  return "bassa"
}

function summarize(content: string) {
  const compact = content.replace(/\s+/g, " ").trim()
  const sentences = compact.split(/(?<=[.!?])\s+/).slice(0, 3).join(" ")

  if (sentences.length > 80) return sentences

  return compact.slice(0, 600)
}
