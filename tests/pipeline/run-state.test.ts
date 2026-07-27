import { describe, expect, it } from "vitest"
import { completeStep, createRunState, mergeRunStates, nextStep, startStep, stepKey } from "../../src/pipeline/state/run-state"
import type { RunState, StepRecord } from "../../src/pipeline/state/types"

const now = "2026-07-27T15:08:27.185Z"
const later = "2026-07-27T15:31:04.902Z"
const chapter = "moduli/m-fc02-agenzie-fiscali/chapters/01-perimetro.md"

const draft = (id: string, target = chapter): Omit<StepRecord, "status" | "attempts" | "evidence"> => ({
  key: stepKey(id, target),
  id,
  phase: "C",
  scope: "chapter",
  target
})

const state = () =>
  createRunState({
    volumeCode: "VOL-03",
    specPath: "wiki/books/volumi/vol-03/planning/00-scheda-pipeline.md",
    specHash: "sha256:abc",
    steps: [draft("08"), draft("09"), draft("10")],
    now
  })

const statusOf = (value: RunState, id: string) => value.steps.find((step) => step.id === id)?.status

describe("createRunState", () => {
  it("starts every step pending with no attempts", () => {
    expect(state().steps).toEqual([
      { ...draft("08"), status: "pending", attempts: 0, evidence: [] },
      { ...draft("09"), status: "pending", attempts: 0, evidence: [] },
      { ...draft("10"), status: "pending", attempts: 0, evidence: [] }
    ])
  })
  it("stamps creation and update time", () => {
    expect(state()).toMatchObject({ volumeCode: "VOL-03", specHash: "sha256:abc", createdAt: now, updatedAt: now })
  })
})

describe("startStep", () => {
  it("claims the step for an owner and agent without mutating the previous state", () => {
    const before = state()
    const after = startStep(before, stepKey("08", chapter), { owner: "collega", agent: "codex-cli", provider: "codex", now })
    expect(statusOf(before, "08")).toBe("pending")
    expect(after.steps[0]).toMatchObject({ status: "in-progress", owner: "collega", agent: "codex-cli", provider: "codex", startedAt: now, attempts: 1 })
  })
  it("refuses a step already claimed by someone else", () => {
    const claimed = startStep(state(), stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now })
    expect(() => startStep(claimed, stepKey("08", chapter), { owner: "altro", agent: "claude-code", now: later })).toThrow(/collega/)
  })
  it("lets the same owner resume their own step", () => {
    const claimed = startStep(state(), stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now })
    expect(startStep(claimed, stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now: later }).steps[0].attempts).toBe(2)
  })
  it("takes the step over when forced, keeping the attempt count", () => {
    const claimed = startStep(state(), stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now })
    const forced = startStep(claimed, stepKey("08", chapter), { owner: "altro", agent: "claude-code", now: later, force: true })
    expect(forced.steps[0]).toMatchObject({ owner: "altro", agent: "claude-code", attempts: 2 })
  })
  it("fails loudly on an unknown step", () => {
    expect(() => startStep(state(), stepKey("99", chapter), { owner: "collega", agent: "codex-cli", now })).toThrow(/99/)
  })
})

describe("completeStep", () => {
  const claimed = () => startStep(state(), stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now })

  it("marks the step done when the gate passes", () => {
    const done = completeStep(claimed(), stepKey("08", chapter), { gate: { passed: true, blockers: [], warnings: [] }, evidence: ["artifacts/a.json"], now: later })
    expect(done.steps[0]).toMatchObject({ status: "done", finishedAt: later, evidence: ["artifacts/a.json"] })
  })
  it("marks the step blocked when the gate fails, and keeps the blockers", () => {
    const gate = { passed: false, blockers: [{ code: "blocking-status", message: "riga 4: parziale" }], warnings: [] }
    const blocked = completeStep(claimed(), stepKey("08", chapter), { gate, now: later })
    expect(blocked.steps[0]).toMatchObject({ status: "blocked", gate })
    expect(blocked.steps[0].finishedAt).toBeUndefined()
  })
  it("accumulates evidence across attempts instead of replacing it", () => {
    const first = completeStep(claimed(), stepKey("08", chapter), { gate: { passed: false, blockers: [{ code: "x", message: "y" }], warnings: [] }, evidence: ["a.json"], now })
    const retried = startStep(first, stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now: later })
    const second = completeStep(retried, stepKey("08", chapter), { gate: { passed: true, blockers: [], warnings: [] }, evidence: ["b.json"], now: later })
    expect(second.steps[0].evidence).toEqual(["a.json", "b.json"])
  })
})

describe("nextStep", () => {
  const pass = { passed: true, blockers: [], warnings: [] }
  const finish = (value: RunState, id: string) =>
    completeStep(startStep(value, stepKey(id, chapter), { owner: "collega", agent: "codex-cli", now }), stepKey(id, chapter), { gate: pass, now: later })

  it("returns the first step still to do", () => {
    expect(nextStep(state())?.id).toBe("08")
  })
  it("skips steps already done", () => {
    expect(nextStep(finish(state(), "08"))?.id).toBe("09")
  })
  it("returns the blocked step itself, since nothing downstream may start", () => {
    const blocked = completeStep(startStep(state(), stepKey("08", chapter), { owner: "collega", agent: "codex-cli", now }), stepKey("08", chapter), {
      gate: { passed: false, blockers: [{ code: "x", message: "y" }], warnings: [] },
      now: later
    })
    expect(nextStep(blocked)?.id).toBe("08")
  })
  it("resumes from an explicit step id", () => {
    expect(nextStep(finish(finish(state(), "08"), "09"), { from: "08" })?.id).toBe("08")
  })
  it("returns undefined when every step is done", () => {
    expect(nextStep(finish(finish(finish(state(), "08"), "09"), "10"))).toBeUndefined()
  })
})

describe("mergeRunStates", () => {
  const done = (value: RunState, id: string, owner: string) =>
    completeStep(startStep(value, stepKey(id, chapter), { owner, agent: "codex-cli", now }), stepKey(id, chapter), { gate: { passed: true, blockers: [], warnings: [] }, now: later })

  it("keeps the more advanced record for each step", () => {
    const merged = mergeRunStates(done(state(), "08", "a"), done(state(), "09", "b"))
    expect([statusOf(merged.state, "08"), statusOf(merged.state, "09"), statusOf(merged.state, "10")]).toEqual(["done", "done", "pending"])
    expect(merged.conflicts).toEqual([])
  })
  it("reports a conflict when both sides finished the same step differently", () => {
    const mine = done(state(), "08", "a")
    const theirs = completeStep(startStep(state(), stepKey("08", chapter), { owner: "b", agent: "claude-code", now }), stepKey("08", chapter), {
      gate: { passed: false, blockers: [{ code: "x", message: "y" }], warnings: [] },
      now: later
    })
    expect(mergeRunStates(mine, theirs).conflicts.map((conflict) => conflict.key)).toEqual([stepKey("08", chapter)])
  })
  it("reports a conflict when two people hold the same step", () => {
    const mine = startStep(state(), stepKey("08", chapter), { owner: "a", agent: "codex-cli", now })
    const theirs = startStep(state(), stepKey("08", chapter), { owner: "b", agent: "claude-code", now })
    expect(mergeRunStates(mine, theirs).conflicts[0]).toMatchObject({ key: stepKey("08", chapter), reason: expect.stringContaining("a") })
  })
  it("adds steps present only on the other side", () => {
    const theirs = { ...state(), steps: [...state().steps, { ...draft("11"), status: "pending" as const, attempts: 0, evidence: [] }] }
    expect(mergeRunStates(state(), theirs).state.steps).toHaveLength(4)
  })
  it("refuses to merge run states of different volumes", () => {
    expect(() => mergeRunStates(state(), { ...state(), volumeCode: "VOL-09" })).toThrow(/VOL-09/)
  })
})
