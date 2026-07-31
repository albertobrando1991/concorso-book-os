# VOL-07 Full Editorial Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Portare VOL-07 da 7 capitoli configurati a 25 capitoli completi, chiudere gli step 08-14 e predisporre tutti i pacchetti dello step 15 lasciando il volume nello stato reale `awaiting-human`.

**Architecture:** La scheda pipeline dichiara l'intero perimetro A-F e resta l'unica sorgente degli step. Il run-state viene riallineato solo con `pipeline sync`; gli step editoriali vengono eseguiti esplicitamente per fase e target per completare tutta la fase C prima della fase D. Book Studio assegna una numerazione editoriale continua soltanto nella vista composita del volume, conservando ID e numerazione tecnica dei moduli.

**Tech Stack:** TypeScript, Vitest, CLI Node/tsx, Markdown con frontmatter YAML, Next.js Book Studio, Git.

## Global Constraints

- Leggere e rispettare `wiki/AGENTS.md` e `.agents/skills/pipeline-volume/SKILL.md`.
- Usare `LocalAgentMemory` prima degli output AI e registrare una traccia sintetica dopo il flusso.
- Non modificare mai `pipeline/VOL-07/run-state.json` a mano.
- Ogni comando pipeline usa `--json`; l'esito dei gate si legge dal payload strutturato.
- Un gate non automatizzato si chiude con `--accept --note` soltanto dopo verifica manuale documentata.
- Lo step 15 non viene completato o accettato senza esiti umani firmati.
- Gli step 16-23 restano non avviati.
- I testi non citano “fonti consolidate”, source note, matrici o pacchetti interni come materiale accessibile allo studente.
- Procedure cliniche e tecniche restano non esecutive senza validazione del setting.
- Gli ID tecnici già registrati non vengono rinumerati.
- La consegna resta locale: nessun push, PR o deploy.
- Preservare i file sporchi non pertinenti; usare stage esatto.

## File Structure

### Pipeline e stato

- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`
- Modify: `src/pipeline/state/run-state.ts`
- Modify: `src/pipeline/cli/commands.ts`
- Modify: `pipeline/VOL-07/run-state.json` esclusivamente tramite CLI
- Create: `tests/pipeline/vol-07-full-run.test.ts`
- Modify: `tests/pipeline/run-state.test.ts`

### Dashboard

- Modify: `src/server/book/book-preview.ts`
- Modify: `tests/book-preview.test.ts`
- Modify: `tests/vol-07-visible-copy.test.ts`

### Indici

- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md`
- Modify: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/index.md`
- Modify: i quattro `planning/00-piano-editoriale.md`

### Capitoli nuovi

- Create: sette file in `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/`
- Create: sette file in `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/`
- Create: quattro file in `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/`

### Evidenze

- Create: report step 08, 10, 11 e 12 per ognuno dei 18 capitoli nuovi in `wiki/reviews/pipeline/VOL-07/`
- Create: report step 13 e 14 per i quattro moduli
- Create: quattro pacchetti step 15, con esiti umani lasciati vuoti

---

### Task 1: Manifest completo dei 25 capitoli

**Files:**
- Create: `tests/pipeline/vol-07-full-run.test.ts`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/planning/00-piano-editoriale.md`

**Interfaces:**
- Consumes: `parseVolumeSpec(markdown, specPath): VolumeSpec` and `buildStepDrafts(spec, phases): StepDraft[]`.
- Produces: spec A-F con 25 target, 125 step C, 16 step D, 7 step E e 2 step F.

- [ ] **Step 1: Write the failing manifest test**

```ts
expect(spec.phases).toEqual(["A", "B", "C", "D", "E", "F"])
expect(spec.modules.flatMap((module) => module.chapters)).toHaveLength(25)
expect(buildStepDrafts(spec, ["C"]).filter((step) => step.id === "09")).toHaveLength(25)
expect(buildStepDrafts(spec, ["D"])).toHaveLength(16)
expect(buildStepDrafts(spec, ["E"])).toHaveLength(7)
expect(buildStepDrafts(spec, ["F"])).toHaveLength(2)
```

- [ ] **Step 2: Run the focused test and verify RED**

Run: `.\node_modules\.bin\vitest.cmd run tests/pipeline/vol-07-full-run.test.ts`

Expected: FAIL because the current sheet declares only phases A-C and seven chapters.

- [ ] **Step 3: Expand the canonical sheet**

Set `phases: [A, B, C, D, E, F]`; declare all module phases and exactly the 25 targets listed in `docs/superpowers/specs/2026-07-31-vol-07-completamento-editoriale-design.md`. Preserve M-SA02 technical IDs `01` and `03`.

- [ ] **Step 4: Align volume and module planning copy**

Replace stale statements such as “non avviato”, “due capitoli” and “fasi D-F non attivate” with the configured scope. Do not claim that unwritten chapters exist or that human review is complete.

- [ ] **Step 5: Run tests and commit**

Run: `.\node_modules\.bin\vitest.cmd run tests/pipeline/vol-07-full-run.test.ts tests/pipeline/volume-spec.test.ts tests/pipeline/build-steps.test.ts`

Expected: PASS.

```text
git add tests/pipeline/vol-07-full-run.test.ts wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md wiki/books/moduli/m-sa02-professioni-sanitarie/planning/00-piano-editoriale.md wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/planning/00-piano-editoriale.md wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/planning/00-piano-editoriale.md
git commit -m "feat(vol-07): declare complete editorial manifest"
```

### Task 2: Stato esplicito `awaiting-human`

**Files:**
- Modify: `src/pipeline/state/run-state.ts`
- Modify: `src/pipeline/cli/commands.ts`
- Modify: `tests/pipeline/run-state.test.ts`

**Interfaces:**
- Consumes: `StepStatus`, `startStep`, registry gate `human-signoff`.
- Produces: `StartStepInput.status?: "in-progress" | "awaiting-human"` e payload `next.step.status` coerente.

- [ ] **Step 1: Write failing state-transition tests**

```ts
const updated = startStep(state, key, {
  owner: "info",
  agent: "codex",
  now: "2026-07-31T12:00:00.000Z",
  status: "awaiting-human"
})
expect(findStep(updated, key)?.status).toBe("awaiting-human")
```

Add a second assertion that the default remains `in-progress`.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `.\node_modules\.bin\vitest.cmd run tests/pipeline/run-state.test.ts`

Expected: FAIL because `StartStepInput` has no `status`.

- [ ] **Step 3: Implement the minimal transition**

Add the optional status to `StartStepInput`, restrict it to the two non-terminal claim states, and replace the hard-coded `status: "in-progress"` with `status: input.status ?? "in-progress"`.

In `next()`, pass `status: definition.gate === "human-signoff" ? "awaiting-human" : "in-progress"` and return the same value in the JSON payload.

- [ ] **Step 4: Run tests and commit**

Run: `.\node_modules\.bin\vitest.cmd run tests/pipeline/run-state.test.ts tests/pipeline/steps.test.ts`

Expected: PASS.

```text
git add src/pipeline/state/run-state.ts src/pipeline/cli/commands.ts tests/pipeline/run-state.test.ts
git commit -m "feat(pipeline): expose awaiting human review state"
```

### Task 3: Sincronizzazione sicura del run

**Files:**
- Modify through CLI only: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: manifest Task 1 and current state with 52 `done`.
- Produces: 167 total step records, 52 preserved `done`, 115 new `pending`.

- [ ] **Step 1: Capture the pre-sync state**

Run: `npm run pipeline -- status VOL-07 --json`

Expected: `counts.done = 52`, no active blocker.

- [ ] **Step 2: Run doctor**

Run: `npm run pipeline -- doctor --json`

Expected: `ok = true`.

- [ ] **Step 3: Sync**

Run: `npm run pipeline -- sync VOL-07 --json`

Expected: `added.length = 115`, `dropped.length = 0`.

- [ ] **Step 4: Verify preservation**

Run: `npm run pipeline -- status VOL-07 --json`

Expected: 167 total steps; all previous 52 remain `done`; first unfinished phase-C target is M-SA02 chapter 04 when filtered with `--phase C`.

- [ ] **Step 5: Commit**

```text
git add pipeline/VOL-07/run-state.json
git commit -m "chore(pipeline): sync full vol-07 run"
```

### Task 4: Numerazione editoriale continua nella dashboard

**Files:**
- Modify: `src/server/book/book-preview.ts`
- Modify: `tests/book-preview.test.ts`

**Interfaces:**
- Consumes: chapters already sorted within each `VolumeModuleBook`.
- Produces: volume-only `outlineSection` 1..N and optional `moduleOutlineSection` containing the technical number.

- [ ] **Step 1: Add a failing composite-volume fixture**

Create two module fixtures with technical sections `04`, `05`, `01`, `03`. Assert:

```ts
expect(readerChapters.map((chapter) => chapter.outlineSection)).toEqual(["1", "2", "3", "4"])
expect(readerChapters.map((chapter) => chapter.moduleOutlineSection)).toEqual(["4", "5", "1", "3"])
expect(new Set(readerChapters.map((chapter) => chapter.path)).size).toBe(4)
```

- [ ] **Step 2: Run and verify RED**

Run: `.\node_modules\.bin\vitest.cmd run tests/book-preview.test.ts`

Expected: FAIL because composite previews expose technical numbering.

- [ ] **Step 3: Implement generic volume numbering**

Add `moduleOutlineSection?: string` to `BookStudioChapter`. In `buildVolumeBookStudioData`, enumerate only real module chapters in volume/module order, preserve the original number in `moduleOutlineSection`, and assign `outlineSection: String(globalIndex + 1)`. Do not change `buildSingleBookStudioData`.

- [ ] **Step 4: Verify distinct previews and commit**

Run: `.\node_modules\.bin\vitest.cmd run tests/book-preview.test.ts tests/book-studio-state.test.ts`

Expected: PASS.

```text
git add src/server/book/book-preview.ts tests/book-preview.test.ts
git commit -m "feat(studio): number composite volume chapters globally"
```

## Chapter Execution Contract

Every chapter task below uses this exact sequence:

1. `npm run pipeline -- next VOL-07 --phase C --step 08 --module <MODULE> --chapter <NN> --json`
2. Create the step-08 plan at the path required by the rendered contract.
3. `npm run pipeline -- complete VOL-07 --step 08 --module <MODULE> --chapter <NN> --accept --note "<evidence>" --json` only if the gate reports `gate-not-implemented` and the plan checklist is complete.
4. Start step 09 with the same filters; use `concorso-book-professional-writer`.
5. Complete step 09 only when its JSON gate passes.
6. Start step 10, create the row-by-row coverage report, and close only with zero uncovered nuclei.
7. Start step 11; use `humanizer`; record the before/after evidence and close only if citation guard passes.
8. Start step 12; use `revisore-editoriale-totale`; write the fixed-format review report and close only when mandatory serious/medium errors are resolved.
9. Run `git diff --check` and the focused visible-copy/editorial tests.
10. Commit only the chapter and its four evidence reports.

Every chapter frontmatter must include `type: book_chapter`, canonical `title`, `status: revised_draft`, `outline_section`, `book_id`, `module_code`, `review_required: true`, exact `source_refs`, and `last_compiled_from`.

Every chapter body must contain: obiettivi; teoria autosufficiente; applicazione concorsuale; caso; errori frequenti; sintesi; verifica; fonti ufficiali per il lettore; limiti e cut-off.

### Task 5: M-SA02 capitolo 04

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/04-assistenza-infermieristica-tecniche-assistenziali-oss.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-04`

**Interfaces:**
- Consumes: row “Scienze infermieristiche e tecniche assistenziali” of `m-sa02.../planning/02-matrice-copertura-didattica.md`, `planning/06-checklist-igiene-letto-trasferimenti-review.md`, sources on profiles, OSS, ICA, therapy, lesions, assistance and transfer devices.
- Produces: non-executive student chapter distinguishing nursing responsibility, OSS support, setting procedure and device-specific instructions.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 04`.
- [ ] Use H2 sections: processo assistenziale; bisogni and planning; safety and ICA; hygiene/nutrition/elimination; mobilization and lesion prevention; nurse-OSS attribution; contest case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 04"`.

### Task 6: M-SA02 capitolo 05

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/05-valutazione-clinica-triage-urgenza-emergenza.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-05`

**Interfaces:**
- Consumes: row “Clinica generale ed emergenza”; sources on triage, NEWS2/sepsis, BLS/ALS/NLS, obstetric emergencies and rehabilitation.
- Produces: recognition, prioritisation and escalation chapter with no executable algorithms or dosages.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 05`.
- [ ] Use H2 sections: initial assessment; deterioration; triage; emergency team; adult and neonatal resuscitation framework; obstetric alerts; reasoned cases; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 05"`.

### Task 7: M-SA02 capitolo 06

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/06-prevenzione-continuita-presa-in-carico.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-06`

**Interfaces:**
- Consumes: row “Prevenzione e presa in carico”; AGENAS, COT/territory, PDTA, consent, ICA, pregnancy and rehabilitation sources.
- Produces: education, chronicity, transitions, territory and fragile-person case.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 06`.
- [ ] Use H2 sections: prevention levels; health education; chronicity; PDTA; discharge and COT; consent/information; multiprofessional case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 06"`.

### Task 8: M-SA02 capitolo 07

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/07-evidenze-pico-grade-applicabilita.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-07`

**Interfaces:**
- Consumes: row “Evidenze scientifiche” and `planning/08-pacchetto-esercizi-pico-grade-applicabilita.md`.
- Produces: PICO, study designs, bias, GRADE, EtD and applicability chapter with five exercises.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 07`.
- [ ] Use H2 sections: clinical question; evidence hierarchy; search; appraisal/bias; GRADE; recommendation versus applicability; five exercises; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 07"`.

### Task 9: M-SA02 capitolo 08

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/08-igiene-pubblica-epidemiologia-screening.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-08`

**Interfaces:**
- Consumes: row “Igiene pubblica ed epidemiologia”, `planning/03-batteria-esercizi-epidemiologia-screening.md`, `planning/04-scenario-risposta-segnale-epidemiologico.md`.
- Produces: measures, studies, screening, surveillance, PREMAL, ICA and quantitative exercises.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 08`.
- [ ] Use H2 sections: frequencies; associations; designs/bias; screening indicators; surveillance/PASSI; PREMAL signal; ICA; calculations and scenario; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 08"`.

### Task 10: M-SA02 capitolo 09

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/09-controlli-tpall-verbalizzazione-campionamento-sanzioni.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-09`

**Interfaces:**
- Consumes: row “Controlli, verbalizzazione e sanzioni” and TPALL sources on official controls, AIA, environmental sampling, emissions and methods.
- Produces: inspection, evidence, sampling plan, chain-of-custody limits, report and non-compliance case.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 09`.
- [ ] Use H2 sections: role and powers; inspection planning; findings; sampling logic; verbalisation; non-compliance/sanctions; environmental case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 09"`.

### Task 11: M-SA02 capitolo 10

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/10-prova-pratica-casi-professionali.md`
- Create: reports 08, 10, 11, 12 for `m-sa02-10`

**Interfaces:**
- Consumes: row “Prova pratica/procedurale/caso professionale” and all M-SA02 rows.
- Produces: reusable reasoning method plus separate nursing/OSS, obstetric, physiotherapy, epidemiology and TPALL cases.

- [ ] Execute the Chapter Execution Contract with `--module M-SA02 --chapter 10`.
- [ ] Use H2 sections: decode prompt; safety and assumptions; output structure; five profile cases; oral defence; scoring rubric; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa02 chapter 10"`.

### Task 12: M-SA03 capitolo 01

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/01-profili-requisiti-prove-dirigenza-sanitaria.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-01`

**Interfaces:**
- Consumes: profile/bandi row of the M-SA03 matrix and `sources/bandi-rappresentativi-m-sa03-dirigenza-medica-sanitaria-2026`.
- Produces: profiles, stable/mobile requirements, exam forms and Bando Decoder.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 01`.
- [ ] Use H2 sections: families; requirements; commissions/proofs; stable versus mobile data; Bando Decoder; guided example; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 01"`.

### Task 13: M-SA03 capitolo 02

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/02-programmazione-sanitaria-organizzazione-servizi.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-02`

**Interfaces:**
- Consumes: “Programmazione sanitaria” row and organisation/LEA/planning sources referenced by the matrix.
- Produces: needs, objectives, resources, levels, indicators and programme-case chapter.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 02`.
- [ ] Use H2 sections: programming cycle; needs; national/regional/company levels; objectives/resources; indicators; programme case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 02"`.

### Task 14: M-SA03 capitolo 03

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/03-linee-guida-appropriatezza-decisioni-cliniche.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-03`

**Interfaces:**
- Consumes: rows “Linee guida e appropriatezza” and sources on SNLG/evidence.
- Produces: evidence-to-decision, appropriateness and traceable decision-case chapter.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 03`.
- [ ] Use H2 sections: guideline lifecycle; recommendation strength; appropriateness dimensions; local adaptation; decision case; oral answer; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 03"`.

### Task 15: M-SA03 capitolo 04

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/04-governo-clinico-hta-qualita-accreditamento-rischio.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-04`

**Interfaces:**
- Consumes: clinical-governance, HTA, quality/accreditation and clinical-risk rows.
- Produces: integrated governance system, audit, indicators, HTA domains, risk cycle and improvement case.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 04`.
- [ ] Use H2 sections: governance architecture; quality; accreditation; audit; HTA; risk; incident learning; improvement case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 04"`.

### Task 16: M-SA03 capitolo 05

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/05-epidemiologia-sanita-pubblica-dirigenza.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-05`

**Interfaces:**
- Consumes: epidemiology/public-health row and ISS surveillance sources.
- Produces: population measures, surveillance, screening and management interpretation.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 05`.
- [ ] Use H2 sections: measures; designs; surveillance; screening; inequalities; management indicators; decision case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 05"`.

### Task 17: M-SA03 capitolo 06

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/06-dirigenza-medica-discipline-casi.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-06`

**Interfaces:**
- Consumes: medical-discipline/case row and `V7-DIR-MED` destinations.
- Produces: method for speciality-specific written, practical and oral cases; no universal clinical manual.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 06`.
- [ ] Use H2 sections: identify speciality perimeter; construct differential reasoning; evidence and setting; risk/escalation; written case; oral defence; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 06"`.

### Task 18: M-SA03 capitolo 07

**Files:**
- Create: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/07-dirigenza-sanitaria-non-medica-discipline-casi.md`
- Create: reports 08, 10, 11, 12 for `m-sa03-07`

**Interfaces:**
- Consumes: non-medical health-management row and `V7-DIR-SAN` destinations.
- Produces: profile-specific reasoning for biology, pharmacy, psychology and other eligible health-management profiles without merging their scopes.

- [ ] Execute the Chapter Execution Contract with `--module M-SA03 --chapter 07`.
- [ ] Use H2 sections: profile map; competence boundaries; laboratory/pharmacy/psychology examples; governance contribution; profile case; oral defence; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa03 chapter 07"`.

### Task 19: M-SA04 capitolo 01

**Files:**
- Create: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/01-profili-tslb-tsrm-requisiti-prove-responsabilita.md`
- Create: reports 08, 10, 11, 12 for `m-sa04-01`

**Interfaces:**
- Consumes: profile/responsibility row and bandi/professional-order sources from the M-SA04 matrix.
- Produces: explicit TSLB/TSRM distinction, requirements, responsibilities and exam map.

- [ ] Execute the Chapter Execution Contract with `--module M-SA04 --chapter 01`.
- [ ] Use H2 sections: profiles; titles/albo; responsibilities; work interfaces; written/practical/oral tests; Bando Decoder; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa04 chapter 01"`.

### Task 20: M-SA04 capitolo 02

**Files:**
- Create: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/02-tslb-processo-laboratorio-qualita-biosicurezza.md`
- Create: reports 08, 10, 11, 12 for `m-sa04-02`

**Interfaces:**
- Consumes: TSLB laboratory-process, applied-discipline, quality and biosafety rows.
- Produces: pre-analytical/analytical/post-analytical process, quality system, biosafety and non-executive cases.

- [ ] Execute the Chapter Execution Contract with `--module M-SA04 --chapter 02`.
- [ ] Use H2 sections: laboratory cycle; samples/traceability; applied bio/chem/micro/haematology map; QC/QA; biosafety; non-conformity case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa04 chapter 02"`.

### Task 21: M-SA04 capitolo 03

**Files:**
- Create: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/03-tsrm-imaging-dosimetria-radioprotezione.md`
- Create: reports 08, 10, 11, 12 for `m-sa04-03`

**Interfaces:**
- Consumes: TSRM technique/image-quality and dosimetry/radioprotection rows.
- Produces: modality principles, image-quality trade-offs, justification/optimisation framework and safety cases without equipment-specific settings.

- [ ] Execute the Chapter Execution Contract with `--module M-SA04 --chapter 03`.
- [ ] Use H2 sections: imaging chain; modality map; image quality; artefacts; dose/dosimetry; radioprotection; safety case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa04 chapter 03"`.

### Task 22: M-SA04 capitolo 04

**Files:**
- Create: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/04-tecnologie-dispositivi-apparecchiature-rischio.md`
- Create: reports 08, 10, 11, 12 for `m-sa04-04`

**Interfaces:**
- Consumes: devices/equipment and technological-risk/improvement rows.
- Produces: lifecycle, controls, maintenance interfaces, vigilance, risk analysis and improvement case.

- [ ] Execute the Chapter Execution Contract with `--module M-SA04 --chapter 04`.
- [ ] Use H2 sections: device lifecycle; equipment acceptance/use; maintenance responsibilities; vigilance; technological risk; incident/improvement case; verification.
- [ ] Commit: `git commit -m "feat(vol-07): complete m-sa04 chapter 04"`.

### Task 23: Indici e copia visibile dei 25 capitoli

**Files:**
- Modify: module indices for M-SA02, M-SA03, M-SA04
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`
- Modify: `tests/vol-07-visible-copy.test.ts`

**Interfaces:**
- Consumes: 25 chapter files and volume-only numbering from Task 4.
- Produces: canonical TOC, 25 unique paths, global sections 1..25 and clean visible copy.

- [ ] **Step 1: Write failing final-copy assertions**

```ts
expect(readerChapters).toHaveLength(25)
expect(readerChapters.map((chapter) => chapter.outlineSection)).toEqual(
  Array.from({ length: 25 }, (_, index) => String(index + 1))
)
expect(new Set(readerChapters.map((chapter) => chapter.path)).size).toBe(25)
expect(readerChapters.map((chapter) => chapter.blocks)).not.toContainEqual([])
```

Add a scan that rejects internal production phrases in chapter bodies and malformed visible accents.

- [ ] **Step 2: Run RED**

Run: `.\node_modules\.bin\vitest.cmd run tests/vol-07-visible-copy.test.ts`

Expected: FAIL until indices and expected copy are aligned.

- [ ] **Step 3: Update all indices**

List chapters in module order; display volume order 1-25; preserve technical IDs in paths. Set volume state to “in attesa di revisione specialistica” only after Task 25 starts all human gates.

- [ ] **Step 4: Run GREEN and commit**

Run: `.\node_modules\.bin\vitest.cmd run tests/vol-07-visible-copy.test.ts tests/book-preview.test.ts tests/editorial-plan.test.ts`

Expected: PASS.

```text
git add tests/vol-07-visible-copy.test.ts wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md wiki/books/moduli/m-sa02-professioni-sanitarie/index.md wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/index.md
git commit -m "docs(vol-07): publish complete student chapter index"
```

### Task 24: Review e correzioni di modulo, step 13-14

**Files:**
- Create: four step-13 review reports
- Create: four step-14 correction reports
- Modify: chapters only where the review identifies serious or medium errors

**Interfaces:**
- Consumes: all chapters after step 12.
- Produces: modules with zero unresolved serious/medium editorial errors; no human specialist signoff.

- [ ] For each of `M-SA02`, `M-SA01`, `M-SA03`, `M-SA04`, run `npm run pipeline -- next VOL-07 --phase D --step 13 --module <MODULE> --json`.
- [ ] Use `revisore-editoriale-totale` and write the exact fixed-format report required by the rendered contract.
- [ ] Close step 13 only when `review-report` passes.
- [ ] Run step 14 for the same module, apply every mandatory serious/medium correction, record file/position/before/after/evidence, and close only when the gate passes or a documented manual gate is legitimately accepted.
- [ ] Rerun affected chapter tests and `git diff --check`.
- [ ] Commit each module separately with `review(vol-07): close <module> editorial corrections`.

### Task 25: Pacchetti dello step 15 e arresto umano

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa01.md`
- Create: `wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa02.md`
- Create: `wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa03.md`
- Create: `wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa04.md`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`
- Modify through CLI: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: step-13/14 reports, all `review_required` flags and existing M-SA02 review dossiers.
- Produces: four complete reviewer workbooks and four state records `awaiting-human`; no gate completion.

- [ ] For each module run `npm run pipeline -- next VOL-07 --phase D --step 15 --module <MODULE> --json`.
- [ ] Verify the JSON returns `step.status = "awaiting-human"`.
- [ ] Create the package table with exact columns: file/position; assertion; official source; question; risk; outcome; correction.
- [ ] Populate every high-risk claim and all existing `review_required` entries; leave outcome, reviewer identity/signature and accepted correction empty.
- [ ] Do not run `complete` or `--accept` for step 15.
- [ ] Verify `npm run pipeline -- status VOL-07 --json` reports four awaiting-human steps and no step 16-23 started.
- [ ] Update the volume index state to “scrittura e revisione editoriale automatiche completate; in attesa di revisione umana specialistica”, without claiming text freeze or publication readiness.
- [ ] Commit the packages and CLI-generated state:

```text
git add wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa01.md wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa02.md wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa03.md wiki/reviews/pipeline/VOL-07/15-review-umana-specialistica-m-sa04.md wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md pipeline/VOL-07/run-state.json
git commit -m "review(vol-07): prepare specialist human signoff"
```

### Task 26: Verifica finale, dashboard e memoria

**Files:**
- Modify: local memory files selected by `LocalAgentMemory`
- Modify: `wiki/log.md` only if required by `wiki/AGENTS.md`

**Interfaces:**
- Consumes: complete automatic work through step 14 and awaiting-human packages.
- Produces: evidence-backed local handoff, no publication claim.

- [ ] Run `npm run pipeline -- doctor --json`; expect `ok = true`.
- [ ] Run `npm run pipeline -- status VOL-07 --json`; expect 52 historical plus 90 new chapter steps and 8 module-review steps done, four step-15 records awaiting human, all later records pending.
- [ ] Run `.\node_modules\.bin\vitest.cmd run`; expect all tests PASS.
- [ ] Run `.\node_modules\.bin\tsc.cmd --noEmit`; expect exit code 0.
- [ ] Run `git diff --check`; expect no output.
- [ ] Start the dashboard with `npm run dev`, open `http://127.0.0.1:3000/?bookId=volumi%2Fvol-07#studio`, and visually verify 25 distinct previews, titles, accents and awaiting-human status.
- [ ] Record the decisions and stopping point through `LocalAgentMemory`.
- [ ] Stage only intended memory/log files and commit `chore(vol-07): record human review handoff`.
- [ ] Report the final commit, test evidence, dashboard URL, reviewer package paths and exact resume command. Do not claim completion of the volume beyond the human gate.
