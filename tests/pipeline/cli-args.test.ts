import { describe, expect, it } from "vitest"
import { parseArgs } from "../../src/pipeline/cli/args"

describe("pipeline CLI arguments", () => {
  it("parses an audited cascade reopen request", () => {
    expect(
      parseArgs(["reopen", "VOL-08", "--step", "08", "--module", "M-TR01", "--cascade", "--note", "Retrofit formato 2 autorizzato"])
    ).toMatchObject({
      command: "reopen",
      volumeCode: "VOL-08",
      step: "08",
      module: "M-TR01",
      cascade: true,
      note: "Retrofit formato 2 autorizzato"
    })
  })

  it("rejects an inline cascade value because cascade is boolean", () => {
    expect(() => parseArgs(["reopen", "VOL-08", "--cascade=true"])).toThrow(/cascade.*boolean|boolean.*cascade/i)
  })
})
