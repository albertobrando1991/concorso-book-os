---
id: preflight-vol-06
type: preflight_report
title: "Preflight tecnico ed editoriale - VOL-06 Scuola, Università, Ricerca e Cultura"
status: completed
book_refs: ["vol-06-scuola-universita-ricerca-cultura"]
updated_at: 2026-08-23
created_at: 2026-08-23
review_required: false
canonical: false
tags: ["pipeline-step-22", "preflight", "volume-06"]
---

# Preflight tecnico ed editoriale - VOL-06

| Controllo | Esito | Evidenza |
| --- | --- | --- |
| Copertura didattica | PASS | `npm run audit:coverage -- --volume VOL-06`: 4 matrici, 50 righe complete, 0 blocker, 0 warning. |
| Stato pipeline | PASS | Quattro moduli completati e M-IR04 in text freeze con manifest. |
| Frontmatter e source refs | PASS | Frontmatter dei moduli e della scheda volume allineati; riferimenti tracciati nei report e nei capitoli. |
| Link e dipendenze interne | PASS | Controlli sui capitoli M-IR04: nessuna dipendenza editoriale nel testo lettore; i rinvii sono gestiti dalla pipeline. |
| Caratteri corrotti | PASS | Ricerca nei percorsi del volume e dei moduli IR01-IR04 senza riscontri bloccanti. |
| Asset e immagini | PASS | L'export PDF ha completato il controllo di immagini mancanti prima della generazione. |
| Tabelle | PASS | Test automatici di Markdown e layout superati nella suite completa. |
| Typecheck | PASS | `npm run typecheck` completato senza errori. |
| Build | PASS | `npm run build` completato: compilazione, validazione tipi, pagine statiche e build traces concluse. |
| Test | PASS | `npm test`: 65 file di test e 554 test superati. |
| Git diff check | WARN | `git diff --check` segnala esclusivamente hard break Markdown già presenti in opzioni di quiz di M-IR02 e un avviso CRLF in un manifest VOL-11 estraneo al volume; nessuna correzione applicata per non alterare il layout delle risposte o modifiche esterne allo scope. |
| PDF KDP | PASS | Export Book Studio con `BOOK_STUDIO_BOOK_ID=volumi/vol-06`: 530 pagine stabilizzate e PDF generato in `delivery/VOL-06/candidate/vol-06-interior-kdp.pdf` (3.487.971 byte). |
| Formato e bleed | PASS | `pdfinfo`: 481,92 × 691,92 pt, equivalenti a 6,69 × 9,61 in; rotazione 0; margini di stampa azzerati dal contratto PDF, quindi no bleed. |
| Font | PASS | `pdffonts`: Arial Bold, Arial, Garamond e CambriaMath incorporati e subset. |
| Conteggio pagine | PASS | `pdfinfo`: 530 pagine; coincide con il conteggio Book Studio stabilizzato. |
| KDP Previewer esterno | LIMIT | Non disponibile nell'ambiente; non viene inventato alcun esito. |

## Esito

Preflight superato senza blocker. Il solo warning di `git diff --check` riguarda hard break Markdown intenzionali e un file fuori dallo scope VOL-06; non compromette il PDF verificato. Le tavole campione delle pagine 1, 265 e 530 sono state renderizzate per controllo tecnico; l'ispezione immagine interattiva non è disponibile nella sandbox corrente.
