# M-FC02 Fiscalità internazionale ACFI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Trasformare la fiscalità internazionale ACFI da nucleo `solo-nominato` a contenuto teorico autonomo e verificato nel capitolo 5 di M-FC02.

**Architecture:** Il bando ufficiale determina il perimetro; le fonti ufficiali vengono conservate nei raw e sintetizzate in una source note canonica; soltanto la source note alimenta il testo editoriale. Capitolo, matrice e report passano attraverso revisioni indipendenti prima di commit e push.

**Tech Stack:** Markdown/Obsidian Wiki, fonti ufficiali AE/Normattiva/Finanze/OCSE/UE, PowerShell, Git, validatore `npm run audit:coverage`.

## Global Constraints

- Perimetro selettivo ACFI: residenza, stabile organizzazione, convenzioni, doppia imposizione, transfer pricing, operazioni infragruppo, rischio e tax control framework.
- Nessun capitolo 5C: integrazione nel capitolo 5 dopo l'adempimento collaborativo.
- Nessun claim editoriale deriva direttamente da `wiki/raw/`.
- Nessuna aliquota, soglia, termine o lista mobile priva di verifica ufficiale puntuale.
- Preservare tutte le modifiche preesistenti nel worktree.
- Il nucleo diventa `completo` soltanto dopo review normativa ed editoriale indipendente.

---

### Task 1: Perimetro ACFI e corpus ufficiale

**Files:**
- Read: `wiki/raw/m-fc02-agenzie-fiscali/ae-avviso-350-funzionari-acfi-2025.html`
- Read: `wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md`
- Create: fonti immutabili pertinenti in `wiki/raw/m-fc02-agenzie-fiscali/`
- Create: `wiki/sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18.md`

**Interfaces:**
- Consumes: programma ACFI ufficiale e corpus normativo vigente.
- Produces: source note canonica con perimetro, mappa istituti, limiti e riferimenti utilizzabili dal writer.

- [ ] **Step 1: Estrarre il programma ufficiale**

Individuare nel bando ACFI le materie e le attività effettivamente richieste; registrare le formulazioni testuali in appunti di audit senza trasformarle direttamente in testo editoriale.

- [ ] **Step 2: Verificare fonti primarie aggiornate**

Consultare esclusivamente fonti ufficiali per: artt. 2, 73, 110 e 162 TUIR; convenzioni e modello OCSE per funzione e struttura; disciplina ufficiale del transfer pricing; documentazione infragruppo e profili di rischio pertinenti. Usare il web perché la vigenza al 18 luglio 2026 è temporalmente instabile.

- [ ] **Step 3: Acquisire i raw mancanti**

Salvare ogni documento ufficiale nel percorso raw con slug descrittivo, senza modificare file raw già presenti. Per ogni acquisizione registrare URL, data della versione e data di audit.

- [ ] **Step 4: Scrivere la source note consolidata**

La nota deve contenere almeno: esito audit; perimetro ACFI; gerarchia delle fonti; residenza; stabile organizzazione; convenzioni/doppia imposizione; transfer pricing; documentazione e rischio; raccordo con TCF; metodo del caso; limiti e review; raw refs e link consolidati.

- [ ] **Step 5: Verificare e revisionare la fonte**

Controllare frontmatter, raw refs, wikilink, UTF-8 e `git diff --check`; sottoporre la nota a review indipendente articolo-specifica. Correggere tutti i finding gravi e medi prima del commit.

- [ ] **Step 6: Commit della fonte**

```powershell
git add -- wiki/sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18.md <raw-esatti-creati>
git commit -m "docs: consolidate M-FC02 international tax sources"
```

Atteso: commit contenente soltanto source note e raw ufficiali ACFI.

---

### Task 2: Integrazione didattica nel capitolo 5

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md`

**Interfaces:**
- Consumes: `[[sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18]]` approvata.
- Produces: blocco editoriale ACFI autonomo nel capitolo 5.

- [ ] **Step 1: Fotografare il diff preesistente**

Eseguire `git diff -- <capitolo-05>` e conservare l'evidenza che il file è già modificato, così da distinguere il nuovo blocco dalle revisioni pregresse e non cancellarle.

- [ ] **Step 2: Aggiornare il frontmatter**

Aggiungere source/topic/entity pertinenti, `companion_to: il-metodo-bando`, data di aggiornamento e source note in `last_compiled_from`, senza alzare arbitrariamente confidence o stato complessivo.

- [ ] **Step 3: Sostituire il richiamo nominale con teoria Livello 3**

Inserire dopo l'adempimento collaborativo: mappa delle fonti; criteri di collegamento e residenza; stabile organizzazione; convenzioni e doppia imposizione; transfer pricing/libera concorrenza; operazioni infragruppo, documentazione e rischio; raccordo con TCF e attività dell'ufficio.

- [ ] **Step 4: Inserire apparato applicativo**

Sviluppare il caso guida società residente–impresa collegata–presenza estera con sequenza fatti → qualificazione → fonti → rischio → istruttoria → output. Aggiungere risposta da commissario, trappole, mini-esercizio risolto, quiz ragionati, errori e checklist.

- [ ] **Step 5: Verifica editoriale indipendente**

Il revisore deve controllare autonomia, progressione, accuratezza, promessa-contenuto, mancata duplicazione dei capitoli 4/6/11, tracciabilità, link, frontmatter, encoding e assenza di dati mobili inventati.

- [ ] **Step 6: Commit del capitolo**

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale.md
git commit -m "docs: complete M-FC02 international tax coverage"
```

Atteso: commit limitato al capitolo 5, inclusivo e preservativo delle revisioni pregresse già presenti nel file.

---

### Task 3: Governance della copertura ACFI

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/00-piano-editoriale.md` only if the ACFI destination is not already precise.

**Interfaces:**
- Consumes: capitolo 5 approvato e source note ACFI.
- Produces: stato di copertura coerente e conteggi verificabili.

- [ ] **Step 1: Aggiornare la destinazione analitica**

Collegare la voce ACFI al capitolo 5 e nominare gli istituti realmente coperti, senza promettere l'intera fiscalità internazionale.

- [ ] **Step 2: Aggiornare la riga della matrice**

Compilare fonte, collocazione, teoria, caso, output, verifica e review. Passare da `solo-nominato` a `completo` soltanto se tutti i campi sono sostenuti dal testo approvato.

- [ ] **Step 3: Ricalcolare i totali**

Atteso dopo approvazione: 80 nuclei = 63 `completo` + 17 `parziale`; 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`; 17 blocker.

- [ ] **Step 4: Aggiornare il report**

Chiudere E05 e il relativo punto prioritario; mantenere esplicitamente lo stato non pubblicabile per i 17 nuclei parziali e non alterare altri finding.

- [ ] **Step 5: Revisionare e committare**

Verificare conteggi, link, assenza di riferimenti stale e coerenza del giudizio; ottenere review indipendente.

```powershell
git add -- <file-governance-effettivamente-modificati>
git commit -m "docs: update M-FC02 ACFI coverage status"
```

---

### Task 4: Gate finale e pubblicazione

**Files:**
- Read: tutti i file modificati nei Task 1-3
- Update through project workflow: memoria locale e log soltanto con strumenti canonici disponibili

**Interfaces:**
- Consumes: tre deliverable approvati.
- Produces: branch `main` verificato e sincronizzato.

- [ ] **Step 1: Eseguire i controlli finali**

```powershell
npm run audit:coverage
git diff --check
git log --oneline origin/main..HEAD
```

Atteso per M-FC02: `80 righe, 63 complete, 17 blocker, 0 warning`. Gli eventuali blocker VOL-03 restano fuori perimetro.

- [ ] **Step 2: Controllare lo staging e il worktree**

Accertare che nessun file estraneo sia incluso nei commit e che tutte le modifiche non pertinenti dell'utente restino presenti e intatte.

- [ ] **Step 3: Registrare la traccia agentica**

Usare `LocalAgentMemory` se tecnicamente disponibile; in caso contrario registrare il limite senza inventare una memoria parallela e senza usare la memoria come fonte normativa.

- [ ] **Step 4: Pubblicare**

```powershell
git push origin main
```

Atteso: `origin/main` avanzato fino all'ultimo commit ACFI, con 17 blocker M-FC02 residui dichiarati.
