# VOL-07 M-SA02 — piano di chiusura coordinata dei blocker

**Obiettivo:** completare in un solo lotto tutte le attività documentali e organizzative ancora eseguibili internamente per lo step 07, aggiornare la matrice in base alle evidenze effettive e consegnare un unico pacchetto tracciabile per le convalide indipendenti residue.

**Vincoli:** non modificare manualmente `pipeline/VOL-07/run-state.json`; non autocertificare review cliniche o professionali; non promuovere a `completo` una riga che dipende da protocollo locale, prova pratica o firma esterna; non alterare i file raw già acquisiti.

## Task 1 — Baseline e inventario

**File da leggere:**
- `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- tutti i `wiki/raw/m-sa02-professioni-sanitarie/*/download-log.json`

**Azioni:**
1. Confermare worktree, branch e stato sporco senza ripulire modifiche preesistenti.
2. Eseguire `npm test` e registrare il numero di test superati.
3. Distinguere per ciascuna delle otto righe i gap documentali interni dai gate di review/prova esterni.

## Task 2 — Acquisizione controllata dei corpus mancanti

**File raw e log da aggiornare:**
- `wiki/raw/m-sa02-professioni-sanitarie/tecnica-ostetrica/`
- `wiki/raw/m-sa02-professioni-sanitarie/tecnica-fisioterapia/`
- `wiki/raw/m-sa02-professioni-sanitarie/tecnica-assistenziale/`
- `wiki/raw/m-sa02-professioni-sanitarie/tecnica-tpall/`

**Azioni:**
1. Ostetricia: acquisire RCOG Green-top 42 pubblicata, RCOG Green-top 50 e la pagina ufficiale di stato della terza edizione; usare l'eventuale bozza di consultazione soltanto se ancora pubblicamente disponibile e sempre come fonte non prescrittiva.
2. Fisioterapia: acquisire i moduli WHO PIR 3 neurologico e 4 cardiopolmonare del 2023.
3. Metodo e continuità: acquisire il Manuale metodologico ISS SNLG 2.0 (dicembre 2024) e il Manuale operativo AGENAS sulla presa in carico della cronicità; collocarli nel sotto-corpus assistenziale.
4. TPALL: acquisire il rapporto ISPRA sui controlli AIA statali 2023 e la nota tecnica ISPRA per l'analisi di rischio dei siti contaminati; non duplicare le fonti SNPA già presenti su rifiuti, aria, acque e terre/rocce.
5. Per ogni file calcolare byte e SHA-256, verificare firma PDF, numero pagine ed estraibilità del testo, quindi aggiungere una voce immutabile al relativo `download-log.json`.

## Task 3 — Source notes e stato di vigenza

**File da aggiornare o creare:**
- `wiki/sources/emergenze-ostetriche-distocia-spalla-prolasso-funicolo-protocolli-italiani.md`
- `wiki/sources/riabilitazione-fisioterapia-iss-ministero.md`
- `wiki/sources/metodo-evidenze-sistema-nazionale-linee-guida-iss.md`
- `wiki/sources/tpall-aia-campionamenti-acque-aria-suolo-rifiuti-alimenti.md`
- `wiki/sources/codici-deontologici-infermiere-ostetrica-fisioterapista-tpall.md`
- `wiki/sources/presa-in-carico-cronicita-pdta-territorio-agenas.md`

**Azioni:**
1. Separare sempre fonte definitiva, documento datato ma ancora pubblicato, bozza di consultazione e protocollo locale.
2. Registrare che RCOG 42 del 2012 è ancora la versione pubblicata mentre la terza edizione risulta in sviluppo; registrare la revisione/estensione dichiarata per RCOG 50.
3. Documentare per FNOFI la provenienza AIFI del testo ospitato dalla Federazione e per FNOPO la versione ufficiale acquisita, senza attribuire date non provate.
4. Esplicitare che i manuali nazionali/internazionali non sostituiscono procedure aziendali, istruzioni del dispositivo o validazione professionale.

## Task 4 — Matrice, audit e pacchetto unico di review

**File da aggiornare o creare:**
- `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/02-matrice-copertura-didattica.md`
- `wiki/reviews/pipeline/VOL-07/07-audit-corpus-tecnici-m-sa02.md`
- `wiki/books/moduli/m-sa02-professioni-sanitarie/planning/07-piano-chiusura-review-esterne-m-sa02.md`

**Azioni:**
1. Rimuovere dalla lista blocker i documenti già acquisiti: raccomandazioni ministeriali sul rischio clinico, triage e codici deontologici.
2. Aggiornare i conteggi e mantenere `parziale` ogni riga che attende firma, protocollo locale, prova su dispositivo o simulazione.
3. Preparare un unico piano di review con cinque verbali separati: OSS/infermieristica, ostetricia, fisioterapia, epidemiologia e TPALL.
4. In ogni verbale includere ruolo minimo del revisore, corpus da verificare, checklist, esito ammesso, data, firma e criteri di riapertura; lasciare vuoti i campi che richiedono una persona reale.
5. Collegare la validazione dei casi e delle rubriche alle cinque review, evitando una firma editoriale sostitutiva.

## Task 5 — Integrità, gate e memoria

**File da aggiornare:**
- `wiki/log.md`
- memoria locale nello scope `pipeline-volume-vol-07-m-sa02`

**Azioni:**
1. Eseguire un audit automatico di tutti i log: esistenza file, byte e SHA-256; verificare i nuovi PDF con PyPDF.
2. Eseguire `npm test`, `npm run typecheck`, `git diff --check` e `npm run pipeline -- status VOL-07 --json`.
3. Eseguire `npm run pipeline -- complete VOL-07 --step 07 --module M-SA02 --json` senza `--accept`; registrare l'esito reale del gate.
4. Se restano soltanto convalide esterne, non forzare il passaggio: aggiornare audit, log e memoria con il pacchetto pronto e l'elenco esatto delle firme/prove mancanti.

## Criteri di completamento

- Tutti i gap documentali interni individuati nel lotto sono acquisiti, verificati e citati.
- La matrice non contiene blocker documentali già risolti né righe sovrastimate.
- Ogni blocker residuo indica una singola azione esterna verificabile e il relativo verbale.
- Corpus integro, test e typecheck verdi, gate rieseguito senza autocertificazione.
