# IVA Task 2 report — architettura IVA nel capitolo 4

## Esito

**DONE_WITH_CONCERNS**

- SPEC COMPLIANCE: PASS
- QUALITY: PASS
- Concern non bloccante per questo task: l'anchor di destinazione `#Operazioni IVA e ciclo degli adempimenti` non esiste ancora nel capitolo 6 corrente; e' l'interfaccia prevista dal Task 3 del piano e il link e' gia' predisposto.

## Baseline

File: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md`

- SHA-256 iniziale del file su disco: `3565DB22EF3FF2A928AB4288D00EE4F99059F40CDFEC9923E054280D4CDE2555`.
- SHA-256 della rappresentazione baseline `HEAD` normalizzata LF: `3ACBE96292F165CD82D2EF1A72266DF48FE97587EECF663E42063A27B8CAAA5F`.
- Diff iniziale del capitolo: assente.
- Stato iniziale: il capitolo non risultava modificato; il worktree conteneva modifiche estranee, lasciate intatte.
- Promesse IVA iniziali: operazione, soggetto passivo, rivalsa, detrazione, liquidazione, dichiarazione, fatturazione, registrazione e controllo erano nominati; risultava spiegata soltanto una sequenza operativa generica. Armonizzazione/consumo, neutralita' condizionata, tre presupposti, ruoli distinti e quattro classi non erano sviluppati nel blocco responsabile.

## Fonti consolidate consumate

Esclusivamente:

- `[[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]`;
- `[[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]`;
- `[[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]]`.

Nessun raw e nessuna ricerca web sono stati usati per la scrittura.

## Mappa requisiti → sezioni

| Requisito | Sezione implementata |
|---|---|
| IVA armonizzata sui consumi | apertura di `## IVA: operazioni, soggetti, detrazione e adempimenti` |
| neutralita' come meccanismo e limiti | `### Neutralita' come meccanismo, non come risultato assoluto` |
| tre presupposti | `### I tre presupposti: oggettivo, soggettivo e territoriale` |
| soggetto passivo/debitore/consumatore | `### Soggetto passivo, debitore e consumatore finale` |
| rivalsa → detrazione → liquidazione | schema nel blocco neutralita' |
| quattro classi e conseguenze | `### Le quattro classi di operazioni` |
| rinvio preciso al capitolo 6 | `### Dalla teoria agli adempimenti: rinvio responsabile` |
| definizione, funzione, distinzione, conseguenza, esempio, errore, verifica | integrate in ciascun nucleo, con verifica finale cumulativa |
| tracciabilita' e data | `source_refs`, `last_compiled_from`, riferimenti, note review; `updated_at` 2026-07-21 |

`status: revised_draft` e `confidence: 0.95` non sono stati aumentati.

## Controlli

- Presenza nuclei richiesti: PASS.
- Assenza di aliquote, soglie, termini, modelli, codici o regole telematiche mobili introdotti nel blocco: PASS.
- Distinzione non imponibile/esente/esclusa: PASS.
- Detrazione e neutralita' non descritte come incondizionate: PASS.
- Casistica applicativa del capitolo 6 non duplicata: PASS; presente soltanto la mappa funzionale.
- Routing verso capitoli 5, 5A, 5B e 7 preservato: PASS.
- UTF-8 senza BOM e nessun carattere sostitutivo rilevato: PASS.
- `git diff --check -- <capitolo>`: PASS, nessun output sostanziale (solo warning CRLF/LF del client Git).
- Blocco IRPEF/IRES: PASS; SHA-256 del segmento baseline e finale identico: `7BEEB06F7A9ECBAC8E5B55C88904FCC73BACA6D0375BDA4D62DADD01AE001780`.
- Metriche pre-fix review (superate): `56` inserimenti, `9` eliminazioni; SHA-256 `B8BA23F23765F7EFD973828D327BE10799B2305FCBAEF3F231945088B8E8B56F`.
- Diffstat finale post-fix effettivo del capitolo: `60` inserimenti, `9` eliminazioni.
- SHA-256 finale post-fix effettivo su disco: `43E74481C88420AD92BABA7BC8CFEDD8C0F0458C8388F0BB35AF63172F708C75`.

## Review separate

### SPEC COMPLIANCE: PASS

Tutti i nuclei richiesti dal brief sono spiegati nel blocco responsabile; frontmatter e riferimenti includono le due nuove source note e la source UE; nessuno status/confidence e' stato promosso; nessun file editoriale estraneo e' stato toccato.

### QUALITY: PASS

Progressione leggibile: funzione → meccanismo → presupposti → ruoli → classificazione → routing. Gli esempi sono classificatori, non sostituiscono la verifica della fattispecie; errori e verifiche sono specifici; non sono presenti automatismi su neutralita', detrazione o compensazione.

## Concern e note operative

1. L'anchor del capitolo 6 e' un forward contract del Task 3: al controllo odierno il relativo heading non e' ancora presente. Il Task 3 dovra' creare esattamente `## Operazioni IVA e ciclo degli adempimenti` o aggiornare contestualmente il link.
2. `LocalAgentMemory` e' stato individuato e il deposito canonico e' rimasto attivo, ma non era disponibile un runner TypeScript (`tsx`) installato per invocare il servizio senza modificare dipendenze. Il tentativo e il limite sono documentati; non e' stata creata memoria parallela.
3. `apply_patch` e' stato tentato due volte (percorso assoluto e relativo) e bloccato prima della lettura dal wrapper Windows: `cannot enforce split writable root sets`. In conformita' al brief e' stato usato un fallback chirurgico tramite `System.IO` sui soli due file autorizzati.
4. Nessun commit e' stato creato, come richiesto dal task delegato.
## Fix review — raccordo direttiva/norma nazionale

Finding Important risolto con un'integrazione circoscritta all'apertura del blocco IVA:

- mini-esempio sul percorso direttiva 2006/112/CE → D.P.R. 633/1972;
- errore-trappola sulla falsa equivalenza tra direttiva e regolamento e sull'omissione di primato/interpretazione conforme;
- verifica in tre passaggi: tipo/funzione della fonte UE, norma nazionale pertinente, compatibilita' unionale.

Test di presenza: PASS per le stringhe `Mini-esempio di raccordo`, `Errore-trappola`, `primato e interpretazione conforme` e `Verifica` nel blocco IVA.

`git diff --check -- wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md .superpowers/sdd/iva-task-2-report.md`

Output: vuoto; exit code `0` (PASS).

Controlli di non regressione: blocco IRPEF/IRES invariato; `status: revised_draft` e `confidence: 0.95` invariati; forward anchor del Task 3 mantenuto; nessun commit.
## Integration fix — anchor capitolo 6

Il solo link residuo `#IVA: la mappa essenziale` e' stato sostituito con `#Operazioni IVA e ciclo degli adempimenti`, allineandolo all'heading effettivo del capitolo 6 e al link gia' corretto nel blocco IVA.

Controlli:

- conteggio vecchio anchor nel capitolo 4: `0`;
- conteggio nuova destinazione nel capitolo 4: `2`;
- heading `## Operazioni IVA e ciclo degli adempimenti` nel capitolo 6: presente, `1` occorrenza;
- `git diff --check` su capitolo 4 e report: exit code `0`, output vuoto;
- nessun altro contenuto modificato; nessun commit.