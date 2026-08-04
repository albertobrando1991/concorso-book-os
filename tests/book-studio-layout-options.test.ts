import { describe, expect, it } from "vitest"
import { resolveBookStudioLayoutOptions } from "@/scripts/book-studio-layout-options.mjs"

describe("Book Studio layout verifier options", () => {
  it("targets VOL-07 with explicit counts and a stable artifact prefix", () => {
    expect(resolveBookStudioLayoutOptions({
      BOOK_STUDIO_BOOK_IDS: "volumi/vol-07",
      BOOK_STUDIO_ARTIFACT_PREFIX: "vol-07-step-19",
      BOOK_STUDIO_EXPECTED_COUNTS: JSON.stringify({
        frontMatter: 6,
        moduleOpenings: 4,
        chapters: 25,
        nuclei: 7
      })
    })).toEqual({
      cases: [{ id: "volumi/vol-07", label: "vol-07" }],
      artifactPrefix: "vol-07-step-19",
      expectedCounts: {
        frontMatter: 6,
        moduleOpenings: 4,
        chapters: 25,
        nuclei: 7
      }
    })
  })

  it("preserves the existing default cases", () => {
    const result = resolveBookStudioLayoutOptions({})

    expect(result.cases.map((item) => item.id)).toEqual([
      "il-metodo-bando",
      "moduli/m-fc01-ministeri"
    ])
    expect(result.artifactPrefix).toBe("book-studio")
    expect(result.expectedCounts).toBeNull()
  })
})
