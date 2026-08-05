# Dashboard Volume Default Preview Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Aprire i volumi compositi sul primo capitolo editoriale reale invece che sul front matter generato comune.

**Architecture:** Aggiungere una funzione pura che sceglie il percorso iniziale dall'elenco capitoli. `BookStudioPanel` la usa soltanto all'inizializzazione, mentre selezione esplicita, click manuali e refresh conservano il comportamento esistente.

**Tech Stack:** React 19, Next.js 15, TypeScript 5.7, Vitest 2.

## Global Constraints

- Nessun polling o rimontaggio forzato.
- Nessuna modifica all'API o alla pipeline VOL-07.
- Nessuna nuova dipendenza.
- Nessun commit: i commit restano riservati allo step 23 della pipeline.

---

## File Structure

- Modify: `app/components/book-studio-state.ts` — scelta pura del capitolo iniziale.
- Modify: `app/components/book-studio-panel.tsx` — usa la scelta pura nello stato iniziale.
- Modify: `tests/book-studio-state.test.ts` — regressione sui volumi compositi e fallback.

### Task 1: Selezione iniziale dell'anteprima

**Files:**
- Modify: `app/components/book-studio-state.ts`
- Modify: `app/components/book-studio-panel.tsx:15-90`
- Test: `tests/book-studio-state.test.ts`

**Interfaces:**
- Consumes: `chapters: ReadonlyArray<{ path: string; isGenerated?: boolean; status?: string }>` e `requestedPath?: string`.
- Produces: `getInitialBookStudioChapterPath(chapters, requestedPath): string`.

- [ ] **Step 1: Scrivere il test fallente**

Importare `getInitialBookStudioChapterPath` e aggiungere:

```ts
it("opens a composite volume on its first editorial chapter", () => {
  const volumeChapters = [
    { path: "books/volumi/vol-07/front-matter/fm1.md", isGenerated: true, status: "generated" },
    { path: "books/moduli/m-sa01/chapters/00-piano.md", isGenerated: false, status: "structure" },
    { path: "books/moduli/m-sa02/chapters/01-profili.md", isGenerated: false, status: "editorial_draft" }
  ]

  expect(getInitialBookStudioChapterPath(volumeChapters)).toBe(volumeChapters[2].path)
  expect(getInitialBookStudioChapterPath(volumeChapters, volumeChapters[0].path)).toBe(volumeChapters[0].path)
})

it("falls back to a non-generated chapter and then to the first available item", () => {
  const structureOnly = [
    { path: "books/front-matter/fm1.md", isGenerated: true, status: "generated" },
    { path: "books/chapters/00-piano.md", isGenerated: false, status: "structure" }
  ]

  expect(getInitialBookStudioChapterPath(structureOnly)).toBe(structureOnly[1].path)
  expect(getInitialBookStudioChapterPath([structureOnly[0]])).toBe(structureOnly[0].path)
  expect(getInitialBookStudioChapterPath([])).toBe("")
})
```

- [ ] **Step 2: Eseguire RED**

Run: `npx vitest run tests/book-studio-state.test.ts`

Expected: FAIL perché `getInitialBookStudioChapterPath` non è esportata.

- [ ] **Step 3: Implementare la funzione minima**

```ts
interface InitialChapterItem extends ChapterPathItem {
  isGenerated?: boolean
  status?: string
}

export function getInitialBookStudioChapterPath(
  chapters: ReadonlyArray<InitialChapterItem>,
  requestedPath?: string
) {
  if (requestedPath && chapters.some((chapter) => chapter.path === requestedPath)) return requestedPath

  return (
    chapters.find((chapter) => !chapter.isGenerated && chapter.status !== "structure")?.path ||
    chapters.find((chapter) => !chapter.isGenerated)?.path ||
    chapters[0]?.path ||
    ""
  )
}
```

- [ ] **Step 4: Collegare il componente**

Importare la funzione in `book-studio-panel.tsx`, inizializzando:

```ts
selectedPath: getInitialBookStudioChapterPath(initialData.chapters, initialChapterPath)
```

Rimuovere la funzione locale `getInitialChapterPath`.

- [ ] **Step 5: Eseguire GREEN e verifiche**

Run:

```powershell
npx vitest run tests/book-studio-state.test.ts
npm run typecheck
npm test -- --run
```

Expected: 7 test mirati passati, typecheck exit 0, suite completa senza failure.

- [ ] **Step 6: Verificare il dato VOL-07**

Eseguire la funzione contro il payload reale dell'API e confermare che il percorso scelto sia:

```text
books/moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md
```

Riaprire `http://127.0.0.1:3000/?bookId=volumi%2Fvol-07#studio`.

- [ ] **Step 7: Preservare il worktree**

Non creare commit, merge o push. Lasciare `vol-07-pipeline-start` nel worktree corrente per lo step 23.
