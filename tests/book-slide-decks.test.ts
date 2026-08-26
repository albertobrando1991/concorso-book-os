import path from "node:path"
import { describe, expect, it } from "vitest"

import { compileStudentSlideDeckFile } from "@/src/server/book/book-slide-decks"

const PROJECT_ROOT = path.resolve(".")
const SAMPLE_DECK = "slides/VOL-01/01-il-nuovo-candidato-pubblico/index.html"

describe("student slide decks", () => {
  it("builds a deterministic self-contained deck without the staff editor", async () => {
    const first = await compileStudentSlideDeckFile(PROJECT_ROOT, SAMPLE_DECK)
    const second = await compileStudentSlideDeckFile(PROJECT_ROOT, SAMPLE_DECK)
    const html = first.bytes.toString("utf8")

    expect(first.bytes.equals(second.bytes)).toBe(true)
    expect(first.slideCount).toBeGreaterThanOrEqual(16)
    expect(first.sourcePaths).toContain(SAMPLE_DECK)
    expect(html).toContain('Content-Security-Policy')
    expect(html).toContain('img-src data:')
    expect(html).toContain('src="data:image/png;base64,')
    expect(html).not.toContain('fonts.googleapis.com')
    expect(html).not.toMatch(/<button\b[^>]*edit-toggle/i)
    expect(html).not.toMatch(/<div\b[^>]*edit-hotzone/i)
    expect(html).not.toContain('localStorage')
    expect(html).not.toMatch(/<[^>]+\scontenteditable\s*=/i)
    expect(html).not.toMatch(/(?:src|href)="https?:/i)
  })

  it("rejects paths outside the canonical slide tree", async () => {
    await expect(compileStudentSlideDeckFile(PROJECT_ROOT, "../secrets.html"))
      .rejects.toThrow("Path repository non sicuro")
  })
})
