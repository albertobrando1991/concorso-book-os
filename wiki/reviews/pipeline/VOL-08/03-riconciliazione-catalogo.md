---
id: review-vol-08-pipeline-03-riconciliazione-catalogo
type: review
title: "VOL-08 - Riconciliazione del catalogo"
status: complete
domain: "concorsi pubblici italiani"
topics: ["catalogo editoriale", "moduli specialistici", "copertura v4"]
entities: ["ConcorsoBook OS", "Metodo BANDO"]
source_refs: ["sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.99
updated_at: 2026-08-05T19:50:00+02:00
created_at: 2026-08-05T19:50:00+02:00
review_required: false
canonical: false
tags: ["review", "pipeline", "vol-08", "catalog-reconciliation"]
issue_type: catalog_reconciliation
severity: low
affected_pages: ["wiki/books/moduli/architettura-moduli-specialistici.md"]
---

# VOL-08 - Riconciliazione del catalogo

## Diagnosi

Il confronto tra `src/catalog/text-volumes.ts`, l'architettura canonica, le cartelle reali e i frontmatter conferma 12 volumi commerciali e 25 moduli specialistici univoci. Non risultano moduli orfani, duplicati, mancanti o assegnati al volume sbagliato. La cartella `_template-modulo` è uno strumento editoriale e non fa parte del catalogo.

Tutti i capitoli presenti dichiarano un `book_id` coincidente con lo slug della cartella. `module_code`, `module_family` e `companion_to` sono completi e coerenti negli indici dei 25 moduli. In 33 capitoli di M-SA02, M-SA04, M-TR01 e M-TR03 uno o entrambi i campi `module_code` e `module_family` non sono ripetuti: non è una collisione di catalogo, perché il frontmatter standard richiede il `book_id` e i metadati di modulo sono canonici nell'indice. Un'eventuale duplicazione obbligatoria di questi campi richiede una decisione di schema separata.

## Mappa definitiva Volume -> moduli -> book_id

| Volume | Moduli | book_id |
| --- | --- | --- |
| VOL-01 | nucleo B-PA01/B-PA11 | `il-metodo-bando` |
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

## Verifica della copertura v4

La collocazione rispetta le sei famiglie canoniche. VOL-01 resta il contenitore del nucleo comune; M-TR01 appartiene correttamente a VOL-08 per ICT, digitale, cybersecurity e dati. M-FL03 resta in VOL-02 e M-FC01 in VOL-03 come eccezioni già riconciliate dalla fonte v4. Sottoprofili e contenuti cross-family non generano nuovi moduli di catalogo: richiedono appendice o rinvio preciso.

## Discrepanze rilevate

| Discrepanza | Esito |
| --- | --- |
| Stato M-TR01 nella tabella architetturale ancora `scaffold` | Correzione non ambigua: indice e pipeline attestano `text_frozen` |
| 33 capitoli senza ripetizione completa di `module_code`/`module_family` | Non bloccante; nessun valore errato e `book_id` sempre coerente |
| Stati di avanzamento degli altri moduli potenzialmente più recenti della tabella | Fuori dal perimetro VOL-08; da sincronizzare dai rispettivi run-state, non dedurre dal numero di file |

## Patch applicate

| File | Patch |
| --- | --- |
| `wiki/books/moduli/architettura-moduli-specialistici.md` | Stato M-TR01 aggiornato da `scaffold` a `text_frozen` |

## Decisioni che richiedono approvazione umana

- Stabilire se `module_code` e `module_family` debbano diventare campi obbligatori anche in ogni capitolo, oltre che nell'indice di modulo.
- Stabilire se lo stato nella tabella architetturale debba essere sincronizzato automaticamente dal run-state della pipeline per evitare futuri disallineamenti.

Non sono state modificate assegnazioni commerciali, famiglie, slug o `book_id`.
