import { readFile } from "node:fs/promises"
import path from "node:path"
import { beforeAll, describe, expect, it } from "vitest"
import {
  INTEGRATION_BUNDLE_SCHEMA_VERSION,
  IntegrationReleaseBlockedError,
  buildBookIntegrationBundle,
  stableStringify,
  validateBookIntegrationBundle
} from "@/src/server/book/book-integration-bundle"
import { buildBookStudioData, normalizeAssetPath } from "@/src/server/book/book-preview"
import { FileWikiStore } from "@/src/server/wiki/file-store"

const PROJECT_ROOT = path.resolve(".")
const SOURCE_SHA = "a".repeat(40)

describe("Book OS integration bundle v1", () => {
  let candidate: Awaited<ReturnType<typeof buildCandidate>>

  beforeAll(async () => {
    candidate = await buildCandidate()
  }, 60_000)

  it("builds a deterministic fail-closed VOL-01 candidate from the shared preview compiler", async () => {
    const first = candidate
    const second = await buildCandidate()

    expect(first.schemaVersion).toBe(INTEGRATION_BUNDLE_SCHEMA_VERSION)
    expect(first.bundleDigest).toBe(second.bundleDigest)
    expect(first.contentDigest).toBe(second.contentDigest)
    expect(stableStringify(first)).toBe(stableStringify(second))
    expect(validateBookIntegrationBundle(first)).toEqual([])

    expect(first.catalog.volumeCount).toBe(12)
    expect(first.catalog.volumes).toHaveLength(12)
    expect(first.catalog.moduleCount).toBe(25)
    expect(first.catalog.modules).toHaveLength(25)
    expect(new Set(first.catalog.modules.map((module) => module.code)).size).toBe(25)

    expect(first.volume.counts).toEqual({
      frontMatter: 0,
      chapters: 54,
      mainChapters: 31,
      ricettarioModules: 23
    })
    expect(first.volume.frontMatter).toEqual([])
    expect(first.volume.introduction).toEqual({
      title: "Introduzione al Manuale base PA",
      summary: expect.stringContaining("dalla lettura del bando alla costruzione del piano"),
      topics: [
        expect.stringContaining("piano di studio da 30, 60 o 90 giorni"),
        expect.stringContaining("Costituzione, diritto amministrativo, pubblico impiego"),
        expect.stringContaining("logica, comprensione del testo, informatica, inglese"),
        expect.stringContaining("quiz, prova scritta, casi pratici e colloquio orale"),
        expect.stringContaining("il diario degli errori, il ripasso, le checklist e il Ricettario operativo")
      ],
      copyrightNotice: expect.stringContaining("vietata la riproduzione"),
      whyDifferent: expect.stringContaining("Invece di accumulare materiali, costruisci un sistema personale")
    })
    expect(first.volume.introduction.summary).not.toContain("B-PA")
    expect(first.volume.introduction.topics.join(" ")).not.toContain("B-PA")
    expect(first.volume.introduction.copyrightNotice).toContain("Copyright")
    expect(first.volume.introduction.copyrightNotice).not.toContain("www.capitalepersonale.it")
    expect(first.volume.introduction.copyrightNotice).not.toContain("servizi digitali")
    expect(new Set(first.volume.chapters.map((chapter) => chapter.id)).size).toBe(54)
    expect(first.volume.chapters.filter((chapter) => chapter.scope === "ricettario")).toHaveLength(23)
    expect(first.volume.chapters.every((chapter) => chapter.sourcePath.startsWith("wiki/books/"))).toBe(true)
    expect(first.volume.chapters.every((chapter) => chapter.sectionType === "chapter")).toBe(true)
    expect(first.volume.chapters.some((chapter) => chapter.sourcePath.includes("/front-matter/"))).toBe(false)
    expect(first.volume.chapters.some((chapter) => chapter.sourcePath.endsWith("/chapters/introduzione.md"))).toBe(false)
    const excludedConsumerRecords = [
      ["frontmatter-servizi-digitali", "Servizi digitali inclusi", "wiki/books/il-metodo-bando/front-matter/01-servizi-digitali.md"],
      ["frontmatter-frontespizio", "Frontespizio", "wiki/books/il-metodo-bando/front-matter/02-frontespizio.md"],
      ["frontmatter-copyright-colophon", "Copyright e note editoriali", "wiki/books/il-metodo-bando/front-matter/03-copyright-colophon.md"],
      ["frontmatter-sommario", "Sommario", "wiki/books/il-metodo-bando/front-matter/04-sommario.md"],
      ["frontmatter-premessa", "Premessa", "wiki/books/il-metodo-bando/front-matter/05-premessa.md"],
      ["frontmatter-indice-analitico", "Indice", "wiki/books/il-metodo-bando/front-matter/06-indice.md"],
      ["chapter-introduzione-metodo-bando", "Perché questo libro è diverso", "wiki/books/il-metodo-bando/chapters/introduzione.md"]
    ]
    const consumerUnits = [...first.volume.frontMatter, ...first.volume.chapters]
    const consumerUnitIds = new Set(consumerUnits.map((unit) => unit.id))
    const consumerUnitTitles = new Set(consumerUnits.map((unit) => unit.title))
    const consumerUnitPaths = new Set(consumerUnits.map((unit) => unit.sourcePath))
    for (const [id, title, sourcePath] of excludedConsumerRecords) {
      expect(consumerUnitIds).not.toContain(id)
      expect(consumerUnitTitles).not.toContain(title)
      expect(consumerUnitPaths).not.toContain(sourcePath)
    }
    expect(first.volume.chapters.every((chapter) => /^[0-9a-f]{64}$/.test(chapter.contentHash))).toBe(true)
    const units = [...first.volume.frontMatter, ...first.volume.chapters]
    expect(units.every((unit) => unit.moduleCode && unit.moduleTitle)).toBe(true)
    expect(new Set(units.map((unit) => unit.moduleCode))).toEqual(new Set([
      "PART-I",
      "PART-II",
      "PART-III",
      "PART-IV",
      "PART-V",
      "CONCLUSION",
      "APPENDICES",
      "RICETTARIO"
    ]))

    expect(first.assets.length).toBeGreaterThan(0)
    expect(first.assets.every((asset) => ["image/png", "image/svg+xml"].includes(asset.mimeType))).toBe(true)
    expect(first.assets.every((asset) => asset.sourcePaths.every((sourcePath) => !sourcePath.includes("..")))).toBe(true)
    expect(first.assets.every((asset) => asset.sourcePaths.every((sourcePath) => !sourcePath.includes("/front-matter/")))).toBe(true)
    expect(first.media.video).toEqual([])
    expect(first.media.audio).toEqual([])
    expect(first.media.slides).toEqual([])
    expect(first.media.renders.length).toBeGreaterThan(0)

    const imageBlocks = [...first.volume.frontMatter, ...first.volume.chapters]
      .flatMap((unit) => unit.blocks)
      .filter((block) => block.type === "image")
    expect(imageBlocks.length).toBeGreaterThan(0)
    expect(imageBlocks.every((block) => block.assetId?.startsWith("sha256:") && block.path?.startsWith("assets/"))).toBe(true)

    const studio = await buildBookStudioData(new FileWikiStore(path.join(PROJECT_ROOT, "wiki")), "volumi/vol-01")
    const referencedConsumerAssets = new Set(studio.chapters
      .filter((chapter) => chapter.sectionType === "chapter" && !chapter.path.endsWith("/chapters/introduzione.md"))
      .flatMap((chapter) => chapter.blocks)
      .filter((block) => block.type === "image" && block.path)
      .flatMap((block) => {
        const sourcePath = normalizeAssetPath(block.path || "")
        return sourcePath.endsWith(".png")
          ? [sourcePath, `${sourcePath.slice(0, -4)}.svg`]
          : [sourcePath]
      }))
    expect(first.assets.every((asset) => asset.sourcePaths.every((sourcePath) => referencedConsumerAssets.has(sourcePath)))).toBe(true)

    expect(first.gate.releaseEligible).toBe(false)
    expect(first.gate.blockers.map((blocker) => blocker.code)).toEqual(expect.arrayContaining([
      "book-status-not-ready",
      "book-review-required",
      "ricettario-status-not-ready",
      "ricettario-review-required",
      "chapter-review-required",
      "digital-introduction-review-required",
      "pipeline-spec-missing",
      "release-approval-missing"
    ]))
  }, 60_000)

  it("rejects a release while current editorial and human gates are open", async () => {
    await expect(buildBookIntegrationBundle({
      projectRoot: PROJECT_ROOT,
      volumeCode: "VOL-01",
      channel: "release",
      sourceSha: SOURCE_SHA
    })).rejects.toBeInstanceOf(IntegrationReleaseBlockedError)
  }, 60_000)

  it("rejects short source SHAs", async () => {
    await expect(buildBookIntegrationBundle({
      projectRoot: PROJECT_ROOT,
      volumeCode: "VOL-01",
      channel: "candidate",
      sourceSha: "abc123"
    })).rejects.toThrow("40 caratteri")
  })

  it("detects duplicate IDs, unsafe paths, missing assets and hash tampering", async () => {
    const original = candidate

    const duplicateId = structuredClone(original)
    duplicateId.volume.chapters[1].id = duplicateId.volume.chapters[0].id
    expect(validateBookIntegrationBundle(duplicateId)).toContain(
      `ID contenuto duplicato: ${duplicateId.volume.chapters[0].id}.`
    )

    const unsafePath = structuredClone(original)
    unsafePath.assets[0].sourcePaths[0] = "books/il-metodo-bando/assets/../../secret.svg"
    expect(validateBookIntegrationBundle(unsafePath).some((issue) => issue.startsWith("Asset path non sicuro"))).toBe(true)

    const missingAsset = structuredClone(original)
    const imageUnit = [...missingAsset.volume.frontMatter, ...missingAsset.volume.chapters]
      .find((unit) => unit.blocks.some((block) => block.type === "image"))
    const imageBlock = imageUnit?.blocks.find((block) => block.type === "image")
    missingAsset.assets = missingAsset.assets.filter((asset) => asset.id !== imageBlock?.assetId)
    expect(validateBookIntegrationBundle(missingAsset)).toContain(`Asset immagine mancante per ${imageUnit?.id}.`)

    const changedContent = structuredClone(original)
    changedContent.volume.chapters[0].blocks.push({ type: "paragraph", text: "manomissione" })
    expect(validateBookIntegrationBundle(changedContent)).toContain(
      `contentHash non corrispondente per ${changedContent.volume.chapters[0].id}.`
    )

    const missingIntroduction = structuredClone(original) as Omit<typeof original, "volume"> & {
      volume: Omit<typeof original.volume, "introduction"> & { introduction?: typeof original.volume.introduction }
    }
    delete missingIntroduction.volume.introduction
    expect(validateBookIntegrationBundle(missingIntroduction)).toContain("Introduzione digitale mancante.")
  }, 60_000)

  it("ships the matching draft 2020-12 JSON Schema", async () => {
    const schema = JSON.parse(await readFile(
      path.join(PROJECT_ROOT, "schemas", "book-os-integration-bundle-v1.schema.json"),
      "utf8"
    )) as { $schema: string; properties: { schemaVersion: { const: string } } }

    expect(schema.$schema).toBe("https://json-schema.org/draft/2020-12/schema")
    expect(schema.properties.schemaVersion.const).toBe(INTEGRATION_BUNDLE_SCHEMA_VERSION)
  })

  it("defines a least-privilege candidate delivery workflow with optional HMAC notification", async () => {
    const workflow = await readFile(
      path.join(PROJECT_ROOT, ".github", "workflows", "capitale-book-bundle.yml"),
      "utf8"
    )

    expect(workflow).toContain("push:")
    expect(workflow).toContain("- main")
    expect(workflow).toContain("workflow_dispatch:")
    expect(workflow).toContain("permissions:\n  contents: read")
    expect(workflow).toContain("ref: ${{ github.sha }}")
    expect(workflow).toContain("node-version: 20")
    expect(workflow).toContain("npm ci")
    expect(workflow).toContain("actions/upload-artifact@v4")
    expect(workflow).toContain("retention-days: 14")
    expect(workflow).toContain("CAPITALE_BOOK_OS_WEBHOOK_URL")
    expect(workflow).toContain("CAPITALE_BOOK_OS_WEBHOOK_SECRET")
    expect(workflow).toContain('createHmac("sha256"')
    expect(workflow).toContain('"x-book-os-signature-256"')
    expect(workflow).toContain('"x-github-event": "push"')
    expect(workflow).toContain("steps.webhook.outputs.configured == 'true'")
    expect(workflow.indexOf("Upload candidate artifact")).toBeLessThan(workflow.indexOf("Check webhook configuration"))
    expect(workflow).not.toContain("pull_request_target")
    expect(workflow).not.toMatch(/echo\s+["']?\$WEBHOOK_SECRET/)
  })
})

function buildCandidate() {
  return buildBookIntegrationBundle({
    projectRoot: PROJECT_ROOT,
    volumeCode: "VOL-01",
    channel: "candidate",
    sourceSha: SOURCE_SHA
  })
}
