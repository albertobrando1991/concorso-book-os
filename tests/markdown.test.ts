import { describe, expect, it } from "vitest"
import { appendToHeadingSection, extractWikiLinks, replaceHeadingSection } from "@/src/server/wiki/markdown"

describe("markdown section operations", () => {
  it("replaces only the requested heading body", () => {
    const updated = replaceHeadingSection(
      "# Note\n\n## Sintesi\nold\n\n## Fonti\n- A",
      "Sintesi",
      "new"
    )

    expect(updated).toContain("## Sintesi\n\nnew")
    expect(updated).toContain("## Fonti\n- A")
    expect(updated).not.toContain("old")
  })

  it("appends to an existing heading section", () => {
    const updated = appendToHeadingSection(
      "# Note\n\n## Fonti\n- A\n\n## Stato revisione\nok",
      "Fonti",
      "- B"
    )

    expect(updated).toContain("## Fonti\n- A\n\n- B")
    expect(updated).toContain("## Stato revisione")
  })

  it("extracts obsidian wiki links", () => {
    expect(extractWikiLinks("[[topics/metodo-bando]] and [[bando-decoder|Bando Decoder]]")).toEqual([
      "topics/metodo-bando",
      "bando-decoder"
    ])
  })
})

