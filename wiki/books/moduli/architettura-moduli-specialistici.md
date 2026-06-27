---
id: architettura-moduli-specialistici
type: module_architecture
title: "Architettura moduli specialistici Metodo BANDO"
status: canonical
domain: "concorsi pubblici italiani"
topics: ["moduli specialistici","famiglie concorsuali","metodo bando","capitale personale"]
entities: ["Metodo BANDO","Capitale Personale"]
source_refs: ["sources/metodo-bando-progetto-editoriale.md","sources/struttura-madre-il-metodo-bando.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.82
updated_at: 2026-06-27T19:56:28+02:00
created_at: 2026-06-27T19:56:28+02:00
review_required: true
canonical: true
tags: ["book-architecture","specialist-modules","metodo-bando"]
module_families: 6
module_count: 25
---

# Architettura moduli specialistici Metodo BANDO

## Decisione
Il prodotto Metodo BANDO usa tre livelli:

1. Libro principale autonomo: metodo, materie comuni, prove, adattamento ai profili e kit finale.
2. Ricettario operativo digitale: i capitoli 25-47 gia scritti, riclassificati come protocolli, casi, schede, checklist e laboratori.
3. Moduli specialistici: percorsi separati per famiglia concorsuale, selezionabili come libri di lavoro nella dashboard.

## Normalizzazione della nuova architettura
Il file esterno "NUOVA ARCHITETTURA PROGETTO LIBRO.txt" contiene etichette numeriche non coerenti tra loro: parla di "5 Famiglie x 23 Moduli" e in altri punti di 27 moduli. La tabella effettiva fornita elenca 6 famiglie e 25 moduli. Questa nota rende canonica la tabella effettiva: 6 famiglie, 25 moduli.

## Famiglie canoniche
- Funzioni Centrali: M-FC01, M-FC02, M-FC03, M-FC04, M-FC05
- Funzioni Locali: M-FL01, M-FL02, M-FL03, M-FL04
- Istruzione e Ricerca: M-IR01, M-IR02, M-IR03, M-IR04
- Sanita: M-SA01, M-SA02, M-SA03, M-SA04
- Trasversali: M-TR01, M-TR02, M-TR03, M-TR04
- Carriere Speciali: M-SP01, M-SP02, M-SP03, M-SP04

## Regole editoriali
- Ogni modulo vive in wiki/books/moduli/<module-id>/.
- Ogni modulo ha un index.md e almeno un capitolo in chapters/.
- Il book_id dei capitoli coincide con lo slug della cartella modulo.
- I moduli sono compagni del libro principale: non duplicano il nucleo comune, ma lo applicano a profili, prove e materie specialistiche.
- Le carriere speciali e i moduli sanitari richiedono source notes settoriali e review umana prima della pubblicazione.
- La promessa corretta e': riusabile, aggiornabile, modulare. Evitare formule come copertura totale garantita o aggiornamento normativo automatico.

## Roadmap
- Fase 1 MVP: M-FL01, M-IR01, M-FC03, M-SA02.
- Fase 2 espansione commerciale: M-FC01, M-FC02, M-FL04, M-SA01, M-TR01, M-TR02.
- Fase 3 profondita settoriale: M-FC04, M-FL02, M-FL03, M-IR02, M-IR03, M-IR04, M-SA03, M-SA04.
- Fase 4 premium/speciali: M-FC05, M-TR03, M-TR04, M-SP01, M-SP02, M-SP03, M-SP04.

## Catalogo moduli
| Famiglia | Codice | Modulo | Fase | Stato |
| --- | --- | --- | --- | --- |
| Funzioni Centrali | M-FC01 | [[books/moduli/m-fc01-ministeri/index|Ministeri e Presidenza del Consiglio]] | 2 | scaffold |
| Funzioni Centrali | M-FC02 | [[books/moduli/m-fc02-agenzie-fiscali/index|Agenzie fiscali]] | 2 | scaffold |
| Funzioni Centrali | M-FC03 | [[books/moduli/m-fc03-enti-non-economici/index|Enti pubblici non economici]] | 1 | scaffold |
| Funzioni Centrali | M-FC04 | [[books/moduli/m-fc04-giustizia/index|Giustizia]] | 3 | scaffold |
| Funzioni Centrali | M-FC05 | [[books/moduli/m-fc05-authority-indipendenti/index|Authority indipendenti]] | 4 | scaffold |
| Funzioni Locali | M-FL01 | [[books/moduli/m-fl01-comuni-unioni/index|Comuni e Unioni]] | 1 | scaffold |
| Funzioni Locali | M-FL02 | [[books/moduli/m-fl02-regioni-province-citta-metropolitane/index|Regioni, Province e Citta Metropolitane]] | 3 | scaffold |
| Funzioni Locali | M-FL03 | [[books/moduli/m-fl03-camere-commercio/index|Camere di Commercio]] | 3 | scaffold |
| Funzioni Locali | M-FL04 | [[books/moduli/m-fl04-polizia-locale/index|Polizia locale]] | 2 | scaffold |
| Istruzione e Ricerca | M-IR01 | [[books/moduli/m-ir01-scuola/index|Scuola]] | 1 | scaffold |
| Istruzione e Ricerca | M-IR02 | [[books/moduli/m-ir02-universita-afam/index|Universita e AFAM]] | 3 | scaffold |
| Istruzione e Ricerca | M-IR03 | [[books/moduli/m-ir03-enti-ricerca/index|Enti di ricerca]] | 3 | scaffold |
| Istruzione e Ricerca | M-IR04 | [[books/moduli/m-ir04-cultura-beni-culturali/index|Cultura e beni culturali]] | 3 | scaffold |
| Sanita | M-SA01 | [[books/moduli/m-sa01-sanita-amministrativa/index|Sanita amministrativa]] | 2 | scaffold |
| Sanita | M-SA02 | [[books/moduli/m-sa02-professioni-sanitarie/index|Professioni sanitarie]] | 1 | scaffold |
| Sanita | M-SA03 | [[books/moduli/m-sa03-dirigenza-medica-sanitaria/index|Dirigenza medica e sanitaria]] | 3 | scaffold |
| Sanita | M-SA04 | [[books/moduli/m-sa04-tecnici-sanitari-prevenzione/index|Tecnici sanitari e prevenzione]] | 3 | scaffold |
| Trasversali | M-TR01 | [[books/moduli/m-tr01-ict-trasformazione-digitale/index|ICT e trasformazione digitale]] | 2 | scaffold |
| Trasversali | M-TR02 | [[books/moduli/m-tr02-appalti-pnrr-fondi-ue/index|Appalti, PNRR e fondi UE]] | 2 | scaffold |
| Trasversali | M-TR03 | [[books/moduli/m-tr03-tecnico-ingegneristico/index|Tecnico-ingegneristico]] | 4 | scaffold |
| Trasversali | M-TR04 | [[books/moduli/m-tr04-ambiente-protezione-civile/index|Ambiente e protezione civile]] | 4 | scaffold |
| Carriere Speciali | M-SP01 | [[books/moduli/m-sp01-forze-ordine/index|Polizia, Carabinieri e Guardia di Finanza]] | 4 | scaffold |
| Carriere Speciali | M-SP02 | [[books/moduli/m-sp02-vigili-fuoco/index|Vigili del Fuoco]] | 4 | scaffold |
| Carriere Speciali | M-SP03 | [[books/moduli/m-sp03-magistratura-avvocatura-notariato/index|Magistratura, Avvocatura e Notariato]] | 4 | scaffold |
| Carriere Speciali | M-SP04 | [[books/moduli/m-sp04-prefettizia-diplomatica/index|Prefettizia e diplomatica]] | 4 | scaffold |

## Modalita di scrittura
La scrittura parte dal piano editoriale del modulo. Prima di generare testo finale occorre consolidare le fonti specifiche in sources/, collegarle a topic/entity pages e poi usare Manual Writer Agent sul capitolo del modulo selezionato in dashboard.
