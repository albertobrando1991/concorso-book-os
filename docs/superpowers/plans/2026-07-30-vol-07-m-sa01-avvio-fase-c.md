# VOL-07 M-SA01 Avvio Fase C Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Abilitare nella pipeline i cinque capitoli M-SA01 già coperti dalla matrice, correggere lo stato mostrato dalla dashboard e completare gli step 08-09 del primo capitolo.

**Architecture:** La scheda VOL-07 resta la fonte dichiarativa dei target e `pipeline sync` è l'unico writer del run-state. La dashboard continua a leggere indice e capitoli canonici; la fase C viene aggiunta a M-SA01 senza alterare gli step già conclusi. I cinque target sono attivati insieme, ma il CLI impone l'esecuzione progressiva iniziando dal capitolo 04.

**Tech Stack:** Markdown, TypeScript, Vitest, CLI editoriale ConcorsoBook OS, LocalAgentMemory.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-07/run-state.json`.
- Non creare capitoli fuori dalle destinazioni 04, 05, 06, 09 e 10 fissate dalla matrice.
- Non dichiarare scritto o pubblicabile un capitolo prima del relativo gate.
- Lo step 08 può essere chiuso con `--accept --note` soltanto dopo verifica manuale del piano.
- Il capitolo 04 deve rispettare il contratto dello studente e non dipendere nel corpo da wiki, source note o report.
- Le review normative, privacy, contabili e procurement dello step 15 restano obbligatorie.
- Non effettuare commit o push senza autorizzazione esplicita.
- Preservare tutte le modifiche non pertinenti già presenti nella worktree.

---

### Task 1: Test della scheda M-SA01 in fase C

**Files:**

- Modify: `tests/pipeline/vol-07-spec.test.ts`
- Read: `src/pipeline/spec/load-volume-spec.ts`
- Read: `src/pipeline/steps/build-steps.ts`

**Interfaces:**

- Consumes: `loadVolumeSpec({ wikiRoot, volumeCode })` e `buildStepDrafts(spec, ["C"])`.
- Produces: regressione che vincola modulo, ordine dei capitoli e 25 step 08-12 M-SA01.

- [ ] **Step 1: Estendere l'aspettativa sui moduli**

Sostituire l'aspettativa M-SA01 da:

```ts
["M-SA01", 2, ["A", "B"]]
```

a:

```ts
["M-SA01", 2, ["A", "B", "C"]]
```

- [ ] **Step 2: Aggiungere l'aspettativa sui cinque capitoli**

Aggiungere dopo il controllo M-SA02:

```ts
const msa01 = loaded.spec.modules.find((module) => module.code === "M-SA01")

expect(msa01).toMatchObject({
  chaptersSource: "declared",
  chapters: [
    {
      number: "04",
      file: "chapters/04-atti-procedimenti-flussi-informativi.md",
      matrix: "planning/02-matrice-copertura-didattica.md",
      expectedStatus: "completo"
    },
    {
      number: "05",
      file: "chapters/05-documentazione-accesso-conservazione.md",
      matrix: "planning/02-matrice-copertura-didattica.md",
      expectedStatus: "completo"
    },
    {
      number: "06",
      file: "chapters/06-front-office-comunicazione-utenza.md",
      matrix: "planning/02-matrice-copertura-didattica.md",
      expectedStatus: "completo"
    },
    {
      number: "09",
      file: "chapters/09-contabilita-budget-controllo-gestione.md",
      matrix: "planning/02-matrice-copertura-didattica.md",
      expectedStatus: "completo"
    },
    {
      number: "10",
      file: "chapters/10-procurement-farmaci-dispositivi-magazzino.md",
      matrix: "planning/02-matrice-copertura-didattica.md",
      expectedStatus: "completo"
    }
  ]
})
```

- [ ] **Step 3: Vincolare l'ordine degli step**

Aggiungere:

```ts
const msa01Steps = buildStepDrafts(loaded.spec, ["C"]).filter((step) =>
  step.target.startsWith("moduli/m-sa01-sanita-amministrativa/chapters/")
)

expect(msa01Steps).toHaveLength(25)
expect(msa01Steps[0]?.key).toBe(
  "08:moduli/m-sa01-sanita-amministrativa/chapters/04-atti-procedimenti-flussi-informativi.md"
)
expect(msa01Steps.at(-1)?.key).toBe(
  "12:moduli/m-sa01-sanita-amministrativa/chapters/10-procurement-farmaci-dispositivi-magazzino.md"
)
```

- [ ] **Step 4: Eseguire il test e osservare il fallimento**

Run:

```text
npx vitest run tests/pipeline/vol-07-spec.test.ts
```

Expected: FAIL perché la scheda corrente assegna M-SA01 alle sole fasi A-B e non dichiara capitoli.

---

### Task 2: Abilitazione dichiarativa dei cinque capitoli

**Files:**

- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`
- Test: `tests/pipeline/vol-07-spec.test.ts`

**Interfaces:**

- Consumes: formato tabellare già usato dalla sezione `## Capitoli M-SA02`.
- Produces: M-SA01 con fasi `A,B,C` e cinque target dichiarati nell'ordine canonico.

- [ ] **Step 1: Abilitare la fase C del modulo**

Nella tabella moduli impostare:

```markdown
| M-SA01 | moduli/m-sa01-sanita-amministrativa | 2 | A,B,C |
```

- [ ] **Step 2: Aggiungere la tabella capitoli M-SA01**

Inserire dopo la sezione M-SA02:

```markdown
## Capitoli M-SA01

| # | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- |
| 04 | chapters/04-atti-procedimenti-flussi-informativi.md | planning/02-matrice-copertura-didattica.md | completo | Atti e procedimenti aziendali; flussi informativi sanitari |
| 05 | chapters/05-documentazione-accesso-conservazione.md | planning/02-matrice-copertura-didattica.md | completo | Documentazione sanitaria, accesso, privacy, FSE, dossier e conservazione |
| 06 | chapters/06-front-office-comunicazione-utenza.md | planning/02-matrice-copertura-didattica.md | completo | Front-office, comunicazione, reclami, accessibilità e riservatezza |
| 09 | chapters/09-contabilita-budget-controllo-gestione.md | planning/02-matrice-copertura-didattica.md | completo | Contabilità economico-patrimoniale, budget e controllo di gestione |
| 10 | chapters/10-procurement-farmaci-dispositivi-magazzino.md | planning/02-matrice-copertura-didattica.md | completo | Procurement sanitario, farmaci, dispositivi, magazzino e ciclo passivo |
```

- [ ] **Step 3: Aggiornare la nota di avanzamento**

Dichiarare che M-SA01 procede progressivamente dal capitolo 04 e che le review dello step 15 restano obbligatorie. Non dichiarare alcun capitolo M-SA01 già scritto.

- [ ] **Step 4: Eseguire il test mirato**

Run:

```text
npx vitest run tests/pipeline/vol-07-spec.test.ts tests/pipeline/build-steps.test.ts
```

Expected: PASS.

---

### Task 3: Correzione dello stato canonico letto dalla dashboard

**Files:**

- Modify: `wiki/books/moduli/m-sa01-sanita-amministrativa/index.md`
- Modify: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/00-piano-editoriale.md`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`

**Interfaces:**

- Consumes: esito già registrato dello step 07 e matrice con 8 nuclei `completo`.
- Produces: stato `ready-for-writing` coerente, senza falsa dichiarazione di capitoli completati.

- [ ] **Step 1: Aggiornare il frontmatter dell'indice M-SA01**

Impostare `draft_stage: ready-for-writing`, `module_status: writing-ready` e `updated_at` alla data corrente. Conservare `review_required: true`.

- [ ] **Step 2: Aggiornare l'elenco dei capitoli**

Nell'indice aggiungere i cinque rinvii ai target dichiarati, specificando che sono target della fase C e non capitoli già completati.

- [ ] **Step 3: Correggere il prossimo passo**

Sostituire il rinvio allo step 07 con:

```markdown
Lo step 07 è superato: 8 nuclei su 8 dispongono di fonti, teoria, applicazione, output e verifica. La fase C è autorizzata e inizia con lo step 08 del capitolo 04; nessun capitolo M-SA01 è ancora congelato o pubblicabile.
```

- [ ] **Step 4: Correggere il piano editoriale**

Impostare `draft_stage: ready-for-writing` e sostituire “Non avviato” con un testo che riporti: step 07 superato, cinque target autorizzati, primo target capitolo 04, review step 15 aperte.

- [ ] **Step 5: Correggere lo stato sintetico del volume**

Rimuovere dall'indice VOL-07 il vecchio blocker sugli 8 nuclei M-SA02 e descrivere: M-SA02 con due capitoli redatti; M-SA01 pronto alla fase C; M-SA03 e M-SA04 fermi dopo la preparazione.

- [ ] **Step 6: Verificare l'assenza della frase obsoleta**

Run:

```text
rg -n "Non avviato|scrittura inizierà dopo il gate.*step 07|8 nuclei parziali" wiki/books/moduli/m-sa01-sanita-amministrativa wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md
```

Expected: nessuna corrispondenza.

---

### Task 4: Sincronizzazione CLI controllata

**Files:**

- CLI-managed: `pipeline/VOL-07/run-state.json`
- Read: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`

**Interfaces:**

- Consumes: nuova scheda validata.
- Produces: 25 nuovi step M-SA01 pending, senza rimozioni o alterazioni degli step conclusi.

- [ ] **Step 1: Salvare l'elenco delle chiavi concluse**

Leggere il run-state e registrare in output il numero di step `done` prima della sincronizzazione. Expected: `27`.

- [ ] **Step 2: Eseguire la sincronizzazione**

Run:

```text
npm run pipeline -- sync VOL-07 --json
```

Expected:

- `ok: true`;
- `specChanged: true`;
- `added.length: 25`;
- `dropped: []`;
- tutte le chiavi aggiunte appartengono a M-SA01 e agli step 08-12.

- [ ] **Step 3: Interrompere in caso di differenza**

Se conteggi, target o `dropped` non coincidono, non eseguire `next`; confrontare scheda, test e run-state senza modificarlo manualmente.

- [ ] **Step 4: Verificare lo stato**

Run:

```text
npm run pipeline -- status VOL-07 --json
```

Expected: `done: 27`, `pending: 25`, nessun blocker e prossimo step 08 sul capitolo 04.

---

### Task 5: Piano operativo del capitolo 04

**Files:**

- Read: `artifacts/pipeline/VOL-07/08/moduli-m-sa01-sanita-amministrativa-chapters-04-atti-procedimenti-flussi-informativi-md/prompt.md`
- Read: `wiki/books/moduli/m-sa01-sanita-amministrativa/planning/02-matrice-copertura-didattica.md`
- Create: `wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa01-04.md`
- CLI-managed: `pipeline/VOL-07/run-state.json`

**Interfaces:**

- Consumes: prompt canonico dello step 08 e le righe M-SA01 collocate nel capitolo 04.
- Produces: piano capitolo verificabile e step 08 chiuso con accettazione manuale motivata.

- [ ] **Step 1: Prendere in carico lo step 08**

Run:

```text
npm run pipeline -- next VOL-07 --module M-SA01 --chapter 04 --json
```

Expected: step 08, gate `chapter-plan`, prompt scritto nell'artefatto indicato.

- [ ] **Step 2: Leggere integralmente il prompt**

Eseguire il lavoro soltanto dal prompt generato sotto il contratto CLI, senza ricostruirlo a memoria.

- [ ] **Step 3: Creare il piano capitolo**

Il report deve includere:

- obiettivo e promessa per lo studente;
- nuclei `Atti e procedimenti delle aziende sanitarie` e `Flussi informativi sanitari applicati`;
- mappa riga-per-riga fra matrice, fonti, sezioni, applicazione, output, verifica e review;
- struttura H1-H3;
- caso guidato su competenza, tracciabilità e qualità del dato;
- domanda da commissario, errore tipico e mini-esercizio;
- budget editoriale compatibile con il formato KDP;
- review step 15 su vigenza, legge regionale, atto aziendale e disciplinari tecnici.

- [ ] **Step 4: Verificare manualmente il piano**

Controllare che ogni nucleo abbia teoria esplicita e non sia coperto soltanto da caso, quiz o fonte. Verificare che nessun esempio locale sia presentato come regola nazionale.

- [ ] **Step 5: Chiudere lo step 08**

Run:

```text
npm run pipeline -- complete VOL-07 --step 08 --module M-SA01 --chapter 04 --accept --note "Piano operativo M-SA01 capitolo 04 verificato: i due nuclei della matrice sono collegati a teoria, applicazione, output, verifica, fonti e review step 15; struttura e budget didattico approvati."
```

Expected: `ok: true` e prossimo step 09 sul capitolo 04.

---

### Task 6: Scrittura autosufficiente del capitolo 04

**Files:**

- Read: `artifacts/pipeline/VOL-07/09/moduli-m-sa01-sanita-amministrativa-chapters-04-atti-procedimenti-flussi-informativi-md/prompt.md`
- Read: `wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa01-04.md`
- Create: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/04-atti-procedimenti-flussi-informativi.md`
- CLI-managed: `pipeline/VOL-07/run-state.json`

**Interfaces:**

- Consumes: piano approvato, matrice e source notes consolidate.
- Produces: capitolo destinato allo studente che supera `runChapterLintGate`.

- [ ] **Step 1: Prendere in carico lo step 09**

Run:

```text
npm run pipeline -- next VOL-07 --module M-SA01 --chapter 04 --json
```

Expected: step 09, gate `chapter-lint`.

- [ ] **Step 2: Richiamare memoria e skill writer**

Usare `LocalAgentMemory` con scope `VOL-07/M-SA01` e leggere integralmente `.agents/skills/concorso-book-professional-writer/SKILL.md`.

- [ ] **Step 3: Scrivere il capitolo**

Il corpo deve includere almeno:

```markdown
# Atti, procedimenti e flussi informativi nelle aziende sanitarie
## Obiettivo del capitolo
## Mappa BANDO
## L'azienda sanitaria e la distribuzione delle competenze
## Atti aziendali e provvedimenti amministrativi
## Il procedimento applicato al contesto sanitario
## Trasparenza, riservatezza e tracciabilità
## NSIS e principali famiglie di flussi
## Qualità, validazione e uso del dato
## Caso guidato
## Domanda da commissario
## Domanda-trappola
## Errore tipico
## Mini-esercizio
## Riferimenti normativi e professionali essenziali
```

Il frontmatter deve contenere `source_refs`, `last_compiled_from`, `draft_stage`, `updated_at` e `review_required`. Il corpo deve spiegare direttamente la materia senza wikilink verso risorse interne e senza presentare scadenze, tracciati o procedure regionali come universali.

- [ ] **Step 4: Eseguire il gate senza chiudere**

Run:

```text
npm run pipeline -- gate VOL-07 --step 09 --module M-SA01 --chapter 04 --json
```

Expected: `passed: true`, zero blocker.

- [ ] **Step 5: Chiudere lo step 09**

Run:

```text
npm run pipeline -- complete VOL-07 --step 09 --module M-SA01 --chapter 04 --json
```

Expected: `ok: true` e prossimo step 10 sul capitolo 04.

---

### Task 7: Verifica dashboard, regressioni e memoria

**Files:**

- Verify: `wiki/books/moduli/m-sa01-sanita-amministrativa/index.md`
- Verify: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/00-piano-editoriale.md`
- Verify: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/04-atti-procedimenti-flussi-informativi.md`
- Modify through API only: `wiki/memory/agent/`

**Interfaces:**

- Consumes: scheda sincronizzata e capitolo 04 scritto.
- Produces: evidenza verificata, dashboard coerente e traccia di continuità.

- [ ] **Step 1: Eseguire i test pipeline**

Run:

```text
npm test -- tests/pipeline
```

Expected: tutti i test passano.

- [ ] **Step 2: Eseguire suite completa e typecheck**

Run:

```text
npm test
npm run typecheck
```

Expected: exit code 0 per entrambi.

- [ ] **Step 3: Verificare la dashboard**

Aprire il volume 7, selezionare M-SA01 e controllare che:

- non compaia “Non avviato”;
- il modulo risulti pronto/in scrittura;
- il capitolo 04 sia visibile come primo capitolo editoriale reale;
- l'anteprima mostri il contenuto aggiornato del capitolo 04.

- [ ] **Step 4: Verificare stato e diff**

Run:

```text
npm run pipeline -- status VOL-07 --json
git diff --check
git status --short
```

Expected: nessun blocker; capitolo 04 fermo correttamente allo step 10; nessun errore whitespace. Distinguere nel report le modifiche di questo piano da quelle preesistenti.

- [ ] **Step 5: Registrare la memoria**

Usare `LocalAgentMemory.captureConversation` con:

- scope: `VOL-07/M-SA01`;
- route: `pipeline-volume/msa01-phase-c-start`;
- decisione: cinque capitoli attivati insieme e lavorati progressivamente;
- esito: step 07 già superato, sync CLI, capitolo 04 avviato, verifiche eseguite.

- [ ] **Step 6: Arrestare il ciclo al prossimo gate**

Non avviare lo step 10 nello stesso blocco senza aver consegnato l'esito del capitolo 04 e verificato la dashboard. Il prossimo ciclo ripartirà dal controllo di copertura dello stesso capitolo.
