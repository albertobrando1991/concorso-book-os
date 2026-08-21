---
id: review-pipeline-vol-04-step-23
type: editorial_review
volume: VOL-04
step: 23
status: passed
review_required: false
updated_at: 2026-08-21
---

# VOL-04 — Step 23: pacchetto candidato e consegna tecnica

## Esito

**PASS TECNICO.** È stato predisposto il candidato `VOL-04-candidate-2026.08.21.2`, con interno, copertina completa, metadati, istruzioni KDP, report di pubblicabilità, preflight, limiti, manutenzione e manifest delle impronte. Il pacchetto è pronto esclusivamente per lo step 24, riservato allo staff umano. Non è stato approvato, caricato o pubblicato su KDP.

## Identificazione e cutoff

| Campo | Valore |
| --- | --- |
| Volume | VOL-04 |
| Titolo | Giustizia e Ufficio per il processo |
| Versione candidata | `VOL-04-candidate-2026.08.21.2` |
| Cutoff normativo | 18 agosto 2026 |
| Commit di base | `1014415c4a681c8eea0663319c8fb68e3ac4e5a7` |
| Ramo | `agent/sync-volumi-04-05-06-09-20260817` |
| Allineamento remoto | HEAD locale e ramo remoto coincidenti al momento del packaging |
| Stato umano | Step 24 non eseguito |

## Contenuto della consegna

Percorso: `delivery/VOL-04/candidate/`

- `vol-04-interior-kdp.pdf`;
- `vol-04-cover-kdp.pdf`;
- `README.md`;
- `VERSION.json`;
- `METADATA-KDP.md`;
- `COVER-SPEC.md`;
- `KDP-UPLOAD-CHECKLIST.md`;
- `REPORT-PUBBLICABILITA.md`;
- `PREFLIGHT.md`;
- `CHANGELOG.md`;
- `LIMITS.md`;
- `MAINTENANCE.md`;
- `MANIFEST.sha256`.

## Controlli sui PDF

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Interno | PASS | 303 pagine fisiche; 6,69 × 9,61 pollici; rotazione 0; nessuna cifratura. |
| Pagine vuote | PASS | Nessuna pagina priva di testo nel controllo strutturale. |
| Font interno | PASS | Arial Bold, Garamond, Arial Black e Arial incorporati. |
| Copertina | PASS | Un'unica pagina; tavola 14,314608 × 9,86 pollici entro la tolleranza PDF. |
| Dorso | PASS | 0,684608 pollici, calcolato su 304 pagine KDP equivalenti e carta bianca. |
| Font copertina | PASS | Garamond, Garamond Bold, Arial e Arial Bold incorporati; nessun font base residuo. |
| Testi copertina | PASS | Titolo, sottotitolo, Metodo BANDO e indicazione VOL-04 presenti e coerenti. |
| Corpo minimo copertina | PASS | Testo visibile minimo rilevato: 9 pt. |
| Protezioni | PASS | Nessun PDF cifrato o protetto. |

Impronte principali:

- interno candidato: `151cf2370bb3a3d60b4e6b99a748f8ea25ff130d289b01ebe09df26c47342755`;
- copertina candidata: `4f0ca664dc62b5eeb0001db2a428111b8e1b8ff284b2d9b6c4e905d80b7cdb42`.

La differenza tra l'impronta del PDF esportato nello step 22 e quella dell'interno consegnato deriva dalla normalizzazione deterministica dei box pagina e dei metadati; i contenuti non sono stati scalati.

## Gate tecnici rieseguiti

| Gate | Esito |
| --- | --- |
| Suite Book Studio pertinenti | PASS — 7 file, 55 test |
| Typecheck | PASS — `tsc --noEmit` |
| Build produzione | PASS — Next.js 15.5.22, 20 pagine statiche |
| QA strutturale PDF | PASS — tutti i controlli obbligatori verdi |
| Manifest SHA-256 | PASS — tutte le impronte corrispondono |
| Diff del perimetro VOL-04 | PASS — nessun errore di whitespace |

Una prima esecuzione dei test aveva intercettato una modifica concorrente al test della preview; la riproduzione isolata e due nuove esecuzioni hanno confermato il comportamento corretto. L'esito finale registrato è 55/55.

## Esclusioni applicate

Lo staging selettivo esclude:

- file e report del VOL-11 e di ogni altro volume;
- log applicativi e output di processi locali;
- cache e backup di sincronizzazione;
- script temporanei di generazione, memoria e QA;
- rendering e immagini di controllo in `artifacts/` e `tmp/`;
- modifiche aggregate della memoria locale e del log wiki non separabili dal lavoro concorrente.

## Limiti e interventi umani residui

- KDP Print Previewer non è eseguibile localmente: deve essere avviato dopo il caricamento nello step umano.
- Autore, ISBN, diritti, territori, collana, finitura e prezzo definitivo richiedono conferma del titolare.
- È raccomandata una copia di prova fisica prima della pubblicazione.
- Se cambia la paginazione o la carta, la copertina deve essere rigenerata.
- Non è stato prodotto un EPUB; l'attuale candidato riguarda l'edizione cartacea.

## Decisione

Il pacchetto supera i controlli tecnici locali ed è idoneo al passaggio allo **step 24 — revisione e approvazione umana**. Questo report non sostituisce tale approvazione e non autorizza la pubblicazione.
