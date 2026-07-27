import type { StepScope } from "../state/types"

export type StepKind = "llm" | "deterministic" | "human"
export type StepAutomation = "automated" | "manual"

export interface StepDefinition {
  id: string
  phase: string
  title: string
  scope: StepScope
  kind: StepKind
  automation: StepAutomation
  gate?: string
}

const definition = (
  id: string,
  phase: string,
  title: string,
  scope: StepScope,
  kind: StepKind,
  automation: StepAutomation,
  gate?: string
): StepDefinition => ({ id, phase, title, scope, kind, automation, gate })

export const STEP_REGISTRY: StepDefinition[] = [
  definition("00", "A", "Presa in carico e regole operative", "catalog", "llm", "manual"),
  definition("01", "A", "Raccolta sicura del lavoro dello staff", "catalog", "llm", "manual"),
  definition("02", "A", "Consolidamento dei contributi", "catalog", "llm", "manual"),
  definition("03", "A", "Riconciliazione del catalogo", "catalog", "llm", "manual"),
  definition("04", "B", "Scheda di apertura del volume", "volume", "llm", "manual"),
  definition("05", "B", "Audit dei bandi rappresentativi", "module", "llm", "manual"),
  definition("06", "B", "Audit e consolidamento delle fonti", "module", "llm", "manual"),
  definition("07", "B", "Matrice di copertura didattica v4", "module", "llm", "manual", "coverage"),
  definition("08", "C", "Piano operativo del singolo capitolo", "chapter", "llm", "automated", "chapter-plan"),
  definition("09", "C", "Scrittura o completamento del capitolo", "chapter", "llm", "automated", "chapter-lint"),
  definition("10", "C", "Controllo di copertura del capitolo", "chapter", "llm", "automated", "coverage"),
  definition("11", "C", "Humanizer del capitolo", "chapter", "llm", "automated", "citation-guard"),
  definition("12", "C", "Revisione editoriale del capitolo", "chapter", "llm", "automated", "review-report"),
  definition("13", "D", "Revisione trasversale del modulo", "module", "llm", "automated", "review-report"),
  definition("14", "D", "Correzione del report editoriale", "module", "llm", "automated", "review-report"),
  definition("15", "D", "Review umana specialistica", "module", "human", "automated", "human-signoff"),
  definition("16", "D", "Congelamento del testo", "module", "deterministic", "automated", "text-freeze"),
  definition("17", "E", "Filosofia visiva del volume", "volume", "llm", "manual"),
  definition("18", "E", "Audit e ottimizzazione delle immagini", "module", "llm", "manual"),
  definition("19", "E", "Impaginazione KDP", "volume", "llm", "manual"),
  definition("20", "E", "Audit pagina per pagina", "volume", "llm", "manual", "page-fill"),
  definition("21", "F", "Revisore Editoriale Totale sull'impaginato", "volume", "llm", "automated", "review-report"),
  definition("22", "F", "Preflight tecnico ed editoriale", "volume", "deterministic", "automated", "preflight"),
  definition("23", "F", "Consegna, commit e pubblicazione", "volume", "human", "automated", "delivery"),
  definition("24", "G", "Manutenzione post-pubblicazione", "volume", "llm", "manual")
]

export const PHASE_STEPS: Record<string, string[]> = STEP_REGISTRY.reduce<Record<string, string[]>>(
  (phases, step) => ({ ...phases, [step.phase]: [...(phases[step.phase] ?? []), step.id] }),
  {}
)

export function findStepDefinition(id: string) {
  return STEP_REGISTRY.find((step) => step.id === id)
}

export function stepsForPhases(phases: string[]) {
  const wanted = new Set(phases.map((phase) => phase.trim().toUpperCase()))

  return STEP_REGISTRY.filter((step) => wanted.has(step.phase))
}

export function requireStepDefinition(id: string) {
  const step = findStepDefinition(id)

  if (!step) {
    throw new Error(`Step ${id} inesistente: il protocollo prevede gli id da 00 a 24.`)
  }

  return step
}
