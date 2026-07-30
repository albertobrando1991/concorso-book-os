import { createHash } from "node:crypto"
import fs from "node:fs/promises"
import path from "node:path"
import { describe, expect, it } from "vitest"
import { loadVolumeSpec } from "../../src/pipeline/spec/load-volume-spec"
import { parseFrontmatter } from "../../src/server/wiki/frontmatter"

const wikiRoot = path.resolve(process.cwd(), "wiki")
const moduleRoot = path.join(wikiRoot, "books", "moduli", "m-sa01-sanita-amministrativa")
const chapter04Path = path.join(moduleRoot, "chapters", "04-atti-procedimenti-flussi-informativi.md")

const essentialChapter04Sources = [
  "sources/ssn-organizzazione-aziende-standard-lea",
  "sources/bandi-rappresentativi-m-sa01-sanita-amministrativa-2025-2026",
  "sources/procurement-farmaci-dispositivi-flussi-nsis",
  "sources/contabilita-budget-aziende-sanitarie",
  "sources/documentazione-sanitaria-accesso-fse-dossier-privacy"
]

const rawManifests = [
  path.join(wikiRoot, "raw", "m-sa01-sanita-amministrativa", "fonti", "download-log.json"),
  path.join(wikiRoot, "raw", "m-sa01-sanita-amministrativa", "bandi", "download-log.json")
]

interface RawManifestItem {
  file: string
  bytes: number
  sha256: string
  status?: string
  valid_corpus?: boolean
  failure?: string
}

describe("VOL-07 M-SA01 packaged corpus", () => {
  it("resolves every declared chapter matrix and the chapter 04 source graph", async () => {
    const loaded = await loadVolumeSpec({
      wikiRoot,
      volumeCode: "VOL-07"
    })
    const msa01 = loaded.spec.modules.find((module) => module.code === "M-SA01")

    expect(loaded.issues).toEqual([])
    expect(msa01).toMatchObject({
      moduleId: "moduli/m-sa01-sanita-amministrativa",
      chaptersSource: "declared"
    })

    for (const chapter of msa01?.chapters ?? []) {
      await expect(
        fs.access(path.join(wikiRoot, "books", msa01?.moduleId ?? "", chapter.matrix))
      ).resolves.toBeUndefined()
    }

    const chapter04 = parseFrontmatter(await fs.readFile(chapter04Path, "utf8"))
    const chapterSourceRefs = asStringArray(chapter04.data.source_refs)

    expect(chapterSourceRefs).toEqual(expect.arrayContaining(essentialChapter04Sources))

    for (const sourceRef of chapterSourceRefs) {
      await expect(fs.access(sourcePath(sourceRef))).resolves.toBeUndefined()
    }

    for (const sourceRef of essentialChapter04Sources) {
      const source = parseFrontmatter(await fs.readFile(sourcePath(sourceRef), "utf8"))

      for (const dependencyRef of asStringArray(source.data.source_refs)) {
        await expect(fs.access(sourcePath(dependencyRef))).resolves.toBeUndefined()
      }
    }
  })

  it.each(rawManifests)("matches every file declared by %s", async (manifestPath) => {
    const manifest = JSON.parse(
      (await fs.readFile(manifestPath, "utf8")).replace(/^\uFEFF/, "")
    ) as RawManifestItem[] | { items: RawManifestItem[] }
    const items = Array.isArray(manifest) ? manifest : manifest.items

    expect(items.length).toBeGreaterThan(0)

    for (const item of items) {
      const raw = await fs.readFile(path.join(path.dirname(manifestPath), item.file))
      const sha256 = createHash("sha256").update(raw).digest("hex").toUpperCase()

      expect(raw.byteLength, `${item.file}: bytes`).toBe(item.bytes)
      expect(sha256, `${item.file}: sha256`).toBe(item.sha256.toUpperCase())

      if (raw.subarray(0, 65_536).toString("utf8").includes("<title>Gcore</title>")) {
        expect(item, `${item.file}: challenge status`).toMatchObject({
          status: "blocked",
          valid_corpus: false,
          failure: "gcore_challenge"
        })
      }
    }
  })
})

function sourcePath(sourceRef: string) {
  return path.join(wikiRoot, `${sourceRef.replace(/\.md$/i, "")}.md`)
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map(String) : []
}
