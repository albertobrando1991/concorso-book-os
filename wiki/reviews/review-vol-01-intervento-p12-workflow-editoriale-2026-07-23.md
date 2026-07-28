---
id: review-vol-01-intervento-p12-workflow-editoriale-2026-07-23
type: review
title: "VOL-01 - Audit P12 sul workflow editoriale"
status: completed
domain: "concorsi pubblici italiani"
topics: ["workflow editoriale", "stati", "revisione"]
entities: ["VOL-01", "Metodo BANDO"]
book_refs: ["il-metodo-bando"]
confidence: 0.95
updated_at: "2026-07-23T00:00:00+02:00"
created_at: "2026-07-23T00:00:00+02:00"
review_required: true
canonical: true
issue_type: editorial_review
severity: medium
affected_pages: ["introduzione", "capitoli 1-24", "appendici A-F"]
tags: ["revisore-editoriale-totale", "vol-01", "p12", "workflow"]
---

# Report editoriale — Il Metodo BANDO

## 1. Sintesi editoriale
- Genere editoriale: manuale-workbook per concorsi pubblici italiani.
- Pubblico target: team editoriale e candidati, che non devono ricevere segnali contraddittori sullo stato di maturità del testo.
- Perimetro di questa revisione: frontmatter del cartaceo principale e workflow in `planning/03-workflow-editoriale.md`.
- Stato generale in una frase: 31 file del cartaceo usavano nove valori diversi di `draft_stage`; sono ora coerentemente in revisione editoriale.

## 2. Punti applicati della checklist
Applicati i punti 1, 4-5, 7-8 e 26, con focus sul workflow e sulla coerenza del frontmatter. Non applicabili gli altri punti: P12 non modifica contenuto, fonti o impaginazione dei capitoli.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P12-E01 | Introduzione, Capitoli 1-24, Appendici A-F | Workflow editoriale | Media | Nove valori di `draft_stage` descrivevano file tutti ancora soggetti a `review_required: true`, rendendo ambiguo il passaggio a impaginazione e pubblicazione. | Definire tre stati canonici e portare il perimetro principale a `editorial-review` fino alla chiusura dei gate. | Risolto |

## 4. Osservazioni per capitolo
### Volume cartaceo principale
- Punti di forza: introduzione, Capitoli 1-24 e Appendici A-F dichiarano ora lo stesso stato, compatibile con i blocker della matrice.
- Criticità: nessun capitolo può passare a `publication-ready` finché `review_required` è vero o un nucleo della matrice resta `parziale`.

### Ricettario operativo digitale
- Punti di forza: è rimasto fuori dal bulk update, preservando il perimetro editoriale del cartaceo.
- Criticità: richiede una propria revisione dedicata.

## 5. Coerenza globale
- Terminologia: `editorial-draft`, `editorial-review` e `publication-ready` sono definiti in una sola fonte operativa.
- Struttura vs indice: invariata.
- Promesse dell'introduzione mantenute: P12 non modifica promesse formative; rende soltanto affidabile il loro monitoraggio editoriale.

## 6. Contenuto da verificare
- Nessuno sul piano normativo; verificare in fase di rilascio che nessun tool esterno dipenda dai vecchi valori liberi di `draft_stage`.

## 7. Suggerimenti facoltativi (non errori)
- Esporre il nuovo stato nella dashboard con una descrizione breve, senza mostrare al lettore finale le note di lavorazione.

## 8. Priorità degli interventi
1. Chiudere le review umane e i 13 nuclei `parziale` della matrice.
2. Solo allora passare selettivamente i file a `publication-ready`.
3. Eseguire preview A4 completa prima della decisione di pubblicazione.

## 9. Giudizio di pubblicabilità
**Non pubblicabile allo stato attuale.** Motivazione: P12 chiude l'ambiguità del workflow, ma non modifica i gate didattici, normativi o di impaginazione ancora aperti.

## 10. Limiti di questa revisione
- Verifica effettuata sul repository e sul frontmatter; non è stata eseguita una prova della dashboard in questo passaggio.
