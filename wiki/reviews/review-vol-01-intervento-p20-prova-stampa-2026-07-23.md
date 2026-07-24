---
id: review-vol-01-intervento-p20-prova-stampa-2026-07-23
type: review
title: "VOL-01 - P20 verifica del percorso PDF e prova di stampa"
status: completed
domain: "concorsi pubblici italiani"
topics: ["prova di stampa", "PDF", "Book Studio"]
entities: ["VOL-01", "Metodo BANDO", "Book Studio"]
source_refs: ["sources/principio-copertura-didattica-integrale-2026-07-17.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.98
updated_at: "2026-07-23T00:00:00+02:00"
created_at: "2026-07-23T00:00:00+02:00"
review_required: true
canonical: true
issue_type: editorial_review
severity: high
affected_pages: ["Book Studio", "intero volume"]
tags: ["revisore-editoriale-totale", "vol-01", "p20", "pdf", "stampa"]
---

# Report editoriale — Il Metodo BANDO

## 1. Sintesi editoriale
- Genere editoriale: manuale-workbook per concorsi pubblici italiani.
- Pubblico target: candidati che devono poter leggere e compilare il volume anche su carta.
- Perimetro di questa revisione: verifica del percorso effettivamente disponibile per PDF e prova di stampa dopo la P19.
- Stato generale in una frase: il Book Studio offre una preview A4 runtime, ma non un comando di stampa, un export PDF né un endpoint di generazione del PDF.

## 2. Punti applicati della checklist
Applicati i punti 1-4, 13-21 e 22-30 per il controllo dell'apparato e della pubblicabilità. Ispezionati il pannello Book Studio, le route API e le occorrenze di `pdf`, `print`, `window.print` ed `export` nel codice applicativo. La P19 resta valida come controllo di overflow della preview, ma non diventa prova tipografica.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P20-E01 | `app/components/book-studio-panel.tsx`, API Book Studio | Produzione editoriale / layout | Grave | Non esiste un percorso applicativo per esportare il volume in PDF o avviare la stampa; l'API restituisce solo dati della preview. | Introdurre un export PDF deterministico oppure definire e usare un flusso editoriale esterno versionato, con preset A4, font incorporati, margini e numerazione verificabili. | Aperto |
| P20-E02 | Intero volume | Prova di pubblicazione | Media | Senza PDF non si possono certificare margini della stampante, font di output, rilegatura e compilabilità a penna. | Eseguire una prova di stampa su PDF finale e registrare esito, data, stampante/preset e pagine campionate. | Aperto |

## 4. Osservazioni per capitolo
### Intero volume
- Punti di forza: la preview runtime P19 ha controllato 349 pagine senza overflow misurato.
- Criticità: la preview non è un file di consegna e non conserva una configurazione di stampa ripetibile.

## 5. Coerenza globale
- Terminologia: `preview A4`, `PDF finale` e `prova di stampa` sono ora distinti in modo esplicito.
- Struttura vs indice: nessun impatto sul contenuto o sulla matrice di copertura.
- Promesse dell'introduzione mantenute: l'autonomia cartacea richiede una prova sul supporto cartaceo, ancora non disponibile.

## 6. Contenuto da verificare
- Preset di esportazione: formato A4, margini, font incorporati, numerazione e gestione delle tabelle.
- Prova di stampa e compilazione del diario, cruscotto, checklist e appendici.

## 7. Suggerimenti facoltativi (non errori)
- Salvare il PDF approvato con hash/versione accanto al report di prova, per rendere ripetibile il controllo pre-stampa.

## 8. Priorità degli interventi
1. Definire il percorso di generazione del PDF e produrre un file di prova.
2. Svolgere prova di stampa e compilazione sulle pagine workbook.
3. Completare le review esterne giuridiche, madrelingua e psicometriche.
4. Rieseguire il gate della matrice dopo le evidenze richieste.

## 9. Giudizio di pubblicabilità
**Non pubblicabile allo stato attuale.** Motivazione: l'assenza di un PDF/prova di stampa blocca la chiusura del requisito di produzione e restano 13 nuclei `parziale` soggetti a review specialistica.

## 10. Limiti di questa revisione
- Non è stato implementato un export, perché l'incarico riguarda la revisione editoriale e non autorizza modifiche funzionali alla piattaforma.
- Nessun PDF finale o prova su carta era disponibile nel workspace.
