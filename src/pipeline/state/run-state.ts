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

export interface ReopenStepsInput {
  fromStep: string
  moduleTarget: string
  chapterTarget?: string
  note: string
  actor: string
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

export function reopenSteps(state: RunState, input: ReopenStepsInput): RunState {
  if (!input.note.trim()) throw new Error("La riapertura richiede una note di audit non vuota.")
  if (!/^\d{2}$/.test(input.fromStep)) throw new Error(`Step iniziale non valido: ${input.fromStep}.`)

  const from = Number(input.fromStep)
  const reopenedKeys: string[] = []
  const steps = state.steps.map((step) => {
    const id = Number(step.id)
    const selectedChapter = step.scope === "chapter"
      && step.target.startsWith(`${input.moduleTarget}/`)
      && (!input.chapterTarget || step.target === input.chapterTarget)
      && id >= from
    const dependentModule = step.scope === "module" && step.target === input.moduleTarget && id >= 13
    const dependentVolume = step.scope === "volume" && id >= 17

    if (!selectedChapter && !dependentModule && !dependentVolume) return step

    reopenedKeys.push(step.key)
    const { owner, agent, provider, startedAt, finishedAt, gate, ...record } = step
    return { ...record, status: "pending" as const, evidence: [] }
  })

  if (!reopenedKeys.length) {
    throw new Error(`Nessuno step riaperto da ${input.fromStep} per ${input.chapterTarget || input.moduleTarget}.`)
  }

  return {
    ...state,
    updatedAt: input.now,
    steps,
    reopenHistory: [
      ...(state.reopenHistory ?? []),
      {
        at: input.now,
        actor: input.actor,
        note: input.note.trim(),
        fromStep: input.fromStep,
        moduleTarget: input.moduleTarget,
        ...(input.chapterTarget ? { chapterTarget: input.chapterTarget } : {}),
        reopenedKeys
      }
    ]
  }
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

export function mergeRunStates(base: RunState, local: RunState, remote: RunState): MergeResult {
  if (local.volumeCode !== remote.volumeCode) {
    throw new Error(`Impossibile unire run-state di volumi diversi: ${local.volumeCode} e ${remote.volumeCode}.`)
  }

  const baseByKey = new Map(base.steps.map((step) => [step.key, step]))
  const localByKey = new Map(local.steps.map((step) => [step.key, step]))
  const remoteByKey = new Map(remote.steps.map((step) => [step.key, step]))
  const keys = new Set([...localByKey.keys(), ...remoteByKey.keys()])
  const conflicts: MergeResult["conflicts"] = []
  const steps: StepRecord[] = []

  for (const key of keys) {
    const localStep = localByKey.get(key)
    const remoteStep = remoteByKey.get(key)

    if (!localStep) {
      if (remoteStep) steps.push(remoteStep)
      continue
    }

    if (!remoteStep) {
      steps.push(localStep)
      continue
    }

    if (sameStep(localStep, remoteStep)) {
      steps.push(localStep)
      continue
    }

    const baseStep = baseByKey.get(key)

    if (baseStep && sameStep(localStep, baseStep)) {
      steps.push(remoteStep)
      continue
    }

    if (baseStep && sameStep(remoteStep, baseStep)) {
      steps.push(localStep)
      continue
    }

    const reason = describeConflict(localStep, remoteStep)

    if (reason) conflicts.push({ key, reason })

    steps.push(preferred(localStep, remoteStep))
  }

  return {
    state: {
      ...local,
      updatedAt: local.updatedAt > remote.updatedAt ? local.updatedAt : remote.updatedAt,
      steps
    },
    conflicts
  }
}

function sameStep(a: StepRecord, b: StepRecord) {
  return JSON.stringify(a) === JSON.stringify(b)
}

function describeConflict(local: StepRecord, remote: StepRecord) {
  if (local.owner && remote.owner && local.owner !== remote.owner) {
    return `${local.owner} ha portato lo step a "${local.status}", ${remote.owner} a "${remote.status}": due persone hanno lavorato sullo stesso step con esiti diversi, decidi quale tenere.`
  }

  return `Due versioni divergenti dello stesso step (nessuna coincide con la base comune): confronta manualmente ${JSON.stringify(local)} e ${JSON.stringify(remote)}.`
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
