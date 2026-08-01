import { describe, expect, it } from "vitest"
import { promptValuesFor } from "../../src/pipeline/cli/commands"
import type { VolumeSpec } from "../../src/pipeline/spec/parse-volume-spec"
import type { StepRecord } from "../../src/pipeline/state/types"

const spec = {
  volumeCode: "VOL-07",
  volumeTitle: "Sanità amministrativa e professioni sanitarie",
  cutOffDate: "2026-07-28",
  responsabileNormativo: "Alberto Brando",
  modules: [
    { code: "M-SA02", moduleId: "moduli/m-sa02-professioni-sanitarie" },
    { code: "M-SA01", moduleId: "moduli/m-sa01-sanita-amministrativa" }
  ]
} as VolumeSpec

const catalogStep = {
  key: "00:VOL-07",
  id: "00",
  phase: "A",
  scope: "catalog",
  target: "VOL-07",
  status: "pending",
  attempts: 0,
  evidence: []
} as StepRecord

describe("promptValuesFor", () => {
  it("supplies the real module set to a catalog-scoped prompt", () => {
    expect(promptValuesFor(spec, catalogStep)).toMatchObject({
      MODULE_CODE: "M-SA02, M-SA01",
      MODULE_ID: "moduli/m-sa02-professioni-sanitarie, moduli/m-sa01-sanita-amministrativa"
    })
  })
})
