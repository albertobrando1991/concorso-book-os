import { describe, expect, it, vi } from "vitest"
import {
  resolveBookStudioLayoutOptions,
  waitForStableBookPageCount
} from "@/scripts/book-studio-layout-options.mjs"

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

  it("waits until the rendered page count is stable across three readings", async () => {
    const counts = [592, 592, 593, 593, 593, 593]
    const count = vi.fn(async () => counts.shift() ?? 593)
    const waitForTimeout = vi.fn(async () => undefined)
    const page = {
      locator: vi.fn(() => ({ count })),
      waitForTimeout
    }

    await expect(waitForStableBookPageCount(page, {
      stableReadings: 3,
      intervalMs: 1,
      confirmationDelayMs: 1,
      maxReadings: 8
    })).resolves.toBe(593)
    expect(count).toHaveBeenCalledTimes(6)
    expect(waitForTimeout).toHaveBeenCalledTimes(5)
  })

  it("rejects a transient stable count that changes during delayed confirmation", async () => {
    const counts = [593, 593, 593, 592, 592, 592, 592]
    const count = vi.fn(async () => counts.shift() ?? 592)
    const waitForTimeout = vi.fn(async () => undefined)
    const page = {
      locator: vi.fn(() => ({ count })),
      waitForTimeout
    }

    await expect(waitForStableBookPageCount(page, {
      stableReadings: 3,
      intervalMs: 1,
      confirmationDelayMs: 1,
      maxReadings: 8
    })).resolves.toBe(592)
    expect(count).toHaveBeenCalledTimes(7)
  })

  it("rejects an impaginato whose page count never settles", async () => {
    const counts = [590, 591, 592, 593]
    const page = {
      locator: vi.fn(() => ({ count: vi.fn(async () => counts.shift() ?? 594) })),
      waitForTimeout: vi.fn(async () => undefined)
    }

    await expect(waitForStableBookPageCount(page, {
      stableReadings: 2,
      intervalMs: 1,
      maxReadings: 4
    })).rejects.toThrow("Conteggio pagine Book Studio non stabile")
  })
})
