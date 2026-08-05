# VOL-07 Step 18 Image Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Chiudere lo step 17 approvato e completare i quattro audit immagini dello step 18 di VOL-07 senza creare asset decorativi quando l'inventario è vuoto.

**Architecture:** La pipeline CLI resta proprietaria di ordine e stato. Ogni modulo riceve un report Markdown autonomo che registra inventario, controllo dei riferimenti e verifica nel contesto del Book Studio; poiché l'inventario iniziale rileva zero directory asset e zero riferimenti immagine nei 25 capitoli, l'esito atteso è “nessun asset da ottimizzare”, non la creazione di nuove immagini. La filosofia `Precisione Vitale` resta il contratto visuale per eventuali asset futuri e per l'impaginazione dello step 19.

**Tech Stack:** Markdown, PowerShell, CLI TypeScript della pipeline tramite `npm run pipeline`, Book Studio asset API in sola lettura, Git, LocalAgentMemory.

## Global Constraints

- Filosofia vincolante: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/05-filosofia-visiva-precisione-vitale.md`.
- Non creare immagini nello step 17 e non aggiungere grafica decorativa nello step 18.
- Gli output ammessi dal workflow visuale sono `.md`, `.png` e `.pdf`; questo piano produce soltanto report `.md` perché l'inventario VOL-07 è vuoto.
- Formato di riferimento: KDP verticale 6,69 × 9,61 pollici, bianco e nero, margini sicuri e leggibilità paperback.
- Non modificare manualmente `pipeline/VOL-07/run-state.json`; usare soltanto `status`, `next` e `complete` con `--json`.
- Usare `--accept --note` solo dopo una risposta esplicita `gate-not-implemented` e dopo avere eseguito la verifica manuale documentata.
- Non modificare capitoli congelati, teoria, fonti, casi, quiz o perimetro durante l'audit immagini.
- Ogni report step 18 usa la tabella esatta `Asset | Problema | Correzione | Verifica nel Book Studio | Esito`.
- Non creare directory `assets/` vuote: l'assenza di asset è un esito valido e deve essere dichiarata.

---

### Task 1: Chiudere la filosofia visiva approvata dello step 17

**Files:**
- Verify: `wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/05-filosofia-visiva-precisione-vitale.md`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: filosofia `Precisione Vitale` approvata e commit `6ed18d6`.
- Produces: step `17:VOL-07` in stato `done`; next ufficiale `18:moduli/m-sa02-professioni-sanitarie`.

- [ ] **Step 1: Verificare il contratto della filosofia**

Run:

```powershell
$path = 'wiki/books/volumi/vol-07-sanita-amministrativa-professioni-sanitarie/planning/05-filosofia-visiva-precisione-vitale.md'
$raw = Get-Content -Raw $path
$body = [regex]::Replace($raw, '(?s)^---\s*.*?\s*---\s*', '')
$paragraphs = @($body -split "(?:`r?`n){2,}" | Where-Object { $_.Trim() -and -not $_.Trim().StartsWith('#') })
[pscustomobject]@{
  Paragraphs = $paragraphs.Count
  Movement = ($body -match '(?m)^# Precisione Vitale$')
  Placeholders = ([regex]::Matches($raw, '(?i)\bTBD\b|\bTODO\b|<placeholder>')).Count
} | Format-List
```

Expected: `Paragraphs: 6`, `Movement: True`, `Placeholders: 0`.

- [ ] **Step 2: Tentare la chiusura canonica senza forzature**

Run:

```powershell
npm run pipeline -- complete VOL-07 --step 17 --json
```

Expected: chiusura verde oppure risposta strutturata `gate-not-implemented`. Non dedurre l'esito dal testo formattato.

- [ ] **Step 3: Accettare manualmente solo se richiesto dal CLI**

Run soltanto dopo `gate-not-implemented`:

```powershell
npm run pipeline -- complete VOL-07 --step 17 --accept --note "Filosofia Precisione Vitale approvata: 6 paragrafi, palette e gerarchia definite, testo minimo, standard professionale e compatibilità KDP 6,69 x 9,61 verificati; nessun asset creato." --json
```

Expected: `ok: true`, `passed: true`, nessun blocker; gli eventuali warning devono essere `accepted:gate-not-implemented` e `manual-acceptance`.

- [ ] **Step 4: Confermare il prossimo target**

Run:

```powershell
npm run pipeline -- status VOL-07 --json
```

Expected: next `18:moduli/m-sa02-professioni-sanitarie`, nessuno step bloccato.

### Task 2: Audit immagini M-SA02 Professioni sanitarie

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa02-professioni-sanitarie.md`
- Inspect: `wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/*.md`
- Inspect if present: `wiki/books/moduli/m-sa02-professioni-sanitarie/assets/`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: step 17 `done`, filosofia `Precisione Vitale`, nove capitoli M-SA02.
- Produces: report step 18 M-SA02 e stato `18:moduli/m-sa02-professioni-sanitarie` `done`.

- [ ] **Step 1: Prendere in carico e leggere il prompt esatto**

Run:

```powershell
npm run pipeline -- next VOL-07 --json
Get-Content -Raw 'artifacts/pipeline/VOL-07/18/moduli-m-sa02-professioni-sanitarie/prompt.md'
```

Expected: target M-SA02, prompt di audit immagini, nessun target concorrente.

- [ ] **Step 2: Inventariare asset e riferimenti reali**

Run:

```powershell
$root = 'wiki/books/moduli/m-sa02-professioni-sanitarie'
$refs = 0
foreach ($file in Get-ChildItem "$root/chapters" -Filter '*.md') {
  $raw = Get-Content -Raw $file.FullName
  $refs += [regex]::Matches($raw, '!\[\[').Count
  $refs += [regex]::Matches($raw, '!\[[^\]]*\]\(').Count
}
[pscustomobject]@{ AssetDirectory = (Test-Path "$root/assets"); ImageReferences = $refs } | Format-List
```

Expected: `AssetDirectory: False`, `ImageReferences: 0`.

- [ ] **Step 3: Creare il report di audit**

Create the report with frontmatter `type: review`, `status: complete`, `review_required: false`, `issue_type: image_audit`, `severity: none`, followed by:

```markdown
# Audit immagini — M-SA02 Professioni sanitarie

## Esito

L'inventario dei nove capitoli non rileva directory asset, wikilink immagine o immagini Markdown. Non esistono quindi asset da correggere o ottimizzare; non viene aggiunta grafica decorativa.

| Asset | Problema | Correzione | Verifica nel Book Studio | Esito |
| --- | --- | --- | --- | --- |
| Nessun asset | Nessuna immagine o path da revisionare | Non applicabile; inventario conservato senza creare asset | Zero riferimenti immagine e zero directory asset; nessun overflow, ritaglio o collisione attribuibile a immagini | conforme |

## Regola per asset futuri

Ogni asset futuro deve seguire `Precisione Vitale`, dichiarare funzione didattica e superare contrasto, margini, risoluzione, didascalia e Book Studio preview prima dell'inserimento.
```

- [ ] **Step 4: Verificare il report**

Run:

```powershell
$report = Get-Content -Raw 'wiki/reviews/pipeline/VOL-07/18-moduli-m-sa02-professioni-sanitarie.md'
[pscustomobject]@{
  ExactHeader = ([regex]::Matches($report, '(?m)^\| Asset \| Problema \| Correzione \| Verifica nel Book Studio \| Esito \|$')).Count
  ConformRows = ([regex]::Matches($report, '(?m)^\| Nessun asset .*\| conforme \|$')).Count
  Placeholders = ([regex]::Matches($report, '(?i)\bTBD\b|\bTODO\b')).Count
} | Format-List
git diff --check -- 'wiki/reviews/pipeline/VOL-07/18-moduli-m-sa02-professioni-sanitarie.md'
```

Expected: `ExactHeader: 1`, `ConformRows: 1`, `Placeholders: 0`, diff check exit 0.

- [ ] **Step 5: Chiudere lo step con la stessa disciplina del Task 1**

Run plain `complete` first. If and only if the JSON reports `gate-not-implemented`, run:

```powershell
npm run pipeline -- complete VOL-07 --step 18 --module M-SA02 --accept --note "Audit immagini M-SA02 completato: 9 capitoli, 0 directory asset, 0 riferimenti immagine, report conforme e nessuna grafica decorativa aggiunta." --json
```

Expected: step M-SA02 `done`, next M-SA01.

- [ ] **Step 6: Commit selettivo del report**

```powershell
git add -- 'wiki/reviews/pipeline/VOL-07/18-moduli-m-sa02-professioni-sanitarie.md'
git diff --cached --check
git commit -m "docs(vol-07): audit M-SA02 image inventory"
```

Expected: commit contenente soltanto il report M-SA02. Non aggiungere il run-state se il suo diff include modifiche precedenti non isolate.

### Task 3: Audit immagini M-SA01 Sanità amministrativa

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa01-sanita-amministrativa.md`
- Inspect: `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/*.md`
- Inspect if present: `wiki/books/moduli/m-sa01-sanita-amministrativa/assets/`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: report M-SA02 chiuso, cinque capitoli M-SA01.
- Produces: report step 18 M-SA01 e stato M-SA01 `done`.

- [ ] **Step 1: Prendere in carico e leggere il prompt**

Run `npm run pipeline -- next VOL-07 --json`, then read:

```powershell
Get-Content -Raw 'artifacts/pipeline/VOL-07/18/moduli-m-sa01-sanita-amministrativa/prompt.md'
```

Expected: target M-SA01.

- [ ] **Step 2: Ripetere l'inventario sul root M-SA01**

Use the PowerShell inventory from Task 2 with:

```powershell
$root = 'wiki/books/moduli/m-sa01-sanita-amministrativa'
```

Expected: `AssetDirectory: False`, `ImageReferences: 0`.

- [ ] **Step 3: Creare e verificare il report M-SA01**

Use the exact report structure from Task 2, changing title, module code, chapter count to cinque and output path to `18-moduli-m-sa01-sanita-amministrativa.md`. The table row remains `Nessun asset ... conforme` because it represents the measured inventory, not a copied assumption.

Run the same regex checks from Task 2 against the M-SA01 report.

- [ ] **Step 4: Chiudere e committare selettivamente**

Run plain `complete` first; after explicit `gate-not-implemented` only:

```powershell
npm run pipeline -- complete VOL-07 --step 18 --module M-SA01 --accept --note "Audit immagini M-SA01 completato: 5 capitoli, 0 directory asset, 0 riferimenti immagine, report conforme e nessuna grafica decorativa aggiunta." --json
git add -- 'wiki/reviews/pipeline/VOL-07/18-moduli-m-sa01-sanita-amministrativa.md'
git diff --cached --check
git commit -m "docs(vol-07): audit M-SA01 image inventory"
```

Expected: step M-SA01 `done`, commit limitato al report, next M-SA03.

### Task 4: Audit immagini M-SA03 Dirigenza medica e sanitaria

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa03-dirigenza-medica-sanitaria.md`
- Inspect: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/*.md`
- Inspect if present: `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria/assets/`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: report M-SA01 chiuso, sette capitoli M-SA03.
- Produces: report step 18 M-SA03 e stato M-SA03 `done`.

- [ ] **Step 1: Prendere in carico e leggere il prompt**

Run `npm run pipeline -- next VOL-07 --json`, then read:

```powershell
Get-Content -Raw 'artifacts/pipeline/VOL-07/18/moduli-m-sa03-dirigenza-medica-sanitaria/prompt.md'
```

Expected: target M-SA03.

- [ ] **Step 2: Inventariare, produrre e verificare il report**

Use the inventory and report checks from Task 2 with root `wiki/books/moduli/m-sa03-dirigenza-medica-sanitaria`, report path `18-moduli-m-sa03-dirigenza-medica-sanitaria.md` and chapter count sette.

Expected: zero asset, zero riferimenti, header esatto, una riga `conforme`, zero placeholder.

- [ ] **Step 3: Chiudere e committare selettivamente**

After the mandatory plain `complete` attempt and only on `gate-not-implemented`:

```powershell
npm run pipeline -- complete VOL-07 --step 18 --module M-SA03 --accept --note "Audit immagini M-SA03 completato: 7 capitoli, 0 directory asset, 0 riferimenti immagine, report conforme e nessuna grafica decorativa aggiunta." --json
git add -- 'wiki/reviews/pipeline/VOL-07/18-moduli-m-sa03-dirigenza-medica-sanitaria.md'
git diff --cached --check
git commit -m "docs(vol-07): audit M-SA03 image inventory"
```

Expected: step M-SA03 `done`, next M-SA04.

### Task 5: Audit immagini M-SA04 Tecnici sanitari e prevenzione

**Files:**
- Create: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa04-tecnici-sanitari-prevenzione.md`
- Inspect: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/chapters/*.md`
- Inspect if present: `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/assets/`
- Modify through CLI only: `pipeline/VOL-07/run-state.json`

**Interfaces:**
- Consumes: report M-SA03 chiuso, quattro capitoli M-SA04.
- Produces: report step 18 M-SA04, tutti gli audit immagini completati, next `19:VOL-07`.

- [ ] **Step 1: Prendere in carico e leggere il prompt**

Run `npm run pipeline -- next VOL-07 --json`, then read:

```powershell
Get-Content -Raw 'artifacts/pipeline/VOL-07/18/moduli-m-sa04-tecnici-sanitari-prevenzione/prompt.md'
```

Expected: target M-SA04.

- [ ] **Step 2: Inventariare, produrre e verificare il report**

Use the inventory and report checks from Task 2 with root `wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione`, report path `18-moduli-m-sa04-tecnici-sanitari-prevenzione.md` and chapter count quattro.

Expected: zero asset, zero riferimenti, header esatto, una riga `conforme`, zero placeholder.

- [ ] **Step 3: Chiudere e committare selettivamente**

After the mandatory plain `complete` attempt and only on `gate-not-implemented`:

```powershell
npm run pipeline -- complete VOL-07 --step 18 --module M-SA04 --accept --note "Audit immagini M-SA04 completato: 4 capitoli, 0 directory asset, 0 riferimenti immagine, report conforme e nessuna grafica decorativa aggiunta." --json
git add -- 'wiki/reviews/pipeline/VOL-07/18-moduli-m-sa04-tecnici-sanitari-prevenzione.md'
git diff --cached --check
git commit -m "docs(vol-07): audit M-SA04 image inventory"
```

Expected: step M-SA04 `done`, next `19:VOL-07`.

### Task 6: Verifica integrata e handoff allo step 19

**Files:**
- Verify: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa02-professioni-sanitarie.md`
- Verify: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa01-sanita-amministrativa.md`
- Verify: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa03-dirigenza-medica-sanitaria.md`
- Verify: `wiki/reviews/pipeline/VOL-07/18-moduli-m-sa04-tecnici-sanitari-prevenzione.md`
- Verify: `pipeline/VOL-07/run-state.json`
- Modify through service only: `wiki/memory/agent/`

**Interfaces:**
- Consumes: quattro report step 18 e cinque step fase E chiusi, incluso step 17.
- Produces: prova finale, memoria locale aggiornata, handoff a `19:VOL-07`.

- [ ] **Step 1: Verificare con una singola scansione i quattro report**

Run:

```powershell
$reports = @(Get-ChildItem 'wiki/reviews/pipeline/VOL-07' -Filter '18-moduli-m-sa*.md')
$raw = ($reports | ForEach-Object { Get-Content -Raw $_.FullName }) -join "`n"
[pscustomobject]@{
  Reports = $reports.Count
  ExactHeaders = ([regex]::Matches($raw, '(?m)^\| Asset \| Problema \| Correzione \| Verifica nel Book Studio \| Esito \|$')).Count
  ConformRows = ([regex]::Matches($raw, '(?m)^\| Nessun asset .*\| conforme \|$')).Count
  Placeholders = ([regex]::Matches($raw, '(?i)\bTBD\b|\bTODO\b')).Count
} | Format-List
```

Expected: `Reports: 4`, `ExactHeaders: 4`, `ConformRows: 4`, `Placeholders: 0`.

- [ ] **Step 2: Confermare che nessun asset sia stato introdotto**

Run:

```powershell
$modules = @('m-sa02-professioni-sanitarie','m-sa01-sanita-amministrativa','m-sa03-dirigenza-medica-sanitaria','m-sa04-tecnici-sanitari-prevenzione')
foreach ($slug in $modules) {
  $root = "wiki/books/moduli/$slug"
  $refs = 0
  foreach ($file in Get-ChildItem "$root/chapters" -Filter '*.md') {
    $text = Get-Content -Raw $file.FullName
    $refs += [regex]::Matches($text, '!\[\[').Count
    $refs += [regex]::Matches($text, '!\[[^\]]*\]\(').Count
  }
  [pscustomobject]@{ Module = $slug; AssetDirectory = (Test-Path "$root/assets"); ImageReferences = $refs }
}
```

Expected: quattro righe, tutte `AssetDirectory: False`, `ImageReferences: 0`.

- [ ] **Step 3: Eseguire test e controllo diff**

Run:

```powershell
npm test -- --run tests/pipeline tests/local-agent-memory.test.ts
git diff --check
```

Expected: tutti i test mirati verdi, diff check exit 0.

- [ ] **Step 4: Verificare lo stato finale della pipeline**

Run:

```powershell
npm run pipeline -- status VOL-07 --json
```

Expected: `done: 163`, `pending: 6`, nessun blocked o in-progress, next `19:VOL-07`.

- [ ] **Step 5: Registrare la traccia tramite LocalAgentMemory**

Use `LocalAgentMemory.fromConfig().captureConversation()` with scope `VOL-07`, route `pipeline-vol-07-step-17-18-visual-audit`, result summary containing: filosofia commit, four reports, zero assets, test count and next step 19. Do not edit JSONL files manually.

- [ ] **Step 6: Commit finale solo se il run-state è isolabile**

Run:

```powershell
git diff -- 'pipeline/VOL-07/run-state.json'
```

If the diff contains only the expected step 17 and four step 18 transitions, stage it with the four reports not already committed and commit:

```powershell
git add -- 'pipeline/VOL-07/run-state.json'
git diff --cached --check
git commit -m "chore(vol-07): complete visual audit phase"
```

If the diff contains pre-existing unrelated state changes, do not stage it; report the exact condition in the handoff while preserving the shared worktree.
