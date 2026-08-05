---
id: review-vol-07-step-22-preflight
type: review
title: "Preflight tecnico ed editoriale - VOL-07"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/book-layout-typography-standards"
  - "reviews/pipeline/VOL-07/21-vol-07"
  - "reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina"
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-08-05T00:00:00+02:00
review_required: false
canonical: true
tags: ["vol-07", "pipeline-step-22", "preflight", "pdf", "kdp"]
---

# Preflight tecnico ed editoriale — VOL-07

## Esito

Il preflight locale è superato. Il candidato PDF contiene 394 pagine, usa il trim KDP 6,69 × 9,61 pollici senza bleed, incorpora tutte le risorse font e corrisponde al corpus che ha superato l'audit pagina per pagina. Non risultano errori bloccanti o significativi aperti.

Il KDP Previewer esterno non è installato e non è stato simulato: eventuali messaggi prodotti dal servizio di upload devono essere registrati nel passaggio di pubblicazione. Questo limite non viene dichiarato verde e non sostituisce un esito inesistente.

## Checklist pass/fail

| Controllo | Esito | Evidenza e comando o verifica usata |
| --- | --- | --- |
| Audit di copertura | PASS | Parser canonico `parseCoverageMatrix` + `auditCoverageRows` sulle cinque matrici VOL-07: 45/45 righe complete, 0 blocker, 0 warning. Le quattro matrici di modulo contengono 41 nuclei; la matrice di volume contiene quattro righe aggregate. |
| Link wiki | PASS | Scansione dei 25 capitoli: 8 rinvii interni, 8 target esistenti, 0 mancanti. |
| `source_refs` | PASS | Scansione con `parseFrontmatter`: 164 riferimenti dichiarati nei 25 capitoli, 0 capitoli privi di fonti, 0 target mancanti. |
| Frontmatter | PASS | 25/25 capitoli con stato e stadio coerenti; M-SA02 riallineato a `specialist-audit-complete`; test di corpus e volume verdi. |
| Asset path | PASS | Nessun riferimento immagine Markdown nei 25 capitoli; audit DOM senza `.missingAsset` o immagini non caricate. |
| File mancanti | PASS | Presenti indice volume, quattro indici modulo, 25 capitoli e i report obbligatori fino allo step 21. |
| Immagini duplicate | PASS | Nessuna immagine editoriale referenziata nel corpus dei capitoli; controllo non applicabile a elementi tipografici e loghi generati dal layout. |
| Tabelle anomale | PASS | Audit DOM finale: 394 pagine, 0 raw Markdown, 0 overflow, 0 collisioni, 0 tabelle fuori contenitore. |
| Caratteri corrotti | PASS | Scansione UTF-8 dei 25 capitoli sui marker `Ã`, `Â`, `â€` e `�`: 0 occorrenze. |
| `git diff --check` | PASS | Eseguito sull'intero worktree: nessun errore di whitespace. Le modifiche non pertinenti già presenti restano escluse dal pacchetto. |
| Test pertinenti | PASS | `npm test`: 47 file di test, 429 test passati, 0 fallimenti. |
| Typecheck | PASS | `npm run typecheck`: `tsc --noEmit`, exit code 0. |
| Build | PASS | `npm run build`: Next.js 15.5.18 compilato, typecheck interno e 20/20 pagine statiche generate. |
| Export PDF | PASS | `npm run export:volume-pdf`; output finale `delivery/VOL-07/candidate/vol-07-interior-kdp.pdf`. |
| Normalizzazione trim | PASS | PyPDF ha normalizzato l'arrotondamento nativo di Chromium da 481,92 pt a MediaBox/CropBox esatti 481,68 × 691,92 pt, scalando uniformemente il contenuto. |
| Font incorporati | PASS | Ispezione delle risorse PDF: Arial Bold, Garamond, Arial Black, Arial, Times New Roman in Type0 incorporato; risorsa Type3 con `CharProcs` incorporati; 0 font esterni mancanti. |
| Dimensione pagina | PASS | 394/394 pagine con MediaBox e CropBox 481,68 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici. |
| Bleed | PASS | Nessun bleed previsto; MediaBox e CropBox coincidono e il layout non contiene elementi al vivo. |
| Margini | PASS | Audit geometrico: gutter interno 23 mm, esterno 13 mm, superiore e inferiore 18 mm; per 394 pagine superano i minimi KDP applicabili al no-bleed. |
| Conteggio pagine | PASS | 394 pagine nel DOM stabile, 394 pagine nel PDF, numerazione progressiva 1-394. |
| Audit pagina per pagina | PASS | `BOOK_STUDIO_EXPECTED_PAGE_COUNT=394`, modalità `verify`: 20 tavole-contatto, 0 bloccanti, 0 significativi, nessuna pagina segnalata. |
| Hash del candidato | PASS | SHA-256 `2BA9C6C130CB52A17767815213A4F90ED7C876E6078E68AD71515A67AEB940A6`; dimensione 24.301.380 byte. |
| KDP Previewer | NON ESEGUITO | Comando locale non disponibile (`KDP_PREVIEWER_NOT_INSTALLED`); nessun warning è stato osservato o inventato. Verifica da ripetere nel servizio KDP al momento dell'upload. |

## Note operative

- Il comando globale `npm run audit:coverage -- --volume VOL-07` non applica il filtro richiesto e attraversa anche `.worktrees` e altri volumi; per il preflight è stato quindi eseguito direttamente il parser canonico sulle sole cinque matrici in perimetro.
- La cache `.next` del server di sviluppo è stata rigenerata dopo un errore locale `routes-manifest.json`; la riesecuzione pulita dell'audit e la build di produzione sono entrambe verdi.
- I file diagnostici temporanei usati per caratterizzare l'arrotondamento di Chromium sono stati rimossi. Le tavole-contatto restano in `artifacts/` come evidenza e non fanno parte del pacchetto di consegna.

## Candidato verificato

- File: `delivery/VOL-07/candidate/vol-07-interior-kdp.pdf`
- Pagine: 394
- Trim: 6,69 × 9,61 pollici
- Bleed: assente
- Colore: bianco e nero
- SHA-256: `2BA9C6C130CB52A17767815213A4F90ED7C876E6078E68AD71515A67AEB940A6`
- Stato: pronto per la preparazione selettiva del pacchetto di consegna dello step 23; non approvato e non pubblicato.
