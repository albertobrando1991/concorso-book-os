export const BOOK_COVERAGE_TAXONOMY_VERSION = "concorso-book/12-volumes-25-modules/2026-07-14" as const

export type BookCoverageDepth = "orientation" | "essential" | "advanced"
export type BookCoverageStatus = "verified" | "partial" | "planned" | "unverified"
export type BookCoverageReviewStatus = "approved" | "pending" | "rejected"

export interface BookCoverageRegistryRow {
  id: string
  volumeCode: string
  moduleCodes: string[]
  subject: string
  subjectSlugs: string[]
  concepts: string[]
  profileScope: string[]
  examOutputs: string[]
  depth: BookCoverageDepth
  status: BookCoverageStatus
  chapterRefs: string[]
  exclusions: string[]
  sourceRefs: string[]
  verifiedAt: string | null
  validAsOf: string | null
  reviewStatus: BookCoverageReviewStatus
}

/**
 * Seed intenzionalmente vuoto e fail-closed.
 *
 * Le note di architettura e il catalogo commerciale non dimostrano che un
 * volume copra un argomento. Aggiungere una riga soltanto dopo aver verificato
 * capitoli, fonti e profondita, impostando insieme status=verified e
 * reviewStatus=approved, almeno un subjectSlug canonico e ambiti espliciti per
 * profilo e tipo di prova. Usare "all" solo dopo una verifica realmente
 * trasversale. Tutte le altre combinazioni restano informative e non possono
 * alimentare raccomandazioni confermate.
 */
export const BOOK_COVERAGE_REGISTRY: readonly BookCoverageRegistryRow[] = []
