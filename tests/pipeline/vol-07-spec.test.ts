import path from "node:path"
import { describe, expect, it } from "vitest"
import { loadVolumeSpec } from "../../src/pipeline/spec/load-volume-spec"

describe("VOL-07 pipeline spec", () => {
  it("loads the real sheet with the approved roles, phases and module order", async () => {
    const loaded = await loadVolumeSpec({
      wikiRoot: path.resolve(process.cwd(), "wiki"),
      volumeCode: "VOL-07"
    })

    expect(loaded.issues).toEqual([])
    expect(loaded.spec).toMatchObject({
      volumeCode: "VOL-07",
      volumeTitle: "Sanità amministrativa e professioni sanitarie",
      cutOffDate: "2026-07-28",
      responsabileNormativo: "Alberto Brando",
      responsabileEditoriale: "Alberto Brando",
      writerProvider: "codex",
      phases: ["A", "B"]
    })
    expect(loaded.spec.modules.map((module) => [module.code, module.priority, module.phases])).toEqual([
      ["M-SA02", 1, ["A", "B"]],
      ["M-SA01", 2, ["A", "B"]],
      ["M-SA03", 3, ["A", "B"]],
      ["M-SA04", 4, ["A", "B"]]
    ])
    expect(loaded.spec.modules.every((module) => module.chaptersSource === "derived")).toBe(true)
  })
})
