---
id: review-m-fc05-integrazione-visiva-2026-07-27
type: review
title: "Audit integrazione visiva M-FC05"
status: completed_with_review
domain: concorsi pubblici italiani
topics: ["authority indipendenti", "design editoriale", "infografiche didattiche"]
entities: ["Metodo BANDO", "AGCM", "ARERA", "AGCOM", "CONSOB", "Banca d'Italia", "IVASS", "Garante per la protezione dei dati personali", "ANAC"]
source_refs: ["sources/vol-05-dossier-editoriale-authority-regolazione-v4.md", "sources/metodo-bando-progetto-editoriale.md", "sources/struttura-madre-il-metodo-bando.md"]
book_refs: ["moduli/m-fc05-authority-indipendenti", "vol-05-authority-regolazione", "il-metodo-bando"]
confidence: 0.9
updated_at: 2026-07-27
created_at: 2026-07-27
review_required: false
canonical: true
tags: ["audit", "m-fc05", "visual-editorial", "assets"]
issue_type: visual_editorial_integration
severity: none
affected_pages: ["books/moduli/m-fc05-authority-indipendenti/chapters/01-authority-viste-dal-candidato.md", "books/moduli/m-fc05-authority-indipendenti/chapters/02-indipendenza-governance-accountability-personale.md", "books/moduli/m-fc05-authority-indipendenti/chapters/03-regolazione-europea-multilivello-reti-autorita.md", "books/moduli/m-fc05-authority-indipendenti/chapters/04-ciclo-regolatorio-consultazione-air-vir.md", "books/moduli/m-fc05-authority-indipendenti/chapters/05-vigilanza-istruttoria-ispezioni-dati-prova.md", "books/moduli/m-fc05-authority-indipendenti/chapters/06-sanzioni-impegni-rimedi-controllo-giurisdizionale.md", "books/moduli/m-fc05-authority-indipendenti/chapters/07-economia-industriale-regolazione-econometria-contabilita.md", "books/moduli/m-fc05-authority-indipendenti/chapters/08-agcm-concorrenza-consumatore-pratiche-scorrette.md", "books/moduli/m-fc05-authority-indipendenti/chapters/09-arera-energia-gas-acqua-rifiuti-tariffe.md", "books/moduli/m-fc05-authority-indipendenti/chapters/10-agcom-comunicazioni-media-utenti-piattaforme.md", "books/moduli/m-fc05-authority-indipendenti/chapters/11-consob-mercati-intermediari-tutela-investitore.md", "books/moduli/m-fc05-authority-indipendenti/chapters/12-banca-italia-ivass-vigilanza-prudenziale.md", "books/moduli/m-fc05-authority-indipendenti/chapters/13-garante-privacy-poteri-procedimenti-cooperazione.md", "books/moduli/m-fc05-authority-indipendenti/chapters/14-anac-prevenzione-vigilanza-whistleblowing.md", "books/moduli/m-fc05-authority-indipendenti/chapters/15-laboratorio-prove-authority.md"]
---

# Audit integrazione visiva M-FC05

## Esito

L'integrazione è completata per i quindici capitoli del modulo M-FC05. Alla verifica iniziale non erano presenti infografiche nel modulo: non sono stati quindi sostituiti asset esistenti. Sono stati creati e inseriti cinque visual didattici per ciascun capitolo.

## Copertura

| Verifica | Esito |
|---|---|
| Capitoli coperti | 15 su 15 |
| Master vettoriali | 75 SVG |
| Asset inseriti nel Markdown | 75 PNG |
| Didascalie e alt text | presenti per ogni figura |
| Cartelle asset e README | 15 su 15 |
| Coerenza grafica | conforme a Il Metodo BANDO e M-FC02 |

## Criteri applicati

- tavole orizzontali 1600 × 1000 px con fondo Off-White, card a contrasto e margini di sicurezza;
- palette Navy, Bordeaux, Muted Gold, Green e Teal; Arial per il testo interno;
- cinque funzioni ricorrenti: Mappa BANDO, architettura concettuale, sequenza, distinzioni, sintesi operativa;
- collocazione fra i blocchi esplicativi e prima degli snodi di prova o di esercitazione;
- esclusione di fotografie e grafica decorativa.

## Verifiche effettuate

1. Controllo automatico: ogni capitolo dichiara cinque `asset_refs`, contiene cinque immagini PNG e possiede i cinque master SVG corrispondenti.
2. Controllo di integrità: file non vuoti, percorsi relativi coerenti e nessun errore di whitespace nel diff.
3. Campionamento visivo: Capitoli 2, 4, 9 e 15 verificati a risoluzione originale; card, titoli, frecce e testo rientrano nella gabbia e non presentano sovrapposizioni.
4. Controllo parser Book Studio: il Capitolo 1 è esposto con cinque blocchi immagine e dieci asset nel catalogo del modulo.

## Nota di review

Le immagini sono strumenti di studio e non sostituiscono le verifiche normative già richieste dal modulo. Una futura esportazione tipografica dovrà comunque includere il controllo finale di riflusso sul PDF di stampa.
