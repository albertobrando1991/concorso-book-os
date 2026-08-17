---
id: review-vol-12-step-22-preflight
type: review
title: "Preflight tecnico ed editoriale - VOL-12"
status: complete
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/book-layout-typography-standards"
  - "reviews/pipeline/VOL-12/21-vol-12"
  - "reviews/pipeline/VOL-12/20-vol-12-audit-pagina-per-pagina"
book_refs: ["vol-12-carriere-speciali-premium"]
updated_at: 2026-08-14T19:00:00+02:00
review_required: false
canonical: true
tags: ["vol-12", "pipeline-step-22", "preflight", "pdf", "kdp"]
---

# Preflight tecnico ed editoriale - VOL-12

## Esito

Il preflight locale è superato. Il candidato PDF contiene 459 pagine, usa il trim KDP 6,69 × 9,61 pollici senza bleed, incorpora tutte le risorse font e corrisponde al corpus sottoposto all'audit pagina per pagina. Non risultano errori bloccanti o significativi aperti.

Il KDP Previewer esterno non è installato e non è stato simulato. Eventuali messaggi prodotti dal servizio di upload dovranno essere registrati al momento della pubblicazione: questo limite non viene dichiarato verde.

## Checklist pass/fail

| Controllo | Esito | Evidenza e comando o verifica usata |
| --- | --- | --- |
| Audit di copertura | PASS | Scansione delle quattro matrici: 50 + 40 + 35 + 37 = 162 nuclei `completo`; 0 `parziale`, `solo-nominato`, `mancante`, `bloccante` o `rinviato`. |
| Link wiki | PASS | Scansione di indici, Bibbia e capitoli: 90 rinvii, 90 target risolti, 0 mancanti. |
| `source_refs` | PASS | 57 riferimenti dichiarati nei 32 capitoli, 16 source note uniche, 0 capitoli senza fonte e 0 target mancanti. |
| Frontmatter | PASS | 32/32 capitoli `revised_draft`, `specialist-audit-complete`, `review_required: false`; quattro moduli `text_frozen`. |
| Asset path | PASS | Nessun riferimento immagine Markdown nei capitoli; audit DOM senza `.missingAsset` o immagini non caricate. |
| File mancanti | PASS | Presenti indice volume, Bibbia, quattro indici modulo, 32 capitoli, quattro matrici e report obbligatori fino allo step 21. |
| Immagini duplicate | PASS | Nessuna immagine editoriale referenziata nel corpus; duplicati 0. |
| Tabelle anomale | PASS | Audit DOM su 459 pagine: 0 raw Markdown, 0 overflow, 0 collisioni, 0 tabelle fuori contenitore e 0 continuazioni prive di intestazione iniziale. |
| Caratteri corrotti | PASS | Scansione UTF-8 dei file e del testo PDF: 0 marker mojibake, 0 caratteri sostitutivi U+FFFD. |
| Placeholder e residui | PASS | Testo estratto dal PDF: 0 `TODO`, `TBD`, `PLACEHOLDER`, separatori `---` o formula interna “pricing alto”. |
| `git diff --check` | PASS NEL PERIMETRO | Nessun errore nei file VOL-12, nei componenti di impaginazione e nei test pertinenti. Il controllo globale segnala whitespace in M-FL02/M-FL04, modifiche estranee già presenti e non alterate. |
| Test pertinenti e globali | PASS | `npm test`: 59 file, 452 test passati, 0 fallimenti. |
| Typecheck | PASS | `npm run typecheck`: `tsc --noEmit`, exit code 0 dopo l'allineamento tipologico dei fixture di audit. |
| Build | PASS | `npm run build`: Next.js 15.5.18 compilato; 20/20 pagine statiche generate. |
| Pipeline doctor | PASS | `npm run pipeline -- doctor --json`: Node, dipendenze, Playwright, git, prompt e merge driver verdi. |
| Export PDF | PASS | Export Book Studio sul file `delivery/VOL-12/candidate/vol-12-interior-kdp.pdf`, DOM stabile a 459 pagine. |
| Normalizzazione trim | PASS | PyPDF ha normalizzato l'arrotondamento nativo di Chromium da 481,92 pt a MediaBox/CropBox/TrimBox/BleedBox esatti 481,68 × 691,92 pt, con scala uniforme 0,999502. |
| Font incorporati | PASS | `pdffonts`: Arial Bold, Garamond, Arial Black, Arial in CID TrueType incorporato; Cambria Math Type3 incorporato; 0 font esterni mancanti. |
| Dimensione pagina | PASS | Verifica PyPDF su 459/459 pagine: tutte le box misurano 481,68 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici. |
| Bleed | PASS | Nessun bleed previsto; MediaBox, CropBox, TrimBox e BleedBox coincidono e non vi sono elementi al vivo. |
| Margini | PASS | Audit geometrico del master: gutter interno 23 mm, esterno 13 mm, superiore e inferiore 18 mm. |
| Conteggio pagine | PASS | 459 pagine nel DOM stabile, 459 nel PDF, numerazione progressiva 1-459. |
| Audit pagina per pagina | PASS | Modalità `verify` sul corpus finale: 23 tavole-contatto, 0 bloccanti, 0 significativi, mediana spazio libero 79 px. |
| Testo PDF | PASS | `pdftotext -layout`: 1.275.262 caratteri estraibili, promessa reader-facing presente, 0 marker corrotti o placeholder. |
| Cifratura e script | PASS | `pdfinfo`: PDF 1.4, non cifrato, nessun JavaScript o modulo. |
| Hash del candidato | PASS | SHA-256 `F8ECF8499C19BF7727F4BB72314CAA84DF828C911DD16D0918DAA278079609F9`; dimensione 30.870.171 byte. |
| KDP Previewer | NON ESEGUITO | Comando locale non disponibile; nessun warning è stato osservato o inventato. Verifica da ripetere nel servizio KDP al momento dell'upload. |

## Note operative

- Il candidato è stato riesportato dopo la correzione reader-facing del frontespizio e l'audit delle 459 pagine è stato ripetuto sulla stessa versione editoriale.
- Le tavole-contatto finali restano in `artifacts/` come evidenza e non fanno parte del pacchetto di consegna.
- I manifest di text freeze dei quattro moduli sono stati rigenerati dopo l'allineamento dei metadati dello step 21.
- Le anomalie whitespace esterne a VOL-12 non sono state modificate per preservare il lavoro altrui nel working tree condiviso.

## Candidato verificato

- File: `delivery/VOL-12/candidate/vol-12-interior-kdp.pdf`
- Pagine: 459
- Trim: 6,69 × 9,61 pollici
- Bleed: assente
- Colore: bianco e nero
- SHA-256: `F8ECF8499C19BF7727F4BB72314CAA84DF828C911DD16D0918DAA278079609F9`
- Stato: pronto per la preparazione selettiva del pacchetto di consegna dello step 23; non approvato e non pubblicato.
