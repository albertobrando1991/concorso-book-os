---
id: review-pipeline-vol-05-step-18-m-fc05
type: review
title: "VOL-05 step 18 — audit immagini M-FC05"
status: complete
book_id: vol-05-authority-regolazione
module_code: M-FC05
updated_at: 2026-08-22
review_required: false
canonical: true
---

# Audit e ottimizzazione immagini — M-FC05

## Esito

Audit automatico e seconda passata di precisione su 75 asset PNG e relativi master SVG. Verificati: dimensioni, rapporto, esistenza del master, riferimenti nei capitoli, metadati accessibili, viewBox, geometria del testo rispetto ai safe-box, margini globali e coerenza del set.

Nessun overflow, ritaglio, collisione o riferimento rotto rilevato. Tutti gli asset sono 1600×1000 px, hanno master SVG e sono collocati nel rispettivo capitolo.

## Matrice operativa

| Asset | Problema | Correzione | Verifica nel Book Studio | Esito |
| --- | --- | --- | --- | --- |
| `chapter-01/01-mappa-bando-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 21 testi SVG controllati | conforme |
| `chapter-01/02-authority-settori-poteri.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 28 testi SVG controllati | conforme |
| `chapter-01/03-percorsi-g-e-p.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 20 testi SVG controllati | conforme |
| `chapter-01/04-nucleo-comune-delta-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 17 testi SVG controllati | conforme |
| `chapter-01/05-bando-decoder-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 20 testi SVG controllati | conforme |
| `chapter-02/01-mappa-bando-indipendenza-governance-accountability-personale.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-02/02-architettura-indipendenza-governance-accountability-personale.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-02/03-flusso-indipendenza-governance-accountability-personale.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-02/04-distinzioni-indipendenza-governance-accountability-personale.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-02/05-sintesi-indipendenza-governance-accountability-personale.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-03/01-mappa-bando-regolazione-europea-reti.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-03/02-architettura-regolazione-europea-reti.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-03/03-flusso-regolazione-europea-reti.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-03/04-distinzioni-regolazione-europea-reti.png` | due etichette superavano il safe-box nella prima passata | font adattivo ridotto da 21 a 16 px e coppia SVG/PNG rigenerata | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-03/05-sintesi-regolazione-europea-reti.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-04/01-mappa-bando-ciclo-regolatorio-air-vir.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-04/02-architettura-ciclo-regolatorio-air-vir.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-04/03-flusso-ciclo-regolatorio-air-vir.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-04/04-distinzioni-ciclo-regolatorio-air-vir.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-04/05-sintesi-ciclo-regolatorio-air-vir.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-05/01-mappa-bando-vigilanza-istruttoria-prova.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-05/02-architettura-vigilanza-istruttoria-prova.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-05/03-flusso-vigilanza-istruttoria-prova.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-05/04-distinzioni-vigilanza-istruttoria-prova.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-05/05-sintesi-vigilanza-istruttoria-prova.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-06/01-mappa-bando-sanzioni-impegni-rimedi.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-06/02-architettura-sanzioni-impegni-rimedi.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-06/03-flusso-sanzioni-impegni-rimedi.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-06/04-distinzioni-sanzioni-impegni-rimedi.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-06/05-sintesi-sanzioni-impegni-rimedi.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-07/01-mappa-bando-economia-regolazione-dati.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-07/02-architettura-economia-regolazione-dati.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-07/03-flusso-economia-regolazione-dati.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-07/04-distinzioni-economia-regolazione-dati.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-07/05-sintesi-economia-regolazione-dati.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-08/01-mappa-bando-agcm-concorrenza-consumatore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-08/02-architettura-agcm-concorrenza-consumatore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-08/03-flusso-agcm-concorrenza-consumatore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-08/04-distinzioni-agcm-concorrenza-consumatore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-08/05-sintesi-agcm-concorrenza-consumatore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-09/01-mappa-bando-arera-servizi-tariffe.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-09/02-architettura-arera-servizi-tariffe.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-09/03-flusso-arera-servizi-tariffe.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-09/04-distinzioni-arera-servizi-tariffe.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-09/05-sintesi-arera-servizi-tariffe.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-10/01-mappa-bando-agcom-media-piattaforme.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-10/02-architettura-agcom-media-piattaforme.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-10/03-flusso-agcom-media-piattaforme.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-10/04-distinzioni-agcom-media-piattaforme.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-10/05-sintesi-agcom-media-piattaforme.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-11/01-mappa-bando-consob-mercati-investitore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-11/02-architettura-consob-mercati-investitore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-11/03-flusso-consob-mercati-investitore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-11/04-distinzioni-consob-mercati-investitore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-11/05-sintesi-consob-mercati-investitore.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-12/01-mappa-bando-banca-italia-ivass.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-12/02-architettura-banca-italia-ivass.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-12/03-flusso-banca-italia-ivass.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-12/04-distinzioni-banca-italia-ivass.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-12/05-sintesi-banca-italia-ivass.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-13/01-mappa-bando-garante-privacy-cooperazione.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-13/02-architettura-garante-privacy-cooperazione.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-13/03-flusso-garante-privacy-cooperazione.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-13/04-distinzioni-garante-privacy-cooperazione.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-13/05-sintesi-garante-privacy-cooperazione.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-14/01-mappa-bando-anac-prevenzione-whistleblowing.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-14/02-architettura-anac-prevenzione-whistleblowing.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-14/03-flusso-anac-prevenzione-whistleblowing.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-14/04-distinzioni-anac-prevenzione-whistleblowing.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-14/05-sintesi-anac-prevenzione-whistleblowing.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |
| `chapter-15/01-mappa-bando-laboratorio-prove-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 15 testi SVG controllati | conforme |
| `chapter-15/02-architettura-laboratorio-prove-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-15/03-flusso-laboratorio-prove-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 11 testi SVG controllati | conforme |
| `chapter-15/04-distinzioni-laboratorio-prove-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 12 testi SVG controllati | conforme |
| `chapter-15/05-sintesi-laboratorio-prove-authority.png` | nessuno | nessuna modifica necessaria | riferimento presente; 1600×1000; 13 testi SVG controllati | conforme |

## Controlli di insieme

- 15 cartelle capitolo, ciascuna con 5 PNG e 5 SVG.
- Palette, tratti, raggi, font e proporzione 8:5 coerenti con il movimento “Regolazione trasparente”.
- Le cinque funzioni ricorrenti — mappa, architettura, sequenza, distinzioni e sintesi — hanno raccordo testuale nel capitolo e didascalie differenziate.
- Nessuna griglia supera tre colonne compatte; il testo resta supporto della composizione e non sostituisce la spiegazione nel capitolo.
- Il colore non è l'unico codice: titoli, forme e posizione mantengono la lettura anche in scala di grigi.

## Seconda passata

La seconda passata ha ricontrollato allineamenti, margini, viewBox, safe-box, ruolo accessibile, corrispondenza PNG/SVG e presenza delle 75 occorrenze nel manoscritto. Non sono emersi difetti residui; non sono stati aggiunti elementi decorativi.

## Ispezione visiva

I tre contact sheet da 25 figure sono stati ispezionati al 100%: gerarchia, contrasto, ritmo, coerenza di palette, leggibilità delle etichette e assenza di contenuto decorativo non funzionale risultano conformi. Le tavole di controllo sono in artifacts/VOL-05/image-audit/.
