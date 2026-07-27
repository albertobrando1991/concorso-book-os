import { mergeRunStates } from "./run-state"
import { parseRunState } from "./run-state-store"
import type { MergeConflict, RunState } from "./types"

export interface MergeDriverInput {
  baseContent: string
  oursContent: string
  theirsContent: string
}

export interface MergeDriverResult {
  ok: boolean
  output: string
  conflicts: MergeConflict[]
  diagnostic: string
}

export function runMergeDriver(input: MergeDriverInput): MergeDriverResult {
  const ours = safeParse(input.oursContent, "locale")
  const theirs = safeParse(input.theirsContent, "remoto")

  if (typeof ours === "string") return failure(ours, input)
  if (typeof theirs === "string") return failure(theirs, input)

  const base = input.baseContent.trim() ? safeParse(input.baseContent, "base comune") : pristineBase(ours, theirs)

  if (typeof base === "string") return failure(base, input)

  let merge: ReturnType<typeof mergeRunStates>

  try {
    merge = mergeRunStates(base, ours, theirs)
  } catch (error) {
    return failure((error as Error).message, input)
  }

  if (merge.conflicts.length) {
    return {
      ok: false,
      output: conflictMarkers(ours, theirs),
      conflicts: merge.conflicts,
      diagnostic: diagnosticFor(merge.conflicts, ours, theirs)
    }
  }

  return { ok: true, output: `${JSON.stringify(merge.state, null, 2)}\n`, conflicts: [], diagnostic: "" }
}

function pristineBase(ours: RunState, theirs: RunState): RunState {
  const byKey = new Map(ours.steps.map((step) => [step.key, step]))

  theirs.steps.forEach((step) => {
    if (!byKey.has(step.key)) byKey.set(step.key, step)
  })

  const steps = [...byKey.values()].map((step) => ({
    key: step.key,
    id: step.id,
    phase: step.phase,
    scope: step.scope,
    target: step.target,
    status: "pending" as const,
    attempts: 0,
    evidence: []
  }))

  return { ...ours, steps }
}

function safeParse(content: string, label: string): RunState | string {
  try {
    return parseRunState(content, `run-state.json (${label})`)
  } catch (error) {
    return (error as Error).message
  }
}

function failure(message: string, input: MergeDriverInput): MergeDriverResult {
  return { ok: false, output: input.oursContent, conflicts: [], diagnostic: message }
}

function conflictMarkers(ours: RunState, theirs: RunState) {
  return ["<<<<<<< HEAD", JSON.stringify(ours, null, 2), "=======", JSON.stringify(theirs, null, 2), ">>>>>>> incoming", ""].join("\n")
}

function diagnosticFor(conflicts: MergeConflict[], ours: RunState, theirs: RunState) {
  const findStep = (state: RunState, key: string) => state.steps.find((step) => step.key === key)
  const lines = conflicts.map((conflict) => {
    const local = findStep(ours, conflict.key)
    const remote = findStep(theirs, conflict.key)
    const target = local?.target ?? remote?.target ?? conflict.key

    return `step ${local?.id ?? remote?.id ?? "?"} su ${target}: ${conflict.reason}`
  })

  return [
    `Conflitto sul run-state di ${ours.volumeCode}: due persone hanno lavorato sullo stesso step.`,
    ...lines,
    "Risolvi a mano nel file (marcatori <<<<<<< / ======= / >>>>>>>), decidi quale versione tenere per lo step in conflitto, poi `git add` e continua il merge.",
    "Non cancellare l'altro blocco senza averlo letto: potrebbe contenere un avanzamento valido."
  ].join("\n")
}
