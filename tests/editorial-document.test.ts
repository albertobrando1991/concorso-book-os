import { describe, expect, it } from "vitest"
import {
  isLegacyEditorialPlanPath,
  isStaffOnlyBookDocument
} from "@/src/server/wiki/editorial-document"

describe("editorial document visibility", () => {
  it("recognizes the legacy module plan path", () => {
    expect(isLegacyEditorialPlanPath("books/moduli/m-sa01/chapters/00-piano-editoriale.md")).toBe(true)
  })

  it("recognizes canonical staff-only metadata", () => {
    expect(isStaffOnlyBookDocument("books/moduli/m-sa01/chapters/altro.md", { type: "editorial_plan" })).toBe(true)
    expect(isStaffOnlyBookDocument("books/moduli/m-sa01/chapters/altro.md", {
      tags: ["specialist-module-plan"]
    })).toBe(true)
  })

  it("keeps a real numbered chapter visible", () => {
    expect(isStaffOnlyBookDocument("books/moduli/m-sa01/chapters/04-atti.md", {
      type: "book_chapter",
      outline_section: 4
    })).toBe(false)
  })
})
