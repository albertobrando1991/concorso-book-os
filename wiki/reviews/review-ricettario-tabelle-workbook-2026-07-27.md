---
id: review-ricettario-tabelle-workbook-2026-07-27
type: review
title: Correzione delle tabelle workbook del Ricettario digitale
status: completed
domain: editoriale-visivo
topics:
  - ricettario-digitale
  - tabelle-workbook
  - book-studio
entities: []
source_refs: []
book_refs:
  - il-metodo-bando
confidence: high
updated_at: 2026-07-27
created_at: 2026-07-27
review_required: false
canonical: false
tags:
  - markdown
  - impaginazione
  - kdp
---

# Correzione delle tabelle workbook del Ricettario digitale

## Difetto

Le tabelle compilabili composte soltanto da righe vuote venivano private delle righe dal parser del Book Studio. L'intestazione e il separatore rimasti non costituivano più una tabella valida e venivano mostrati come testo continuo con pipe e sequenze `|---|`.

## Correzione

Il parser conserva ora le righe vuote intenzionali come campi workbook reali. La modifica è generale e corregge tutte le schede analoghe, compresi i blocchi “Fonte controllata” e “Cosa aggiorno oggi?” del modulo R1.

## Verifiche

| Controllo | Esito |
|---|---:|
| Capitoli Ricettario verificati | 23 |
| Blocchi tabella verificati | 720 |
| Righe workbook vuote preservate | 60 |
| Separatori Markdown mostrati come testo | 0 |
| Tabelle fuori pagina o sul piè di pagina | 0 |

È stato aggiunto un test di regressione specifico per impedire che le righe compilabili vuote vengano nuovamente eliminate.
