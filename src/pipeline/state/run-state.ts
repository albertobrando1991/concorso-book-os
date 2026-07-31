import { isTerminal, type GateResult, type MergeResult, type RunState, type StepRecord, type StepStatus } from "./types"

const STATUS_RANK: Record<StepStatus, number> = {
  pending: 0,
  "awaiting-agent": 1,
  "in-progress": 2,
  "awaiting-human": 3,
  blocked: 4,
  done: 5,
  skipped: 5
}

export type StepDraft = Omit<StepRecord, "status" | "attempts" | "evidence">

export interface CreateRunStateInput {
  volumeCode: string
  specPath: string
  specHash: string
  steps: StepDraft[]
  now: string
}

export interface StartStepInput {
  owner: string
  agent: string
  provider?: string
  now: string
  force?: boolean
  status?: Extract<StepStatus, "in-progress" | "awaiting-human">
}

export interface CompleteStepInput {
  gate: GateResult
  evidence?: string[]
  now: string
}

export function stepKey(id: string, target: string) {
  return target ? `${id}:${target}` : id
}

export function createRunState(input: CreateRunStateInput): RunState {
  return {
    volumeCode: input.volumeCode,
    specPath: input.specPath,
    specHash: input.specHash,
    createdAt: input.now,
    updatedAt: input.now,
    steps: input.steps.map((step) => ({ ...step, status: "pending", attempts: 0, evidence: [] }))
  }
}

export function findStep(state: RunState, key: string) {
  return state.steps.find((step) => step.key === key)
}

export function startStep(state: RunState, key: string, input: StartStepInput): RunState {
  const step = requireStep(state, key)

  if (step.status === "in-progress" && step.owner && step.owner !== input.owner && !input.force) {
    throw new Error(
      `Lo step ${step.id} su ${step.target || state.volumeCode} è già in carico a ${step.owner} dal ${step.startedAt}. Usa --force per subentrare.`
    )
  }

  return replaceStep(
    state,
    {
      ...step,
      status: input.status ?? "in-progress",
      owner: input.owner,
      agent: input.agent,
      provider: input.provider,
      startedAt: input.now,
      finishedAt: undefined,
      attempts: step.attempts + 1
    },
    input.now
  )
}

export function completeStep(state: RunState, key: string, input: CompleteStepInput): RunState {
  const step = requireStep(state, key)

  return replaceStep(
    state,
    {
      ...step,
      status: input.gate.passed ? "done" : "blocked",
      gate: input.gate,
      evidence: [...step.evidence, ...(input.evidence ?? [])],
      finishedAt: input.gate.passed ? input.now : undefined
    },
    input.now
  )
}

export function markStep(state: RunState, key: string, status: StepStatus, now: string): RunState {
  return replaceStep(state, { ...requireStep(state, key), status }, now)
}

export function nextStep(state: RunState, options: { from?: string; phase?: string; target?: string } = {}) {
  const candidates = state.steps.filter(
    (step) => (!options.phase || step.phase === options.phase) && (!options.target || step.target === options.target)
  )

  if (!options.from) return candidates.find((step) => !isTerminal(step.status))

  const start = candidates.findIndex((step) => step.id === options.from)

  if (start < 0) {
    throw new Error(`Lo step ${options.from} non esiste nel perimetro richiesto: controlla l'id o rimuovi --from.`)
  }

  return candidates[start]
}

export function blockedSteps(state: RunState) {
  return state.steps.filter((step) => step.status === "blocked")
}

export function mergeRunStates(local: RunState, remote: RunState): MergeResult {
  if (local.volumeCode !== remote.volumeCode) {
    throw new Error(`Impossibile unire run-state di volumi diversi: ${local.volumeCode} e ${remote.volumeCode}.`)
  }

  const remoteByKey = new Map(remote.steps.map((step) => [step.key, step]))
  const conflicts: MergeResult["conflicts"] = []
  const steps = local.steps.map((step) => {
    const other = remoteByKey.get(step.key)
    remoteByKey.delete(step.key)

    if (!other) return step

    const reason = describeConflict(step, other)

    if (reason) conflicts.push({ key: step.key, reason })

    return preferred(step, other)
  })

  return {
    state: {
      ...local,
      updatedAt: local.updatedAt > remote.updatedAt ? local.updatedAt : remote.updatedAt,
      steps: [...steps, ...remoteByKey.values()]
    },
    conflicts
  }
}

function describeConflict(local: StepRecord, remote: StepRecord) {
  if (isTerminal(local.status) && isTerminal(remote.status) && local.status !== remote.status) {
    return `esiti diversi: ${local.owner ?? "?"} ha chiuso come ${local.status}, ${remote.owner ?? "?"} come ${remote.status}.`
  }

  if (local.status === "done" && remote.status === "blocked") {
    return `${local.owner ?? "?"} ha chiuso lo step, ${remote.owner ?? "?"} lo ha lasciato bloccato: verificare quale gate è valido.`
  }

  if (remote.status === "done" && local.status === "blocked") {
    return `${remote.owner ?? "?"} ha chiuso lo step, ${local.owner ?? "?"} lo ha lasciato bloccato: verificare quale gate è valido.`
  }

  if (local.status === "in-progress" && remote.status === "in-progress" && local.owner !== remote.owner) {
    return `lo step è in carico a ${local.owner ?? "?"} e a ${remote.owner ?? "?"} contemporaneamente.`
  }

  return ""
}

function preferred(local: StepRecord, remote: StepRecord) {
  return STATUS_RANK[remote.status] > STATUS_RANK[local.status] ? remote : local
}

function requireStep(state: RunState, key: string) {
  const step = findStep(state, key)

  if (!step) {
    throw new Error(`Step ${key} assente dal run-state di ${state.volumeCode}: rigenera lo stato con "pipeline init".`)
  }

  return step
}

function replaceStep(state: RunState, step: StepRecord, now: string): RunState {
  return {
    ...state,
    updatedAt: now,
    steps: state.steps.map((current) => (current.key === step.key ? step : current))
  }
}
