# VOL-03 Ricostruzione Ex Novo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ricostruire e sostituire il VOL-03 canonico con un corpus normativo ufficiale consolidato, due moduli completi e un indice editoriale analitico conforme al Metodo BANDO.

**Architecture:** Il flusso separa audit, acquisizione grezza immutabile, consolidamento wiki e proiezione editoriale. Ogni fonte scaricata genera una source note tracciabile; topic ed entity alimentano volume, moduli e front matter senza usare direttamente `wiki/raw/` come testo editoriale.

**Tech Stack:** Markdown/Obsidian, YAML frontmatter, PowerShell `Invoke-WebRequest`, Normattiva, EUR-Lex e portali istituzionali, Node.js/TypeScript, Git.

## Global Constraints

- Cut-off: **17 luglio 2026**.
- Lingua italiana e tono formale, professionale, didattico.
- Sostituzione canonica di VOL-03, M-FC02 e M-FC03.
- Raw sources esistenti immutabili; nuovi documenti in `wiki/raw/`.
- Nessun testo editoriale finale deriva direttamente dalle raw.
- Solo delta specialistico: nessuna duplicazione del nucleo B-PA di VOL-01.
- Conservare tutte le modifiche preesistenti non pertinenti.
- Stato finale `source_ready`; `review_required: true` per dati mobili e interpretazioni puntuali.
- Fonti prioritarie: Normattiva, EUR-Lex, Gazzetta Ufficiale, portali istituzionali, giurisprudenza ufficiale e ARAN.
- Richiamare e aggiornare LocalAgentMemory; registrare come warning l'attuale errore sui record senza `keywords`.

## Mappa dei file

- `wiki/raw/vol-03-fisco-dogane-previdenza-ispettivo/`: manifest trasversale.
- `wiki/raw/m-fc02-agenzie-fiscali/`: corpus fiscale e doganale.
- `wiki/raw/m-fc03-enti-non-economici/`: corpus previdenziale, ispettivo ed EPNE.
- `wiki/sources/m-fc02-*.md`, `wiki/sources/m-fc03-*.md`, `wiki/sources/vol-03-*.md`: consolidamento.
- `wiki/topics/`, `wiki/entities/`: conoscenza cumulativa.
- `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/`: volume commerciale.
- `wiki/books/moduli/m-fc02-agenzie-fiscali/`, `wiki/books/moduli/m-fc03-enti-non-economici/`: moduli.
- `wiki/reviews/vol-03-*.md`: audit e gap report.
- `wiki/index.md`, `wiki/log.md`: catalogo e traccia append-only.

---

### Task 1: Audit riproducibile

**Files:**
- Create: `wiki/reviews/vol-03-audit-iniziale-2026-07-17.md`
- Create: `wiki/raw/vol-03-fisco-dogane-previdenza-ispettivo/manifest-fonti-2026-07-17.csv`
- Read: dossier esterno e knowledge base persistente.

**Interfaces:**
- Consumes: dossier v4, specifica e corpus esistente.
- Produces: matrice `area;materia;profilo;fonte_richiesta;fonte_esistente;stato;azione`.

- [ ] **Step 1: Inventariare i file pertinenti**

```powershell
rg --files wiki/raw wiki/sources wiki/topics wiki/entities wiki/books | rg "vol-03|m-fc02|m-fc03|tribut|dogan|accis|previd|inps|inail|ispett|epne|ader"
```

Expected: elenco completo senza modifiche.

- [ ] **Step 2: Estrarre materie, profili, bandi e marker di incertezza**

```powershell
rg -n "^#|^\||DA VERIFICARE|http|Materia|Profil|Fonte|Bando" "C:\Users\aless\OneDrive\Desktop\VOLUMI LIBRO PROG\VOL-03-fisco-dogane-previdenza-ispettivo-dossier-v4 (1).md"
```

Expected: nessun elemento del dossier escluso.

- [ ] **Step 3: Scrivere manifest e audit**

Il manifest usa: `module;area;source_id;title;authority;url;local_path;source_date;retrieved_at;status;sha256;notes`. L'audit classifica ogni fonte come `riutilizzabile`, `da_aggiornare`, `mancante`, `fuori_perimetro` o `conflitto`.

- [ ] **Step 4: Verificare e committare selettivamente**

```powershell
rg -n "mancante|da_aggiornare|conflitto|fuori_perimetro" wiki/reviews/vol-03-audit-iniziale-2026-07-17.md
git add -- wiki/reviews/vol-03-audit-iniziale-2026-07-17.md wiki/raw/vol-03-fisco-dogane-previdenza-ispettivo/manifest-fonti-2026-07-17.csv
git commit -m "docs(vol-03): audit iniziale del corpus"
```

Expected: ogni lacuna ha fonte-obiettivo o rinvio motivato.

### Task 2: Corpus ufficiale M-FC02

**Files:**
- Modify: manifest.
- Create: documenti in `wiki/raw/m-fc02-agenzie-fiscali/`.
- Create/Modify: `wiki/sources/m-fc02-*.md`.

**Interfaces:**
- Consumes: lacune M-FC02.
- Produces: corpus e source notes per tributario, riscossione, dogane, accise, monopoli, catasto, audit e bandi.

- [ ] **Step 1: Chiudere l'elenco minimo**

Includere Costituzione artt. 23 e 53; L. 212/2000; TUIR; DPR 633/1972; DPR 600/1973; DPR 602/1973; D.Lgs. 546/1992; D.Lgs. 471/1997; D.Lgs. 472/1997; D.Lgs. 74/2000; D.Lgs. 300/1999; riforma fiscale 2023-2026 pertinente; CDU Reg. (UE) 952/2013 e atti collegati; normativa nazionale doganale vigente; accise; atti ADM su giochi; fonti AdER; bandi AE, ADM e AdER 2023-2026.

- [ ] **Step 2: Scaricare ogni fonte mancante**

```powershell
$headers = @{ 'User-Agent' = 'Mozilla/5.0 ConcorsoBookOS/1.0' }
Invoke-WebRequest -Uri '<URL_UFFICIALE>' -Headers $headers -OutFile '<PERCORSO_ESATTO>' -UseBasicParsing -TimeoutSec 45
Get-FileHash -Algorithm SHA256 -LiteralPath '<PERCORSO_ESATTO>'
```

Expected: file non vuoto, hash nel manifest; i fallimenti sono marcati `download_failed`.

- [ ] **Step 3: Consolidare le source notes**

Ogni nota contiene frontmatter standard, URL, data, autorita, sintesi, disposizioni rilevanti, capitoli, dati mobili, topic/entity e percorso raw.

- [ ] **Step 4: Verificare e committare**

```powershell
rg -L "source_url:" wiki/sources/m-fc02-*.md
rg -L "authority_level:" wiki/sources/m-fc02-*.md
git add -- wiki/raw/m-fc02-agenzie-fiscali wiki/raw/vol-03-fisco-dogane-previdenza-ispettivo/manifest-fonti-2026-07-17.csv wiki/sources/m-fc02-*.md
git commit -m "docs(m-fc02): acquisisce fonti ufficiali"
```

Expected: nessuna nuova nota priva di provenienza o autorita.

### Task 3: Corpus ufficiale M-FC03

**Files:**
- Modify: manifest.
- Create: documenti in `wiki/raw/m-fc03-enti-non-economici/`.
- Create/Modify: `wiki/sources/m-fc03-*.md`.

**Interfaces:**
- Consumes: lacune M-FC03.
- Produces: corpus per previdenza, INAIL, vigilanza, legislazione sociale, EPNE, CCNL e bandi.

- [ ] **Step 1: Chiudere l'elenco minimo**

Includere R.D.L. 1827/1935; DPR 639/1970; L. 153/1969; L. 335/1995; D.Lgs. 479/1994; DPR 1124/1965; D.Lgs. 38/2000; L. 222/1984; DPCM 159/2013; D.Lgs. 148/2015; D.Lgs. 124/2004; D.Lgs. 81/2008; L. 689/1981; D.Lgs. 758/1994; fonti INL; statuti/regolamenti INPS-INAIL; CCNL vigente; PIAO EPNE; bandi INPS, INAIL, INL ed EPNE 2023-2026.

- [ ] **Step 2: Scaricare, calcolare hash e aggiornare manifest**

Usare il comando esplicito del Task 2. Separare normativa, bandi, circolari, statuti, regolamenti, PIAO e guide.

- [ ] **Step 3: Consolidare le source notes**

Separare previdenza/prestazioni, contribuzione, INAIL, ISEE, ammortizzatori, vigilanza, sicurezza, sanzioni, EPNE, bilancio/controlli, personale/CCNL, servizi digitali e bandi.

- [ ] **Step 4: Verificare e committare**

```powershell
rg -L "source_url:" wiki/sources/m-fc03-*.md
rg -L "authority_level:" wiki/sources/m-fc03-*.md
git add -- wiki/raw/m-fc03-enti-non-economici wiki/raw/vol-03-fisco-dogane-previdenza-ispettivo/manifest-fonti-2026-07-17.csv wiki/sources/m-fc03-*.md
git commit -m "docs(m-fc03): acquisisce fonti ufficiali"
```

Expected: ogni nuovo raw ha hash e source note corrispondente.

### Task 4: Consolidamento wiki

**Files:**
- Create/Modify: topic ed entity pertinenti.
- Create: `wiki/sources/vol-03-corpus-ufficiale-2026-07-17.md`.
- Modify: `wiki/index.md`, `wiki/log.md`.

**Interfaces:**
- Consumes: source notes dei Task 2-3.
- Produces: knowledge pack per la scrittura editoriale.

- [ ] **Step 1: Creare o aggiornare topic/entity canonici**

Ogni topic collega fonti, entity, gerarchia e capitoli; ogni entity descrive identita, fonti istitutive, funzioni concorsuali e relazioni.

- [ ] **Step 2: Creare la mappa trasversale del corpus**

La nota elenca per modulo area, fonti primarie, prassi, bandi, copertura e dati mobili.

- [ ] **Step 3: Aggiornare indice e log append-only**

Non cancellare eventi precedenti e non duplicare pagine canoniche.

- [ ] **Step 4: Verificare e committare**

```powershell
rg -n "\[\[(sources|topics|entities)/[^]]+\]\]" wiki/sources wiki/topics wiki/entities
git add -- wiki/sources/vol-03-corpus-ufficiale-2026-07-17.md wiki/topics wiki/entities wiki/index.md wiki/log.md
git commit -m "docs(vol-03): consolida knowledge base"
```

Expected: ogni source note collega topic/entity e ogni topic nuovo collega almeno una fonte.

### Task 5: Ricostruzione canonica

**Files:**
- Replace/Modify: volume `index.md`, `planning/`, `front-matter/`.
- Replace/Modify: M-FC02 e M-FC03 `index.md`, `planning/`, `front-matter/`, schede in `chapters/`.

**Interfaces:**
- Consumes: struttura madre, design system e knowledge pack consolidato.
- Produces: volume e moduli `source_ready`.

- [ ] **Step 1: Ricostruire l'architettura**

Ordine: sezioni editoriali, orientamento, M-FC02, M-FC03, strumenti condivisi, appendici, registro aggiornamenti e rinvii.

- [ ] **Step 2: Scrivere l'indice analitico M-FC02**

Per ogni capitolo: finalita, profili, sezioni/sottosezioni, output, caso/errore/quiz, fonti, rinvii e review. Sequenza: ente e bando; sistema tributario; adempimento; controllo/compliance; riscossione/contenzioso; dogane/accise/monopoli; competenze economico-contabili; laboratorio.

- [ ] **Step 3: Scrivere l'indice analitico M-FC03**

Usare gli stessi campi. Sequenza: enti e bando; previdenza/contribuzione/prestazioni; INAIL; vigilanza/tecnica ispettiva/sanzioni; EPNE/governance/servizi/controlli; laboratorio.

- [ ] **Step 4: Riscrivere le sei sezioni editoriali**

Creare contenuto effettivo per Servizi digitali, Frontespizio, Copyright e note editoriali, Sommario, Premessa e Indice. Evitare placeholder e promesse assolute.

- [ ] **Step 5: Allineare metadati e rinvii**

Ogni modulo dichiara `module_code`, `module_family`, `companion_to: il-metodo-bando`, `draft_stage: source-ready`, fonti, libri e review.

- [ ] **Step 6: Verificare e committare**

```powershell
rg -n "B-PA0|B-PA10|B-PA11|Cfr\. VOL-01|VOL-07|VOL-08|VOL-09|VOL-12" wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo wiki/books/moduli/m-fc02-agenzie-fiscali wiki/books/moduli/m-fc03-enti-non-economici
git add -- wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo wiki/books/moduli/m-fc02-agenzie-fiscali wiki/books/moduli/m-fc03-enti-non-economici
git commit -m "docs(vol-03): ricostruisce volume e moduli"
```

Expected: materie comuni rinviate, non duplicate.

### Task 6: Gap report e collaudo

**Files:**
- Create: `wiki/reviews/vol-03-gap-report-2026-07-17.md`.
- Modify: `wiki/log.md`.
- Modify through service: `wiki/memory/agent/`.

**Interfaces:**
- Consumes: risultato dei Task 1-5.
- Produces: evidenza finale di copertura e tracciabilita.

- [ ] **Step 1: Costruire la matrice finale**

Colonne: `modulo | materia | profili | capitoli | fonti primarie | prassi/bandi | stato | dati mobili | review umana`. Stati: `completa`, `parziale_motivata`, `rinvio_cross_family`, `review_necessaria`.

- [ ] **Step 2: Scansionare placeholder e verificare il progetto**

```powershell
rg -n "TBD|TODO|DA VERIFICARE|placeholder|fonte da inserire" wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo wiki/books/moduli/m-fc02-agenzie-fiscali wiki/books/moduli/m-fc03-enti-non-economici wiki/sources/m-fc02-*.md wiki/sources/m-fc03-*.md
npm run typecheck
npm test -- --run
```

Expected: nessun placeholder non spiegato; distinguere errori preesistenti da regressioni.

- [ ] **Step 3: Verificare raw e diff**

```powershell
Get-ChildItem -File -Recurse wiki/raw/m-fc02-agenzie-fiscali,wiki/raw/m-fc03-enti-non-economici | Where-Object Length -eq 0
git status --short
git diff --check
git diff --stat
```

Expected: nessun file vuoto e nessuna modifica accidentale fuori scope.

- [ ] **Step 4: Richiamare e registrare LocalAgentMemory**

Tentare il servizio canonico. Se persiste l'errore `memory.keywords`, registrarlo nel gap report e nel log senza modificare il servizio. La cattura finale indica obiettivo, fonti, percorsi sostituiti e review residue.

- [ ] **Step 5: Commit finale e consegna**

```powershell
git add -- wiki/reviews/vol-03-gap-report-2026-07-17.md wiki/log.md wiki/memory/agent
git commit -m "docs(vol-03): completa collaudo"
```

La consegna riporta indice, fonti nuove/riutilizzate, download falliti, copertura, test, warning memoria, dati mobili e review umana.

