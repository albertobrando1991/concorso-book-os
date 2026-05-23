import type { SourceInput } from "../wiki/types"

export interface SourceSearchCandidate {
  url: string
  title: string
  snippet: string
  score: number
  source: string
}

export interface SourceSearchResult {
  query: string
  selected: SourceSearchCandidate
  candidates: SourceSearchCandidate[]
  searchedQueries: string[]
}

const DEFAULT_SEARCH_TIMEOUT_MS = 20000

const OFFICIAL_DOMAIN_SCORES: Array<[string, number]> = [
  ["normattiva.it", 75],
  ["gazzettaufficiale.it", 70],
  ["cortecostituzionale.it", 60],
  ["giustizia-amministrativa.it", 58],
  ["anticorruzione.it", 55],
  ["funzionepubblica.gov.it", 52],
  ["governo.it", 50],
  ["inpa.gov.it", 48],
  ["interno.gov.it", 46],
  ["mef.gov.it", 46],
  ["aranagenzia.it", 44],
  [".gov.it", 40],
  [".gov", 35]
]

export async function searchOfficialSource(input: {
  query: string
  sourceType?: SourceInput["sourceType"]
  fetchImpl?: typeof fetch
}): Promise<SourceSearchResult> {
  const query = cleanQuery(input.query)

  if (!query) {
    throw new Error("query is required when url is not provided")
  }

  const fetchImpl = input.fetchImpl || fetch
  const searchedQueries = buildSearchQueries(query, input.sourceType)
  const candidates: SourceSearchCandidate[] = []

  for (const searchQuery of searchedQueries) {
    const html = await fetchSearchHtml(searchQuery, fetchImpl)
    const parsed = parseDuckDuckGoHtml(html, "duckduckgo")
    candidates.push(...parsed.map((candidate) => scoreCandidate(candidate, query)))

    if (candidates.some((candidate) => candidate.score >= 90)) {
      break
    }
  }

  const ranked = dedupeCandidates(candidates)
    .sort((left, right) => right.score - left.score)
    .slice(0, 8)

  const selected = ranked[0]

  if (!selected) {
    throw new Error(`No document candidate found for query: ${query}`)
  }

  return {
    query,
    selected,
    candidates: ranked,
    searchedQueries
  }
}

export function buildSearchQueries(query: string, sourceType?: SourceInput["sourceType"]) {
  const normalized = cleanQuery(query)
  const officialHints = sourceType === "law" || sourceType === "decree"
    ? [
        `${normalized} site:normattiva.it`,
        `${normalized} site:gazzettaufficiale.it`,
        `${normalized} filetype:pdf site:gazzettaufficiale.it`
      ]
    : [
        `${normalized} filetype:pdf site:gov.it`,
        `${normalized} site:gov.it`
      ]

  return Array.from(new Set([...officialHints, `${normalized} filetype:pdf`, normalized]))
}

export function parseDuckDuckGoHtml(html: string, source: string): SourceSearchCandidate[] {
  const candidates: SourceSearchCandidate[] = []
  const anchorPattern = /<a\b[^>]*href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi
  let match: RegExpExecArray | null

  while ((match = anchorPattern.exec(html))) {
    const url = normalizeSearchUrl(match[1])
    const title = stripHtml(match[2])

    if (!url || !title || !isHttpUrl(url) || isSearchEngineUrl(url)) {
      continue
    }

    candidates.push({
      url,
      title,
      snippet: "",
      score: 0,
      source
    })
  }

  return candidates
}

export function findPdfLinks(html: string, pageUrl: string, query = "") {
  const links: SourceSearchCandidate[] = []
  const anchorPattern = /<a\b[^>]*href=["']([^"']+\.pdf(?:\?[^"']*)?)["'][^>]*>([\s\S]*?)<\/a>/gi
  let match: RegExpExecArray | null

  while ((match = anchorPattern.exec(html))) {
    const url = resolveUrl(match[1], pageUrl)
    const title = stripHtml(match[2]) || titleFromUrl(url)

    if (!url || !isHttpUrl(url)) {
      continue
    }

    links.push(scoreCandidate({
      url,
      title,
      snippet: "",
      score: 0,
      source: "page-pdf-link"
    }, query))
  }

  return dedupeCandidates(links).sort((left, right) => right.score - left.score)
}

export function scoreCandidate(candidate: SourceSearchCandidate, query: string): SourceSearchCandidate {
  const url = candidate.url.toLowerCase()
  const haystack = `${candidate.title} ${candidate.snippet} ${candidate.url}`.toLowerCase()
  const queryTokens = cleanQuery(query).toLowerCase().split(/\s+/).filter((token) => token.length > 2)
  let score = 10

  for (const [domain, value] of OFFICIAL_DOMAIN_SCORES) {
    if (url.includes(domain)) {
      score += value
      break
    }
  }

  if (url.includes(".pdf")) score += 25
  if (url.includes("download")) score += 8
  if (url.includes("allegati")) score += 6
  if (url.includes("legge") || url.includes("decreto") || url.includes("dlgs")) score += 5

  const matchingTokens = queryTokens.filter((token) => haystack.includes(token))
  score += matchingTokens.length * 4

  return { ...candidate, score }
}

async function fetchSearchHtml(query: string, fetchImpl: typeof fetch) {
  const controller = new AbortController()
  const timeoutMs = Number(process.env.HERMES_SOURCE_SEARCH_TIMEOUT_MS || DEFAULT_SEARCH_TIMEOUT_MS)
  const timer = setTimeout(() => controller.abort(), Number.isFinite(timeoutMs) ? timeoutMs : DEFAULT_SEARCH_TIMEOUT_MS)
  const url = `https://duckduckgo.com/html/?q=${encodeURIComponent(query)}`

  try {
    const response = await fetchImpl(url, {
      signal: controller.signal,
      headers: {
        Accept: "text/html,application/xhtml+xml",
        "User-Agent": "Mozilla/5.0 ConcorsoBookOS/1.0"
      }
    })

    if (!response.ok) {
      throw new Error(`Search failed ${response.status}: ${await response.text()}`)
    }

    return response.text()
  } finally {
    clearTimeout(timer)
  }
}

function dedupeCandidates(candidates: SourceSearchCandidate[]) {
  const byUrl = new Map<string, SourceSearchCandidate>()

  for (const candidate of candidates) {
    const key = candidate.url.replace(/#.*$/, "")
    const current = byUrl.get(key)

    if (!current || candidate.score > current.score) {
      byUrl.set(key, candidate)
    }
  }

  return Array.from(byUrl.values())
}

function normalizeSearchUrl(value: string) {
  const decoded = htmlDecode(value)
  const absolute = decoded.startsWith("//") ? `https:${decoded}` : decoded

  try {
    const url = new URL(absolute)
    const redirected = url.searchParams.get("uddg") || url.searchParams.get("u")

    if (redirected) {
      return decodeURIComponent(redirected)
    }

    return url.href
  } catch {
    return ""
  }
}

function resolveUrl(value: string, baseUrl: string) {
  try {
    return new URL(htmlDecode(value), baseUrl).href
  } catch {
    return ""
  }
}

function isSearchEngineUrl(value: string) {
  try {
    const host = new URL(value).hostname
    return host.includes("duckduckgo.com") || host.includes("google.com") || host.includes("bing.com")
  } catch {
    return true
  }
}

function isHttpUrl(value: string) {
  try {
    const url = new URL(value)
    return url.protocol === "http:" || url.protocol === "https:"
  } catch {
    return false
  }
}

function titleFromUrl(value: string) {
  try {
    const url = new URL(value)
    return decodeURIComponent(url.pathname.split("/").filter(Boolean).at(-1) || "documento")
      .replace(/\.[a-z0-9]+$/i, "")
      .replace(/[-_]+/g, " ")
  } catch {
    return "documento"
  }
}

function stripHtml(value: string) {
  return htmlDecode(value.replace(/<[^>]+>/g, " "))
    .replace(/\s+/g, " ")
    .trim()
}

function htmlDecode(value: string) {
  return value
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
}

function cleanQuery(value: string) {
  return value.replace(/\s+/g, " ").trim()
}
