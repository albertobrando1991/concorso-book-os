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
  startKeys: string[]
  cascade: boolean
  note: string
  now: string
}

export interface ReopenStepsResult {
  state: RunState
  reopenedKeys: string[]
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

export function reopenSteps(state: RunState, input: ReopenStepsInput): ReopenStepsResult {
  if (input.startKeys.length === 0) {
    throw new Error("Indica almeno uno step da riaprire.")
  }

  if (!input.note.trim()) {
    throw new Error("La nota di riapertura non può essere vuota.")
  }

  const selectedSteps = input.startKeys.map((key) => {
    const step = state.steps.find((candidate) => candidate.key === key)

    if (!step) {
      throw new Error(`Step ${key} assente dal run-state di ${state.volumeCode}.`)
    }

    return step
  })
  const selectedKeys = new Set(input.startKeys)
  const startOrder = Math.min(...selectedSteps.map(stepOrder))
  const cascadeScope = buildCascadeScope(state, selectedSteps)
  const isDownstream = (step: StepRecord) =>
    stepOrder(step) >= startOrder && stepOrder(step) < 24 && matchesCascadeScope(step, cascadeScope)
  const reopenedKeys = input.cascade
    ? new Set(state.steps.filter(isDownstream).map((step) => step.key))
    : selectedKeys

  if (!input.cascade) {
    const terminalDownstream = state.steps.find(
      (step) => stepOrder(step) > startOrder && isDownstream(step) && !reopenedKeys.has(step.key) && isTerminal(step.status)
    )

    if (terminalDownstream) {
      throw new Error(`Lo step ${terminalDownstream.id} è già terminale a valle: usa la riapertura con cascade.`)
    }
  }

  return {
    state: {
      ...state,
      updatedAt: input.now,
      steps: state.steps.map((step) =>
        reopenedKeys.has(step.key)
          ? pendingStep(step, selectedKeys.has(step.key) ? input.note : undefined)
          : step
      )
    },
    reopenedKeys: state.steps.filter((step) => reopenedKeys.has(step.key)).map((step) => step.key)
  }
}

interface CascadeScope {
  global: boolean
  chapterTargets: Set<string>
  moduleTargets: Set<string>
  chapterModuleTargets: Set<string>
}

function buildCascadeScope(state: RunState, selectedSteps: StepRecord[]): CascadeScope {
  const global = selectedSteps.some((step) => step.scope === "volume" || step.scope === "catalog")
  const chapterTargets = new Set(selectedSteps.filter((step) => step.scope === "chapter").map((step) => step.target))
  const moduleTargets = new Set(selectedSteps.filter((step) => step.scope === "module").map((step) => step.target))
  const chapterModuleTargets = new Set(moduleTargets)
  const declaredModuleTargets = new Set(state.steps.filter((step) => step.scope === "module").map((step) => step.target))

  for (const chapterTarget of chapterTargets) {
    const declared = [...declaredModuleTargets].filter((target) => chapterTarget.startsWith(`${target}/`))

    if (declared.length) {
      for (const target of declared) moduleTargets.add(target)
      continue
    }

    const marker = chapterTarget.indexOf("/chapters/")
    if (marker >= 0) moduleTargets.add(chapterTarget.slice(0, marker))
  }

  return { global, chapterTargets, moduleTargets, chapterModuleTargets }
}

function matchesCascadeScope(step: StepRecord, scope: CascadeScope) {
  if (scope.global || step.scope === "volume" || step.scope === "catalog") return true
  if (step.scope === "module") return scope.moduleTargets.has(step.target)

  return scope.chapterTargets.has(step.target) || [...scope.chapterModuleTargets].some((target) => step.target.startsWith(`${target}/`))
}

function stepOrder(step: StepRecord) {
  const parsed = Number.parseInt(step.id, 10)
  return Number.isFinite(parsed) ? parsed : Number.MAX_SAFE_INTEGER
}
function pendingStep(step: StepRecord, note?: string): StepRecord {
  return {
    ...step,
    status: "pending",
    attempts: 0,
    gate: undefined,
    owner: undefined,
    agent: undefined,
    provider: undefined,
    startedAt: undefined,
    finishedAt: undefined,
    evidence: note ? [...step.evidence, `reopen: ${note}`] : step.evidence
  }
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
