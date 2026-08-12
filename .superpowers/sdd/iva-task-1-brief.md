# Task 1 brief — M-FC02 IVA e adempimenti

Plan: `docs/superpowers/plans/2026-07-20-m-fc02-iva-adempimenti.md`

## Global constraints

## Global Constraints

- Seguire `wiki/AGENTS.md` e usare `LocalAgentMemory`; se il runner non Ã¨ disponibile, documentare l'errore senza creare memorie parallele.
- Applicare `concorso-book-professional-writer` e l'Integral Didactic Coverage Gate.
- Il testo editoriale deriva soltanto da `wiki/sources/`, `wiki/topics/`, `wiki/entities/` e conoscenza consolidata; non scrivere dai raw.
- Preservare tutte le modifiche preesistenti del worktree e usare `apply_patch` per le modifiche; se il wrapper Windows lo impedisce, registrare il fallimento prima di un fallback chirurgico sul solo file autorizzato.
- Usare struttura normativa stabile; aliquote, soglie, termini, modelli, codici e regole telematiche soltanto se ufficialmente verificati, datati e didatticamente necessari.
- Non presentare l'IVA come neutrale in modo assoluto; non confondere non imponibilitÃ , esenzione ed esclusione; non descrivere detrazione o compensazione come incondizionate.
- Non duplicare nei capitoli 4 e 6 la disciplina responsabile dei capitoli 5, 5A, 5B e 7.
- Ogni task richiede implementazione, SPEC COMPLIANCE review, QUALITY review, fix loop e commit isolato.
- Governance attesa dopo approvazione: 80 nuclei, 66 `completo`, 14 `parziale`, 0 `solo-nominato`, 0 `rinviato`, 0 `mancante`, 14 blocker; giudizio globale ancora `Non pubblicabile allo stato attuale`.

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

- [ ] **Step 2: Verificare versioni ufficiali e acquisire solo ciÃ² che manca**

Consultare fonti ufficiali Normattiva ed EUR-Lex. Per ogni atto separare: data di consultazione, data/identificativo della versione, ultimo aggiornamento dichiarato e decorrenze future. Se il file locale non consente questa riconciliazione, acquisire un export ufficiale integrale con nome che includa la data di riferimento; non sovrascrivere silenziosamente un raw con hash giÃ  tracciato.

Atteso: provenienza e versione verificabili per D.P.R. 633/1972, D.P.R. 322/1998, D.Lgs. 241/1997 e direttiva 2006/112/CE.

- [ ] **Step 3: Scrivere la source note IVA**

La nota deve consolidare almeno:

```text
funzione e armonizzazione UE
presupposti soggettivo, oggettivo e territoriale
cessioni e prestazioni
imponibili / non imponibili / esenti / escluse
effettuazione ed esigibilitÃ 
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

