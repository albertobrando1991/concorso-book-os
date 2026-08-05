# VOL-07 Progressive Writing Start Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Abilitare la fase C per il solo primo capitolo di M-SA02, sincronizzare il run-state tramite CLI ed eseguire gli step 08 e 09 fino a ottenere il primo capitolo editoriale valido.

**Architecture:** La scheda di volume dichiara esplicitamente un solo capitolo M-SA02 e abilita C soltanto per quel modulo. `pipeline sync` riproietta il piano preservando per chiave i 17 step A-B già conclusi e aggiunge il ciclo 08-12; il CLI resta l'unico writer del run-state.

**Tech Stack:** Markdown wiki, TypeScript, CLI `tsx`, Vitest, pipeline editoriale ConcorsoBook OS, LocalAgentMemory.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-07/run-state.json`.
- Non abilitare ancora le fasi D-F.
- Non dichiarare capitoli successivi durante questo ciclo.
- Il capitolo deve restare non esecutivo quando servono setting, protocollo locale o review specialistica.
- Usare `apply_patch` per ogni modifica a file testuali.
- Conservare tutte le modifiche preesistenti del worktree condiviso.
- Non creare commit intermedi: la pipeline riserva commit e pubblicazione allo step 23 e il worktree contiene modifiche condivise non isolate.

---

### Task 1: Dichiarare il primo capitolo e abilitare la fase C

**Files:**
- Modify: `tests/pipeline/vol-07-spec.test.ts`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`

**Interfaces:**
- Consumes: `loadVolumeSpec({ wikiRoot, volumeCode })`.
- Produces: specifica VOL-07 valida con `phases: ["A", "B", "C"]`, M-SA02 in A/B/C, gli altri moduli in A/B e un capitolo dichiarato per M-SA02.

- [ ] **Step 1: Aggiornare il test della specifica prima della scheda**

Sostituire le attese di `tests/pipeline/vol-07-spec.test.ts` con:

```ts
expect(loaded.spec).toMatchObject({
  volumeCode: "VOL-07",
  volumeTitle: "Sanità amministrativa e professioni sanitarie",
  cutOffDate: "2026-07-28",
  responsabileNormativo: "Alberto Brando",
  responsabileEditoriale: "Alberto Brando",
  writerProvider: "codex",
  phases: ["A", "B", "C"]
})
expect(loaded.spec.modules.map((module) => [module.code, module.priority, module.phases])).toEqual([
  ["M-SA02", 1, ["A", "B", "C"]],
  ["M-SA01", 2, ["A", "B"]],
  ["M-SA03", 3, ["A", "B"]],
  ["M-SA04", 4, ["A", "B"]]
])
expect(loaded.spec.modules[0]).toMatchObject({
  chaptersSource: "declared",
  chapters: [
    {
      number: "01",
      file: "chapters/01-mappa-profili-e-prove.md",
      matrix: "planning/02-matrice-copertura-didattica.md",
      expectedStatus: "completo"
    }
  ]
})
expect(loaded.spec.modules.slice(1).every((module) => module.chaptersSource === "derived")).toBe(true)
```

- [ ] **Step 2: Eseguire il test e confermare il fallimento**

Run:

```powershell
npx vitest run tests\pipeline\vol-07-spec.test.ts
```

Expected: FAIL perché la scheda reale dichiara ancora soltanto A/B e nessuna tabella capitoli.

- [ ] **Step 3: Aggiornare la scheda con la modifica minima**

Applicare:

```yaml
phases: [A, B, C]
```

e nella tabella moduli:

```markdown
| M-SA02 | moduli/m-sa02-professioni-sanitarie | 1 | A,B,C |
```

Lasciare gli altri moduli in `A,B`, quindi aggiungere:

```markdown
## Capitoli M-SA02

| # | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- |
| 01 | chapters/01-mappa-profili-e-prove.md | planning/02-matrice-copertura-didattica.md | completo | Primo ciclo progressivo della fase C |
```

Aggiornare la nota introduttiva per dichiarare che C è aperta progressivamente sul primo capitolo M-SA02.

- [ ] **Step 4: Eseguire i test della specifica e della costruzione step**

Run:

```powershell
npx vitest run tests\pipeline\vol-07-spec.test.ts tests\pipeline\volume-spec.test.ts tests\pipeline\build-steps.test.ts
```

Expected: tutti i test passano.

- [ ] **Step 5: Verificare il diff del task**

Run:

```powershell
git diff --check -- tests/pipeline/vol-07-spec.test.ts wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md
```

Expected: exit code 0, nessun errore di whitespace.

---

### Task 2: Sincronizzare il run-state tramite CLI

**Files:**
- Modified by CLI: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: specifica VOL-07 validata dal Task 1.
- Produces: cinque step nuovi con chiavi `08`-`12` per `moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md`.

- [ ] **Step 1: Eseguire sync strutturato**

Run:

```powershell
npm run pipeline -- sync VOL-07 --json
```

Expected:

```json
{
  "ok": true,
  "command": "sync",
  "added": [
    "08:moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md",
    "09:moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md",
    "10:moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md",
    "11:moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md",
    "12:moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md"
  ],
  "dropped": []
}
```

- [ ] **Step 2: Verificare lo stato**

Run:

```powershell
npm run pipeline -- status VOL-07 --json
```

Expected: `done: 17`, `pending: 5`, nessun blocker e step 08 come `next`.

- [ ] **Step 3: Interrompere in caso di proiezione diversa**

Se `added` non contiene esattamente le cinque chiavi previste o `dropped` non è vuoto, non eseguire `next`. Confrontare la scheda caricata e il run-state con:

```powershell
npx vitest run tests\pipeline\vol-07-spec.test.ts tests\pipeline\run-state.test.ts
npm run pipeline -- status VOL-07 --json
```

Correggere la scheda e ripetere `sync`; non editare il JSON.

---

### Task 2A: Assegnare un nucleo di matrice al capitolo 01

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`

**Interfaces:**
- Consumes: corpus bandi M-SA02, D.P.R. 220/2001 e ordinamento delle professioni sanitarie.
- Produces: una riga `completo` collocata in `cap. 01`, leggibile dal gate di copertura.

- [ ] **Step 1: Aggiungere il nucleo mancante**

Inserire la riga `Mappa della famiglia concorsuale e delle prove` con teoria, applicazione, output e verifica; aggiornare il totale da 8 a 9 nuclei.

- [ ] **Step 2: Rivalidare il gate di modulo**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 07 --module M-SA02 --json
```

Expected: `passed: true`, zero blocker e zero warning.

- [ ] **Step 3: Verificare l'assegnazione del capitolo**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 10 --module M-SA02 --chapter 01 --json
```

Expected: il gate trova la riga del capitolo 01 e passa; lo step 10 resta `pending` perché il comando `gate` non cambia lo stato.

---

### Task 3: Eseguire lo step 08 e approvare il piano del capitolo

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa02-01.md`
- Modified by CLI: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: Bibbia VOL-07, matrice M-SA02, source note collegate e prompt renderizzato dello step 08.
- Produces: piano H1/H2/H3 riga-per-riga collegato ai nuclei del capitolo 01.

- [ ] **Step 1: Aprire lo step 08**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step 08, modulo M-SA02, capitolo 01, gate `chapter-plan`.

- [ ] **Step 2: Scrivere il piano operativo senza creare il capitolo**

Creare `wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa02-01.md` con:

- frontmatter `type: review`, `status: complete`, riferimenti a Bibbia, matrice e fonti;
- nuclei assegnati al capitolo 01;
- tabella `nucleo | fonte | sezione | applicazione | verifica | review`;
- struttura proposta con un H1 e gerarchia H2/H3;
- budget orientativo KDP;
- duplicazioni vietate rispetto al VOL-01;
- casi, domande ed esercizi;
- review umane differite allo step 15.

- [ ] **Step 3: Verificare manualmente il piano**

Controllare che ogni nucleo collocato in `cap. 01` nella matrice abbia una sezione, una fonte, un'applicazione e una verifica. Controllare inoltre che il piano non modifichi `chapters/01-mappa-profili-e-prove.md`.

- [ ] **Step 4: Chiudere il gate non automatizzato con nota verificabile**

Run:

```powershell
npm run pipeline -- complete VOL-07 --step 08 --module M-SA02 --chapter 01 --accept --note "Piano operativo salvato in wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa02-01.md; nuclei del cap. 01 collegati riga per riga a matrice, fonti, applicazioni, verifiche, struttura H1-H3, budget KDP e review step 15; il capitolo non è stato ancora creato." --json
```

Expected: `ok: true`, step 08 `done`, step 09 come `next`.

---

### Task 4: Scrivere e validare il primo capitolo allo step 09

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md`
- Modified by CLI: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: piano step 08, matrice M-SA02, Bibbia VOL-07, corpus bandi M-SA02 e source note professionali consolidate.
- Produces: capitolo editoriale con un solo H1, frontmatter tracciabile e `draft_stage: editorial-draft`.

- [ ] **Step 1: Aprire lo step 09 e leggere il prompt renderizzato**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step 09 sul file dichiarato e gate `chapter-lint`.

- [ ] **Step 2: Applicare la skill professionale di scrittura**

Leggere integralmente `.agents/skills/concorso-book-professional-writer/SKILL.md` e usare le sue regole insieme al prompt 09.

- [ ] **Step 3: Creare il capitolo completo**

Il file deve contenere:

- frontmatter con `source_refs`, `book_refs`, `draft_stage: editorial-draft`, `review_required: true`, `last_compiled_from` e date veritiere;
- un solo H1;
- apertura, obiettivo e Mappa BANDO;
- teoria progressiva sui profili e sulle forme di prova assegnate al capitolo;
- box “Da sapere in 5 righe”;
- caso guidato non esecutivo;
- domanda da commissario, domanda-trappola ed errore tipico;
- mini-esercizio o checklist;
- riferimenti consolidati e note di review;
- nessun segnaposto, meta-commento, soglia inventata o rinvio generico.

- [ ] **Step 4: Eseguire il gate senza chiudere**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 09 --module M-SA02 --chapter 01 --json
```

Expected: `passed: true`, zero blocker. Correggere il capitolo e ripetere lo stesso comando se il gate fallisce.

- [ ] **Step 5: Chiudere lo step 09**

Run:

```powershell
npm run pipeline -- complete VOL-07 --step 09 --module M-SA02 --chapter 01 --json
```

Expected: `ok: true`, step 09 `done`, step 10 come `next`.

---

### Task 5: Verifica finale e memoria

**Files:**
- Modify through `LocalAgentMemory`: memoria locale pertinente in `wiki/memory/agent/`

**Interfaces:**
- Consumes: modifiche dei Task 1-4.
- Produces: evidenza che pipeline, test, typecheck, diff e memoria sono coerenti.

- [ ] **Step 1: Eseguire i test mirati**

Run:

```powershell
npx vitest run tests\pipeline\vol-07-spec.test.ts tests\pipeline\volume-spec.test.ts tests\pipeline\build-steps.test.ts tests\pipeline\gates.test.ts tests\didactic-coverage.test.ts
```

Expected: tutti i test passano.

- [ ] **Step 2: Eseguire il typecheck**

Run:

```powershell
npm run typecheck
```

Expected: exit code 0.

- [ ] **Step 3: Controllare diff e stato pipeline**

Run:

```powershell
git diff --check
npm run pipeline -- status VOL-07 --json
```

Expected: nessun errore di whitespace; step A-B e 08-09 `done`; step 10 `pending`; nessun blocker.

- [ ] **Step 4: Registrare la traccia con LocalAgentMemory**

Usare l'interfaccia `LocalAgentMemory` già adottata dalla repo per registrare:

- chiusura dei quattro gate 05-07;
- apertura progressiva della fase C su M-SA02 capitolo 01;
- percorso del piano step 08;
- percorso del capitolo step 09;
- esito dei gate e verifiche;
- decisione di non abilitare ancora D-F.

- [ ] **Step 5: Rileggere la memoria e verificare la continuità**

Richiamare la traccia appena salvata tramite `LocalAgentMemory` e controllare che contenga target, decisione e prossimo step 10 senza usare la memoria come fonte normativa.
