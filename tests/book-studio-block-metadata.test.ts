import { describe, expect, it } from "vitest"
import { getPreviewBlockMetadata } from "@/src/server/book/book-preview-block-metadata"

describe("Book Studio block metadata", () => {
  it("repeats and charges headers on continued table fragments", () => {
    expect(getPreviewBlockMetadata({
      type: "table",
      continued: true,
      headers: ["Voce", "Regola"]
    })).toEqual({
      blockType: "table",
      continued: true,
      showTableHeader: true,
      tableHeaderCost: 24
    })
  })

  it("exposes paragraph continuation without table presentation", () => {
    expect(getPreviewBlockMetadata({
      type: "paragraph",
      continued: true
    })).toEqual({
      blockType: "paragraph",
      continued: true,
      showTableHeader: false,
      tableHeaderCost: 0
    })
  })

  it("does not invent a table header when the source has no columns", () => {
    expect(getPreviewBlockMetadata({
      type: "table",
      continued: true,
      headers: []
    })).toEqual({
      blockType: "table",
      continued: true,
      showTableHeader: false,
      tableHeaderCost: 0
    })
  })
})
