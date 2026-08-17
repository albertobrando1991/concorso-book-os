---
type: pipeline_spec
volume_code: VOL-12
volume_title: Carriere speciali premium
cut_off_date: 2026-08-14
writer_provider: codex
phases: [A, B, C, D, E, F]
status: active
updated_at: 2026-08-14
review_required: true
---

# Scheda di pipeline — VOL-12

Input eseguibile della pipeline editoriale per VOL-12. Il protocollo dei 25 prompt resta in `[[templates/prompt-staff-revisione-completa-volumi]]`.

Le fasi A e B e la lavorazione editoriale della fase C sono concluse. La scheda dichiara ora i 32 capitoli approvati e abilita le fasi C-F. Il run-state viene esteso esclusivamente con `npm run pipeline -- sync VOL-12 --json`, senza modifiche manuali.

Lo step 24 resta una conferma umana conclusiva e non può essere chiuso automaticamente.

## Moduli

| Codice | Module id | Priorità | Fasi |
| --- | --- | ---: | --- |
| M-SP01 | moduli/m-sp01-forze-ordine | 1 | A,B,C,D,E,F |
| M-SP02 | moduli/m-sp02-vigili-fuoco | 2 | A,B,C,D,E,F |
| M-SP03 | moduli/m-sp03-magistratura-avvocatura-notariato | 3 | A,B,C,D,E,F |
| M-SP04 | moduli/m-sp04-prefettizia-diplomatica | 4 | A,B,C,D,E,F |

## Capitoli M-SP01

Fase C chiusa: 50 nuclei; review integrale chiusa; pubblicabile.

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Mappa della famiglia e struttura della selezione | chapters/01-mappa-famiglia-struttura-selezione.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 02 | La tua posizione prima della domanda | chapters/02-posizione-prima-domanda.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 03 | I formati della prova scritta | chapters/03-formati-prova-scritta.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 04 | Gli accertamenti e la preparazione | chapters/04-accertamenti-preparazione.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 05 | Prova orale, titoli e lingua facoltativa | chapters/05-prova-orale-titoli-lingua.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 06 | Le materie: riuso dal VOL-01 e specialistiche | chapters/06-materie-riuso-specialistiche.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 07 | Bando Decoder della famiglia | chapters/07-bando-decoder.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 08 | Piano 30/60/90 a doppio binario | chapters/08-piano-30-60-90-doppio-binario.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 09 | Errori frequenti e casi guidati | chapters/09-errori-casi-guidati.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 10 | Checklist finale del modulo | chapters/10-checklist-finale.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |

## Capitoli M-SP02

Fase C chiusa: 40 nuclei; review chiusa senza rilievi; pubblicabile.

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Mappa della famiglia: ruoli e selezioni | chapters/01-mappa-della-famiglia.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 02 | La tua posizione prima della domanda: requisiti, riserve e vie di accesso | chapters/02-la-tua-posizione-prima-della-domanda.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 03 | La preselezione: un cancello, non un esame | chapters/03-la-preselezione.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 04 | Le prove d'esame: tre prove motorio-attitudinali e i titoli | chapters/04-tre-prove-motorio-attitudinali.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 05 | Prove direttive e percorsi di specializzazione | chapters/05-prove-direttive-e-specializzazione.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 06 | Materie da riusare e Bando Decoder | chapters/06-riuso-e-bando-decoder.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 07 | Piano 30/60/90 per binario | chapters/07-piano-30-60-90.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 08 | Errori, casi guidati e checklist finale | chapters/08-errori-casi-checklist.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |

## Capitoli M-SP03

Fase C chiusa: 35 nuclei; review integrale chiusa; pubblicabile.

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Mappa delle tre professioni e scelta del binario | chapters/01-mappa-scelta-binario.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 02 | Magistratura ordinaria: accesso, prove e ordinamento | chapters/02-magistratura-prove-ordinamento.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 03 | Avvocatura dello Stato: selezione, prove e funzione | chapters/03-avvocatura-stato-prove-ordinamento.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 04 | Notariato: pratica, atti e ordinamento | chapters/04-notariato-prove-ordinamento.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 05 | Metodo per tema, atto e prova teorico-pratica | chapters/05-metodo-prove-scritte.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 06 | Piano pluriennale e gestione delle incognite | chapters/06-piano-pluriennale.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 07 | Errori tipici, casi integrati e checklist finale | chapters/07-errori-casi-checklist.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |

## Capitoli M-SP04

Fase C chiusa: 37 nuclei; review chiusa; pubblicabile.

| # | Titolo | File | Matrice | Stato atteso | Note |
| --- | --- | --- | --- | --- | --- |
| 01 | Mappa, scelta del binario e Bando Decoder | chapters/01-mappa-scelta-bando-decoder.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 02 | Carriera prefettizia: prove, materie e ordinamento | chapters/02-carriera-prefettizia-prove-materie-ordinamento.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 03 | Carriera diplomatica: prove, materie e ordinamento | chapters/03-carriera-diplomatica-prove-materie-ordinamento.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 04 | Le lingue straniere: diagnosi, prove e manutenzione | chapters/04-le-lingue-straniere.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 05 | La prova orale e la postura professionale | chapters/05-prova-orale-postura-professionale.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 06 | Piano di preparazione, carico e tentativi | chapters/06-piano-preparazione-tentativi.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |
| 07 | Errori, casi e checklist finali | chapters/07-errori-casi-checklist.md | planning/02-matrice-copertura-didattica.md | completo | Gate di capitolo e review di modulo chiusi |

## Stato editoriale acquisito

- M-SP01: dieci capitoli, 50 nuclei, pubblicabile dopo chiusura del solo rilievo sul link istituzionale.
- M-SP02: otto capitoli, 40 nuclei, pubblicabile senza rilievi.
- M-SP03: sette capitoli, 35 nuclei, pubblicabile dopo review integrale e una correzione lessicale lieve.
- M-SP04: sette capitoli, 37 nuclei, pubblicabile dopo correzione del valore `ABcomune` nel binario.

## Vincoli di volume

- M-SP01 esclude le Forze armate in senso proprio.
- M-SP03 mantiene tre binari separati; M-SP04 ne mantiene due.
- Il notariato è incluso per affinità di preparazione ma non costituisce accesso al pubblico impiego.
- Gli orizzonti dei piani di studio restano differenziati per modulo.
- Dati di tornata, soglie, calendari, materiali e modalità vanno ricontrollati al text freeze.

## Prosecuzione

```text
npm run pipeline -- doctor --json
npm run pipeline -- sync VOL-12 --json
npm run pipeline -- status VOL-12 --json
npm run pipeline -- next VOL-12 --json
```
