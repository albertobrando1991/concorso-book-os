# IVA final end-to-end review package

## Range
Base: a212645
Head: 
8c0e28b75addce717b39f123b459169680133e03

## Commits
```text
8c0e28b docs: close M-FC02 VAT and filing coverage gaps
1a8c3c1 docs: complete M-FC02 VAT and filing coverage
df2791d docs: strengthen M-FC02 VAT framework
7ecd2c8 docs: consolidate M-FC02 VAT and filing sources
953ec67 docs: plan M-FC02 VAT and filing coverage

```

## Full diffstat including raw
```text
 .../plans/2026-07-20-m-fc02-iva-adempimenti.md     |   368 +
 .../04-diritto-tributario-teoria-imposta.md        |    71 +-
 ...dempimenti-fiscali-redditi-iva-dichiarazioni.md |   173 +-
 .../planning/02-indice-analitico-2026.md           |     4 +-
 .../planning/02-matrice-copertura-didattica.md     |     8 +-
 ...997-versamenti-compensazioni-akn-2026-07-20.xml |  2251 +++
 ...25-tu-versamenti-riscossione-akn-2026-07-20.xml | 16644 +++++++++++++++++++
 ...pr-100-1998-liquidazioni-iva-akn-2026-07-20.xml |   296 +
 ...2-1998-dichiarazioni-fiscali-akn-2026-07-20.xml |  1764 ++
 .../normattiva-dpr-633-1972-iva-akn-2026-07-20.xml | 13406 +++++++++++++++
 ...c02-copertura-didattica-integrale-2026-07-17.md |    56 +-
 ...menti-compensazioni-aggiornamento-2026-07-20.md |   135 +
 .../iva-dpr-633-1972-aggiornamento-2026-07-20.md   |   124 +
 13 files changed, 35213 insertions(+), 87 deletions(-)

```

## Raw official manifest
```text
normattiva-dlgs-241-1997-versamenti-compensazioni-akn-2026-07-20.xml | 237174 bytes | articles=42 | sha256=E89C8DFF010A03B21622395F2265BDF83F983BEC42D846E05969453DA5864B54
normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml | 1514465 bytes | articles=1 | sha256=D20152E0904998A57A5C8C698E076ED73EF82E47F67F463EC5ECAAABF823524A
normattiva-dpr-100-1998-liquidazioni-iva-akn-2026-07-20.xml | 23914 bytes | articles=2 | sha256=F35BF35E95D0EF4736AB862CC3EC5542931A800CFEEF55169A7621FB9D837D08
normattiva-dpr-322-1998-dichiarazioni-fiscali-akn-2026-07-20.xml | 225664 bytes | articles=12 | sha256=6AD5066623A8FAFB950C723A021633F3B5A451C142E044EC67CEEC74A97450C7
normattiva-dpr-633-1972-iva-akn-2026-07-20.xml | 1363594 bytes | articles=172 | sha256=3BD03FB841720EA471418FFCC928345DD72B40403B9289F53E8DE9E0D3C4FD81
```

## Editorial and governance diff (raw excluded)
```diff
diff --git a/docs/superpowers/plans/2026-07-20-m-fc02-iva-adempimenti.md b/docs/superpowers/plans/2026-07-20-m-fc02-iva-adempimenti.md
new file mode 100644
index 0000000..3fb9f97
--- /dev/null
+++ b/docs/superpowers/plans/2026-07-20-m-fc02-iva-adempimenti.md
@@ -0,0 +1,368 @@
+# M-FC02 IVA and Filing Obligations Implementation Plan
+
+> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
+
+**Goal:** Portare a Livello 3 i nuclei M-FC02 su IVA e dichiarazione-versamento-compensazione, chiudendo soltanto i relativi due blocker dopo verifica normativa ed editoriale indipendente.
+
+**Architecture:** La conoscenza normativa viene prima acquisita e consolidata in due source note coordinate. Il capitolo 4 resta responsabile dell'architettura IVA; il capitolo 6 sviluppa operazioni e adempimenti. Solo dopo i gate sui contenuti vengono aggiornati indice, matrice e report.
+
+**Tech Stack:** Markdown/Obsidian wiki, fonti ufficiali Normattiva ed EUR-Lex, PowerShell, Git, audit Node `scripts/audit-didactic-coverage.mjs`.
+
+## Global Constraints
+
+- Seguire `wiki/AGENTS.md` e usare `LocalAgentMemory`; se il runner non è disponibile, documentare l'errore senza creare memorie parallele.
+- Applicare `concorso-book-professional-writer` e l'Integral Didactic Coverage Gate.
+- Il testo editoriale deriva soltanto da `wiki/sources/`, `wiki/topics/`, `wiki/entities/` e conoscenza consolidata; non scrivere dai raw.
+- Preservare tutte le modifiche preesistenti del worktree e usare `apply_patch` per le modifiche; se il wrapper Windows lo impedisce, registrare il fallimento prima di un fallback chirurgico sul solo file autorizzato.
+- Usare struttura normativa stabile; aliquote, soglie, termini, modelli, codici e regole telematiche soltanto se ufficialmente verificati, datati e didatticamente necessari.
+- Non presentare l'IVA come neutrale in modo assoluto; non confondere non imponibilità, esenzione ed esclusione; non descrivere detrazione o compensazione come incondizionate.
+- Non duplicare nei capitoli 4 e 6 la disciplina responsabile dei capitoli 5, 5A, 5B e 7.
+- Ogni task richiede implementazione, SPEC COMPLIANCE review, QUALITY review, fix loop e commit isolato.
+- Governance attesa dopo approvazione: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`, 14 blocker; giudizio globale ancora `Non pubblicabile allo stato attuale`.
+
+---
+
+### Task 1: Corpus ufficiale e conoscenza consolidata
+
+**Files:**
+- Verify/conditionally refresh: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html`
+- Verify/conditionally refresh: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html`
+- Verify/conditionally refresh: `wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html`
+- Reuse: `wiki/raw/m-fc02-agenzie-fiscali/eurlex-direttiva-2006-112-iva-consolidata-2025-04-14.html`
+- Create: `wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md`
+- Create: `wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md`
+- Create: `.superpowers/sdd/iva-task-1-report.md`
+
+**Interfaces:**
+- Consumes: fonti ufficiali, source note esistenti `normativa-tributaria-tuir-iva-accertamento-m-fc02`, `adempimenti-contabilita-civile-commerciale-m-fc02` e `diritto-ue-fiscale-doganale-iva-cdu-2026-07-18`.
+- Produces: due note consolidate canoniche che i Task 2 e 3 useranno come unica base normativa nuova.
+
+- [ ] **Step 1: Registrare baseline e insufficienza delle note esistenti**
+
+Eseguire:
+
+```powershell
+git status --short -- wiki/raw/m-fc02-agenzie-fiscali wiki/sources
+Get-FileHash -Algorithm SHA256 wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html
+Get-FileHash -Algorithm SHA256 wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html
+Get-FileHash -Algorithm SHA256 wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html
+rg -n "imponibile|non imponibile|esente|esclus|integrativa|correttiva|compensazione" wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md wiki/sources/adempimenti-contabilita-civile-commerciale-m-fc02.md
+```
+
+Atteso: raw esistenti identificati; le vecchie note non sostengono ancora la copertura articolo-specifica richiesta.
+
+- [ ] **Step 2: Verificare versioni ufficiali e acquisire solo ciò che manca**
+
+Consultare fonti ufficiali Normattiva ed EUR-Lex. Per ogni atto separare: data di consultazione, data/identificativo della versione, ultimo aggiornamento dichiarato e decorrenze future. Se il file locale non consente questa riconciliazione, acquisire un export ufficiale integrale con nome che includa la data di riferimento; non sovrascrivere silenziosamente un raw con hash già tracciato.
+
+Atteso: provenienza e versione verificabili per D.P.R. 633/1972, D.P.R. 322/1998, D.Lgs. 241/1997 e direttiva 2006/112/CE.
+
+- [ ] **Step 3: Scrivere la source note IVA**
+
+La nota deve consolidare almeno:
+
+```text
+funzione e armonizzazione UE
+presupposti soggettivo, oggettivo e territoriale
+cessioni e prestazioni
+imponibili / non imponibili / esenti / escluse
+effettuazione ed esigibilità
+base imponibile
+rivalsa
+detrazione e limiti concettuali
+documentazione, registrazioni, liquidazione e dichiarazione
+routing responsabile capitolo 4 / capitolo 6
+claim mobili esclusi o datati
+```
+
+Atteso: ogni nucleo ha articoli/fonti di sostegno, distinzione tra dato testuale e sintesi didattica, esempi ammessi e note di prudenza.
+
+- [ ] **Step 4: Scrivere la source note sugli adempimenti**
+
+La nota deve consolidare almeno:
+
+```text
+funzione della dichiarazione
+presentazione e regole strutturali
+originaria / correttiva / integrativa / omessa
+versamento unitario
+modello F24 come funzione, non repertorio di codici
+compensazione verticale / orizzontale
+limiti e controlli senza soglie non verificate
+errore, correzione, rimborso e raccordo con controllo/sanzione
+routing capitoli 5, 5A, 5B, 6 e 7
+```
+
+Atteso: nessun automatismo e nessuna regola mobile non datata.
+
+- [ ] **Step 5: Eseguire il gate della conoscenza**
+
+Eseguire:
+
+```powershell
+rg -n "^## |D.P.R. 633|D.P.R. 322|D.Lgs. 241|data di consultazione|versione|capitolo 4|capitolo 6" wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
+git diff --check -- wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
+```
+
+Atteso: due note autonome, UTF-8 valide, routing coerente e diff-check pulito. Gli eventuali whitespace di raw ufficiali sono documentati e non normalizzati.
+
+- [ ] **Step 6: Review indipendente e commit**
+
+Richiedere due verdetti separati, correggere ogni rilievo bloccante e committare esclusivamente raw nuovi/aggiornati realmente necessari e le due source note:
+
+```powershell
+git add -- wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
+git add -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html
+git diff --cached --name-only
+git commit -m "docs: consolidate M-FC02 VAT and filing sources"
+```
+
+Prima del commit, per ciascun raw invariato o non necessario eseguire il comando corrispondente: `git restore --staged -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html`, `git restore --staged -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html` oppure `git restore --staged -- wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html`. Il diff cached deve mostrare soltanto le due source note e gli eventuali raw ufficiali realmente acquisiti.
+
+Atteso: `SPEC COMPLIANCE: PASS`, `QUALITY: PASS`, commit isolato.
+
+---
+
+### Task 2: Architettura IVA nel capitolo 4
+
+**Files:**
+- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`
+- Create: `.superpowers/sdd/iva-task-2-report.md`
+
+**Interfaces:**
+- Consumes: le due source note approvate nel Task 1 e la source UE già consolidata.
+- Produces: sede teorica responsabile dell'architettura IVA e anchor precisi per il capitolo 6.
+
+- [ ] **Step 1: Registrare baseline e mappare le promesse**
+
+Eseguire stat, SHA-256 e diff del capitolo. Elencare le affermazioni già presenti sotto `## IVA: operazioni, soggetti, detrazione e adempimenti` e verificare ciò che è soltanto nominato.
+
+- [ ] **Step 2: Integrare il quadro teorico**
+
+Sviluppare nel blocco IVA:
+
+```text
+IVA come imposta armonizzata sui consumi
+neutralità come meccanismo, con limiti
+tre presupposti
+soggetto passivo / debitore / consumatore finale
+catena rivalsa → detrazione → liquidazione
+quattro classi di operazioni e loro conseguenza essenziale
+rinvio esatto al capitolo 6
+```
+
+Per ciascun concetto includere definizione, funzione, distinzione, conseguenza, mini-esempio, errore tipico e verifica, senza duplicare la casistica applicativa del capitolo 6.
+
+- [ ] **Step 3: Aggiornare tracciabilità e frontmatter**
+
+Aggiungere le source note approvate e la data di compilazione/review pertinente. Non aumentare automaticamente `status` o `confidence`.
+
+- [ ] **Step 4: Eseguire il gate del capitolo 4**
+
+Verificare presenza dei nuclei, assenza di aliquote/soglie mobili non datate, anchor del capitolo 6, UTF-8 e:
+
+```powershell
+git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
+```
+
+Atteso: diff pulito e nessuna regressione del blocco IRPEF/IRES.
+
+- [ ] **Step 5: Review indipendente e commit**
+
+Ottenere `SPEC COMPLIANCE: PASS` e `QUALITY: PASS`, applicare il fix loop e committare:
+
+```powershell
+git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
+git commit -m "docs: strengthen M-FC02 VAT framework"
+```
+
+---
+
+### Task 3: Operazioni IVA e ciclo degli adempimenti nel capitolo 6
+
+**Files:**
+- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`
+- Create: `.superpowers/sdd/iva-task-3-report.md`
+
+**Interfaces:**
+- Consumes: source note approvate, quadro teorico del Task 2 e anchor esistenti dei capitoli 5, 5A, 5B e 7.
+- Produces: trattazione teorico-operativa autosufficiente che sostiene la chiusura dei due blocker.
+
+- [ ] **Step 1: Registrare baseline e proteggere il blocco redditi**
+
+Rilevare stat/hash e salvare la mappa delle sezioni IRPEF/IRES già approvate. Il diff finale deve dimostrare che il nuovo intervento è circoscritto a IVA, adempimenti, apparato applicativo condiviso, riferimenti e review.
+
+- [ ] **Step 2: Sviluppare le operazioni IVA a Livello 3**
+
+Integrare progressivamente:
+
+```text
+cessioni / prestazioni
+soggettività IVA
+territorialità essenziale
+imponibile / non imponibile / esente / esclusa
+effettuazione / esigibilità
+base imponibile / aliquota
+rivalsa / detrazione
+documentazione / registrazione / liquidazione
+```
+
+Ogni nucleo deve includere teoria, conseguenza operativa, esempio, errore e controllo dell'apprendimento.
+
+- [ ] **Step 3: Sviluppare dichiarazioni, versamenti e compensazioni**
+
+Usare la sequenza canonica:
+
+```text
+fattispecie → documentazione → registrazione → liquidazione → dichiarazione → versamento o compensazione → controllo → eventuale correzione
+```
+
+Spiegare dichiarazione originaria, correttiva, integrativa e omessa; versamento unitario/F24; compensazione verticale e orizzontale; limiti e controlli; errore, correzione e rimborso; rinvii precisi alle sedi responsabili.
+
+- [ ] **Step 4: Costruire l'apparato applicativo**
+
+Inserire con soluzione motivata:
+
+```text
+caso IVA completo
+caso comparativo sulle quattro classi di operazioni
+caso correttiva vs integrativa
+esercizio debiti-crediti-compensazione con dati pedagogici
+quiz ragionati
+risposta modello alla commissione
+domande-trappola
+errori frequenti
+checklist e diario degli errori
+```
+
+Gli esempi numerici devono dichiarare la natura pedagogica dei valori.
+
+- [ ] **Step 5: Aggiornare frontmatter, riferimenti e note di review**
+
+Registrare le nuove source note; mantenere `status` e `confidence` prudenti; indicare le verifiche pre-pubblicazione per dati mobili e sistemi telematici.
+
+- [ ] **Step 6: Eseguire il gate del capitolo 6**
+
+Controllare tutte le promesse della specifica, anchor verso capitoli 4/5/5A/5B/7, assenza di scaffold redazionali, preservazione IRPEF/IRES, UTF-8 e:
+
+```powershell
+git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
+```
+
+- [ ] **Step 7: Review indipendente e commit**
+
+Ottenere entrambi i PASS, correggere rilievi e committare:
+
+```powershell
+git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
+git commit -m "docs: complete M-FC02 VAT and filing coverage"
+```
+
+---
+
+### Task 4: Governance dei due nuclei
+
+**Files:**
+- Modify if necessary: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md`
+- Modify: `wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md`
+- Modify: `wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md`
+- Create: `.superpowers/sdd/iva-task-4-report.md`
+
+**Interfaces:**
+- Consumes: capitoli 4 e 6 approvati e source note consolidate.
+- Produces: stato canonico di copertura e conteggi verificabili.
+
+- [ ] **Step 1: Verificare le prove prima dello stato**
+
+Per ciascuno dei due nuclei compilare una mappa:
+
+```text
+teoria → sede/heading
+caso → sede/heading
+output concorsuale → sede/heading
+verifica → sede/heading
+source → nota consolidata
+review → esito
+```
+
+Atteso: nessun passaggio a `completo` basato solo sulla lunghezza del testo.
+
+- [ ] **Step 2: Aggiornare indice e matrice**
+
+Usare heading canonici esatti. Portare a `completo` solo le righe IVA e adempimenti; registrare fonti, casi, output e verifiche. Non modificare gli altri 14 nuclei.
+
+- [ ] **Step 3: Aggiornare il report M-FC02**
+
+Chiudere esclusivamente i due blocker corrispondenti; impostare i conteggi a 80/66/14/0/0 e mantenere `Non pubblicabile allo stato attuale` con elenco dei 14 blocker residui.
+
+- [ ] **Step 4: Eseguire conteggio e controllo reciproco**
+
+Eseguire:
+
+```powershell
+rg -c "\| completo \|" wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
+rg -c "\| parziale \|" wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
+rg -n "Non pubblicabile|14 blocker|14 nuclei" wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
+git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
+```
+
+Atteso: `66`, `14`, stato non pubblicabile e diff-check pulito.
+
+- [ ] **Step 5: Review indipendente e commit**
+
+Ottenere i due PASS, applicare fix loop e committare solo i file governance realmente modificati:
+
+```powershell
+git add -- wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
+git diff --cached --name-only
+git commit -m "docs: close M-FC02 VAT and filing coverage gaps"
+```
+
+---
+
+### Task 5: Audit end-to-end, memoria e pubblicazione GitHub
+
+**Files:**
+- Verify: tutti i file committati dal Task 1 al Task 4
+- Update through service if available: `wiki/memory/agent/`
+
+**Interfaces:**
+- Consumes: intervallo completo dei commit del blocco.
+- Produces: evidenza finale, traccia di memoria e branch remoto allineato.
+
+- [ ] **Step 1: Eseguire audit fresco**
+
+```powershell
+npm run audit:coverage
+```
+
+Atteso per M-FC02: `80 righe, 66 complete, 14 blocker, 0 warning`. L'exit globale può restare 1 per i blocker dichiarati M-FC02 e VOL03; distinguere questo esito da errori tecnici.
+
+- [ ] **Step 2: Eseguire diff-check editoriale e verifica Git**
+
+```powershell
+git diff --check a212645..HEAD -- . ':(exclude)wiki/raw/**'
+git log --oneline a212645..HEAD
+git status --short -- wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
+```
+
+Atteso: diff editoriale pulito, commit isolati e nessun file del blocco non committato. I raw ufficiali non sono normalizzati per far passare il controllo.
+
+- [ ] **Step 3: Richiedere review finale end-to-end**
+
+Il revisore deve valutare progressione, completezza teorica, accuratezza, autonomia, coerenza promessa/contenuto, applicazioni, tracciabilità e conteggi. Correggere ogni rilievo Critical o Important e ripetere il gate.
+
+- [ ] **Step 4: Registrare la memoria locale**
+
+Usare `LocalAgentMemory.captureConversation` per registrare sinteticamente decisione, risultati, commit e blocker residui. Se `tsx`/runner non è disponibile, riportare l'errore esatto e non scrivere manualmente store paralleli.
+
+- [ ] **Step 5: Push e verifica remota**
+
+```powershell
+git push origin main
+git rev-parse HEAD
+git rev-parse origin/main
+git status -sb
+```
+
+Atteso: SHA locale e `origin/main` coincidenti; modifiche preesistenti non appartenenti al blocco ancora preservate.
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
index e1de011..9f204ba 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
@@ -1,37 +1,37 @@
 ---
 id: chapter-m-fc02-diritto-tributario-teoria-imposta
 type: book_chapter
 title: "Diritto tributario e teoria dell'imposta"
 status: revised_draft
 domain: "concorsi pubblici italiani"
 topics: ["diritto tributario","teoria imposta","agenzie fiscali","obbligazione tributaria","imposte sui redditi","IRPEF","IRES","categorie reddituali","reddito complessivo","reddito d'impresa","iva","diritto tributario UE","IVA armonizzata","diritto doganale UE"]
 entities: ["Agenzia delle Entrate","Agenzia delle Dogane e dei Monopoli","Agenzia delle Entrate-Riscossione","Normattiva","Unione europea","Commissione europea","EUR-Lex"]
-source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","sources/costituzione-repubblica-italiana-testo-vigente.md","sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
+source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md","sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md","sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","sources/costituzione-repubblica-italiana-testo-vigente.md","sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
 book_refs: ["m-fc02-agenzie-fiscali","il-metodo-bando"]
 asset_refs:
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/01-mappa-bando-diritto-tributario.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/02-sequenza-nascita-tributo.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/03-categorie-del-tributo.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/04-presupposto-base-aliquota.png"
   - "books/moduli/m-fc02-agenzie-fiscali/assets/chapter-04/05-tuir-iva-accertamento-riscossione.png"
 confidence: 0.95
-updated_at: 2026-07-20T00:00:00+02:00
+updated_at: 2026-07-21T00:00:00+02:00
 created_at: 2026-07-01T21:00:00+02:00
 review_required: true
 canonical: true
 tags: ["book-chapter","module-code-m-fc02","professional-draft","revised-draft","illustrated"]
 book_id: m-fc02-agenzie-fiscali
 companion_to: il-metodo-bando
 outline_section: 4
 draft_stage: revised-editorial-draft
 module_code: M-FC02
 module_family: funzioni-centrali
-last_compiled_from: ["wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","wiki/entities/agenzia-delle-entrate.md","wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md","wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/03-ordinamento-organizzazione-ae-adm-ader.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md","wiki/sources/costituzione-repubblica-italiana-testo-vigente.md","wiki/sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","wiki/sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","wiki/sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
+last_compiled_from: ["wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md","wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md","wiki/entities/agenzia-delle-entrate.md","wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md","wiki/sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/02-bando-decoder-fiscale.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/03-ordinamento-organizzazione-ae-adm-ader.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md","wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md","wiki/sources/costituzione-repubblica-italiana-testo-vigente.md","wiki/sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18.md","wiki/sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo.md","wiki/sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17.md"]
 ---
 
 # Diritto tributario e teoria dell'imposta
 
 ## Apertura editoriale
 
 Nel modulo Agenzie fiscali il diritto tributario non e' una materia da studiare come un blocco astratto. E' il linguaggio di lavoro dell'amministrazione fiscale. Serve a capire perche' nasce un'imposta, chi deve pagarla, su quale base si calcola, quale adempimento viene richiesto, quali controlli puo' svolgere l'amministrazione e come si passa dalla regola generale al caso concreto.
 
@@ -353,29 +353,77 @@ Questo capitolo spiega perche' il raccordo esiste. La meccanica contabile e gli
 **Soluzione.** Non si parte dalla somma aritmetica degli incassi ne' dall'aliquota. Si identificano fonte e causa di ciascun provento, si verifica la categoria applicabile, si determina ogni reddito con le regole proprie e solo dopo si forma il reddito complessivo nei limiti previsti. Seguono oneri deducibili, imponibile, imposta lorda, detrazioni e altri scomputi. La prestazione occasionale non diventa lavoro autonomo abituale per il solo fatto di essere remunerata e neppure confluisce automaticamente nei redditi diversi senza verificare la fattispecie normativa.
 
 ### Errore tipico
 
 Confondere il denaro ricevuto con il reddito imponibile. L'incasso e' un fatto finanziario; il reddito e' una grandezza qualificata e determinata dalla disciplina tributaria. Prima di calcolare occorre rispondere, nell'ordine: chi e' il soggetto, quale fonte ha prodotto il provento, in quale categoria rientra, quale criterio di determinazione e imputazione si applica.
 
 ## IVA: operazioni, soggetti, detrazione e adempimenti
 
-L'IVA richiede un ragionamento diverso dalle imposte sui redditi. Il candidato deve spostare l'attenzione sulle operazioni, sui soggetti e sul meccanismo applicativo dell'imposta.
+L'IVA e' un'imposta armonizzata sui consumi: la direttiva 2006/112/CE costruisce il sistema comune, mentre il D.P.R. 633/1972 ne disciplina l'applicazione nazionale negli spazi consentiti. Non e' quindi soltanto una percentuale aggiunta al prezzo. La sua funzione e' far gravare il prelievo, attraverso applicazione e detrazione nelle diverse fasi, sul consumo finale. Una direttiva, tuttavia, non opera come un regolamento: nel caso concreto occorre raccordare istituto unionale e norma nazionale di attuazione.
 
-Nel modulo M-FC02 l'IVA va studiata in modo operativo. Le parole guida sono: operazione, soggetto passivo, rivalsa, detrazione, liquidazione, dichiarazione, fatturazione, registrazione, controllo. Non serve anticipare qui tutto il capitolo sugli adempimenti, ma serve capire che l'IVA non si riduce a "una percentuale sul prezzo".
+**Mini-esempio di raccordo.** Per qualificare una cessione, il candidato riconosce prima la categoria armonizzata nella direttiva 2006/112/CE e verifica poi come il D.P.R. 633/1972 la disciplina nell'ordinamento nazionale: la direttiva orienta il quadro comune, la norma interna governa l'applicazione del caso negli spazi consentiti.
 
-La logica base e':
+**Errore-trappola:** trattare la direttiva come un regolamento direttamente applicabile in modo identico, oppure ignorare primato e interpretazione conforme. **Verifica:** indica tipo e funzione della fonte UE, individua la disposizione nazionale pertinente e controlla che la lettura interna sia compatibile con il quadro unionale, senza attribuire automaticamente alla direttiva gli effetti propri di un regolamento.
+
+### Neutralita' come meccanismo, non come risultato assoluto
+
+Per l'operatore economico la neutralita' deriva dalla combinazione tra **rivalsa** e **detrazione**. Con la rivalsa il cedente o prestatore addebita l'imposta al cliente; con la detrazione recupera, alle condizioni previste, l'imposta dovuta o assolta sugli acquisti destinati a operazioni che attribuiscono tale diritto. La liquidazione confronta poi imposta a debito e imposta detraibile.
 
 ```text
-operazione rilevante -> soggetto -> applicazione dell'imposta -> documentazione -> detrazione/liquidazione -> dichiarazione -> controllo
+rivalsa sulle operazioni attive -> detrazione sugli acquisti ammessi -> liquidazione del saldo
 ```
 
-Questa sequenza aiuta a risolvere quiz e casi. Se una domanda riguarda l'IVA, chiediti sempre: qual e' l'operazione? chi e' il soggetto? quale documento entra in gioco? quale adempimento segue? quale controllo potrebbe svolgere l'amministrazione?
+La neutralita' non e' incondizionata: esenzioni, indetraibilita', percentuale di detrazione, requisiti documentali e rettifiche possono lasciare l'onere, in tutto o in parte, sull'operatore. La detrazione non e' ne' un rimborso automatico ne' una compensazione liberamente utilizzabile.
+
+**Mini-esempio.** Un professionista acquista un bene per l'attivita' e presta un servizio imponibile. L'imposta sull'acquisto puo' entrare nel confronto con quella addebitata al cliente soltanto se ricorrono inerenza, destinazione, documento, registrazione e gli altri requisiti applicabili.
+
+**Errore tipico:** affermare che l'IVA e' sempre neutrale per chiunque eserciti un'attivita'. **Verifica:** indica almeno una condizione della detrazione e un limite capace di interrompere o ridurre la neutralita'.
+
+### I tre presupposti: oggettivo, soggettivo e territoriale
+
+Una normale operazione interna entra nel campo IVA quando si coordinano tre profili:
+
+- il **presupposto oggettivo**, cioe' una cessione di beni o prestazione di servizi riconducibile alle fattispecie legali;
+- il **presupposto soggettivo**, cioe' l'esercizio abituale di impresa, arte o professione da parte del soggetto che effettua l'operazione;
+- il **presupposto territoriale**, cioe' la localizzazione dell'operazione nel territorio dello Stato secondo le regole proprie della fattispecie.
+
+Le importazioni sono assoggettate dall'art. 1 del D.P.R. 633/1972 da chiunque effettuate e richiedono quindi una lettura distinta dalla sequenza ordinaria delle operazioni interne. Anche il momento di effettuazione e l'esigibilita' sono passaggi ulteriori: non vanno confusi con la verifica dei tre presupposti.
+
+**Mini-esempio.** Una prestazione resa nell'esercizio abituale di una professione soddisfa il profilo soggettivo, ma non basta per concludere: occorre ancora qualificare la prestazione e applicare la regola di territorialita' pertinente.
+
+**Errore tipico:** ritenere territoriale ogni operazione solo perche' una parte e' italiana. **Verifica:** davanti a un caso, formula tre domande separate: che operazione e', chi la compie e dove si considera effettuata?
+
+### Soggetto passivo, debitore e consumatore finale
+
+Il **soggetto passivo** esercita in modo indipendente un'attivita' economica rilevante e partecipa al meccanismo IVA. Il **debitore d'imposta** e' invece il soggetto sul quale, nella specifica operazione, ricadono gli obblighi verso l'Erario: normalmente coincide con chi effettua l'operazione, ma la legge puo' porre gli obblighi sul cessionario o committente. Il **consumatore finale** sopporta economicamente l'imposta senza inserirla, di regola, in una successiva catena di detrazione.
+
+**Mini-esempio.** Nella vendita al consumatore, l'impresa e' soggetto passivo e normalmente debitore; il cliente finale paga il prezzo comprensivo dell'imposta e ne resta inciso economicamente. Una specifica inversione degli obblighi puo' mutare il debitore, non trasformare automaticamente il cliente in consumatore finale.
+
+**Errore tipico:** usare come sinonimi soggetto passivo, debitore e soggetto inciso. **Verifica:** per ciascuna figura indica rispettivamente posizione nel sistema, obbligo verso l'Erario e incidenza economica.
+
+### Le quattro classi di operazioni
+
+| Classe | Definizione e funzione | Conseguenza essenziale |
+|---|---|---|
+| **Imponibile** | Ricorrono i presupposti e si applica il regime ordinario. | L'imposta e' addebitata secondo le regole applicabili e l'operazione alimenta il meccanismo di detrazione-liquidazione. |
+| **Non imponibile** | L'operazione resta rilevante nel sistema, ma la legge non applica l'imposta, tipicamente nella logica della tassazione a destinazione. | In linea generale conserva il diritto a detrazione, da verificare sulla fattispecie. |
+| **Esente** | L'operazione e' nel campo IVA ma beneficia di un'esenzione tipizzata. | Non comporta addebito dell'imposta e puo' limitare la detrazione sugli acquisti. |
+| **Esclusa o fuori campo** | Manca un presupposto o una norma sottrae la fattispecie al campo applicativo. | Non segue il regime delle operazioni imponibili; gli effetti documentali e sulla detrazione dipendono dalla ragione dell'esclusione. |
+
+**Mini-esempio comparativo.** Una vendita interna imponibile, un'esportazione non imponibile, una prestazione sanitaria che ricade nell'esenzione tipica e una prestazione priva di territorialita' italiana appartengono a classi diverse. L'esempio serve a classificare, non a sostituire la verifica dei requisiti del caso.
+
+**Errore tipico:** trattare non imponibilita', esenzione ed esclusione come tre modi equivalenti di dire "IVA non addebitata". **Verifica:** spiega quale delle tre categorie resta normalmente collegata al diritto a detrazione e quale presuppone che l'operazione sia fuori dal campo applicativo. Le somme escluse dal computo della base imponibile ai sensi dell'art. 15 non formano, per cio' solo, una quinta classe di operazioni.
+
+### Dalla teoria agli adempimenti: rinvio responsabile
+
+La mappa teorica termina qui con la catena **fatturazione -> registrazione -> liquidazione -> dichiarazione annuale**. La funzione, l'ordine e le regole operative di documentazione, registrazione delle operazioni attive e degli acquisti, liquidazione periodica e dichiarazione IVA sono sviluppati nel [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#Operazioni IVA e ciclo degli adempimenti|capitolo 6, sezione "Operazioni IVA e ciclo degli adempimenti"]]. Il rinvio non comprende accertamento, sanzioni, riscossione o rimedi, affidati ai rispettivi capitoli 5, 5A, 5B e 7.
+
+**Verifica finale.** In novanta secondi ricostruisci: funzione dell'IVA; tre presupposti; differenza tra soggetto passivo, debitore e consumatore; rivalsa, detrazione e liquidazione; quattro classi e conseguenza essenziale. Se inizi da aliquota o calendario, stai saltando l'architettura.
 
-L'errore tipico e' studiare l'IVA solo come aliquota. L'aliquota conta, ma nel concorso conta anche il meccanismo. L'amministrazione fiscale non guarda solo al numero finale; guarda al comportamento del soggetto, alla documentazione, alla liquidazione, alla coerenza dei dati e agli adempimenti.
 
 ## Livello 3 - Quadro UE fiscale, IVA e dogane
 
 ### Attribuzione e principi di esercizio
 
 L'Unione europea agisce soltanto nei limiti delle competenze che gli Stati membri le hanno attribuito. Il principio di attribuzione risponde quindi alla prima domanda: l'Unione puo' intervenire in questa materia e con quale fondamento? Nelle competenze non esclusive opera anche la sussidiarieta: l'intervento unionale deve risultare giustificato rispetto a obiettivi che gli Stati non possono conseguire in misura sufficiente. La proporzionalita impone inoltre che contenuto e forma dell'azione non eccedano quanto necessario per raggiungere gli obiettivi dei Trattati.
 
 La cooperazione leale completa il quadro: Unione e Stati membri devono assistersi reciprocamente nell'adempimento dei compiti derivanti dai Trattati. Per il candidato questi principi non sono formule isolate. Servono a spiegare perche' una materia possa essere disciplinata in modo uniforme, armonizzata oppure lasciata, entro determinati limiti, alla normativa nazionale.
@@ -403,17 +451,17 @@ La diretta applicabilita del regolamento, l'attuazione della direttiva e l'event
 | Limite orizzontale | La direttiva, da sola, non puo' imporre obblighi a un altro soggetto privato in una controversia tra privati. |
 
 Queste condizioni non autorizzano automatismi. Occorre identificare la disposizione, il destinatario della pretesa e il rapporto concreto; vanno inoltre considerati primato e interpretazione conforme. Prima della pubblicazione o dell'uso su una fattispecie reale resta necessaria una review giuridica specifica.
 
 ### IVA armonizzata: direttiva europea e D.P.R. 633/1972
 
 La direttiva 2006/112/CE costruisce il sistema comune dell'IVA: operazioni rilevanti, soggetti passivi, fatto generatore, esigibilita, base imponibile, detrazione, obblighi e regimi speciali appartengono a un'architettura armonizzata. Il D.P.R. 633/1972 resta la disciplina nazionale di attuazione da applicare nel quadro della direttiva. Non e' una fonte isolata dal diritto UE, ma neppure una semplice copia che il candidato possa ignorare.
 
-Il metodo corretto e' tripartito: individua l'istituto armonizzato, ricerca la disposizione unionale pertinente, poi verifica la norma nazionale che lo attua. Per presupposti, operazioni, rivalsa, detrazione e liquidazione prosegui con [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#IVA: la mappa essenziale]].
+Il metodo corretto e' tripartito: individua l'istituto armonizzato, ricerca la disposizione unionale pertinente, poi verifica la norma nazionale che lo attua. Per presupposti, operazioni, rivalsa, detrazione e liquidazione prosegui con [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#Operazioni IVA e ciclo degli adempimenti]].
 
 ### Il sistema doganale multilivello
 
 Il Regolamento (UE) n. 952/2013 istituisce il Codice doganale dell'Unione e fissa il quadro generale su merci, soggetti, decisioni, dichiarazioni, controlli, classificazione, origine, valore, obbligazione doganale e regimi. Il Regolamento delegato (UE) 2015/2446 integra il CDU nei limiti della delega; il Regolamento di esecuzione (UE) 2015/2447 stabilisce condizioni uniformi di applicazione. I tre atti formano un sistema, ma svolgono funzioni differenti.
 
 Il diritto nazionale, compreso il D.Lgs. 141/2024, disciplina i profili rimessi allo Stato e completa il quadro negli spazi consentiti: non sostituisce il CDU e non puo' contraddirlo. Per la sequenza operativa delle procedure doganali rinvia a [[books/moduli/m-fc02-agenzie-fiscali/chapters/08-dogane-procedure-doganali-adm#1. Le fonti: prima l'Unione, poi il complemento nazionale]].
 
 ### Metodo del caso: importazione e vendita interna
@@ -654,16 +702,18 @@ Prima di passare al capitolo 5, verifica questi punti.
 Se manca uno di questi punti, il rischio e' portare nei capitoli successivi una confusione di base. Meglio correggerla qui.
 
 ## Riferimenti consolidati
 
 Questo capitolo e' costruito sulle note e sulle pagine consolidate del wiki del progetto:
 
 - [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
 - [[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]
+- [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]
+- [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]
 - [[topics/diritto-tributario-concorsi-agenzie-fiscali]]
 - [[entities/agenzia-delle-entrate]]
 - [[sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026]]
 - [[sources/costituzione-repubblica-italiana-testo-vigente]]
 - [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]]
 - [[sources/vol-03-fonti-specialistiche-fisco-dogane-previdenza-ispettivo]]
 - [[sources/m-fc02-corpus-ufficiale-integrativo-2026-07-17]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/01-mappa-agenzie-fiscali-profili-concorsuali]]
@@ -673,13 +723,14 @@ Questo capitolo e' costruito sulle note e sulle pagine consolidate del wiki del
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco]]
 
 Le fonti consolidate sostengono il nucleo teorico e concorsuale del capitolo. Per citazioni articolo-per-articolo e per dettagli su TUIR, IVA, accertamento, riscossione, riforma fiscale e decreti attuativi, resta necessaria una verifica su Normattiva e sulle fonti istituzionali aggiornate prima della pubblicazione.
 
 ## Note di review
 
 - Verificare su Normattiva il testo vigente del D.P.R. 917/1986, del D.P.R. 633/1972, del D.P.R. 600/1973 e della L. 111/2023 prima di inserire articoli, commi, soglie, date o esempi numerici.
 - Il quadro IRPEF/IRES consolida l'architettura stabile, non aliquote, scaglioni, soglie, importi, percentuali, termini o regimi mobili: verificarli sulla fonte ufficiale vigente prima della pubblicazione.
+- Il quadro IVA e' compilato sulle source note consolidate con audit al 20 luglio 2026; sottoporre a review umana tributaria/UE territorialita', esenzioni, inversione contabile, detrazione e decorrenze prima della pubblicazione.
 - Sottoporre a review normativa articolo per articolo soggetti, residenza, categorie, formazione del reddito complessivo e raccordo civilistico-fiscale; verificare separatamente derivazione rafforzata ed eccezioni quando il bando richiede dettaglio.
 - Coordinare la terminologia con i capitoli 5, 6 e 7, cosi' che accertamento, adempimenti e riscossione mantengano lo stesso significato in tutto il modulo.
 - Integrare eventuali riferimenti allo Statuto dei diritti del contribuente solo dopo una source note consolidata dedicata, per evitare richiami non tracciati.
 - I quiz presenti in questa bozza sono didattici e non articolo-specifici; prima dell'export finale possono essere ampliati con quesiti normativi puntuali dopo review umana.
 - Il capitolo ha taglio concorsuale e non costituisce consulenza fiscale.
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
index 1eab7a2..d5b07d8 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
@@ -1,33 +1,35 @@
 ---
 id: chapter-m-fc02-adempimenti-fiscali-redditi-iva-dichiarazioni
 type: book_chapter
 title: "Adempimenti fiscali: redditi, IVA, dichiarazioni"
 status: draft
 domain: "concorsi pubblici italiani"
 topics: ["adempimenti fiscali","IRPEF","IRES","categorie reddituali","reddito d'impresa","iva","dichiarazioni fiscali","versamenti"]
 entities: ["Agenzia delle Entrate"]
-source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/adempimenti-contabilita-civile-commerciale-m-fc02.md"]
+source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/adempimenti-contabilita-civile-commerciale-m-fc02.md","sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md","sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md"]
 book_refs: ["m-fc02-agenzie-fiscali"]
 confidence: 0.84
 updated_at: 2026-07-20T00:00:00+02:00
 created_at: 2026-07-01T21:00:00+02:00
 review_required: true
 canonical: true
 tags: ["book-chapter","module-code-m-fc02","professional-draft"]
 book_id: m-fc02-agenzie-fiscali
 outline_section: 6
 draft_stage: professional-draft
 module_code: M-FC02
 module_family: funzioni-centrali
 last_compiled_from:
   - wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md
   - wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md
   - wiki/sources/adempimenti-contabilita-civile-commerciale-m-fc02.md
+  - wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md
+  - wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
   - wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md
   - wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
   - wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md
 ---
 
 # Adempimenti fiscali: redditi, IVA, dichiarazioni
 
 ## Specifica struttura madre
@@ -315,81 +317,166 @@ Classifica l'effetto, senza usare importi vigenti:
 - Non classificare un provento dal nome usato dalle parti: ricostruisci fonte e rapporto effettivo.
 - Non usare «occasionale» come sinonimo universale di reddito diverso.
 - Non confondere reddito di capitale e guadagno finanziario tipizzato nei redditi diversi.
 - Non equiparare utile, imponibile, incasso e liquidità.
 - Non dedurre un costo soltanto perché è contabilizzato o collegato genericamente all'impresa.
 - Non descrivere la sintesi interpretativa dell'inerenza come testo letterale dell'art. 109.
 - Verifica sempre soggetto, residenza, categoria, periodo, determinazione, regimi speciali, dichiarazione e versamento.
 
-## IVA: la mappa essenziale
+## Operazioni IVA e ciclo degli adempimenti
 
-Nell'IVA il centro è l'operazione inserita in un meccanismo documentale e contabile:
+Il [[books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta#IVA: operazioni, soggetti, detrazione e adempimenti|capitolo 4]] presenta l'IVA come imposta armonizzata sui consumi e spiega la catena rivalsa, detrazione e liquidazione. Qui quella struttura diventa un metodo per trattare la singola operazione e seguirla fino all'eventuale correzione:
 
 ```text
-operazione -> soggetto -> disciplina applicabile -> documentazione
-          -> rivalsa/detrazione -> liquidazione -> dichiarazione -> controllo
+fattispecie -> documentazione -> registrazione -> liquidazione -> dichiarazione
+-> versamento o compensazione -> controllo -> eventuale correzione
 ```
 
-L'IVA non è soltanto una percentuale sul prezzo. Occorre capire chi effettua l'operazione, in quale veste, quale trattamento si applica, come l'operazione viene documentata e come concorre alla liquidazione.
+La sequenza ordina il ragionamento, ma non rende identiche tutte le fattispecie. Regole speciali, limiti alla detrazione, inversione contabile e regimi particolari richiedono sempre la verifica della disciplina applicabile.
 
-### Presupposti e operazioni
+### 1. Cessione o prestazione: qualificare il profilo oggettivo
 
-Le domande guida sono:
+La cessione trasferisce, di regola, la proprietà o un diritto reale su un bene; la prestazione deriva da un'obbligazione di fare, non fare o permettere. Le assimilazioni e le esclusioni previste dalla legge impediscono di classificare l'operazione soltanto dal nome del contratto.
 
-- che cosa è avvenuto: cessione, prestazione, acquisto o altra operazione?;
-- chi ha effettuato l'operazione e nell'esercizio di quale attività?;
-- dove si considera effettuata secondo le regole pertinenti?;
-- l'operazione è imponibile o riceve un trattamento diverso?;
-- quale documento e quale registrazione rendono il dato conoscibile?
+**Conseguenza operativa.** La qualificazione seleziona le regole su territorialità, effettuazione e documentazione. **Esempio:** vendita di un bene e consulenza verso corrispettivo appartengono a famiglie diverse. **Errore:** chiamare prestazione qualunque fattura. **Verifica:** quale fatto economico e quale disposizione di inclusione o esclusione sostengono la qualifica?
 
-È importante distinguere un'operazione estranea al campo applicativo da un'operazione che vi rientra ma riceve un particolare trattamento. Dire genericamente che «non si paga l'IVA» cancella differenze che possono produrre conseguenze sostanziali e documentali diverse.
+### 2. Soggettività e territorialità
 
-### Rivalsa, detrazione e neutralità
+La soggettività risponde a una domanda preliminare: chi compie l'operazione agisce come soggetto passivo? Rilevano l'esercizio abituale di impresa, arte o professione e, nella nozione unionale, l'attività economica indipendente. Una vendita privata occasionale non diventa operazione IVA soltanto perché ha un prezzo; per società ed enti occorre comunque verificare la sfera in cui agiscono.
 
-In termini essenziali, il soggetto che effettua un'operazione imponibile addebita l'imposta secondo il meccanismo applicabile; chi acquista, quando ricorrono i presupposti, può detrarre l'imposta assolta sugli acquisti. La liquidazione confronta le grandezze rilevanti:
+La territorialità localizza la singola operazione. Per i **beni** si guarda alla regola pertinente alla cessione: luogo del bene e, se vi è trasporto, partenza, arrivo e specifica fattispecie. Per i **servizi** la mappa essenziale distingue:
 
-```text
-IVA sulle operazioni attive
-- IVA detraibile sugli acquisti ammessi
-= risultato della liquidazione
-```
+| Prestazione | Regola-guida da verificare | Domanda operativa |
+| --- | --- | --- |
+| B2B, verso soggetto passivo | In via generale rileva il luogo del committente. | Il cliente agisce come soggetto passivo e dove è stabilito? |
+| B2C, verso consumatore | In via generale rileva il luogo del prestatore. | Il cliente agisce da privato e dove è stabilito il prestatore? |
 
-Lo schema non sostituisce le regole su detraibilità, rettifiche, operazioni particolari o regimi speciali. Dire che l'IVA è sempre neutrale per chiunque sarebbe inesatto: la detrazione richiede condizioni e può essere limitata o esclusa.
+Le regole generali non chiudono il caso. Immobili, trasporti, accesso a eventi, ristorazione, servizi elettronici e altre fattispecie possono seguire criteri speciali. Le eccezioni vanno usate come **controllo**: prima si classifica bene o servizio e B2B o B2C; poi si domanda se la natura concreta attiva una deroga, senza imparare un repertorio scollegato.
 
-Fattura, registrazione, liquidazione e dichiarazione svolgono funzioni differenti. La fattura documenta l'operazione; la registrazione la inserisce nel sistema contabile-fiscale; la liquidazione determina il risultato periodico; la dichiarazione rappresenta i dati del periodo.
+**Conseguenza operativa.** Territorialità italiana significa applicare la disciplina interna pertinente; territorialità estera impone di verificare obblighi e debitore senza concludere automaticamente «nessun adempimento». **Esempio:** consulenza resa da un'impresa italiana a un'impresa francese che agisce come soggetto passivo: la regola-guida B2B orienta verso il luogo del committente, salva verifica di qualificazione, stabilimento ed eccezioni. **Errore:** localizzare dal domicilio di una parte o dal luogo materiale in cui il consulente scrive il parere. **Verifica:** è bene o servizio, il cliente agisce B2B o B2C, qual è la regola generale e ricorre un'eccezione?
+
+### 3. Le quattro classi di operazioni
+
+| Classe | Inquadramento | Conseguenza essenziale |
+| --- | --- | --- |
+| Imponibile | Ricorrono i presupposti e si applica il regime ordinario. | L'imposta è addebitata secondo le regole applicabili e confluisce nella liquidazione. |
+| Non imponibile | L'operazione è nel sistema IVA, ma la legge non applica l'imposta, spesso secondo la logica della destinazione. | In linea generale conserva il diritto a detrazione, da verificare sulla fattispecie. |
+| Esente | L'operazione rientra nel campo IVA e beneficia di un'esenzione tipizzata. | Può limitare la detrazione sugli acquisti; non equivale a non imponibilità. |
+| Esclusa o fuori campo | Manca un presupposto oppure una norma sottrae la fattispecie al campo applicativo. | Non va trattata come operazione esente; restano da verificare gli obblighi propri del caso. |
 
-## Dichiarazione, liquidazione e versamento
+Le somme escluse dal computo della base imponibile non costituiscono automaticamente una quinta classe. **Errore comune:** dire soltanto «senza IVA». **Verifica:** l'operazione è dentro o fuori dal campo e, se è dentro, quale trattamento riceve?
 
-### Dichiarazione e documentazione
+### 4. Effettuazione ed esigibilità
 
-La dichiarazione fiscale rappresenta dati, elementi e risultati rilevanti secondo la disciplina del tributo. Non crea necessariamente il fatto imponibile, che trova fondamento nella legge; rende però la posizione conoscibile e consente i meccanismi di liquidazione e controllo.
+Il momento di effettuazione colloca l'operazione nel tempo secondo regole differenziate; fatturazione o pagamento possono assumere rilievo anticipato nei casi previsti. L'esigibilità indica quando l'Erario può pretendere l'imposta. I concetti sono collegati, ma non sovrapponibili.
 
-La documentazione sostiene ciò che viene rappresentato. Scritture, fatture, certificazioni e altri documenti collegano il dato alla sua origine. Un dato fiscale affidabile deve poter essere ricostruito.
+**Conseguenza operativa.** Il momento rilevante governa documentazione e periodo di liquidazione. **Esempio:** non si estende automaticamente a una prestazione la regola temporale propria di una cessione. **Errore:** assumere che data del contratto, consegna, fattura, pagamento ed esigibilità coincidano sempre. **Verifica:** quale evento rende effettuata la specifica operazione e quando diviene esigibile l'imposta?
 
-La dichiarazione non prova, da sola, che ogni importo sia corretto o pagato. Allo stesso modo, un versamento non dimostra che ogni obbligo dichiarativo sia stato assolto.
+### 5. Base imponibile e aliquota
 
-### Liquidazione e versamento
+La base imponibile muove dal corrispettivo complessivo e comprende gli elementi accessori indicati dalla disciplina. Le somme escluse dal computo devono ricadere in una previsione pertinente. L'aliquota è la misura applicata alla base, non il punto di partenza del caso.
 
-Liquidare significa determinare il risultato applicando le regole ai dati. Non significa svolgere un accertamento sostanziale. Il versamento è invece l'esecuzione monetaria dell'obbligazione e può riferirsi a saldo, acconti, ritenute o altri titoli previsti.
+**Conseguenza operativa.** Prima si ricostruiscono corrispettivo, accessori ed esclusioni; soltanto dopo si individua l'aliquota vigente. **Esempio:** una spesa accessoria non sparisce dalla base perché esposta separatamente. **Errore:** applicare una percentuale a un importo non qualificato. **Verifica:** quali componenti formano la base e quale fonte vigente sostiene l'aliquota?
+
+### 6. Rivalsa, detrazione e liquidazione
+
+La rivalsa riguarda l'addebito dell'imposta al cliente; la detrazione riguarda l'imposta dovuta o assolta sugli acquisti. La detrazione richiede attività economica, destinazione a operazioni che attribuiscono il diritto, documento e registrazione richiesti e assenza di limiti specifici. Non è un rimborso né una compensazione automatica.
+
+```text
+IVA sulle operazioni attive - IVA detraibile sugli acquisti ammessi
+= debito o eccedenza della liquidazione
+```
 
-Per risolvere un caso chiediti quale somma è dovuta, chi deve pagarla, a quale periodo si riferisce e se il dato è coerente con dichiarazione e documentazione. Versare non corregge automaticamente un dato dichiarativo errato; dichiarare non equivale a pagare.
+**Esempio pedagogico:** IVA attiva 1.200 e IVA detraibile 700 producono un saldo di 500; i valori allenano il calcolo e non rappresentano aliquote, soglie o parametri vigenti. **Errore:** sottrarre tutta l'IVA sugli acquisti senza verificarne il diritto. **Verifica:** quali acquisti sono documentati, inerenti e destinati a operazioni con diritto a detrazione?
 
-### Compensazione e correzione degli errori
+### 7. Documento, registri e liquidazione
 
-La compensazione consente, nel perimetro stabilito dalla legge, di utilizzare crediti per assolvere debiti. Non è una cancellazione informale: richiede esistenza e utilizzabilità del credito, corretta individuazione del debito e rispetto delle modalità applicabili.
+La fattura o il documento previsto descrive l'operazione e consente di collegare parti, oggetto, momento, base e imposta. Le operazioni attive documentate alimentano il **registro delle fatture emesse** o, quando applicabile, quello dei corrispettivi: l'imposta esigibile concorre al debito del periodo. Le fatture di acquisto confluiscono nel **registro degli acquisti**: l'imposta non diventa detraibile per la sola annotazione, ma soltanto se esistono diritto, documento e condizioni di esercizio.
 
-Gli errori possono riguardare dato, qualificazione, calcolo, omissione o pagamento. Lo strumento di correzione dipende dal tipo di errore, dal momento in cui viene rilevato e dalla disciplina vigente:
+Alla chiusura del periodo, la liquidazione riconcilia registri e documenti:
 
 ```text
-qual è l'errore? -> dove produce effetto? -> quando viene rilevato?
--> quale strumento prevede la disciplina vigente?
+imposta esigibile dalle operazioni attive registrate
+- imposta sugli acquisti ammessa in detrazione
+= debito da versare oppure eccedenza da gestire
 ```
 
-In prova è preferibile spiegare questa logica senza improvvisare termini, sanzioni o scadenze.
+**Esempio proprio, con valori pedagogici.** Il registro vendite espone imposta esigibile per 900; il registro acquisti espone 500, ma 80 riguardano un acquisto per il quale, nell'ipotesi, manca il diritto a detrazione. La detrazione ammessa è 420 e la liquidazione produce un debito di 480. Sottrarre tutti i 500 genererebbe un errore di detrazione; omettere una fattura attiva ridurrebbe invece il debito in modo indebito.
+
+**Percorso di soluzione.** Per ogni scostamento: risalire dal registro al documento; verificare momento ed esigibilità; correggere l'annotazione secondo la disciplina; riliquidare; valutare gli effetti su comunicazione, dichiarazione e pagamento. **Errore:** credere che fattura, registro e liquidazione siano duplicati dello stesso atto. **Verifica:** quale registro alimenta il debito, quale annotazione sostiene la detrazione e il saldo si riconcilia con i documenti?
+
+### Caso IVA completo
+
+**Fatti determinati.** Alfa S.r.l., stabilita a Bologna, presta a Beta S.p.A., soggetto passivo stabilito a Milano, un servizio ordinario di consulenza utilizzato nell'impresa. Il lavoro è ultimato il 12 marzo; Alfa emette fattura lo stesso giorno. Il corrispettivo pattuito è 4.000, oltre a 200 per spese accessorie contrattualmente addebitate. Per evitare dati mobili, si indica con **t** l'aliquota vigente da verificare alla data dell'operazione. Nel medesimo periodo Alfa riceve da Gamma S.r.l. una fattura per un acquisto inerente di 1.500 più imposta pedagogica di 300; documento e registrazione sono regolari e si assume, ai soli fini dell'esercizio, che l'imposta sia integralmente detraibile. Le altre operazioni del periodo generano imposta a debito pedagogica di 700.
+
+**Soluzione applicata.** (1) Alfa e Beta agiscono come soggetti passivi; si tratta di servizio B2B. (2) La regola-guida localizza la prestazione presso il committente: Milano, quindi Italia, non emergendo eccezioni dai fatti. (3) La prestazione è imponibile nell'ipotesi. (4) Per la prestazione ordinaria nazionale, la sola ultimazione del 12 marzo non basterebbe, secondo la regola generale, a determinare l’effettuazione: la fattura emessa nello stesso giorno anticipa invece il momento di effettuazione per l’importo fatturato. Su questa base si collocano operazione ed esigibilità nel periodo, ferma la verifica di eventuali regole speciali. (5) La base pedagogica è 4.200, perché le spese accessorie addebitate partecipano al corrispettivo; l'imposta è **4.200 × t**, senza attribuire a **t** un valore mobile. (6) Alfa esercita la rivalsa in fattura e registra l'operazione tra le vendite, alimentando il debito. (7) La fattura Gamma, registrata e relativa all'acquisto inerente, alimenta la detrazione per 300 nell'ipotesi. (8) La liquidazione pedagogica è **700 + (4.200 × t) - 300**. Il risultato positivo è debito; se fosse negativo sarebbe eccedenza, non rimborso automatico.
+
+**Controllo finale.** Se Alfa omettesse la fattura dal registro vendite, dovrebbe riallineare documento, registrazione, liquidazione, eventuale comunicazione/dichiarazione e pagamento con gli strumenti vigenti. Il [[books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale#Dal dato al controllo|capitolo 5]] tratta il controllo; il [[books/moduli/m-fc02-agenzie-fiscali/chapters/05a-sanzioni-amministrative-reati-tributari|capitolo 5A]] le sanzioni; il [[books/moduli/m-fc02-agenzie-fiscali/chapters/05b-tutela-processo-tributario|capitolo 5B]] la tutela; il [[books/moduli/m-fc02-agenzie-fiscali/chapters/07-riscossione-nazionale-lavoro-ader#2. Accertamento e riscossione: la separazione essenziale|capitolo 7]] la riscossione.
+
+### Caso comparativo: quattro operazioni, quattro esiti
+
+Classifica: vendita interna imponibile; esportazione che soddisfa i requisiti di non imponibilità; prestazione sanitaria compresa nell'esenzione tipizzata; prestazione priva di territorialità italiana. La soluzione non è «tutte senza IVA»: la prima applica l'imposta; la seconda resta nel sistema e, in linea generale, conserva la detrazione; la terza può limitarla; la quarta è fuori dal campo territoriale italiano. Requisiti e documenti vanno verificati nel caso concreto.
+
+## Dichiarazioni, versamenti e compensazioni
+
+### Dichiarazione originaria, correttiva, integrativa e omessa
+
+L'**originaria** è la prima dichiarazione validamente presentata per il periodo. Se ne viene trasmessa un'altra entro il termine ordinario, la qualificazione come **correttiva nei termini** e le modalità di sostituzione dipendono anche dalle istruzioni del modello vigente: non basta il nome scelto dal contribuente. Dopo il termine ordinario, l'**integrativa** corregge errori od omissioni nei limiti temporali, sostanziali e procedurali di legge.
+
+Una dichiarazione inviata entro la finestra che la legge considera **tardiva ma valida** resta dichiarazione presentata, ferma la disciplina della tardività. Oltre quella finestra è **omessa**; l'invio successivo può rilevare per gli effetti espressamente previsti, ma non converte automaticamente l'omissione in presentazione tempestiva o tardiva valida.
+
+La correzione può essere **a sfavore** del contribuente, quando emerge maggiore debito o minore credito, oppure **a favore**, quando emerge minore debito o maggiore credito. In entrambi i casi vanno verificati termini, prova, utilizzabilità del credito, effetti sui versamenti e strumento vigente: «integrativa» non significa credito immediatamente spendibile.
+
+**Caso 1.** Alfa scopre un ricavo omesso quando il termine ordinario è ancora aperto: consulta le istruzioni del modello e presenta la dichiarazione sostitutiva qualificata come correttiva, poi riallinea il pagamento. **Caso 2.** Lo stesso errore emerge dopo il termine: valuta un'integrativa a sfavore e la regolarizzazione. **Caso 3.** Un costo è stato duplicato e ha prodotto un credito apparente: anche se la correzione elimina il credito, occorre verificare se esso sia già stato usato. **Caso 4.** Un costo spettante era stato omesso: l'integrativa a favore non rende automatici compensazione o rimborso.
+
+### Versamento unitario e quadro temporale
+
+Il versamento unitario consente mediante F24 pagamenti e compensazioni riferiti ai tributi e contributi ammessi. Il modello organizza debiti, crediti e saldo; non crea il credito e non prova da solo la correttezza della dichiarazione. **Al 20 luglio 2026, per il percorso descritto sono vigenti gli artt. 17-20 e le altre disposizioni pertinenti del D.Lgs. 241/1997; l’art. 24 ha natura transitoria e non costituisce il fondamento del modello F24. Il D.Lgs. 33/2025 costituisce il futuro testo unico applicabile dal 1° gennaio 2027.** Codici, canali e specifiche restano dati mobili da verificare.
+
+### Compensazione: gate in sei controlli
+
+Prima di utilizzare un credito si verificano nell'ordine: **esistenza**, cioè formazione documentabile; **spettanza**, cioè fondamento sostanziale; **disponibilità**, cioè maturazione e possibilità di utilizzo; **perimetro**, verticale nello stesso tributo oppure orizzontale tra debiti e crediti ammessi; **cause ostative**, limiti o blocchi riferiti al contribuente e al credito; **controlli e modalità**, inclusi, quando richiesti, dichiarazione preventiva, visto, canale telematico e presentazione dell'F24. Un credito esposto non supera da solo questi gate.
+
+**Scenario risolto A — verticale.** Debito IVA pedagogico 900 e credito IVA disponibile 600: verificati i sei gate, 600 sono usati nello stesso tributo e resta 300. Se il credito è soltanto contabilizzato ma non disponibile, il calcolo è aritmeticamente possibile ma l'uso non è ammesso.
+
+**Scenario risolto B — orizzontale.** Credito IVA pedagogico 600 e debito contributivo ammesso 400: l'uso di 400 è orizzontale solo dopo verifica di spettanza, disponibilità, limiti, cause ostative e canale; residuano 200. Se manca un adempimento preventivo richiesto, non si procede confidando nella successiva correzione.
+
+### Credito IVA: riporto, compensazione e rimborso
+
+Un'eccedenza detraibile può essere **riportata** ai periodi successivi secondo le regole, mantenendola nel circuito IVA; può essere **compensata**, verticalmente o orizzontalmente, se esistente, spettante, disponibile e utilizzabile; può essere chiesta a **rimborso** soltanto nei casi e alle condizioni previsti, mediante il relativo percorso dichiarativo e di controllo. Sono tre destinazioni diverse: il saldo a credito non genera automaticamente denaro né libertà di scelta illimitata.
+
+**Percorso prudente.** Riconciliare origine e dichiarazione del credito; verificare presupposti della destinazione scelta; controllare limiti, garanzie, visto e cause ostative eventualmente applicabili; usare il canale vigente; conservare la prova; monitorare controlli ed eventuali rettifiche.
+
+### Errore e correzione
+
+Si identifica il fatto, si localizza l'effetto in documento, registro, liquidazione, dichiarazione o pagamento, si stabilisce quando emerge e si sceglie lo strumento vigente. Un versamento carente può richiedere pagamento e regolarizzazione; un versamento eccedente non produce automaticamente rimborso. Correzione dichiarativa, recupero del credito e regolarizzazione del pagamento sono percorsi coordinati ma distinti.
+
+### Quiz ragionati e risposta alla commissione
+
+**1. Un'operazione esente è fuori campo?** No: rientra nel campo IVA ma riceve un'esenzione tipizzata.
+**2. Rivalsa e detrazione coincidono?** No: la prima è addebito al cliente, la seconda è il diritto, esercitato alle condizioni di legge, di sottrarre dall'imposta dovuta quella assolta o dovuta sugli acquisti ammessi.
+**3. La correttiva è sempre un'integrativa?** No: conta se il termine ordinario è ancora aperto.
+**4. Un credito dichiarato è sempre compensabile?** No: vanno verificati esistenza, disponibilità, limiti e modalità.
+
+**Domanda.** Descriva il ciclo degli adempimenti IVA e il raccordo con dichiarazione e pagamento.
+**Risposta modello.** Si qualifica la fattispecie verificando operazione, soggetto, territorialità e trattamento; si individuano effettuazione, esigibilità, base e aliquota; quindi si documenta e registra. La liquidazione confronta imposta a debito e detraibile. La dichiarazione rappresenta annualmente dati e risultanze, mentre versamento, compensazione o rimborso seguono presupposti propri. Controllo, sanzione, tutela e riscossione appartengono a fasi successive e a sedi distinte.
+
+### Domande-trappola, errori e checklist
+
+- «Non imponibile» ed «esente» significano la stessa cosa? No.
+- Un F24 a saldo zero è irrilevante? No: modalità e obblighi di presentazione vanno verificati.
+- Pagare corregge automaticamente la dichiarazione? No.
+- Una dichiarazione oltre il termine ordinario è sempre integrativa valida? No.
+
+**Errori frequenti:** partire dall'aliquota; confondere art. 15 e operazione fuori campo; considerare neutrale l'IVA in assoluto; detrarre senza condizioni; confondere credito IVA, rimborso e compensazione; scegliere la correzione senza verificare la data.
+
+**Checklist:** ho qualificato operazione, soggetto e territorio; distinto le quattro classi; verificato effettuazione, esigibilità, base e aliquota; separato rivalsa e detrazione; riconciliato documento, registro, liquidazione e dichiarazione; qualificato la dichiarazione; verificato credito, debito e modalità; instradato controllo, sanzione, tutela e riscossione ai capitoli responsabili.
+
+**Diario degli errori:** registra in quattro colonne: fatto; passaggio saltato; regola corretta; prova di recupero. Una voce utile è «ho detto esente invece di fuori campo; non ho verificato i presupposti; ripasso le quattro classi; riclassifico quattro casi senza appunti».
 
 ## Servizi fiscali e rapporto con il contribuente
 
 Gli adempimenti sono anche un problema di servizio pubblico. I servizi fiscali consentono di consultare dati, trasmettere dichiarazioni e istanze, ricevere comunicazioni e correggere anomalie attraverso i canali previsti.
 
 Il funzionario deve identificare la richiesta, verificare competenza e identità, spiegare il percorso, indicare i documenti necessari e lasciare traccia dell'attività quando previsto. Non può sostituirsi al contribuente nelle scelte che non competono all'ufficio o anticipare l'esito di un controllo.
 
 | Situazione | Condotta corretta | Rischio da evitare |
@@ -398,21 +485,21 @@ Il funzionario deve identificare la richiesta, verificare competenza e identità
 | Documento mancante | Spiegare quale dato deve essere comprovato. | Anticipare l'esito del controllo. |
 | Anomalia nei dati | Identificare fonte, periodo e percorso di chiarimento. | Trattarla come evasione provata. |
 | Richiesta sulla riscossione | Distinguere la fase e indirizzare correttamente. | Confondere Agenzia delle Entrate e AdER. |
 
 Assistenza e controllo non sono alternativi: una comunicazione chiara favorisce l'adempimento spontaneo, mentre legalità e imparzialità assicurano il corretto trattamento delle posizioni.
 
 ## Da sapere in 5 righe
 
-1. L'adempimento fiscale è una sequenza di qualificazione, documentazione, dichiarazione, liquidazione e pagamento.
-2. Le imposte sui redditi partono da soggetto, categoria, periodo e regole di determinazione.
-3. L'IVA si studia attraverso operazione, soggetto, rivalsa, detrazione e liquidazione.
-4. Dichiarazione, versamento, controllo e riscossione sono momenti distinti.
-5. Compensazione e correzione degli errori richiedono presupposti e regole vigenti.
+1. Si parte dalla fattispecie e dalla sua qualificazione: fatto, soggetto, tributo e trattamento applicabile.
+2. La fattispecie qualificata conduce alla documentazione e poi alla registrazione nei registri pertinenti.
+3. Dai registri si passa alla liquidazione e, successivamente, alla dichiarazione dei dati e delle risultanze.
+4. Il saldo conduce al versamento oppure, quando ne ricorrono i presupposti, alla compensazione.
+5. Seguono il controllo e, se emerge un errore, l'eventuale correzione con lo strumento vigente.
 
 ## Caso guidato
 
 Una piccola società presta servizi e riceve fatture per acquisti inerenti all'attività. Al termine del periodo emergono tre problemi: una fattura attiva non è stata inserita correttamente nella liquidazione IVA; un costo è stato classificato senza verificarne il trattamento ai fini del reddito; il versamento non coincide con il risultato ricostruito.
 
 **Primo:** separare i tributi. L'operazione attiva entra nel circuito IVA: soggetto, operazione, documento, registrazione e liquidazione. Il costo entra nel circuito delle imposte sui redditi: natura del componente, periodo, regola di determinazione e incidenza sulla base imponibile.
 
 **Secondo:** ricostruire i dati dai documenti. Non si parte dalla somma versata per dedurre ciò che avrebbe dovuto essere dichiarato.
@@ -506,16 +593,18 @@ Trasforma la tabella in una risposta orale usando i verbi qualificare, documenta
 - Non confondo controllo, accertamento e riscossione.
 - Ho svolto caso, esercizio e quiz.
 
 ## Riferimenti consolidati
 
 - [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
 - [[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]
 - [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]
+- [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]
+- [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]
 - [[topics/diritto-tributario-concorsi-agenzie-fiscali]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/07-riscossione-nazionale-lavoro-ader]]
 
 ## Note di review
 
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
index f0435c0..5a602b2 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-indice-analitico-2026.md
@@ -28,18 +28,18 @@ draft_stage: revised-editorial-draft
 1. Agenzie fiscali, funzioni e organizzazione.
 2. Bando Decoder AE, ADM e AdER.
 3. Piano tributario, doganale, ACFI e tecnico-catastale.
 
 ## Blocco B - Ciclo tributario
 
 4. Principi, fonti UE/nazionali e obbligazione tributaria — cap. 4.
 5. IRPEF e IRES: quadro sistematico e soggetti - cap. 4, `IRPEF e IRES: il quadro sistematico`; categorie reddituali, determinazione, reddito d'impresa, casi e verifiche - cap. 6, da `Imposte sui redditi: qualificare prima di calcolare` a `Trappole e checklist operativa sui redditi`; raccordo civilistico-contabile e variazioni fiscali - cap. 11, `14. Dal bilancio al reddito imponibile`.
-6. IVA e imposte indirette.
-7. Dichiarazioni, versamenti e adempimenti.
+6. IVA e imposte indirette - cap. 4, `IVA: operazioni, soggetti, detrazione e adempimenti` per funzione, presupposti, soggetti, rivalsa, detrazione e classi di operazioni; cap. 6, `Operazioni IVA e ciclo degli adempimenti` per qualificazione, documentazione, registrazione, liquidazione, dichiarazione, casi e verifiche.
+7. Dichiarazioni, versamenti e adempimenti - cap. 6, `Il ciclo dell'adempimento fiscale` e `Dichiarazioni, versamenti e compensazioni`, con dichiarazione originaria/correttiva/integrativa/omessa, F24, compensazione verticale e orizzontale, correzione, casi e verifiche.
 8. Accertamento, istruttoria e contraddittorio.
 9. Interpello, compliance, adempimento collaborativo e verticale ACFI: residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e Tax Control Framework - cap. 5.
 10. Riscossione e AdER.
 11. Sanzioni amministrative e reati tributari — intercalare 5A, sviluppato.
 12. Tutela e processo tributario secondo TU 175 vigente — intercalare 5B, sviluppato.
 
 ## Blocco C - Dogane e monopoli
 
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
index 1f5fc9c..143daeb 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md
@@ -38,25 +38,25 @@ Audit semantico del testo reale dei 14 capitoli numerati e dei due intercalari 5
 | M-FC02/tutti | Orale | Risposta breve sull'organizzazione | alta | [[sources/agenzie-fiscali-organizzazione-ae-adm-ader]] | cap. 3, `Risposta modello da due minuti` | struttura della risposta esplicita | risposta completa | orale | domanda commissario | completo | aggiornare dati mobili | - |
 | M-FC02/tributario | Principi | Legalita, capacita contributiva, progressivita | alta | [[sources/costituzione-repubblica-italiana-testo-vigente]] | cap. 4, sezione omonima | principi definiti e distinti | esempi concorsuali | quiz/orale | quiz e caso | completo | review articolo-specifica | - |
 | M-FC02/tributario | Fonti | Gerarchia delle fonti tributarie | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4, `Le fonti` | livelli e funzione spiegati | lettura norma | orale | esercizio | completo | verifica vigenza | - |
 | M-FC02/tributario | Teoria imposta | Tributo, imposta, tassa, contributo | alta | [[topics/diritto-tributario-concorsi-agenzie-fiscali]] | cap. 4, sezione omonima | definizioni e distinzioni | tabella errori | quiz/orale | quiz | completo | stabile, review finale | - |
 | M-FC02/tributario | Teoria imposta | Presupposto e soggetto passivo | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4, sezioni omonime | definizione/funzione/conseguenze | caso guidato | quiz/orale | esercizio | completo | verifica fonti vigenti | - |
 | M-FC02/tributario | Teoria imposta | Base imponibile, aliquota, imposta dovuta | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4, sezione omonima | sequenza spiegata | esempio numerico semplice | quiz/orale | quiz | completo | non usare soglie mobili | - |
 | M-FC02/tributario | Rapporto tributario | Obbligazione e procedimento | alta | [[topics/diritto-tributario-concorsi-agenzie-fiscali]] | cap. 4, `Obbligazione tributaria` e `Rapporto` | nascita, funzione e interazione amministrativa | caso | orale | mini-esercizio | completo | review normativa | - |
 | M-FC02/tributario | IRPEF/IRES | Categorie reddituali, soggetti e reddito d'impresa | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]; [[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]] | cap. 4, `IRPEF e IRES: il quadro sistematico`; cap. 6, da `Imposte sui redditi: qualificare prima di calcolare` a `Trappole e checklist operativa sui redditi`; cap. 11, `14. Dal bilancio al reddito imponibile` | quadro sistematico, soggetti IRPEF/IRES, sei categorie, criteri di qualificazione e determinazione, reddito d'impresa e ponte utile-imponibile spiegati | esempi per categoria, caso IRPEF multi-componente, caso IRES e raccordo contabile con variazioni fiscali | classificazione motivata, risposta orale comparativa e ricostruzione del reddito imponibile | errori/verifiche per categoria, quiz dedicati, esercizio e checklist | completo | review TUIR vigente e disciplina articolo-specifica obbligatorie | - |
-| M-FC02/tributario | IVA | Presupposti, operazioni, rivalsa, detrazione, liquidazione | alta | [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]] | cap. 4 `IVA`; cap. 6 `IVA: mappa essenziale` | architettura spiegata, casistica/esclusioni limitate | caso societa | quiz/orale | quiz | parziale | DPR 633/1972 vigente | - |
+| M-FC02/tributario | IVA | Presupposti, operazioni, rivalsa, detrazione, liquidazione | alta | [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]] | cap. 4, `IVA: operazioni, soggetti, detrazione e adempimenti`; cap. 6, `Operazioni IVA e ciclo degli adempimenti` | funzione, armonizzazione, presupposti, soggetti, quattro classi, base, rivalsa, detrazione, documentazione e liquidazione spiegati | caso Alfa e caso comparativo su quattro operazioni | caso/quiz/orale | verifiche, quiz e checklist | completo | review tributaria/UE; dati mobili esclusi | - |
 | M-FC02/tributario | Accertamento | Controllo automatico, formale, sostanziale | alta | [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]] | cap. 5, sezione omonima | differenze e funzione spiegate | caso | quiz/orale | quiz | completo | verificare articoli | - |
 | M-FC02/tributario | Accertamento | Selezione, istruttoria, contraddittorio, atto | alta | [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]] | cap. 5, sezioni `Dal dato`-`Atto finale` | sequenza, poteri, prova e motivazione spiegati | caso guidato | caso/orale | esercizio | completo | art. 6-bis e termini mobili | - |
 | M-FC02/tributario | Tutela amministrativa/deflativa | Condizioni ed effetti articolo-specifici di autotutela e ulteriori strumenti deflativi | alta | [[sources/accertamento-contraddittorio-compliance-aggiornamento-2026-07-17]], [[sources/processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18]] | cap. 5, `Autotutela, definizione e tutela giurisdizionale`; cap. 5B, sez. 1-2 | tutela giurisdizionale e processo coperti sistematicamente nel 5B; restano funzionali, non articolo-specifici, condizioni ed effetti dei singoli strumenti amministrativi/deflativi | caso Omega e raccordi | orale/caso | tabella tre piani e verifiche; manca batteria sui singoli strumenti | parziale | riforme recenti e disciplina specifica degli strumenti | - |
 | M-FC02/tributario | Compliance | Compliance ordinaria | alta | [[sources/adempimento-collaborativo-compliance-fiscale-m-fc02]] | cap. 5, `Compliance fiscale ordinaria` | funzione e strumenti spiegati | esempio comunicazione | orale/caso | checklist | completo | aggiornare strumenti | - |
 | M-FC02/ACFI | Compliance | Adempimento collaborativo e tax control framework | alta profilo | [[sources/adempimento-collaborativo-compliance-fiscale-m-fc02]] | cap. 5, sezione omonima | struttura, rischio e interlocuzione spiegati | caso | orale/caso | quiz | completo | soglie/requisiti mobili | - |
 | M-FC02/ACFI | Fiscalita internazionale | Residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e Tax Control Framework | alta profilo | [[sources/fiscalita-internazionale-acfi-aggiornamento-2026-07-18]] | cap. 5, `Profili ACFI e fiscalita internazionale`, da `Fonti e metodo operativo` a `Commissario, trappole, esercizio e quiz` | istituti, fonti e metodo operativo spiegati nel perimetro ACFI selettivo | caso completo ACFI e mini-esercizio risolto | domanda da commissario, checklist e mappa dei rischi | verifiche risolte e quiz dedicati | completo | review didattica ACFI superata il 2026-07-18; manutenzione normativa e verifica delle fonti vigenti ancora obbligatorie | - |
-| M-FC02/tributario | Adempimenti | Ciclo fatto-documento-dichiarazione-liquidazione-versamento | alta | [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]] | cap. 6, `Il ciclo dell'adempimento` | sequenza spiegata | caso societa | caso/orale | esercizio | completo | modelli e termini mobili | - |
-| M-FC02/tributario | Adempimenti | Dichiarazione, versamento e compensazione | alta | [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]] | cap. 6, sezione omonima | funzioni distinte, correttive/integrative e limiti non sviluppati | caso generico | orale | quiz | parziale | DPR 322 e DLgs 241 vigenti | - |
+| M-FC02/tributario | Adempimenti | Ciclo fatto-documento-dichiarazione-liquidazione-versamento | alta | [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]] | cap. 6, `Il ciclo dell'adempimento fiscale` | sequenza spiegata | caso societa | caso/orale | esercizio | completo | modelli e termini mobili | - |
+| M-FC02/tributario | Adempimenti | Dichiarazione, versamento e compensazione | alta | [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]] | cap. 6, `Dichiarazioni, versamenti e compensazioni` | originaria, correttiva, integrativa, tardiva/omessa, F24, compensazione verticale/orizzontale, credito IVA e correzione spiegati | quattro casi dichiarativi e due scenari di compensazione | caso/orale | quiz, domande-trappola e checklist | completo | review tributaria; modelli, termini, soglie e canali mobili | - |
 | M-FC02/servizi | Servizi fiscali | Assistenza e rapporto col contribuente | media | [[sources/m-fc02-dossier-redazionale-agenzie-fiscali]] | cap. 6, sezione omonima | ruolo, documenti e limiti spiegati | front-office | situazionale | checklist | completo | aggiornare servizi telematici | - |
 | M-FC02/AdER | Riscossione | Imposizione, accertamento, riscossione | alta | [[topics/riscossione-tributaria-ader]] | cap. 7, sez. 1-2 | fasi e competenze distinte | casi | quiz/orale | quiz | completo | review normativa | - |
 | M-FC02/AdER | Riscossione | Ruolo, cartella, pagamento | alta | [[sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17]] | cap. 7, sez. 3 | sequenza e atti spiegati | caso cartella | caso/orale | esercizio | completo | DPR 602 vigente | - |
 | M-FC02/AdER | Riscossione | Accertamento esecutivo e presa in carico | alta | [[sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17]] | cap. 7, sez. 4 | modello e differenze spiegati | raccordo con caso | quiz/orale | quiz | completo | verificare disciplina vigente | - |
 | M-FC02/AdER | Riscossione | Rateizzazione, sospensione, sgravio, ricorso | alta | [[sources/riscossione-ader-aggiornamento-istituzionale-2026-07-17]] | cap. 7, sez. 5-6 | funzioni e competenze distinte | caso pagamento gia eseguito | situazionale | quiz | completo | soglie/termini mobili | - |
 | M-FC02/AdER | Riscossione | Misure cautelari ed esecuzione forzata | alta | [[sources/riscossione-agenzia-entrate-riscossione-m-fc02]] | cap. 7, sez. 7 | categorie inquadrate, presupposti/limiti non sviluppati | nessun caso dedicato | orale introduttivo | quiz limitato | parziale | soglie/esclusioni da verificare | - |
 | M-FC02/AdER | Lavoro | Front-office/back-office, competenza e tracciabilita | alta profilo | [[sources/assetti-organizzativi-ae-adm-ader-verifica-2026-07-17]] | cap. 7, sez. 8-9 | condotta e limiti spiegati | caso utente | situazionale | checklist | completo | allineare avviso/CCNL | - |
 | M-FC02/ADM | Dogane | Fonti UE e complemento nazionale | alta | [[sources/codice-doganale-unione-procedure-adm-aggiornamento-2026-07-17]] | cap. 8, sez. 1 | gerarchia e funzione spiegate | mappa procedurale | quiz/orale | quiz | completo | CDU consolidato | - |
@@ -100,9 +100,9 @@ Audit semantico del testo reale dei 14 capitoli numerati e dei due intercalari 5
 | M-FC02/tutti | Processo | Tutela e processo tributario | alta da indice | [[sources/processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18]] | cap. 5B, sez. 1-13 | tutela, organi, parti, atti, ricorso, prova, cautela, conciliazione, decisione, impugnazioni ed esecuzione spiegati | caso Omega atto-esito | caso/quiz/orale | esercizi, quiz e checklist PTT | completo | TU 175 vigente; review processuale | - |
 | M-FC02/tutti | UE | Diritto UE fiscale e doganale trasversale | media/alta | [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]] | cap. 4, `Livello 3 - Quadro UE`; rinvio cap. 8, sez. 1 | competenze, fonti, regolamento/direttiva, IVA armonizzata e sistema CDU-2446-2447 spiegati | importazione e vendita interna | quiz/orale/caso | domanda-trappola, errori e verifica | completo | versioni EUR-Lex e attuazione nazionale | - |
 | M-FC02/front-office | Relazione | Comunicazione, data protection, contribuente/operatore | alta profilo | [[sources/regolamento-ue-2016-679-gdpr-protezione-dati-personali]] | cap. 14, appendice C solo prevista; frammenti cap. 7/13 | teoria privacy e comunicazione non sistematica | casi sparsi | situazionale previsto | nessuna verifica dedicata | parziale | GDPR e policy enti | - |
 | M-FC02/tutti | Lessico | Glossario fiscale-doganale-catastale 80-100 voci | media | [[sources/m-fc02-dossier-redazionale-agenzie-fiscali]] | cap. 14, appendice A | 80 voci uniche con definizione funzionale, distinzione e rinvio preciso | esempi incorporati negli strumenti | ripasso/orale | checklist e piano | completo | aggiornamento terminologico al cut-off | - |
 | M-FC02/tutti | Perimetro | Schede allerta crisi, HR, gare, ICT | media | [[sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026]] | cap. 14, appendice E solo prevista | criteri sparsi nei capp. 1-2, scheda promessa assente | rinvii generici di famiglia | tabella prevista | nessuna | parziale | verificare bandi | - |
 
 ## Totali
 
-La classificazione contiene 80 nuclei: 64 `completo`, 16 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. Il validatore rileva quindi 16 blocker editoriali.
+La classificazione contiene 80 nuclei: 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. Il validatore rileva quindi 14 blocker editoriali.
diff --git a/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md b/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
index ee23287..96d0378 100644
--- a/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
+++ b/wiki/reviews/review-m-fc02-copertura-didattica-integrale-2026-07-17.md
@@ -21,33 +21,33 @@ affected_pages: ["books/moduli/m-fc02-agenzie-fiscali"]
 
 # Report editoriale - M-FC02 Agenzie fiscali
 
 ## 1. Sintesi editoriale
 
 - Genere editoriale: manuale-workbook specialistico per concorsi nelle Agenzie fiscali.
 - Pubblico target: candidati AE, ADM, AdER e profili Territorio/SPI, con nucleo comune nel VOL-01.
 - Perimetro di questa revisione: index, piano, indice analitico, 14 capitoli numerati e intercalari 5A/5B; confronto con source/topic/entity consolidate.
-- Stato generale in una frase: sanzioni, reati, processo, quadro UE, perimetro selettivo ACFI e nucleo IRPEF/IRES sono ora sviluppati e tracciati, ma il modulo resta non pubblicabile per 16 blocker residui, tutti nuclei parziali.
+- Stato generale in una frase: sanzioni, reati, processo, quadro UE, perimetro selettivo ACFI, IRPEF/IRES, IVA e adempimenti sono ora sviluppati e tracciati, ma il modulo resta non pubblicabile per 14 blocker residui, tutti nuclei parziali.
 
 ## 2. Punti applicati della checklist
 
 Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura integrale. I punti 16 e 22-26 sono stati osservati solo quando incidenti sulla chiarezza della promessa, poiche il perimetro non era una correzione microtestuale. I punti 27-28 non sono applicabili: non e' stato fornito un impaginato finale. Ogni promessa e' stata confrontata con spiegazione, esempio, output, verifica e fonti reali; lunghezza e presenza del file non sono state usate come prova di completezza.
 
 ## 3. Tabella errori
 
 | ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |
 | --- | --- | --- | --- | --- | --- | --- |
 | E01 | Cap. 12, intero | Completezza spiegazioni/gate | Grave | Il precedente stato `source_ready` e' superato: civile, contratti, impresa e societa sono sviluppati con casi e verifiche. La crisi resta deliberatamente parziale. | Mantenere chiuso il gap strutturale; consolidare una source ufficiale dedicata prima di ampliare la crisi d'impresa. | Chiuso per civile/commerciale; crisi aperta |
 | E02 | Cap. 14, intero | Completezza spiegazioni/gate | Grave | Il precedente placeholder e' superato: il capitolo e' un workbook autonomo con glossario di 80 voci, tavole, scadenziario, schemi, canvas, orale e ripasso. Non sostituisce i nuclei teorici mancanti o parziali. | Mantenere chiuso il gap workbook; sviluppare separatamente privacy e destinazioni cross-family, senza attribuire al workbook funzioni teoriche ulteriori. | Chiuso per workbook; nuclei teorici aperti |
 | E03 | Cap. 5A | Promessa didattica | Grave | Sanzioni amministrative e reati tributari sono ora sviluppati con fonti vigenti, casi, quiz e verifiche. | Mantenere review tributaria/penal-tributaria e controllo del passaggio al TU 173 dal 2027. | Chiuso |
 | E04 | Cap. 5B | Promessa didattica | Grave | Tutela e processo tributario sono ora sviluppati autonomamente secondo il TU 175 vigente, con cautela, prova, impugnazioni ed esecuzione. | Mantenere verifica articolo-specifica e review processual-tributaria. | Chiuso |
 | E05 | Cap. 5, `Profili ACFI e fiscalita internazionale` | Copertura selettiva ACFI | Grave | Il perimetro ACFI sviluppa residenza, stabile organizzazione, convenzioni e doppia imposizione, transfer pricing, documentazione e operazioni infragruppo, rischio fiscale e TCF, con fonti consolidate, caso, verifiche e quiz dedicati. | Mantenere il perimetro selettivo e la review normativa/editoriale; non estendere la promessa all'intera fiscalita internazionale. | Chiuso |
 | E06 | Capp. 4, 6 e 11, redditi | Completezza spiegazioni | Grave | Il cap. 4 inquadra soggetti e architettura IRPEF/IRES; il cap. 6 sviluppa le sei categorie, qualificazione e determinazione, reddito d'impresa, soggetti e struttura IRES con casi, quiz e orale; il cap. 11 completa il raccordo civilistico-contabile e le variazioni fiscali. | Mantenere review TUIR articolo-specifica e aggiornare le discipline mobili senza riaprire il nucleo didattico. | Chiuso |
-| E07 | Capp. 4 e 6, IVA | Completezza spiegazioni | Grave | Architettura IVA presente, ma casistica, esclusioni e applicazione sono troppo sintetiche per autonomia specialistica. | Ampliare presupposti/operazioni, detrazione, documentazione e liquidazione con casi graduati. | Aperto |
+| E07 | Capp. 4 e 6, IVA e adempimenti | Completezza spiegazioni | Grave | Funzione, presupposti, soggetti, classi di operazioni, rivalsa, detrazione, documentazione e liquidazione sono sviluppati; dichiarazioni successive, F24, compensazioni e correzioni hanno casi e verifiche dedicate, con fonti ufficiali consolidate al 20 luglio 2026. | Mantenere review tributaria/UE e verificare soltanto i dati mobili prima della pubblicazione. | Chiuso |
 | E08 | Capp. 5 e 5B, tutela amministrativa/deflativa | Progressione/completezza | Grave | Il cap. 5B copre sistematicamente tutela giurisdizionale e processo. Restano parziali le condizioni e gli effetti articolo-specifici di autotutela e degli ulteriori strumenti amministrativi/deflativi richiamati nei capp. 5 e 5B. | Sviluppare per ciascuno strumento amministrativo/deflativo presupposti, competenza, procedimento ed effetti, senza riaprire il nucleo processuale gia coperto. | Aperto, perimetro delimitato |
 | E09 | Cap. 7, misure cautelari/esecutive | Completezza | Grave | Categorie presenti, ma presupposti, limiti e distinzioni non raggiungono autonomia didattica. | Integrare schema comparativo e caso, dopo verifica delle soglie vigenti. | Aperto |
 | E10 | Cap. 8, regimi e debito doganale | Completezza | Grave | Regimi, debito e garanzia sono corretti come mappa ma insufficienti per il peso ADM. | Sviluppare condizioni, effetti, responsabilita e casi distinti con CDU consolidato. | Aperto |
 | E11 | Cap. 9, settori accise e giochi | Completezza | Grave | Prodotti, prelievi e controlli sono volutamente sintetici; l'output specialistico resta parziale. | Integrare nucleo stabile e rinviare solo dati mobili a fonti vive precise. | Aperto |
 | E12 | Cap. 10, DOCFA/PREGEO/estimo | Completezza tecnica | Grave | Le funzioni sono spiegate, ma procedura e applicazione estimativa richiedono maggiore profondita e review specialistica. | Aggiungere casi procedurali e applicazioni validate da revisore tecnico. | Aperto |
 | E13 | Cap. 11, partita doppia/indici/fisco | Completezza tecnica | Grave | La teoria e' leggibile, ma esercizi svolti e applicazione numerica non sono proporzionati alla promessa contabile. | Aggiungere registrazioni, riclassificazioni, indici e raccordi civilistico-fiscali svolti. | Aperto |
 | E14 | Cap. 14/7/13, privacy e front-office | Coerenza tra capitoli | Grave | Frammenti applicativi esistono, ma manca teoria unitaria su comunicazione, riservatezza e protezione dati. | Consolidare nel cap. 14 e rinviare dai casi con destinazione precisa. | Aperto |
 | E15 | Capp. 1-2 e cap. 14/E | Rinvii | Grave | I rinvii cross-family indicano il modulo, ma non una destinazione verificata a capitolo/paragrafo completo. | Trasformarli in destinazioni precise solo dopo verifica del contenuto ricevente. | Aperto |
@@ -64,32 +64,32 @@ Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura int
 - Criticita: valgono i limiti sui rinvii; denominazioni e prove richiedono sempre bando vivo.
 
 ### Capitolo 3 - Ordinamento e organizzazione
 - Punti di forza: distingue natura, funzioni, MEF e livelli organizzativi con caso e orale.
 - Criticita: assetti e regolamenti sono mobili e correttamente marcati per review.
 
 ### Capitolo 4 - Diritto tributario e teoria dell'imposta
 - Punti di forza: nucleo teorico di base, quadro sistematico IRPEF/IRES e Livello 3 UE completi, con competenze, fonti, IVA armonizzata e sistema CDU tracciati.
-- Criticita: l'IVA non raggiunge ancora la profondita specialistica promessa dai capitoli successivi; il quadro dei redditi resta soggetto a review normativa articolo-specifica.
+- Criticita: IVA e quadro dei redditi restano soggetti a review normativa articolo-specifica e alla verifica dei dati mobili, senza gap didattico locale aperto.
 
 ### Capitolo 5 - Accertamento, controlli e compliance
 - Punti di forza: ciclo del controllo, contraddittorio e compliance sono ben strutturati; il blocco ACFI tratta con metodo operativo gli istituti internazionali selezionati, fino a caso, verifiche e quiz.
 - Criticita: la tutela resta parziale; il blocco ACFI richiede manutenzione normativa sulle fonti e convenzioni vigenti, senza promettere una trattazione integrale della fiscalita internazionale.
 
 ### Capitolo 5A - Sanzioni amministrative e reati tributari
 - Punti di forza: distingue tributo, interessi, sanzione e reato; sviluppa parte generale, fattispecie, ravvedimento e D.Lgs. 74/2000 con casi e verifiche.
 - Criticita: soglie, pene e disciplina temporale richiedono review umana; il TU 173 resta applicabile dal 2027.
 
 ### Capitolo 5B - Tutela e processo tributario
 - Punti di forza: percorso autonomo dal riesame all'ottemperanza secondo TU 175, con prova, cautela, PTT, conciliazione e impugnazioni.
 - Criticita: termini, specifiche telematiche e singoli articoli richiedono controllo sulla versione coordinata vigente.
 ### Capitolo 6 - Adempimenti fiscali
 - Punti di forza: sequenza economica-documentale-dichiarativa chiara e applicata; categorie IRPEF, determinazione, reddito d'impresa e struttura IRES sono sviluppati con esempi, casi, quiz, orale e checklist.
-- Criticita: IVA, dichiarazioni correttive/integrative e compensazioni richiedono espansione; i redditi richiedono manutenzione normativa sul TUIR vigente.
+- Criticita: IVA, dichiarazioni e compensazioni richiedono manutenzione normativa sui dati mobili; i redditi richiedono manutenzione sul TUIR vigente.
 
 ### Capitolo 7 - Riscossione e AdER
 - Punti di forza: competenze, sequenze, front-office e principali alternative sono chiare.
 - Criticita: misure cautelari/esecutive e dati mobili non sono ancora sufficienti per pubblicazione.
 
 ### Capitolo 8 - Dogane
 - Punti di forza: progressione dall'arrivo allo svincolo e triade classificazione/origine/valore efficace.
 - Criticita: regimi, debito e garanzia richiedono maggiore profondita e fonte UE consolidata vigente.
@@ -116,18 +116,18 @@ Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura int
 
 ### Capitolo 14 - Appendici operative
 - Punti di forza: workbook autonomo con 80 voci di glossario, tavole comparative, scadenziario, checklist, schemi, canvas, orale e piano 1-3-7-14-30; rinvii verificati ai capitoli.
 - Criticita: i presidi su privacy, crisi e rinvii cross-family restano parziali e non vanno scambiati per teoria validata.
 
 ## 5. Coerenza globale
 
 - Terminologia: generalmente coerente; distinzione accertamento/riscossione ben presidiata.
-- Struttura vs indice: coerente per sanzioni, reati, processo, quadro UE, perimetro ACFI e IRPEF/IRES, collocati nei capp. 4, 5, 5A, 5B, 6 e 11; restano i 16 blocker parziali censiti.
-- Promesse dell'introduzione mantenute: solo in parte. Orientamento, performance, civile/commerciale, sanzioni/processo, quadro UE, perimetro ACFI, IRPEF/IRES e workbook sono forti; i 16 blocker impediscono ancora la copertura integrale.
+- Struttura vs indice: coerente per sanzioni, reati, processo, quadro UE, perimetro ACFI, IRPEF/IRES, IVA e adempimenti, collocati nei capp. 4, 5, 5A, 5B, 6 e 11; restano i 14 blocker parziali censiti.
+- Promesse dell'introduzione mantenute: solo in parte. Orientamento, performance, civile/commerciale, sanzioni/processo, quadro UE, perimetro ACFI, IRPEF/IRES, IVA, adempimenti e workbook sono forti; i 14 blocker impediscono ancora la copertura integrale.
 
 ## 6. Contenuto da verificare
 
 - Vigenza di statuti, regolamenti e assetti AE/ADM/AdER.
 - TUIR, IVA, accertamento, contraddittorio, riscossione e processo tributario vigenti.
 - CDU, regolamenti delegato/esecutivo, D.Lgs. 141/2024 e sistemi ADM.
 - TUA, EMCS/e-AD, riordino giochi, concessioni e prelievi.
 - DOCFA, PREGEO, Voltura Web, Sister, OMI e procedimenti estimativi.
@@ -136,41 +136,39 @@ Applicati i punti 1-15 e 17-21, 29-30, oltre al gate aggiuntivo di copertura int
 
 ## 7. Suggerimenti facoltativi (non errori)
 
 - Mantenere i glossari locali anche dopo la creazione del glossario unitario, usandoli come ripasso di capitolo.
 - Usare una sola simulazione trasversale aggiornata dopo la chiusura dei gap, invece di duplicare batterie simili.
 
 ## 8. Priorita degli interventi
 
-1. Chiudere i 16 nuclei parziali senza usare capitoli operativi o rinvii generici come sostituti della teoria.
+1. Chiudere i 14 nuclei parziali senza usare capitoli operativi o rinvii generici come sostituti della teoria.
 2. Mantenere aggiornato e sottoposto a review il perimetro selettivo ACFI, senza ampliarlo implicitamente all'intera fiscalita internazionale.
 3. Consolidare le fonti mancanti per crisi, privacy e verticali tecnici e svolgere review specialistiche.
 4. Riesaminare casi, quiz e laboratorio dopo la chiusura dei nuclei tecnici.
 5. Validare le destinazioni cross-family prima di trasformare i gap in rinvii editoriali.
 
 ## 9. Giudizio di pubblicabilita
 
-**Non pubblicabile allo stato attuale.** La matrice registra 80 nuclei: 64 `completo`, 16 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. I blocker editoriali sono quindi 16.
-
-I 16 nuclei `parziale` restano:
-
-1. IVA, casistica ed esclusioni;
-2. condizioni ed effetti articolo-specifici di autotutela e degli ulteriori strumenti amministrativi/deflativi;
-3. dichiarazione, versamento, compensazione e correzioni;
-4. misure cautelari ed esecuzione forzata AdER;
-5. regimi doganali;
-6. debito doganale e garanzia;
-7. prodotti energetici, alcole e tabacchi;
-8. tutela del giocatore, illegalita, prelievi e controlli;
-9. DOCFA, PREGEO e voltura;
-10. estimo e applicazioni OMI;
-11. conti e partita doppia;
-12. indici ed equilibri aziendali;
-13. utile civilistico e reddito imponibile;
-14. crisi d'impresa;
-15. comunicazione, front-office e privacy;
-16. schede e destinazioni cross-family per crisi, HR, gare e ICT.
-
-Il perimetro selettivo della fiscalita internazionale ACFI e' chiuso didatticamente nel cap. 5; non equivale a una promessa di copertura integrale della materia. Non restano nuclei `solo-nominato` o `mancante`: sanzioni, reati, processo, quadro UE, ACFI e IRPEF/IRES sono stati chiusi didatticamente nei capp. 4, 5, 5A, 5B, 6 e 11. Restano 16 blocker parziali e il modulo non e' pubblicabile. E16 mantiene obbligatoria la review normativa e tecnica prima della pubblicazione.
+**Non pubblicabile allo stato attuale.** La matrice registra 80 nuclei: 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`. I blocker editoriali sono quindi 14.
+
+I 14 nuclei `parziale` restano:
+
+1. condizioni ed effetti articolo-specifici di autotutela e degli ulteriori strumenti amministrativi/deflativi;
+2. misure cautelari ed esecuzione forzata AdER;
+3. regimi doganali;
+4. debito doganale e garanzia;
+5. prodotti energetici, alcole e tabacchi;
+6. tutela del giocatore, illegalita, prelievi e controlli;
+7. DOCFA, PREGEO e voltura;
+8. estimo e applicazioni OMI;
+9. conti e partita doppia;
+10. indici ed equilibri aziendali;
+11. utile civilistico e reddito imponibile;
+12. crisi d'impresa;
+13. comunicazione, front-office e privacy;
+14. schede e destinazioni cross-family per crisi, HR, gare e ICT.
+
+Il perimetro selettivo della fiscalita internazionale ACFI e' chiuso didatticamente nel cap. 5; non equivale a una promessa di copertura integrale della materia. Non restano nuclei `solo-nominato` o `mancante`: sanzioni, reati, processo, quadro UE, ACFI, IRPEF/IRES, IVA e adempimenti sono stati chiusi didatticamente nei capp. 4, 5, 5A, 5B, 6 e 11. Restano 14 blocker parziali e il modulo non e' pubblicabile. E16 mantiene obbligatoria la review normativa e tecnica prima della pubblicazione.
 
 ## 10. Limiti di questa revisione
 Audit eseguito sul markdown e sulle note consolidate presenti nel wiki, senza usare `raw/` e senza ricerca web. Non sono stati verificati layout impaginato, vigenza articolo-per-articolo, correttezza specialistica contabile/estimativa o aggiornamento dei sistemi telematici. Lo stato `completo` indica completezza didattica rispetto alla promessa locale osservata, non certificazione normativa finale.
diff --git a/wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md b/wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
new file mode 100644
index 0000000..edc3e5f
--- /dev/null
+++ b/wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
@@ -0,0 +1,135 @@
+---
+id: source-dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20
+type: source
+title: "Dichiarazioni, versamenti unitari e compensazioni: quadro vigente consolidato"
+status: consolidated
+domain: "concorsi pubblici italiani"
+topics: ["dichiarazioni fiscali", "versamenti unitari", "compensazione tributaria", "modello F24"]
+entities: ["Agenzia delle Entrate", "Normattiva"]
+source_refs: ["sources/adempimenti-contabilita-civile-commerciale-m-fc02", "sources/normativa-tributaria-tuir-iva-accertamento-m-fc02", "sources/iva-dpr-633-1972-aggiornamento-2026-07-20"]
+book_refs: ["m-fc02-agenzie-fiscali"]
+confidence: 0.93
+updated_at: 2026-07-20T00:00:00+02:00
+created_at: 2026-07-20T00:00:00+02:00
+review_required: true
+canonical: true
+tags: ["source", "official-source", "dichiarazioni", "f24", "compensazioni", "module-code-m-fc02", "cutoff-2026-07-20"]
+source_type: official_legal_corpus
+source_url: "mixed:https://www.normattiva.it/eli/id/1998/09/07/098G0373/CONSOLIDATED/20260720|https://www.normattiva.it/eli/id/1997/07/28/097G0277/CONSOLIDATED/20260720|https://www.normattiva.it/eli/id/2025/03/26/25G00044/CONSOLIDATED/20260523"
+source_date: "2026-07-20"
+audit_date: "2026-07-20"
+latest_official_update_checked: "D.P.R. 322/1998: ultimo aggiornamento pubblicato 17/06/2025; D.Lgs. 241/1997: disciplina vigente al 20/07/2026; D.Lgs. 33/2025: testo unico applicabile dal 01/01/2027"
+authority_level: very_high
+raw_refs:
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali.html"
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni.html"
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-322-1998-dichiarazioni-fiscali-akn-2026-07-20.xml"
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-241-1997-versamenti-compensazioni-akn-2026-07-20.xml"
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dlgs-33-2025-tu-versamenti-riscossione-akn-2026-07-20.xml"
+---
+
+# Dichiarazioni, versamenti unitari e compensazioni: quadro vigente consolidato
+
+## Esito dell'audit e versione
+
+**Data di consultazione:** 20 luglio 2026. I vecchi HTML verificano i metadati ma visualizzano integralmente soltanto l'art. 1. **D.P.R. 322/1998:** ELI `098G0373`, HTML a singola vigenza 2 luglio 2026, ultimo aggiornamento pubblicato 17 giugno 2025; AKN integrale di 12 articoli, expression `ita@2025-06-18`. **D.Lgs. 241/1997:** ELI `097G0277`; AKN integrale di 42 articoli, expression `ita@2026-01-10`. Il markup di abrogazione rinvia al D.Lgs. 33/2025, ma non basta a fissarne la decorrenza. **D.Lgs. 33/2025:** AKN ufficiale, alias ELI consolidato `20260523`; la FRBRExpression principale e quelle degli allegati sono `ita@2025-03-27`, mentre il markup successivo degli artt. 241 e 243 stabilisce che le abrogazioni e l'applicazione del testo unico operano dal 1° gennaio 2027.
+
+I claim su dichiarazioni sono verificati sui nodi dell'AKN D.P.R. 322/1998. Al cutoff, i claim vigenti su versamento e compensazione sono verificati sugli artt. 17-24 del D.Lgs. 241/1997; gli artt. 3 e 5-10 del D.Lgs. 33/2025 sono mappati separatamente come disciplina futura dal 1° gennaio 2027.
+
+## Funzione della dichiarazione
+
+**Dato normativo.** Il D.P.R. 322/1998 disciplina forma, sottoscrizione, presentazione e vicende delle dichiarazioni: l'art. 1 per redditi e IRAP, l'art. 2 per presentazione e dichiarazioni successive, l'art. 3 per modalità e soggetti della trasmissione; l'art. 8 contiene la disciplina della dichiarazione IVA. Le regole speciali prevalgono sulla mappa generale.
+
+**Sintesi didattica.** La dichiarazione non è il tributo: è l'atto con cui il contribuente rappresenta dati, componenti e risultanze secondo il modello normativamente previsto. Produce effetti propri e alimenta liquidazione e controllo. Presentazione, pagamento e successivo controllo sono fasi collegate ma distinte.
+
+## Presentazione e regole strutturali
+
+Il candidato deve ricostruire la sequenza: soggetto obbligato; dichiarazione e periodo; modello e sottoscrizione; canale e intermediario; ricevuta/prova della presentazione; conservazione; eventuale dichiarazione successiva. Gli artt. 1-3 del D.P.R. 322/1998 sostengono la struttura generale; per l'IVA la fonte dell'obbligo annuale è l'art. 8. L'art. 30 del D.P.R. 633/1972 riguarda conguaglio e rimborso dell'eccedenza, non fonda in generale la dichiarazione annuale.
+
+Modelli, istruzioni, software e scadenze appartengono al livello attuativo e mobile. Questa nota non li cristallizza.
+
+## Originaria, correttiva, integrativa e omessa
+
+- **Originaria:** prima dichiarazione presentata per il periodo e il tributo considerati.
+- **Correttiva nei termini:** espressione operativa per una nuova dichiarazione presentata entro il termine ordinario, che sostituisce la precedente; la qualificazione dipende dalle istruzioni ufficiali del modello applicabile, non è una categoria generale autosufficiente inventata dal manuale.
+- **Integrativa:** dichiarazione successiva oltre il termine ordinario nei casi e nei limiti previsti. Per redditi/IRAP rileva l'art. 2, commi 8 e 8-bis, D.P.R. 322/1998; per IVA l'art. 8, commi 6-bis e seguenti. Effetti sul debito, sul credito, sull'utilizzo e sul controllo non sono identici in ogni caso.
+- **Tardiva/omessa:** l'art. 2, comma 7, conserva validità alla dichiarazione presentata entro la finestra legale successiva, ferma la sanzione; oltre tale finestra la dichiarazione è considerata omessa, ma costituisce titolo per la riscossione delle imposte dovute in base agli imponibili indicati. Il regime IVA va coordinato con l'art. 8 e con la disciplina sanzionatoria vigente.
+
+**Nota di prudenza.** Correzione favorevole, correzione sfavorevole, emendabilità, rimborso e utilizzo del credito seguono condizioni e termini propri. Non è corretto affermare che ogni errore si corregga sempre con lo stesso tipo di integrativa o che il credito diventi immediatamente spendibile.
+
+## Versamento unitario e funzione del modello F24
+
+**Disciplina vigente al 20 luglio 2026.** L'art. 17 del D.Lgs. 241/1997 disciplina versamento unitario e compensazione; l'art. 18 i termini, l'art. 19 la delega e l'art. 20 la rateazione. L'art. 24 appartiene alle disposizioni transitorie e non va usato come fonte generale del modello F24.
+
+**Disciplina futura.** Il D.Lgs. 33/2025, art. 243, dispone che il testo unico si applica dal 1° gennaio 2027. L'art. 241 collega espressamente alla stessa data l'abrogazione degli artt. 17-28 e 30 del D.Lgs. 241/1997. Solo da quella data il routing passa agli artt. 3 (versamento unitario e compensazione), 5-7 (modalità, limiti e controlli secondo fattispecie), 8 (termini), 9 (delega, anche a saldo zero) e 10 (rateazione) del testo unico.
+
+**Sintesi didattica.** Il modello F24 è lo strumento unitario con cui si espongono debiti, crediti utilizzabili e saldo e si conferisce la delega di pagamento. Non è un repertorio da memorizzare per codici tributo. Un saldo nullo non rende irrilevante l'adempimento: trasmissione e controlli seguono le regole vigenti.
+
+## Compensazione verticale e orizzontale
+
+- **Verticale (interna):** il credito relativo a un tributo riduce un debito dello stesso tributo; la disciplina può operare nella liquidazione o dichiarazione del tributo.
+- **Orizzontale (esterna):** il credito relativo a un'imposta o contributo è usato, nel sistema del versamento unitario, contro debiti di diversa natura ammessi dall'art. 17 del D.Lgs. 241/1997.
+
+La distinzione è didattica e funzionale. Non autorizza l'uso di qualunque credito contro qualunque debito. Prima dell'utilizzo vanno verificati esistenza, spettanza, disponibilità, esposizione dichiarativa quando richiesta, perimetro compensabile, eventuali adempimenti preventivi, canale e cause ostative.
+
+**Esempio ammesso.** Un'eccedenza IVA può essere riportata, chiesta a rimborso o impiegata secondo le opzioni e condizioni applicabili; l'uso per ridurre un debito IVA e l'uso in F24 contro un debito diverso non sono la stessa operazione. L'esempio non afferma soglie o libera disponibilità.
+
+## Limiti e controlli senza automatismi
+
+La compensazione è soggetta a limiti quantitativi, temporali e procedurali e a controlli preventivi o successivi previsti dalla normativa vigente. Le condizioni possono dipendere da tipo e importo del credito, dichiarazione, visto o altra attestazione, situazione debitoria e canale telematico. Questa nota esclude valori numerici non verificati e non trasforma il controllo in diniego automatico.
+
+Un credito **non spettante** e un credito **inesistente** non sono sinonimi; qualificazione, recupero, sanzione e termini competono alla disciplina vigente e al capitolo responsabile. Anche lo scarto o la sospensione di una delega non equivalgono, senza la norma del caso, a una decisione definitiva sull'intero rapporto tributario.
+
+## Errore, correzione, rimborso e raccordo con controllo/sanzione
+
+La catena corretta è: individuare errore e dichiarazione interessata; stabilire se il termine ordinario è aperto; scegliere lo strumento previsto; rideterminare debito o credito; verificare pagamento, compensazione o rimborso; considerare controllo e sanzione separatamente. Dichiarazione integrativa, ravvedimento, istanza di rimborso e autotutela hanno funzioni diverse e non sono intercambiabili.
+
+Questa nota consolida classificazione e routing, non la disciplina completa di controllo, recupero e sanzioni. Nessuna correzione cancella automaticamente interessi o sanzioni; nessun credito dichiarato genera automaticamente rimborso o compensabilità.
+
+## Routing editoriale responsabile
+
+- **Capitolo 5 — accertamento, controlli e compliance:** selezione, liquidazione e controllo delle dichiarazioni; poteri e atti. Riceve il caso dopo la fase dichiarativa.
+- **Capitolo 5A — sanzioni:** qualificazione della violazione, elemento soggettivo quando rilevante, ravvedimento e conseguenze sanzionatorie.
+- **Capitolo 5B — riscossione:** recupero e riscossione delle somme risultanti, accertate o indebitamente compensate.
+- **Capitolo 6 — adempimenti fiscali:** funzione, presentazione e correzione della dichiarazione; versamento unitario; F24; distinzione verticale/orizzontale; sequenza errore-correzione. È il capitolo responsabile di questa nota.
+- **Capitolo 7 — contenzioso/rimedi:** tutela contro atti e dinieghi secondo la disciplina processuale e amministrativa pertinente.
+
+Il capitolo 6 non deve assorbire la disciplina completa dei capitoli 5, 5A, 5B e 7; questi ultimi non devono ripetere la meccanica ordinaria dell'adempimento.
+
+## Claim mobili esclusi o da datare
+
+Sono esclusi: scadenze annuali, calendario dei versamenti, soglie e massimali di compensazione o rimborso, codici tributo, modelli, campi, specifiche e canali telematici, importi per visto/attestazioni, sospensioni e cause ostative variabili. Se didatticamente necessari, vanno verificati su fonte ufficiale corrente e accompagnati dalla data di riferimento.
+
+## Mappa vigente al 20 luglio 2026
+
+| Claim | Fonte e articoli |
+|---|---|
+| forma e sottoscrizione | D.P.R. 322/1998, art. 1 |
+| presentazione, tardiva/omessa, integrativa redditi/IRAP | D.P.R. 322/1998, art. 2, commi 7, 8 e 8-bis |
+| trasmissione e intermediari | D.P.R. 322/1998, art. 3 |
+| dichiarazione e integrativa IVA | D.P.R. 322/1998, art. 8, in particolare commi 1, 6 e 6-bis ss. |
+| versamento unitario e compensazione | D.Lgs. 241/1997, art. 17 |
+| termini del versamento | D.Lgs. 241/1997, art. 18 |
+| delega di pagamento/F24, incluso saldo zero | D.Lgs. 241/1997, art. 19 |
+| rateazione | D.Lgs. 241/1997, art. 20 |
+| assistenza e visto di conformità | D.Lgs. 241/1997, artt. 35-39, secondo fattispecie |
+
+## Mappa futura dal 1° gennaio 2027
+
+| Claim | Fonte futura |
+|---|---|
+| decorrenza del testo unico | D.Lgs. 33/2025, art. 243 |
+| abrogazione degli artt. 17-28 e 30 D.Lgs. 241/1997 | D.Lgs. 33/2025, art. 241, comma 1, lett. t), dalla data dell'art. 243 |
+| versamento unitario e compensazione | D.Lgs. 33/2025, art. 3 |
+| modalità, limiti e controlli dei versamenti unitari | D.Lgs. 33/2025, artt. 5-7, secondo fattispecie |
+| termini, delega e rateazione | D.Lgs. 33/2025, artt. 8-10 |
+
+## Limiti e review
+
+Lo stato `consolidated` sostiene le distinzioni e la sequenza, non certifica regole mobili o ogni effetto dell'emendabilità. Prima della pubblicazione: review umana tributaria su dichiarazioni successive, crediti non spettanti/inesistenti, rimborso e raccordo sanzionatorio; verifica ufficiale datata per ogni termine, soglia o requisito operativo introdotto.
+
+## Riferimenti consolidati
+
+- [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]
+- [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
+- [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]
diff --git a/wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md b/wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md
new file mode 100644
index 0000000..1c9082f
--- /dev/null
+++ b/wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md
@@ -0,0 +1,124 @@
+---
+id: source-iva-dpr-633-1972-aggiornamento-2026-07-20
+type: source
+title: "IVA: sistema unionale e disciplina nazionale consolidata"
+status: consolidated
+domain: "concorsi pubblici italiani"
+topics: ["IVA", "diritto tributario UE", "adempimenti IVA"]
+entities: ["Unione europea", "Agenzia delle Entrate", "Normattiva", "EUR-Lex"]
+source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02", "sources/adempimenti-contabilita-civile-commerciale-m-fc02", "sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18"]
+book_refs: ["m-fc02-agenzie-fiscali"]
+confidence: 0.94
+updated_at: 2026-07-20T00:00:00+02:00
+created_at: 2026-07-20T00:00:00+02:00
+review_required: true
+canonical: true
+tags: ["source", "official-source", "iva", "module-code-m-fc02", "cutoff-2026-07-20"]
+source_type: official_legal_corpus
+source_url: "mixed:https://www.normattiva.it/eli/id/1972/11/11/072U0633/CONSOLIDATED/20260720|https://www.normattiva.it/eli/id/1998/04/16/098G0158/CONSOLIDATED/20260720|https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:02006L0112-20250414"
+source_date: "2026-07-20"
+audit_date: "2026-07-20"
+latest_official_update_checked: "D.P.R. 633/1972: ultimo aggiornamento pubblicato 22/05/2026; D.P.R. 100/1998: ultimo aggiornamento pubblicato 05/08/2024; direttiva 2006/112/CE: consolidamento 14/04/2025"
+authority_level: very_high
+raw_refs:
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva.html"
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-633-1972-iva-akn-2026-07-20.xml"
+  - "wiki/raw/m-fc02-agenzie-fiscali/normattiva-dpr-100-1998-liquidazioni-iva-akn-2026-07-20.xml"
+  - "wiki/raw/m-fc02-agenzie-fiscali/eurlex-direttiva-2006-112-iva-consolidata-2025-04-14.html"
+---
+
+# IVA: sistema unionale e disciplina nazionale consolidata
+
+## Esito dell'audit e versione
+
+**Data di consultazione:** 20 luglio 2026. **D.P.R. 633/1972:** il vecchio HTML certifica ELI `072U0633`, singola vigenza 1° luglio 2026 e ultimo aggiornamento pubblicato 22 maggio 2026, ma visualizza integralmente soltanto l'art. 1. Il nuovo export AKN integrale richiesto al 20 luglio contiene 172 elementi `article`; la `FRBRExpression` principale è `ita@2026-05-23`. I claim articolo-specifici nazionali sono stati verificati su questo AKN, non sul vecchio HTML. **D.P.R. 100/1998:** export AKN integrale di 2 articoli, expression `ita@2024-08-06`, ultimo aggiornamento dichiarato dalla pagina ufficiale 5 agosto 2024. **Versione unionale:** direttiva 2006/112/CE, CELEX `02006L0112-20250414`, ELI `dir/2006/112/2025-04-14`, consolidata al 14 aprile 2025 e indicata da EUR-Lex come versione corrente.
+
+Gli AKN mostrano anche abrogazioni e decorrenze differite. In particolare, i primi due commi dell'art. 27 del D.P.R. 633/1972 sono abrogati dal D.P.R. 100/1998: l'art. 27 non è usato come fonte vigente della liquidazione periodica. I raw sono prova di audit; questa nota è la base consolidata dopo verifica puntuale dei nodi richiamati.
+
+## Funzione dell'IVA e armonizzazione UE
+
+**Dato normativo.** La direttiva configura un sistema comune nel quale l'IVA, proporzionale al prezzo, grava sui consumi attraverso applicazione e detrazione nelle diverse fasi (direttiva 2006/112/CE, art. 1). Delimita operazioni soggette e soggetto passivo (artt. 2 e 9), mentre il D.P.R. 633/1972 assoggetta all'imposta le cessioni di beni e le prestazioni di servizi effettuate nel territorio dello Stato nell'esercizio di imprese, arti o professioni, nonché le importazioni da chiunque effettuate (art. 1).
+
+**Sintesi didattica.** L'IVA è armonizzata ma applicata mediante la disciplina nazionale negli spazi e secondo le opzioni consentite. La neutralità riguarda, in via strutturale, l'operatore che realizza operazioni con diritto a detrazione; non è assoluta: esenzioni, indetraibilità, pro rata, requisiti e rettifiche possono lasciare l'onere sull'operatore.
+
+## Presupposti e classificazione delle operazioni
+
+### Profilo oggettivo
+
+Le cessioni trasferiscono, di regola, la proprietà o costituiscono/trasferiscono diritti reali su beni; la norma include e sottrae fattispecie specifiche (D.P.R. 633/1972, art. 2; direttiva, art. 14). Le prestazioni sono operazioni verso corrispettivo dipendenti da obbligazioni di fare, non fare o permettere, con assimilazioni ed esclusioni previste dalla legge (D.P.R. 633/1972, art. 3; direttiva, artt. 24-26).
+
+### Profilo soggettivo
+
+L'esercizio d'impresa e l'esercizio di arti e professioni delimitano l'abitualità e l'ambito delle attività rilevanti (D.P.R. 633/1972, artt. 4 e 5). La nozione unionale di soggetto passivo è autonoma e guarda all'esercizio indipendente di un'attività economica (direttiva, art. 9).
+
+### Profilo territoriale
+
+Le regole di territorialità stabiliscono se la singola operazione si considera effettuata nel territorio dello Stato. Il rinvio responsabile è agli artt. 7-7-septies del D.P.R. 633/1972 e, nel sistema unionale, ai titoli relativi al luogo delle operazioni (in particolare artt. 31-61 della direttiva). Non basta che cedente o cliente siano italiani.
+
+### Imponibili, non imponibili, esenti ed escluse
+
+- **Imponibile:** ricorrono i presupposti e l'operazione concorre all'applicazione dell'imposta secondo le regole ordinarie.
+- **Non imponibile:** l'operazione è rilevante nel sistema IVA, ma la legge non applica l'imposta, tipicamente per assicurare la tassazione nel luogo di destinazione; gli esempi nazionali principali sono le cessioni all'esportazione e operazioni assimilate (D.P.R. 633/1972, artt. 8, 8-bis e 9). In linea generale conserva il diritto a detrazione, da verificare sulla fattispecie.
+- **Esente:** l'operazione rientra nel campo IVA ma beneficia di un'esenzione tipizzata (D.P.R. 633/1972, art. 10; direttiva, artt. 131 e seguenti). L'esenzione può limitare la detrazione degli acquisti: non equivale a non imponibilità.
+- **Esclusa/fuori campo:** manca un presupposto oppure una disposizione sottrae la fattispecie al campo applicativo (tra gli altri, artt. 2, 3 e 7-7-septies). Le somme escluse dal computo della base imponibile ai sensi dell'art. 15 non costituiscono, per ciò solo, una quinta categoria di operazioni.
+
+**Esempio ammesso.** Una cessione interna imponibile, un'esportazione non imponibile, una prestazione sanitaria esente se ricade nella previsione tipica e una prestazione priva di territorialità italiana producono conseguenze diverse su addebito e detrazione. L'esempio serve a classificare; aliquota, requisiti documentali e regime applicabile vanno verificati nel caso.
+
+## Effettuazione, fatto generatore ed esigibilità
+
+L'art. 6 del D.P.R. 633/1972 individua, per categorie di operazioni, il momento di effettuazione e disciplina anticipazioni collegate a pagamento o fatturazione. Nel quadro UE occorre distinguere fatto generatore ed esigibilità (direttiva, artt. 62-71). Didatticamente: prima si identifica la fattispecie, poi il momento rilevante, quindi quando l'Erario può esigere l'imposta. Non si estende la regola di una categoria a tutte le altre.
+
+## Base imponibile, debitore e rivalsa
+
+La base imponibile è costruita sul corrispettivo complessivo secondo le condizioni contrattuali, inclusi oneri e spese accessorie previsti dalla norma (D.P.R. 633/1972, art. 13; direttiva, artt. 72-92). L'art. 15 elenca somme che non concorrono alla base: esclusione dal computo e operazione fuori campo sono concetti distinti.
+
+L'art. 17 individua il debitore d'imposta e contiene ipotesi nelle quali gli obblighi ricadono sul cessionario o committente. L'art. 18 disciplina la rivalsa. **Sintesi didattica:** rivalsa e detrazione sono meccanismi diversi: la prima riguarda l'addebito dell'imposta al cliente, la seconda il recupero dell'imposta assolta sugli acquisti. Eventuali inversioni contabili richiedono la specifica fattispecie, non ammettono automatismi.
+
+## Detrazione e limiti concettuali
+
+Il diritto alla detrazione nasce e si esercita alle condizioni dell'art. 19; gli artt. 19-bis, 19-bis.1 e 19-bis.2 disciplinano, rispettivamente, percentuale di detrazione, ipotesi di indetraibilità e rettifica. Nel quadro UE rilevano gli artt. 167 e seguenti, con condizioni formali nell'art. 178.
+
+La formula operativa è: acquisto inerente ad attività economica, imposta dovuta/assolta, destinazione a operazioni che attribuiscono il diritto, documento e registrazione richiesti, assenza di limiti specifici. La detrazione non è un rimborso automatico né un diritto incondizionato; va distinta dalla compensazione di crediti nel versamento unitario.
+
+## Documentazione, registrazioni, liquidazione e dichiarazione
+
+La sequenza nazionale collega fatturazione (D.P.R. 633/1972, art. 21 e disposizioni contigue), registrazione delle operazioni attive (artt. 23 e 24), registrazione degli acquisti (art. 25), liquidazione e versamento periodico (D.P.R. 100/1998, art. 1) e dichiarazione annuale IVA (D.P.R. 322/1998, art. 8). L'art. 30 del D.P.R. 633/1972 disciplina il versamento di conguaglio e il rimborso dell'eccedenza: non è la fonte generale dell'obbligo dichiarativo. La direttiva disciplina fatturazione e obblighi dichiarativi, tra gli altri, agli artt. 217 e seguenti e 250 e seguenti.
+
+**Sintesi didattica.** Il documento alimenta i registri; le registrazioni consentono di confrontare imposta a debito e detraibile; la liquidazione determina il saldo periodico; la dichiarazione rappresenta annualmente i dati e le risultanze. Questa è una mappa funzionale, non un calendario: termini, modelli, specifiche telematiche e regimi speciali sono claim mobili da verificare per periodo.
+
+## Routing editoriale responsabile
+
+- **Capitolo 4 — diritto tributario e teoria dell'imposta:** funzione dell'IVA, armonizzazione, presupposti, categorie di operazioni, base imponibile, rivalsa, detrazione e neutralità non assoluta.
+- **Capitolo 6 — adempimenti fiscali:** sola sequenza operativa IVA di documentazione, registrazione, liquidazione e dichiarazione, raccordata a [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]. Non deve duplicare accertamento, controlli, sanzioni, riscossione o contabilità aziendale affidati ai capitoli 5, 5A, 5B e 7.
+
+## Claim mobili esclusi o da datare
+
+Questa nota non consolida aliquote, soglie, termini di trasmissione o versamento, modelli, codici tributo, specifiche telematiche, regimi temporanei, percentuali di detrazione o requisiti quantitativi. Possono entrare nel testo solo se necessari, verificati su fonte ufficiale per il periodo e marcati con data di riferimento.
+
+## Mappa articoli → claim
+
+| Claim | D.P.R. 633/1972 | Direttiva 2006/112/CE |
+|---|---|---|
+| sistema e operazioni soggette | art. 1 | artt. 1-2 |
+| cessioni/prestazioni e soggetti | artt. 2-5 | artt. 9, 14, 24-26 |
+| territorialità | artt. 7-7-septies | artt. 31-61 |
+| effettuazione/esigibilità | art. 6 | artt. 62-71 |
+| non imponibilità/esenzione | artt. 8, 8-bis, 9, 10 | artt. 131 ss. |
+| base ed esclusioni dal computo | artt. 13 e 15 | artt. 72-92 |
+| debitore e rivalsa | artt. 17-18 | art. 193 ss. |
+| detrazione, limiti, rettifica | artt. 19-19-bis.2 | artt. 167 ss., 178 |
+| fatture e registri | artt. 21, 23-25 | artt. 217 ss. |
+| liquidazione periodica | D.P.R. 100/1998, art. 1 | quadro di esigibilità e obblighi della direttiva |
+| dichiarazione annuale IVA | D.P.R. 322/1998, art. 8 | artt. 250 ss. |
+| conguaglio/rimborso dell'eccedenza | art. 30 | artt. 183 ss., secondo condizioni |
+
+## Limiti e review
+
+Il consolidamento sostiene la struttura concettuale, non certifica ogni regime o caso transfrontaliero. Prima della pubblicazione: review umana tributaria/UE per territorialità, esenzioni, inversione contabile, detrazione e decorrenze; verifica articolo-specifica se si introducono dati mobili.
+
+## Riferimenti consolidati
+
+- [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
+- [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]
+- [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]]
+- [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]

```