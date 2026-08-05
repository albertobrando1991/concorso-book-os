# VOL-07 M-SA02 Capitolo 03 Progressivo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Estendere la fase C di VOL-07 al solo capitolo 03 di M-SA02 e completarne in ordine gli step 08-12, lasciando differite le review professionali dello step 15.

**Architecture:** La scheda pipeline resta l'unica fonte dichiarativa del nuovo target; `pipeline sync` riconcilia il run-state e deve aggiungere esattamente cinque step. Ogni step editoriale produce il proprio artefatto canonico, supera il gate previsto dal CLI e conserva la separazione fra testo didattico non esecutivo e verifiche professionali esterne.

**Tech Stack:** Markdown wiki con frontmatter YAML, TypeScript, Vitest, CLI `tsx`, ConcorsoBook OS Pipeline, `LocalAgentMemory`.

## Global Constraints

- Lavorare nel worktree `C:\Users\info\OneDrive\Desktop\concorso-book-os\.worktrees\vol-07-pipeline-start`.
- Leggere `wiki/AGENTS.md` e `.agents/skills/pipeline-volume/SKILL.md` prima dell'esecuzione.
- Richiamare `LocalAgentMemory` prima di generare il nuovo testo editoriale.
- Usare sempre `--json` per interpretare l'esito dei comandi pipeline.
- Non modificare mai manualmente `pipeline/VOL-07/run-state.json`; l'unico writer autorizzato è il CLI.
- Conservare le fasi globali `[A, B, C]`; M-SA02 resta in `A,B,C`, gli altri moduli in `A,B`.
- Dichiarare soltanto i capitoli 01 e 03 di M-SA02; il capitolo 02 e i capitoli 04-10 restano fuori da questo ciclo.
- Non attivare le fasi D, E o F.
- Non simulare review giuridiche, cliniche o professionali: restano assegnate allo step 15.
- Non inserire procedure cliniche esecutive, attribuzioni professionali non supportate o regole nazionali ricavate da prassi locali.
- Non duplicare il nucleo comune del Metodo BANDO e del VOL-01.
- Non creare commit intermedi: consegna e commit restano riservati allo step 23.
- Preservare tutte le modifiche già presenti nel worktree condiviso.

---

### Task 1: Dichiarare il capitolo 03 con TDD e sincronizzare la pipeline

**Files:**
- Modify: `tests/pipeline/vol-07-spec.test.ts`
- Modify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`
- CLI-managed: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: `loadVolumeSpec({ wikiRoot, volumeCode })` e `buildStepDrafts(spec, phases)`.
- Produces: la dichiarazione del capitolo `chapters/03-discipline-professionali-autonomia-responsabilita.md` e cinque step pending con ID 08-12.

- [ ] **Step 1: Richiamare memoria e stato prima di intervenire**

Run:

```powershell
npm run pipeline -- doctor --json
npm run pipeline -- status VOL-07 --json
npm run pipeline -- next VOL-07 --json
```

Expected:

- `doctor` restituisce tutti i check con esito positivo;
- `status` mostra `done: 22`, nessun blocker e nessuno step in corso;
- `next` restituisce `"step": null`.

Richiamare inoltre `LocalAgentMemory` con scope `pipeline-volume` e query:

```text
VOL-07 M-SA02 estensione progressiva capitolo 03 discipline professionali autonomia responsabilità deontologia ciclo 08-12
```

Applicare soltanto preferenze e decisioni pertinenti; le source note restano canoniche per i contenuti.

- [ ] **Step 2: Scrivere il test rosso sulla scheda reale**

In `tests/pipeline/vol-07-spec.test.ts`, importare anche:

```ts
import { buildStepDrafts } from "../../src/pipeline/steps/build-steps"
```

Sostituire l'aspettativa `chapters` di M-SA02 con:

```ts
chapters: [
  {
    number: "01",
    file: "chapters/01-mappa-profili-e-prove.md",
    matrix: "planning/02-matrice-copertura-didattica.md",
    expectedStatus: "completo"
  },
  {
    number: "03",
    file: "chapters/03-discipline-professionali-autonomia-responsabilita.md",
    matrix: "planning/02-matrice-copertura-didattica.md",
    expectedStatus: "completo"
  }
]
```

Nello stesso test, dopo il controllo sui moduli, aggiungere:

```ts
const chapter03Target =
  "moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md"
const chapter03Steps = buildStepDrafts(loaded.spec, ["C"]).filter(
  (step) => step.target === chapter03Target
)

expect(chapter03Steps.map((step) => step.key)).toEqual([
  `08:${chapter03Target}`,
  `09:${chapter03Target}`,
  `10:${chapter03Target}`,
  `11:${chapter03Target}`,
  `12:${chapter03Target}`
])
```

- [ ] **Step 3: Eseguire il test e verificare il fallimento atteso**

Run:

```powershell
npx vitest run tests/pipeline/vol-07-spec.test.ts
```

Expected: FAIL perché la scheda reale dichiara ancora soltanto il capitolo 01.

- [ ] **Step 4: Estendere la scheda con la sola riga 03**

In `00-scheda-pipeline.md`, aggiungere alla tabella `Capitoli M-SA02`:

```markdown
| 03 | chapters/03-discipline-professionali-autonomia-responsabilita.md | planning/02-matrice-copertura-didattica.md | completo | Secondo ciclo progressivo della fase C; nucleo Discipline professionali specifiche |
```

Aggiornare i due paragrafi descrittivi affinché dichiarino esplicitamente:

```markdown
La fase C procede in modo progressivo sui capitoli 01 e 03 di M-SA02. Il capitolo 02 non viene dichiarato perché il nucleo comune del Metodo BANDO resta nel VOL-01 e non deve essere duplicato.

I capitoli 01 e 03 di M-SA02 sono dichiarati esplicitamente; gli altri moduli continuano a derivare gli eventuali capitoli dagli scaffold presenti in `<module id>/chapters/`. La dichiarazione autorizza il ciclo 08-12 soltanto sui target indicati e non abilita ancora i capitoli successivi o le fasi D-F.
```

- [ ] **Step 5: Eseguire i test mirati e verificare il verde**

Run:

```powershell
npx vitest run tests/pipeline/vol-07-spec.test.ts tests/pipeline/build-steps.test.ts
```

Expected: PASS; il test reale vede i capitoli 01 e 03 e il builder emette cinque step per il nuovo target.

- [ ] **Step 6: Sincronizzare attraverso il CLI**

Run:

```powershell
npm run pipeline -- sync VOL-07 --json
```

Expected payload:

```json
{
  "ok": true,
  "command": "sync",
  "added": [
    "08:moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md",
    "09:moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md",
    "10:moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md",
    "11:moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md",
    "12:moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md"
  ],
  "dropped": [],
  "specChanged": true
}
```

Se `added` o `dropped` differiscono, fermarsi e correggere scheda o test prima di avviare lo step 08.

- [ ] **Step 7: Verificare l'ordine senza modificare lo stato a mano**

Run:

```powershell
npm run pipeline -- status VOL-07 --json
npm run pipeline -- next VOL-07 --json
```

Expected: 22 step done, 5 pending, nessun blocker; `next` assegna lo step 08 al capitolo 03.

- [ ] **Step 8: Controllare il diff del task**

Run:

```powershell
git diff --check
git diff -- tests/pipeline/vol-07-spec.test.ts wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md pipeline/VOL-07/run-state.json
```

Expected: nessun errore whitespace e nessuna modifica al run-state diversa dalla riconciliazione prodotta da `sync`.

---

### Task 2: Step 08 — Progettare il capitolo 03

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa02-03.md`
- Read: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Read: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/04-bibbia-del-volume.md`
- Read: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/01-mappa-profili-e-prove.md`

**Interfaces:**
- Consumes: riga `Discipline professionali specifiche`, Bibbia VOL-07, capitolo 01 e source note consolidate.
- Produces: un piano editoriale approvato manualmente per il target del capitolo 03; non crea ancora il capitolo.

- [ ] **Step 1: Ottenere dal CLI il prompt canonico dello step 08**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step `08`, target esatto del capitolo 03, gate `chapter-plan` e percorso report sotto `wiki/reviews/pipeline/VOL-07/`.

- [ ] **Step 2: Leggere le fonti assegnate dalla matrice**

Usare almeno queste source note:

```text
wiki/sources/profili-professionali-infermiere-ostetrica-fisioterapista-tpall.md
wiki/sources/ordinamento-professioni-sanitarie-leggi-42-251-43-3.md
wiki/sources/codici-deontologici-infermiere-ostetrica-fisioterapista-tpall.md
wiki/sources/sicurezza-cure-responsabilita-consenso-leggi-24-219.md
wiki/sources/profilo-oss-dpcm-25-marzo-2025.md
wiki/sources/attuazione-regionale-oss-lombardia-2025.md
wiki/sources/attuazione-regionale-oss-emilia-romagna-veneto-2025.md
wiki/sources/bandi-rappresentativi-m-sa02-professioni-sanitarie-2025-2026.md
wiki/sources/bandi-rappresentativi-oss-2025-2026.md
```

Registrare nel piano quali affermazioni sostengono, quali aspetti sono mobili e quali controlli restano allo step 15.

- [ ] **Step 3: Scrivere il piano operativo**

Il report deve contenere:

```markdown
# Piano operativo — M-SA02, capitolo 03

Target: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`.

## Esito dell'assegnazione

La matrice assegna al capitolo il nucleo completo **Discipline professionali specifiche**. Il testo confronterà infermiere, ostetrica, fisioterapista, TPALL e OSS per fonte del profilo, autonomia, responsabilità, deontologia, limiti e collaborazione multiprofessionale.

## Matrice riga per riga

| Nucleo | Fonti | Sezioni | Applicazione | Verifica | Review differita |
| --- | --- | --- | --- | --- | --- |
| Discipline professionali specifiche | profili; ordinamento; codici deontologici; responsabilità e consenso; profilo e attuazioni OSS; corpus dei bandi | quadro comune; cinque profili; autonomia e responsabilità; deontologia; collaborazione; confini | confronto fra profili e caso deontologico non esecutivo | quiz, domanda orale, caso con griglia e checklist | review giuridica e cinque review professionali allo step 15 |
```

Completare lo stesso file con:

- contenuti già consolidati e informazioni mobili;
- duplicazioni da evitare rispetto al capitolo 01 e al VOL-01;
- struttura H1/H2/H3;
- budget di 5.000-6.000 parole, circa 15-18 pagine KDP;
- apparati didattici;
- fonti per sezione;
- controlli umani richiesti;
- criterio di approvazione che non anticipi lo step 15.

- [ ] **Step 4: Verificare manualmente il piano**

Controllare che:

- ogni voce della riga di matrice abbia una sezione, un'applicazione e una verifica;
- OSS sia distinto dalle professioni sanitarie ordinistiche;
- l'autonomia non sia descritta come assenza di limiti o di collaborazione;
- i casi siano non esecutivi;
- le differenze regionali OSS e le procedure di setting siano dichiarate mobili;
- il file target del capitolo non esista ancora.

- [ ] **Step 5: Eseguire il gate e chiuderlo con accettazione motivata**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 08 --module M-SA02 --chapter 03 --json
```

Expected: blocker `gate-not-implemented` per `chapter-plan`.

Solo dopo la verifica manuale, run:

```powershell
npm run pipeline -- complete VOL-07 --step 08 --module M-SA02 --chapter 03 --accept --note "Piano operativo salvato in wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa02-03.md; il nucleo Discipline professionali specifiche è collegato a fonti, sezioni, applicazione, verifica, budget e review step 15; il capitolo non è stato ancora creato." --json
```

Expected: step 08 `done`; nessun altro step cambia stato.

---

### Task 3: Step 09 — Scrivere il capitolo con il writer professionale

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`
- Read: `wiki/reviews/pipeline/VOL-07/08-piano-capitolo-m-sa02-03.md`
- Read: le nove source note elencate nel Task 2

**Interfaces:**
- Consumes: piano approvato dello step 08 e source note consolidate.
- Produces: capitolo Markdown completo, tracciabile e conforme al gate `chapter-lint`.

- [ ] **Step 1: Ottenere il prompt dello step 09**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step `09`, gate `chapter-lint`, target esatto del capitolo 03.

- [ ] **Step 2: Caricare la skill di scrittura e richiamare la memoria pertinente**

Usare `concorso-book-professional-writer` prima di generare il testo. Richiamare `LocalAgentMemory` con scope `manual-writer` e query:

```text
Scrittura M-SA02 capitolo 03 discipline professionali autonomia responsabilità deontologia collaborazione multiprofessionale infermiere ostetrica fisioterapista TPALL OSS
```

Non trasferire nel capitolo claim normativi provenienti soltanto dalla memoria.

- [ ] **Step 3: Creare il frontmatter completo**

Usare questa identità e questi riferimenti:

```yaml
---
id: chapter-m-sa02-03-discipline-professionali-autonomia-responsabilita
type: chapter
title: "Discipline professionali: autonomia, responsabilità e deontologia"
status: draft
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/profili-professionali-infermiere-ostetrica-fisioterapista-tpall"
  - "sources/ordinamento-professioni-sanitarie-leggi-42-251-43-3"
  - "sources/codici-deontologici-infermiere-ostetrica-fisioterapista-tpall"
  - "sources/sicurezza-cure-responsabilita-consenso-leggi-24-219"
  - "sources/profilo-oss-dpcm-25-marzo-2025"
  - "sources/attuazione-regionale-oss-lombardia-2025"
  - "sources/attuazione-regionale-oss-emilia-romagna-veneto-2025"
  - "sources/bandi-rappresentativi-m-sa02-professioni-sanitarie-2025-2026"
  - "sources/bandi-rappresentativi-oss-2025-2026"
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie", "il-metodo-bando"]
book_id: m-sa02-professioni-sanitarie
chapter_number: "03"
draft_stage: written
review_required: true
canonical: true
tags: ["m-sa02", "professioni-sanitarie", "autonomia", "responsabilita", "deontologia", "pipeline-step-09"]
---
```

Impostare `created_at`, `updated_at` e `last_compiled_from` con i valori reali dell'esecuzione e con il piano dello step 08, la matrice e le source note effettivamente usate.

- [ ] **Step 4: Scrivere la struttura editoriale concordata**

Il corpo deve avere un solo H1:

```markdown
# Discipline professionali: autonomia, responsabilità e deontologia
```

Sviluppare in ordine:

1. obiettivo e mappa `fonte → profilo → autonomia → responsabilità → collaborazione`;
2. quadro comune delle professioni sanitarie e distinzione dell'OSS;
3. infermiere: profilo, responsabilità, relazione con equipe e supporto;
4. ostetrica: profilo, autonomia, responsabilità e limiti del setting;
5. fisioterapista: valutazione funzionale, programma professionale e collaborazione;
6. TPALL: prevenzione, vigilanza, atti e responsabilità tecnico-professionale;
7. OSS: profilo nazionale, attuazione regionale e rapporto con i professionisti;
8. deontologia: principi comuni e differenze documentate tra codici;
9. collaborazione multiprofessionale, consegne, escalation e tracciabilità;
10. caso deontologico comparato non clinico-esecutivo;
11. domanda da commissario, domanda-trappola ed errore tipico;
12. quiz, mini-esercizio comparativo, griglia di soluzione e checklist finale;
13. riferimenti consolidati e controlli differiti.

Ogni sezione deve distinguere:

- regola sostenuta dalla fonte;
- applicazione al concorso;
- elemento dipendente da bando, regione, setting o review professionale;
- confine con i capitoli 04-10, che non va anticipato con procedure.

- [ ] **Step 5: Eseguire il gate automatico**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 09 --module M-SA02 --chapter 03 --json
```

Expected:

- un solo H1;
- nessun salto nella gerarchia;
- frontmatter con `source_refs` e `draft_stage`;
- nessun segnaposto o meta-commento da agente;
- zero blocker.

Correggere il capitolo e ripetere lo stesso gate finché `passed` è `true`.

- [ ] **Step 6: Completare lo step 09**

Run:

```powershell
npm run pipeline -- complete VOL-07 --step 09 --module M-SA02 --chapter 03 --json
```

Expected: step 09 `done`; step 10 diventa il successivo.

---

### Task 4: Step 10 — Verificare la copertura didattica

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/10-controllo-copertura-m-sa02-03.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Read: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`

**Interfaces:**
- Consumes: capitolo scritto e riga `Discipline professionali specifiche`.
- Produces: audit criterio per criterio e collegamento della riga di matrice all'evidenza dello step 10.

- [ ] **Step 1: Ottenere il prompt dello step 10**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step `10`, gate `coverage`, target capitolo 03.

- [ ] **Step 2: Auditare il capitolo sugli undici criteri**

Nel report usare questa tabella:

```markdown
| Criterio | Evidenza nel capitolo | Esito |
| --- | --- | --- |
| Definizione | sezione che definisce profilo, autonomia, responsabilità e deontologia | coperto |
| Funzione | relazione tra fonti professionali, decisione e responsabilità | coperto |
| Inquadramento | quadro ordinamentale e distinzione OSS | coperto |
| Elementi | cinque profili, fonti, limiti, collaborazione e tracciabilità | coperto |
| Distinzioni | autonomia/isolamento; responsabilità/colpa automatica; professione/OSS; nazionale/regionale | coperto |
| Conseguenze | effetti su risposta orale, caso e scelta professionale | coperto |
| Esempio/caso | caso deontologico comparato non esecutivo | coperto |
| Uso nella prova | domanda orale, confronto e caso motivato | coperto |
| Errore tipico | sovrapposizione dei profili o generalizzazione locale | coperto |
| Verifica | quiz, esercizio, griglia e checklist | coperto |
| Fonti | source note nel frontmatter e riferimenti consolidati | coperto |
```

Ogni evidenza deve citare il titolo reale della sezione del capitolo, non la descrizione generica riportata sopra.

- [ ] **Step 3: Registrare il delta e i controlli differiti**

Nel report aggiungere:

```markdown
| Nucleo | Stato prima | Intervento | Stato dopo |
| --- | --- | --- | --- |
| Discipline professionali specifiche | completo | Audit integrale sul testo del capitolo 03 e collegamento dell'evidenza alla matrice | completo |
```

Elencare separatamente le verifiche dello step 15: confini professionali, codici correnti, applicazione regionale OSS, attribuzioni nel setting e correttezza dei casi.

- [ ] **Step 4: Collegare la matrice al report**

Nella colonna `Note` della sola riga `Discipline professionali specifiche`, aggiungere:

```markdown
Copertura verificata nello [[reviews/pipeline/VOL-07/10-controllo-copertura-m-sa02-03|step 10]].
```

Non modificare lo stato `completo` delle altre otto righe.

- [ ] **Step 5: Eseguire il gate e completare**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 10 --module M-SA02 --chapter 03 --json
```

Expected: `passed: true`, nessuna riga `parziale`, `solo-nominato` o `mancante`, nessun rinvio privo di destinazione.

Poi:

```powershell
npm run pipeline -- complete VOL-07 --step 10 --module M-SA02 --chapter 03 --json
```

Expected: step 10 `done`; step 11 diventa il successivo.

---

### Task 5: Step 11 — Umanizzare senza alterare fonti o norme

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`
- Create: `wiki/reviews/pipeline/VOL-07/11-humanizer-m-sa02-03.md`
- CLI-created snapshot: `artifacts/pipeline/VOL-07/11/moduli-m-sa02-professioni-sanitarie-chapters-03-discipline-professionali-autonomia-responsabilita-md/before.md`

**Interfaces:**
- Consumes: capitolo dopo lo step 10 e snapshot creato da `next`.
- Produces: prosa più naturale con wikilink, `source_refs` e riferimenti normativi invariati.

- [ ] **Step 1: Avviare lo step e verificare lo snapshot**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step `11`, gate `citation-guard`; il file `before.md` esiste nel percorso dichiarato sopra.

- [ ] **Step 2: Applicare la skill `humanizer`**

Eseguire due passate:

1. rimuovere aperture astratte, enfasi generica, parallelismi rigidi, formule meta-editoriali e ripetizioni;
2. rileggere per ritmo, naturalezza, varietà sintattica e tono professionale.

Preservare integralmente:

- significato tecnico;
- nomi dei profili;
- cautele normative;
- struttura didattica;
- domande, soluzioni e checklist;
- frontmatter e `source_refs`;
- wikilink e riferimenti normativi.

- [ ] **Step 3: Scrivere il report Humanizer**

Il report deve documentare:

```markdown
# Humanizer — M-SA02, capitolo 03

Target: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`.

Snapshot precedente all'intervento: `artifacts/pipeline/VOL-07/11/moduli-m-sa02-professioni-sanitarie-chapters-03-discipline-professionali-autonomia-responsabilita-md/before.md`.

## Prima passata

## Seconda passata anti-AI

## Elementi preservati

## Controlli umani ancora richiesti
```

Descrivere soltanto interventi realmente applicati e ribadire che lo Humanizer non sostituisce le review dello step 15.

- [ ] **Step 4: Eseguire il citation guard e completare**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 11 --module M-SA02 --chapter 03 --json
```

Expected: `passed: true`; zero wikilink, `source_refs` o riferimenti normativi rimossi o introdotti rispetto allo snapshot.

Poi:

```powershell
npm run pipeline -- complete VOL-07 --step 11 --module M-SA02 --chapter 03 --json
```

Expected: step 11 `done`; step 12 diventa il successivo.

---

### Task 6: Step 12 — Revisione editoriale totale e coerenza di modulo

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/00-piano-editoriale.md`
- Create: `wiki/reviews/pipeline/VOL-07/12-moduli-m-sa02-professioni-sanitarie-chapters-03-discipline-professionali-autonomia-responsabilita-md.md`

**Interfaces:**
- Consumes: capitolo umanizzato, matrice, Bibbia, piano editoriale, indice e capitolo 01.
- Produces: capitolo corretto, indice coerente e report accettato dal gate `review-report`.

- [ ] **Step 1: Ottenere il prompt dello step 12**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected: step `12`, gate `review-report` e percorso report esatto.

- [ ] **Step 2: Applicare la skill `revisore-editoriale-totale`**

Revisionare:

- struttura H1/H2/H3;
- coerenza con capitolo 01, matrice e Bibbia;
- terminologia per profilo, albo, autonomia, responsabilità, deontologia, collaborazione e OSS;
- accuratezza delle distinzioni senza sostituire la review professionale;
- chiarezza di esempi, caso, quiz, soluzioni e checklist;
- ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura e uniformità Markdown;
- rinvii puntuali al VOL-01 e al Metodo BANDO;
- separazione tra testo pubblicabile nel ciclo e verifiche obbligatorie prima del congelamento.

Applicare direttamente le correzioni oggettive. Registrare come `review umana` le questioni che richiedono un professionista o un giurista.

- [ ] **Step 3: Aggiornare indice e piano editoriale**

In `index.md`, aggiungere dopo il capitolo 01:

```markdown
- [[books/moduli/m-sa02-professioni-sanitarie/chapters/03-discipline-professionali-autonomia-responsabilita|Capitolo 03 - Discipline professionali: autonomia, responsabilità e deontologia]]
```

In `chapters/00-piano-editoriale.md`, registrare che:

- i capitoli 01 e 03 hanno completato il ciclo 08-12;
- sette nuclei restano da trasformare nei capitoli 04-10;
- le review esterne dello step 15 restano aperte;
- nessuna fase D-F è stata attivata.

- [ ] **Step 4: Scrivere il report nella struttura fissa**

Usare questi titoli:

```markdown
# Report editoriale — Discipline professionali: autonomia, responsabilità e deontologia

## 1. Sintesi editoriale
## 2. Punti applicati della checklist
## 3. Tabella errori
## 4. Osservazioni per capitolo
## 5. Coerenza globale
## 6. Contenuto da verificare
## 7. Suggerimenti facoltativi (non errori)
## 8. Priorità degli interventi
## 9. Giudizio di pubblicabilità
## 10. Limiti di questa revisione
```

La tabella errori deve avere esattamente:

```markdown
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
```

Gli errori certi gravi o medi devono risultare `applicato`; le verifiche normative e professionali non accertate devono risultare `review umana`. Il giudizio deve usare la formula:

```markdown
**Pubblicabile con correzioni minori** nel ciclo editoriale corrente, fermo restando il divieto di congelamento prima delle review obbligatorie dello step 15.
```

- [ ] **Step 5: Eseguire il gate e completare**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 12 --module M-SA02 --chapter 03 --json
```

Expected: `passed: true`, report presente, tabella valida e zero errori gravi aperti.

Poi:

```powershell
npm run pipeline -- complete VOL-07 --step 12 --module M-SA02 --chapter 03 --json
```

Expected: step 12 `done`.

---

### Task 7: Verifica finale, stato pipeline e memoria locale

**Files:**
- Verify: tutti i file modificati nei Task 1-6
- CLI-managed: `pipeline/VOL-07/run-state.json`
- Memory-managed: `wiki/memory/agent/`

**Interfaces:**
- Consumes: ciclo 08-12 completato.
- Produces: evidenza verificabile che lo scope dichiarato è concluso e traccia sintetica in memoria.

- [ ] **Step 1: Ricontrollare il gate preparatorio M-SA02**

Run:

```powershell
npm run pipeline -- gate VOL-07 --step 07 --module M-SA02 --json
```

Expected: `passed: true`; la matrice conserva nove nuclei `completo` e nessun blocker preparatorio.

- [ ] **Step 2: Eseguire i test mirati**

Run:

```powershell
npx vitest run tests/pipeline/vol-07-spec.test.ts tests/pipeline/build-steps.test.ts tests/pipeline/run-state.test.ts
```

Expected: PASS.

- [ ] **Step 3: Eseguire suite e typecheck**

Run:

```powershell
npm test
npm run typecheck
```

Expected: exit code 0 per entrambi.

- [ ] **Step 4: Verificare integrità del diff**

Run:

```powershell
git diff --check
git status -sb
```

Expected: nessun errore whitespace; tutte le modifiche restano non committate e appartengono allo scope già presente nel worktree.

- [ ] **Step 5: Verificare lo stato finale del CLI**

Run:

```powershell
npm run pipeline -- status VOL-07 --json
npm run pipeline -- next VOL-07 --json
```

Expected per `status`:

```json
{
  "counts": {
    "done": 27
  },
  "blocked": [],
  "inProgress": []
}
```

Expected per `next`: `"step": null`.

I payload reali possono includere altri campi, ma non devono contenere step pending, blocker o fasi D-F.

- [ ] **Step 6: Registrare la traccia con `LocalAgentMemory`**

Run:

```powershell
npx tsx -e 'import { LocalAgentMemory } from "./src/server/memory/local-agent-memory"; const memory = LocalAgentMemory.fromConfig(); const result = await memory.captureConversation({ scope: "pipeline-volume", route: "vol-07-m-sa02-capitolo-03-progressivo", messages: [{ role: "user", content: "Procedere in ordine con il solo capitolo 03 M-SA02, completando il ciclo pipeline 08-12 senza attivare le fasi D-F." }], reply: "VOL-07 M-SA02 capitolo 03 completato negli step 08-12; test, typecheck, gate e stato finale verificati; review professionali esterne conservate allo step 15.", metadata: { volume: "VOL-07", module: "M-SA02", chapter: "03", stepsCompleted: 5 } }); console.log(JSON.stringify({ conversationId: result.conversationId, atoms: result.atoms.length }))'
```

Expected: `conversationId` non vuoto e almeno un atomo registrato.

- [ ] **Step 7: Preparare il riepilogo di consegna senza commit**

Riportare:

- capitolo e quattro report creati;
- cinque step aggiunti e completati;
- esito dei gate 08-12;
- conteggio test e typecheck;
- stato pipeline finale;
- ID della traccia memoria;
- review esterne ancora aperte allo step 15;
- conferma che nessun commit e nessuna fase D-F sono stati creati.
