import { describe, expect, it } from "vitest"
import { resolvePageAuditOptions } from "@/scripts/book-studio-page-audit-core.mjs"

describe("page audit screenshot policy", () => {
  it("can skip duplicate page screenshots while preserving contact sheets", () => {
    expect(resolvePageAuditOptions({
      BOOK_STUDIO_SKIP_PAGE_SCREENSHOTS: "1"
    }).skipPageScreenshots).toBe(true)

    expect(resolvePageAuditOptions({}).skipPageScreenshots).toBe(false)
  })
})
