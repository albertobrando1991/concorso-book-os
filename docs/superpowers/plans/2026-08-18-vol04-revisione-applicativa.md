# VOL-04 Revisione Applicativa Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Portare il VOL-04 da bozza professionale bloccata a manoscritto reader-facing corretto, completo negli apparati e verificabile nel pipeline.

**Architecture:** Le correzioni procedono dalle fonti al testo, poi dagli apparati alla produzione. Le modifiche normative vengono consolidate in una source note; i capitoli conservano il contenuto valido ma perdono il materiale redazionale visibile. Appendici e conclusione sono file autonomi inclusi nell'assemblaggio del volume.

**Tech Stack:** Markdown Obsidian, TypeScript/Node.js, CLI pipeline, Vitest, renderer Book Studio/KDP, LocalAgentMemory.

## Global Constraints

- Non modificare manualmente `pipeline/VOL-04/run-state.json`.
- Non usare `wiki/raw/` per scrivere il testo finale.
- Non modificare file di altri volumi o eliminare modifiche preesistenti.
- Usare esclusivamente fonti ufficiali per i claim normativi ad alta mobilità.
- Il corpo reader-facing non deve contenere wikilink verso source, topic, entity, raw, planning o review.
- Non promuovere i capitoli legacy a `format_version: 2` senza retrofit completo.
- Non dichiarare superato un gate che restituisce blocker.
- Conservare voce, metodo workbook e lavoro editoriale già valido.

---

### Task 1: Baseline, inventario e fonti normative

**Files:**
- Create: `wiki/sources/vol-04-aggiornamento-normativo-2026-08-18.md`
- Modify: source note esistenti elencate nei frontmatter dei capitoli 2, 4, 8, 10 e 12
- Test: scansioni `rg` sui claim critici e controllo URL ufficiali

**Interfaces:**
- Consumes: report step 21 e fonti ufficiali.
- Produces: fonte consolidata usata dai capitoli corretti.

- [ ] Registrare per ogni claim fonte, data, stato e conseguenza editoriale.
- [ ] Collegare la nuova source note a topic, entità e capitoli coinvolti.
- [ ] Verificare che nessun claim sia sostenuto da una pagina secondaria quando esiste una fonte primaria.
- [ ] Eseguire una scansione iniziale delle occorrenze e salvare i conteggi nel report di lavorazione.

### Task 2: Correzioni normative e istituzionali P0

**Files:**
- Modify: `wiki/books/vol-04-giustizia-upp/front-matter/06-indice.md`
- Modify: `wiki/books/vol-04-giustizia-upp/modules/01-m-fc04-frontespizio-sommario.md`
- Modify: capitoli 1-5, 8, 10 e 12 di `wiki/books/moduli/m-fc04-giustizia/chapters/`

**Interfaces:**
- Consumes: source note della Task 1.
- Produces: testo privo dei tre errori critici e della formulazione privacy eccessiva.

- [ ] Sostituire la mappa DOG/DAP/DGMC/DGSIA con DAG/DOG/DIT/DAP/DGMC e ricollocare DGSIA.
- [ ] Rimuovere ogni uso vigente del D.L. 100/2026 e spiegare la decadenza solo dove didatticamente necessaria.
- [ ] Riscrivere spiegazione, tabella, casi, domande e checklist sulla copia esecutiva.
- [ ] Correggere il trattamento dei dati giudiziari nei rapporti di lavoro.
- [ ] Separare magistratura di sorveglianza, DAP, DGMC e UEPE.
- [ ] Verificare con `rg` l'assenza delle formulazioni obsolete.

### Task 3: Manoscritto reader-facing

**Files:**
- Modify: tutti i 14 capitoli di `wiki/books/moduli/m-fc04-giustizia/chapters/`
- Create temporaneamente: `scripts/.tmp-clean-vol04-reader-copy.ts`

**Interfaces:**
- Consumes: capitoli corretti della Task 2.
- Produces: corpo leggibile senza workflow interno; il frontmatter conserva la tracciabilità.

- [ ] Scrivere uno script deterministico che rimuova soltanto i blocchi `Specifica struttura madre`, `Scheda di lavoro`, `Riferimenti consolidati` e `Note di review` esterni al testo utile.
- [ ] Eseguire lo script sui 14 capitoli e rimuoverlo con `apply_patch`.
- [ ] Sostituire nel corpo i rinvii wiki necessari con riferimenti editoriali leggibili e destinazioni reali.
- [ ] Eliminare formule come “nel corpus”, “source note”, “alla verifica del” e istruzioni al redattore.
- [ ] Verificare zero heading interni proibiti e zero wikilink nel corpo post-frontmatter.

### Task 4: Appendici, strumenti, conclusione e indici

**Files:**
- Create: `wiki/books/moduli/m-fc04-giustizia/chapters/15-appendici-strumenti-finali.md`
- Create: `wiki/books/moduli/m-fc04-giustizia/chapters/16-conclusione-vol-04.md`
- Modify: front matter, indice commerciale, indice del modulo e wrapper.

**Interfaces:**
- Consumes: termini e modelli dei capitoli 1-14.
- Produces: appendici A-E, cinque strumenti finali, conclusione e collegamenti di assemblaggio.

- [ ] Creare Toolkit UPP con schede fascicolo, udienza, ricerca, cronologia e nota sintetica.
- [ ] Creare tavole per cancelleria, spese, casellario e UNEP.
- [ ] Creare mappe minorile/comunità/riparativa e penitenziario/misure/trattamento.
- [ ] Creare il ponte preciso a M-SP03 senza promettere contenuti inesistenti.
- [ ] Creare Bando Decoder, piano 30/60/90, diario errori, simulazione e griglia profilo-materia-output.
- [ ] Scrivere la conclusione e aggiornare tutti gli indici.
- [ ] Rimuovere dalla pagina servizi digitali QR e link finché non esiste una destinazione reale.

### Task 5: Copertura didattica e verifiche dei capitoli

**Files:**
- Modify: capitoli 1, 6, 7 e 11 per gli ampliamenti.
- Modify: tutti i 14 capitoli per la verifica finale.
- Modify: `wiki/books/vol-04-giustizia-upp/planning/02-matrice-copertura-didattica.md`.

**Interfaces:**
- Consumes: manoscritto pulito e appendici.
- Produces: almeno sei quiz commentati e un caso per capitolo, con evidenze nella matrice.

- [ ] Aggiungere un caso completo al capitolo 1.
- [ ] Integrare nel capitolo 6 sequenza civile, competenze, atti e controlli senza duplicare un trattato.
- [ ] Integrare nel capitolo 7 sequenza penale, fasi filtro, impugnazioni e PPT con data certa.
- [ ] Integrare nel capitolo 11 notificazioni, esecuzioni e protesti con confini di ruolo.
- [ ] Aggiungere almeno quattro quiz commentati nuovi a ciascun capitolo, raggiungendo sei complessivi.
- [ ] Aggiornare la matrice con stato ed evidenze reali, senza promozioni automatiche non verificate.
- [ ] Eseguire l'audit tramite `npx tsx scripts/audit-didactic-coverage.mjs`.

### Task 6: Proofreading e Humanizer

**Files:**
- Modify: front matter, indici, wrapper, capitoli 1-16.
- Create temporaneamente: `scripts/.tmp-normalize-vol04-text.ts`.

**Interfaces:**
- Consumes: corpus didatticamente completo.
- Produces: testo normalizzato e meno meccanico.

- [ ] Normalizzare in modo contestuale accenti, apostrofi, maiuscole, sigle e denominazioni.
- [ ] Correggere doppie parole, spaziature, forme come “una anomalia” e “uffici come giudice di pace”.
- [ ] Ridurre ripetizioni “il candidato deve”, negazioni parallele e aperture identiche.
- [ ] Eseguire il doppio prompt Humanizer: residui artificiali e revisione finale.
- [ ] Rimuovere lo script temporaneo e verificare zero pattern noti.

### Task 7: Report, audit e gate dello step 21

**Files:**
- Modify: `wiki/reviews/pipeline/VOL-04/21-vol-04.md`
- Modify tramite CLI: `pipeline/VOL-04/run-state.json`

**Interfaces:**
- Consumes: corpus corretto e verifiche delle Task 1-6.
- Produces: registro errori aggiornato con stati dimostrabili e gate rieseguito.

- [ ] Riesaminare ognuno degli ID E-001/E-014 contro il testo corrente.
- [ ] Marcare “corretto” soltanto gli errori con evidenza verificata.
- [ ] Aggiornare giudizio, limiti e numeri senza cancellare la diagnosi storica.
- [ ] Eseguire `git diff --check`, audit mirati, typecheck e test pertinenti.
- [ ] Eseguire `npm run pipeline -- complete VOL-04 --step 21 --json` e leggere l'esito JSON.

### Task 8: Export cartaceo, digitale e preflight

**Files:**
- Create: artefatti sotto `output/` o percorso previsto dal renderer.
- Modify: report step 21 con esito del preflight.

**Interfaces:**
- Consumes: volume assemblato e gate editoriale.
- Produces: PDF KDP e formato digitale supportato, con controllo documentato.

- [ ] Leggere le skill PDF/documenti prima della generazione.
- [ ] Eseguire il comando `export:volume-pdf` con il codice o slug previsto dal renderer.
- [ ] Renderizzare e controllare il PDF pagina per pagina o per campione sistematico, secondo la skill PDF.
- [ ] Verificare sommario, tabelle, link, font, margini, vedove/orfane e pagine bianche.
- [ ] Cercare un comando nativo per EPUB/DOCX; se assente, documentare il limite senza inventare l'artefatto.
- [ ] Ripetere fact-check e scansione “zero errori” sul prodotto finale.

### Task 9: Memoria e consegna

**Files:**
- Modify tramite `LocalAgentMemory`: `wiki/memory/agent/`.

**Interfaces:**
- Consumes: esiti finali di audit, gate e preflight.
- Produces: traccia sintetica riusabile e consegna verificata.

- [ ] Registrare decisioni, correzioni, blocker residui e percorsi degli artefatti.
- [ ] Verificare che non restino script temporanei.
- [ ] Verificare stato Git limitato ai file VOL-04 e preservazione delle modifiche non correlate.
- [ ] Applicare `verification-before-completion` prima di qualunque dichiarazione finale.

## Self-review del piano

- Copertura: i dieci punti richiesti dall'utente sono mappati nelle Task 1-9.
- Placeholder: nessun passaggio richiede contenuti non definiti; l'unica scelta condizionale riguarda il formato digitale, subordinato a uno strumento reale già presente.
- Coerenza: appendici e conclusione sono prodotte prima dell'aggiornamento della matrice e dell'assemblaggio; fonti precedono le correzioni; proofreading segue i cambi strutturali.
- Rischio: la suite globale non è assunta come baseline verde; le verifiche del VOL-04 restano distinguibili dai fallimenti infrastrutturali preesistenti.
