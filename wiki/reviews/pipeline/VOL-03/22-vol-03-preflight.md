---
id: review-vol-03-step-22-preflight
type: review
title: "Preflight tecnico ed editoriale - VOL-03"
status: blocked
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/book-layout-typography-standards"
  - "reviews/pipeline/VOL-03/21-vol-03"
book_refs: ["vol-03-fisco-dogane-previdenza-ispettivo"]
updated_at: 2026-08-12T12:20:00+02:00
review_required: true
canonical: true
tags: ["vol-03", "pipeline-step-22", "preflight", "pdf", "kdp"]
---

# Preflight tecnico ed editoriale — VOL-03

## Esito

**FAIL — gate non ancora chiudibile.** L'audit canonico della copertura è ora verde: tutte le 67 righe della matrice aggregata superano il gate e i 27 rinvii delle righe 61-67 risolvono file e heading reali del VOL-01. Il candidato PDF resta però precedente alle correzioni editoriali del 12 agosto 2026 e deve essere rigenerato e ricontrollato prima del completamento dello step 22.

Il comando globale `npm run audit:coverage -- --volume VOL-03` non applica il filtro richiesto e attraversa anche `.worktrees` e altri volumi; l'esito vincolante qui riportato deriva dall'invocazione diretta del parser canonico sulle quattro matrici del solo VOL-03.

## Checklist pass/fail

| Controllo | Esito | Evidenza e comando o verifica usata |
| --- | --- | --- |
| Audit di copertura | **PASS** | Parser canonico `parseCoverageMatrix` + `auditCoverageRows`: matrice aggregata VOL-03, 67 righe, 0 blocker e 0 warning. Le righe 61-67 rinviano a 27 destinazioni precise nel VOL-01; verifica automatica locale: 27/27 file e heading risolti. |
| Link wiki | PASS | Audit editoriale step 21 e test `book-preview`/`text-volumes`: composizione del volume risolta; nessun link interno reader-inaccessibile residuo. |
| `source_refs` | PASS | Audit step 21: 100 riferimenti unici e 0 target mancanti nel corpus del volume. |
| Frontmatter | PASS | Test `frontmatter.test.ts` e scansione step 21; 59 sezioni caricate dal Book Studio. |
| Asset path | PASS | Book Studio: 140 asset dichiarati; audit DOM su 769 pagine, 0 immagini mancanti. |
| File mancanti | PASS | API Book Studio caricata con 59 sezioni; indici, capitoli e front matter presenti. |
| Immagini duplicate | PASS | Audit editoriale step 21: nessun duplicato bloccante; 70 riferimenti Markdown M-FC02 su 140 asset disponibili. |
| Tabelle anomale | PASS | Audit geometrico DOM: 0 tabelle fuori area utile su 769 pagine. |
| Caratteri corrotti | PASS | Scansione UTF-8 del corpus eseguita nello step 21: 0 marker di mojibake bloccanti. |
| `git diff --check` | PASS | Nessun errore di whitespace; solo avviso di futura normalizzazione CRLF sullo script di export. |
| Test pertinenti | PASS | 6 file mirati, 178 test passati; suite completa 428/429 con unico timeout estraneo VOL-07, poi test isolato passato 2/2. |
| Typecheck | PASS | `npm run typecheck`, exit code 0. |
| Build | PASS | `npm run build`: Next.js 15.5.18, compilazione riuscita e 20/20 pagine statiche generate. |
| Export PDF | PASS tecnico | `npm run export:volume-pdf` con `BOOK_STUDIO_BOOK_ID=volumi/vol-03`: PDF generato; lo script è stato riallineato alla modalità dashboard `advanced=1` e al pannello Book Studio effettivo. |
| Font incorporati | PASS | Ispezione struttura PDF: 6 FontDescriptor, 5 FontFile; nessuna risorsa font esterna richiesta dal file. |
| Dimensione pagina | PASS | 769/769 pagine con MediaBox e CropBox 481,68 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici. |
| Bleed | PASS | MediaBox e CropBox coincidono; profilo senza bleed. |
| Margini | PASS | Audit DOM: 0 anomalie; margini speculari 23/13 mm e 18 mm sopra/sotto. |
| Conteggio pagine | PASS | DOM stabile e PDF: 769 pagine, numerazione progressiva, entro il limite KDP di 828 pagine. |
| Overflow e raw Markdown | PASS | Audit DOM: 0 overflow, 0 raw Markdown, 0 immagini mancanti. |
| Hash PDF | PASS | SHA-256 `47BE45588E61BBDF1545D9C1175A416CEC66A2FC33CA525137043ECF18B7CFAD`; 9.304.348 byte. |
| KDP Previewer | NON ESEGUITO | `KDP_PREVIEWER_NOT_INSTALLED`; nessun warning esterno è stato simulato o dichiarato verde. |

## Blocker da chiudere

- Riga 14: **CHIUSA il 12 agosto 2026** con fonte ufficiale consolidata, blocco didattico nel capitolo M-FC02 04 e rinvio preciso.
- Righe 40-43: **CHIUSE il 12 agosto 2026** con fonte strutturale verificata, quattro blocchi didattici nel capitolo M-FC03 03 e rinvii precisi; dati mobili esclusi dal testo stabile.
- Righe 45-46 e 57: **CHIUSE il 12 agosto 2026** con fonte ufficiale verificata, sequenza accesso-istruttoria-verbalizzazione, mappa ispettiva della sicurezza e laboratorio fatto-prova-conclusione.
- Righe 56 e 58: **CHIUSE il 12 agosto 2026** nel Bando Decoder trasversale con glossario fiscale-doganale-previdenziale-assicurativo e schemi 10/20/30 righe più orale specialistico.
- Riga 59: **CHIUSA il 12 agosto 2026** nel capitolo M-FC02 14 con fonte ufficiale consolidata, teoria minima, caso, errore e verifica.
- Righe 61-67: **CHIUSE il 12 agosto 2026** con 27 rinvii precisi e verificati ai capitoli VOL-01 su amministrativo, pubblico impiego, trasparenza-anticorruzione, privacy-CAD, contabilità pubblica, contratti e reati PA.

## Candidato tecnico provvisorio

- File: `delivery/VOL-03/candidate/vol-03-interior-kdp.pdf`
- Pagine: 769
- Trim: 6,69 × 9,61 pollici
- Bleed: assente
- SHA-256: `47BE45588E61BBDF1545D9C1175A416CEC66A2FC33CA525137043ECF18B7CFAD`
- Stato: **non consegnabile** finché il PDF non viene rigenerato dopo le correzioni editoriali e sottoposto nuovamente ai controlli tecnici.
