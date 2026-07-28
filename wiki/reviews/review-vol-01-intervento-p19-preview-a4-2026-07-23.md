---
id: review-vol-01-intervento-p19-preview-a4-2026-07-23
type: review
title: "VOL-01 - Audit P19 della preview A4"
status: completed
domain: "concorsi pubblici italiani"
topics: ["preview A4", "impaginazione", "kit finale"]
entities: ["VOL-01", "Metodo BANDO", "Book Studio"]
source_refs: ["sources/principio-copertura-didattica-integrale-2026-07-17.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.94
updated_at: "2026-07-23T00:00:00+02:00"
created_at: "2026-07-23T00:00:00+02:00"
review_required: true
canonical: true
issue_type: editorial_review
severity: medium
affected_pages: ["preview A4 dell'intero volume", "capitolo 23"]
tags: ["revisore-editoriale-totale", "vol-01", "p19", "a4"]
---

# Report editoriale — Il Metodo BANDO

## 1. Sintesi editoriale
- Genere editoriale: manuale-workbook per concorsi pubblici italiani.
- Pubblico target: candidati che usano il volume anche come strumento cartaceo operativo.
- Perimetro di questa revisione: preview A4 corrente del Book Studio e campione di pagine del capitolo 23.
- Stato generale in una frase: la preview runtime produce 349 pagine senza overflow del contenuto rispetto al piè di pagina; resta obbligatoria la prova su PDF/stampa finale.

## 2. Punti applicati della checklist
Applicati i punti 1-4, 6-11, 13-21 e 22-26 con controllo runtime della preview. L'evidenza è nel report tecnico `artifacts/vol01-p19-a4-report.json`: 349 pagine, 0 pagine con overflow oltre 8 px e overflow massimo pari a 0 px. Sono state catturate sei pagine del capitolo 23 (`artifacts/vol01-p19-page-269.png`–`274.png`) come evidenza di campionamento.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P19-E01 | Preview A4 runtime, 349 pagine | Overflow contenuto/piè di pagina | Grave | Il controllo DOM non rileva contenuti oltre il limite di pagina. | Nessuna correzione necessaria nella preview corrente. | Risolto |
| P19-E02 | PDF/esportazione e stampa | Prova di pubblicazione | Media | Il Book Studio non sostituisce un PDF di stampa, una prova su carta né un test con candidati. | Generare il PDF finale e svolgere una prova di stampa/compilazione prima del via libera. | Aperto |

## 4. Osservazioni per capitolo
### Capitolo 23 — Diario degli errori
- Punti di forza: le sei pagine campionate (269-274) rientrano nel limite della pagina e non presentano overflow misurato.
- Criticità: la compilabilità a penna va ancora osservata su stampa reale, non solo in preview.

### Intero volume
- Punti di forza: la preview ha prodotto 349 pagine e il controllo non ha rilevato collisioni del contenuto con il piè di pagina.
- Criticità: questo risultato non certifica font di stampa, margini della stampante, PDF o rilegatura.

## 5. Coerenza globale
- Terminologia: coerente con il workflow `editorial-review` e con il lessico del kit finale.
- Struttura vs indice: la paginazione runtime include il cartaceo principale senza sovrapporre contenuto e piè di pagina.
- Promesse dell'introduzione mantenute: il supporto workbook è tecnicamente leggibile in preview; la validazione d'uso resta distinta.

## 6. Contenuto da verificare
- PDF finale, prova di stampa e compilazione reale delle pagine workbook.
- Dati mobili di bandi, catalogo e piattaforme.

## 7. Suggerimenti facoltativi (non errori)
- Conservare le evidenze P19 insieme al futuro PDF di consegna, così da separare controllo runtime e prova tipografica.

## 8. Priorità degli interventi
1. Generare il PDF e svolgere prova di stampa/compilazione del kit e delle appendici.
2. Completare le review esterne giuridiche, madrelingua e psicometriche.
3. Rieseguire il gate della matrice solo dopo le evidenze specialistiche e di stampa.

## 9. Giudizio di pubblicabilità
**Non pubblicabile allo stato attuale.** Motivazione: P19 chiude il controllo di overflow della preview runtime, ma non la prova PDF/stampa né i 13 nuclei `parziale` della matrice.

## 10. Limiti di questa revisione
- Nessun PDF finale, prova di stampa o test con candidati disponibile.
- Il controllo è tecnico e non sostituisce le certificazioni esterne previste dal gate.
