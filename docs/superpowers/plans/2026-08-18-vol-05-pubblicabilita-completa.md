# VOL-05 Publishability Retrofit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert VOL-05 into a complete format-2 editorial package, pass pipeline steps C–F through delivery, and stop with step 24 awaiting human sign-off.

**Architecture:** Preserve the existing fifteen-chapter module and integrate verified specialist gaps before rebuilding each chapter as an autonomous format-2 unit. Add the promised appendices, reader front matter, conclusion, source apparatus, visual audit, KDP layout, ebook reflow checks, and delivery manifest in the order enforced by the pipeline CLI. Internal plans and reviews remain outside reader-visible content.

**Tech Stack:** Markdown/YAML frontmatter, ConcorsoBook pipeline CLI, TypeScript/tsx, Vitest, LocalAgentMemory, official primary-source web research, Book Studio/Next.js, Playwright/Chromium, PDF inspection tooling.

**Spec:** `docs/superpowers/specs/2026-08-18-vol-05-retrofit-editoriale-integrale-design.md`

## Global Constraints

- Preserve the fifteen existing numbered chapters and the author's professional, operational voice.
- Use `N-FC05-<CAP>-<NN>` as the canonical nucleus-ID interface.
- Every worked chapter declares `format_version: 2`; the exact contract printed by `pipeline next` overrides remembered defaults.
- Default minimums are five nuclei of at least 600 words, 3,000 chapter words, six commented quizzes, one reasoned case, and a `▣ Verifica` block every five to seven nuclei.
- Use the editorial cut-off `2026-08-18`; every dynamic source records its own verification date.
- Never write final reader text directly from `wiki/raw/`; consolidate official sources first.
- Reader files contain no staff plans, review notes, wiki paths, internal IDs outside visible Nucleo IDs, or links to `sources/`, `topics/`, `entities/`, `raw/`, `planning/`, or `reviews/`.
- `parziale`, `solo-nominato`, and `mancante` are blocking; `rinviato` requires a precise, existing, complete destination.
- Never edit `pipeline/VOL-05/run-state.json` manually; use `init`, `next`, `gate`, `complete`, `sync`, and structured `--json` output.
- Open step 11 with `next` before any Humanizer edit so the citation snapshot exists.
- Use `--accept --note` only for a manually verified `gate-not-implemented`, never to hide a blocker.
- Call `LocalAgentMemory` with scope `VOL-05` before every LLM step and capture a concise trace after each important flow.
- Keep `.dashboard-dev.stderr.log`, `.dashboard-dev.stdout.log`, pre-existing memory changes, and unrelated work out of scoped commits.
- Do not complete step 24, publish, push, or claim human approval.

---

### Task 1: Correct the nucleus interface and capture the baseline

**Files:**
- Modify: `docs/superpowers/specs/2026-08-18-vol-05-retrofit-editoriale-integrale-design.md`
- Create: `wiki/reviews/pipeline/VOL-05/00-retrofit-baseline.md`

**Interfaces:**
- Consumes: approved design, final review dated 2026-08-18, fifteen existing chapter files.
- Produces: canonical `N-FC05` naming and an auditable before-state.

- [ ] **Step 1: Correct the approved spec interface**

Replace `N-M-FC05-<CAP>-<NN>` with `N-FC05-<CAP>-<NN>`; no other design requirement changes.

- [ ] **Step 2: Inventory the baseline**

Record for each chapter: word count, H2/H3 count, current `format_version`, nucleus IDs, quiz headings, reasoned cases, figures, internal reader links, `Scheda di lavoro`, `Riferimenti consolidati`, and `Note di review editoriale`. Record volume-level counts for chapters, referenced figures, appendices, conclusion, and internal links.

- [ ] **Step 3: Run baseline assertions**

Run:

```text
npm run pipeline -- doctor --json
npm run pipeline -- status VOL-05 --json
git diff --check
```

Expected: doctor `ok: true`; status reports missing run-state; diff check exits 0.

- [ ] **Step 4: Commit only spec correction and baseline**

```text
git add docs/superpowers/specs/2026-08-18-vol-05-retrofit-editoriale-integrale-design.md wiki/reviews/pipeline/VOL-05/00-retrofit-baseline.md
git commit -m "docs(vol-05): capture publishability retrofit baseline"
```

### Task 2: Create the canonical pipeline specification and coverage matrix

**Files:**
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/planning/00-scheda-pipeline.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/planning/02-matrice-copertura-didattica.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/planning/03-bibbia-editoriale-retrofit.md`

**Interfaces:**
- Consumes: `wiki/templates/scheda-pipeline-volume-template.md`, approved spec, current index, fifteen chapters.
- Produces: one declared M-FC05 module, fifteen ordered chapter targets, exact matrix path, vocabulary/style contract.

- [ ] **Step 1: Write the pipeline frontmatter**

Use exactly:

```yaml
type: pipeline_spec
volume_code: VOL-05
volume_title: Authority e regolazione
cut_off_date: 2026-08-18
writer_provider: codex
phases: [C, D, E, F]
status: approved
updated_at: 2026-08-18
```

Declare `M-FC05 | moduli/m-fc05-authority-indipendenti | 1 | C, D, E, F` and all fifteen existing files in numerical order, each with matrix `planning/02-matrice-copertura-didattica.md`, expected state `completo`, minimum 3,000 words, and minimum six quizzes.

- [ ] **Step 2: Build the format-2 coverage matrix**

Create columns `Materia | Concetto | Nucleo ID | Fonte | Collocazione | Teoria | Applicazione | Output | Verifica | Evidenza Q/C/E | Stato | Review normativa`. Allocate every promise from the analytical index and every issue V05-006 through V05-029 to one exact `N-FC05-CC-NN` destination. Keep actual incompleteness visible in the baseline report; the matrix expresses the approved target contract and later gates must prove it.

- [ ] **Step 3: Write the editorial Bible**

Fix terminology and casing: `Autorità` in Italian prose; lowercase `authority` only for sector usage or the product title; official spellings `Banca d'Italia`, `CONSOB`, `AGCOM`, `AGCM`, `ARERA`, `IVASS`, `ANAC`, `Garante per la protezione dei dati personali`, `ACER`, `BEREC`, `EDPB`, `BCE`. Define the chain `fonte → potere → procedura → garanzia → output`, approved box names, citation form, acronym first-use rule, date/percentage style, caption style, and banned generic endings.

- [ ] **Step 4: Validate paths without initializing state**

Run the repository's pipeline specification tests and confirm all fifteen declared files and the matrix path exist. Expected: specification parses, catalog resolves VOL-05 to M-FC05, and no undeclared chapter target is created.

- [ ] **Step 5: Commit the planning contract**

```text
git add wiki/books/moduli/m-fc05-authority-indipendenti/planning/00-scheda-pipeline.md wiki/books/moduli/m-fc05-authority-indipendenti/planning/02-matrice-copertura-didattica.md wiki/books/moduli/m-fc05-authority-indipendenti/planning/03-bibbia-editoriale-retrofit.md
git commit -m "docs(vol-05): define format 2 pipeline contract"
```

### Task 3: Consolidate the missing official-source package

**Files:**
- Create: `wiki/sources/regolamento-ue-2024-1106-remit-ii.md`
- Create: `wiki/sources/bce-vigilanza-unica-si-lsi-2026-08-18.md`
- Create: `wiki/sources/regolamento-ue-2022-1925-digital-markets-act.md`
- Create: `wiki/sources/micar-regolamento-ue-2023-1114-vigilanza-italiana.md`
- Create: `wiki/sources/dora-regolamento-ue-2022-2554-resilienza-operativa.md`
- Create: `wiki/sources/ivass-arbitro-assicurativo-operativo-2026.md`
- Create: `wiki/sources/anac-whistleblowing-ritorsioni-onere-prova-2026.md`
- Create: `wiki/sources/arera-mtr-3-deliberazione-397-2025-r-rif.md`
- Modify: `wiki/sources/regolazione-ue-digitale-e-finanziaria-vol-05.md`
- Modify: `wiki/sources/banca-italia-ivass-vigilanza-prudenziale-2026-07-24.md`
- Modify: `wiki/sources/anac-prevenzione-vigilanza-whistleblowing-2026-07-24.md`
- Modify: `wiki/index.md`
- Append: `wiki/log.md`

**Interfaces:**
- Consumes: EUR-Lex CELEX 32024R1106, 32022R1925, 32023R1114, 32022R2554; official ECB SSM material; official Banca d'Italia, CONSOB, IVASS, ANAC and ARERA pages/acts.
- Produces: source summaries with `source_url`, `source_date`, `authority_level`, topics, entities, impact on chapters, and 2026-08-18 verification.

- [ ] **Step 1: Verify every primary source online**

Open the official act or institutional page, verify title, date, current applicability, competent authorities, transition dates, and limits. Use no commercial summaries as authority.

- [ ] **Step 2: Create the eight source notes**

Each note states what the source proves, what it does not prove, affected chapters, relevant articles/sections, and cut-off. For AAS record operation from 15 January 2026; for whistleblowing record the retaliation burden/presumption; for SSM distinguish significant and less significant institutions.

- [ ] **Step 3: Reconcile the three existing aggregate notes**

Add links and deltas without deleting prior history. Remove stale statements only by adding an explicit superseding update section.

- [ ] **Step 4: Update the canonical index and append-only log**

Add the new source notes under the correct source catalog sections. Append one `knowledge_ingest` event listing eight notes, official-source classes, affected chapters 3/9/10/12/14, and cut-off.

- [ ] **Step 5: Run source integrity checks and commit**

Assert YAML validity, unique IDs, official URLs, inbound/outbound links, and no missing source paths. Commit only the source package, `wiki/index.md`, and the new append-only log block with `docs(vol-05): consolidate 2026 regulatory sources`.

### Task 4: Initialize VOL-05 and close the source-ready baseline steps

**Files:**
- Create through CLI: `pipeline/VOL-05/run-state.json`
- Create/update: reports and prompts required by the initialized phase contract.

**Interfaces:**
- Consumes: pipeline spec, matrix, source package.
- Produces: CLI-owned ordered state for steps 08–24.

- [ ] **Step 1: Recall LocalAgentMemory**

Query scope `VOL-05` for approved retrofit, format 2, source cut-off, appendices, and human sign-off; use memory only as workflow context.

- [ ] **Step 2: Run doctor and initialize**

Run:

```text
npm run pipeline -- doctor --json
npm run pipeline -- init VOL-05 --json
npm run pipeline -- status VOL-05 --json
```

Expected: doctor and init `ok: true`; state contains fifteen chapter cycles, one module cycle, visual/layout steps, final steps, and pending step 24.

- [ ] **Step 3: Validate generated targets**

Assert exactly fifteen step-08 through step-12 targets, all under M-FC05, and no appendices treated as numbered chapters.

- [ ] **Step 4: Commit the initialized state**

```text
git add pipeline/VOL-05/run-state.json
git commit -m "chore(vol-05): initialize publication pipeline"
```

### Task 5: Retrofit chapter 01 — reader map, profiles, and Bando Decoder

**Files:**
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/01-authority-viste-dal-candidato.md`
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/planning/02-matrice-copertura-didattica.md`
- Update through CLI: `pipeline/VOL-05/run-state.json`
- Create/update: chapter-01 reports under `wiki/reviews/pipeline/VOL-05/`

**Interfaces:** Produces `N-FC05-01-01` through `N-FC05-01-06`: authority map; profiles and examinations; source/power recognition; specialist delta versus VOL-01; legal/economic/mixed paths; Bando Decoder.

- [ ] Open step 08, read the generated prompt, map the six nuclei and all Q/C/E evidence, then close the chapter-plan gate with documented manual evidence if required.
- [ ] Open step 09, remove `Specifica struttura madre`, `Scheda di lavoro`, internal references and review notes; set format 2; write autonomous reader text meeting the printed contract.
- [ ] Add six commented quizzes and a reasoned decoder case in `▣ Verifica`; keep only reader-meaningful figures and specific captions.
- [ ] Complete step 09, pass the composite step-10 gate, and correct every coverage, density or referral blocker.
- [ ] Open step 11 before Humanizer edits; preserve citations and claims; complete step 11, then run the fixed total-review report at step 12 and resolve every grave finding.
- [ ] Verify IDs, word thresholds, quizzes, case, source refs, no internal links, and clean diff; commit `docs(vol-05): retrofit chapter 01 to format 2`.

### Task 6: Retrofit chapter 02 — independence, governance, and personnel

**Files:** Target `chapters/02-indipendenza-governance-accountability-personale.md`, matrix, run-state, and chapter-02 reports.

**Interfaces:** Produces `N-FC05-02-01` through `N-FC05-02-06`: foundations of independence; appointments and terms; incompatibilities and conflicts; accountability; personnel and recruitment; comparative authority table.

- [ ] Run step 08 and assign each governance promise to one nucleus with exact sources and Q/C/E evidence.
- [ ] Run step 09 with a real comparative table for selected authorities; replace research instructions with directly taught distinctions.
- [ ] Add a reasoned appointment/incompatibility case and six commented quizzes; pass step 10 without generic claims about all authorities.
- [ ] Run step 11 Humanizer after its snapshot and step 12 total review; correct blockers.
- [ ] Verify and commit `docs(vol-05): retrofit chapter 02 to format 2`.

### Task 7: Retrofit chapter 03 — EU networks, REMIT II, and SSM

**Files:** Target `chapters/03-regolazione-europea-multilivello-reti-autorita.md`, matrix, run-state, source refs, and chapter-03 reports.

**Interfaces:** Produces `N-FC05-03-01` through `N-FC05-03-06`: EU legal sources; network/agency/authority distinctions; ECN/BEREC/ACER/EDPB/ESFS; REMIT II powers; SSM SI/LSI allocation; cross-border case.

- [ ] Open step 08 and bind REMIT II to CELEX 32024R1106 and SSM claims to the consolidated ECB note.
- [ ] Rewrite step 09 text so ACER's post-2024 investigatory role is not omitted and ECB/NCA responsibilities are not collapsed.
- [ ] Add a cross-border competence case, one comparison table, and six commented quizzes.
- [ ] Pass step 10, citation guard, Humanizer, and total review in the required order.
- [ ] Verify no statement presents networks, agencies and national authorities as interchangeable; commit `docs(vol-05): update EU regulation chapter`.

### Task 8: Retrofit chapter 04 — consultation, AIR, and VIR

**Files:** Target `chapters/04-ciclo-regolatorio-consultazione-air-vir.md`, matrix, run-state, and chapter-04 reports.

**Interfaces:** Produces `N-FC05-04-01` through `N-FC05-04-06`: regulatory cycle; consultation; AIR; options/evidence; VIR; documented ARERA/AGCOM comparison and output.

- [ ] Map the six nuclei at step 08 using the DPCM 169/2017 note and two verified authority procedures.
- [ ] At step 09 distinguish general method from authority-specific rules and add a worked consultation-to-VIR example.
- [ ] Add six commented quizzes, a case requiring an AIR outline, and a comparison table with scope caveats.
- [ ] Pass steps 10–12, correcting over-generalization and every source/citation blocker.
- [ ] Verify and commit `docs(vol-05): strengthen regulatory cycle chapter`.

### Task 9: Retrofit chapter 05 — supervision, investigation, inspections, and evidence

**Files:** Target `chapters/05-vigilanza-istruttoria-ispezioni-dati-prova.md`, matrix, run-state, and chapter-05 reports.

**Interfaces:** Produces `N-FC05-05-01` through `N-FC05-05-06`: source of powers; information requests; inspections; data/evidence; adversarial safeguards/access; comparative investigation case.

- [ ] Map authority-specific powers and limits at step 08; do not infer one authority's powers from another's statute.
- [ ] Retrofit step 09 around the evidentiary chain and procedural safeguards, preserving useful original passages.
- [ ] Add a document-classification exercise, reasoned inspection case, and six commented quizzes.
- [ ] Pass steps 10–12; verify proportionality and due-process statements against the declared sources.
- [ ] Verify and commit `docs(vol-05): retrofit investigation chapter`.

### Task 10: Retrofit chapter 06 — sanctions, commitments, remedies, and judicial control

**Files:** Target `chapters/06-sanzioni-impegni-rimedi-controllo-giurisdizionale.md`, matrix, run-state, and chapter-06 reports.

**Interfaces:** Produces `N-FC05-06-01` through `N-FC05-06-06`: sanction principles; commitments and corrective measures; sanction procedure; judicial protection; authority–act–judge–procedure–term matrix; reasoned remedy case.

- [ ] Build the step-08 plan from law 689/1981, the administrative-procedure code, and authority-specific sources; mark variable terms by scope.
- [ ] At step 09 add the promised comparison matrix and correct `Nel privacy` to natural Italian.
- [ ] Add a remedy-selection case and six commented quizzes; never present one appeal term as universal.
- [ ] Pass steps 10–12 and resolve every jurisdiction/cut-off warning.
- [ ] Verify and commit `docs(vol-05): complete sanctions and remedies chapter`.

### Task 11: Retrofit chapter 07 — industrial economics, econometrics, and regulatory accounting

**Files:** Target `chapters/07-economia-industriale-regolazione-econometria-contabilita.md`, matrix, run-state, and chapter-07 reports.

**Interfaces:** Produces `N-FC05-07-01` through `N-FC05-07-06`: market structure; market power/concentration; natural monopoly and tariffs; indicators/uncertainty/econometrics; cost allocation/regulatory accounting; complete numerical case.

- [ ] At step 08 define the exact formulas, assumptions, evidence, Q/C/E and calculator-free examination outputs.
- [ ] At step 09 teach concentration indicators, interpretation limits, cost drivers, allocated/common costs, and tariff logic with worked numbers.
- [ ] Add at least two solved calculations, one reasoned regulatory-accounting case, and six commented quizzes.
- [ ] Pass step 10 only if every formula is defined, units are coherent, and interpretation accompanies calculation.
- [ ] Run steps 11–12, preserve mathematical meaning during Humanizer edits, verify totals, and commit `docs(vol-05): deepen regulatory economics chapter`.

### Task 12: Retrofit chapter 08 — AGCM, competition, and consumer enforcement

**Files:** Target `chapters/08-agcm-concorrenza-consumatore-pratiche-scorrette.md`, matrix, run-state, and chapter-08 reports.

**Interfaces:** Produces `N-FC05-08-01` through `N-FC05-08-07`: system/competence; Article 101; Article 102; concentrations; exemptions/leniency/commitments; sanctions/procedure; consumer and unfair-practice enforcement.

- [ ] Map all seven nuclei at step 08 and distinguish competition enforcement from consumer protection.
- [ ] At step 09 explain legal tests, procedure, remedies, evidentiary issues and EU/national coordination without reducing them to labels.
- [ ] Add one antitrust classification case, one consumer-practice microcase, and six commented quizzes.
- [ ] Pass steps 10–12; correct any unsupported threshold, deadline or universalized procedural statement.
- [ ] Verify and commit `docs(vol-05): deepen AGCM chapter`.

### Task 13: Retrofit chapter 09 — ARERA sectors, tariffs, quality, and remedies

**Files:** Target `chapters/09-arera-energia-gas-acqua-rifiuti-tariffe.md`, matrix, run-state, and chapter-09 reports.

**Interfaces:** Produces `N-FC05-09-01` through `N-FC05-09-07`: mandate/sectors; electricity and gas; water; waste/MTR-3; tariff and quality logic; user protection/ADR; integrated case.

- [ ] Use the MTR-3 source and sector sources in step 08; identify what changes by regulated service.
- [ ] Retrofit step 09, remove the `?**.` punctuation error, and explain tariff/quality reasoning without implying identical rules across sectors.
- [ ] Add a tariff-quality case, sector comparison, and six commented quizzes.
- [ ] Pass steps 10–12 and verify all time-sensitive regime claims at the cut-off.
- [ ] Verify and commit `docs(vol-05): update ARERA chapter`.

### Task 14: Retrofit chapter 10 — AGCOM, DSA, DMA, and English memo

**Files:** Target `chapters/10-agcom-comunicazioni-media-utenti-piattaforme.md`, matrix, run-state, and chapter-10 reports.

**Interfaces:** Produces `N-FC05-10-01` through `N-FC05-10-07`: AGCOM system; electronic communications; media/pluralism; users/Corecom/ConciliaWeb; DSA; DMA boundaries; professional English memo.

- [ ] At step 08 bind DSA claims to AGCOM's official DSC role and DMA claims to CELEX 32022R1925; separate Commission enforcement from national sector powers.
- [ ] At step 09 develop DMA beyond a mention and add a complete English memo with factual background, issue, applicable framework, analysis, recommendation and risk note.
- [ ] Add one platform-competence case and six commented quizzes, including one English comprehension/application item.
- [ ] Pass steps 10–12; the review must check both legal allocation and idiomatic professional English.
- [ ] Verify and commit `docs(vol-05): complete AGCOM digital regulation chapter`.

### Task 15: Retrofit chapter 11 — CONSOB, markets, intermediaries, and ACF

**Files:** Target `chapters/11-consob-mercati-intermediari-tutela-investitore.md`, matrix, run-state, and chapter-11 reports.

**Interfaces:** Produces `N-FC05-11-01` through `N-FC05-11-07`: TUF architecture; issuers/prospectuses; investment services/MiFID; markets and abuse/MAR; CONSOB powers/procedure; ACF; integrated investor-protection case.

- [ ] Map legal ownership and specialist depth at step 08, distinguishing CONSOB, Banca d'Italia, ESMA and ACF roles.
- [ ] Expand step 09 with sufficient TUF, prospectus, services, market, proceeding and ADR theory.
- [ ] Add an investor-protection case, a competence table, and six commented quizzes.
- [ ] Pass steps 10–12 and correct any stale or overly broad allocation of powers.
- [ ] Verify and commit `docs(vol-05): deepen CONSOB chapter`.

### Task 16: Retrofit chapter 12 — Banca d'Italia, IVASS, MiCAR, and DORA

**Files:** Target `chapters/12-banca-italia-ivass-vigilanza-prudenziale.md`, matrix, run-state, source refs, and chapter-12 reports.

**Interfaces:** Produces `N-FC05-12-01` through `N-FC05-12-07`: SSM/Banca d'Italia; prudential banking; payments/ABF; IVASS/Solvency II; AAS; MiCAR allocation; DORA/resilience.

- [ ] At step 08 bind every nucleus to current official sources and explicitly allocate MiCAR responsibilities between Banca d'Italia and CONSOB.
- [ ] At step 09 teach payments, ABF, AAS operational from 15 January 2026, Solvency II pillars, MiCAR and DORA as autonomous nuclei rather than footnotes.
- [ ] Add a multi-authority allocation case, one SSM table, one ADR comparison, and six commented quizzes.
- [ ] Pass step 10 only after all V05-006 through V05-009 and V05-026 promises are evidenced.
- [ ] Run steps 11–12 with specialist fact-check, verify dates and institutional roles, and commit `docs(vol-05): complete prudential and digital finance chapter`.

### Task 17: Retrofit chapter 13 — Garante, proceedings, and European cooperation

**Files:** Target `chapters/13-garante-privacy-poteri-procedimenti-cooperazione.md`, matrix, run-state, and chapter-13 reports.

**Interfaces:** Produces `N-FC05-13-01` through `N-FC05-13-06`: authority role; complaint/report; corrective powers/sanctions; one-stop-shop; lead/concerned authorities and EDPB; cross-border case.

- [ ] Map GDPR provisions and national procedural sources at step 08; distinguish complaint, report and ex officio action.
- [ ] Retrofit step 09 with a complete cross-border cooperation sequence and limits of the one-stop-shop.
- [ ] Add a lead-authority case and six commented quizzes.
- [ ] Pass steps 10–12, checking that standard GDPR formulations are attributed and not presented as unattributed encyclopedia prose.
- [ ] Verify and commit `docs(vol-05): strengthen Garante chapter`.

### Task 18: Retrofit chapter 14 — ANAC, prevention, and whistleblowing

**Files:** Target `chapters/14-anac-prevenzione-vigilanza-whistleblowing.md`, matrix, run-state, source refs, and chapter-14 reports.

**Interfaces:** Produces `N-FC05-14-01` through `N-FC05-14-07`: ANAC role; PNA/RPCT; transparency and supervision; reporting channels/subjects; protected persons/facilitators; retaliation burden/presumption; sanctions/support and case.

- [ ] At step 08 use d.lgs. 24/2023, ANAC guidance, PNA 2025 and the 2026 source note; map the burden-of-proof issue explicitly.
- [ ] At step 09 integrate protected subjects, facilitators, channels, retaliation, evidentiary presumption, sanctions and support measures.
- [ ] Add a retaliation-classification case, a protection table, and six commented quizzes.
- [ ] Pass steps 10–12 with current-source verification and no confusion between anti-corruption planning, transparency and whistleblowing functions.
- [ ] Verify and commit `docs(vol-05): complete ANAC whistleblowing chapter`.

### Task 19: Retrofit chapter 15 — complete authority examination laboratory

**Files:** Target `chapters/15-laboratorio-prove-authority.md`, matrix, run-state, and chapter-15 reports.

**Interfaces:** Produces `N-FC05-15-01` through `N-FC05-15-07`: prompt analysis; concise answer; legal/economic case; technical oral; English memo; ten simulations with at least three full model solutions; rubric/error diary/30-60-90 plan.

- [ ] At step 08 map every exercise to theory actually taught in chapters 01–14; remove references to unarchived bandi.
- [ ] At step 09 provide at least three complete model solutions, one complete English memo, scoring rubrics, and examiner-facing answer structures.
- [ ] Add six commented meta-quiz items and one integrated full simulation under `▣ Verifica`.
- [ ] Pass step 10 with no exercise whose solution depends on omitted theory; then complete Humanizer and total review in steps 11–12.
- [ ] Verify internal references, model-answer completeness and bando status consistency; commit `docs(vol-05): complete authority examination laboratory`.

### Task 20: Build the five promised appendices

**Files:**
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/appendice-a-atlante-comparativo-authority.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/appendice-b-tavole-procedimenti.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/appendice-c-toolkit-bando-decoder.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/appendice-d-lessico-inglese-memo.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/appendice-e-registro-aggiornamenti.md`
- Modify: `wiki/books/vol-05-authority-regolazione/index.md`

**Interfaces:**
- Consumes: frozen chapter concepts, verified source package, editorial Bible.
- Produces: five reader-visible, printable appendices not treated as numbered pipeline chapters.

- [ ] Create Appendix A with source, organs, powers, EU networks, personnel, judge and scope columns for AGCM, ARERA, AGCOM, CONSOB, Banca d'Italia, IVASS, Garante and ANAC.
- [ ] Create Appendix B with separate tables for consultation, AIR/VIR, investigation, inspection, commitments, sanctions and remedies; every non-universal term has authority and cut-off.
- [ ] Create Appendix C with complete printable Bando Decoder, subject matrix, source register, output checklist and gap diary.
- [ ] Create Appendix D with contextual regulatory English, phrase patterns and at least two full memo models linked to chapters 10 and 15.
- [ ] Create Appendix E with a printable update register containing source, act, date, scope, affected nucleus/chapter, action and verification status; state that updates are not automatic.
- [ ] Give appendices reader frontmatter, book ID `m-fc05-authority-indipendenti`, non-numbered titles and ordered `outline_section` values 60–64; keep draft/review metadata truthful until sign-off.
- [ ] Verify no appendix is empty, decorative, internally linked or dependent on dashboard access; commit `docs(vol-05): add promised operational appendices`.

### Task 21: Rebuild front matter, services promise, index, and conclusion

**Files:**
- Modify: `wiki/books/vol-05-authority-regolazione/index.md`
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/index.md`
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/21-conclusione.md`
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/planning/00-piano-editoriale.md`

**Interfaces:**
- Consumes: final chapter and appendix filenames.
- Produces: one reader front matter, accurate commercial promise, complete analytical index, genuine ending.

- [ ] Expand `Premessa` into `Come usare questo volume` with audience, prerequisites, legal/economic/mixed routes, boxes, exercises, updates and connection to VOL-01.
- [ ] Retain only digital services with a real, tested, durable destination; otherwise remove their promise without replacing it with vague future language.
- [ ] Replace `completo per outline` with a reader-facing index and keep the actual coverage matrix in planning.
- [ ] Link all fifteen chapters and five appendices with exact titles; remove stale bando and status contradictions from both indices and the old plan.
- [ ] Write `21-conclusione.md` with source–power–procedure–guarantee–output synthesis, final adaptation sequence, 30/60/90 application and a memorable close; introduce no new legal theory.
- [ ] Confirm Book Studio ends on the conclusion rather than a review note; commit `docs(vol-05): complete reader front matter and conclusion`.

### Task 22: Reconcile the module and freeze text through steps 13–16

**Files:**
- Modify when required: all M-FC05 reader files, matrix, Bible, indices.
- Create/update: step 13–16 reports under `wiki/reviews/pipeline/VOL-05/`.
- Update through CLI: `pipeline/VOL-05/run-state.json`.

**Interfaces:** Produces a blocker-free text-frozen module with one-to-one matrix/nucleus coverage.

- [ ] Add an audit that extracts all `N-FC05-CC-NN` IDs from fifteen chapters and the matrix; fail on duplicates, missing IDs, malformed prefixes, or unequal sets.
- [ ] Open step 13 and apply the fixed Revisore Editoriale Totale template across chapters and appendices: progression, duplication, terminology, voice, references, cross-chapter consistency and promised outputs.
- [ ] Open step 14 and apply every mandatory correction; rerun affected chapter gates before closing the correction report.
- [ ] Open step 15 and verify specialist claims for REMIT II, competition, DSA/DMA, financial supervision, MiCAR, DORA, privacy, ANAC, ADR and MTR-3; close every grave item.
- [ ] Manually verify text-freeze requirements at step 16 and use `--accept --note` only because the CLI reports `gate-not-implemented` and the evidence report is complete.
- [ ] Run the nucleus-set audit, coverage audit, internal-link scan and `git diff --check`; commit `docs(vol-05): freeze complete authority module`.

### Task 23: Audit and rationalize the visual system through steps 17–18

**Files:**
- Create: `wiki/books/moduli/m-fc05-authority-indipendenti/planning/04-filosofia-visiva-vol-05.md`
- Modify only when justified: figure references/captions in reader files and corresponding assets.
- Create/update: step 17–18 reports under `wiki/reviews/pipeline/VOL-05/`.
- Update through CLI: `pipeline/VOL-05/run-state.json`.

**Interfaces:** Produces a grayscale-safe, paperback-readable figure set; unused source assets remain on disk.

- [ ] Read the Canvas Design skill and write the visual philosophy before generating or editing any image.
- [ ] Open step 17 and inventory all referenced figures by chapter, didactic function, dimensions, text size, grayscale contrast and caption specificity.
- [ ] Keep approximately two or three genuinely useful figures per chapter; exclude redundant figures from reader text without deleting their source assets.
- [ ] Replace all generic repeated captions with one sentence explaining the specific cognitive function of that figure.
- [ ] Open step 18, inspect every retained figure in Book Studio at 6.69 × 9.61 inches and in reflow; correct only documented legibility or instructional failures.
- [ ] Verify no missing asset, overflow, clipped label, decorative sequence or illegible internal text; close manual gates with evidence and commit `docs(vol-05): pass visual publication audit`.

### Task 24: Pass KDP layout and page-by-page audit through steps 19–20

**Files:**
- Create/update: `wiki/reviews/pipeline/VOL-05/19-impaginazione-kdp.md`
- Create/update: `wiki/reviews/pipeline/VOL-05/20-audit-pagina-per-pagina.md`
- Create/update: VOL-05 layout artifacts under `artifacts/` as required by the scripts.
- Modify reader files only to correct demonstrated layout blockers.
- Update through CLI: `pipeline/VOL-05/run-state.json`.

**Interfaces:** Produces stable 6.69 × 9.61 inch pages and two verified ebook viewport layouts.

- [ ] Open step 19, run Book Studio layout verification for book ID `volumi/vol-05`, and record stable page count, chapters, appendices, nuclei, verification headings, images, overflow and collision diagnostics.
- [ ] Assert fifteen numbered chapters, five appendices, a conclusion, non-zero equal chapter/index nucleus counts, non-zero verification headings, zero missing assets, zero horizontal overflow and zero collisions.
- [ ] Correct orphan headings, table splits, caption separation, figure scaling, excessive blank space and final-page order; rerun until stable.
- [ ] Open step 20, render and inspect every page/contact sheet; record each corrected and accepted finding with page number and reason.
- [ ] Test ebook reflow at a narrow phone viewport and a wider tablet viewport; check heading hierarchy, table fallback, figure width, links and quiz readability.
- [ ] Close `page-fill` manually only with the final reports and stable evidence; commit `docs(vol-05): pass KDP and reflow audit`.

### Task 25: Run final review, zero-error proof, and preflight through steps 21–22

**Files:**
- Create/update: step-21 final editorial report under `wiki/reviews/pipeline/VOL-05/`.
- Create/update: step-22 preflight report under `wiki/reviews/pipeline/VOL-05/`.
- Modify reader files only for mandatory corrections.
- Update through CLI: `pipeline/VOL-05/run-state.json`.

**Interfaces:** Produces a final judgment of at least `Pubblicabile con correzioni minori`, followed by zero unresolved blockers.

- [ ] Read the complete Revisore Editoriale Totale skill, 30-point checklist and fixed report template; open step 21 and review macro, meso, micro and surface levels.
- [ ] Verify introduction, conclusion, five appendices, global redundancies, terminology, originality/attribution flags, sources, current law and reader autonomy.
- [ ] Apply mandatory findings, rerun affected chapter/module/layout gates, and repeat the final review until no grave issue remains.
- [ ] Perform the independent “zero errori” pass for typos, double words, missing words, punctuation, numbering, titles, names, dates, percentages, notes, bibliography, links and formatting.
- [ ] Open step 22 and verify front matter, index, trim, fonts, grayscale, bleed, page order, image resolution, source cut-off, ebook reflow, filenames and delivery metadata.
- [ ] Run `npm test`, `npm run typecheck`, pipeline tests, Book Studio layout/page audit and `git diff --check`; close preflight only with zero blockers and commit `docs(vol-05): pass final review and preflight`.

### Task 26: Build delivery package and stop at human sign-off

**Files:**
- Create/update according to step 23: `delivery/VOL-05/` package and manifest.
- Create/update: step-23 delivery report under `wiki/reviews/pipeline/VOL-05/`.
- Update through CLI: step 23 only in `pipeline/VOL-05/run-state.json`.
- Append through services: LocalAgentMemory and `wiki/log.md`.

**Interfaces:** Produces a versioned PDF/ebook-ready package, checksums, source commit and `ready_for_human_signoff`; leaves step 24 incomplete.

- [ ] Open step 23 and follow its rendered delivery contract exactly; export the interior PDF after page count is stable and include the ebook/reflow artifact supported by the repository.
- [ ] Create a manifest with title, volume code, edition/cut-off, trim size, bleed/colour profile, page count, files, byte sizes, checksums, source commit and non-blocking limitations.
- [ ] Verify PDF page sequence, embedded fonts, images, metadata and checksum; validate the ebook artifact or explicitly document the exact supported reflow deliverable without calling a nonexistent EPUB complete.
- [ ] Complete step 23 and run `npm run pipeline -- status VOL-05 --json`; assert every selected step through 23 is done and step 24 is the only remaining step.
- [ ] Capture LocalAgentMemory with scope `VOL-05`, route `vol-05-publishability-retrofit`, main artifacts, tests, final page count, cut-off and next step 24; append a concise `editorial_delivery` event to `wiki/log.md`.
- [ ] Commit only VOL-05 delivery, reports, run-state and the exact new memory/log append blocks with `docs(vol-05): prepare human signoff package`.
- [ ] Do not call `complete VOL-05 --step 24`, do not use `--accept` for human sign-off, and do not publish or push automatically.

## Final Verification Checklist

- [ ] `npm run pipeline -- status VOL-05 --json` reports no blocker and step 24 as the only remaining step.
- [ ] Exactly fifteen numbered chapters declare `format_version: 2`.
- [ ] Every chapter passes the current CLI word, nucleus, quiz, case, citation and referral contract.
- [ ] Chapter nucleus IDs and matrix nucleus IDs are equal, unique and non-empty.
- [ ] Appendices A–E exist, are complete and appear after chapter 15.
- [ ] The conclusion is the last substantive reader page.
- [ ] No reader body exposes `Scheda di lavoro`, `Specifica struttura madre`, `Note di review editoriale`, internal source paths or wiki links.
- [ ] MiCAR, DORA, REMIT II, DMA, SSM, AAS/ABF, Solvency II, whistleblowing burden of proof and MTR-3 are verified at the cut-off.
- [ ] Services-digital copy refers only to existing tested resources.
- [ ] Book Studio reports fifteen chapters, five appendices, non-zero nuclei and verification headings, zero missing assets, overflow and collisions.
- [ ] PDF KDP and two ebook viewports pass visual inspection.
- [ ] Final total review contains no grave open issue and the zero-error pass is recorded separately.
- [ ] `npm test` exits 0.
- [ ] `npm run typecheck` exits 0.
- [ ] `git diff --check` exits 0.
- [ ] Delivery manifest identifies source commit, cut-off, files and checksums.
- [ ] Unrelated dashboard logs and pre-existing shared-memory changes are not included in scoped commits.
- [ ] Step 24 remains incomplete until the user provides human sign-off.

