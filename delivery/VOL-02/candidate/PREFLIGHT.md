---
id: review-vol-02-step-22-preflight
type: review
title: "Preflight tecnico ed editoriale - VOL-02"
status: complete
domain: "concorsi pubblici italiani"
source_refs: ["reviews/pipeline/VOL-02/21-vol-02", "reviews/pipeline/VOL-02/22-vol-02-page-audit"]
book_refs: ["vol-02-enti-locali-polizia-locale"]
updated_at: 2026-08-09T13:00:00+02:00
review_required: false
canonical: true
tags: ["vol-02", "pipeline-step-22", "preflight", "pdf", "kdp"]
---

# Preflight tecnico ed editoriale — VOL-02

## Esito

Il preflight locale è superato. Il PDF candidato contiene 830 pagine, usa il trim KDP 6,69 × 9,61 pollici senza bleed, incorpora i quattro font di collana e corrisponde al corpus revisionato. Il difetto iniziale di due titoli orfani è stato corretto nel paginatore con test di regressione; la riesecuzione registra 0 bloccanti.

Il KDP Previewer esterno non è installato e non è stato simulato. Eventuali messaggi del servizio di upload dovranno essere registrati allo step di pubblicazione.

## Checklist pass/fail

| Controllo | Esito | Evidenza e comando o verifica usata |
| --- | --- | --- |
| Audit di copertura | PASS | Cinque matrici nel perimetro: M-FL01 62/62, M-FL02 69/69, M-FL03 25/25, M-FL04 75/75, volume 4/4; 0 blocker e 0 warning. |
| Link wiki | PASS | Gate dei capitoli e test pertinenti verdi; rinvii puntuali preservati nelle matrici e nei frontmatter. |
| `source_refs` | PASS | Audit specialistici dei quattro moduli chiusi; nessun capitolo privo delle fonti richieste dai gate. |
| Frontmatter | PASS | Indice generale e matrice aggregata riallineati; moduli e capitoli conservano gli stati conclusivi degli step 15-16. |
| Asset path | PASS | Rendering Book Studio: 10 immagini caricate, 0 `.missingAsset`, 0 immagini con dimensione nulla. |
| File mancanti | PASS | Presenti 4 capitoli di raccordo, 46 capitoli specialistici, 4 indici di modulo e i report obbligatori fino allo step 21. |
| Immagini duplicate | PASS | Gli asset PNG/SVG sono coppie di produzione intenzionali; il rendering usa 10 immagini senza duplicazioni visive consecutive. |
| Tabelle anomale | PASS | Audit DOM su 830 pagine: nessun overflow o collisione bloccante; tabelle lunghe spezzate con intestazione ripetuta. |
| Caratteri corrotti | PASS | Scansione del corpus sui marker `Ãƒ`, `Ã‚`, `â€™`, `ï¿½`: 0 occorrenze. |
| `git diff --check` | PASS | Nessun errore di whitespace. |
| Test pertinenti | PASS | `npm test`: 47 file e 429 test verdi prima della correzione; test di regressione dedicato: 2/2 verdi. |
| Typecheck | PASS | `npm run typecheck`: `tsc --noEmit`, exit code 0. |
| Build | PASS | `npm run build`: Next.js 15.5.18 compilato e 20/20 pagine statiche generate. |
| Export PDF | PASS | `BOOK_STUDIO_BOOK_ID=volumi/vol-02`, 830 pagine stabili; candidato in `delivery/VOL-02/candidate/vol-02-interior-kdp.pdf`. |
| Font incorporati | PASS | Risorse PDF subset: Arial Bold, Garamond, Arial Black e Arial; quattro stream `FontFile` presenti nel file. |
| Dimensione pagina | PASS | PyPDF: 830/830 pagine con MediaBox e CropBox 481,68 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici. |
| Bleed | PASS | Nessun bleed previsto; MediaBox e CropBox coincidono. |
| Margini | PASS | Layout canonico a colonna singola con gutter e margini interni al box pagina; nessun contenuto intercetta il footer nell'audit DOM. |
| Conteggio pagine | PASS | 830 pagine nel DOM stabile e 830 pagine nel PDF; numerazione progressiva verificata dall'audit. |
| Audit pagina per pagina | PASS | Riesecuzione su 830 pagine e 9 tavole-contatto: 0 bloccanti. I 14 segnali medi automatici sono stati riesaminati: 4 sono continuazioni intenzionali dell'indice analitico; gli altri riguardano spazi di chiusura prodotti da tabelle indivisibili o una tabella continuata con intestazione ripetuta, senza overflow, collisioni o titolo orfano. |
| Hash del candidato | PASS | SHA-256 `5A410CBE778D9F163684E8E97E0D643C44207E9C9B431E5A671085039262F29D`; dimensione 51.304.061 byte. |
| KDP Previewer | NON ESEGUITO | Applicazione esterna non disponibile; nessun warning inventato. Verifica da ripetere all'upload. |

## Correzione tecnica applicata

La baseline pagina per pagina rilevava titoli H3 isolati in fondo alle pagine 482 e 515. La causa era nel raffinamento post-render: gestiva l'overflow ma non ricontrollava il vincolo strutturale “heading con blocco successivo”. È stata introdotta una funzione pura che sposta l'ultimo heading sulla pagina successiva dello stesso capitolo, con due test di regressione. La verifica DOM finale su tutte le 830 pagine trova zero heading come ultimo elemento.

## Candidato verificato

- File: `delivery/VOL-02/candidate/vol-02-interior-kdp.pdf`
- Pagine: 830
- Trim: 6,69 × 9,61 pollici
- Bleed: assente
- Colore: bianco e nero
- SHA-256: `5A410CBE778D9F163684E8E97E0D643C44207E9C9B431E5A671085039262F29D`
- Stato: pronto per la preparazione selettiva del pacchetto dello step 23; non approvato e non pubblicato.
