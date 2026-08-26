import { createHash } from "node:crypto"
import { readFile } from "node:fs/promises"
import path from "node:path"

export interface StudentSlideDeckAsset {
  id: string
  kind: "slide-deck"
  sourcePaths: string[]
  bundlePath: string
  mimeType: "text/html"
  sizeBytes: number
  sha256: string
}

export interface IntegrationSlideDeck {
  chapterId: string
  assetId: string
  title: string
  slideCount: number
}

interface SlideManifestChapter {
  source: string
  folder: string
  title: string
  status: string
}

interface SlideManifest {
  volume: string
  chapters: SlideManifestChapter[]
}

interface SlideChapterTarget {
  id: string
  sourcePath: string
  title: string
}

const STUDENT_DECK_CSP = [
  "default-src 'none'",
  "img-src data:",
  "style-src 'unsafe-inline'",
  "script-src 'unsafe-inline'",
  "font-src data:",
  "connect-src 'none'",
  "object-src 'none'",
  "base-uri 'none'",
  "form-action 'none'"
].join("; ")

const STUDENT_DECK_SCRIPT = `
(() => {
  const slides = Array.from(document.querySelectorAll(".slide"));
  const stage = document.getElementById("deckStage");
  const progress = document.getElementById("progressFill");
  const pageCount = document.getElementById("pageCount");
  let current = 0;
  let wheelLocked = false;

  const scale = () => {
    if (!stage) return;
    const factor = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
    const x = (window.innerWidth - 1920 * factor) / 2;
    const y = (window.innerHeight - 1080 * factor) / 2;
    stage.style.transform = "translate(" + x + "px, " + y + "px) scale(" + factor + ")";
  };

  const show = (index) => {
    current = Math.max(0, Math.min(index, slides.length - 1));
    slides.forEach((slide, slideIndex) => {
      slide.classList.toggle("active", slideIndex === current);
      slide.classList.toggle("visible", slideIndex === current);
    });
    const number = current + 1;
    if (progress) progress.style.width = ((number / slides.length) * 100) + "%";
    if (pageCount) pageCount.textContent = String(number).padStart(2, "0") + " / " + String(slides.length).padStart(2, "0");
  };

  document.addEventListener("keydown", (event) => {
    if (["ArrowRight", "ArrowDown", "PageDown", " "].includes(event.key)) {
      event.preventDefault();
      show(current + 1);
    } else if (["ArrowLeft", "ArrowUp", "PageUp"].includes(event.key)) {
      event.preventDefault();
      show(current - 1);
    } else if (event.key === "Home") {
      event.preventDefault();
      show(0);
    } else if (event.key === "End") {
      event.preventDefault();
      show(slides.length - 1);
    }
  });

  let touchStartX = 0;
  document.addEventListener("touchstart", (event) => {
    touchStartX = event.changedTouches[0]?.screenX || 0;
  }, { passive: true });
  document.addEventListener("touchend", (event) => {
    const delta = (event.changedTouches[0]?.screenX || 0) - touchStartX;
    if (Math.abs(delta) >= 50) show(current + (delta < 0 ? 1 : -1));
  }, { passive: true });
  window.addEventListener("wheel", (event) => {
    if (wheelLocked || Math.abs(event.deltaY) < 20) return;
    wheelLocked = true;
    show(current + (event.deltaY > 0 ? 1 : -1));
    window.setTimeout(() => { wheelLocked = false; }, 500);
  }, { passive: true });
  window.addEventListener("resize", scale);
  scale();
  show(0);
})();
`.trim()

export async function buildStudentSlideDecks(input: {
  projectRoot: string
  volumeCode: string
  chapters: SlideChapterTarget[]
  ignoredSourcePaths?: string[]
}): Promise<{ assets: StudentSlideDeckAsset[]; slides: IntegrationSlideDeck[] }> {
  const projectRoot = path.resolve(input.projectRoot)
  const volumeCode = input.volumeCode.trim().toUpperCase()
  const manifestPath = safeProjectPath(projectRoot, `slides/${volumeCode}/manifest.json`)
  const manifest = JSON.parse(await readFile(manifestPath, "utf8")) as SlideManifest

  if (manifest.volume !== volumeCode || !Array.isArray(manifest.chapters)) {
    throw new Error(`Manifest slide non valido per ${volumeCode}.`)
  }

  const chaptersBySource = new Map(input.chapters.map((chapter) => [normalizeRepoPath(chapter.sourcePath), chapter]))
  const ignored = new Set((input.ignoredSourcePaths || []).map(normalizeRepoPath))
  const seenFolders = new Set<string>()
  const seenSources = new Set<string>()
  const assetsById = new Map<string, StudentSlideDeckAsset>()
  const slides: IntegrationSlideDeck[] = []

  for (const manifestChapter of manifest.chapters) {
    const folder = String(manifestChapter.folder || "").trim()
    const sourcePath = normalizeRepoPath(String(manifestChapter.source || ""))
    if (!/^\d{2}-[a-z0-9][a-z0-9-]*$/.test(folder)) {
      throw new Error(`Cartella slide non valida per ${volumeCode}: ${folder}.`)
    }
    if (!/^wiki\/books\/[a-z0-9/_-]+\.md$/.test(sourcePath)) {
      throw new Error(`Sorgente slide non valida per ${volumeCode}: ${sourcePath}.`)
    }
    if (manifestChapter.status !== "ready") {
      throw new Error(`Deck slide non pronto per ${volumeCode}: ${folder}.`)
    }
    if (seenFolders.has(folder) || seenSources.has(sourcePath)) {
      throw new Error(`Deck slide duplicato per ${volumeCode}: ${folder}.`)
    }
    seenFolders.add(folder)
    seenSources.add(sourcePath)

    const chapter = chaptersBySource.get(sourcePath)
    if (!chapter) {
      if (ignored.has(sourcePath)) continue
      throw new Error(`Deck slide senza capitolo consumer per ${volumeCode}: ${sourcePath}.`)
    }

    const deckSourcePath = `slides/${volumeCode}/${folder}/index.html`
    const compiled = await compileStudentSlideDeckFile(projectRoot, deckSourcePath)
    const digest = sha256(compiled.bytes)
    const assetId = `sha256:${digest}`
    const existing = assetsById.get(assetId)
    if (existing) {
      existing.sourcePaths = [...new Set([...existing.sourcePaths, ...compiled.sourcePaths])]
    } else {
      assetsById.set(assetId, {
        id: assetId,
        kind: "slide-deck",
        sourcePaths: compiled.sourcePaths,
        bundlePath: `assets/${digest}.html`,
        mimeType: "text/html",
        sizeBytes: compiled.bytes.byteLength,
        sha256: digest
      })
    }
    slides.push({
      chapterId: chapter.id,
      assetId,
      title: String(manifestChapter.title || chapter.title).trim() || chapter.title,
      slideCount: compiled.slideCount
    })
  }

  return {
    assets: [...assetsById.values()].sort((left, right) => left.bundlePath.localeCompare(right.bundlePath)),
    slides
  }
}

export async function compileStudentSlideDeckFile(projectRootInput: string, sourcePathInput: string) {
  const projectRoot = path.resolve(projectRootInput)
  const sourcePath = normalizeRepoPath(sourcePathInput)
  if (!/^slides\/VOL-(0[1-9]|1[0-2])\/\d{2}-[a-z0-9][a-z0-9-]*\/index\.html$/.test(sourcePath)) {
    throw new Error(`Path deck slide non valido: ${sourcePath}.`)
  }
  const sourceFile = safeProjectPath(projectRoot, sourcePath)
  const sourceDirectory = path.dirname(sourceFile)
  const cssSourcePath = "slides/assets/capitale-personale.css"
  const css = await readFile(safeProjectPath(projectRoot, cssSourcePath), "utf8")
  let html = await readFile(sourceFile, "utf8")
  const dependencies = new Set<string>([sourcePath, cssSourcePath])

  html = html.replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, "")
  html = html.replace(/\s*<link\b[^>]*>/gi, "")
  html = html.replace(/\s*<div\b[^>]*class="[^"]*\bedit-hotzone\b[^"]*"[^>]*>\s*<\/div>/gi, "")
  html = html.replace(/\s*<button\b[^>]*class="[^"]*\bedit-toggle\b[^"]*"[^>]*>[\s\S]*?<\/button>/gi, "")
  html = html.replace(/\sdata-edit-key\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)/gi, "")
  html = html.replace(/\scontenteditable\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)/gi, "")

  const imageRefs = [...new Set([...html.matchAll(/<img\b[^>]*\bsrc="([^"]+)"[^>]*>/gi)].map((match) => match[1]))]
  for (const imageRef of imageRefs) {
    if (!imageRef || /^(data:|https?:|\/\/|\/)/i.test(imageRef)) {
      throw new Error(`Riferimento immagine slide non locale: ${imageRef}.`)
    }
    const imageFile = safeProjectPath(projectRoot, normalizeRepoPath(path.relative(projectRoot, path.resolve(sourceDirectory, imageRef))))
    const relativeImagePath = normalizeRepoPath(path.relative(projectRoot, imageFile))
    if (!relativeImagePath.startsWith("slides/")) {
      throw new Error(`Immagine slide esterna alla cartella slides: ${imageRef}.`)
    }
    const bytes = await readFile(imageFile)
    const mimeType = imageMimeType(imageFile)
    dependencies.add(relativeImagePath)
    html = html.replaceAll(`src="${imageRef}"`, `src="data:${mimeType};base64,${bytes.toString("base64")}"`)
  }

  const slideCount = (html.match(/<section\s+class="[^"]*\bslide\b/gi) || []).length
  if (slideCount < 1 || slideCount > 100) {
    throw new Error(`Numero slide non valido per ${sourcePath}: ${slideCount}.`)
  }

  rejectUnsafeStudentDeckHtml(html, sourcePath)
  const csp = `<meta http-equiv="Content-Security-Policy" content="${STUDENT_DECK_CSP}">`
  html = html.replace(/<head>/i, `<head>\n    ${csp}`)
  html = html.replace(/<\/head>/i, `    <style>\n${css}\n    </style>\n</head>`)
  html = html.replace(/<\/body>/i, `    <script>\n${STUDENT_DECK_SCRIPT}\n    </script>\n</body>`)

  return {
    bytes: Buffer.from(html, "utf8"),
    slideCount,
    sourcePaths: [sourcePath, ...[...dependencies].filter((item) => item !== sourcePath).sort()]
  }
}

function rejectUnsafeStudentDeckHtml(html: string, sourcePath: string) {
  const forbidden = [
    /<\s*(iframe|object|embed|form|base)\b/i,
    /<meta\b[^>]*http-equiv=["']?refresh/i,
    /\son[a-z]+\s*=\s*["']/i,
    /javascript\s*:/i,
    /(?:src|href)=["'](?:https?:|\/\/|\/)/i
  ]
  if (forbidden.some((pattern) => pattern.test(html))) {
    throw new Error(`Deck slide con contenuto attivo non consentito: ${sourcePath}.`)
  }
}

function imageMimeType(filePath: string) {
  switch (path.extname(filePath).toLowerCase()) {
    case ".png": return "image/png"
    case ".jpg":
    case ".jpeg": return "image/jpeg"
    case ".webp": return "image/webp"
    case ".svg": return "image/svg+xml"
    default: throw new Error(`Formato immagine slide non supportato: ${filePath}.`)
  }
}

function normalizeRepoPath(value: string) {
  const normalized = value.replace(/\\/g, "/").replace(/^\.\//, "")
  if (!normalized || normalized.startsWith("/") || normalized.split("/").some((part) => part === ".." || part === ".")) {
    throw new Error(`Path repository non sicuro: ${value}.`)
  }
  return normalized
}

function safeProjectPath(projectRoot: string, relativePath: string) {
  const normalizedRoot = path.resolve(projectRoot)
  const absolute = path.resolve(normalizedRoot, relativePath)
  if (absolute !== normalizedRoot && !absolute.startsWith(`${normalizedRoot}${path.sep}`)) {
    throw new Error(`Path esterno alla root progetto: ${relativePath}.`)
  }
  return absolute
}

function sha256(value: string | Buffer) {
  return createHash("sha256").update(value).digest("hex")
}
