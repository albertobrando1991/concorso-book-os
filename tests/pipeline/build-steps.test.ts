import { describe, expect, it } from "vitest"
import { parseVolumeSpec } from "../../src/pipeline/spec/parse-volume-spec"
import { buildStepDrafts } from "../../src/pipeline/steps/build-steps"

const sheet = (phases: string, extra = "") => `---
volume_code: VOL-03
volume_title: Funzioni centrali
cut_off_date: 2026-07-27
responsabile_normativo: Alberto Brando
phases: [${phases}]
---

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | --- | --- |
| M-FC01 | moduli/m-fc01-ministeri | 2 | |
| M-FC02 | moduli/m-fc02-agenzie-fiscali | 1 | |

## Capitoli M-FC02

| # | File |
| --- | --- |
| 01 | chapters/01-perimetro.md |
| 02 | chapters/02-tributi.md |

## Capitoli M-FC01

| # | File |
| --- | --- |
| 01 | chapters/01-ministeri.md |
${extra}`

const spec = (phases: string, extra = "") => parseVolumeSpec(sheet(phases, extra), "planning/00-scheda-pipeline.md")
const build = (phases: string) =>
  buildStepDrafts(
    spec(phases),
    phases.split(",").map((phase) => phase.trim())
  )

describe("buildStepDrafts", () => {
  it("walks modules by priority, not by declaration order", () => {
    expect([...new Set(build("C").map((step) => step.target.split("/chapters/")[0]))]).toEqual([
      "moduli/m-fc02-agenzie-fiscali",
      "moduli/m-fc01-ministeri"
    ])
  })
  it("repeats the chapter loop for every chapter, in protocol order", () => {
    const first = build("C").filter((step) => step.target.endsWith("01-perimetro.md"))
    expect(first.map((step) => step.id)).toEqual(["08", "09", "10", "11", "12"])
  })
  it("targets a chapter with its full wiki book path", () => {
    expect(build("C")[0].target).toBe("moduli/m-fc02-agenzie-fiscali/chapters/01-perimetro.md")
  })
  it("closes a module before opening the next one", () => {
    const ids = build("C,D").map((step) => `${step.id}:${step.target}`)
    expect(ids.indexOf("16:moduli/m-fc02-agenzie-fiscali")).toBeLessThan(
      ids.indexOf("08:moduli/m-fc01-ministeri/chapters/01-ministeri.md")
    )
  })
  it("runs module-scoped steps once per module", () => {
    expect(build("D").filter((step) => step.id === "13").map((step) => step.target)).toEqual([
      "moduli/m-fc02-agenzie-fiscali",
      "moduli/m-fc01-ministeri"
    ])
  })
  it("runs volume-scoped steps once, after every module", () => {
    const steps = build("C,F")
    expect(steps.filter((step) => step.id === "22")).toHaveLength(1)
    expect(steps.at(-1)?.id).toBe("23")
  })
  it("gives volume-scoped steps the volume code as target", () => {
    expect(build("F")[0].target).toBe("VOL-03")
  })
  it("assigns a unique key to every step", () => {
    const keys = build("C,D,F").map((step) => step.key)
    expect(new Set(keys).size).toBe(keys.length)
  })
  it("carries phase and scope from the registry", () => {
    expect(build("C")[0]).toMatchObject({ id: "08", phase: "C", scope: "chapter" })
  })
  it("skips a module that does not declare the requested phase", () => {
    const declared = parseVolumeSpec(
      sheet("C,D").replace("| M-FC01 | moduli/m-fc01-ministeri | 2 | |", "| M-FC01 | moduli/m-fc01-ministeri | 2 | D |"),
      "s.md"
    )
    expect(buildStepDrafts(declared, ["C"]).some((step) => step.target.includes("m-fc01"))).toBe(false)
  })
  it("refuses to build the chapter loop for a module with no known chapters", () => {
    const missing = parseVolumeSpec(sheet("C").replace(/## Capitoli M-FC01[\s\S]*$/, ""), "planning/00-scheda-pipeline.md")
    expect(() => buildStepDrafts(missing, ["C"])).toThrow(/M-FC01/)
  })
  it("returns nothing when no phase is requested", () => {
    expect(buildStepDrafts(spec("C"), [])).toEqual([])
  })
})
