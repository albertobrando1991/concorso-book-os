import { createHash } from "node:crypto"
import { mkdir, readFile, writeFile } from "node:fs/promises"
import path from "node:path"
import {
  TEXT_CATALOG_MODULE_COUNT,
  TEXT_VOLUME_CATALOG,
  textVolumeBookId,
  type TextVolume
} from "../../catalog/text-volumes"
import { FileWikiStore } from "../wiki/file-store"
import { parseFrontmatter } from "../wiki/frontmatter"
import {
  buildBookStudioData,
  getAssetContentType,
  normalizeAssetPath,
  type BookStudioChapter,
  type MarkdownBlock
} from "./book-preview"
import {
  buildStudentSlideDecks,
  compileStudentSlideDeckFile,
  type IntegrationSlideDeck
} from "./book-slide-decks"

export const INTEGRATION_BUNDLE_SCHEMA_VERSION = "book-os-integration-bundle/v1" as const
export const INTEGRATION_BLOCKS_FORMAT = "book-os-blocks/v1" as const

export type IntegrationBundleChannel = "candidate" | "release"
export type IntegrationAssetKind = "image-master" | "image-render" | "slide-deck"

export interface IntegrationCatalogModule {
  code: string
  volumeCode: string
  bookId: string
}

export interface IntegrationCatalogVolume {
  code: string
  title: string
  shortTitle: string
  tier: TextVolume["tier"]
  launchWave: TextVolume["launchWave"]
  modules: string[]
  bookIds: string[]
  orientationBookId?: string
}

export interface IntegrationCatalog {
  volumeCount: number
  moduleCount: number
  volumes: IntegrationCatalogVolume[]
  modules: IntegrationCatalogModule[]
}

export interface IntegrationVolumeIntroduction {
  title: string
  summary: string
  topics: string[]
  copyrightNotice: string
  whyDifferent: string
}

export interface IntegrationContentBlock extends MarkdownBlock {
  assetId?: string
}

export interface IntegrationContentUnit {
  id: string
  sourcePath: string
  sourceHash: string
  contentHash: string
  title: string
  outlineSection: string
  scope: "main" | "ricettario"
  sectionType: "front_matter" | "chapter"
  status: string
  draftStage: string
  reviewRequired: boolean
  contentState: "written" | "draft" | "structure"
  moduleCode?: string
  moduleTitle?: string
  blocksFormat: typeof INTEGRATION_BLOCKS_FORMAT
  blocks: IntegrationContentBlock[]
}

export interface IntegrationAsset {
  id: string
  kind: IntegrationAssetKind
  sourcePaths: string[]
  bundlePath: string
  mimeType: "image/png" | "image/svg+xml" | "text/html"
  sizeBytes: number
  sha256: string
}

export interface IntegrationGateBlocker {
  code: string
  message: string
  sourcePath?: string
  count?: number
}

export interface BookIntegrationBundleV1 {
  schemaVersion: typeof INTEGRATION_BUNDLE_SCHEMA_VERSION
  bundleId: string
  bundleDigest: string
  contentDigest: string
  channel: IntegrationBundleChannel
  source: {
    repository: string
    commit: string
  }
  catalog: IntegrationCatalog
  volume: {
    code: string
    bookId: string
    title: string
    introduction: IntegrationVolumeIntroduction
    counts: {
      frontMatter: number
      chapters: number
      mainChapters: number
      ricettarioModules: number
    }
    frontMatter: IntegrationContentUnit[]
    chapters: IntegrationContentUnit[]
  }
  assets: IntegrationAsset[]
  media: {
    video: string[]
    audio: string[]
    slides: IntegrationSlideDeck[]
    renders: string[]
  }
  gate: {
    releaseEligible: boolean
    blockers: IntegrationGateBlocker[]
  }
}

export interface BuildBookIntegrationBundleOptions {
  projectRoot: string
  volumeCode: string
  channel: IntegrationBundleChannel
  sourceSha: string
  repository?: string
}

export class IntegrationReleaseBlockedError extends Error {
  constructor(readonly bundle: BookIntegrationBundleV1) {
    super(`Release bloccata da ${bundle.gate.blockers.length} gate per ${bundle.volume.code}.`)
    this.name = "IntegrationReleaseBlockedError"
  }
}

interface AssetDraft {
  kind: IntegrationAssetKind
  sourcePaths: Set<string>
  bundlePath: string
  mimeType: "image/png" | "image/svg+xml"
  sizeBytes: number
  sha256: string
}

interface DigitalIntroductionSources {
  overview?: BookStudioChapter
  copyright?: BookStudioChapter
}

const DIGITAL_INTRODUCTION_SOURCE = "books/il-metodo-bando/chapters/introduzione.md"
const COPYRIGHT_NOTICE_SOURCE = "books/il-metodo-bando/front-matter/03-copyright-colophon.md"

export async function buildBookIntegrationBundle(
  options: BuildBookIntegrationBundleOptions
): Promise<BookIntegrationBundleV1> {
  const projectRoot = path.resolve(options.projectRoot)
  const sourceSha = options.sourceSha.trim().toLowerCase()
  const volumeCode = options.volumeCode.trim().toUpperCase()

  if (!/^[0-9a-f]{40}$/.test(sourceSha)) {
    throw new Error("sourceSha deve essere uno SHA Git completo di 40 caratteri esadecimali.")
  }

  const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === volumeCode)

  if (!volume) throw new Error(`Volume sconosciuto: ${volumeCode}.`)

  const catalog = buildIntegrationCatalog()
  assertCatalogContract(catalog)

  const wikiRoot = path.join(projectRoot, "wiki")
  const store = new FileWikiStore(wikiRoot)
  const bookId = textVolumeBookId(volume)

  const studio = await buildBookStudioData(store, `volumi/${volumeCode.toLowerCase()}`)
  const introductionSources = resolveDigitalIntroductionSources(volume, studio.chapters)
  const introduction = buildVolumeIntroduction(volume, introductionSources)
  const consumerChapters = studio.chapters.filter((chapter) => isConsumerChapter(volume, chapter))
  const { assets, sourceAssets } = await buildAssets(store, consumerChapters)
  const chapters = await Promise.all(consumerChapters.map((chapter) => buildContentUnit(store, chapter, sourceAssets, volume)))
  assertUniqueUnitIds(chapters)
  const slideDecks = await buildStudentSlideDecks({
    projectRoot,
    volumeCode: volume.code,
    chapters,
    ignoredSourcePaths: volume.code === "VOL-01" ? [`wiki/${DIGITAL_INTRODUCTION_SOURCE}`] : []
  })
  const integrationAssets = [...assets, ...slideDecks.assets].sort((left, right) => left.bundlePath.localeCompare(right.bundlePath))

  const frontMatter: IntegrationContentUnit[] = []
  const mainChapters = chapters.filter((unit) => unit.scope === "main")
  const ricettarioModules = chapters.filter((unit) => unit.scope === "ricettario")
  const content = {
    catalog,
    volume: {
      code: volume.code,
      bookId,
      title: studio.title,
      introduction,
      counts: {
        frontMatter: frontMatter.length,
        chapters: chapters.length,
        mainChapters: mainChapters.length,
        ricettarioModules: ricettarioModules.length
      },
      frontMatter,
      chapters
    },
    assets: integrationAssets,
    media: {
      video: [] as string[],
      audio: [] as string[],
      slides: slideDecks.slides,
      renders: assets.filter((asset) => asset.kind === "image-render").map((asset) => asset.id).sort()
    }
  }
  const contentDigest = sha256(stableStringify(content))
  const blockers = await collectReleaseBlockers({
    projectRoot,
    store,
    sourceSha,
    contentDigest,
    volume,
    chapters,
    introductionSources: Object.values(introductionSources).filter((source): source is BookStudioChapter => Boolean(source))
  })
  const unsigned = {
    schemaVersion: INTEGRATION_BUNDLE_SCHEMA_VERSION,
    bundleId: `${INTEGRATION_BUNDLE_SCHEMA_VERSION}:${volume.code}:${sourceSha}`,
    contentDigest,
    channel: options.channel,
    source: {
      repository: options.repository || "https://github.com/albertobrando1991/concorso-book-os.git",
      commit: sourceSha
    },
    ...content,
    gate: {
      releaseEligible: blockers.length === 0,
      blockers
    }
  }
  const bundle: BookIntegrationBundleV1 = {
    ...unsigned,
    bundleDigest: sha256(stableStringify(unsigned))
  }

  if (options.channel === "release" && !bundle.gate.releaseEligible) {
    throw new IntegrationReleaseBlockedError(bundle)
  }

  assertValidBookIntegrationBundle(bundle)

  return bundle
}

export async function writeBookIntegrationBundle(
  projectRoot: string,
  outputDirectory: string,
  bundle: BookIntegrationBundleV1
) {
  const root = path.resolve(projectRoot)
  const output = path.resolve(outputDirectory)
  await mkdir(output, { recursive: true })

  const bundleText = `${stableStringify(bundle, 2)}\n`
  await writeFile(path.join(output, "bundle.json"), bundleText, "utf8")

  const checksumRows: string[] = [`${sha256(bundleText)}  bundle.json`]

  for (const asset of bundle.assets) {
    const destination = safeOutputPath(output, asset.bundlePath)
    const bytes = asset.kind === "slide-deck"
      ? (await compileStudentSlideDeckFile(root, asset.sourcePaths[0])).bytes
      : await readFile(safeProjectPath(path.join(root, "wiki"), asset.sourcePaths[0]))

    if (sha256(bytes) !== asset.sha256) {
      throw new Error(`Hash asset cambiato durante l'export: ${asset.sourcePaths[0]}.`)
    }

    await mkdir(path.dirname(destination), { recursive: true })
    await writeFile(destination, bytes)
    checksumRows.push(`${asset.sha256}  ${asset.bundlePath}`)
  }

  await writeFile(path.join(output, "SHA256SUMS"), `${checksumRows.sort().join("\n")}\n`, "utf8")

  return {
    outputDirectory: output,
    bundlePath: path.join(output, "bundle.json"),
    bundleFileSha256: sha256(bundleText)
  }
}

export function validateBookIntegrationBundle(bundle: unknown): string[] {
  const issues: string[] = []
  const value = bundle as Partial<BookIntegrationBundleV1> | null

  if (!value || typeof value !== "object") return ["Il bundle deve essere un oggetto JSON."]
  if (value.schemaVersion !== INTEGRATION_BUNDLE_SCHEMA_VERSION) issues.push("schemaVersion non supportata.")
  if (!/^[0-9a-f]{64}$/.test(String(value.bundleDigest || ""))) issues.push("bundleDigest non valido.")
  if (!/^[0-9a-f]{64}$/.test(String(value.contentDigest || ""))) issues.push("contentDigest non valido.")
  if (value.channel !== "candidate" && value.channel !== "release") issues.push("channel non valido.")
  if (!/^[0-9a-f]{40}$/.test(String(value.source?.commit || ""))) issues.push("source.commit non valido.")
  if (value.catalog?.volumeCount !== 12 || value.catalog?.volumes?.length !== 12) issues.push("Il catalogo deve avere 12 volumi.")
  if (value.catalog?.moduleCount !== 25 || value.catalog?.modules?.length !== 25) issues.push("Il catalogo deve avere 25 moduli.")
  if (!/^VOL-(0[1-9]|1[0-2])$/.test(String(value.volume?.code || ""))) issues.push("Codice volume non valido.")
  const catalogVolume = value.catalog?.volumes?.find((volume) => volume.code === value.volume?.code)
  if (!catalogVolume) issues.push("Il volume non appartiene al catalogo canonico.")
  if (value.volume?.bookId !== textVolumeBookIdForCode(String(value.volume?.code || ""))) {
    issues.push("bookId aggregato non corrispondente al volume.")
  }
  if (!Array.isArray(value.volume?.frontMatter) || !Array.isArray(value.volume?.chapters)) issues.push("Contenuti volume mancanti.")
  if (value.volume?.introduction === undefined) {
    issues.push("Introduzione digitale mancante.")
  } else {
    const introduction = value.volume.introduction
    if (!introduction || typeof introduction !== "object") {
      issues.push("Introduzione digitale non valida.")
    } else {
      if (![introduction.title, introduction.summary, introduction.copyrightNotice, introduction.whyDifferent]
        .every((field) => typeof field === "string" && field.trim().length > 0)) {
        issues.push("I campi dell'introduzione digitale sono obbligatori.")
      }
      if (!Array.isArray(introduction.topics)
        || introduction.topics.length === 0
        || introduction.topics.some((topic) => typeof topic !== "string" || topic.trim().length === 0)
        || new Set(introduction.topics).size !== introduction.topics.length) {
        issues.push("Gli argomenti dell'introduzione digitale non sono validi.")
      }
    }
  }
  if (!Array.isArray(value.assets)) issues.push("assets deve essere un array.")
  if (!Array.isArray(value.media?.video) || !Array.isArray(value.media?.audio) || !Array.isArray(value.media?.slides)) {
    issues.push("Gli array media video/audio/slides sono obbligatori.")
  }
  if (!value.gate || typeof value.gate.releaseEligible !== "boolean" || !Array.isArray(value.gate.blockers)) {
    issues.push("Gate di release non valido.")
  } else {
    if (value.gate.releaseEligible !== (value.gate.blockers.length === 0)) {
      issues.push("releaseEligible non corrisponde ai blocker.")
    }
    if (value.channel === "release" && !value.gate.releaseEligible) {
      issues.push("Un bundle release non può contenere blocker.")
    }
  }

  const units = [...(value.volume?.frontMatter || []), ...(value.volume?.chapters || [])]
  const unitIds = new Set<string>()

  for (const unit of units) {
    if (!unit.id || !unit.sourcePath) issues.push("Ogni unità deve avere id e sourcePath.")
    if (unitIds.has(unit.id)) issues.push(`ID contenuto duplicato: ${unit.id}.`)
    unitIds.add(unit.id)
    if (!/^[0-9a-f]{64}$/.test(unit.sourceHash) || !/^[0-9a-f]{64}$/.test(unit.contentHash)) {
      issues.push(`Hash non valido per ${unit.id || unit.sourcePath}.`)
    }
    if (sha256(stableStringify(unit.blocks)) !== unit.contentHash) {
      issues.push(`contentHash non corrispondente per ${unit.id || unit.sourcePath}.`)
    }
  }

  const assetsById = new Map<string, IntegrationAsset>()

  for (const asset of value.assets || []) {
    if (!asset.sourcePaths.every((sourcePath) => isSafeAssetSourcePath(sourcePath, asset.kind))) {
      issues.push(`Asset path non sicuro: ${asset.sourcePaths.join(", ")}.`)
    }
    if (asset.kind === "slide-deck") {
      if (asset.mimeType !== "text/html" || !/^assets\/[0-9a-f]{64}\.html$/.test(asset.bundlePath)) {
        issues.push(`Formato asset slide non valido: ${asset.id}.`)
      }
    } else if (
      !["image/png", "image/svg+xml"].includes(asset.mimeType)
      || !/^assets\/[0-9a-f]{64}\.(png|svg)$/.test(asset.bundlePath)
    ) {
      issues.push(`Formato asset immagine non valido: ${asset.id}.`)
    }
    if (!/^[0-9a-f]{64}$/.test(asset.sha256)) issues.push(`Hash asset non valido: ${asset.id}.`)
    if (asset.id !== `sha256:${asset.sha256}`) issues.push(`ID asset non corrispondente: ${asset.id}.`)
    if (assetsById.has(asset.id)) issues.push(`ID asset duplicato: ${asset.id}.`)
    assetsById.set(asset.id, asset)
  }

  const slideChapterIds = new Set<string>()
  for (const slide of value.media?.slides || []) {
    const asset = assetsById.get(slide.assetId)
    if (!unitIds.has(slide.chapterId)) issues.push(`Capitolo slide mancante: ${slide.chapterId}.`)
    if (slideChapterIds.has(slide.chapterId)) issues.push(`Deck slide duplicato per ${slide.chapterId}.`)
    slideChapterIds.add(slide.chapterId)
    if (!asset || asset.kind !== "slide-deck" || asset.mimeType !== "text/html") {
      issues.push(`Asset deck slide non risolto per ${slide.chapterId}.`)
    }
    if (!Number.isInteger(slide.slideCount) || slide.slideCount < 1 || slide.slideCount > 100) {
      issues.push(`Conteggio slide non valido per ${slide.chapterId}.`)
    }
  }

  for (const unit of units) {
    for (const block of unit.blocks) {
      if (block.type !== "image") continue
      const asset = block.assetId ? assetsById.get(block.assetId) : undefined

      if (!asset) issues.push(`Asset immagine mancante per ${unit.id}.`)
      else if (block.path !== asset.bundlePath) issues.push(`Bundle path asset non corrispondente per ${unit.id}.`)
    }
  }

  if (value.volume?.counts) {
    const chapters = value.volume.chapters || []
    if (value.volume.counts.frontMatter !== (value.volume.frontMatter || []).length) issues.push("Conteggio front matter non corrispondente.")
    if (value.volume.counts.chapters !== chapters.length) issues.push("Conteggio capitoli non corrispondente.")
    if (value.volume.counts.mainChapters !== chapters.filter((unit) => unit.scope === "main").length) issues.push("Conteggio capitoli main non corrispondente.")
    if (value.volume.counts.ricettarioModules !== chapters.filter((unit) => unit.scope === "ricettario").length) issues.push("Conteggio moduli Ricettario non corrispondente.")
  }

  if (hasCompleteDigestShape(value)) {
    const { bundleDigest, ...unsigned } = value
    if (sha256(stableStringify(unsigned)) !== bundleDigest) issues.push("bundleDigest non corrispondente al contenuto.")
    const expectedContentDigest = sha256(stableStringify({
      catalog: value.catalog,
      volume: value.volume,
      assets: value.assets,
      media: value.media
    }))
    if (expectedContentDigest !== value.contentDigest) issues.push("contentDigest non corrispondente al contenuto editoriale.")
  }

  return [...new Set(issues)]
}

export function assertValidBookIntegrationBundle(bundle: unknown) {
  const issues = validateBookIntegrationBundle(bundle)

  if (issues.length > 0) {
    throw new Error(`Bundle non conforme a book-os-integration-bundle-v1:\n- ${issues.join("\n- ")}`)
  }
}

export function stableStringify(value: unknown, space?: number) {
  return JSON.stringify(sortJson(value), null, space)
}

function buildIntegrationCatalog(): IntegrationCatalog {
  const volumes = TEXT_VOLUME_CATALOG.map((volume) => ({
    code: volume.code,
    title: volume.title,
    shortTitle: volume.shortTitle,
    tier: volume.tier,
    launchWave: volume.launchWave,
    modules: [...volume.modules],
    bookIds: [...volume.bookIds],
    ...(volume.orientationBookId ? { orientationBookId: volume.orientationBookId } : {})
  }))
  const modules = TEXT_VOLUME_CATALOG.flatMap((volume) => volume.modules.map((code, index) => ({
    code,
    volumeCode: volume.code,
    bookId: volume.bookIds[index] || ""
  })))

  return {
    volumeCount: volumes.length,
    moduleCount: TEXT_CATALOG_MODULE_COUNT,
    volumes,
    modules
  }
}

function assertCatalogContract(catalog: IntegrationCatalog) {
  const volumeCodes = new Set(catalog.volumes.map((volume) => volume.code))
  const moduleCodes = new Set(catalog.modules.map((module) => module.code))
  const moduleBookIds = new Set(catalog.modules.map((module) => module.bookId))

  if (catalog.volumeCount !== 12 || volumeCodes.size !== 12) throw new Error("Catalogo invalido: attesi 12 volumi unici.")
  if (catalog.moduleCount !== 25 || moduleCodes.size !== 25) throw new Error("Catalogo invalido: attesi 25 moduli unici.")
  if (moduleBookIds.size !== 25 || catalog.modules.some((module) => !module.bookId)) {
    throw new Error("Catalogo invalido: ogni modulo deve avere un bookId univoco.")
  }
}

function textVolumeBookIdForCode(volumeCode: string) {
  const volume = TEXT_VOLUME_CATALOG.find((item) => item.code === volumeCode)
  return volume ? textVolumeBookId(volume) : ""
}

function resolveDigitalIntroductionSources(
  volume: TextVolume,
  chapters: BookStudioChapter[]
): DigitalIntroductionSources {
  if (volume.code !== "VOL-01") return {}

  const overview = chapters.find((chapter) => chapter.path === DIGITAL_INTRODUCTION_SOURCE)
  const copyright = chapters.find((chapter) => chapter.path === COPYRIGHT_NOTICE_SOURCE)

  if (!overview) throw new Error(`Sorgente introduzione digitale mancante: ${DIGITAL_INTRODUCTION_SOURCE}.`)
  if (!copyright) throw new Error(`Sorgente copyright editoriale mancante: ${COPYRIGHT_NOTICE_SOURCE}.`)

  return { overview, copyright }
}

function buildVolumeIntroduction(
  volume: TextVolume,
  sources: DigitalIntroductionSources
): IntegrationVolumeIntroduction {
  const copyrightLines = (sources.copyright?.blocks || [])
    .filter((block) => block.type === "paragraph" || block.type === "callout")
    .map((block) => block.text?.trim() || "")
    .filter((text) => (
      /^Copyright\b/i.test(text) || text.toLocaleLowerCase("it").includes("vietata la riproduzione")
    ))

  if (volume.code === "VOL-01" && copyrightLines.length < 2) {
    throw new Error(`Copyright editoriale incompleto in ${COPYRIGHT_NOTICE_SOURCE}.`)
  }

  const digitalIntroduction = volume.digitalIntroduction
  const summary = digitalIntroduction?.summary.trim() || volume.promise.trim()
  const topics = [...new Set(digitalIntroduction?.topics.map((topic) => topic.trim()).filter(Boolean) || volume.verticals)]
  const whyDifferent = digitalIntroduction?.whyDifferent.trim()
    || `Percorso pensato per ${volume.audience}. ${volume.promise}`

  if (!summary || topics.length === 0 || !whyDifferent) {
    throw new Error(`Presentazione editoriale digitale incompleta per ${volume.code}.`)
  }

  return {
    title: `Introduzione al ${volume.title}`,
    summary,
    topics,
    copyrightNotice: copyrightLines.join(" ") || "Copyright © 2026 Capitale Personale. Tutti i diritti riservati. È vietata la riproduzione non autorizzata.",
    whyDifferent
  }
}

function isConsumerChapter(volume: TextVolume, chapter: BookStudioChapter) {
  return chapter.sectionType === "chapter"
    && (volume.code !== "VOL-01" || chapter.path !== DIGITAL_INTRODUCTION_SOURCE)
}

async function buildAssets(store: FileWikiStore, chapters: BookStudioChapter[]) {
  const referenced = new Set<string>()

  for (const chapter of chapters) {
    for (const block of chapter.blocks) {
      if (block.type !== "image" || !block.path) continue
      referenced.add(assertLocalImagePath(block.path))
    }
  }

  const selected = new Set(referenced)

  for (const sourcePath of referenced) {
    if (path.posix.extname(sourcePath).toLowerCase() !== ".png") continue
    const svgPath = sourcePath.slice(0, -4) + ".svg"
    if (await store.exists(svgPath)) selected.add(svgPath)
  }

  const draftsByHash = new Map<string, AssetDraft>()
  const sourceHashes = new Map<string, string>()

  for (const sourcePath of [...selected].sort()) {
    const bytes = await readFile(store.resolve(sourcePath))
    const hash = sha256(bytes)
    const extension = path.posix.extname(sourcePath).toLowerCase()
    const mimeType = getAssetContentType(sourcePath)

    if (extension !== ".png" && extension !== ".svg") {
      throw new Error(`Formato asset non supportato da v1: ${sourcePath}.`)
    }
    if (mimeType !== "image/png" && mimeType !== "image/svg+xml") {
      throw new Error(`MIME asset non supportato da v1: ${sourcePath}.`)
    }

    const existing = draftsByHash.get(hash)
    sourceHashes.set(sourcePath, hash)

    if (existing) {
      existing.sourcePaths.add(sourcePath)
      continue
    }

    draftsByHash.set(hash, {
      kind: extension === ".svg" ? "image-master" : "image-render",
      sourcePaths: new Set([sourcePath]),
      bundlePath: `assets/${hash}${extension}`,
      mimeType,
      sizeBytes: bytes.byteLength,
      sha256: hash
    })
  }

  const assets = [...draftsByHash.values()]
    .map((asset): IntegrationAsset => ({
      id: `sha256:${asset.sha256}`,
      kind: asset.kind,
      sourcePaths: [...asset.sourcePaths].sort(),
      bundlePath: asset.bundlePath,
      mimeType: asset.mimeType,
      sizeBytes: asset.sizeBytes,
      sha256: asset.sha256
    }))
    .sort((left, right) => left.bundlePath.localeCompare(right.bundlePath))
  const assetsByHash = new Map(assets.map((asset) => [asset.sha256, asset]))
  const sourceAssets = new Map(
    [...sourceHashes].map(([sourcePath, hash]) => [sourcePath, assetsByHash.get(hash)] as const)
  )

  if ([...sourceAssets.values()].some((asset) => !asset)) {
    throw new Error("Impossibile risolvere uno o più asset content-addressed.")
  }

  return { assets, sourceAssets: sourceAssets as Map<string, IntegrationAsset> }
}

async function buildContentUnit(
  store: FileWikiStore,
  chapter: BookStudioChapter,
  sourceAssets: Map<string, IntegrationAsset>,
  volume: TextVolume
): Promise<IntegrationContentUnit> {
  const source = await store.readText(chapter.path)
  const parsed = parseFrontmatter(source)
  const id = String(parsed.data.id || "").trim()

  if (!id || !/^[a-z0-9][a-z0-9-]*$/.test(id)) {
    throw new Error(`ID stabile mancante o non valido: ${chapter.path}.`)
  }

  const blocks = chapter.blocks.map((block): IntegrationContentBlock => {
    if (block.type !== "image" || !block.path) return { ...block }
    const sourcePath = assertLocalImagePath(block.path)
    const asset = sourceAssets.get(sourcePath)

    if (!asset) throw new Error(`Asset referenziato non incluso: ${sourcePath}.`)

    return {
      ...block,
      path: asset.bundlePath,
      assetId: asset.id
    }
  })
  const integrationModule = resolveIntegrationModule(chapter, volume)

  return {
    id,
    sourcePath: `wiki/${chapter.path}`,
    sourceHash: sha256(source),
    contentHash: sha256(stableStringify(blocks)),
    title: chapter.title,
    outlineSection: chapter.outlineSection,
    scope: chapter.bookScope,
    sectionType: chapter.sectionType,
    status: chapter.status,
    draftStage: chapter.draftStage,
    reviewRequired: chapter.reviewRequired,
    contentState: chapter.contentState,
    ...(integrationModule
      ? { moduleCode: integrationModule.code, moduleTitle: integrationModule.title }
      : {}),
    blocksFormat: INTEGRATION_BLOCKS_FORMAT,
    blocks
  }
}

function resolveIntegrationModule(
  chapter: BookStudioChapter,
  volume: TextVolume
): { code: string; title: string } | null {
  if (chapter.volumeModuleCode) {
    return { code: chapter.volumeModuleCode, title: chapter.volumeModuleCode }
  }

  if (chapter.sectionType === "front_matter" || chapter.outlineSection === "") {
    return { code: "INTRO", title: "Introduzione" }
  }

  if (chapter.bookScope === "ricettario") {
    return { code: "RICETTARIO", title: "Ricettario operativo digitale" }
  }

  if (volume.code !== "VOL-01") {
    return { code: "MAIN", title: volume.shortTitle }
  }

  const numericSection = Number.parseInt(chapter.outlineSection, 10)

  if (Number.isInteger(numericSection)) {
    if (numericSection <= 3) {
      return { code: "PART-I", title: "Parte I - Capire il concorso prima di studiare" }
    }
    if (numericSection <= 12) {
      return { code: "PART-II", title: "Parte II - Il nucleo comune dei concorsi pubblici" }
    }
    if (numericSection <= 18) {
      return { code: "PART-III", title: "Parte III - Allenarsi come in prova" }
    }
    if (numericSection <= 22) {
      return { code: "PART-IV", title: "Parte IV - Adattare il metodo ai profili concorsuali" }
    }
    if (numericSection <= 24) {
      return { code: "PART-V", title: "Parte V - Kit finale del candidato" }
    }
  }

  if (chapter.outlineSection === "CONCLUSIONE") {
    return { code: "CONCLUSION", title: "Conclusione" }
  }
  if (/^[A-F]$/.test(chapter.outlineSection)) {
    return { code: "APPENDICES", title: "Appendici" }
  }
  return { code: "MAIN", title: "Manuale" }
}

async function collectReleaseBlockers(input: {
  projectRoot: string
  store: FileWikiStore
  sourceSha: string
  contentDigest: string
  volume: TextVolume
  chapters: IntegrationContentUnit[]
  introductionSources: BookStudioChapter[]
}) {
  const blockers: IntegrationGateBlocker[] = []
  const sourceBookIds = [...input.volume.bookIds, ...(input.volume.orientationBookId ? [input.volume.orientationBookId] : [])]

  for (const sourceBookId of sourceBookIds) {
    const bookPath = `books/${sourceBookId}/index.md`
    if (!await input.store.exists(bookPath)) {
      blockers.push({ code: "book-index-missing", message: `${sourceBookId} non ha un index editoriale.`, sourcePath: `wiki/${bookPath}` })
      continue
    }

    const book = parseFrontmatter(await input.store.readText(bookPath)).data
    if (String(book.status || "") !== "publication-ready") {
      blockers.push({ code: "book-status-not-ready", message: `${sourceBookId} ha status ${String(book.status || "missing")}.`, sourcePath: `wiki/${bookPath}` })
    }
    if (Boolean(book.review_required)) {
      blockers.push({ code: "book-review-required", message: `${sourceBookId} richiede ancora review.`, sourcePath: `wiki/${bookPath}` })
    }
  }

  if (input.volume.code === "VOL-01") {
    const ricettarioPath = "books/il-metodo-bando/ricettario-digitale.md"
    const ricettario = parseFrontmatter(await input.store.readText(ricettarioPath)).data
    if (String(ricettario.status || "") !== "publication-ready") {
      blockers.push({ code: "ricettario-status-not-ready", message: `Il Ricettario ha status ${String(ricettario.status || "missing")}.`, sourcePath: `wiki/${ricettarioPath}` })
    }
    if (Boolean(ricettario.review_required)) {
      blockers.push({ code: "ricettario-review-required", message: "Il Ricettario richiede ancora review.", sourcePath: `wiki/${ricettarioPath}` })
    }
  }

  if (input.chapters.length === 0) {
    blockers.push({ code: "volume-content-missing", message: `${input.volume.code} non contiene capitoli importabili.` })
  }

  const pendingChapters = input.chapters.filter((chapter) => chapter.reviewRequired)
  if (pendingChapters.length > 0) {
    blockers.push({
      code: "chapter-review-required",
      message: `${pendingChapters.length} capitoli o moduli richiedono ancora review.`,
      count: pendingChapters.length
    })
  }

  const incompleteChapters = input.chapters.filter((chapter) => chapter.contentState !== "written")
  if (incompleteChapters.length > 0) {
    blockers.push({
      code: "chapter-content-incomplete",
      message: `${incompleteChapters.length} capitoli o moduli non sono ancora in stato written.`,
      count: incompleteChapters.length
    })
  }

  const pendingIntroductionSources = input.introductionSources.filter((chapter) => chapter.reviewRequired)
  if (pendingIntroductionSources.length > 0) {
    blockers.push({
      code: "digital-introduction-review-required",
      message: `${pendingIntroductionSources.length} sorgenti dell'introduzione digitale richiedono ancora review.`,
      sourcePath: `wiki/${pendingIntroductionSources[0].path}`,
      count: pendingIntroductionSources.length
    })
  }

  const pipelinePath = path.join(input.projectRoot, "pipeline", input.volume.code, "run-state.json")
  const pipeline = await readJsonOptional(pipelinePath)
  if (!pipeline) {
    blockers.push({
      code: "pipeline-spec-missing",
      message: `Manca lo stato pipeline di ${input.volume.code}.`,
      sourcePath: `pipeline/${input.volume.code}/run-state.json`
    })
  } else {
    const finalStep = Array.isArray(pipeline.steps)
      ? pipeline.steps.find((step: { id?: unknown }) => String(step.id || "") === "24")
      : undefined
    if (!finalStep || finalStep.status !== "done" || finalStep.gate?.passed !== true) {
      blockers.push({
        code: "pipeline-final-gate-pending",
        message: `Lo step 24 di ${input.volume.code} non risulta completato e approvato.`,
        sourcePath: `pipeline/${input.volume.code}/run-state.json`
      })
    }
  }

  const approvalRelativePath = `delivery/${input.volume.code}/release-approval.json`
  const approvalPath = path.join(input.projectRoot, "delivery", input.volume.code, "release-approval.json")
  const approval = await readJsonOptional(approvalPath)

  if (!approval) {
    blockers.push({ code: "release-approval-missing", message: `Manca release-approval.json per ${input.volume.code}.`, sourcePath: approvalRelativePath })
  } else if (
    approval.status !== "approved" ||
    approval.volumeCode !== input.volume.code ||
    approval.sourceCommit !== input.sourceSha ||
    approval.contentDigest !== input.contentDigest
  ) {
    blockers.push({ code: "release-approval-stale", message: "L'approvazione non corrisponde a volume, SHA e digest del bundle.", sourcePath: approvalRelativePath })
  }

  return blockers
}

function assertUniqueUnitIds(units: IntegrationContentUnit[]) {
  const seen = new Set<string>()

  for (const unit of units) {
    if (seen.has(unit.id)) throw new Error(`ID contenuto duplicato: ${unit.id}.`)
    seen.add(unit.id)
  }
}

function assertLocalImagePath(value: string) {
  const normalized = normalizeAssetPath(value)
  const extension = path.posix.extname(normalized).toLowerCase()

  if (extension !== ".png" && extension !== ".svg") {
    throw new Error(`Solo PNG e SVG sono supportati nel bundle v1: ${normalized}.`)
  }

  return normalized
}

function isSafeAssetSourcePath(value: string, kind: IntegrationAssetKind) {
  if (kind === "slide-deck") {
    return /^(?:slides\/VOL-(0[1-9]|1[0-2])\/\d{2}-[a-z0-9][a-z0-9-]*\/(?:index\.html|images\/[a-zA-Z0-9._-]+)|slides\/assets\/(?:capitale-personale\.css|logo\.png))$/.test(value)
  }
  try {
    return assertLocalImagePath(value) === value
  } catch {
    return false
  }
}

function safeProjectPath(root: string, relativePath: string) {
  const normalizedRoot = path.resolve(root)
  const absolute = path.resolve(normalizedRoot, relativePath)
  const prefix = `${normalizedRoot}${path.sep}`

  if (absolute !== normalizedRoot && !absolute.startsWith(prefix)) {
    throw new Error(`Path esterno alla root: ${relativePath}.`)
  }

  return absolute
}

function safeOutputPath(outputRoot: string, relativePath: string) {
  return safeProjectPath(outputRoot, relativePath)
}

async function readJsonOptional(filePath: string): Promise<Record<string, unknown> | null> {
  try {
    return JSON.parse(await readFile(filePath, "utf8")) as Record<string, unknown>
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") return null
    throw new Error(`JSON non valido: ${filePath}.`)
  }
}

function sha256(value: string | Buffer) {
  return createHash("sha256").update(value).digest("hex")
}

function hasCompleteDigestShape(value: Partial<BookIntegrationBundleV1>): value is BookIntegrationBundleV1 {
  return Boolean(
    value.bundleDigest &&
    value.contentDigest &&
    value.catalog &&
    value.volume &&
    value.assets &&
    value.media &&
    value.gate &&
    value.source &&
    value.channel &&
    value.schemaVersion &&
    value.bundleId
  )
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
