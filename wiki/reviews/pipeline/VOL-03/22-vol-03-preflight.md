---
id: review-vol-03-step-22-preflight
type: review
title: "Preflight tecnico ed editoriale - VOL-03"
status: passed
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/book-layout-typography-standards"
  - "reviews/pipeline/VOL-03/21-vol-03"
book_refs: ["vol-03-fisco-dogane-previdenza-ispettivo"]
updated_at: 2026-08-12T18:50:00+02:00
review_required: true
canonical: true
tags: ["vol-03", "pipeline-step-22", "preflight", "pdf", "kdp"]
---

# Preflight tecnico ed editoriale — VOL-03

## Esito

**PASS — preflight manuale completato.** Il candidato finale è stato rigenerato dalla build validata del 12 agosto 2026. L'audit DOM completo registra 819 pagine stabili, numerazione progressiva, 0 anomalie bloccanti e 14 note non bloccanti riesaminate: tre continuazioni dell'indice completo, nove spazi pagina prodotti da blocchi indivisibili e due frammenti di paragrafo senza overflow. Il PDF rispetta il limite KDP di 828 pagine e il trim 6,69 × 9,61 pollici.
## Checklist pass/fail

| Controllo | Esito | Evidenza e comando o verifica usata |
| --- | --- | --- |
| Audit di copertura | **PASS** | Parser canonico `parseCoverageMatrix` + `auditCoverageRows`: matrice aggregata VOL-03, 67 righe, 0 blocker e 0 warning. Le righe 61-67 rinviano a 27 destinazioni precise nel VOL-01; verifica automatica locale: 27/27 file e heading risolti. |
| Link wiki | PASS | Audit editoriale step 21 e test `book-preview`/`text-volumes`: composizione del volume risolta; nessun link interno reader-inaccessibile residuo. |
| `source_refs` | PASS | Audit step 21: 100 riferimenti unici e 0 target mancanti nel corpus del volume. |
| Frontmatter | PASS | Test `frontmatter.test.ts` e scansione step 21; 59 sezioni caricate dal Book Studio. |
| Asset path | PASS | Book Studio: 140 asset dichiarati; audit DOM su 819 pagine, 0 immagini mancanti. |
| File mancanti | PASS | API Book Studio caricata con 59 sezioni; indici, capitoli e front matter presenti. |
| Immagini duplicate | PASS | Audit editoriale step 21: nessun duplicato bloccante; 70 riferimenti Markdown M-FC02 su 140 asset disponibili. |
| Tabelle anomale | PASS | Audit geometrico DOM: 0 tabelle fuori area utile su 819 pagine. |
| Caratteri corrotti | PASS | Scansione UTF-8 del corpus eseguita nello step 21: 0 marker di mojibake bloccanti. |
| `git diff --check` | PASS | Nessun errore di whitespace; solo avviso di futura normalizzazione CRLF sullo script di export. |
| Test pertinenti | PASS | 6 file mirati, 178 test passati; suite completa 428/429 con unico timeout estraneo VOL-07, poi test isolato passato 2/2. |
| Typecheck | PASS | `npm run typecheck`, exit code 0. |
| Build | PASS | `npm run build`: Next.js 15.5.18, compilazione riuscita e 20/20 pagine statiche generate. |
| Export PDF | PASS tecnico | `npm run export:volume-pdf` con `BOOK_STUDIO_BOOK_ID=volumi/vol-03`: PDF generato; lo script è stato riallineato alla modalità dashboard `advanced=1` e al pannello Book Studio effettivo. |
| Font incorporati | PASS | Ispezione struttura PDF: 12 riferimenti FontDescriptor e 5 stream FontFile; nessuna risorsa font esterna richiesta dal file. |
| Dimensione pagina | PASS | 819/819 pagine con MediaBox 481,92 × 691,92 pt, equivalenti a 6,69 × 9,61 pollici; assenza di CropBox esplicito, quindi il MediaBox è il box pagina effettivo. |
| Bleed | PASS | Nessun BleedBox o CropBox separato; profilo PDF basato sul MediaBox, senza bleed. |
| Margini | PASS | Audit DOM: 0 anomalie; margini speculari 23/13 mm e 18 mm sopra/sotto. |
| Conteggio pagine | PASS | DOM stabile e PDF: 819 pagine, numerazione progressiva, entro il limite KDP di 828 pagine. |
| Overflow e raw Markdown | PASS | Audit DOM: 0 overflow, 0 raw Markdown, 0 immagini mancanti. |
| Hash PDF | PASS | SHA-256 `357B144AE867BDED32195D75E47DC24A4898B180E6D91EC5AAD0C4EFB6234884`; 9.517.620 byte. |
| KDP Previewer | NON ESEGUITO | `KDP_PREVIEWER_NOT_INSTALLED`; nessun warning esterno è stato simulato o dichiarato verde. |

## Blocker da chiudere

- Riga 14: **CHIUSA il 12 agosto 2026** con fonte ufficiale consolidata, blocco didattico nel capitolo M-FC02 04 e rinvio preciso.
- Righe 40-43: **CHIUSE il 12 agosto 2026** con fonte strutturale verificata, quattro blocchi didattici nel capitolo M-FC03 03 e rinvii precisi; dati mobili esclusi dal testo stabile.
- Righe 45-46 e 57: **CHIUSE il 12 agosto 2026** con fonte ufficiale verificata, sequenza accesso-istruttoria-verbalizzazione, mappa ispettiva della sicurezza e laboratorio fatto-prova-conclusione.
- Righe 56 e 58: **CHIUSE il 12 agosto 2026** nel Bando Decoder trasversale con glossario fiscale-doganale-previdenziale-assicurativo e schemi 10/20/30 righe più orale specialistico.
- Riga 59: **CHIUSA il 12 agosto 2026** nel capitolo M-FC02 14 con fonte ufficiale consolidata, teoria minima, caso, errore e verifica.
- Righe 61-67: **CHIUSE il 12 agosto 2026** con 27 rinvii precisi e verificati ai capitoli VOL-01 su amministrativo, pubblico impiego, trasparenza-anticorruzione, privacy-CAD, contabilità pubblica, contratti e reati PA.

## Candidato tecnico finale

- File: `delivery/VOL-03/candidate/vol-03-interior-kdp.pdf`
- Pagine: 819
- Trim: 6,69 × 9,61 pollici
- Bleed: assente
- SHA-256: `357B144AE867BDED32195D75E47DC24A4898B180E6D91EC5AAD0C4EFB6234884`
- Stato: **candidato tecnico conforme al preflight manuale**; resta la preparazione della consegna dello step 23 e la conferma umana dello step 24.
