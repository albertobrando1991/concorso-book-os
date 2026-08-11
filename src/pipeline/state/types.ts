export const STEP_STATUSES = ["pending", "in-progress", "awaiting-agent", "awaiting-human", "blocked", "done", "skipped"] as const
export type StepStatus = (typeof STEP_STATUSES)[number]

export type StepScope = "catalog" | "volume" | "module" | "chapter"

export interface GateIssue {
  code: string
  message: string
  location?: string
}

export interface GateResult {
  passed: boolean
  blockers: GateIssue[]
  warnings: GateIssue[]
  notImplemented?: string[]
}

export interface StepRecord {
  key: string
  id: string
  phase: string
  scope: StepScope
  target: string
  status: StepStatus
  attempts: number
  evidence: string[]
  owner?: string
  agent?: string
  provider?: string
  startedAt?: string
  finishedAt?: string
  gate?: GateResult
}

export interface RunState {
  volumeCode: string
  specPath: string
  specHash: string
  createdAt: string
  updatedAt: string
  steps: StepRecord[]
  reopenHistory?: ReopenEvent[]
}

export interface ReopenEvent {
  at: string
  actor: string
  note: string
  fromStep: string
  moduleTarget: string
  chapterTarget?: string
  reopenedKeys: string[]
}

export interface MergeConflict {
  key: string
  reason: string
}

export interface MergeResult {
  state: RunState
  conflicts: MergeConflict[]
}

export const TERMINAL_STATUSES: StepStatus[] = ["done", "skipped"]

export function isTerminal(status: StepStatus) {
  return TERMINAL_STATUSES.includes(status)
}
