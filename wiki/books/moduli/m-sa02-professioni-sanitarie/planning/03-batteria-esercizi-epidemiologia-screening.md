---
id: m-sa02-batteria-esercizi-epidemiologia-screening
type: planning
title: "M-SA02 - Batteria verificata di esercizi su epidemiologia e screening"
status: draft
domain: "concorsi pubblici italiani"
source_refs:
  - "sources/epidemiologia-base-iss"
  - "sources/sorveglianza-passi-protocollo-operativo-iss"
  - "sources/programmi-screening-oncologici-dati-passi-iss"
book_refs: ["m-sa02-professioni-sanitarie", "vol-07-sanita-amministrativa-professioni-sanitarie"]
updated_at: 2026-07-29T17:30:00+02:00
created_at: 2026-07-29T17:30:00+02:00
review_required: true
canonical: false
tags: ["m-sa02", "esercizi", "epidemiologia", "screening", "passi", "pipeline-step-07"]
---

# Batteria verificata di esercizi su epidemiologia e screening

## Regole d'uso

Questa è una risorsa di pianificazione, non un capitolo pubblicabile. Ogni esercizio indica il dato ufficiale, il calcolo derivato e la cautela interpretativa. Le percentuali PASSI sono stime campionarie pesate: trasformarle in frequenze su 1.000 persone produce frequenze attese didattiche, non conteggi osservati.

## Esercizio 1 - Divario mammografico

**Dati ufficiali:** copertura mammografica totale PASSI 2021-2022: Italia 70,4%; Molise 50,6%.

**Quesito:** calcolare il divario assoluto e il rapporto Molise/Italia.

**Soluzione verificata:**

- divario assoluto: `70,4 - 50,6 = 19,8` punti percentuali;
- rapporto: `50,6 / 70,4 = 0,71875`, cioè circa `71,9%`.

**Interpretazione:** la copertura molisana stimata equivale a circa il 71,9% di quella nazionale. Non è corretto dire che sia “inferiore del 19,8%”: 19,8 è una differenza in punti percentuali.

## Esercizio 2 - Divario cervicale

**Dati ufficiali:** copertura cervicale totale PASSI 2021-2022: Italia 77,7%; Molise 53,5%.

**Quesito:** calcolare il divario assoluto e la riduzione relativa rispetto al valore nazionale.

**Soluzione verificata:**

- divario assoluto: `77,7 - 53,5 = 24,2` punti percentuali;
- riduzione relativa: `24,2 / 77,7 = 0,31145`, cioè circa `31,1%`.

**Interpretazione:** il dato regionale è inferiore di 24,2 punti percentuali, pari a circa il 31,1% del valore nazionale preso come riferimento. Il calcolo non spiega le cause del divario.

## Esercizio 3 - Gradiente geografico colorettale

**Dati ufficiali:** copertura colorettale PASSI 2023-2024: Nord 62%; Centro 55%; Sud 30%.

**Quesito:** calcolare la differenza Nord-Sud e il rapporto Nord/Sud.

**Soluzione verificata:**

- differenza: `62 - 30 = 32` punti percentuali;
- rapporto: `62 / 30 = 2,0667`, cioè circa `2,07`.

**Interpretazione:** la stima del Nord è poco più del doppio di quella del Sud. Il confronto descrive un'associazione geografica e non dimostra un nesso causale.

## Esercizio 4 - Frequenze attese su 1.000

**Dati ufficiali:** pool nazionale della tabella ISS 2025, screening colorettale: totale 47,4%; organizzato 39,3%; spontaneo 7,7%.

**Quesito:** esprimere le tre stime come frequenze attese su 1.000 persone target.

**Soluzione verificata:**

- totale: `0,474 × 1.000 = 474`;
- organizzato: `0,393 × 1.000 = 393`;
- spontaneo: `0,077 × 1.000 = 77`.

**Cautela:** `393 + 77 = 470`, non 474. Lo scarto di 4 per 1.000 riflette la trasformazione di stime arrotondate e pesate; non va corretto alterando i dati ufficiali.

## Esercizio 5 - Quota organizzata sul totale

**Dati ufficiali:** pool nazionale ISS 2025, screening colorettale: totale 47,4%; organizzato 39,3%.

**Quesito:** stimare quale quota della copertura totale è attribuita alla componente organizzata.

**Soluzione verificata:** `39,3 / 47,4 = 0,82911`, cioè circa `82,9%`.

**Interpretazione:** è un rapporto fra due stime di prevalenza, utile didatticamente. Non è una probabilità individuale né una misura di efficacia del programma.

## Esercizio 6 - Confronto Umbria-pool nazionale

**Dati ufficiali:** screening colorettale totale, Regione Umbria 60,6% (IC95% 56,8-64,2); pool nazionale 47,4% (IC95% 46,7-48,1).

**Quesito:** calcolare differenza assoluta e rapporto tra le stime puntuali; osservare gli intervalli.

**Soluzione verificata:**

- differenza: `60,6 - 47,4 = 13,2` punti percentuali;
- rapporto: `60,6 / 47,4 = 1,27848`, cioè circa `1,28`;
- gli intervalli riportati non si sovrappongono: `56,8 > 48,1`.

**Cautela:** la non sovrapposizione è un'indicazione descrittiva forte, ma una conclusione inferenziale formale richiede il metodo di confronto previsto dal disegno PASSI. Non si ricava causalità dal solo confronto.

## Esercizio 7 - Coerenza fra componenti

**Dati ufficiali:** pool nazionale ISS 2025, screening cervicale: totale 77,7%; organizzato 46,8%; spontaneo 30,7%.

**Quesito:** verificare la somma delle componenti e spiegare l'eventuale scarto.

**Soluzione verificata:** `46,8 + 30,7 = 77,5%`; scarto rispetto al totale: `77,7 - 77,5 = 0,2` punti percentuali.

**Interpretazione:** lo scarto è compatibile con arrotondamento e stima pesata. L'esercizio valuta la capacità di non forzare l'identità aritmetica fra valori pubblicati separatamente.

## Esercizio 8 - Numeratore e denominatore

**Definizione ufficiale:** per il sangue occulto fecale, la popolazione di riferimento è costituita da persone residenti e assistite nella ASL, 50-69 anni. Il numeratore comprende chi dichiara un test preventivo nei due anni precedenti; il denominatore comprende chi risponde di averlo o non averlo eseguito, escludendo rifiuti e “non so”.

**Scenario didattico:** 1.250 intervistati eleggibili; 50 rifiutano o rispondono “non so”; 516 dichiarano il test nei due anni precedenti.

**Quesito:** calcolare l'indicatore grezzo nello scenario.

**Soluzione verificata:**

- denominatore valido: `1.250 - 50 = 1.200`;
- indicatore: `516 / 1.200 = 0,43`, cioè `43,0%`.

**Cautela:** i conteggi dello scenario sono didattici, non dati PASSI reali. In un'analisi PASSI effettiva si applicano disegno campionario, pesi e procedure previste dal protocollo.

## Controllo della batteria

| Esercizio | Operazione verificata | Risultato |
| --- | --- | ---: |
| 1 | `70,4 - 50,6`; `50,6 / 70,4 × 100` | `19,8 pp`; `71,9%` |
| 2 | `77,7 - 53,5`; `24,2 / 77,7 × 100` | `24,2 pp`; `31,1%` |
| 3 | `62 - 30`; `62 / 30` | `32 pp`; `2,07` |
| 4 | percentuali `× 1.000` | `474`; `393`; `77` |
| 5 | `39,3 / 47,4 × 100` | `82,9%` |
| 6 | `60,6 - 47,4`; `60,6 / 47,4` | `13,2 pp`; `1,28` |
| 7 | `46,8 + 30,7`; `77,7 - 77,5` | `77,5%`; `0,2 pp` |
| 8 | `(1.250 - 50)`; `516 / 1.200 × 100` | `1.200`; `43,0%` |

## Review richiesta

I controlli riproducibili sono nella [[books/moduli/m-sa02-professioni-sanitarie/planning/05-pacchetto-review-epidemiologica-indipendente|checklist automatica epidemiologica]]. La loro predisposizione non equivale alla chiusura del gate: calcoli e inferenze devono essere verificati e corretti prima del freeze.

Prima di trasformare gli esercizi in contenuto editoriale servono:

1. controllo indipendente dei calcoli;
2. audit automatico epidemiologico su pesi, intervalli e formulazioni inferenziali;
3. verifica della versione dei dati al momento della pubblicazione;
4. separazione grafica tra dati osservati ufficiali e scenari didattici.
