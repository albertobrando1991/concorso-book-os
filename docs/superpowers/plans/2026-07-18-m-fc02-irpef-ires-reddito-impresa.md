# M-FC02 IRPEF, IRES e reddito d'impresa Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Portare a Livello 3 il nucleo M-FC02 su soggetti IRPEF/IRES, categorie reddituali e reddito d'impresa attraverso una divisione funzionale tra capitoli 4, 6 e 11.

**Architecture:** Una source note articolo-specifica consolida il TUIR vigente al 18 luglio 2026. Il capitolo 4 assume la responsabilità del quadro sistematico; il capitolo 6 sviluppa categorie e determinazione; il capitolo 11 resta la destinazione delle applicazioni contabili. Ogni deliverable supera review indipendente prima del commit.

**Tech Stack:** Markdown/Obsidian Wiki, Normattiva e fonti ufficiali fiscali, PowerShell, Git, validatore `npm run audit:coverage`.

## Global Constraints

- Nessun nuovo capitolo: divisione funzionale tra capitoli 4, 6 e 11.
- Il capitolo 4 non replica la determinazione analitica delle singole categorie.
- Il capitolo 6 non duplica scritture ed esercizi contabili articolati del capitolo 11.
- Nessun claim editoriale deriva direttamente da `wiki/raw/`.
- Aliquote, scaglioni, soglie, importi e regimi mobili non entrano nel corpo stabile senza verifica ufficiale puntuale.
- Preservare tutte le modifiche preesistenti nel worktree.
- Il nucleo passa a `completo` soltanto dopo review normativa ed editoriale indipendente di entrambi i capitoli e dei rinvii al capitolo 11.

---

### Task 1: Corpus TUIR articolo-specifico

**Files:**
- Read: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-917-1986-tuir.html`
- Read: `wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md`
- Read: `wiki/sources/contabilita-aziendale-bilancio-reddito-impresa-aggiornamento-2026-07-18.md`
- Create: `wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md`
- Create: nuovi raw ufficiali soltanto se necessari per integrare o sostituire la versione TUIR già acquisita.

**Interfaces:**
- Consumes: TUIR ufficiale vigente e source notes fiscali/contabili esistenti.
- Produces: source note canonica utilizzabile dai writer dei capitoli 4 e 6.

- [ ] **Step 1: Verificare versione e perimetro del TUIR**

Separare data di consultazione, espressione vigente e ultimo aggiornamento dell'atto. Verificare le parti necessarie su soggetti IRPEF/IRES, reddito complessivo e categorie, determinazione delle categorie, reddito d'impresa e raccordo civilistico-fiscale.

- [ ] **Step 2: Costruire la mappa articolo-istituto**

La nota deve mappare almeno: soggetti/passività IRPEF e IRES; categorie dell'art. 6; reddito complessivo e sequenza deduzioni–imponibile–imposta–detrazioni; redditi fondiari, capitale, dipendente, autonomo, impresa e diversi; principi e componenti essenziali del reddito d'impresa. Ogni riferimento articolo-specifico deve essere verificato sulla versione auditata.

- [ ] **Step 3: Scrivere la source note consolidata**

Inserire frontmatter canonico, esito audit, perimetro, mappa normativa, definizioni e distinzioni, raccordo con contabilità, limiti sui dati mobili, metodo dei casi, raw refs e link consolidati.

- [ ] **Step 4: Eseguire controlli e review indipendente**

Verificare frontmatter, raw refs, wikilink, UTF-8 e `git diff --check`. Il revisore controlla articoli, completezza selettiva, distinzioni tra categorie e prudenza sui dati mobili.

- [ ] **Step 5: Commit isolato**

```powershell
git add -- wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md <eventuali-raw-esatti>
git commit -m "docs: consolidate M-FC02 income tax sources"
```

Atteso: soltanto source note ed eventuali raw ufficiali.

---

### Task 2: Quadro sistematico nel capitolo 4

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md`

**Interfaces:**
- Consumes: `[[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]` approvata.
- Produces: quadro di sistema e rinvii responsabili, senza determinazione analitica duplicata.

- [ ] **Step 1: Fotografare il diff preesistente**

Registrare stat e hash del file prima dell'intervento per preservare revisioni pregresse.

- [ ] **Step 2: Aggiornare il frontmatter**

Aggiungere source/topic/entity e `last_compiled_from` pertinenti, mantenendo invariati confidence e stato complessivo salvo diversa review.

- [ ] **Step 3: Integrare il quadro IRPEF/IRES**

Spiegare soggetti, reddito complessivo, deduzioni, imponibile, imposta lorda e detrazioni; presentare le sei categorie e la funzione della classificazione; distinguere fonte, categoria e criterio di determinazione; introdurre risultato civilistico e reddito fiscale.

- [ ] **Step 4: Inserire rinvii e verifica**

Collegare con anchor reali i blocchi responsabili dei capitoli 6 e 11. Aggiungere una verifica risolta e un errore tipico senza duplicare casi e determinazione dettagliata.

- [ ] **Step 5: Review e commit**

Controllare progressione, autonomia nel perimetro, accuratezza, non duplicazione, link, encoding e diff. Ottenere review indipendente.

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
git commit -m "docs: strengthen M-FC02 income tax framework"
```

---

### Task 3: Categorie e determinazione nel capitolo 6

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
- Read: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md`

**Interfaces:**
- Consumes: source note approvata e quadro sistematico del Task 2.
- Produces: disciplina selettiva Livello 3, casi ed esercizi risolti.

- [ ] **Step 1: Fotografare il diff preesistente e aggiornare il frontmatter**

Registrare stat/hash della baseline; aggiungere source e `last_compiled_from` senza cancellare revisioni esistenti.

- [ ] **Step 2: Sviluppare le sei categorie**

Per fondiari, capitale, dipendente, autonomo, impresa e diversi coprire definizione, funzione, elementi, distinzioni, determinazione selettiva, conseguenze, esempio, prova, errore e verifica.

- [ ] **Step 3: Sviluppare IRES e reddito d'impresa**

Spiegare soggetti IRES, struttura del reddito, derivazione, competenza, inerenza, imputazione, variazioni fiscali e componenti positivi/negativi essenziali. Usare rinvio preciso al capitolo 11 per scritture e applicazioni contabili.

- [ ] **Step 4: Inserire apparato applicativo**

Creare caso di classificazione IRPEF, caso IRES risultato civilistico–imponibile, esercizio deduzione/detrazione, quiz categorie/soggetti, risposta orale, trappole, errori e checklist. Gli eventuali numeri sono dati didattici, non parametri correnti.

- [ ] **Step 5: Review e commit**

Verificare copertura Livello 3, soluzioni, accuratezza, non duplicazione del capitolo 11, rinvii, frontmatter, encoding e diff; ottenere review indipendente.

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
git commit -m "docs: complete M-FC02 IRPEF and IRES coverage"
```

---

### Task 4: Governance della copertura redditi

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md` only if destinations are not already precise.
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`

**Interfaces:**
- Consumes: Tasks 1-3 approvati.
- Produces: stato e conteggi coerenti con la copertura reale.

- [ ] **Step 1: Verificare destinazioni analitiche**

Collegare, se necessario, quadro sistematico al capitolo 4, categorie/determinazione al 6 e applicazioni contabili all'11, senza cambiare le 16 unità.

- [ ] **Step 2: Aggiornare la riga della matrice**

Compilare fonte, collocazione, teoria, casi, output, verifica e manutenzione normativa. Passare da `parziale` a `completo` soltanto dopo le review.

- [ ] **Step 3: Ricalcolare i totali**

Atteso: 80 nuclei = 64 `completo` + 16 `parziale`; 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`; 16 blocker.

- [ ] **Step 4: Aggiornare report e committare**

Chiudere E06, aggiornare cap. 4/6, sintesi, priorità e giudizio; mantenere il modulo non pubblicabile e gli altri 16 parziali.

```powershell
git add -- <file-governance-effettivamente-modificati>
git commit -m "docs: update M-FC02 income tax coverage status"
```

---

### Task 5: Gate finale e pubblicazione

**Files:**
- Read: tutti i file modificati nei Task 1-4.
- Update through project workflow: memoria locale e log soltanto con strumenti canonici disponibili.

**Interfaces:**
- Consumes: quattro deliverable approvati.
- Produces: blocco revisionato e sincronizzato su `origin/main`.

- [ ] **Step 1: Eseguire audit e controlli**

```powershell
npm run audit:coverage
git diff --check
git log --oneline origin/main..HEAD
```

Atteso M-FC02: `80 righe, 64 complete, 16 blocker, 0 warning`.

- [ ] **Step 2: Richiedere review finale end-to-end**

Il revisore controlla source → capitolo 4 → capitolo 6 → capitolo 11 → governance, con finding Critical/Important/Minor e verdetto READY/NOT READY.

- [ ] **Step 3: Registrare la traccia agentica**

Usare `LocalAgentMemory` se tecnicamente disponibile; se `tsx` resta assente dalla cache, registrare il limite senza creare memoria parallela.

- [ ] **Step 4: Pubblicare**

```powershell
git push origin main
```

Atteso: `origin/main` avanzato ai commit del blocco, con 16 blocker M-FC02 residui dichiarati.
