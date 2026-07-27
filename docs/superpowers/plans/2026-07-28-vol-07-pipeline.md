# VOL-07 Source Ingest and Pipeline Start Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Importare integralmente il dossier VOL-07 nel wiki, registrare tutte le fonti e le materie richieste e avviare tramite CLI lo step 00 della pipeline editoriale.

**Architecture:** Il dossier viene conservato come raw immutabile e sintetizzato in una source note editoriale. Un aggregatore di volume collega i quattro moduli esistenti, un inventario registra tutte le fonti candidate e una matrice globale registra tutte le materie; la pipeline parte con le sole fasi A e B e viene inizializzata esclusivamente dal CLI.

**Tech Stack:** Markdown/Obsidian wiki, PowerShell, Node.js 20+, TypeScript, `tsx`, Vitest, CLI `npm run pipeline`.

## Global Constraints

- Source file: `C:\Users\info\OneDrive\Desktop\# VOL-07 – Sanità amministrativa e.txt`.
- Source SHA-256: `4045E18DE2B1AC2B0760047821D48683934321C98499E3A5446481769E0C2466`.
- Cut-off date: `2026-07-28`.
- Responsabile normativo: `Alberto Brando`.
- Responsabile editoriale: `Alberto Brando`.
- Module order: `M-SA02`, `M-SA01`, `M-SA03`, `M-SA04`.
- Initial pipeline phases: `[A, B]`.
- Il dossier è una fonte editoriale di pianificazione, non una fonte normativa primaria.
- Tutte le voci di `OUTPUT A` entrano nell'inventario, anche quando non hanno un URL.
- Il testo editoriale finale non può derivare direttamente da `wiki/raw/`.
- Le fonti generali già consolidate in VOL-01 vanno rinviate senza duplicazione.
- `mancante`, `solo-nominato` e `parziale` restano blocker reali.
- Non modificare manualmente `pipeline/VOL-07/run-state.json`.
- Preservare `.claude/settings.local.json` e ogni altra modifica non pertinente dell'utente.
- Non avviare le fasi C, D, E o F in questo piano.

---

### Task 1: Preparare e verificare l'ambiente della pipeline

**Files:**
- Read: `package.json`
- Read: `.env.example`
- Create if absent and keep ignored: `.env.local`
- Verify: `node_modules/`

**Interfaces:**
- Consumes: repository corrente sul branch `main`.
- Produces: ambiente in cui `npm run pipeline -- doctor` può eseguire tutti i controlli.

- [ ] **Step 1: Registrare il baseline Git e Node**

Run:

```powershell
git status -sb
node --version
npm --version
```

Expected:

- branch `main`;
- solo modifiche già note dell'utente;
- Node conforme a `package.json` (`>=20.11.0`).

- [ ] **Step 2: Verificare che il doctor fallisca per cause ambientali note**

Run:

```powershell
npm run pipeline -- doctor
```

Expected before setup: FAIL se `tsx`, `.env.local` o Chromium non sono disponibili. Conservare l'elenco esatto dei blocker.

- [ ] **Step 3: Installare le dipendenze bloccanti**

Run:

```powershell
npm ci
```

Expected: exit code 0 e presenza di `node_modules/tsx`.

- [ ] **Step 4: Creare `.env.local` soltanto se assente**

Run:

```powershell
if (-not (Test-Path -LiteralPath '.env.local')) {
  Copy-Item -LiteralPath '.env.example' -Destination '.env.local'
}
```

Expected: `.env.local` presente con `WRITER_PROVIDER=codex`; nessuna chiave segreta inventata.

- [ ] **Step 5: Installare Chromium soltanto se il doctor lo richiede**

Run:

```powershell
npx playwright install chromium
```

Expected: browser Chromium disponibile per i controlli del doctor.

- [ ] **Step 6: Verificare ambiente e baseline test**

Run:

```powershell
npm run pipeline -- doctor
npx vitest run tests/pipeline
npm run typecheck
```

Expected:

- doctor: `Ambiente pronto`;
- test pipeline: tutti passati;
- typecheck: exit code 0.

- [ ] **Step 7: Configurare l'identità Git locale già usata dalla repository**

Run:

```powershell
git config --local user.name "Alberto Brando 1991"
git config --local user.email "albertobrando1991@gmail.com"
git config --local --get user.name
git config --local --get user.email
```

Expected: identità uguale a quella dei commit recenti. La configurazione resta locale alla repository.

No commit: `node_modules`, browser, `.env.local` e `.git/config` sono ambiente locale.

---

### Task 2: Acquisire il dossier raw e creare la source note editoriale

**Files:**
- Create: `wiki/raw/business/vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt`
- Create: `wiki/sources/vol-07-dossier-fonti-materie-sanita-2026-07-28.md`

**Interfaces:**
- Consumes: dossier esterno verificato dalla Task 1.
- Produces: raw immutabile e source note richiamabile da topic, entità, volume, moduli e matrici.

- [ ] **Step 1: Verificare che il raw non sia già presente**

Run:

```powershell
Test-Path -LiteralPath 'wiki\raw\business\vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt'
```

Expected before ingest: `False`.

- [ ] **Step 2: Copiare il file senza trasformazioni**

Run:

```powershell
Copy-Item -LiteralPath 'C:\Users\info\OneDrive\Desktop\# VOL-07 – Sanità amministrativa e.txt' `
  -Destination 'wiki\raw\business\vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt'
```

Expected: copia byte-per-byte.

- [ ] **Step 3: Verificare l'impronta del raw**

Run:

```powershell
$sourceHash = (Get-FileHash -LiteralPath 'C:\Users\info\OneDrive\Desktop\# VOL-07 – Sanità amministrativa e.txt' -Algorithm SHA256).Hash
$rawHash = (Get-FileHash -LiteralPath 'wiki\raw\business\vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt' -Algorithm SHA256).Hash
$sourceHash
$rawHash
if ($sourceHash -ne $rawHash) { throw 'Hash mismatch durante ingest VOL-07' }
```

Expected: entrambi gli hash uguali a `4045E18DE2B1AC2B0760047821D48683934321C98499E3A5446481769E0C2466`.

- [ ] **Step 4: Creare la source note**

Create `wiki/sources/vol-07-dossier-fonti-materie-sanita-2026-07-28.md` con questo frontmatter:

```yaml
---
id: source-vol-07-dossier-fonti-materie-sanita-2026-07-28
type: source
title: "VOL-07 - Dossier fonti, materie e indice della sanità"
status: processed
domain: "concorsi pubblici italiani"
topics: ["sanità amministrativa", "professioni sanitarie", "servizio sanitario nazionale", "concorsi sanitari"]
entities: ["Servizio sanitario nazionale", "Ministero della Salute", "Agenas", "Istituto Superiore di Sanità", "Azienda sanitaria"]
source_refs: []
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie", "m-sa01-sanita-amministrativa", "m-sa02-professioni-sanitarie", "m-sa03-dirigenza-medica-sanitaria", "m-sa04-tecnici-sanitari-prevenzione"]
confidence: 0.84
updated_at: 2026-07-28T00:00:00+02:00
created_at: 2026-07-28T00:00:00+02:00
review_required: true
canonical: true
tags: ["source", "vol-07", "dossier-editoriale", "source-map", "coverage-map"]
source_type: user_editorial_dossier
source_url: ""
source_date: 2026-07-28
authority_level: editorial_planning_input
---
```

Il corpo deve contenere esattamente queste sezioni:

```markdown
# VOL-07 - Dossier fonti, materie e indice della sanità

## Sintesi
## Perimetro e moduli
## Materie richieste
## Mappa delle fonti
## Profili e prove
## Indice proposto
## Appendici e verticali
## Gap dichiarati
## Capitoli collegati
## Stato revisione
```

La sezione `Stato revisione` deve dire che il dossier è canonico per pianificazione e copertura, ma ogni fonte normativa, contrattuale, professionale, giurisprudenziale o di bando richiede acquisizione e verifica autonoma.

- [ ] **Step 5: Verificare la source note**

Run:

```powershell
rg -n "^id: source-vol-07|^## (Sintesi|Perimetro e moduli|Materie richieste|Mappa delle fonti|Profili e prove|Indice proposto|Appendici e verticali|Gap dichiarati|Capitoli collegati|Stato revisione)$" wiki\sources\vol-07-dossier-fonti-materie-sanita-2026-07-28.md
rg -n "fonte normativa primaria|verifica autonoma|M-SA01|M-SA02|M-SA03|M-SA04" wiki\sources\vol-07-dossier-fonti-materie-sanita-2026-07-28.md
git diff --check
```

Expected: tutte le sezioni presenti, quattro moduli presenti, nessun errore whitespace.

- [ ] **Step 6: Commit**

```powershell
git add -- wiki/raw/business/vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt wiki/sources/vol-07-dossier-fonti-materie-sanita-2026-07-28.md
git commit -m "docs(wiki): acquisisci dossier fonti VOL-07"
```

---

### Task 3: Registrare l'inventario completo delle fonti e il grafo sanitario

**Files:**
- Create: `wiki/topics/sanita-amministrativa-professioni-sanitarie.md`
- Modify: `wiki/topics/profili-sanita-scuola-universita.md`
- Create: `wiki/entities/servizio-sanitario-nazionale.md`
- Create: `wiki/entities/ministero-della-salute.md`
- Create: `wiki/entities/agenas.md`
- Create: `wiki/entities/istituto-superiore-di-sanita.md`
- Create: `wiki/entities/azienda-sanitaria.md`
- Create: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/03-mappa-fonti-specialistiche.md`

**Interfaces:**
- Consumes: source note della Task 2 e `OUTPUT A` del raw.
- Produces: inventario verificabile con stato per ogni fonte candidata e pagine canoniche per il grafo.

- [ ] **Step 1: Creare la mappa delle fonti con schema fisso**

Prima creare il percorso:

```powershell
New-Item -ItemType Directory -Force -Path 'wiki\books\volumi\vol-07-sanita-amministrativa-professioni-sanitarie\planning'
```

Create `planning/03-mappa-fonti-specialistiche.md` con frontmatter `type: review`, `issue_type: source-audit`, `severity: critical`, `status: working`, `canonical: false`, collegato a VOL-07 e ai quattro moduli.

Usare questa tabella:

```markdown
| ID | Categoria | Fonte/estremi | Autorità | URL ufficiale | Moduli | Materie | Stato | Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Inserire tutte le righe del dossier:

- normativa primaria: 11 righe;
- normativa secondaria e regolamenti: 13 righe;
- contrattazione collettiva: 3 righe;
- soft law e linee guida: 10 righe;
- giurisprudenza: 9 aree;
- fonti operative: 14 righe;
- bandi iniziali: 4 righe;
- manualistica e dottrina: 10 categorie.

Stati iniziali ammessi:

- `da_acquisire`: estremi o documento da reperire;
- `da_verificare`: documento noto ma vigenza, versione o pertinenza da verificare;
- `consolidata`: solo se esiste già una source note verificata nel wiki;
- `superata`: disciplina esplicitamente sostituita, con rinvio alla fonte vigente;
- `rinviata_VOL-01`: fonte generale già consolidata nel volume base.

Non usare `consolidata` per i soli tre URL finali del dossier senza verifica ufficiale.

- [ ] **Step 2: Verificare il numero minimo di righe dell'inventario**

Run:

```powershell
$rows = Select-String -LiteralPath 'wiki\books\volumi\vol-07-sanita-amministrativa-professioni-sanitarie\planning\03-mappa-fonti-specialistiche.md' -Pattern '^\| (NP|NS|CC|SL|GIU|OP|BAN|DOT)-'
$rows.Count
```

Expected: almeno 74 righe (`11+13+3+10+9+14+4+10`).

- [ ] **Step 3: Creare il topic sanitario canonico**

Create `wiki/topics/sanita-amministrativa-professioni-sanitarie.md` con:

- sintesi del delta rispetto a VOL-01;
- moduli M-SA01–M-SA04;
- materie comuni e specialistiche;
- fonti collegate;
- capitoli/volumi collegati;
- stato revisione e gap.

Frontmatter minimo:

```yaml
id: topic-sanita-amministrativa-professioni-sanitarie
type: topic
status: working
canonical: true
review_required: true
parent_topics: ["famiglie concorsuali", "moduli specialistici"]
child_topics: ["organizzazione sanitaria", "professioni sanitarie", "responsabilità sanitaria", "documentazione sanitaria"]
```

- [ ] **Step 4: Creare le cinque entity page**

Ogni entity page deve contenere:

```markdown
## Identità
## Ruolo nel VOL-07
## Fonti collegate
## Moduli e capitoli collegati
## Stato revisione
```

Non inserire date, competenze puntuali o assetti correnti non presenti in source notes verificate.

- [ ] **Step 5: Aggiornare il topic trasversale esistente**

In `wiki/topics/profili-sanita-scuola-universita.md`:

- aggiungere la source note VOL-07 a `source_refs` e `## Fonti`;
- aggiungere VOL-07 e M-SA01–M-SA04 a `book_refs`/`chapter_refs`;
- collegare il nuovo topic sanitario;
- aggiornare `updated_at` a `2026-07-28T00:00:00+02:00`;
- preservare integralmente scuola, ATA e università.

- [ ] **Step 6: Verificare link e contenuto**

Run:

```powershell
rg -n "source-vol-07-dossier|M-SA01|M-SA02|M-SA03|M-SA04" wiki\topics\sanita-amministrativa-professioni-sanitarie.md wiki\topics\profili-sanita-scuola-universita.md wiki\entities\servizio-sanitario-nazionale.md wiki\entities\ministero-della-salute.md wiki\entities\agenas.md wiki\entities\istituto-superiore-di-sanita.md wiki\entities\azienda-sanitaria.md
rg -n "TODO|TBD|\\[DA COMPLETARE\\]|lorem ipsum" wiki\topics\sanita-amministrativa-professioni-sanitarie.md wiki\entities
git diff --check
```

Expected: collegamenti presenti; nessun segnaposto; whitespace pulito.

- [ ] **Step 7: Commit**

```powershell
git add -- wiki/topics/sanita-amministrativa-professioni-sanitarie.md wiki/topics/profili-sanita-scuola-universita.md wiki/entities/servizio-sanitario-nazionale.md wiki/entities/ministero-della-salute.md wiki/entities/agenas.md wiki/entities/istituto-superiore-di-sanita.md wiki/entities/azienda-sanitaria.md wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/03-mappa-fonti-specialistiche.md
git commit -m "docs(wiki): mappa fonti e grafo sanitario VOL-07"
```

---

### Task 4: Creare aggregatore, dossier source-ready e matrice didattica

**Files:**
- Create: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md`
- Create: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/01-dossier-source-ready.md`
- Create: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`

**Interfaces:**
- Consumes: source note, inventario, topic ed entity page delle Task 2–3.
- Produces: architettura di volume e baseline di copertura usate dalle fasi A/B.

- [ ] **Step 1: Creare l'index dell'aggregatore**

Usare frontmatter:

```yaml
---
id: volume-vol-07-sanita-amministrativa-professioni-sanitarie
type: volume
title: "VOL-07 - Sanità amministrativa e professioni sanitarie"
status: source_ready
domain: "concorsi pubblici italiani"
topics: ["sanità amministrativa", "professioni sanitarie", "servizio sanitario nazionale", "concorsi sanitari"]
entities: ["Servizio sanitario nazionale", "Ministero della Salute", "Agenas", "Istituto Superiore di Sanità", "Azienda sanitaria"]
source_refs: ["sources/vol-07-dossier-fonti-materie-sanita-2026-07-28"]
book_refs: ["m-sa02-professioni-sanitarie", "m-sa01-sanita-amministrativa", "m-sa03-dirigenza-medica-sanitaria", "m-sa04-tecnici-sanitari-prevenzione", "il-metodo-bando"]
confidence: 0.84
updated_at: 2026-07-28T00:00:00+02:00
created_at: 2026-07-28T00:00:00+02:00
review_required: true
canonical: true
tags: ["volume", "volume-code-vol-07", "sanita", "source-ready"]
book_id: vol-07-sanita-amministrativa-professioni-sanitarie
volume_code: VOL-07
module_codes: ["M-SA01", "M-SA02", "M-SA03", "M-SA04"]
module_family: sanita
companion_to: il-metodo-bando
draft_stage: source-ready
last_compiled_from: ["sources/vol-07-dossier-fonti-materie-sanita-2026-07-28"]
---
```

Il corpo deve descrivere identità, quattro moduli, principio delta VOL-01, documenti canonici, ordine di sviluppo, cut-off e review.

- [ ] **Step 2: Creare il dossier source-ready**

`planning/01-dossier-source-ready.md` deve conservare in forma operativa:

- sei fasi del dossier;
- tredici profili dichiarati;
- campione bandi e gap;
- materie per ciascun modulo;
- decisioni di collocazione;
- quindici capitoli proposti;
- sei appendici;
- cinque verticali esterni;
- checklist v4;
- rinvii cross-family.

Non dichiarare frequenze numeriche: usare `ND` come nel dossier.

- [ ] **Step 3: Creare la matrice globale**

Usare le colonne canoniche:

```markdown
| # | Famiglia/profilo | Materia | Concetto atomico | Peso | Fonti consolidate | Collocazione prevista | Copertura teorica | Applicazione | Output | Verifica | Stato | Review normativa | Destinazione rinvio |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Creare almeno una riga per ciascuna materia esplicita:

- comuni: SSN; aziende sanitarie; LEA; documentazione; privacy/accesso; consenso; deontologia; responsabilità; rischio clinico; sicurezza lavoro sanitaria; qualità/accreditamento; flussi informativi;
- M-SA01: organizzazione; atti/procedimenti; documentazione/accesso; front-office; contabilità sanitaria; budget; procurement; farmaci/dispositivi/magazzino/ciclo passivo; flussi informativi;
- M-SA02: scienze infermieristiche; tecniche assistenziali; clinica/emergenza; prevenzione/presa in carico; discipline professionali; evidenze scientifiche; igiene/epidemiologia; controlli/verbalizzazione/sanzioni;
- M-SA03: disciplina clinica; casi clinici; linee guida/appropriatezza; clinical governance; programmazione; epidemiologia/sanità pubblica; HTA/qualità/accreditamento; rischio clinico; discipline sanitarie non mediche;
- M-SA04: laboratorio; biochimica/microbiologia/ematologia applicate; qualità/biosicurezza; radiologia; dosimetria/radioprotezione; qualità immagine/apparecchiature; tecnologie biomedicali; dispositivi/manutenzione; rischio tecnologico.

Stato iniziale:

- `rinviato` solo per B-PA con destinazione VOL-01 precisa e già completa;
- `mancante` per materia specialistica non ancora sviluppata;
- `parziale` soltanto se esiste testo reale ma incompleto.

- [ ] **Step 4: Verificare la completezza strutturale**

Run:

```powershell
rg -n "^# VOL-07|^## (Moduli|Principio delta|Documenti canonici|Ordine di sviluppo|Cut-off e review)$" wiki\books\volumi\vol-07-sanita-amministrativa-professioni-sanitarie\index.md
rg -n "^## (Perimetro|Profili|Campione bandi|Materie|Collocazione|Indice|Appendici|Verticali|Checklist)$" wiki\books\volumi\vol-07-sanita-amministrativa-professioni-sanitarie\planning\01-dossier-source-ready.md
$matrixRows = Select-String -LiteralPath 'wiki\books\volumi\vol-07-sanita-amministrativa-professioni-sanitarie\planning\02-matrice-copertura-didattica.md' -Pattern '^\| \d+ \|'
$matrixRows.Count
git diff --check
```

Expected: almeno 47 righe di materia, sezioni presenti, diff pulito.

- [ ] **Step 5: Commit**

```powershell
git add -- wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/index.md wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/01-dossier-source-ready.md wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/02-matrice-copertura-didattica.md
git commit -m "docs(wiki): crea aggregatore e matrice VOL-07"
```

---

### Task 5: Collegare i quattro moduli e aggiornare indice e log

**Files:**
- Modify: `wiki/books/moduli/m-sa01-sanita-amministrativa/index.md`
- Modify: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/index.md`
- Modify: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/index.md`
- Modify: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/00-piano-editoriale.md`
- Modify: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/index.md`
- Modify: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/00-piano-editoriale.md`
- Modify: `wiki/index.md`
- Modify append-only: `wiki/log.md`

**Interfaces:**
- Consumes: aggregatore, source note e matrice globale.
- Produces: navigazione bidirezionale e tracciamento dell'ingest.

- [ ] **Step 1: Aggiornare gli index dei moduli**

Per tutti e quattro:

- aggiungere la source note VOL-07 a `source_refs`;
- aggiungere l'aggregatore a `book_refs`;
- aggiungere il topic sanitario;
- aggiornare `updated_at`;
- aggiungere link a dossier source-ready, matrice globale e mappa fonti;
- preservare `book_id`, `module_code`, `module_family`, `companion_to` e lo stato scaffold finché i capitoli non esistono.

- [ ] **Step 2: Aggiornare i quattro piani editoriali**

Per tutti e quattro:

- sostituire la lista generica delle fonti con rinvio a inventario e matrice;
- riportare le materie specifiche del dossier;
- indicare ordine `M-SA02 → M-SA01 → M-SA03 → M-SA04`;
- mantenere `## Testo editoriale` non sviluppato;
- non scrivere capitoli o claim normativi.

- [ ] **Step 3: Aggiornare `wiki/index.md`**

Aggiungere cataloghi navigabili per:

- volume VOL-07;
- source note del dossier;
- topic sanitario;
- cinque entity page;
- mappa fonti;
- matrice di copertura.

Seguire l'ordinamento e lo stile esistenti senza rigenerare sezioni non pertinenti.

- [ ] **Step 4: Appendere un evento a `wiki/log.md`**

Appendere una sola riga:

```text
- 2026-07-28T00:00:00+02:00 | knowledge_ingest | VOL-07 Sanità amministrativa e professioni sanitarie | raw=wiki/raw/business/vol-07-sanita-amministrativa-professioni-sanitarie-2026-07-28.txt | source_note=wiki/sources/vol-07-dossier-fonti-materie-sanita-2026-07-28.md | modules=M-SA02,M-SA01,M-SA03,M-SA04 | source_inventory=74_plus_entries | coverage_matrix=47_plus_rows | status=source_ready_for_pipeline_A_B | review=fonti_ufficiali_bandi_giurisprudenza_da_acquisire_e_verificare
```

Non modificare eventi precedenti.

- [ ] **Step 5: Verificare collegamenti e append-only**

Run:

```powershell
rg -n "vol-07-dossier-fonti-materie|vol-07-sanita-amministrativa-professioni-sanitarie|03-mappa-fonti-specialistiche|02-matrice-copertura-didattica" wiki\books\moduli\m-sa01-sanita-amministrativa wiki\books\moduli\m-sa02-professioni-sanitarie wiki\books\moduli\m-sa03-dirigenza-medica-sanitaria wiki\books\moduli\m-sa04-tecnici-sanitari-prevenzione wiki\index.md
Get-Content -Tail 3 'wiki\log.md'
git diff --check
```

Expected: tutti i moduli collegati; nuovo evento in coda; nessuna riscrittura del log.

- [ ] **Step 6: Commit**

```powershell
git add -- wiki/books/moduli/m-sa01-sanita-amministrativa wiki/books/moduli/m-sa02-professioni-sanitarie wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione wiki/index.md wiki/log.md
git commit -m "docs(wiki): collega moduli e catalogo VOL-07"
```

---

### Task 6: Creare la scheda, testarla e avviare lo step 00

**Files:**
- Create: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md`
- Create: `tests/pipeline/vol-07-spec.test.ts`
- Generated by CLI: `pipeline/VOL-07/run-state.json`
- Generated and ignored: `artifacts/pipeline/VOL-07/00/vol-07/prompt.md`

**Interfaces:**
- Consumes: quattro module id esistenti e planning A/B completo.
- Produces: spec validata, run-state versionato e prompt canonico dello step 00.

- [ ] **Step 1: Scrivere il test che richiede la scheda VOL-07**

Create `tests/pipeline/vol-07-spec.test.ts`:

```ts
import path from "node:path"
import { describe, expect, it } from "vitest"
import { loadVolumeSpec } from "../../src/pipeline/spec/load-volume-spec"

describe("VOL-07 pipeline spec", () => {
  it("starts phases A and B with the approved module priority", async () => {
    const loaded = await loadVolumeSpec({
      wikiRoot: path.resolve(process.cwd(), "wiki"),
      volumeCode: "VOL-07"
    })

    expect(loaded.issues).toEqual([])
    expect(loaded.spec).toMatchObject({
      volumeCode: "VOL-07",
      volumeTitle: "Sanità amministrativa e professioni sanitarie",
      cutOffDate: "2026-07-28",
      responsabileNormativo: "Alberto Brando",
      responsabileEditoriale: "Alberto Brando",
      writerProvider: "codex",
      phases: ["A", "B"]
    })
    expect(loaded.spec.modules.map((module) => [module.code, module.priority])).toEqual([
      ["M-SA02", 1],
      ["M-SA01", 2],
      ["M-SA03", 3],
      ["M-SA04", 4]
    ])
  })
})
```

- [ ] **Step 2: Eseguire il test e verificare che fallisca**

Run:

```powershell
npx vitest run tests/pipeline/vol-07-spec.test.ts
```

Expected: FAIL con `Nessuna scheda di pipeline per VOL-07`.

- [ ] **Step 3: Creare la scheda minima valida**

Create `planning/00-scheda-pipeline.md`:

```markdown
---
type: pipeline_spec
volume_code: VOL-07
volume_title: Sanità amministrativa e professioni sanitarie
cut_off_date: 2026-07-28
responsabile_normativo: Alberto Brando
responsabile_editoriale: Alberto Brando
writer_provider: codex
phases: [A, B]
status: active
updated_at: 2026-07-28
review_required: true
---

# Scheda di pipeline — VOL-07

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | ---: | --- |
| M-SA02 | moduli/m-sa02-professioni-sanitarie | 1 | A,B |
| M-SA01 | moduli/m-sa01-sanita-amministrativa | 2 | A,B |
| M-SA03 | moduli/m-sa03-dirigenza-medica-sanitaria | 3 | A,B |
| M-SA04 | moduli/m-sa04-tecnici-sanitari-prevenzione | 4 | A,B |

## Stato di partenza

- Dossier source-ready: [[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/01-dossier-source-ready]]
- Matrice globale: [[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/02-matrice-copertura-didattica]]
- Mappa fonti: [[books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/03-mappa-fonti-specialistiche]]
- Ordine: M-SA02, M-SA01, M-SA03, M-SA04.
- Le fasi C, D e F saranno aggiunte solo dopo indice definitivo, capitoli e matrici per modulo.
```

- [ ] **Step 4: Eseguire test, typecheck e doctor**

Run:

```powershell
npx vitest run tests/pipeline/vol-07-spec.test.ts tests/pipeline
npm run typecheck
npm run pipeline -- doctor
```

Expected: tutti passati e doctor verde.

- [ ] **Step 5: Inizializzare il run-state con output JSON**

Run:

```powershell
npm run pipeline -- init VOL-07 --json
npm run pipeline -- status VOL-07 --json
```

Expected:

- `ok: true`;
- fasi `A`, `B`;
- `pipeline/VOL-07/run-state.json` creato dal CLI;
- prossimo step `00`.

- [ ] **Step 6: Prendere in carico lo step 00**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
```

Expected:

- step `00` in stato `in-progress`;
- prompt creato in `artifacts/pipeline/VOL-07/00/vol-07/prompt.md`;
- owner e agent registrati;
- nessuno step successivo chiuso o accettato.

- [ ] **Step 7: Verificare prompt e run-state senza modificarli**

Run:

```powershell
Get-Content -Raw 'artifacts\pipeline\VOL-07\00\vol-07\prompt.md'
npm run pipeline -- status VOL-07 --json
git diff --check
```

Expected: contratto di esecuzione sopra `---`, prompt canonico sotto `---`, step 00 in carico.

- [ ] **Step 8: Commit**

```powershell
git add -- wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/00-scheda-pipeline.md tests/pipeline/vol-07-spec.test.ts pipeline/VOL-07/run-state.json
git commit -m "feat(pipeline): inizializza VOL-07 fasi A e B"
```

Non aggiungere `artifacts/pipeline/`, che è ignorato.

---

### Task 7: Registrare memoria e verificare la consegna

**Files:**
- Modify through service: `wiki/memory/agent/l0/`
- Modify through service: `wiki/memory/agent/l1/atoms.jsonl`
- Modify through service when atoms are extracted: `wiki/memory/agent/l2/scenarios.md`
- Modify through service when stable instructions change: `wiki/memory/agent/l3/persona.md`

**Interfaces:**
- Consumes: esito reale delle Task 1–6.
- Produces: traccia condivisa per i futuri agenti e report finale verificato.

- [ ] **Step 1: Catturare la conversazione con `LocalAgentMemory`**

Usare `LocalAgentMemory.fromConfig().captureConversation()` con:

```ts
{
  scope: "VOL-07",
  route: "codex-vol-07-source-ingest-pipeline-start",
  messages: [
    {
      role: "user",
      content: "Importare il dossier VOL-07, registrare tutte le fonti e le materie richieste e avviare la pipeline."
    }
  ],
  reply: "Dossier acquisito, inventario e matrice creati, moduli collegati, pipeline A/B inizializzata e step 00 preso in carico.",
  metadata: {
    volume: "VOL-07",
    modules: "M-SA02,M-SA01,M-SA03,M-SA04",
    cutOffDate: "2026-07-28",
    pipelineStep: "00"
  }
}
```

Non scrivere direttamente nei file di memoria.

- [ ] **Step 2: Verificare memoria e stato Git**

Run:

```powershell
npx vitest run tests/local-agent-memory.test.ts
git status --short
git diff --check
```

Expected: test memoria passati; soltanto file di memoria attesi e `.claude/settings.local.json` non tracciato.

- [ ] **Step 3: Commit della traccia di memoria**

Run:

```powershell
git add -- wiki/memory/agent
git commit -m "docs(memory): registra avvio pipeline VOL-07"
```

- [ ] **Step 4: Verifica finale completa**

Run:

```powershell
npx vitest run tests/pipeline tests/local-agent-memory.test.ts
npm run typecheck
npm run pipeline -- doctor
npm run pipeline -- status VOL-07 --json
git diff --check
git status -sb
```

Expected:

- test e typecheck passati;
- doctor verde;
- VOL-07 con step 00 `in-progress`;
- branch avanti soltanto dei commit intenzionali;
- `.claude/settings.local.json` preservato;
- nessuna modifica editoriale non committata.

