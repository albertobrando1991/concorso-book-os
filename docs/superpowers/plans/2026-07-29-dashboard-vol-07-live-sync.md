# Dashboard VOL-07 Live Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Aggiornare automaticamente la lista capitoli dello Studio quando arriva un nuovo payload VOL-07 con lo stesso `bookId`, preservando una selezione ancora valida.

**Architecture:** Estrarre la scelta del capitolo in una funzione pura e testabile. Cablarla nell'effetto di sincronizzazione di `BookStudioPanel`, facendo dipendere l'effetto dall'intero `initialData` invece che dal solo `bookId`; l'API e il parent restano invariati.

**Tech Stack:** Next.js 15, React 19, TypeScript 5.7, Vitest 2.

## Global Constraints

- Nessun polling periodico.
- Nessun rimontaggio forzato del workspace.
- Nessuna modifica all'API `book-studio` o allo stato della pipeline VOL-07.
- `initialChapterPath` valido ha precedenza; altrimenti si conserva `selectedPath` se ancora presente; in ultima istanza si seleziona il primo capitolo.
- Nessuna nuova dipendenza di test.
- Nessun commit durante questa esecuzione: il worktree contiene lo stato editoriale condiviso e i commit restano riservati allo step 23 della pipeline.

## File Structure

- Create: `app/components/book-studio-state.ts` — funzione pura per riconciliare la selezione con un nuovo elenco di capitoli.
- Create: `tests/book-studio-state.test.ts` — regressione sulla selezione e controllo del cablaggio nel componente.
- Modify: `app/components/book-studio-panel.tsx` — usa la funzione pura e reagisce al payload `initialData` aggiornato.

---

### Task 1: Riconciliazione pura della selezione

**Files:**
- Create: `app/components/book-studio-state.ts`
- Create: `tests/book-studio-state.test.ts`

**Interfaces:**
- Consumes: `chapters: ReadonlyArray<{ path: string }>`, `currentPath: string`, `requestedPath?: string`.
- Produces: `reconcileSelectedChapterPath(chapters, currentPath, requestedPath): string`.

- [ ] **Step 1: Scrivere il test fallente della funzione desiderata**

```ts
import { describe, expect, it } from "vitest"
import { reconcileSelectedChapterPath } from "@/app/components/book-studio-state"

const chapters = [
  { path: "books/moduli/m-sa02/chapters/00-piano.md" },
  { path: "books/moduli/m-sa02/chapters/01-mappa.md" }
]

describe("reconcileSelectedChapterPath", () => {
  it("uses an explicit valid path before the current selection", () => {
    expect(reconcileSelectedChapterPath(chapters, chapters[0].path, chapters[1].path)).toBe(chapters[1].path)
  })

  it("preserves the current selection when it still exists", () => {
    expect(reconcileSelectedChapterPath(chapters, chapters[1].path)).toBe(chapters[1].path)
  })

  it("falls back to the first chapter when the selection disappeared", () => {
    expect(reconcileSelectedChapterPath(chapters, "books/removed.md")).toBe(chapters[0].path)
  })

  it("returns an empty path for an empty payload", () => {
    expect(reconcileSelectedChapterPath([], "books/removed.md")).toBe("")
  })
})
```

- [ ] **Step 2: Eseguire il test e verificare RED**

Run: `npx vitest run tests/book-studio-state.test.ts`

Expected: FAIL perché `app/components/book-studio-state.ts` non esiste.

- [ ] **Step 3: Implementare la funzione minima**

```ts
interface ChapterPathItem {
  path: string
}

export function reconcileSelectedChapterPath(
  chapters: ReadonlyArray<ChapterPathItem>,
  currentPath: string,
  requestedPath?: string
) {
  if (requestedPath && chapters.some((chapter) => chapter.path === requestedPath)) return requestedPath
  if (chapters.some((chapter) => chapter.path === currentPath)) return currentPath

  return chapters[0]?.path || ""
}
```

- [ ] **Step 4: Eseguire il test e verificare GREEN**

Run: `npx vitest run tests/book-studio-state.test.ts`

Expected: 4 test passati.

### Task 2: Cablaggio del payload aggiornato nello Studio

**Files:**
- Modify: `tests/book-studio-state.test.ts`
- Modify: `app/components/book-studio-panel.tsx:1-115`

**Interfaces:**
- Consumes: `reconcileSelectedChapterPath` prodotto dal Task 1 e il prop `initialData: BookStudioData`.
- Produces: sincronizzazione dello stato locale quando cambia `initialData`, con selezione riconciliata.

- [ ] **Step 1: Aggiungere un test di cablaggio fallente**

```ts
import { readFile } from "node:fs/promises"

it("wires incoming payload changes to the chapter reconciliation", async () => {
  const source = await readFile("app/components/book-studio-panel.tsx", "utf8")

  expect(source).toContain('from "./book-studio-state"')
  expect(source).toContain(
    "setSelectedPath((currentPath) => reconcileSelectedChapterPath(initialData.chapters, currentPath, initialChapterPath))"
  )
  expect(source).toContain("}, [initialData, initialChapterPath])")
})
```

- [ ] **Step 2: Eseguire il test e verificare RED**

Run: `npx vitest run tests/book-studio-state.test.ts`

Expected: FAIL perché il componente non importa né usa ancora `reconcileSelectedChapterPath` e l'effetto dipende da `initialData.bookId`.

- [ ] **Step 3: Applicare la modifica minima al componente**

Aggiungere l'import:

```ts
import { reconcileSelectedChapterPath } from "./book-studio-state"
```

Sostituire l'effetto di sincronizzazione con:

```ts
useEffect(() => {
  setData(initialData)
  setSelectedPath((currentPath) =>
    reconcileSelectedChapterPath(initialData.chapters, currentPath, initialChapterPath)
  )
  setViewMode("chapter")
  setMessage("")
  setError("")
  setLastResult(null)
  setMeasuredPages(null)
}, [initialData, initialChapterPath])
```

- [ ] **Step 4: Eseguire il test mirato e verificare GREEN**

Run: `npx vitest run tests/book-studio-state.test.ts`

Expected: 5 test passati.

- [ ] **Step 5: Eseguire typecheck**

Run: `npm run typecheck`

Expected: exit code 0.

### Task 3: Verifica di regressione e dato VOL-07

**Files:**
- Verify: `app/components/book-studio-state.ts`
- Verify: `app/components/book-studio-panel.tsx`
- Verify: `tests/book-studio-state.test.ts`

**Interfaces:**
- Consumes: implementazione completata nei Task 1-2.
- Produces: evidenza che API, test e compilazione restano coerenti.

- [ ] **Step 1: Eseguire la suite completa**

Run: `npm test -- --run`

Expected: tutti i test passano, inclusi i 5 nuovi test.

- [ ] **Step 2: Verificare il payload reale VOL-07**

Run:

```powershell
$data=Invoke-RestMethod -Uri 'http://127.0.0.1:3000/api/book-studio?bookId=volumi%2Fvol-07'
$data.chapters | Where-Object { $_.path -like '*m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md' }
```

Expected: una riga con titolo `Professioni sanitarie: profili, requisiti e prove`.

- [ ] **Step 3: Controllare il diff**

Run: `git diff --check`

Expected: nessun errore; sono ammissibili soltanto avvisi di normalizzazione CRLF/LF su file preesistenti.

- [ ] **Step 4: Ricaricare VOL-07 nella dashboard**

Aprire `http://127.0.0.1:3000/?bookId=volumi%2Fvol-07#studio` e verificare che il capitolo 01 M-SA02 compaia nella lista senza usare il pulsante manuale di refresh.
