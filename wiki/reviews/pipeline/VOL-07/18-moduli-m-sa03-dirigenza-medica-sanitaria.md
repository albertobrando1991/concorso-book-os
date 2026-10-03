---
id: review-vol-07-step-18-m-sa03-image-audit
type: review
title: Audit immagini - M-SA03 Dirigenza medica e sanitaria
status: complete
domain: concorsi pubblici italiani
book_refs:
  - m-sa03-dirigenza-medica-sanitaria
  - vol-07-sanita-amministrativa-professioni-sanitarie
confidence: 1
updated_at: 2026-08-04T13:50:00+02:00
created_at: 2026-08-04T13:50:00+02:00
review_required: false
canonical: false
tags:
  - pipeline-step-18
  - image-audit
  - m-sa03
issue_type: image_audit
severity: none
affected_pages:
  - books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters
---

# Audit immagini — M-SA03 Dirigenza medica e sanitaria

## Esito

L'inventario dei sette capitoli non rileva directory asset, file immagine, wikilink immagine o immagini Markdown. Non esistono quindi asset da correggere o ottimizzare; non viene aggiunta grafica decorativa.

| Asset | Problema | Correzione | Verifica nel Book Studio | Esito |
| --- | --- | --- | --- | --- |
| Nessun asset | Nessuna immagine o path da revisionare | Non applicabile; inventario conservato senza creare asset | Zero riferimenti immagine e zero directory asset; nessun overflow, ritaglio o collisione attribuibile a immagini | conforme |

## Verifica di precisione

La seconda passata conferma sette file di capitolo, zero directory `assets/`, zero file immagine e zero riferimenti con sintassi wikilink o Markdown. Non sono presenti didascalie, sequenze di figure, griglie visuali o campi esercitativi dipendenti da immagini da controllare; contrasto, risoluzione, margini, proporzioni, palette e rapporto immagine-testo risultano pertanto non applicabili. L'assenza di asset esclude inoltre path spezzati e problemi di rendering imputabili alle immagini nel Book Studio.

## Regola per asset futuri

Ogni asset futuro deve seguire `Precisione Vitale`, dichiarare una funzione didattica e superare i controlli su testo, ordine di lettura, contrasto in bianco e nero, margini, risoluzione, proporzioni, didascalia, coerenza visuale e anteprima nel Book Studio prima dell'inserimento. Tabelle ed esercizi visuali non devono superare tre colonne compatte; le griglie dense vanno divise senza ridurre il carattere.


## Riesame di produzione del 3 ottobre 2026

Questa verifica aggiorna il precedente inventario senza cancellarlo. Prova corrente: `vol-07-release-20261003-proof.pdf`; hash e copertura nel registro `VOL-07-production-visual-checkpoint.json`.

| Asset | Problema | Correzione | Verifica nel Book Studio | Esito |
| --- | --- | --- | --- | --- |
| Apparati di M-SA03 | Verifica del contesto dopo le correzioni editoriali | Schede comparative e casi della dirigenza sanitaria osservati nelle pagine 315–379. Non sono presenti immagini raster. | Proiezione Book Studio esportata e controllata in PDF; panoramica di tutte le pagine e dettagli indicati | Verificato nel perimetro dichiarato |

La seconda passata ha controllato uniformità, margini, proporzioni e raccordi nelle tavole e nei dettagli. Corpo nominale 11 pt e tabelle 9,5 pt; nessun overflow geometrico o asset mancante. Le tavole panoramiche non equivalgono a lettura a piena risoluzione di ogni pagina. Nessun giudizio di pubblicabilità complessiva: promesse digitali e dati editoriali comuni restano aperti.
