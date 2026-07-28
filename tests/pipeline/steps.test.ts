import { readFileSync } from "node:fs"
import { resolve } from "node:path"
import { describe, expect, it } from "vitest"
import { loadPromptCatalog, PROMPT_TEMPLATE_PATH, renderPrompt } from "../../src/pipeline/steps/prompt-renderer"
import { PHASE_STEPS, STEP_REGISTRY, findStepDefinition, stepsForPhases } from "../../src/pipeline/steps/registry"

const template = readFileSync(resolve(PROMPT_TEMPLATE_PATH), "utf8")
const catalog = loadPromptCatalog(template)
const values = {
  VOLUME_CODE: "VOL-03",
  VOLUME_TITLE: "Funzioni centrali",
  MODULE_CODE: "M-FC02",
  MODULE_ID: "moduli/m-fc02-agenzie-fiscali",
  CHAPTER_FILE: "wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/01-perimetro.md",
  CHAPTER_NUMBER: "01",
  CUT_OFF_DATE: "2026-07-27",
  RESPONSABILE: "Alberto Brando"
}

describe("step registry", () => {
  it("covers the twenty-five prompts of the protocol, in order", () => {
    expect(STEP_REGISTRY.map((step) => step.id)).toEqual(Array.from({ length: 25 }, (_, index) => String(index).padStart(2, "0")))
  })
  it("assigns every step to a declared phase", () => {
    expect(STEP_REGISTRY.every((step) => PHASE_STEPS[step.phase]?.includes(step.id))).toBe(true)
  })
  it("keeps the chapter loop on phase C and the module consolidation on phase D", () => {
    expect(PHASE_STEPS.C).toEqual(["08", "09", "10", "11", "12"])
    expect(PHASE_STEPS.D).toEqual(["13", "14", "15", "16"])
    expect(PHASE_STEPS.F).toEqual(["21", "22", "23"])
  })
  it("runs the chapter loop at chapter scope", () => {
    expect(PHASE_STEPS.C.every((id) => findStepDefinition(id)?.scope === "chapter")).toBe(true)
  })
  it("marks as human the steps the protocol reserves to a person", () => {
    expect(STEP_REGISTRY.filter((step) => step.kind === "human").map((step) => step.id)).toEqual(["15", "23"])
  })
  it("keeps phases A, B and E manual until the backbone is proven", () => {
    expect(STEP_REGISTRY.filter((step) => step.automation === "manual").map((step) => step.phase)).toEqual(
      expect.arrayContaining(["A", "B", "E"])
    )
    expect(STEP_REGISTRY.filter((step) => ["C", "D", "F"].includes(step.phase)).every((step) => step.automation === "automated")).toBe(true)
  })
  it("selects steps for the requested phases only, keeping protocol order", () => {
    expect(stepsForPhases(["D", "C"]).map((step) => step.id)).toEqual(["08", "09", "10", "11", "12", "13", "14", "15", "16"])
  })
  it("attaches a gate to every automated step of phases C, D and F", () => {
    expect(STEP_REGISTRY.filter((step) => ["C", "D", "F"].includes(step.phase)).every((step) => Boolean(step.gate))).toBe(true)
  })
})

describe("prompt catalog", () => {
  it("extracts the twenty-five prompt bodies from the canonical wiki template", () => {
    expect([...catalog.keys()]).toHaveLength(25)
    expect(catalog.get("09")?.title).toContain("Scrittura")
  })
  it("keeps the prompt body without the surrounding code fence", () => {
    const prompt = catalog.get("10")
    expect(prompt?.body.startsWith("```")).toBe(false)
    expect(prompt?.body).toContain("[CHAPTER_FILE]")
  })
  it("captures the gate declared under each prompt", () => {
    expect(catalog.get("10")?.gate).toContain("blocker")
  })
  it("fails when the template holds no prompt, instead of returning silence", () => {
    expect(() => loadPromptCatalog("# Nessun prompt qui")).toThrow(/nessun prompt/i)
  })
})

describe("renderPrompt", () => {
  it("substitutes every placeholder of a chapter prompt", () => {
    const rendered = renderPrompt(catalog, "09", values)
    expect(rendered).toContain(values.CHAPTER_FILE)
    expect(rendered).not.toMatch(/\[[A-Z_]{4,}\]/)
  })
  it("renders all twenty-five prompts with a complete value set", () => {
    expect(() => [...catalog.keys()].forEach((id) => renderPrompt(catalog, id, values))).not.toThrow()
  })
  it("refuses to render when a placeholder has no value", () => {
    expect(() => renderPrompt(catalog, "09", { ...values, CHAPTER_FILE: "" })).toThrow(/CHAPTER_FILE/)
  })
  it("names the missing placeholders in the error, so the sheet can be fixed", () => {
    expect(() => renderPrompt(catalog, "05", { ...values, MODULE_CODE: "", CUT_OFF_DATE: "" })).toThrow(
      /MODULE_CODE[\s\S]*CUT_OFF_DATE|CUT_OFF_DATE[\s\S]*MODULE_CODE/
    )
  })
  it("fails on an unknown prompt id", () => {
    expect(() => renderPrompt(catalog, "99", values)).toThrow(/99/)
  })
})
