# VOL-07 Publishable Through Step 23 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Portare VOL-07 dal completamento dello step 20 a un candidato di pubblicazione completo e riproducibile, chiudendo gli step 21, 22 e 23 e lasciando lo step umano 24 pendente.

**Architecture:** Il CLI resta l'unica autorita per ordine, stato e gate. Lo step 21 produce il report editoriale fisso richiesto dal gate `review-report`; lo step 22 produce un preflight documentato e un PDF KDP verificabile; lo step 23 assembla un pacchetto di consegna con manifest, changelog, limiti e istruzioni di riproduzione. I gate non implementati `preflight` e `delivery` vengono prima tentati normalmente e solo dopo l'esito JSON `gate-not-implemented` chiusi con `--accept --note` basato su evidenze reali.

**Tech Stack:** ConcorsoBook OS pipeline CLI, Markdown, TypeScript/Vitest, Next.js, Playwright/Chromium PDF, Python/PyPDF, Git, LocalAgentMemory.

## Global Constraints

- Non modificare mai a mano `pipeline/VOL-07/run-state.json`.
- Preservare tutte le modifiche preesistenti del worktree e usare staging selettivo.
- Leggere integralmente il prompt renderizzato da `next` prima di ogni step.
- Non chiudere uno step con blocker; fermarsi e correggere la causa.
- Non usare `--accept` prima di avere osservato `gate-not-implemented` in JSON e completato la verifica manuale.
- Lo step 24 resta pendente: nessuna dichiarazione di approvazione umana o pubblicazione autorizzata.
- Il candidato KDP mantiene 6.69 x 9.61 pollici, no bleed, margini speculari 23/13 mm, 18 mm sopra/sotto e 394 pagine salvo variazione giustificata del DOM.
- Il report editoriale usa senza variazioni le dieci sezioni del template `revisore-editoriale-totale` e applica tutti i 30 controlli più il gate di copertura v4.

---

### Task 1: Eseguire lo step 21 e ottenere il giudizio pubblicabile

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/21-vol-07.md`
- Read: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`
- Read: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/*.md`
- Read: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/*.md`
- Read: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/*.md`
- Read: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/*.md`
- Read: `wiki/reviews/pipeline/VOL-07/15-*.md`
- Read: `wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md`

**Interfaces:**
- Consumes: volume congelato, matrici v4, audit specialistici, impaginazione finale e report step 20.
- Produces: report con tabella `ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato` e giudizio esatto `Pubblicabile con correzioni minori`.

- [ ] **Step 1: Prendere in carico lo step 21 e leggere il prompt canonico**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
Get-Content -Raw artifacts/pipeline/VOL-07/21/vol-07/prompt.md
```

Expected: step `21:VOL-07` in progress, gate `review-report`, report richiesto in `wiki/reviews/pipeline/VOL-07/21-vol-07.md`.

- [ ] **Step 2: Costruire l'evidenza editoriale completa**

Leggere indice, 25 capitoli, quattro matrici e report 15/20. Verificare meccanicamente gerarchie, promesse, rinvii, `source_refs`, cut-off, caratteri corrotti, duplicazioni e corrispondenza indice/file; confrontare i risultati con le evidenze visive delle 394 pagine.

- [ ] **Step 3: Scrivere il report fisso**

Creare tutte e sole le sezioni 1-10 del template. La tabella deve contenere almeno una riga verificabile anche in assenza di errori aperti, per esempio una voce di controllo chiusa:

```markdown
| C01 | Intero volume | Copertura didattica integrale | Lieve | Controllo conclusivo su matrici e rinvii. | Nessuna modifica: evidenza conforme. | Chiuso |
```

Il giudizio può essere `Pubblicabile con correzioni minori` soltanto se non restano errori gravi o medi da correggere.

- [ ] **Step 4: Eseguire il gate automatico**

Run:

```powershell
npm run pipeline -- complete VOL-07 --step 21 --json
```

Expected: `ok: true`, nessun `open-severe-error`, nessun `deferred-to-human`, next `22:VOL-07`.

- [ ] **Step 5: Commit circoscritto del report**

```powershell
git add wiki/reviews/pipeline/VOL-07/21-vol-07.md
git diff --cached --check
git commit -m "docs(vol-07): record final editorial review"
```

### Task 2: Eseguire lo step 22 e produrre il preflight tecnico

**Files:**
- Create: `scripts/export-book-studio-volume-pdf.mjs`
- Create: `scripts/book-studio-pdf-export-core.mjs`
- Create: `scripts/book-studio-pdf-export-core.d.mts`
- Create: `tests/book-studio-pdf-export-core.test.ts`
- Create: `wiki/reviews/pipeline/VOL-07/22-vol-07-preflight.md`
- Generate: `delivery/VOL-07/candidate/vol-07-interior-kdp.pdf`

**Interfaces:**
- Produces: export PDF riproducibile da `BOOK_STUDIO_URL`, `BOOK_STUDIO_BOOK_ID` e `BOOK_STUDIO_PDF_OUTPUT`; verifica attesa di 394 pagine e master 6.69 x 9.61 pollici.
- Consumed by: Task 3 manifest e pacchetto.

- [ ] **Step 1: Prendere in carico lo step 22 e leggere il prompt canonico**

```powershell
npm run pipeline -- next VOL-07 --json
Get-Content -Raw artifacts/pipeline/VOL-07/22/vol-07/prompt.md
```

- [ ] **Step 2: Testare il contratto dell'export PDF**

Scrivere test Vitest per opzioni obbligatorie, dimensioni pagina e conteggio atteso. Run:

```powershell
npm test -- tests/book-studio-pdf-export-core.test.ts
```

Expected red: modulo mancante; dopo l'implementazione, green.

- [ ] **Step 3: Implementare ed eseguire l'export**

Il browser deve attendere paginazione stabile e font, isolare `.bookPages`, applicare `break-after: page` a ogni `.bookPage`, usare `printBackground: true`, `preferCSSPageSize: true`, `width: "6.69in"`, `height: "9.61in"`, margini PDF zero e scrivere solo il file dichiarato.

Avviare Book Studio su porta dedicata e generare:

```powershell
$env:BOOK_STUDIO_URL='http://127.0.0.1:3010'
$env:BOOK_STUDIO_BOOK_ID='volumi/vol-07'
$env:BOOK_STUDIO_EXPECTED_PAGE_COUNT='394'
$env:BOOK_STUDIO_PDF_OUTPUT='delivery/VOL-07/candidate/vol-07-interior-kdp.pdf'
node scripts/export-book-studio-volume-pdf.mjs
```

- [ ] **Step 4: Eseguire tutti i controlli di preflight**

Run almeno:

```powershell
npm run audit:coverage
npm run typecheck
npm test
npm run build
git diff --check
```

Usare PyPDF per verificare 394 pagine, media box 6.69 x 9.61 pollici, assenza di pagine con dimensione diversa e presenza di risorse font. Verificare inoltre link wiki, `source_refs`, frontmatter, asset mancanti, immagini duplicate, tabelle anomale, caratteri corrotti e file dichiarati mancanti. Registrare per ogni riga pass/fail, comando, conteggio ed evidenza in `22-vol-07-preflight.md`. Se KDP Previewer non è installato, dichiararlo come limite non eseguito senza inventare un esito.

- [ ] **Step 5: Tentare il gate normale e poi accettarlo solo se non implementato**

```powershell
npm run pipeline -- complete VOL-07 --step 22 --json
npm run pipeline -- complete VOL-07 --step 22 --accept --note "Preflight VOL-07 conforme: copertura, link, frontmatter, asset, typecheck, test, build e PDF KDP verificati; 394 pagine 6.69 x 9.61 in, no bleed, font presenti; report step 22 registrato." --json
```

Il secondo comando si esegue soltanto dopo il blocker JSON `gate-not-implemented` per `preflight`.

- [ ] **Step 6: Commit circoscritto di export, test e preflight**

```powershell
git add scripts/export-book-studio-volume-pdf.mjs scripts/book-studio-pdf-export-core.mjs scripts/book-studio-pdf-export-core.d.mts tests/book-studio-pdf-export-core.test.ts wiki/reviews/pipeline/VOL-07/22-vol-07-preflight.md
git diff --cached --check
git commit -m "feat(vol-07): add reproducible KDP preflight"
```

### Task 3: Eseguire lo step 23 e assemblare il candidato di consegna

**Files:**
- Create: `delivery/VOL-07/candidate/README.md`
- Create: `delivery/VOL-07/candidate/manifest.sha256`
- Create: `delivery/VOL-07/candidate/CHANGELOG.md`
- Create: `delivery/VOL-07/candidate/LIMITS.md`
- Create: `wiki/reviews/pipeline/VOL-07/23-vol-07-delivery.md`
- Include: `delivery/VOL-07/candidate/vol-07-interior-kdp.pdf`

**Interfaces:**
- Consumes: report 21, preflight 22, PDF verificato e stato CLI.
- Produces: candidato autosufficiente con checksum, versione, cut-off, riproduzione, limiti e manutenzione futura.

- [ ] **Step 1: Prendere in carico lo step 23 e leggere il prompt canonico**

```powershell
npm run pipeline -- next VOL-07 --json
Get-Content -Raw artifacts/pipeline/VOL-07/23/vol-07/prompt.md
```

- [ ] **Step 2: Verificare stato Git senza incorporare lavoro estraneo**

```powershell
git status --short
git diff --cached --check
```

Il manifest include soltanto i file del candidato; non include cache, log, `artifacts/pipeline`, memoria condivisa o modifiche editoriali estranee già presenti nel worktree.

- [ ] **Step 3: Assemblare e documentare il pacchetto**

`README.md` registra versione `VOL-07-candidate-2026-08-05`, stato `pronto per step 24`, istruzione di rigenerazione PDF e riferimenti ai report 21/22. `CHANGELOG.md` riassume gli step 17-23. `LIMITS.md` dichiara cut-off normativo, mancata esecuzione eventuale del KDP Previewer e ciclo di manutenzione. `manifest.sha256` contiene SHA-256 e dimensione di ogni file del candidato, escluso il manifest stesso.

- [ ] **Step 4: Ripetere le verifiche finali sul pacchetto**

Ricalcolare i checksum, rileggere il PDF con PyPDF, rieseguire typecheck/test pertinenti e verificare che `git diff --cached` contenga soltanto i file autorizzati.

- [ ] **Step 5: Tentare il gate normale e poi accettarlo solo se non implementato**

```powershell
npm run pipeline -- complete VOL-07 --step 23 --json
npm run pipeline -- complete VOL-07 --step 23 --accept --note "Candidato VOL-07 completo e riproducibile: PDF KDP verificato, report 21/22, manifest SHA-256, changelog, limiti e istruzioni presenti; nessun file estraneo incluso; pronto esclusivamente per il sign-off umano dello step 24." --json
```

Il secondo comando si esegue soltanto dopo il blocker JSON `gate-not-implemented` per `delivery`.

- [ ] **Step 6: Commit del pacchetto e conferma dello stop umano**

```powershell
git add delivery/VOL-07/candidate wiki/reviews/pipeline/VOL-07/23-vol-07-delivery.md
git diff --cached --check
git commit -m "chore(vol-07): prepare publication candidate"
npm run pipeline -- status VOL-07 --json
```

Expected: `done: 168`, `pending: 1`, next `24:VOL-07` con gate `human-signoff`. Non eseguire `next` o `complete` sullo step 24.

### Task 4: Memoria e handoff verso VOL-02

**Files:**
- Modify only through `LocalAgentMemory`: `wiki/memory/agent/`

**Interfaces:**
- Produces: traccia finale VOL-07 e punto di ripartenza VOL-02.

- [ ] **Step 1: Registrare la traccia locale**

Usare `LocalAgentMemory.captureConversation()` con scope `VOL-07`, route `pipeline-steps-21-23`, conteggi finali, commit, report, PDF, checksum, limiti e next step 24.

- [ ] **Step 2: Confermare VOL-02 senza prenderne ancora in carico uno step**

```powershell
npm run pipeline -- status VOL-02 --json
```

Expected: prossimo step canonico riportato dal CLI; il passaggio operativo a VOL-02 avviene dopo la consegna del riepilogo VOL-07.
