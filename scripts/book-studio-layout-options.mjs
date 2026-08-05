const DEFAULT_CASES = [
  { id: "il-metodo-bando", label: "base" },
  { id: "moduli/m-fc01-ministeri", label: "m-fc01" }
]

export function resolveBookStudioLayoutOptions(env = process.env) {
  const ids = String(env.BOOK_STUDIO_BOOK_IDS || "")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean)
  const cases = ids.length > 0
    ? ids.map((id) => ({ id, label: id.split("/").at(-1) || "book" }))
    : DEFAULT_CASES
  const expectedCounts = env.BOOK_STUDIO_EXPECTED_COUNTS
    ? JSON.parse(env.BOOK_STUDIO_EXPECTED_COUNTS)
    : null

  if (expectedCounts) {
    for (const key of ["frontMatter", "moduleOpenings", "chapters", "nuclei"]) {
      if (!Number.isInteger(expectedCounts[key]) || expectedCounts[key] < 0) {
        throw new Error(`Conteggio atteso non valido: ${key}`)
      }
    }
  }

  return {
    cases,
    artifactPrefix: String(env.BOOK_STUDIO_ARTIFACT_PREFIX || "book-studio"),
    expectedCounts
  }
}
