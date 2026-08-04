# VOL-07 Step 19 KDP Book Studio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rendere VOL-07 un volume KDP completo nel Book Studio, con indice dei nuclei riconciliato alle pagine effettive, master canonico e verifica automatica dell'intero rendering.

**Architecture:** Il server conserva l'identità tecnica dei `Nucleo ID`, rinumera i nuclei per il volume composito e genera le righe dell'indice. Il client riconcilia capitoli e nuclei con la paginazione misurata; il renderer condiviso applica gutter e stile `▣ Verifica`, mentre Playwright certifica struttura e assenza di overflow senza produrre un PDF.

**Tech Stack:** TypeScript, React, Next.js, Vitest, Playwright, CSS print, Markdown, PowerShell, pipeline CLI, LocalAgentMemory.

## Global Constraints

- Il `bookId` canonico del volume è `volumi/vol-07`.
- Non modificare i venticinque capitoli congelati, le matrici, gli indici di modulo o i manifest di text freeze.
- Non creare un PDF nello step 19; `output/pdf/` resta invariato.
- Pagina KDP 6,69 × 9,61 pollici, bianco e nero, senza bleed, colonna singola.
- Corpo Garamond 11 pt con interlinea 1,18; H1/H2/H3 Arial Bold 20/14/12 pt; tabelle, quiz, box e strumenti Arial 9,5-10 pt.
- Gutter interno 23 mm, margine esterno 13 mm, alto e basso 18 mm, speculari recto/verso.
- Nel modulo standalone `N-SA02-05-01`–`07` resta `5.1–5.7`; nel volume composito diventa `9.1–9.7`.
- Usare `path + nucleusId` come identità tecnica; non usare il numero visibile come chiave.
- Non modificare manualmente `pipeline/VOL-07/run-state.json`; usare solo il CLI con `--json`.
- Tentare `complete` senza forzature; usare `--accept --note` solo dopo un esplicito `gate-not-implemented` e verifica manuale documentata.
- Preservare tutte le modifiche preesistenti nel worktree; ogni commit deve contenere soltanto i file dichiarati nel task.

---

### Task 1: Conservare identità dei nuclei e semantica dei blocchi Verifica

**Files:**
- Modify: `src/server/book/book-preview.ts:16-43, 800-835, 1170-1200`
- Test: `tests/book-preview.test.ts`

**Interfaces:**
- Consumes: heading Markdown `N-XX00-00-00 · Titolo` e `▣ Verifica`.
- Produces: `MarkdownBlock.nucleusId?: string` e `MarkdownBlock.verification?: boolean`, usati dai Task 2-5.

- [ ] **Step 1: Scrivere il test rosso per identità e semantica**

Add a Vitest case to `tests/book-preview.test.ts` that creates one temporary chapter and asserts both fields:

```ts
it("preserves nucleus identity and verification semantics", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-nucleus-meta-"))

  try {
    await mkdir(path.join(root, "books/moduli/m-sa02-professioni-sanitarie/chapters"), { recursive: true })
    await writeFile(
      path.join(root, "books/moduli/m-sa02-professioni-sanitarie/index.md"),
      "---\ntitle: M-SA02 - Professioni sanitarie\n---\n# M-SA02",
      "utf8"
    )
    await writeFile(
      path.join(root, "books/moduli/m-sa02-professioni-sanitarie/chapters/05-pilota.md"),
      [
        "---",
        "title: Capitolo pilota",
        "outline_section: 5",
        "---",
        "# Capitolo pilota",
        "",
        "## N-SA02-05-04 · Team e sicurezza",
        "",
        "Testo del nucleo.",
        "",
        "## ▣ Verifica",
        "",
        "1. Domanda di controllo."
      ].join("\n"),
      "utf8"
    )

    const data = await buildBookStudioData(
      new FileWikiStore(root),
      "moduli/m-sa02-professioni-sanitarie"
    )
    const headings = data.chapters[0].blocks.filter((block) => block.type === "heading")

    expect(headings.find((block) => block.nucleusId)?.nucleusId).toBe("N-SA02-05-04")
    expect(headings.find((block) => block.nucleusId)?.number).toBe("5.4")
    expect(headings.find((block) => block.verification)?.text).toBe("▣ Verifica")
  } finally {
    await rm(root, { recursive: true, force: true })
  }
})
```

- [ ] **Step 2: Eseguire il test e confermare il fallimento**

Run:

```powershell
npm test -- --run tests/book-preview.test.ts -t "preserves nucleus identity and verification semantics"
```

Expected: FAIL because `nucleusId` and `verification` are absent.

- [ ] **Step 3: Aggiungere i campi e valorizzarli nel parser**

Extend `MarkdownBlock`:

```ts
export interface MarkdownBlock {
  // existing fields remain unchanged
  nucleusId?: string
  verification?: boolean
}
```

Add the semantic helper near `parseNucleusHeading()`:

```ts
function isVerificationHeading(value: string) {
  return /^▣\s*Verifica\b/i.test(value.trim())
}
```

When `markdownToBlocks()` handles a heading, preserve the technical ID and semantic flag:

```ts
const text = cleanInlineText(heading[2])
const nucleus = parseNucleusHeading(text)

blocks.push({
  type: "heading",
  level: Math.min(heading[1].length, 4),
  text: nucleus?.title || text,
  ...(nucleus ? { number: nucleus.number, nucleusId: nucleus.id } : {}),
  ...(isVerificationHeading(text) ? { verification: true } : {})
})
```

- [ ] **Step 4: Eseguire il test mirato e il file completo**

Run:

```powershell
npm test -- --run tests/book-preview.test.ts -t "preserves nucleus identity and verification semantics"
npm test -- --run tests/book-preview.test.ts
```

Expected: new test PASS; all `book-preview` tests PASS.

- [ ] **Step 5: Commit selettivo**

```powershell
git add -- 'src/server/book/book-preview.ts' 'tests/book-preview.test.ts'
git diff --cached --check
git diff --cached --name-only
git commit -m "feat(book-studio): preserve nucleus metadata"
```

Expected: commit contains only the parser and its test.

### Task 2: Rinumero globale e indice dei nuclei nel volume composito

**Files:**
- Modify: `src/server/book/book-preview.ts:230-380, 545-590, 700-760`
- Test: `tests/book-preview.test.ts`

**Interfaces:**
- Consumes: `MarkdownBlock.nucleusId` from Task 1 and module-local `chapter.outlineSection`.
- Produces: composite chapter blocks with reader number `globalChapter.progressive`; `index-row` blocks carrying `path`, `nucleusId`, `number`, and estimated `pageNumber`.

- [ ] **Step 1: Scrivere il test rosso sul mapping 5.4 → 9.4**

Add a Vitest case that uses the VOL-03 fixture catalog, writes eight chapters in M-FC01 and one local chapter 05 in M-FC02, then builds both the composite and standalone books:

```ts
it("maps local nucleus numbers to global volume chapters", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "book-preview-volume-nuclei-"))

  try {
    for (const moduleId of ["m-fc01-ministeri", "m-fc02-agenzie-fiscali"]) {
      await mkdir(path.join(root, `books/moduli/${moduleId}/chapters`), { recursive: true })
      await writeFile(
        path.join(root, `books/moduli/${moduleId}/index.md`),
        `---\ntitle: ${moduleId}\n---\n# ${moduleId}`,
        "utf8"
      )
    }

    for (let index = 1; index <= 8; index += 1) {
      const number = String(index).padStart(2, "0")
      await writeFile(
        path.join(root, `books/moduli/m-fc01-ministeri/chapters/${number}-base.md`),
        `---\ntitle: Capitolo ${index}\noutline_section: ${index}\n---\n# Capitolo ${index}\n\nTesto completo.`,
        "utf8"
      )
    }

    const pilotPath = path.join(root, "books/moduli/m-fc02-agenzie-fiscali/chapters/05-pilota.md")
    await writeFile(
      pilotPath,
      [
        "---",
        "title: Capitolo pilota",
        "outline_section: 5",
        "---",
        "# Capitolo pilota",
        "",
        "## N-FC02-05-04 · Nucleo pilota",
        "",
        "Testo completo."
      ].join("\n"),
      "utf8"
    )

    const store = new FileWikiStore(root)
    const volume = await buildBookStudioData(store, "volumi/vol-03")
    const standalone = await buildBookStudioData(store, "moduli/m-fc02-agenzie-fiscali")
    const volumePilot = volume.chapters.find((chapter) => chapter.title === "Capitolo pilota")
    const volumeNucleus = volumePilot?.blocks.find((block) => block.nucleusId === "N-FC02-05-04")
    const standaloneNucleus = standalone.chapters[0].blocks.find((block) => block.nucleusId === "N-FC02-05-04")
    const index = volume.chapters.find((chapter) => chapter.frontMatterLayout === "analytical-index")
    const row = index?.blocks.find((block) => block.nucleusId === "N-FC02-05-04")

    expect(volumePilot?.outlineSection).toBe("9")
    expect(volumePilot?.moduleOutlineSection).toBe("5")
    expect(volumeNucleus?.number).toBe("9.4")
    expect(standaloneNucleus?.number).toBe("5.4")
    expect(row).toMatchObject({
      type: "index-row",
      number: "9.4",
      nucleusId: "N-FC02-05-04",
      path: volumePilot?.path
    })
  } finally {
    await rm(root, { recursive: true, force: true })
  }
})
```

- [ ] **Step 2: Eseguire il test e confermare il fallimento**

```powershell
npm test -- --run tests/book-preview.test.ts -t "maps local nucleus numbers to global volume chapters"
```

Expected: FAIL because the volume heading remains `5.4` and no volume `index-row` exists.

- [ ] **Step 3: Rinumero dei blocchi del capitolo composito**

Introduce this focused helper in `book-preview.ts`:

```ts
function mapChapterIntoVolume(chapter: BookStudioChapter, volumeChapterNumber: number): BookStudioChapter {
  return {
    ...chapter,
    moduleOutlineSection: chapter.outlineSection,
    outlineSection: String(volumeChapterNumber),
    blocks: chapter.blocks.map((block) => {
      if (block.type !== "heading" || !block.nucleusId) return block

      const match = /-(\d{2})$/.exec(block.nucleusId)
      if (!match) return block

      return {
        ...block,
        number: `${volumeChapterNumber}.${Number.parseInt(match[1], 10)}`
      }
    })
  }
}
```

Replace the inline mapping in `buildVolumeBookStudioData()` with a call that increments `nextChapterNumber` exactly once per chapter.

- [ ] **Step 4: Emettere le righe dei nuclei nell'indice volume**

Extend the heading metadata returned by `estimateChapterPages()`:

```ts
const headings: Array<{
  text: string
  number?: string
  nucleusId?: string
  pageNumber: number
}> = []
```

Preserve `block.nucleusId` when adding a heading estimate. After each `index-chapter` in `buildVolumeIndexBlocks()`, append only numbered nucleus headings:

```ts
for (const heading of estimate.headings.filter((item) => item.nucleusId && item.number)) {
  blocks.push({
    type: "index-row",
    text: heading.text,
    number: heading.number,
    nucleusId: heading.nucleusId,
    path: chapter.path,
    pageNumber: heading.pageNumber
  })
}
```

- [ ] **Step 5: Eseguire test mirati e regressione server**

```powershell
npm test -- --run tests/book-preview.test.ts -t "maps local nucleus numbers to global volume chapters"
npm test -- --run tests/book-preview.test.ts tests/text-volumes.test.ts
```

Expected: mapping test PASS; all selected tests PASS.

- [ ] **Step 6: Commit selettivo**

```powershell
git add -- 'src/server/book/book-preview.ts' 'tests/book-preview.test.ts'
git diff --cached --check
git commit -m "feat(book-studio): index composite volume nuclei"
```

Expected: commit contains only composite numbering/index work and its tests.

### Task 3: Riconciliare l'indice con le pagine misurate

**Files:**
- Create: `app/components/book-studio-index-pages.ts`
- Modify: `app/components/book-studio-panel.tsx:49-56, 120-220, 940-995`
- Test: `tests/book-studio-index-pages.test.ts`

**Interfaces:**
- Consumes: pagine con `chapter.path`, heading con `nucleusId`, righe indice con `path + nucleusId`.
- Produces: `reconcileIndexPageNumbers<T extends BookStudioPageLike>(pages: T[]): T[]`, con numeri pagina aggiornati senza mutare l'input.

- [ ] **Step 1: Scrivere il test rosso della riconciliazione**

Create `tests/book-studio-index-pages.test.ts`:

```ts
import { describe, expect, it } from "vitest"
import { reconcileIndexPageNumbers } from "@/app/components/book-studio-index-pages"
import type { BookStudioChapter, MarkdownBlock } from "@/src/server/book/book-preview"

const chapter = (input: Partial<BookStudioChapter>): BookStudioChapter => ({
  path: "books/volumi/vol-07/front-matter/fm6-indice-completo.md",
  title: "Indice completo",
  outlineSection: "FM6",
  bookScope: "main",
  sectionType: "front_matter",
  frontMatterLayout: "analytical-index",
  indexDetail: "volume-modules",
  status: "generated",
  draftStage: "generated-volume-layout",
  reviewRequired: false,
  topics: [],
  sourceRefs: [],
  wordCount: 0,
  contentState: "written",
  blocks: [],
  ...input
})

it("reconciles chapter and nucleus rows against measured pages without mutation", () => {
  const pilotPath = "books/moduli/m-sa02-professioni-sanitarie/chapters/05-pilota.md"
  const indexBlocks: MarkdownBlock[] = [
    { type: "index-chapter", text: "Capitolo pilota", path: pilotPath, pageNumber: 1 },
    {
      type: "index-row",
      text: "Team e sicurezza",
      path: pilotPath,
      nucleusId: "N-SA02-05-04",
      number: "9.4",
      pageNumber: 1
    }
  ]
  const pages = [
    {
      chapter: chapter({ blocks: indexBlocks }),
      blocks: indexBlocks,
      pageNumber: 6,
      chapterPageNumber: 1,
      isFirstPage: true
    },
    {
      chapter: chapter({
        path: pilotPath,
        title: "Capitolo pilota",
        outlineSection: "9",
        sectionType: "chapter",
        frontMatterLayout: "",
        blocks: []
      }),
      blocks: [{ type: "paragraph", text: "Apertura" }],
      pageNumber: 41,
      chapterPageNumber: 1,
      isFirstPage: true
    },
    {
      chapter: chapter({
        path: pilotPath,
        title: "Capitolo pilota",
        outlineSection: "9",
        sectionType: "chapter",
        frontMatterLayout: "",
        blocks: []
      }),
      blocks: [
        {
          type: "heading",
          text: "Team e sicurezza",
          number: "9.4",
          nucleusId: "N-SA02-05-04"
        }
      ],
      pageNumber: 43,
      chapterPageNumber: 3,
      isFirstPage: false
    }
  ]
  const original = structuredClone(pages)
  const reconciled = reconcileIndexPageNumbers(pages)
  const blocks = reconciled[0].blocks

  expect(blocks[0].pageNumber).toBe(41)
  expect(blocks[1].pageNumber).toBe(43)
  expect(pages).toEqual(original)
})
```

- [ ] **Step 2: Eseguire il test e confermare il fallimento**

```powershell
npm test -- --run tests/book-studio-index-pages.test.ts
```

Expected: FAIL because the helper module does not exist.

- [ ] **Step 3: Implementare la funzione pura**

Create `app/components/book-studio-index-pages.ts`:

```ts
import type { BookStudioChapter, MarkdownBlock } from "@/src/server/book/book-preview"

export interface BookStudioPageLike {
  chapter: BookStudioChapter
  blocks: MarkdownBlock[]
  pageNumber: number
}

export function reconcileIndexPageNumbers<T extends BookStudioPageLike>(pages: T[]): T[] {
  const chapterPages = new Map<string, number>()
  const nucleusPages = new Map<string, number>()

  for (const page of pages) {
    if (page.chapter.sectionType === "chapter" && !chapterPages.has(page.chapter.path)) {
      chapterPages.set(page.chapter.path, page.pageNumber)
    }

    for (const block of page.blocks) {
      if (block.type === "heading" && block.nucleusId) {
        nucleusPages.set(`${page.chapter.path}\n${block.nucleusId}`, page.pageNumber)
      }
    }
  }

  return pages.map((page) => {
    if (page.chapter.frontMatterLayout !== "analytical-index") return page

    return {
      ...page,
      blocks: page.blocks.map((block) => {
        if (block.type === "index-chapter" && block.path) {
          const pageNumber = chapterPages.get(block.path)
          return pageNumber ? { ...block, pageNumber } : block
        }

        if (block.type === "index-row" && block.path && block.nucleusId) {
          const pageNumber = nucleusPages.get(`${block.path}\n${block.nucleusId}`)
          return pageNumber ? { ...block, pageNumber } : block
        }

        return block
      })
    }
  })
}
```

- [ ] **Step 4: Integrare il helper dopo stima, misura e rifinitura**

Import the helper in `book-studio-panel.tsx`. Rename the pre-reconciliation value and memoize the final pages:

```ts
const rawPreviewPages = measuredPages || estimatedPages
const previewPages = useMemo(
  () => reconcileIndexPageNumbers(rawPreviewPages),
  [rawPreviewPages]
)
```

Do not feed reconciled pages back into `paginateMeasuredChapters()` or `refineRenderedPageOverflows()`; this keeps the process single-pass and deterministic.

- [ ] **Step 5: Esporre identità diagnostiche senza testo visibile**

On the nucleus heading and index row elements rendered by `PreviewBlock`, add:

```tsx
data-nucleus-id={block.nucleusId || undefined}
data-index-path={block.path || undefined}
```

The attributes are diagnostic only; do not render the technical ID as reader-visible text.

- [ ] **Step 6: Eseguire test e typecheck**

```powershell
npm test -- --run tests/book-studio-index-pages.test.ts tests/book-preview.test.ts
npm run typecheck
```

Expected: all selected tests PASS; typecheck exit 0.

- [ ] **Step 7: Commit selettivo**

```powershell
git add -- 'app/components/book-studio-index-pages.ts' 'app/components/book-studio-panel.tsx' 'tests/book-studio-index-pages.test.ts'
git diff --cached --check
git commit -m "feat(book-studio): reconcile analytical index pages"
```

### Task 4: Applicare gutter canonico e resa dei blocchi Verifica

**Files:**
- Modify: `app/globals.css:20-40, 1015-1080, 1180-1240`
- Modify: `app/components/book-studio-panel.tsx:940-955`
- Test: `tests/editorial-typography.test.ts`

**Interfaces:**
- Consumes: `MarkdownBlock.verification` from Task 1.
- Produces: classe `.verificationHeading`; master con `--book-padding-inside: 23mm` e resa print-safe.

- [ ] **Step 1: Scrivere le asserzioni rosse sul master**

Extend the first test in `tests/editorial-typography.test.ts`:

```ts
const component = await readProjectFile("app/components/book-studio-panel.tsx")

expect(css).toContain("--book-page-width: 6.69in")
expect(css).toContain("--book-page-height: 9.61in")
expect(css).toContain("--book-padding-inside: 23mm")
expect(css).toMatch(/\.verificationHeading\s*\{[^}]*border:[^;}]*;[^}]*background:\s*#f2f2f2;[^}]*break-after:\s*avoid;/)
expect(component).toContain('block.verification ? "verificationHeading" : undefined')
```

- [ ] **Step 2: Eseguire il test e confermare il fallimento**

```powershell
npm test -- --run tests/editorial-typography.test.ts
```

Expected: FAIL on 20 mm gutter and missing verification class.

- [ ] **Step 3: Aggiornare il gutter condiviso**

Change the root variable only:

```css
--book-padding-inside: 23mm;
```

Keep outside/top/bottom dimensions unchanged. Preserve `.bookPageVerso`, which swaps inside and outside margins.

- [ ] **Step 4: Rendere semanticamente il titolo Verifica**

In the heading branch of `PreviewBlock`:

```tsx
const headingText = block.number ? `${block.number} ${block.text}` : block.text
const headingClassName = block.verification ? "verificationHeading" : undefined

if ((block.level || 2) <= 2) {
  return <h3 className={headingClassName} data-nucleus-id={block.nucleusId || undefined}>{headingText}</h3>
}
```

Apply the same `className` and diagnostic attribute to H4/H5 for defensive consistency.

- [ ] **Step 5: Aggiungere lo stile bianco e nero**

Add after the shared heading rules:

```css
.previewBlocks .verificationHeading {
  border: 1.5pt solid #111111;
  border-left-width: 4pt;
  background: #f2f2f2;
  color: #020617;
  padding: 6pt 8pt;
  break-after: avoid;
  page-break-after: avoid;
}
```

Do not use navy, bordeaux or gold as the sole distinction; the block must remain legible in grayscale.

- [ ] **Step 6: Eseguire test e typecheck**

```powershell
npm test -- --run tests/editorial-typography.test.ts tests/book-preview.test.ts tests/book-studio-index-pages.test.ts
npm run typecheck
```

Expected: all selected tests PASS; typecheck exit 0.

- [ ] **Step 7: Commit selettivo**

```powershell
git add -- 'app/globals.css' 'app/components/book-studio-panel.tsx' 'tests/editorial-typography.test.ts'
git diff --cached --check
git commit -m "style(book-studio): apply canonical KDP verification master"
```

### Task 5: Parametrizzare e irrigidire il verifier Playwright

**Files:**
- Create: `scripts/book-studio-layout-options.mjs`
- Create: `scripts/book-studio-layout-options.d.mts`
- Modify: `scripts/verify-book-studio-layout.mjs:1-180`
- Modify: `app/components/book-studio-panel.tsx:820-935`
- Test: `tests/book-studio-layout-options.test.ts`

**Interfaces:**
- Consumes: environment variables `BOOK_STUDIO_BOOK_IDS`, `BOOK_STUDIO_ARTIFACT_PREFIX`, `BOOK_STUDIO_EXPECTED_COUNTS`.
- Produces: `resolveBookStudioLayoutOptions(env)` and JSON report `artifacts/<prefix>-layout-report.json` with structural counts and page diagnostics.

- [ ] **Step 1: Scrivere il test rosso delle opzioni**

Create `tests/book-studio-layout-options.test.ts`:

```ts
import { describe, expect, it } from "vitest"
import { resolveBookStudioLayoutOptions } from "@/scripts/book-studio-layout-options.mjs"

describe("Book Studio layout verifier options", () => {
  it("targets VOL-07 with explicit counts and a stable artifact prefix", () => {
    expect(resolveBookStudioLayoutOptions({
      BOOK_STUDIO_BOOK_IDS: "volumi/vol-07",
      BOOK_STUDIO_ARTIFACT_PREFIX: "vol-07-step-19",
      BOOK_STUDIO_EXPECTED_COUNTS: JSON.stringify({
        frontMatter: 6,
        moduleOpenings: 4,
        chapters: 25,
        nuclei: 7
      })
    })).toEqual({
      cases: [{ id: "volumi/vol-07", label: "vol-07" }],
      artifactPrefix: "vol-07-step-19",
      expectedCounts: {
        frontMatter: 6,
        moduleOpenings: 4,
        chapters: 25,
        nuclei: 7
      }
    })
  })

  it("preserves the existing default cases", () => {
    const result = resolveBookStudioLayoutOptions({})

    expect(result.cases.map((item) => item.id)).toEqual([
      "il-metodo-bando",
      "moduli/m-fc01-ministeri"
    ])
    expect(result.artifactPrefix).toBe("book-studio")
    expect(result.expectedCounts).toBeNull()
  })
})
```

- [ ] **Step 2: Eseguire il test e confermare il fallimento**

```powershell
npm test -- --run tests/book-studio-layout-options.test.ts
```

Expected: FAIL because the options module does not exist.

- [ ] **Step 3: Implementare il parser delle opzioni**

Create `scripts/book-studio-layout-options.mjs`:

```js
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
```

Add the matching declaration in `scripts/book-studio-layout-options.d.mts` so the strict TypeScript suite can import the `.mjs` helper without an implicit-`any` module:

```ts
export interface BookStudioLayoutCase {
  id: string
  label: string
}

export interface BookStudioLayoutOptions {
  cases: BookStudioLayoutCase[]
  artifactPrefix: string
  expectedCounts: Record<string, number> | null
}

export function resolveBookStudioLayoutOptions(
  env?: Record<string, string | undefined>
): BookStudioLayoutOptions
```

- [ ] **Step 4: Aggiungere attributi strutturali alle pagine renderizzate**

On every `<article className="bookPage ...">` emitted by chapter and front-matter renderers, add:

```tsx
data-chapter-path={page.chapter.path}
data-section-type={page.chapter.sectionType}
data-front-matter-layout={page.chapter.frontMatterLayout || undefined}
data-volume-module-code={page.chapter.volumeModuleCode || undefined}
```

These attributes are diagnostic and must not change visible output.

- [ ] **Step 5: Usare le opzioni nello script Playwright**

Import and resolve at the top of `verify-book-studio-layout.mjs`:

```js
import { resolveBookStudioLayoutOptions } from "./book-studio-layout-options.mjs"

const baseUrl = process.env.BOOK_STUDIO_URL || "http://127.0.0.1:3010"
const { cases, artifactPrefix, expectedCounts } = resolveBookStudioLayoutOptions(process.env)
```

Write screenshots to `artifacts/${artifactPrefix}-${current.label}.png` and the report to `artifacts/${artifactPrefix}-layout-report.json`.

- [ ] **Step 6: Raccogliere struttura, progressione e indice**

Extend the browser evaluation with:

```js
const structure = await page.evaluate(() => {
  const pages = Array.from(document.querySelectorAll(".bookPages .bookPage"))
  const unique = (values) => new Set(values.filter(Boolean)).size

  return {
    pageCount: pages.length,
    pageNumbers: pages.map((item) => Number(item.querySelector(".pageFooter span:last-child")?.textContent || 0)),
    frontMatter: unique(
      pages
        .filter((item) => item.getAttribute("data-front-matter-layout") !== "module-opening")
        .map((item) => item.getAttribute("data-front-matter-layout"))
    ),
    moduleOpenings: unique(
      pages
        .filter((item) => item.getAttribute("data-front-matter-layout") === "module-opening")
        .map((item) => item.getAttribute("data-chapter-path"))
    ),
    chapters: unique(
      pages
        .filter((item) => item.getAttribute("data-section-type") === "chapter")
        .map((item) => item.getAttribute("data-chapter-path"))
    ),
    nuclei: unique(
      Array.from(document.querySelectorAll(".bookPages [data-nucleus-id]"))
        .map((item) => item.getAttribute("data-nucleus-id"))
    ),
    indexNuclei: unique(
      Array.from(document.querySelectorAll(".bookPages .indexSubLine[data-nucleus-id]"))
        .map((item) => item.getAttribute("data-nucleus-id"))
    ),
    verificationHeadings: document.querySelectorAll(".bookPages .verificationHeading").length
  }
})
```

Ensure `data-nucleus-id` is placed on `.indexSubLine` itself, not only a child, so `indexNuclei` is measurable.

- [ ] **Step 7: Aggiungere fallimenti strutturali espliciti**

Append failures when:

```js
const expectedSequence = Array.from({ length: entry.structure.pageCount }, (_, index) => index + 1)

if (JSON.stringify(entry.structure.pageNumbers) !== JSON.stringify(expectedSequence)) {
  failures.push(`${entry.label}: numerazione pagine non progressiva`)
}

if (entry.structure.nuclei !== entry.structure.indexNuclei) {
  failures.push(`${entry.label}: nuclei testo=${entry.structure.nuclei}, indice=${entry.structure.indexNuclei}`)
}

if (expectedCounts) {
  for (const [key, expected] of Object.entries(expectedCounts)) {
    if (entry.structure[key] !== expected) {
      failures.push(`${entry.label}: ${key}=${entry.structure[key]}, atteso=${expected}`)
    }
  }
}
```

Keep the existing typography, overflow, overlap, font and image checks unchanged.

- [ ] **Step 8: Eseguire test e typecheck**

```powershell
npm test -- --run tests/book-studio-layout-options.test.ts tests/book-studio-index-pages.test.ts tests/book-preview.test.ts tests/editorial-typography.test.ts
npm run typecheck
```

Expected: all tests PASS; typecheck exit 0.

- [ ] **Step 9: Commit selettivo**

```powershell
git add -- 'scripts/book-studio-layout-options.mjs' 'scripts/book-studio-layout-options.d.mts' 'scripts/verify-book-studio-layout.mjs' 'app/components/book-studio-panel.tsx' 'tests/book-studio-layout-options.test.ts'
git diff --cached --check
git commit -m "test(book-studio): verify configurable KDP volumes"
```

### Task 6: Verifica integrata, report step 19 e chiusura CLI

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md`
- Generate diagnostics: `artifacts/vol-07-step-19-vol-07.png`
- Generate diagnostics: `artifacts/vol-07-step-19-layout-report.json`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`
- Modify through service only: `wiki/memory/agent/`

**Interfaces:**
- Consumes: tasks 1-5, `bookId` `volumi/vol-07`, pipeline step `19:VOL-07` in-progress.
- Produces: verified Book Studio rendering, review report, step 19 done, next `20:VOL-07`.

- [ ] **Step 1: Eseguire suite completa e controlli statici**

```powershell
npm run typecheck
npm test
git diff --check
```

Expected: typecheck exit 0; 41 or more test files PASS; 389 or more tests PASS; diff check exit 0.

- [ ] **Step 2: Avviare il Book Studio su porta 3010**

Use a hidden background process and preserve logs:

```powershell
$server = Start-Process -FilePath 'npm.cmd' `
  -ArgumentList @('run','dev','--','-p','3010') `
  -WindowStyle Hidden `
  -PassThru `
  -RedirectStandardOutput 'artifacts/vol-07-step-19-next.stdout.log' `
  -RedirectStandardError 'artifacts/vol-07-step-19-next.stderr.log'

$ready = $false
for($attempt = 0; $attempt -lt 60; $attempt++) {
  try {
    $response = Invoke-WebRequest -UseBasicParsing 'http://127.0.0.1:3010/?bookId=volumi%2Fvol-07#studio' -TimeoutSec 2
    if($response.StatusCode -eq 200) { $ready = $true; break }
  } catch {}
  Start-Sleep -Seconds 1
}
if(-not $ready) { throw 'Book Studio non disponibile sulla porta 3010.' }
```

- [ ] **Step 3: Eseguire il verifier sull'intero VOL-07**

Run inside `try/finally` so the process started in Step 2 is stopped:

```powershell
try {
  $env:BOOK_STUDIO_URL = 'http://127.0.0.1:3010'
  $env:BOOK_STUDIO_BOOK_IDS = 'volumi/vol-07'
  $env:BOOK_STUDIO_ARTIFACT_PREFIX = 'vol-07-step-19'
  $env:BOOK_STUDIO_EXPECTED_COUNTS = '{"frontMatter":6,"moduleOpenings":4,"chapters":25,"nuclei":7}'
  node scripts/verify-book-studio-layout.mjs
} finally {
  if($server -and -not $server.HasExited) { Stop-Process -Id $server.Id -Force }
  Remove-Item Env:BOOK_STUDIO_URL -ErrorAction SilentlyContinue
  Remove-Item Env:BOOK_STUDIO_BOOK_IDS -ErrorAction SilentlyContinue
  Remove-Item Env:BOOK_STUDIO_ARTIFACT_PREFIX -ErrorAction SilentlyContinue
  Remove-Item Env:BOOK_STUDIO_EXPECTED_COUNTS -ErrorAction SilentlyContinue
}
```

Expected: exit 0; JSON report and screenshot exist; zero overflow or overlap failures.

- [ ] **Step 4: Validare il JSON diagnostico senza affidarsi al log formattato**

```powershell
$entry = @(Get-Content -Raw 'artifacts/vol-07-step-19-layout-report.json' | ConvertFrom-Json)[0]
$entry.structure | Format-List
[pscustomobject]@{
  Pages = $entry.structure.pageCount
  FrontMatter = $entry.structure.frontMatter
  ModuleOpenings = $entry.structure.moduleOpenings
  Chapters = $entry.structure.chapters
  Nuclei = $entry.structure.nuclei
  IndexNuclei = $entry.structure.indexNuclei
  OverflowPages = @($entry.diagnostics | Where-Object { $_.overflow -gt 8 }).Count
  OverlapPages = @($entry.diagnostics | Where-Object { $_.overlaps.Count -gt 0 }).Count
} | Format-List
```

Expected: `Pages` is a positive integer; front matter 6; module openings 4; chapters 25; nuclei/index nuclei 7/7; overflow and overlap pages 0.

- [ ] **Step 5: Creare il report Markdown con i valori misurati**

Use `apply_patch` to create `wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md`. Its frontmatter must include:

```yaml
id: review-vol-07-step-19-kdp-layout
type: review
title: Impaginazione KDP - VOL-07
status: complete
domain: concorsi pubblici italiani
topics:
  - impaginazione KDP
  - Book Studio
entities:
  - Amazon KDP
source_refs: []
book_refs:
  - vol-07-sanita-amministrativa-professioni-sanitarie
confidence: 1
review_required: false
canonical: false
updated_at: 2026-08-04T00:00:00+02:00
created_at: 2026-08-04T00:00:00+02:00
tags:
  - pipeline-step-19
  - kdp-layout
  - vol-07
issue_type: kdp_layout
severity: none
affected_pages:
  - books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md
```

The body must record the integer `pageCount` printed in Step 4, then state: 6 front-matter sections, 4 module openings, 25 chapters, 7 nucleus headings, 7 index nucleus rows, progressive numbering, zero overflow, zero overlaps, Arial/Garamond scale, 23 mm mirrored gutter, no PDF generated, and step 20 as the page-by-page audit. Do not leave symbolic tokens or inferred values.

- [ ] **Step 6: Verificare report, artefatti e assenza di PDF**

```powershell
$report = Get-Content -Raw 'wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md'
[pscustomobject]@{
  ReportExists = (Test-Path 'wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md')
  JsonExists = (Test-Path 'artifacts/vol-07-step-19-layout-report.json')
  ScreenshotExists = (Test-Path 'artifacts/vol-07-step-19-vol-07.png')
  Placeholders = ([regex]::Matches($report, '(?i)\bTBD\b|\bTODO\b|<placeholder>')).Count
  Chapters = $report.Contains('25 capitoli')
  Nuclei = $report.Contains('7 nuclei')
  NoPdf = $report.Contains('Nessun PDF')
} | Format-List
git diff --check -- 'wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md'
```

Expected: all booleans true; placeholders 0; diff check exit 0. Confirm separately that `output/pdf/` has no new VOL-07 file.

- [ ] **Step 7: Tentare la chiusura canonica dello step 19**

```powershell
npm run pipeline -- complete VOL-07 --step 19 --json
```

Expected: `ok: true`, `passed: true`, zero blockers. A warning `no-gate` is informational and does not require `--accept`.

If and only if the JSON explicitly returns `gate-not-implemented`, run after the manual evidence above:

```powershell
npm run pipeline -- complete VOL-07 --step 19 --accept --note "Master KDP VOL-07 verificato nel Book Studio: 6 sezioni front matter, 4 aperture modulo, 25 capitoli, 7 nuclei indicizzati, numerazione progressiva, gutter 23 mm, zero overflow e sovrapposizioni; evidenza in wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md." --json
```

- [ ] **Step 8: Verificare lo stato pipeline**

```powershell
npm run pipeline -- status VOL-07 --json
```

Expected: `done: 164`, `pending: 5`, no blocked, no in-progress, next `20:VOL-07`.

- [ ] **Step 9: Registrare la traccia tramite LocalAgentMemory**

Use `LocalAgentMemory.fromConfig().captureConversation()` with:

```ts
{
  scope: "VOL-07",
  route: "pipeline-vol-07-step-19-kdp-book-studio",
  messages: [{ role: "user", content: "Procedi con lo step 19 nel Book Studio senza generare il PDF." }],
  reply: "Step 19 completato: master KDP renderizzato, indice nuclei riconciliato, report e test verificati; prossimo step 20.",
  metadata: {
    volume: "VOL-07",
    pipelineStep: 19,
    chapters: 25,
    nuclei: 7,
    nextStep: 20
  }
}
```

Do not edit JSONL files manually.

- [ ] **Step 10: Commit selettivo del report**

```powershell
git add -- 'wiki/reviews/pipeline/VOL-07/19-vol-07-impaginazione-kdp.md'
git diff --cached --check
git diff --cached --name-only
git commit -m "docs(vol-07): record KDP Book Studio layout"
```

Do not stage `pipeline/VOL-07/run-state.json` if its diff still includes earlier step 15-18 transitions. Do not stage shared LocalAgentMemory files or generated diagnostics unless the repository already tracks those exact artifact paths.

- [ ] **Step 11: Verifica finale fresca**

```powershell
npm run typecheck
npm test
npm run pipeline -- status VOL-07 --json
git diff --check
git log -6 --oneline
```

Expected: typecheck and full suite green; pipeline next 20; recent commits correspond to Tasks 1-6; no staged file remains.
