# VOL-10 Format 2 Retrofit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convertire i 13 capitoli M-TR03 al formato 2, ripetere i gate editoriali e portare VOL-10 fino allo step 23 con il solo sign-off umano dello step 24 residuo.

**Architecture:** Il CLI resta l'unico proprietario dello stato. Un comando `reopen` testato invalida gli step dipendenti; ogni capitolo attraversa 08-12 come unità autonoma, poi il modulo attraversa 13-18 e il volume 19-23. Il Book Studio valida il grafo dei nuclei e l'impaginato effettivo.

**Tech Stack:** TypeScript 5.7, Node.js 24, Vitest, CLI pipeline, Markdown/YAML, LocalAgentMemory, Book Studio Next.js, Playwright.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-10/run-state.json`.
- Ogni capitolo dichiara `format_version: 2` e `dati_operativi: []` salvo dati realmente censiti.
- Almeno 5 nuclei `N-TR03-CC-NN`, 600 parole per nucleo o soglia CLI più severa, 6 quiz commentati e 1 caso ragionato.
- Preservare testo e tracciabilità esistenti; niente contenuti finali da `raw/`.
- Zero nuclei `parziale`, `solo-nominato` o `mancante`.
- Nessun commit include modifiche estranee preesistenti.
- Lo step 24 non viene chiuso dall'agente.

---

### Task 1: Comando CLI `reopen`

**Files:**
- Modify: `src/pipeline/cli/commands.ts`
- Modify: `scripts/pipeline/cli.ts`
- Modify: `src/pipeline/state/types.ts` se necessario per l'evidenza di riapertura
- Test: `tests/pipeline/commands.test.ts` o nuovo `tests/pipeline/reopen.test.ts`

**Interfaces:**
- Consumes: run-state, volume spec e ordinamento degli step esistenti.
- Produces: `pipeline reopen VOL-10 --from-step 08 --module M-TR03 [--chapter 01] --note <testo> --json`.

- [ ] **Step 1: Scrivere test di rifiuto senza `--note`**

Creare un fixture con step 08-23 conclusi e verificare che il comando non muti lo stato senza motivazione.

- [ ] **Step 2: Eseguire il test rosso**

Run: `npx vitest run tests/pipeline/reopen.test.ts`
Expected: FAIL perché `reopen` non è riconosciuto.

- [ ] **Step 3: Scrivere test di riapertura capitolo e invalidazione dipendenze**

Verificare che `--chapter 01 --from-step 08` riapra 08-12 del capitolo 01 e gli step modulo/volume dipendenti, lasciando intatti gli altri capitoli.

- [ ] **Step 4: Implementare parsing, validazione e transazione atomica**

Riutilizzare lettura/scrittura e selezione target già usate da `complete`; registrare autore, data, nota ed evidenza senza scritture parziali.

- [ ] **Step 5: Verificare test e help**

Run: `npx vitest run tests/pipeline/reopen.test.ts tests/pipeline/steps.test.ts`
Expected: PASS.

Run: `npm run pipeline -- help`
Expected: mostra `reopen` e i flag richiesti.

- [ ] **Step 6: Commit isolato**

`git add` soltanto CLI e test; commit `feat(pipeline): add controlled reopen command`.

### Task 2: Riapertura controllata VOL-10 e baseline

**Files:**
- Modify via CLI: `pipeline/VOL-10/run-state.json`
- Create: `wiki/reviews/pipeline/VOL-10/retrofit-format-2-baseline.md`

**Interfaces:**
- Consumes: comando `reopen` della Task 1 e report Book Studio step 19.
- Produces: run-state coerente e baseline verificabile 93 pagine/0 nuclei/0 verifiche.

- [ ] **Step 1: Richiamare LocalAgentMemory scope VOL-10**
- [ ] **Step 2: Eseguire `reopen` per M-TR03 dagli step 08-23 con nota esplicita**
- [ ] **Step 3: Salvare baseline con conteggi per capitolo**

Per ogni capitolo registrare parole, heading, nuclei, verifiche, quiz, casi, source refs e riga matrice.

- [ ] **Step 4: Verificare status JSON**

Run: `npm run pipeline -- status VOL-10 --json`
Expected: primo target riaperto `08` capitolo 01, nessun target in conflitto.

- [ ] **Step 5: Commit isolato**

Commit `chore(vol-10): reopen pipeline for format 2 retrofit` includendo solo run-state e baseline.

### Task 3: Retrofit capitolo 01 — profili e prove

**Files:**
- Modify: `wiki/books/moduli/m-tr03-tecnico-ingegneristico/chapters/01-concorso-tecnico-pa-profili-prove.md`
- Modify: matrice M-TR03
- Modify/Create: planning e report step 08-12 del target 01

**Interfaces:** Produces nuclei `N-TR03-01-01`…`N-TR03-01-05+` e verifica commentata.

- [ ] Aprire step 08 e aggiornare il piano sul testo reale.
- [ ] Eseguire `next` step 09 prima di modificare il capitolo.
- [ ] Mappare profili, enti/prove, lettura bando, matrice profilo-materia-prova e confini cross-family in almeno cinque nuclei.
- [ ] Aggiungere `▣ Verifica` con sei quiz commentati e caso bando tecnico.
- [ ] Completare 09-12, correggere ogni blocker e verificare `git diff --check`.
- [ ] Commit `docs(vol-10): retrofit chapter 01 to format 2`.

### Task 4: Retrofit capitolo 02 — ufficio tecnico e atti

**Files:** capitolo 02, matrice, planning e report 08-12.

**Interfaces:** Produces nuclei su ruolo dell'ufficio, procedimento, sopralluogo, relazione/verbale, responsabilità e output.

- [ ] Eseguire ciclo 08-12 con snapshot prima della scrittura.
- [ ] Costruire almeno cinque nuclei conformi e una verifica con sei quiz commentati più caso istruttorio.
- [ ] Verificare rinvio preciso al nucleo comune VOL-01.
- [ ] Eseguire gate, diff check e commit `docs(vol-10): retrofit chapter 02 to format 2`.

### Task 5: Retrofit capitolo 03 — scienza e tecnica delle costruzioni

**Files:** capitolo 03, matrice, planning e report 08-12.

- [ ] Eseguire ciclo 08-12.
- [ ] Nuclei: modello strutturale; azioni/equilibrio; tensione/deformazione; resistenza/rigidezza/stabilità; materiali/durabilità; uso in prova.
- [ ] Verificare formule, segni e unità sulle fonti consolidate senza introdurre calcolo professionale.
- [ ] Aggiungere verifica e caso ragionato; eseguire gate e commit `docs(vol-10): retrofit chapter 03 to format 2`.

### Task 6: Retrofit capitolo 04 — NTC, sismica e geotecnica

**Files:** capitolo 04, matrice, planning e report 08-12.

- [ ] Eseguire ciclo 08-12.
- [ ] Nuclei: quadro NTC; vita/classe/stati limite; azioni e verifica; rischio sismico; terreno/fondazioni; esistenti/collaudo.
- [ ] Conservare cut-off NTC 2018, Circolare 2019 e modifiche 2023.
- [ ] Verifica con quiz commentati e caso edificio esistente; gate e commit `docs(vol-10): retrofit chapter 04 to format 2`.

### Task 7: Retrofit capitoli 05-06 — territorio ed edilizia

**Files:** capitoli 05-06, matrice, planning e report 08-12 per entrambi.

- [ ] Capitolo 05: nuclei su livelli di piano, attuazione/standard, conformità, vincoli, espropriazione e paesaggio.
- [ ] Capitolo 05: verifica e caso piano-intervento; chiudere 08-12.
- [ ] Capitolo 06: nuclei su categorie, regimi/titoli, SUE, stato legittimo/agibilità, vigilanza/regolarizzazione.
- [ ] Capitolo 06: verifica e caso edilizio; chiudere 08-12.
- [ ] Ricontrollare disciplina nazionale/territoriale, diff e commit separati per capitolo.

### Task 8: Retrofit capitoli 07-10 — ciclo dell'opera

**Files:** capitoli 07-10, matrice, planning e report 08-12.

- [ ] Capitolo 07: bisogno-DIP-PFTE-esecutivo-verifica-validazione; ciclo 08-12 e commit.
- [ ] Capitolo 08: RUP-DL-CSE, consegna, controllo, modifiche/sospensioni, sicurezza; ciclo 08-12 e commit.
- [ ] Capitolo 09: ultimazione, collaudi, regolare esecuzione, manutenzione/gestione; ciclo 08-12 e commit.
- [ ] Capitolo 10: prezzi/computo, capitolato, misure/documenti, SAL/conto finale, riserve; ciclo 08-12 e commit.
- [ ] Per ciascuno: almeno cinque nuclei, sei quiz commentati, caso ragionato e zero soglie mobili non verificate.

### Task 9: Retrofit capitoli 11-12 — infrastrutture e dati

**Files:** capitoli 11-12, matrice, planning e report 08-12.

- [ ] Capitolo 11: rete/opera, rischio, censimento/ispezione, classe di attenzione, valutazione, monitoraggio/decisione.
- [ ] Verificare decreto CSLP 413/2025 e Istruzioni ANSFISA 4 agosto 2025; ciclo 08-12 e commit.
- [ ] Capitolo 12: BIM, ACD/interoperabilità, GIS, rilievo, catasto, patrimonio/decisione.
- [ ] Verificare art. 43/Allegato I.9, RNDT e fonti catastali; ciclo 08-12 e commit.

### Task 10: Retrofit capitolo 13 — laboratorio

**Files:** capitolo 13, matrice, planning e report 08-12.

- [ ] Eseguire ciclo 08-12.
- [ ] Organizzare nuclei per lettura consegna, piano output, scritto tecnico, scritto-grafico/computo, sopralluogo/relazione, orale e Diario errori.
- [ ] Conservare almeno otto forme di output e simulazione finale; aggiungere verifica commentata conforme.
- [ ] Gate, diff e commit `docs(vol-10): retrofit chapter 13 to format 2`.

### Task 11: Riconciliazione del grafo e revisione modulo

**Files:** matrice, indice M-TR03, Bibbia, report step 13-15.

- [ ] Verificare unicità e sequenza di tutti gli ID `N-TR03-*`.
- [ ] Controllare che ogni promessa della matrice punti a testo e verifica reali.
- [ ] Eseguire step 13 con Revisore Editoriale Totale.
- [ ] Applicare step 14; per modifiche sostanziali riaprire il capitolo interessato.
- [ ] Eseguire step 15 con fonti ufficiali e zero esiti pendenti.
- [ ] Testare gate e commit `docs(vol-10): reconcile format 2 nucleus graph`.

### Task 12: Nuovo text freeze e sistema visivo

**Files:** manifest 16, filosofia/report immagini 17-18.

- [ ] Generare nuovi SHA-256 e sostituire il manifest precedente preservandone la traccia.
- [ ] Verificare manualmente condizioni step 16 e chiudere con `--accept --note` solo se conformi.
- [ ] Rieseguire 17-18 con Canvas Design; non creare asset se non necessari.
- [ ] Commit `docs(vol-10): freeze format 2 module`.

### Task 13: Book Studio step 19 e audit pagina step 20

**Files:** report e artefatti Book Studio 19-20; eventuali correzioni layout mirate.

- [ ] Avviare Book Studio su porta dedicata.
- [ ] Eseguire layout verifier con `BOOK_STUDIO_BOOK_IDS=volumi/vol-10`.
- [ ] Richiedere `chapters=13`, `nuclei > 0`, `nuclei === indexNuclei`, `verificationHeadings > 0`, zero overflow/collisioni.
- [ ] Eseguire auditor pagina per pagina in modalità write con conteggio stabile.
- [ ] Ispezionare contact sheet e pagine segnalate; correggere e rieseguire.
- [ ] Chiudere 19-20 con evidenze e commit `docs(vol-10): pass format 2 KDP audit`.

### Task 14: Revisione finale e preflight step 21-23

**Files:** report editoriale step 21, preflight step 22, pacchetto consegna step 23.

- [ ] Eseguire Revisore Editoriale Totale sull'impaginato, checklist 30 punti e copertura integrale.
- [ ] Correggere ogni errore grave/medio e ripetere i controlli impattati.
- [ ] Eseguire preflight KDP: formato, margini, font, pagine, tabelle, immagini, indice e numerazione.
- [ ] Preparare manifest di consegna, fonti, cut-off, limiti e hash.
- [ ] Chiudere 21-23 soltanto con zero blocker.

### Task 15: Verifica finale e handoff umano

**Files:** run-state VOL-10, memoria locale e riepilogo finale.

- [ ] Leggere `verification-before-completion`.
- [ ] Run: `npm run typecheck` — Expected: PASS.
- [ ] Run: `npx vitest run tests/pipeline tests/book-preview.test.ts tests/book-studio-page-audit-core.test.ts tests/editorial-typography.test.ts` — Expected: PASS.
- [ ] Run: `git diff --check` — Expected: nessun output.
- [ ] Run: `npm run pipeline -- status VOL-10 --json` — Expected: unico target residuo step 24.
- [ ] Catturare la traccia con LocalAgentMemory.
- [ ] Consegnare all'utente il pacchetto `ready_for_human_signoff`, senza chiudere lo step 24.

## Plan Self-Review

- Copertura della specifica: CLI, 13 capitoli, modulo, visuale, Book Studio, preflight e handoff sono assegnati a task verificabili.
- Nessun placeholder o attività rinviata senza criterio.
- Gli ID, i comandi e gli stati prodotti sono coerenti fra task.
