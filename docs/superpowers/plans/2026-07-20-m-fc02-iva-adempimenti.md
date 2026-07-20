# M-FC02 IVA and Filing Obligations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Portare a Livello 3 i nuclei M-FC02 su IVA e dichiarazione-versamento-compensazione, chiudendo soltanto i relativi due blocker dopo verifica normativa ed editoriale indipendente.

**Architecture:** La conoscenza normativa viene prima acquisita e consolidata in due source note coordinate. Il capitolo 4 resta responsabile dell'architettura IVA; il capitolo 6 sviluppa operazioni e adempimenti. Solo dopo i gate sui contenuti vengono aggiornati indice, matrice e report.

**Tech Stack:** Markdown/Obsidian wiki, fonti ufficiali Normattiva ed EUR-Lex, PowerShell, Git, audit Node `scripts/audit-didactic-coverage.mjs`.

## Global Constraints

- Seguire `wiki/AGENTS.md` e usare `LocalAgentMemory`; se il runner non è disponibile, documentare l'errore senza creare memorie parallele.
- Applicare `concorso-book-professional-writer` e l'Integral Didactic Coverage Gate.
- Il testo editoriale deriva soltanto da `wiki/sources/`, `wiki/topics/`, `wiki/entities/` e conoscenza consolidata; non scrivere dai raw.
- Preservare tutte le modifiche preesistenti del worktree e usare `apply_patch` per le modifiche; se il wrapper Windows lo impedisce, registrare il fallimento prima di un fallback chirurgico sul solo file autorizzato.
- Usare struttura normativa stabile; aliquote, soglie, termini, modelli, codici e regole telematiche soltanto se ufficialmente verificati, datati e didatticamente necessari.
- Non presentare l'IVA come neutrale in modo assoluto; non confondere non imponibilità, esenzione ed esclusione; non descrivere detrazione o compensazione come incondizionate.
- Non duplicare nei capitoli 4 e 6 la disciplina responsabile dei capitoli 5, 5A, 5B e 7.
- Ogni task richiede implementazione, SPEC COMPLIANCE review, QUALITY review, fix loop e commit isolato.
- Governance attesa dopo approvazione: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`, 14 blocker; giudizio globale ancora `Non pubblicabile allo stato attuale`.

---

### Task 1: Corpus ufficiale e conoscenza consolidata

**Files:**
- Verify/conditionally refresh: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html`
- Verify/conditionally refresh: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html`
- Verify/conditionally refresh: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html`
- Reuse: `wiki/raw/m-fc02-agenzie-fiscali/eurlex-direttiva-2006-112-iva-consolidata-2025-04-14.html`
- Create: `wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md`
- Create: `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md`
- Create: `.superpowers/sdd/iva-task-1-report.md`

**Interfaces:**
- Consumes: fonti ufficiali, source note esistenti `normativa-tributaria-tuir-iva-accertamento-m-fc02`, `adempimenti-contabilita-civile-commerciale-m-fc02` e `diritto-ue-fiscale-doganale-iva-cdu-2026-07-18`.
- Produces: due note consolidate canoniche che i Task 2 e 3 useranno come unica base normativa nuova.

- [ ] **Step 1: Registrare baseline e insufficienza delle note esistenti**

Eseguire:

```powershell
git status --short -- wiki/raw/m-fc02-agenzie-fiscali wiki/sources
Get-FileHash -Algorithm SHA256 wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html
Get-FileHash -Algorithm SHA256 wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html
Get-FileHash -Algorithm SHA256 wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html
rg -n "imponibile|non imponibile|esente|esclus|integrativa|correttiva|compensazione" wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md wiki/sources/adempimenti-contabilita-civile-commerciale-m-fc02.md
```

Atteso: raw esistenti identificati; le vecchie note non sostengono ancora la copertura articolo-specifica richiesta.

- [ ] **Step 2: Verificare versioni ufficiali e acquisire solo ciò che manca**

Consultare fonti ufficiali Normattiva ed EUR-Lex. Per ogni atto separare: data di consultazione, data/identificativo della versione, ultimo aggiornamento dichiarato e decorrenze future. Se il file locale non consente questa riconciliazione, acquisire un export ufficiale integrale con nome che includa la data di riferimento; non sovrascrivere silenziosamente un raw con hash già tracciato.

Atteso: provenienza e versione verificabili per D.P.R. 633/1972, D.P.R. 322/1998, D.Lgs. 241/1997 e direttiva 2006/112/CE.

- [ ] **Step 3: Scrivere la source note IVA**

La nota deve consolidare almeno:

```text
funzione e armonizzazione UE
presupposti soggettivo, oggettivo e territoriale
cessioni e prestazioni
imponibili / non imponibili / esenti / escluse
effettuazione ed esigibilità
base imponibile
rivalsa
detrazione e limiti concettuali
documentazione, registrazioni, liquidazione e dichiarazione
routing responsabile capitolo 4 / capitolo 6
claim mobili esclusi o datati
```

Atteso: ogni nucleo ha articoli/fonti di sostegno, distinzione tra dato testuale e sintesi didattica, esempi ammessi e note di prudenza.

- [ ] **Step 4: Scrivere la source note sugli adempimenti**

La nota deve consolidare almeno:

```text
funzione della dichiarazione
presentazione e regole strutturali
originaria / correttiva / integrativa / omessa
versamento unitario
modello F24 come funzione, non repertorio di codici
compensazione verticale / orizzontale
limiti e controlli senza soglie non verificate
errore, correzione, rimborso e raccordo con controllo/sanzione
routing capitoli 5, 5A, 5B, 6 e 7
```

Atteso: nessun automatismo e nessuna regola mobile non datata.

- [ ] **Step 5: Eseguire il gate della conoscenza**

Eseguire:

```powershell
rg -n "^## |D.P.R. 633|D.P.R. 322|D.Lgs. 241|data di consultazione|versione|capitolo 4|capitolo 6" wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
git diff --check -- wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
```

Atteso: due note autonome, UTF-8 valide, routing coerente e diff-check pulito. Gli eventuali whitespace di raw ufficiali sono documentati e non normalizzati.

- [ ] **Step 6: Review indipendente e commit**

Richiedere due verdetti separati, correggere ogni rilievo bloccante e committare esclusivamente raw nuovi/aggiornati realmente necessari e le due source note:

```powershell
git add -- wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
git add -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html
git diff --cached --name-only
git commit -m "docs: consolidate M-FC02 VAT and filing sources"
```

Prima del commit, per ciascun raw invariato o non necessario eseguire il comando corrispondente: `git restore --staged -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html`, `git restore --staged -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html` oppure `git restore --staged -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html`. Il diff cached deve mostrare soltanto le due source note e gli eventuali raw ufficiali realmente acquisiti.

Atteso: `SPEC COMPLIANCE: PASS`, `QUALITY: PASS`, commit isolato.

---

### Task 2: Architettura IVA nel capitolo 4

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
- Create: `.superpowers/sdd/iva-task-2-report.md`

**Interfaces:**
- Consumes: le due source note approvate nel Task 1 e la source UE già consolidata.
- Produces: sede teorica responsabile dell'architettura IVA e anchor precisi per il capitolo 6.

- [ ] **Step 1: Registrare baseline e mappare le promesse**

Eseguire stat, SHA-256 e diff del capitolo. Elencare le affermazioni già presenti sotto `## IVA: operazioni, soggetti, detrazione e adempimenti` e verificare ciò che è soltanto nominato.

- [ ] **Step 2: Integrare il quadro teorico**

Sviluppare nel blocco IVA:

```text
IVA come imposta armonizzata sui consumi
neutralità come meccanismo, con limiti
tre presupposti
soggetto passivo / debitore / consumatore finale
catena rivalsa → detrazione → liquidazione
quattro classi di operazioni e loro conseguenza essenziale
rinvio esatto al capitolo 6
```

Per ciascun concetto includere definizione, funzione, distinzione, conseguenza, mini-esempio, errore tipico e verifica, senza duplicare la casistica applicativa del capitolo 6.

- [ ] **Step 3: Aggiornare tracciabilità e frontmatter**

Aggiungere le source note approvate e la data di compilazione/review pertinente. Non aumentare automaticamente `status` o `confidence`.

- [ ] **Step 4: Eseguire il gate del capitolo 4**

Verificare presenza dei nuclei, assenza di aliquote/soglie mobili non datate, anchor del capitolo 6, UTF-8 e:

```powershell
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
```

Atteso: diff pulito e nessuna regressione del blocco IRPEF/IRES.

- [ ] **Step 5: Review indipendente e commit**

Ottenere `SPEC COMPLIANCE: PASS` e `QUALITY: PASS`, applicare il fix loop e committare:

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
git commit -m "docs: strengthen M-FC02 VAT framework"
```

---

### Task 3: Operazioni IVA e ciclo degli adempimenti nel capitolo 6

**Files:**
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`
- Create: `.superpowers/sdd/iva-task-3-report.md`

**Interfaces:**
- Consumes: source note approvate, quadro teorico del Task 2 e anchor esistenti dei capitoli 5, 5A, 5B e 7.
- Produces: trattazione teorico-operativa autosufficiente che sostiene la chiusura dei due blocker.

- [ ] **Step 1: Registrare baseline e proteggere il blocco redditi**

Rilevare stat/hash e salvare la mappa delle sezioni IRPEF/IRES già approvate. Il diff finale deve dimostrare che il nuovo intervento è circoscritto a IVA, adempimenti, apparato applicativo condiviso, riferimenti e review.

- [ ] **Step 2: Sviluppare le operazioni IVA a Livello 3**

Integrare progressivamente:

```text
cessioni / prestazioni
soggettività IVA
territorialità essenziale
imponibile / non imponibile / esente / esclusa
effettuazione / esigibilità
base imponibile / aliquota
rivalsa / detrazione
documentazione / registrazione / liquidazione
```

Ogni nucleo deve includere teoria, conseguenza operativa, esempio, errore e controllo dell'apprendimento.

- [ ] **Step 3: Sviluppare dichiarazioni, versamenti e compensazioni**

Usare la sequenza canonica:

```text
fattispecie → documentazione → registrazione → liquidazione → dichiarazione → versamento o compensazione → controllo → eventuale correzione
```

Spiegare dichiarazione originaria, correttiva, integrativa e omessa; versamento unitario/F24; compensazione verticale e orizzontale; limiti e controlli; errore, correzione e rimborso; rinvii precisi alle sedi responsabili.

- [ ] **Step 4: Costruire l'apparato applicativo**

Inserire con soluzione motivata:

```text
caso IVA completo
caso comparativo sulle quattro classi di operazioni
caso correttiva vs integrativa
esercizio debiti-crediti-compensazione con dati pedagogici
quiz ragionati
risposta modello alla commissione
domande-trappola
errori frequenti
checklist e diario degli errori
```

Gli esempi numerici devono dichiarare la natura pedagogica dei valori.

- [ ] **Step 5: Aggiornare frontmatter, riferimenti e note di review**

Registrare le nuove source note; mantenere `status` e `confidence` prudenti; indicare le verifiche pre-pubblicazione per dati mobili e sistemi telematici.

- [ ] **Step 6: Eseguire il gate del capitolo 6**

Controllare tutte le promesse della specifica, anchor verso capitoli 4/5/5A/5B/7, assenza di scaffold redazionali, preservazione IRPEF/IRES, UTF-8 e:

```powershell
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

- [ ] **Step 7: Review indipendente e commit**

Ottenere entrambi i PASS, correggere rilievi e committare:

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
git commit -m "docs: complete M-FC02 VAT and filing coverage"
```

---

### Task 4: Governance dei due nuclei

**Files:**
- Modify if necessary: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
- Modify: `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`
- Create: `.superpowers/sdd/iva-task-4-report.md`

**Interfaces:**
- Consumes: capitoli 4 e 6 approvati e source note consolidate.
- Produces: stato canonico di copertura e conteggi verificabili.

- [ ] **Step 1: Verificare le prove prima dello stato**

Per ciascuno dei due nuclei compilare una mappa:

```text
teoria → sede/heading
caso → sede/heading
output concorsuale → sede/heading
verifica → sede/heading
source → nota consolidata
review → esito
```

Atteso: nessun passaggio a `completo` basato solo sulla lunghezza del testo.

- [ ] **Step 2: Aggiornare indice e matrice**

Usare heading canonici esatti. Portare a `completo` solo le righe IVA e adempimenti; registrare fonti, casi, output e verifiche. Non modificare gli altri 14 nuclei.

- [ ] **Step 3: Aggiornare il report M-FC02**

Chiudere esclusivamente i due blocker corrispondenti; impostare i conteggi a 80/66/14/0/0 e mantenere `Non pubblicabile allo stato attuale` con elenco dei 14 blocker residui.

- [ ] **Step 4: Eseguire conteggio e controllo reciproco**

Eseguire:

```powershell
rg -c "\| completo \|" wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
rg -c "\| parziale \|" wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
rg -n "Non pubblicabile|14 blocker|14 nuclei" wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
```

Atteso: `66`, `14`, stato non pubblicabile e diff-check pulito.

- [ ] **Step 5: Review indipendente e commit**

Ottenere i due PASS, applicare fix loop e committare solo i file governance realmente modificati:

```powershell
git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
git diff --cached --name-only
git commit -m "docs: close M-FC02 VAT and filing coverage gaps"
```

---

### Task 5: Audit end-to-end, memoria e pubblicazione GitHub

**Files:**
- Verify: tutti i file committati dal Task 1 al Task 4
- Update through service if available: `wiki/memory/agent/`

**Interfaces:**
- Consumes: intervallo completo dei commit del blocco.
- Produces: evidenza finale, traccia di memoria e branch remoto allineato.

- [ ] **Step 1: Eseguire audit fresco**

```powershell
npm run audit:coverage
```

Atteso per M-FC02: `80 righe, 66 complete, 14 blocker, 0 warning`. L'exit globale può restare 1 per i blocker dichiarati M-FC02 e VOL03; distinguere questo esito da errori tecnici.

- [ ] **Step 2: Eseguire diff-check editoriale e verifica Git**

```powershell
git diff --check a212645..HEAD -- . ':(exclude)wiki/raw/**'
git log --oneline a212645..HEAD
git status --short -- wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
```

Atteso: diff editoriale pulito, commit isolati e nessun file del blocco non committato. I raw ufficiali non sono normalizzati per far passare il controllo.

- [ ] **Step 3: Richiedere review finale end-to-end**

Il revisore deve valutare progressione, completezza teorica, accuratezza, autonomia, coerenza promessa/contenuto, applicazioni, tracciabilità e conteggi. Correggere ogni rilievo Critical o Important e ripetere il gate.

- [ ] **Step 4: Registrare la memoria locale**

Usare `LocalAgentMemory.captureConversation` per registrare sinteticamente decisione, risultati, commit e blocker residui. Se `tsx`/runner non è disponibile, riportare l'errore esatto e non scrivere manualmente store paralleli.

- [ ] **Step 5: Push e verifica remota**

```powershell
git push origin main
git rev-parse HEAD
git rev-parse origin/main
git status -sb
```

Atteso: SHA locale e `origin/main` coincidenti; modifiche preesistenti non appartenenti al blocco ancora preservate.
