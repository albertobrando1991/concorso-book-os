# Student Index and Staff Editorial Plan Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Separare in tutti i volumi l'indice destinato allo studente dal piano editoriale dello staff, migrare i 25 piani di modulo nel percorso canonico e correggere titoli, accenti e numerazione visibili del VOL-07.

**Architecture:** `BookStudioData.chapters` continuerà a contenere soltanto sezioni realmente leggibili; un nuovo builder server-side ricaverà `editorialPlan` dalla scheda canonica e dal run-state della pipeline. La visibilità dei documenti interni sarà centralizzata, riusata da Book Studio, Manual Writer e discovery della pipeline, mentre una migrazione repository-wide porterà ogni piano in `planning/`.

**Tech Stack:** TypeScript 5.7, Next.js 15, React 19, Vitest 2.1, Markdown/frontmatter wiki, CLI pipeline TypeScript.

## Global Constraints

- `chapters/` contiene esclusivamente testo destinato al lettore.
- `planning/` contiene piani, matrici e strumenti interni.
- `pipeline/<VOL>/run-state.json` non viene mai modificato manualmente.
- I capitoli non dichiarati non vengono inventati.
- ID, slug, nomi file, tag tecnici e chiavi macchina restano ASCII.
- Le stringhe visibili usano accenti italiani corretti e non contengono mojibake.
- Il titolo e l'H1 di un capitolo non contengono il numero: la numerazione proviene da `outline_section`.
- L'anteprima commerciale non include `editorialPlan`.
- Conservare tutte le modifiche preesistenti nel worktree e creare commit selettivi.
- Nessun push remoto senza una richiesta esplicita dell'utente.

---

## File map

### Nuovi file

- `src/server/book/editorial-plan.ts`: costruisce moduli, target, stato aggregato e prossimo step per il pannello staff.
- `src/server/wiki/editorial-document.ts`: unica regola di riconoscimento dei documenti interni e dei piani legacy.
- `app/components/editorial-plan-panel.tsx`: rendering non interattivo del piano staff.
- `tests/editorial-plan.test.ts`: test del builder con e senza run-state.
- `tests/editorial-document.test.ts`: test della classificazione condivisa.
- `tests/editorial-layout.test.ts`: controllo repository-wide della collocazione dei 25 piani.
- `tests/book-studio-display.test.ts`: test delle etichette visibili e della numerazione.
- `tests/vol-07-visible-copy.test.ts`: audit automatico delle stringhe visibili del VOL-07.

### File modificati

- `src/pipeline/spec/parse-volume-spec.ts`: aggiunge `title` a `VolumeSpecChapter`.
- `src/pipeline/spec/validate-volume-spec.ts`: richiede un titolo ai capitoli dichiarati.
- `src/pipeline/spec/load-volume-spec.ts`: non deriva mai un piano legacy come capitolo.
- `src/server/book/book-preview.ts`: filtra documenti staff-only e allega `editorialPlan`.
- `src/server/agents/manual-writer-agent.ts`: esclude documenti staff-only dall'elenco dei capitoli.
- `app/api/book-studio/route.ts`: passa il project root al builder.
- `app/components/book-studio-panel.tsx`: inserisce il pannello staff separato dall'indice.
- `app/globals.css`: stili del pannello staff e delle etichette di stato.
- `src/catalog/text-volumes.ts`: corregge il titolo visibile del VOL-07.
- `wiki/templates/scheda-pipeline-volume-template.md`: aggiunge la colonna canonica `Titolo`.
- `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`: registra i titoli dichiarati.
- `wiki/books/moduli/m-sa01-sanita-amministrativa/index.md`: corregge `Sanità` e i collegamenti al planning.
- `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`: corregge `Sanità` e i collegamenti al planning.
- `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md`: corregge `Sanità` e i collegamenti al planning.
- `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/index.md`: corregge `Sanità` e i collegamenti al planning.
- `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`: aggiunge `outline_section: 3`.
- `docs/PIPELINE.md`: documenta la separazione lettore/staff.
- `wiki/AGENTS.md`: rende la separazione una regola agentica canonica.
- `.agents/skills/pipeline-volume/SKILL.md`: allinea l'esecuzione della pipeline alla nuova struttura.
- `tests/book-preview.test.ts`, `tests/manual-writer-agent.test.ts`, `tests/pipeline/volume-spec.test.ts`, `tests/pipeline/build-steps.test.ts`, `tests/pipeline/vol-07-spec.test.ts`: regressioni TDD.

### Migrazioni

I 23 file `wiki/books/moduli/*/chapters/00-piano-editoriale.md` vengono spostati in `planning/00-piano-editoriale.md`. I moduli `m-fc01-ministeri` e `m-fc02-agenzie-fiscali` sono già nel percorso corretto e richiedono soltanto la normalizzazione del tipo.

---

### Task 1: Titolo canonico dei capitoli dichiarati nella scheda pipeline

**Files:**
- Modify: `src/pipeline/spec/parse-volume-spec.ts`
- Modify: `src/pipeline/spec/validate-volume-spec.ts`
- Modify: `wiki/templates/scheda-pipeline-volume-template.md`
- Modify: `tests/pipeline/volume-spec.test.ts`

**Interfaces:**
- Produces: `VolumeSpecChapter.title: string`
- Produces: validazione `modules[N].chapters[M].title` per tabelle dichiarate
- Consumes later: `buildEditorialPlan()` usa `chapter.title` senza ricavarlo dallo slug

- [ ] **Step 1: Estendere il fixture del test con la colonna `Titolo`**

Nel fixture `complete` usare:

```markdown
| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Perimetro delle Agenzie fiscali | chapters/01-perimetro.md | planning/02-matrice-copertura-didattica.md | completo | |
| 02 | Tributi e procedimenti | chapters/02-tributi.md | planning/02-matrice-copertura-didattica.md | completo | rivedere soglie |
```

Aggiornare l'attesa:

```ts
expect(module.chapters[0]).toEqual({
  number: "01",
  title: "Perimetro delle Agenzie fiscali",
  file: "chapters/01-perimetro.md",
  matrix: "planning/02-matrice-copertura-didattica.md",
  expectedStatus: "completo",
  notes: ""
})
```

- [ ] **Step 2: Aggiungere il test rosso per il titolo mancante**

```ts
it("requires a public title for every explicitly declared chapter", () => {
  const markdown = complete.replace("Perimetro delle Agenzie fiscali", "")
  expect(issueFields(markdown)).toContain("modules[0].chapters[0].title")
})
```

- [ ] **Step 3: Eseguire il test mirato e verificare il fallimento**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/pipeline/volume-spec.test.ts
```

Expected: FAIL perché `VolumeSpecChapter` non espone `title` e la validazione non lo controlla.

- [ ] **Step 4: Implementare parsing e validazione minima**

In `parse-volume-spec.ts`:

```ts
export interface VolumeSpecChapter {
  number: string
  title: string
  file: string
  matrix: string
  expectedStatus: string
  notes: string
}

function toChapter(row: Record<string, string>): VolumeSpecChapter {
  return {
    number: row["#"] ?? row.numero ?? "",
    title: row.titolo ?? row.title ?? "",
    file: row.file ?? "",
    matrix: row.matrice ?? "",
    expectedStatus: row["stato atteso"] ?? "",
    notes: row.note ?? ""
  }
}
```

In `validate-volume-spec.ts` passare il capitolo intero e `module.chaptersSource`:

```ts
if (chaptersSource === "declared" && !chapter.title.trim()) {
  issues.push({
    field: `${prefix}.title`,
    message: "Titolo capitolo mancante nella colonna Titolo.",
    line
  })
}
```

I capitoli derivati possono mantenere `title: ""` perché il titolo sarà letto dal file.

- [ ] **Step 5: Aggiornare il template dello staff**

La tabella del template deve essere:

```markdown
| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Titolo editoriale destinato al lettore | chapters/01-nome-file.md | planning/02-matrice-copertura-didattica.md | completo | |
```

Spiegare subito sopra che il titolo è obbligatorio quando la tabella è dichiarata.

- [ ] **Step 6: Eseguire i test della specifica**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/pipeline/volume-spec.test.ts tests/pipeline/build-steps.test.ts
```

Expected: PASS.

- [ ] **Step 7: Commit selettivo**

```powershell
git add src/pipeline/spec/parse-volume-spec.ts src/pipeline/spec/validate-volume-spec.ts wiki/templates/scheda-pipeline-volume-template.md tests/pipeline/volume-spec.test.ts
git commit -m "feat: require titles for declared pipeline chapters"
```

---

### Task 2: Classificazione condivisa dei documenti editoriali interni

**Files:**
- Create: `src/server/wiki/editorial-document.ts`
- Create: `tests/editorial-document.test.ts`
- Modify: `src/server/book/book-preview.ts`
- Modify: `src/server/agents/manual-writer-agent.ts`
- Modify: `src/pipeline/spec/load-volume-spec.ts`
- Modify: `tests/book-preview.test.ts`
- Modify: `tests/manual-writer-agent.test.ts`
- Modify: `tests/pipeline/build-steps.test.ts`

**Interfaces:**
- Produces: `isLegacyEditorialPlanPath(path: string): boolean`
- Produces: `isStaffOnlyBookDocument(path: string, data?: Record<string, unknown>): boolean`
- Consumes: Book Studio, Manual Writer e discovery dei capitoli derivati

- [ ] **Step 1: Scrivere i test rossi della regola condivisa**

```ts
import { describe, expect, it } from "vitest"
import {
  isLegacyEditorialPlanPath,
  isStaffOnlyBookDocument
} from "@/src/server/wiki/editorial-document"

describe("editorial document visibility", () => {
  it("recognizes the legacy module plan path", () => {
    expect(isLegacyEditorialPlanPath("books/moduli/m-sa01/chapters/00-piano-editoriale.md")).toBe(true)
  })

  it("recognizes canonical staff-only metadata", () => {
    expect(isStaffOnlyBookDocument("books/moduli/m-sa01/chapters/altro.md", { type: "editorial_plan" })).toBe(true)
    expect(isStaffOnlyBookDocument("books/moduli/m-sa01/chapters/altro.md", {
      tags: ["specialist-module-plan"]
    })).toBe(true)
  })

  it("keeps a real numbered chapter visible", () => {
    expect(isStaffOnlyBookDocument("books/moduli/m-sa01/chapters/04-atti.md", {
      type: "book_chapter",
      outline_section: 4
    })).toBe(false)
  })
})
```

- [ ] **Step 2: Eseguire il test e verificare il fallimento**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-document.test.ts
```

Expected: FAIL perché il modulo non esiste.

- [ ] **Step 3: Implementare la regola minima**

```ts
export function isLegacyEditorialPlanPath(value: string) {
  return /\/chapters\/00-piano-editoriale\.md$/i.test(value.replace(/\\/g, "/"))
}

export function isStaffOnlyBookDocument(
  value: string,
  data: Record<string, unknown> = {}
) {
  const type = String(data.type ?? "").toLowerCase()
  const tags = Array.isArray(data.tags) ? data.tags.map((tag) => String(tag).toLowerCase()) : []

  return (
    value.replace(/\\/g, "/").includes("/planning/") ||
    isLegacyEditorialPlanPath(value) ||
    type === "editorial_plan" ||
    type === "module_plan" ||
    tags.includes("specialist-module-plan")
  )
}
```

- [ ] **Step 4: Rendere rosso il test Book Studio esistente**

Nel test `loads nested specialist module books`, creare sia il piano legacy sia `chapters/01-capitolo.md` e attendere:

```ts
expect(data.chapters.map((chapter) => chapter.path)).toEqual([
  "books/moduli/m-fl01-comuni-unioni/chapters/01-capitolo.md"
])
expect(data.summary.structure).toBe(0)
```

- [ ] **Step 5: Filtrare i documenti interni durante il caricamento**

In `buildSingleBookStudioData`, leggere frontmatter e percorso prima di creare `BookStudioChapter`, quindi scartare:

```ts
if (isStaffOnlyBookDocument(file, parsed.data as Record<string, unknown>)) return null
```

Applicare una type guard dopo `Promise.all`:

```ts
const chapters = loaded.filter((chapter): chapter is BookStudioChapter => chapter !== null)
```

- [ ] **Step 6: Aggiungere e rendere rosso il test Manual Writer**

Nel fixture con `00-piano-editoriale.md` e un capitolo reale:

```ts
expect(await agent.listChapters("moduli/m-fl01-comuni-unioni")).toEqual([
  expect.objectContaining({
    path: "books/moduli/m-fl01-comuni-unioni/chapters/01-capitolo.md"
  })
])
```

- [ ] **Step 7: Applicare la stessa regola al Manual Writer**

Nel ciclo `listChapters`:

```ts
for (const file of files.filter(
  (item) => item.includes("/chapters/") && !isLegacyEditorialPlanPath(item)
)) {
  // parsing esistente
  if (isStaffOnlyBookDocument(file, data)) continue
}
```

- [ ] **Step 8: Proteggere la derivazione dei capitoli della pipeline**

In `load-volume-spec.ts`:

```ts
return entries
  .filter((entry) =>
    entry.isFile() &&
    entry.name.endsWith(".md") &&
    !entry.name.startsWith("_") &&
    !isLegacyEditorialPlanPath(`/chapters/${entry.name}`)
  )
```

Aggiungere al test di build-step un modulo derivato con soli `00-piano-editoriale.md` e verificare `chapters: []`.

- [ ] **Step 9: Eseguire i test mirati**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-document.test.ts tests/book-preview.test.ts tests/manual-writer-agent.test.ts tests/pipeline/build-steps.test.ts
```

Expected: PASS.

- [ ] **Step 10: Commit selettivo**

```powershell
git add src/server/wiki/editorial-document.ts src/server/book/book-preview.ts src/server/agents/manual-writer-agent.ts src/pipeline/spec/load-volume-spec.ts tests/editorial-document.test.ts tests/book-preview.test.ts tests/manual-writer-agent.test.ts tests/pipeline/build-steps.test.ts
git commit -m "fix: keep editorial plans out of reader chapters"
```

---

### Task 3: Builder del piano editoriale staff

**Files:**
- Create: `src/server/book/editorial-plan.ts`
- Create: `tests/editorial-plan.test.ts`
- Modify: `src/server/book/book-preview.ts`
- Modify: `app/api/book-studio/route.ts`
- Modify: `tests/book-preview.test.ts`

**Interfaces:**
- Produces: `EditorialTargetState`
- Produces: `BookStudioEditorialTarget`
- Produces: `BookStudioEditorialModule`
- Produces: `BookStudioEditorialPlan`
- Produces: `buildEditorialPlan(input): Promise<BookStudioEditorialPlan | null>`
- Consumes: `VolumeSpecChapter.title`, `loadVolumeSpec()`, `loadRunState()`

- [ ] **Step 1: Definire nel test il contratto dei dati**

```ts
expect(plan).toMatchObject({
  volumeCode: "VOL-07",
  modules: [
    {
      code: "M-SA01",
      title: "Sanità amministrativa",
      chaptersSource: "declared",
      targets: [
        {
          number: "04",
          title: "Atti, procedimenti e flussi informativi nelle aziende sanitarie",
          exists: true,
          state: "in-review",
          nextStep: "10"
        },
        {
          number: "05",
          title: "Documentazione sanitaria, accesso, privacy e conservazione",
          exists: false,
          state: "to-plan",
          nextStep: "08"
        }
      ]
    }
  ]
})
```

Il fixture deve avere una scheda pipeline, un indice modulo, il file del capitolo 04 e un run-state con step 08-09 `done` e step 10 `in-progress`.

- [ ] **Step 2: Aggiungere i casi senza run-state e senza scheda**

```ts
it("uses declared targets when the run-state does not exist", async () => {
  expect((await buildEditorialPlan(inputWithoutRunState))?.modules[0].targets[0]).toMatchObject({
    state: "written",
    exists: true
  })
})

it("returns null when the catalog volume has no pipeline sheet", async () => {
  expect(await buildEditorialPlan(inputWithoutSpec)).toBeNull()
})
```

- [ ] **Step 3: Eseguire il test e verificare il fallimento**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-plan.test.ts
```

Expected: FAIL perché builder e tipi non esistono.

- [ ] **Step 4: Implementare i tipi**

```ts
export type EditorialTargetState =
  | "to-plan"
  | "to-write"
  | "in-progress"
  | "written"
  | "in-review"
  | "complete"
  | "blocked"

export interface BookStudioEditorialTarget {
  number: string
  title: string
  path: string
  exists: boolean
  state: EditorialTargetState
  nextStep: string
  gate: string
}

export interface BookStudioEditorialModule {
  code: string
  title: string
  moduleId: string
  priority: number
  chaptersSource: "declared" | "derived"
  targets: BookStudioEditorialTarget[]
}

export interface BookStudioEditorialPlan {
  volumeCode: string
  updatedAt: string
  modules: BookStudioEditorialModule[]
}
```

- [ ] **Step 5: Implementare la firma del builder**

```ts
export async function buildEditorialPlan(input: {
  store: FileWikiStore
  projectRoot: string
  bookId: string
}): Promise<BookStudioEditorialPlan | null>
```

Regole:

1. trovare il volume con `findTextVolumeForBookId`;
2. restituire `null` per cataloghi senza moduli o senza scheda;
3. caricare `loadVolumeSpec({ wikiRoot: store.getRoot(), volumeCode })`;
4. caricare facoltativamente `loadRunState(projectRoot, volumeCode)`;
5. filtrare un solo modulo quando `bookId` è `moduli/...`;
6. leggere titolo e frontmatter dei file esistenti;
7. usare il titolo dichiarato per i file assenti;
8. ordinare moduli per `priority` e target numericamente.

- [ ] **Step 6: Implementare la funzione di stato aggregato**

```ts
function targetState(
  steps: StepRecord[],
  exists: boolean,
  fileStatus: string
): EditorialTargetState {
  if (steps.some((step) => step.status === "blocked")) return "blocked"
  if (steps.every((step) => step.status === "done" || step.status === "skipped")) return "complete"
  if (steps.some((step) => step.status === "in-progress" || step.status === "awaiting-agent")) return "in-progress"
  if (steps.some((step) => step.id === "09" && step.status === "done")) return "in-review"
  if (steps.some((step) => step.id === "08" && step.status === "done")) return "to-write"
  if (exists && fileStatus !== "structure") return "written"
  return "to-plan"
}
```

Per un array vuoto, evitare il falso positivo di `every()` controllando prima `steps.length > 0`.

- [ ] **Step 7: Collegare il builder a `BookStudioData`**

In `book-preview.ts`:

```ts
export interface BookStudioData {
  // campi esistenti
  editorialPlan: BookStudioEditorialPlan | null
}

export async function buildBookStudioData(
  store: FileWikiStore,
  bookId = "il-metodo-bando",
  options: { projectRoot?: string } = {}
): Promise<BookStudioData>
```

Costruire prima i dati leggibili e aggiungere:

```ts
editorialPlan: options.projectRoot
  ? await buildEditorialPlan({ store, projectRoot: options.projectRoot, bookId: normalizedBookId })
  : null
```

- [ ] **Step 8: Passare il project root dall'API**

```ts
const data = await buildBookStudioData(
  new FileWikiStore(getWikiRoot()),
  bookId,
  { projectRoot: getProjectRoot() }
)
```

- [ ] **Step 9: Eseguire i test del builder e del preview**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-plan.test.ts tests/book-preview.test.ts
```

Expected: PASS, inclusi `editorialPlan: null` nei fixture senza project root.

- [ ] **Step 10: Commit selettivo**

```powershell
git add src/server/book/editorial-plan.ts src/server/book/book-preview.ts app/api/book-studio/route.ts tests/editorial-plan.test.ts tests/book-preview.test.ts
git commit -m "feat: expose pipeline-backed staff editorial plan"
```

---

### Task 4: Sezione visuale separata nella dashboard

**Files:**
- Create: `app/components/editorial-plan-panel.tsx`
- Create: `tests/book-studio-display.test.ts`
- Modify: `app/components/book-studio-panel.tsx`
- Modify: `app/globals.css`

**Interfaces:**
- Consumes: `BookStudioEditorialPlan`
- Produces: `editorialTargetStateLabel(state): string`
- Produces: lista staff non selezionabile e non inclusa in `previewChapters`

- [ ] **Step 1: Scrivere il test rosso delle etichette**

```ts
import { describe, expect, it } from "vitest"
import { editorialTargetStateLabel, formatChapterLabel } from "@/app/components/editorial-plan-panel"

describe("Book Studio display labels", () => {
  it("formats staff chapter numbers with leading zero and a long dash", () => {
    expect(formatChapterLabel("3", "Discipline professionali")).toBe(
      "Capitolo 03 — Discipline professionali"
    )
  })

  it.each([
    ["to-plan", "Da pianificare"],
    ["to-write", "Da scrivere"],
    ["in-progress", "In lavorazione"],
    ["written", "Scritto"],
    ["in-review", "In revisione"],
    ["complete", "Completato"],
    ["blocked", "Bloccato"]
  ] as const)("maps %s to %s", (state, label) => {
    expect(editorialTargetStateLabel(state)).toBe(label)
  })
})
```

- [ ] **Step 2: Eseguire il test e verificare il fallimento**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/book-studio-display.test.ts
```

Expected: FAIL perché il componente non esiste.

- [ ] **Step 3: Implementare il componente**

Il componente deve rendere:

```tsx
export function EditorialPlanPanel({ plan }: { plan: BookStudioEditorialPlan }) {
  return (
    <section className="editorialPlanPanel" aria-label="Piano editoriale staff">
      <div className="editorialPlanHeading">
        <span>Piano editoriale staff</span>
        <small>Non incluso nell'anteprima del libro</small>
      </div>
      {plan.modules.map((module) => (
        <details className="editorialPlanModule" key={module.code} open>
          <summary>{formatCodedTitle(module.code, module.title)}</summary>
          {module.targets.length ? (
            module.targets.map((target) => (
              <div className="editorialPlanTarget" key={target.path}>
                <span>{formatChapterLabel(target.number, target.title)}</span>
                <small>
                  {editorialTargetStateLabel(target.state)}
                  {target.nextStep ? ` · prossimo step ${target.nextStep}` : ""}
                </small>
              </div>
            ))
          ) : (
            <p>Capitoli non ancora dichiarati nella pipeline.</p>
          )}
        </details>
      ))}
    </section>
  )
}
```

`formatCodedTitle()` deve eliminare un eventuale codice già presente nel titolo e restituire `CODICE — Titolo`.

- [ ] **Step 4: Inserire il pannello fuori da `chapterList`**

In `BookStudioPanel`, dopo il blocco dell'indice:

```tsx
{data.editorialPlan ? <EditorialPlanPanel plan={data.editorialPlan} /> : null}
```

Non aggiungere target pianificati a `mainChapters`, `publishableChapters`, `previewChapters`, Manual Writer o Editorial Reviewer.

- [ ] **Step 5: Aggiungere gli stili**

```css
.editorialPlanPanel {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid var(--line);
}

.editorialPlanHeading,
.editorialPlanTarget {
  display: grid;
  gap: 3px;
}

.editorialPlanHeading > span,
.editorialPlanModule summary {
  font-weight: 700;
}

.editorialPlanHeading small,
.editorialPlanTarget small,
.editorialPlanModule p {
  color: var(--muted);
  font-size: 12px;
}

.editorialPlanModule {
  margin-top: 10px;
}

.editorialPlanTarget {
  margin-top: 6px;
  padding: 8px;
  border: 1px dashed var(--line);
  border-radius: 5px;
  background: #fff;
}
```

- [ ] **Step 6: Eseguire test e typecheck**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/book-studio-display.test.ts tests/book-studio-state.test.ts
npm run typecheck
```

Expected: PASS.

- [ ] **Step 7: Commit selettivo**

```powershell
git add app/components/editorial-plan-panel.tsx app/components/book-studio-panel.tsx app/globals.css tests/book-studio-display.test.ts
git commit -m "feat: separate staff plan from student preview"
```

---

### Task 5: Migrazione repository-wide dei 25 piani editoriali

**Files:**
- Create: `tests/editorial-layout.test.ts`
- Move: 23 file da `wiki/books/moduli/*/chapters/00-piano-editoriale.md` a `wiki/books/moduli/*/planning/00-piano-editoriale.md`
- Modify: 25 file `wiki/books/moduli/*/planning/00-piano-editoriale.md`
- Modify: gli `index.md` e gli altri file restituiti da `rg -l "chapters/00-piano-editoriale"`

**Interfaces:**
- Produces: percorso canonico unico `planning/00-piano-editoriale.md`
- Produces: `type: editorial_plan`
- Produces: tag `specialist-module-plan`
- Consumes later: audit repository e discovery sicura della pipeline

- [ ] **Step 1: Scrivere il test repository-wide e verificarne il fallimento**

```ts
it("keeps every catalog module plan under planning", async () => {
  const moduleIds = [...new Set(TEXT_VOLUME_CATALOG.flatMap((volume) => volume.bookIds))]
    .filter((bookId) => bookId.startsWith("moduli/"))

  expect(moduleIds).toHaveLength(TEXT_CATALOG_MODULE_COUNT)

  for (const moduleId of moduleIds) {
    expect(await exists(path.join(wikiRoot, "books", moduleId, "chapters", "00-piano-editoriale.md"))).toBe(false)
    const planPath = path.join(wikiRoot, "books", moduleId, "planning", "00-piano-editoriale.md")
    expect(await exists(planPath)).toBe(true)
    const data = parseFrontmatter(await readFile(planPath, "utf8")).data
    expect(data.type).toBe("editorial_plan")
    expect(data.tags).toContain("specialist-module-plan")
  }
})
```

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-layout.test.ts
```

Expected: FAIL sui 23 moduli legacy e sui due `type: module_plan`.

- [ ] **Step 2: Registrare l'inventario esatto prima della migrazione**

Run:

```powershell
Get-ChildItem wiki\books\moduli -Recurse -Filter 00-piano-editoriale.md -File |
  ForEach-Object { $_.FullName.Substring((Get-Location).Path.Length + 1) }
```

Expected: 25 file totali, 23 sotto `chapters/` e 2 sotto `planning/`.

- [ ] **Step 3: Spostare i 23 file senza alterarne la cronologia**

Usare una patch `*** Move to:` per ciascuno dei moduli legacy:

```text
m-fc03, m-fc04, m-fc05,
m-fl01, m-fl02, m-fl03, m-fl04,
m-ir01, m-ir02, m-ir03, m-ir04,
m-sa01, m-sa02, m-sa03, m-sa04,
m-sp01, m-sp02, m-sp03, m-sp04,
m-tr01, m-tr02, m-tr03, m-tr04
```

Ogni destinazione è:

```text
wiki/books/moduli/<module-id>/planning/00-piano-editoriale.md
```

Prima di ogni move verificare che la destinazione non esista.

- [ ] **Step 4: Normalizzare il frontmatter dei 25 piani**

Per tutti:

```yaml
type: editorial_plan
```

Conservare `id`, `book_id`, fonti, stato e contenuto. Rimuovere `outline_section` perché non sono capitoli. Conservare o aggiungere:

```yaml
tags: [..., "specialist-module-plan", ...]
```

- [ ] **Step 5: Aggiornare tutti i riferimenti**

Run:

```powershell
rg -l "books/moduli/.+/chapters/00-piano-editoriale|chapters/00-piano-editoriale" wiki docs tests src
```

In ogni riferimento editoriale sostituire:

```text
chapters/00-piano-editoriale
```

con:

```text
planning/00-piano-editoriale
```

Non cambiare i fixture che testano intenzionalmente la compatibilità legacy.

- [ ] **Step 6: Eseguire l'audit e i test di discovery**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-layout.test.ts tests/book-preview.test.ts tests/manual-writer-agent.test.ts tests/pipeline/build-steps.test.ts tests/pipeline/vol-07-spec.test.ts
```

Expected: PASS.

- [ ] **Step 7: Verificare la forma della migrazione**

Run:

```powershell
git diff --summary
rg -n "chapters/00-piano-editoriale" wiki docs src
```

Expected: 23 rename/move riconoscibili; nessun riferimento runtime o wiki al percorso legacy.

- [ ] **Step 8: Commit selettivo**

```powershell
git add wiki/books/moduli tests/editorial-layout.test.ts
git commit -m "refactor: move module plans out of reader chapters"
```

---

### Task 6: Correzioni visibili e indice canonico del VOL-07

**Files:**
- Create: `tests/vol-07-visible-copy.test.ts`
- Modify: `src/catalog/text-volumes.ts`
- Modify: `src/server/book/book-preview.ts`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`
- Modify: `wiki/books/moduli/m-sa01-sanita-amministrativa/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md`
- Modify: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/index.md`
- Modify: `wiki/books/moduli/m-sa01-sanita-amministrativa/planning/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/planning/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`
- Modify: `tests/pipeline/vol-07-spec.test.ts`
- Modify: `tests/book-preview.test.ts`

**Interfaces:**
- Produces: titoli dichiarati completi del VOL-07
- Produces: `outline_section: 3` per M-SA02/03
- Produces: formato visibile `CODICE — Titolo`

- [ ] **Step 1: Scrivere il test rosso dell'audit visibile**

```ts
it("keeps VOL-07 reader-visible copy accented and free of mojibake", async () => {
  const visibleFiles = [
    "wiki/books/moduli/m-sa01-sanita-amministrativa/index.md",
    "wiki/books/moduli/m-sa02-professioni-sanitarie/index.md",
    "wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md",
    "wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/index.md"
  ]
  const copy = (await Promise.all(visibleFiles.map((file) => readFile(file, "utf8")))).join("\n")

  expect(copy).not.toMatch(/\bSanita\b/)
  expect(copy).not.toMatch(/Ã|Â|�/)
  expect(copy).toContain("Sanità")
})
```

Aggiungere:

```ts
expect(parseFrontmatter(chapter03).data.outline_section).toBe(3)
expect(TEXT_VOLUME_CATALOG.find((volume) => volume.code === "VOL-07")).toMatchObject({
  title: "Sanità amministrativa e professioni sanitarie",
  shortTitle: "Sanità"
})
```

- [ ] **Step 2: Eseguire il test e verificare il fallimento**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/vol-07-visible-copy.test.ts
```

Expected: FAIL su `Sanita` e `outline_section`.

- [ ] **Step 3: Correggere catalogo e moduli**

Applicare nelle stringhe visibili:

```text
Sanita → Sanità
Priorita → Priorità
Qualita → Qualità
Responsabilita → Responsabilità
Contabilita → Contabilità
Accessibilita → Accessibilità
```

Non modificare slug, `module_family: sanita`, tag tecnici o nomi file.

- [ ] **Step 4: Aggiungere i titoli alla scheda VOL-07**

Usare:

```markdown
| # | Titolo | File | Matrice | Stato atteso | Note |
| 01 | Professioni sanitarie: profili, requisiti e prove | chapters/01-mappa-profili-e-prove.md | ... |
| 03 | Discipline professionali: autonomia, responsabilità e deontologia | chapters/03-discipline-professionali-autonomia-responsabilita.md | ... |
```

Per M-SA01:

```text
04 Atti, procedimenti e flussi informativi nelle aziende sanitarie
05 Documentazione sanitaria, accesso, privacy e conservazione
06 Front office e comunicazione con l'utenza
09 Contabilità, budget e controllo di gestione
10 Procurement sanitario, farmaci, dispositivi e magazzino
```

- [ ] **Step 5: Correggere il capitolo M-SA02/03**

Nel frontmatter aggiungere:

```yaml
outline_section: 3
```

Non inserire `03` nel titolo né nell'H1.

- [ ] **Step 6: Uniformare i separatori visibili generati**

In `book-preview.ts`:

```ts
title: `${input.moduleCode} — ${stripModuleCode(input.moduleTitle)}`
```

e:

```ts
title: `${volume.code} — ${volume.title}`
```

Aggiornare `stripModuleCode`:

```ts
return value.replace(/^M-[A-Z]{2}\d{2}\s*[-–—]\s*/i, "").trim()
```

- [ ] **Step 7: Aggiornare e lanciare i test**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/vol-07-visible-copy.test.ts tests/pipeline/vol-07-spec.test.ts tests/book-preview.test.ts tests/book-studio-display.test.ts
```

Expected: PASS.

- [ ] **Step 8: Sincronizzare la pipeline esclusivamente via CLI**

Run:

```powershell
npm run pipeline -- sync VOL-07 --json
npm run pipeline -- status VOL-07 --json
```

Expected: nessuno step `dropped`; i target capitolo restano invariati; lo step 10 M-SA01/04 resta il lavoro corrente.

- [ ] **Step 9: Commit selettivo**

```powershell
git add src/catalog/text-volumes.ts src/server/book/book-preview.ts wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md wiki/books/moduli/m-sa01-sanita-amministrativa wiki/books/moduli/m-sa02-professioni-sanitarie wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione tests/vol-07-visible-copy.test.ts tests/pipeline/vol-07-spec.test.ts tests/book-preview.test.ts
git commit -m "fix: normalize VOL-07 chapter list and titles"
```

---

### Task 7: Regole operative per staff e agenti

**Files:**
- Modify: `docs/PIPELINE.md`
- Modify: `wiki/AGENTS.md`
- Modify: `.agents/skills/pipeline-volume/SKILL.md`

**Interfaces:**
- Produces: contratto operativo unico per persone e agenti
- Consumes: percorsi e modello dati implementati nei task precedenti

- [ ] **Step 1: Prima di modificare la skill, caricare le istruzioni obbligatorie**

Leggere integralmente:

```text
C:/Users/info/.codex/plugins/cache/openai-curated-remote/superpowers/6.2.0/skills/writing-skills/SKILL.md
.agents/skills/pipeline-volume/SKILL.md
```

- [ ] **Step 2: Aggiornare `docs/PIPELINE.md`**

Aggiungere una sezione `Indice studente e piano staff` con le regole:

```markdown
- `chapters/` contiene soltanto contenuti destinati al lettore.
- `planning/` contiene piani, matrici, review e strumenti interni.
- La dashboard mostra i target dichiarati nel riquadro staff, non nell'anteprima.
- Un file assente può apparire nel piano staff, ma non nell'indice studente.
- Un capitolo entra nella pipeline tramite la scheda e avanza soltanto via CLI.
```

Correggere la frase sulla derivazione: la pipeline deriva soltanto veri file capitolo e ignora esplicitamente i piani legacy.

- [ ] **Step 3: Aggiornare `wiki/AGENTS.md`**

Nella sezione dei moduli specialistici aggiungere:

```markdown
- `chapters/` è reader-only: non contiene piani o artefatti interni.
- Il piano canonico del modulo è `planning/00-piano-editoriale.md`.
- Non creare o ripristinare `chapters/00-piano-editoriale.md`.
- Titolo e H1 non includono il numero; usare `outline_section`.
```

- [ ] **Step 4: Aggiornare la skill pipeline**

Nella fase di discovery e nelle precondizioni:

```markdown
Prima di derivare o dichiarare capitoli:
1. escludi ogni documento staff-only;
2. verifica che i piani siano sotto `planning/`;
3. usa il titolo dichiarato nella scheda per i target ancora assenti;
4. non presentare un piano come capitolo al writer o al revisore.
```

- [ ] **Step 5: Verificare la documentazione**

Run:

```powershell
rg -n "chapters/00-piano-editoriale|planning/00-piano-editoriale|reader-only|Piano editoriale staff" docs/PIPELINE.md wiki/AGENTS.md .agents/skills/pipeline-volume/SKILL.md
git diff --check -- docs/PIPELINE.md wiki/AGENTS.md .agents/skills/pipeline-volume/SKILL.md
```

Expected: il vecchio percorso appare solo come divieto esplicito; nessuna anomalia whitespace.

- [ ] **Step 6: Commit selettivo**

```powershell
git add docs/PIPELINE.md wiki/AGENTS.md .agents/skills/pipeline-volume/SKILL.md
git commit -m "docs: align staff on reader-only chapter folders"
```

---

### Task 8: Verifica integrata, dashboard live e ripresa della pipeline

**Files:**
- Modify only if gate evidence requires it: `wiki/reviews/pipeline/VOL-07/10-controllo-copertura-m-sa01-04.md`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`
- Append through LocalAgentMemory: `wiki/memory/agent/`

**Interfaces:**
- Consumes: tutti i task precedenti
- Produces: dashboard verificata, suite verde, pipeline senza blocker, step 10 concluso solo se il gate passa

- [ ] **Step 1: Eseguire i test mirati completi**

Run:

```powershell
.\node_modules\.bin\vitest.cmd run tests/editorial-document.test.ts tests/editorial-plan.test.ts tests/editorial-layout.test.ts tests/book-preview.test.ts tests/book-studio-display.test.ts tests/book-studio-state.test.ts tests/manual-writer-agent.test.ts tests/vol-07-visible-copy.test.ts tests/pipeline/volume-spec.test.ts tests/pipeline/build-steps.test.ts tests/pipeline/vol-07-spec.test.ts
```

Expected: PASS.

- [ ] **Step 2: Eseguire suite, typecheck e controllo diff**

Run:

```powershell
npm test
npm run typecheck
git diff --check
```

Expected: tutti i test PASS, typecheck senza errori, nessun whitespace error.

- [ ] **Step 3: Verificare il repository editoriale**

Run:

```powershell
Get-ChildItem wiki\books\moduli -Recurse -Filter 00-piano-editoriale.md -File |
  Group-Object { Split-Path $_.DirectoryName -Leaf }
rg -n "chapters/00-piano-editoriale" wiki docs src
```

Expected: tutti i 25 piani sotto cartelle `planning`; nessun uso operativo del percorso legacy.

- [ ] **Step 4: Verificare la pipeline con JSON**

Run:

```powershell
npm run pipeline -- doctor --json
npm run pipeline -- status VOL-07 --json
npm run pipeline -- gate VOL-07 --step 10 --module M-SA01 --chapter 04 --json
```

Expected: doctor verde; nessun blocker estraneo; gate 10 `passed: true`.

- [ ] **Step 5: Chiudere lo step 10 solo se il gate è verde**

Run:

```powershell
npm run pipeline -- complete VOL-07 --step 10 --module M-SA01 --chapter 04 --json
npm run pipeline -- status VOL-07 --json
```

Expected: step 10 `done`; il prossimo step è 11 sullo stesso capitolo. Se il gate non passa, correggere soltanto le lacune indicate e ripetere `gate`; non usare `--accept`.

- [ ] **Step 6: Verificare l'API live**

Run:

```powershell
curl.exe -s "http://127.0.0.1:3000/api/book-studio?bookId=volumi%2Fvol-07"
```

Controllare nel JSON:

```text
chapters: nessun path /chapters/00-piano-editoriale.md
M-SA02/03: outlineSection "3"
editorialPlan M-SA01: target 04,05,06,09,10
editorialPlan M-SA02: target 01,03
editorialPlan M-SA03/M-SA04: targets []
```

- [ ] **Step 7: Aprire e controllare la dashboard**

Run:

```powershell
Start-Process "http://127.0.0.1:3000/?bookId=volumi%2Fvol-07#studio"
```

Verificare:

1. indice studente senza piani interni;
2. titoli accentati;
3. capitolo M-SA02/03 numerato;
4. pannello `Piano editoriale staff` separato;
5. target pianificati non cliccabili e assenti dalla preview libro;
6. aggiornamento live dopo refresh.

- [ ] **Step 8: Registrare la memoria locale**

Richiamare e poi catturare tramite `LocalAgentMemory`:

```text
scope: pipeline-volume/standard-indice-studente-staff
decisione: chapters reader-only, planning staff-only, dashboard a due livelli
risultato: 25 piani canonici, VOL-07 corretto, step 10 verificato
```

- [ ] **Step 9: Applicare la verification-before-completion**

Leggere integralmente:

```text
C:/Users/info/.codex/plugins/cache/openai-curated-remote/superpowers/6.2.0/skills/verification-before-completion/SKILL.md
```

Controllare gli output effettivi dell'ultima esecuzione, non risultati precedenti.

- [ ] **Step 10: Commit finale isolato se restano solo evidenze**

```powershell
git add pipeline/VOL-07/run-state.json wiki/reviews/pipeline/VOL-07 wiki/memory/agent
git commit -m "chore: verify editorial list standard and advance VOL-07"
```

Non includere file preesistenti non pertinenti. Non eseguire push.

---

## Self-review

### Spec coverage

- Indice studente reader-only: Task 2.
- Piano staff separato: Task 3 e Task 4.
- Stato da scheda/run-state: Task 1 e Task 3.
- Nessun capitolo inventato: Task 1 e Task 3.
- Migrazione globale dei 25 moduli: Task 5.
- Protezione pipeline e Manual Writer: Task 2.
- Accenti, punteggiatura e numero M-SA02/03: Task 6.
- Allineamento staff e agenti: Task 7.
- Dashboard live e ripresa step 10: Task 8.

### Placeholder scan

Ogni attività contiene file, interfacce, codice, comando di verifica e risultato atteso.

### Type consistency

- `VolumeSpecChapter.title` è prodotto nel Task 1 e consumato nel Task 3.
- `BookStudioEditorialPlan` è prodotto nel Task 3 e consumato nel Task 4.
- `isStaffOnlyBookDocument()` è prodotto nel Task 2 e consumato da Book Studio e Manual Writer.
- Gli stati del Task 3 coincidono con le etichette del Task 4.
