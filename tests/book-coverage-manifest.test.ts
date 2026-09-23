import { readFile } from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import {
  BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION,
  buildBookCoverageManifest,
  isEligibleCoverageRow,
  stableStringify,
  validateBookCoverageManifest
} from "@/src/server/book/book-coverage-manifest"
import type { BookCoverageRegistryRow } from "@/src/catalog/book-coverage-registry"

const PROJECT_ROOT = path.resolve(".")
const SOURCE_SHA = "b".repeat(40)
const REPOSITORY = "https://github.com/albertobrando1991/concorso-book-os.git"

describe("Book OS coverage manifest v1", () => {
  it("builds a deterministic fail-closed manifest from the canonical catalog", () => {
    const first = buildBookCoverageManifest({ repository: REPOSITORY, sourceSha: SOURCE_SHA })
    const second = buildBookCoverageManifest({ repository: REPOSITORY, sourceSha: SOURCE_SHA })

    expect(first.schemaVersion).toBe(BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION)
    expect(first.source).toEqual({ repository: REPOSITORY, commit: SOURCE_SHA })
    expect(first.catalog.volumeCount).toBe(12)
    expect(first.catalog.moduleCount).toBe(25)
    expect(first.catalog.volumes).toHaveLength(12)
    expect(first.coverage.rowCount).toBe(0)
    expect(first.coverage.eligibleRowCount).toBe(0)
    expect(first.manifestDigest).toBe(second.manifestDigest)
    expect(stableStringify(first)).toBe(stableStringify(second))
    expect(validateBookCoverageManifest(first)).toEqual([])
  })

  it("counts only rows that are both verified and approved", () => {
    const verifiedApproved = row({ status: "verified", reviewStatus: "approved" })

    expect(isEligibleCoverageRow(verifiedApproved)).toBe(true)
    expect(isEligibleCoverageRow(row({ status: "partial", reviewStatus: "approved" }))).toBe(false)
    expect(isEligibleCoverageRow(row({ status: "verified", reviewStatus: "pending" }))).toBe(false)
    expect(isEligibleCoverageRow(row({ subjectSlugs: [] }))).toBe(false)
    expect(isEligibleCoverageRow(row({ profileScope: [] }))).toBe(false)
    expect(isEligibleCoverageRow(row({ examOutputs: [] }))).toBe(false)
  })

  it("detects digest tampering, missing joins and modules outside the declared volume", () => {
    const manifest = buildBookCoverageManifest({ repository: REPOSITORY, sourceSha: SOURCE_SHA })
    const tampered = structuredClone(manifest)
    tampered.catalog.volumes[0].title = "Titolo manomesso"
    expect(validateBookCoverageManifest(tampered)).toContain("catalogDigest non corrispondente.")

    const invalidCoverage = structuredClone(manifest)
    invalidCoverage.coverage.rows.push(row({
      subjectSlugs: [],
      moduleCodes: ["M-FC01"],
      chapterRefs: [],
      sourceRefs: []
    }))
    invalidCoverage.coverage.rowCount = 1
    invalidCoverage.coverage.eligibleRowCount = 0
    expect(validateBookCoverageManifest(invalidCoverage)).toEqual(expect.arrayContaining([
      "Coverage row-1 approvata senza subjectSlugs.",
      "Coverage row-1 contiene moduli esterni a VOL-01.",
      "Coverage row-1 approvata senza evidenze.",
      "manifestDigest non corrispondente."
    ]))
  })

  it("ships the matching draft 2020-12 JSON Schema", async () => {
    const schema = JSON.parse(await readFile(
      path.join(PROJECT_ROOT, "schemas", "book-os-coverage-v1.schema.json"),
      "utf8"
    )) as { $schema: string; properties: { schemaVersion: { const: string } } }

    expect(schema.$schema).toBe("https://json-schema.org/draft/2020-12/schema")
    expect(schema.properties.schemaVersion.const).toBe(BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION)
  })
})

function row(overrides: Partial<BookCoverageRegistryRow> = {}): BookCoverageRegistryRow {
  return {
    id: "row-1",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "diritto-amministrativo",
    subjectSlugs: ["diritto-amministrativo"],
    concepts: ["procedimento-amministrativo"],
    profileScope: ["pa-generalista"],
    examOutputs: ["written", "oral"],
    depth: "essential",
    status: "verified",
    chapterRefs: ["wiki/books/il-metodo-bando/chapters/chapter-05.md"],
    exclusions: [],
    sourceRefs: ["wiki/sources/example.md"],
    verifiedAt: "2026-09-23T00:00:00.000Z",
    validAsOf: "2026-09-23T00:00:00.000Z",
    reviewStatus: "approved",
    ...overrides
  }
}
