# VOL-07 M-SA02 Setting-ready Residuals Implementation Plan

> **For Codex:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Ridurre i residui interni dello step 07 con un pacchetto PICO/GRADE, fonti territoriali regionali e fonti operative TPALL, rendendo la matrice pronta per la scrittura e destinando le review umane allo step 15.

**Architecture:** Le nuove fonti entrano in sottocartelle raw già governate da `download-log.json`; source notes e planning traducono il delta documentale in copertura didattica controllata. Il CLI conserva ordine e gate; lo stato non viene modificato a mano.

**Tech Stack:** Markdown, PowerShell/curl, Node/tsx, PyPDF, pipeline CLI, LocalAgentMemory.

---

### Task 1: Baseline e isolamento

**Files:**
- Read: `pipeline/VOL-07/run-state.json`
- Read: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`

- [ ] Verificare worktree collegato, branch e stato dirty senza modificare file esistenti.
- [ ] Richiamare `LocalAgentMemory` nello scope `pipeline-volume-vol-07-m-sa02`.
- [ ] Confermare via CLI che step 07 è il solo step bloccato e che nessun downstream è in corso.

### Task 2: Fonti territorio e continuità

**Files:**
- Modify: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenziale/download-log.json`
- Create: `wiki/sources/territorio-cot-continuita-pdta-persona-fragile-toscana.md`
- Modify: `wiki/sources/presa-in-carico-cronicita-pdta-territorio-agenas.md`

- [ ] Scaricare i tre PDF ufficiali Toscana: accesso/COT, continuità ospedale-territorio, PDTA persona fragile.
- [ ] Verificare firma PDF, pagine, byte e SHA-256.
- [ ] Registrare il corpus raw senza attribuirgli valore di procedura aziendale universale.
- [ ] Creare la source note e collegarla alla base nazionale AGENAS.

### Task 3: Fonti TPALL per emissioni

**Files:**
- Modify: `wiki/raw/m-sa02-professioni-sanitarie/tecnica-tpall/download-log.json`
- Create: `wiki/sources/tpall-emissioni-convogliate-bat-ael-metodi-snpa-arpa.md`
- Modify: `wiki/sources/tpall-aia-campionamenti-acque-aria-suolo-rifiuti-alimenti.md`

- [ ] Scaricare SNPA 25/2020, SNPA 49/2023 e pubblicazione tecnica SNPA 2025 sulle emissioni odorigene.
- [ ] Catturare le pagine ARPA Lombardia e ARPAV che mantengono i repertori dei metodi.
- [ ] Verificare byte, hash, pagine e contenuto.
- [ ] Distinguere sicurezza/organizzazione, BAT-AEL, odori e norme tecniche applicabili.

### Task 4: Pacchetto esercizi PICO/GRADE

**Files:**
- Create: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/08-pacchetto-esercizi-pico-grade-applicabilita.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/07-piano-chiusura-review-esterne-m-sa02.md`

- [ ] Costruire almeno 5 esercizi su PICO, disegno, certezza, forza e applicabilità.
- [ ] Separare traccia per il candidato e chiave editoriale.
- [ ] Inserire controlli di versione, setting, preferenze, equità, fattibilità e limiti professionali.
- [ ] Integrare il pacchetto nella review `REV-EPI` senza inventare firma o verbale.

### Task 5: Matrice, audit e indici

**Files:**
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [ ] Aggiornare soltanto le righe SA02-03, SA02-05 e SA02-07 e i relativi blocker.
- [ ] Classificare `completo` ciò che dispone di teoria, applicazione non esecutiva e verifica progettata; mantenere `review_required` e rinviare firme/prove specialistiche allo step 15.
- [ ] Collegare i nuovi artefatti negli indici pertinenti.

### Task 6: Verifica e memoria

**Files:**
- Modify: `wiki/memory/agent/`
- CLI-owned: `pipeline/VOL-07/run-state.json`

- [ ] Verificare tutti i `download-log.json`, esistenza, byte e SHA-256.
- [ ] Eseguire `npm test`, `npm run typecheck` e `git diff --check`.
- [ ] Rieseguire `complete VOL-07 --step 07 --module M-SA02 --json` senza override e avanzare solo se il gate passa realmente.
- [ ] Registrare una traccia sintetica in `LocalAgentMemory` e nel log editoriale.
- [ ] Non eseguire commit, merge o push senza richiesta esplicita dell’utente.
