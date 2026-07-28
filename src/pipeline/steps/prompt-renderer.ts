export const PROMPT_TEMPLATE_PATH = "wiki/templates/prompt-staff-revisione-completa-volumi.md"

export interface PromptDefinition {
  id: string
  title: string
  body: string
  gate: string
}

export type PromptCatalog = Map<string, PromptDefinition>
export type PromptValues = Record<string, string>

const PROMPT_HEADING = /^##\s+Prompt\s+(\d{2})\s*[—-]\s*(.+?)\s*$/
const FENCE = /^```/
const GATE_LINE = /^Gate\s*:\s*(.+?)\s*$/i
const PLACEHOLDER = /\[([A-Z][A-Z0-9_]{2,})\]/g

export function loadPromptCatalog(markdown: string): PromptCatalog {
  const lines = markdown.replace(/^﻿/, "").replace(/\r\n/g, "\n").split("\n")
  const catalog: PromptCatalog = new Map()

  for (let index = 0; index < lines.length; index += 1) {
    const heading = PROMPT_HEADING.exec(lines[index])

    if (!heading) continue

    const prompt = readPrompt(lines, index + 1)

    if (prompt) catalog.set(heading[1], { id: heading[1], title: heading[2], ...prompt })
  }

  if (!catalog.size) {
    throw new Error(
      `Nessun prompt trovato nel template: atteso il formato "## Prompt NN — titolo" seguito da un blocco di codice in ${PROMPT_TEMPLATE_PATH}.`
    )
  }

  return catalog
}

export function renderPrompt(catalog: PromptCatalog, id: string, values: PromptValues) {
  const prompt = catalog.get(id)

  if (!prompt) {
    throw new Error(`Prompt ${id} assente dal template ${PROMPT_TEMPLATE_PATH}: verifica l'id o aggiorna il template.`)
  }

  const missing = placeholdersOf(prompt.body).filter((name) => !values[name]?.trim())

  if (missing.length) {
    throw new Error(
      `Prompt ${id} non renderizzabile: mancano i valori per ${missing.join(", ")}. Completa la scheda del volume prima di eseguire lo step.`
    )
  }

  return prompt.body.replace(PLACEHOLDER, (match, name: string) => values[name] ?? match)
}

export function placeholdersOf(body: string) {
  return [...new Set(Array.from(body.matchAll(PLACEHOLDER), (match) => match[1]))]
}

function readPrompt(lines: string[], start: number) {
  const openIndex = lines.findIndex((line, index) => index >= start && FENCE.test(line.trim()))

  if (openIndex === -1) return null

  const closeIndex = lines.findIndex((line, index) => index > openIndex && FENCE.test(line.trim()))

  if (closeIndex === -1) return null

  return {
    body: lines.slice(openIndex + 1, closeIndex).join("\n").trim(),
    gate: readGate(lines, closeIndex + 1)
  }
}

function readGate(lines: string[], start: number) {
  for (let index = start; index < lines.length; index += 1) {
    if (PROMPT_HEADING.test(lines[index])) break

    const gate = GATE_LINE.exec(lines[index].replace(/\*\*/g, "").trim())

    if (gate) return gate[1]
  }

  return ""
}
