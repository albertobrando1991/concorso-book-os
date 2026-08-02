import { describe, expect, it } from "vitest"
import { reprojectRunState } from "../../src/pipeline/cli/commands"
import type { RunState, StepRecord } from "../../src/pipeline/state/types"

const step = (id: string, status: StepRecord["status"]): StepRecord => ({
  key: `${id}:target`,
  id,
  phase: id === "24" ? "F" : "D",
  scope: id === "24" ? "volume" : "module",
  target: "target",
  status,
  attempts: 1,
  evidence: [],
  owner: "legacy-reviewer",
  agent: "unknown",
  provider: "codex",
  startedAt: "2026-08-01T10:00:00.000Z"
})

const state = (steps: StepRecord[]): RunState => ({
  volumeCode: "VOL-99",
  specPath: "spec.md",
  specHash: "hash",
  createdAt: "2026-08-01T09:00:00.000Z",
  updatedAt: "2026-08-01T10:00:00.000Z",
  steps
})

describe("pipeline sync state migration", () => {
  it("returns obsolete human claims to automatic pending work and preserves final signoff", () => {
    const fresh = state([step("15", "pending"), step("24", "pending")])
    const existing = state([step("15", "awaiting-human"), step("24", "awaiting-human")])

    const projected = reprojectRunState(fresh, existing)

    expect(projected.steps[0]).toEqual({
      key: "15:target",
      id: "15",
      phase: "D",
      scope: "module",
      target: "target",
      status: "pending",
      attempts: 1,
      evidence: []
    })
    expect(projected.steps[1]).toMatchObject({
      id: "24",
      status: "awaiting-human",
      owner: "legacy-reviewer"
    })
  })
})
