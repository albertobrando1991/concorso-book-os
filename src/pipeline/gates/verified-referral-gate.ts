import { readFile } from "node:fs/promises"
import path from "node:path"
import { extractWikiLinks } from "../../server/wiki/markdown"
import type { GateIssue, GateResult } from "../state/types"
import { headingsOf } from "./chapter-lint-gate"

export interface VerifiedReferralGateInput {
  content: string
  wikiRoot: string
  chapterPath: string
}

const VOL01_PREFIX = "books/il-metodo-bando/"

export async function runVerifiedReferralGate(input: VerifiedReferralGateInput): Promise<GateResult> {
  const blockers: GateIssue[] = []
  const links = extractWikiLinks(input.content).filter((link) => link.startsWith(VOL01_PREFIX))
  const baseRoot = path.resolve(input.wikiRoot, "books", "il-metodo-bando")

  for (const link of links) {
    const [target, rawHeading = ""] = link.split("#", 2)
    const relativeTarget = target.endsWith(".md") ? target : `${target}.md`
    const absolute = path.resolve(input.wikiRoot, ...relativeTarget.split("/"))
    const at = (message: string): GateIssue => ({
      code: "rinvio-non-risolto",
      message: `${message}: [[${link}]].`,
      location: input.chapterPath
    })

    if (!rawHeading || !absolute.startsWith(`${baseRoot}${path.sep}`)) {
      blockers.push(at("Il rinvio a VOL-01 deve indicare un file ammesso e un heading preciso"))
      continue
    }

    const targetContent = await readFile(absolute, "utf8").catch(() => null)
    if (targetContent === null) {
      blockers.push(at("Il file di destinazione non esiste"))
      continue
    }

    const wanted = normalizeHeading(decodeURIComponent(rawHeading))
    const found = headingsOf(targetContent).some((heading) => normalizeHeading(heading.text) === wanted)
    if (!found) blockers.push(at("L'heading di destinazione non esiste"))
  }

  return { passed: blockers.length === 0, blockers, warnings: [] }
}

function normalizeHeading(value: string) {
  return value.trim().replace(/\s+/g, " ").toLocaleLowerCase("it")
}
