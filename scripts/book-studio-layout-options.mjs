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

export async function waitForStableBookPageCount(page, options = {}) {
  const selector = options.selector || ".bookPages .bookPage"
  const stableReadings = options.stableReadings ?? 3
  const intervalMs = options.intervalMs ?? 250
  const confirmationDelayMs = options.confirmationDelayMs ?? 1_500
  const maxReadings = options.maxReadings ?? 20
  let previous = null
  let streak = 0

  for (let reading = 0; reading < maxReadings; reading += 1) {
    const current = await page.locator(selector).count()

    if (current > 0 && current === previous) {
      streak += 1
    } else {
      previous = current
      streak = current > 0 ? 1 : 0
    }

    if (streak >= stableReadings) {
      await page.waitForTimeout(confirmationDelayMs)
      const confirmation = await page.locator(selector).count()
      if (confirmation === current) return current
      previous = confirmation
      streak = confirmation > 0 ? 1 : 0
      continue
    }
    if (reading < maxReadings - 1) await page.waitForTimeout(intervalMs)
  }

  throw new Error(
    "Conteggio pagine Book Studio non stabile dopo " +
      maxReadings +
      " letture (ultimo valore: " +
      (previous ?? 0) +
      ")"
  )
}
