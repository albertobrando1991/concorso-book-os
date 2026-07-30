---
id: review-vol-07-pipeline-03-riconciliazione-catalogo
type: review
title: "VOL-07 - Riconciliazione del catalogo e dei perimetri"
status: complete
domain: "concorsi pubblici italiani"
topics: ["catalogo volumi", "moduli specialistici", "copertura v4"]
entities: ["Metodo BANDO", "ConcorsoBook OS"]
source_refs: ["sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["vol-07-sanita-amministrativa-professioni-sanitarie"]
confidence: 0.98
updated_at: 2026-07-28T19:10:00+02:00
created_at: 2026-07-28T19:10:00+02:00
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-07", "catalog-reconciliation"]
issue_type: catalog_reconciliation
severity: low
affected_pages: []
---

# VOL-07 - Riconciliazione del catalogo e dei perimetri

## Diagnosi

Il catalogo applicativo, l'architettura wiki e le 25 directory modulari coincidono. Il test del catalogo passa con 12 volumi e 25 codici modulo univoci; l'audit aggiuntivo non rileva directory mancanti, duplicati, `module_code` incoerenti o `book_id` difformi dallo slug.

## Mappa definitiva

| Volume | Moduli | Book ID |
| --- | --- | --- |
| VOL-01 | B-PA01/B-PA11 + ricettario | `il-metodo-bando` |
| VOL-02 | M-FL01, M-FL02, M-FL03, M-FL04 | `moduli/m-fl01-comuni-unioni`; `moduli/m-fl02-regioni-province-citta-metropolitane`; `moduli/m-fl03-camere-commercio`; `moduli/m-fl04-polizia-locale` |
| VOL-03 | M-FC01, M-FC02, M-FC03 | `moduli/m-fc01-ministeri`; `moduli/m-fc02-agenzie-fiscali`; `moduli/m-fc03-enti-non-economici` |
| VOL-04 | M-FC04 | `moduli/m-fc04-giustizia` |
| VOL-05 | M-FC05 | `moduli/m-fc05-authority-indipendenti` |
| VOL-06 | M-IR01, M-IR02, M-IR03, M-IR04 | `moduli/m-ir01-scuola`; `moduli/m-ir02-universita-afam`; `moduli/m-ir03-enti-ricerca`; `moduli/m-ir04-cultura-beni-culturali` |
| VOL-07 | M-SA01, M-SA02, M-SA03, M-SA04 | `moduli/m-sa01-sanita-amministrativa`; `moduli/m-sa02-professioni-sanitarie`; `moduli/m-sa03-dirigenza-medica-sanitaria`; `moduli/m-sa04-tecnici-sanitari-prevenzione` |
| VOL-08 | M-TR01 | `moduli/m-tr01-ict-trasformazione-digitale` |
| VOL-09 | M-TR02 | `moduli/m-tr02-appalti-pnrr-fondi-ue` |
| VOL-10 | M-TR03 | `moduli/m-tr03-tecnico-ingegneristico` |
| VOL-11 | M-TR04 | `moduli/m-tr04-ambiente-protezione-civile` |
| VOL-12 | M-SP01, M-SP02, M-SP03, M-SP04 | `moduli/m-sp01-forze-ordine`; `moduli/m-sp02-vigili-fuoco`; `moduli/m-sp03-magistratura-avvocatura-notariato`; `moduli/m-sp04-prefettizia-diplomatica` |

## Applicazione della copertura v4 a VOL-07

- Comune: diritto amministrativo, impiego pubblico, contabilità generale, contratti generali, privacy generale, CAD e competenze trasversali restano nel VOL-01.
- Famiglia sanitaria: organizzazione SSN, aziende, LEA, documentazione sanitaria, responsabilità, professioni, dirigenza, laboratorio e tecnologie restano nel VOL-07.
- Sottoprofili: infermiere, dirigenza per disciplina, TSLB e TSRM sono verticali o appendici soltanto quando la specializzazione è reale.
- Cross-family: procurement generale rinvia a VOL-09 e componenti ICT avanzate a VOL-08; il VOL-07 conserva il delta sanitario.

## Discrepanze

Nessuna discrepanza di catalogo bloccante. Le incoerenze fra stato dichiarato e contenuto effettivo di alcuni moduli storici, rilevate nello step 01, sono problemi editoriali e non di assegnazione al catalogo.

## Patch applicate

Nessuna patch al catalogo: una modifica senza discrepanza sarebbe arbitraria.

## Decisioni umane residue

- Definire l'estensione commerciale finale dei cinque verticali sanitari.
- Rendere puntuali i rinvii dal VOL-07 al VOL-01, VOL-08 e VOL-09 in fase B.
- Confermare, dopo l'audit dei bandi, se OSS richieda un verticale autonomo o soltanto un percorso distinto.

## Verifica

- `tests/text-volumes.test.ts`: 3 test superati.
- Audit filesystem/frontmatter: 12 volumi, 25 moduli, 0 issue.
