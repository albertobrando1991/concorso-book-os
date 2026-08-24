# VOL-01, VOL-03, VOL-05, VOL-10 e VOL-11 Publication Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Portare VOL-01, VOL-03, VOL-05, VOL-10 e VOL-11 fino a un candidato di pubblicazione completo, lasciando aperta soltanto la conferma umana finale e senza modificare VOL-06.

**Architecture:** Il CLI della pipeline resta l'unica autorita per stato, ordine e gate. Il lavoro editoriale usa i sorgenti consolidati del wiki, applica i controlli a livello capitolo, modulo e volume, quindi produce PDF e pacchetti riproducibili in `delivery/<VOL>/candidate/`. Gli stati non vengono mai modificati a mano.

**Tech Stack:** Markdown/Obsidian wiki, TypeScript/Node.js, CLI pipeline, Book Studio/Playwright, PDF KDP, LocalAgentMemory.

**Spec:** `wiki/templates/prompt-staff-revisione-completa-volumi.md`

## Global Constraints

- VOL-06 e tutti i suoi artefatti sono fuori perimetro e non devono essere modificati.
- Lo step 24 resta aperto: e l'unico passaggio umano.
- Ogni step si apre con `npm run pipeline -- next <VOL> --json` e si chiude solo dopo il relativo gate.
- Nessun contenuto finale deriva direttamente da `wiki/raw/`; norme e dati provengono da source note consolidate o fonti ufficiali trasformate in source note.
- Il corpo lettore non contiene wikilink interni, note di review, prompt, piani o riferimenti al sistema.
- Nessun nucleo `parziale`, `solo-nominato` o `mancante` puo raggiungere il text freeze.
- Nessun errore grave o medio puo essere rinviato allo step 24.
- I file locali gia modificati in `wiki/log.md` e `wiki/memory/agent/` restano preservati e fuori dallo staging editoriale.

---

### Task 1: Baseline e protezione del perimetro

**Files:**
- Create: `docs/superpowers/plans/2026-08-21-volumes-publication-completion.md`
- Inspect: `pipeline/<VOL>/run-state.json`
- Inspect: `wiki/books/**/planning/00-scheda-pipeline.md`

**Interfaces:**
- Consumes: stato Git e `origin/main` gia integrato.
- Produces: baseline dei file VOL-06 e matrice degli step iniziali.

- [ ] Eseguire `npm run pipeline -- doctor --json` e richiedere esito `ok: true`.
- [ ] Salvare l'elenco e gli hash dei file sotto `pipeline/VOL-06`, `wiki/books/volumi/vol-06-*`, `wiki/books/moduli/m-ir0*` e `wiki/reviews/pipeline/VOL-06` per il confronto finale.
- [ ] Interrogare `status --json` per VOL-01, 03, 05, 10 e 11.
- [ ] Richiamare LocalAgentMemory per ciascun volume prima del primo step LLM.

### Task 2: Riallineamento VOL-11

**Files:**
- Modify through CLI: `pipeline/VOL-11/run-state.json`
- Verify: `wiki/reviews/pipeline/VOL-11/12-*.md`, `13-*.md`, `14-*.md`, `15-*.md`, `21-vol-11.md`, `22-vol-11.md`, `23-vol-11-delivery.md`
- Verify: `delivery/VOL-11/candidate/*`

**Interfaces:**
- Consumes: report e pacchetto gia presenti.
- Produces: run-state coerente con gli artefatti, con solo step 24 aperto.

- [ ] Verificare hash, report, manifest di freeze, PDF e manifest della consegna.
- [ ] Aprire in ordine gli step pendenti con `next --json`, leggere ogni prompt generato e rieseguire il gate pertinente.
- [ ] Chiudere gli step soltanto se l'evidenza esistente e la nuova verifica soddisfano il contratto.
- [ ] Confermare con `status VOL-11 --json` che l'unico eventuale step residuo sia 24.

### Task 3: Completamento VOL-10

**Files:**
- Modify: `wiki/books/moduli/m-tr03-tecnico-ingegneristico/chapters/*.md`
- Create/modify: `wiki/reviews/pipeline/VOL-10/15-*.md`, `16-*.md`, `17-*.md`, `18-*.md`, `19-*.md`, `20-*.md`, `21-*.md`, `22-*.md`, `23-*.md`
- Create: `delivery/VOL-10/candidate/*`
- Modify through CLI: `pipeline/VOL-10/run-state.json`

**Interfaces:**
- Consumes: report step 13-14 e source note tecniche consolidate.
- Produces: audit specialistico chiuso, text freeze, PDF KDP e delivery.

- [ ] Rieseguire lo step 15 verificando NTC, edilizia, urbanistica, contratti, sicurezza, DL, collaudo, ponti, BIM, GIS, catasto, formule e unita.
- [ ] Applicare tutte le correzioni obbligatorie e chiudere zero errori gravi/medi.
- [ ] Eseguire step 16 e produrre manifest di freeze.
- [ ] Eseguire step 17-20: filosofia visiva, audit asset, impaginazione e controllo di tutte le pagine.
- [ ] Eseguire step 21-23: revisione finale, preflight e pacchetto di consegna.
- [ ] Lasciare aperto esclusivamente lo step 24.

### Task 4: Ricertificazione VOL-01

**Files:**
- Create: scheda pipeline canonica per VOL-01 e relativo run-state tramite CLI.
- Modify as required: `wiki/books/il-metodo-bando/chapters/*.md`, front matter, indice e planning.
- Create: report pipeline VOL-01 e completamento `delivery/VOL-01/candidate/*`.

**Interfaces:**
- Consumes: matrice con zero nuclei bloccanti e candidato PDF recuperato.
- Produces: perimetro cartaceo/digitale congelato, review flags chiusi, PDF ispezionato e delivery completa.

- [ ] Definire nella scheda il perimetro editoriale effettivo senza includere il Ricettario digitale nel cartaceo se non dichiarato.
- [ ] Inizializzare e sincronizzare la pipeline esclusivamente via CLI.
- [ ] Chiudere le marcature `review_required` mediante audit normativo, linguistico e tecnico automatico documentato.
- [ ] Eseguire revisione trasversale, correzioni, audit specialistico e freeze.
- [ ] Riesportare e ispezionare tutte le pagine del PDF.
- [ ] Eseguire revisione finale, preflight e completare report, changelog, limiti, manutenzione, versione e manifest.

### Task 5: Completamento VOL-03

**Files:**
- Modify: scheda VOL-03 e run-state soltanto tramite `sync`/CLI.
- Modify: capitoli 11-15 M-FC01 e 19 capitoli/appendici M-FC03.
- Create: report mancanti step 08-16 e 21-23.
- Create: `delivery/VOL-03/candidate/*`.

**Interfaces:**
- Consumes: M-FC02 gia congelato e capitoli professionali esistenti.
- Produces: M-FC01 e M-FC03 completi, revisionati e congelati; volume consegnabile.

- [ ] Correggere la scheda affinche `planning/00-piano-editoriale.md` non sia trattato come capitolo e sincronizzare il run-state.
- [ ] Portare M-FC01 capitoli 11-15 attraverso step 08-12 mancanti.
- [ ] Portare tutti i 19 file M-FC03 attraverso step 08-12, con retrofit formato 2 quando richiesto dal contratto.
- [ ] Eseguire step 13-16 per M-FC01 e M-FC03.
- [ ] Eseguire step 21-23 e produrre PDF e delivery.
- [ ] Lasciare aperto esclusivamente lo step 24 se previsto dalla scheda.

### Task 6: Revisione strutturale VOL-05

**Files:**
- Create: scheda pipeline VOL-05 e run-state tramite CLI.
- Modify: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/*.md`, indice e planning.
- Create: introduzione, conclusione e appendici soltanto se mantenute nell'indice approvato.
- Create: report pipeline e `delivery/VOL-05/candidate/*`.

**Interfaces:**
- Consumes: report finale del 18 agosto con 48 correzioni aperte.
- Produces: volume senza apparato interno, con copertura completa, voce naturale e pacchetto pubblicabile.

- [ ] Trasformare il report del 18 agosto in matrice operativa e chiudere ogni voce grave/obbligatoria.
- [ ] Riallineare indice e promesse; produrre o rimuovere appendici e servizi non esistenti.
- [ ] Integrare i nuclei normativi e tecnici mancanti, inclusi MiCAR, DORA, pagamenti, ABF/AAS, REMIT e whistleblowing.
- [ ] Rimuovere note di review e wikilink interni dal corpo lettore.
- [ ] Applicare Humanizer a struttura seriale, aperture e didascalie ripetute.
- [ ] Eseguire i cicli 08-16 previsti dalla scheda e chiudere tutti i blocker.
- [ ] Eseguire revisione finale, PDF, preflight e delivery.

### Task 7: Verifica globale e handoff

**Files:**
- Verify: tutti i file modificati e i pacchetti `delivery/VOL-{01,03,05,10,11}/candidate/`.
- Verify unchanged: tutti i file VOL-06 censiti nella Task 1.

**Interfaces:**
- Consumes: cinque candidati completati.
- Produces: evidenze finali e diff selettivo pronto per commit.

- [ ] Eseguire audit di copertura per ciascun volume.
- [ ] Eseguire test completi, typecheck, build e `git diff --check`.
- [ ] Verificare hash e apertura dei PDF, font, trim, pagine e manifest.
- [ ] Confrontare gli hash VOL-06 con la baseline e richiedere zero modifiche.
- [ ] Controllare che nessun file locale estraneo sia incluso.
- [ ] Riportare eventuali limiti reali senza dichiarare verdi controlli non eseguiti.
