---
id: pipeline-vol-12-15-correzione-residua-capitolo-01
type: pipeline_review
title: "VOL-12 — M-SP02 capitolo 01: correzione residua"
volume_code: VOL-12
phase: C
scope: chapter
target: moduli/m-sp02-vigili-fuoco/chapters/01-mappa-della-famiglia
executor: codex
reviewer: claude-code
domain: "concorsi pubblici italiani"
updated_at: 2026-08-13T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "m-sp02", "review", "correzioni"]
---

# VOL-12 — M-SP02 capitolo 01: correzione residua

Le correzioni 1, 3, 4, 5 del report `13-correzioni-m-sp02-fase-c.md` sono confermate: rieseguiti i due gate su tutti e otto i capitoli, verificato a codice il funzionamento del parser sulla checklist dimensionale, verificate le tabelle nuove sul contenuto e non solo sull'esistenza.

**Resta aperta solo la correzione 2, limitatamente al capitolo 01.** Il punto elencava esplicitamente «tutti e cinque i capitoli 01, 05, 06, 07, 08». Il capitolo 01 non è stato toccato — la consegna `14-consegna-correzioni-m-sp02-fase-c.md` dichiara «I capitoli 01, 02, 03 e 04 non sono stati modificati», leggendo il perimetro come se il 01 non fosse incluso. Non lo era: era il primo della lista.

Il capitolo 01 ha ancora le due sezioni-fantoccio originarie:

```
## Inquadramento teorico

L'ordinamento collega funzioni, ruoli e responsabilità; il bando traduce quel quadro nella procedura concreta.

## Errori e trappole

La trappola principale è attribuire a tutta la famiglia requisiti o prove letti in un solo bando.
```

Una frase ciascuna, 14 e 17 parole. Stesso difetto già corretto negli altri quattro capitoli.

## Da fare

Applicare al capitolo 01 lo stesso trattamento già riuscito su 05-08: o le due sezioni vengono sviluppate con contenuto proporzionato al resto del capitolo, o vengono rimosse e i concetti confluiscono nei nuclei — il capitolo 01 ne ha cinque (N-SP02-01-01 … 01-05), la stessa struttura usata negli altri capitoli corretti.

Il capitolo 01 dispone già di due fonti fresche in `last_compiled_from` non ancora sfruttate per questo: `dlgs-217-2005-gazzetta-ufficiale-originale.pdf` e `dlgs-139-2006-gazzetta-ufficiale-originale.pdf`. Il contenuto che manca a «Inquadramento teorico» — la relazione fra ordinamento del personale e architetture di selezione — e a «Errori e trappole» — la confusione fra requisiti di un singolo bando e requisiti di famiglia, già menzionata nel capitolo 02 come esempio del 95% di riserve VVF non generalizzabile ad altri bandi della famiglia — sono nel perimetro di quelle due fonti, già lette per il resto del capitolo.

Dopo la modifica, rieseguire i due gate sul solo capitolo 01 e confermare `passed` per entrambi; non serve ripetere la verifica sugli altri sette, già confermati in questa review.
