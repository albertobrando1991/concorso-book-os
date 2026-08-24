# VOL-06 M-IR02 Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completare e verificare M-IR02 — Università e AFAM, rendendolo ammissibile ai gate di modulo della pipeline VOL-06.

**Architecture:** Il CLI assegna un solo step e capitolo alla volta. Per ciascuno dei capitoli 09–12 l'agente legge il prompt generato, richiama LocalAgentMemory, consolida eventuali fonti mancanti, redige il testo reader-facing e chiude soltanto i gate superati. Dopo l'ultimo capitolo procede alla revisione trasversale M-IR02, alle correzioni, all'audit e al text freeze.

**Tech Stack:** Markdown, ConcorsoBook OS wiki, `npm run pipeline`, TypeScript gates, fonti primarie istituzionali.

**Spec:** `docs/superpowers/specs/2026-08-20-vol06-completamento-moduli-design.md`

## Global Constraints

- Non modificare manualmente `pipeline/VOL-06/run-state.json`.
- Conservare il testo per il lettore solo in `wiki/books/moduli/m-ir02-universita-afam/chapters/`.
- Usare source notes consolidate, topic/entity pages e matrice; non usare raw sources per scrittura finale.
- Prima di ogni produzione LLM richiamare `LocalAgentMemory`; al termine registrare una traccia sintetica.
- Superare i gate in ordine; un `gate-not-implemented` richiede verifica manuale documentata e `--accept --note`.

---

### Task 1: Capitolo 09 — Biblioteche, cataloghi e open access

**Files:**
- Modify: `wiki/books/moduli/m-ir02-universita-afam/chapters/09-biblioteche-cataloghi-open-access.md`
- Create: `wiki/reviews/pipeline/VOL-06/12-moduli-m-ir02-universita-afam-chapters-09-biblioteche-cataloghi-open-access-md.md`

- [ ] Eseguire `npm run pipeline -- next VOL-06 --json`, leggere il prompt generato e richiamare LocalAgentMemory per il capitolo.
- [ ] Verificare matrice, piano capitolo, source notes e fonti ufficiali; consolidare solo le lacune decisive.
- [ ] Redigere o integrare il capitolo conforme a contratto e chiudere i gate 09–12 mediante CLI.

### Task 2: Capitolo 10 — Orientamento, placement e terza missione

**Files:**
- Modify: `wiki/books/moduli/m-ir02-universita-afam/chapters/10-orientamento-placement-terza-missione.md`
- Create: `wiki/reviews/pipeline/VOL-06/12-moduli-m-ir02-universita-afam-chapters-10-orientamento-placement-terza-missione-md.md`

- [ ] Ripetere il ciclo CLI, fonti consolidate, redazione e gate 09–12 sul target assegnato.

### Task 3: Capitolo 11 — AFAM: ordinamento e amministrazione

**Files:**
- Modify: `wiki/books/moduli/m-ir02-universita-afam/chapters/11-afam-ordinamento-amministrazione.md`
- Create: `wiki/reviews/pipeline/VOL-06/12-moduli-m-ir02-universita-afam-chapters-11-afam-ordinamento-amministrazione-md.md`

- [ ] Ripetere il ciclo CLI, fonti consolidate, redazione e gate 09–12 sul target assegnato.

### Task 4: Capitolo 12 — Laboratorio per i quattro profili

**Files:**
- Modify: `wiki/books/moduli/m-ir02-universita-afam/chapters/12-laboratorio-quattro-profili.md`
- Create: `wiki/reviews/pipeline/VOL-06/12-moduli-m-ir02-universita-afam-chapters-12-laboratorio-quattro-profili-md.md`

- [ ] Ripetere il ciclo CLI, fonti consolidate, redazione e gate 09–12 sul target assegnato.

### Task 5: Freeze M-IR02

**Files:**
- Create: `wiki/reviews/pipeline/VOL-06/13-moduli-m-ir02-universita-afam.md`
- Create: `wiki/reviews/pipeline/VOL-06/14-moduli-m-ir02-universita-afam.md`
- Create: `wiki/reviews/pipeline/VOL-06/15-moduli-m-ir02-universita-afam.md`

- [ ] Completare gli step 13–16 tramite i prompt CLI, correggendo ogni blocker prima del passaggio successivo.
- [ ] Verificare matrice di copertura, rinvii a VOL-01, non duplicazione B-PA, aggiornamento normativo, report di revisione e text freeze.

### Task 6: Handoff verificato

- [ ] Eseguire `npm run pipeline -- status VOL-06 --json` e confermare che il prossimo target appartiene alla tranche M-IR03.
- [ ] Registrare la traccia LocalAgentMemory della tranche e aggiornare questo piano con gli esiti effettivi.
