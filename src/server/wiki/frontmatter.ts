import type { BaseFrontmatter } from "./types"

export interface ParsedMarkdown {
  data: Partial<BaseFrontmatter>
  body: string
}

export function parseFrontmatter(content: string): ParsedMarkdown {
  const normalized = content.replace(/^\uFEFF/, "").replace(/\r\n/g, "\n")

  if (!normalized.startsWith("---\n")) {
    return { data: {}, body: normalized }
  }

  const closingIndex = normalized.indexOf("\n---\n", 4)

  if (closingIndex === -1) {
    return { data: {}, body: normalized }
  }

  const yaml = normalized.slice(4, closingIndex)
  const body = normalized.slice(closingIndex + 5)
  const data: Partial<BaseFrontmatter> = {}

  for (const line of yaml.split("\n")) {
    const separatorIndex = line.indexOf(":")

    if (separatorIndex === -1) continue

    const key = line.slice(0, separatorIndex).trim()
    const rawValue = line.slice(separatorIndex + 1).trim()

    data[key] = parseYamlValue(rawValue)
  }

  return { data, body }
}

export function stringifyFrontmatter(data: Record<string, unknown>) {
  const lines = Object.entries(data)
    .filter(([, value]) => value !== undefined)
    .map(([key, value]) => `${key}: ${stringifyYamlValue(value)}`)

  return `---\n${lines.join("\n")}\n---\n`
}

export function withFrontmatter(data: Record<string, unknown>, body: string) {
  return `${stringifyFrontmatter(data)}\n${body.trim()}\n`
}

export function mergeFrontmatter(content: string, patch: Record<string, unknown>) {
  const parsed = parseFrontmatter(content)
  return withFrontmatter(
    {
      ...parsed.data,
      ...patch
    },
    parsed.body
  )
}

function parseYamlValue(rawValue: string): unknown {
  if (rawValue === "") return ""
  if (rawValue === "true") return true
  if (rawValue === "false") return false
  if (/^-?\d+(\.\d+)?$/.test(rawValue)) return Number(rawValue)

  if (rawValue.startsWith("[") && rawValue.endsWith("]")) {
    try {
      return JSON.parse(rawValue)
    } catch {
      return rawValue
        .slice(1, -1)
        .split(",")
        .map((item) => stripQuotes(item.trim()))
        .filter(Boolean)
    }
  }

  return stripQuotes(rawValue)
}

function stringifyYamlValue(value: unknown): string {
  if (Array.isArray(value)) {
    return JSON.stringify(value)
  }

  if (typeof value === "boolean" || typeof value === "number") {
    return String(value)
  }

  if (value === null) return "null"

  const text = String(value)

  if (text === "" || /[:#\[\]{},"\n]/.test(text) || text !== text.trim()) {
    return JSON.stringify(text)
  }

  return text
}

function stripQuotes(value: string) {
  if (
    (value.startsWith('"') && value.endsWith('"')) ||
    (value.startsWith("'") && value.endsWith("'"))
  ) {
    return value.slice(1, -1)
  }

  return value
}

