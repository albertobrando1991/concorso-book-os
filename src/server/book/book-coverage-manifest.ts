import { createHash } from "node:crypto"
import {
  BOOK_COVERAGE_REGISTRY,
  BOOK_COVERAGE_TAXONOMY_VERSION,
  type BookCoverageRegistryRow
} from "../../catalog/book-coverage-registry"
import { TEXT_VOLUME_CATALOG } from "../../catalog/text-volumes"

export const BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION = "book-os-coverage/v1" as const

export interface BookCoverageManifestV1 {
  schemaVersion: typeof BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION
  manifestId: string
  manifestDigest: string
  taxonomyVersion: typeof BOOK_COVERAGE_TAXONOMY_VERSION
  source: {
    repository: string
    commit: string
  }
  catalogDigest: string
  registryDigest: string
  catalog: {
    volumeCount: number
    moduleCount: number
    volumes: Array<{
      code: string
      title: string
      shortTitle: string
      modules: string[]
      bookIds: string[]
    }>
  }
  coverage: {
    rowCount: number
    eligibleRowCount: number
    rows: BookCoverageRegistryRow[]
  }
}

export function buildBookCoverageManifest(input: {
  repository: string
  sourceSha: string
}): BookCoverageManifestV1 {
  const sourceSha = input.sourceSha.trim().toLowerCase()

  if (!/^[0-9a-f]{40}$/.test(sourceSha)) {
    throw new Error("sourceSha deve essere uno SHA Git completo di 40 caratteri esadecimali.")
  }

  const catalog = {
    volumeCount: TEXT_VOLUME_CATALOG.length,
    moduleCount: TEXT_VOLUME_CATALOG.reduce((count, volume) => count + volume.modules.length, 0),
    volumes: TEXT_VOLUME_CATALOG.map((volume) => ({
      code: volume.code,
      title: volume.title,
      shortTitle: volume.shortTitle,
      modules: [...volume.modules],
      bookIds: [...volume.bookIds]
    }))
  }
  const rows = BOOK_COVERAGE_REGISTRY.map(cloneCoverageRow)
  const eligibleRowCount = rows.filter(isEligibleCoverageRow).length
  const catalogDigest = sha256(stableStringify(catalog))
  const registryDigest = sha256(stableStringify(rows))
  const unsigned = {
    schemaVersion: BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION,
    manifestId: `${BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION}:${sourceSha}`,
    taxonomyVersion: BOOK_COVERAGE_TAXONOMY_VERSION,
    source: {
      repository: input.repository,
      commit: sourceSha
    },
    catalogDigest,
    registryDigest,
    catalog,
    coverage: {
      rowCount: rows.length,
      eligibleRowCount,
      rows
    }
  }

  return {
    ...unsigned,
    manifestDigest: sha256(stableStringify(unsigned))
  }
}

export function validateBookCoverageManifest(manifest: unknown): string[] {
  const issues: string[] = []
  const value = manifest as Partial<BookCoverageManifestV1> | null

  if (!value || typeof value !== "object") return ["Il manifest deve essere un oggetto JSON."]
  if (value.schemaVersion !== BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION) issues.push("schemaVersion non supportata.")
  if (value.taxonomyVersion !== BOOK_COVERAGE_TAXONOMY_VERSION) issues.push("taxonomyVersion non supportata.")
  if (value.manifestId !== `${BOOK_COVERAGE_MANIFEST_SCHEMA_VERSION}:${String(value.source?.commit || "")}`) {
    issues.push("manifestId non corrispondente alla sorgente.")
  }
  if (!value.source?.repository?.trim()) issues.push("source.repository mancante.")
  if (!/^[0-9a-f]{40}$/.test(String(value.source?.commit || ""))) issues.push("source.commit non valido.")
  if (!/^[0-9a-f]{64}$/.test(String(value.manifestDigest || ""))) issues.push("manifestDigest non valido.")
  if (!/^[0-9a-f]{64}$/.test(String(value.catalogDigest || ""))) issues.push("catalogDigest non valido.")
  if (!/^[0-9a-f]{64}$/.test(String(value.registryDigest || ""))) issues.push("registryDigest non valido.")

  const volumes = value.catalog?.volumes
  if (value.catalog?.volumeCount !== 12 || volumes?.length !== 12) issues.push("Il catalogo deve avere 12 volumi.")
  if (value.catalog?.moduleCount !== 25) issues.push("Il catalogo deve avere 25 moduli.")

  const rows = value.coverage?.rows
  if (!Array.isArray(rows)) {
    issues.push("coverage.rows deve essere un array.")
  } else {
    if (value.coverage?.rowCount !== rows.length) issues.push("rowCount non corrisponde alle righe.")
    const eligible = rows.filter(isEligibleCoverageRow).length
    if (value.coverage?.eligibleRowCount !== eligible) issues.push("eligibleRowCount non corrisponde alle righe approvate e verificate.")
    const modulesByVolume = new Map((volumes || []).map((volume) => [volume.code, new Set(volume.modules)]))
    const ids = new Set<string>()

    for (const row of rows) {
      if (!row.id || ids.has(row.id)) issues.push(`ID coverage mancante o duplicato: ${row.id || "missing"}.`)
      ids.add(row.id)
      const volumeModules = modulesByVolume.get(row.volumeCode)
      if (!volumeModules) issues.push(`Volume coverage sconosciuto: ${row.volumeCode}.`)
      if (!Array.isArray(row.moduleCodes) || row.moduleCodes.some((moduleCode) => !volumeModules?.has(moduleCode))) {
        issues.push(`Coverage ${row.id} contiene moduli esterni a ${row.volumeCode}.`)
      }
      if (row.status === "verified" && row.reviewStatus === "approved") {
        if (!Array.isArray(row.subjectSlugs) || row.subjectSlugs.length === 0) {
          issues.push(`Coverage ${row.id} approvata senza subjectSlugs.`)
        }
        if (!row.verifiedAt || !row.validAsOf) issues.push(`Coverage ${row.id} approvata senza date di verifica.`)
        if (!Array.isArray(row.profileScope) || row.profileScope.length === 0 || !Array.isArray(row.examOutputs) || row.examOutputs.length === 0) {
          issues.push(`Coverage ${row.id} approvata senza ambito profilo o prova.`)
        }
        if (!Array.isArray(row.chapterRefs) || row.chapterRefs.length === 0 || !Array.isArray(row.sourceRefs) || row.sourceRefs.length === 0) {
          issues.push(`Coverage ${row.id} approvata senza evidenze.`)
        }
      }
    }
  }

  if (hasCompleteManifestShape(value)) {
    if (sha256(stableStringify(value.catalog)) !== value.catalogDigest) issues.push("catalogDigest non corrispondente.")
    if (sha256(stableStringify(value.coverage.rows)) !== value.registryDigest) issues.push("registryDigest non corrispondente.")
    const { manifestDigest, ...unsigned } = value
    if (sha256(stableStringify(unsigned)) !== manifestDigest) issues.push("manifestDigest non corrispondente.")
  }

  return [...new Set(issues)]
}

export function assertValidBookCoverageManifest(manifest: unknown) {
  const issues = validateBookCoverageManifest(manifest)

  if (issues.length > 0) {
    throw new Error(`Manifest non conforme a book-os-coverage/v1:\n- ${issues.join("\n- ")}`)
  }
}

export function isEligibleCoverageRow(row: BookCoverageRegistryRow) {
  return row.status === "verified" &&
    row.reviewStatus === "approved" &&
    Array.isArray(row.subjectSlugs) &&
    row.subjectSlugs.length > 0 &&
    Array.isArray(row.profileScope) &&
    row.profileScope.length > 0 &&
    Array.isArray(row.examOutputs) &&
    row.examOutputs.length > 0
}

export function stableStringify(value: unknown, space?: number) {
  return JSON.stringify(sortJson(value), null, space)
}

function cloneCoverageRow(row: BookCoverageRegistryRow): BookCoverageRegistryRow {
  return {
    ...row,
    moduleCodes: [...row.moduleCodes],
    subjectSlugs: [...row.subjectSlugs],
    concepts: [...row.concepts],
    profileScope: [...row.profileScope],
    examOutputs: [...row.examOutputs],
    chapterRefs: [...row.chapterRefs],
    exclusions: [...row.exclusions],
    sourceRefs: [...row.sourceRefs]
  }
}

function hasCompleteManifestShape(value: Partial<BookCoverageManifestV1>): value is BookCoverageManifestV1 {
  return Boolean(
    value.schemaVersion &&
    value.manifestId &&
    value.manifestDigest &&
    value.taxonomyVersion &&
    value.source &&
    value.catalogDigest &&
    value.registryDigest &&
    value.catalog &&
    value.coverage
  )
}

function sha256(value: string) {
  return createHash("sha256").update(value).digest("hex")
}

function sortJson(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(sortJson)
  if (!value || typeof value !== "object") return value

  return Object.fromEntries(
    Object.entries(value as Record<string, unknown>)
      .sort(([left], [right]) => left.localeCompare(right))
      .map(([key, child]) => [key, sortJson(child)])
  )
}
