---
id: pipeline-vol-12-03-riconciliazione-catalogo
type: pipeline_review
title: "VOL-12 — Step 03: riconciliazione del catalogo"
volume_code: VOL-12
step: "03"
phase: A
scope: catalog
domain: "concorsi pubblici italiani"
updated_at: 2026-08-11T00:00:00+02:00
review_required: true
canonical: true
tags: ["pipeline", "vol-12", "step-03", "catalogo"]
---

# VOL-12 — Step 03: riconciliazione del catalogo

## Numeri canonici — verificati

| Grandezza | Atteso | Rilevato | Esito |
| --- | ---: | ---: | --- |
| Volumi commerciali in `TEXT_VOLUME_CATALOG` | 12 | 12 | ✅ |
| Moduli distinti (`TEXT_CATALOG_MODULE_COUNT`) | 25 | 25 | ✅ |
| Cartelle reali in `wiki/books/moduli/m-*` | 25 | 25 | ✅ |
| Righe modulo nella tabella di architettura | 25 | 25 | ✅ |

## Mappa definitiva Volume → moduli → book_id

| Volume | Tier | Moduli | book_id dei moduli | Libro di orientamento |
| --- | --- | --- | --- | --- |
| VOL-01 | base | — | `il-metodo-bando` | — |
| VOL-02 | standard | M-FL01…M-FL04 | `moduli/m-fl01-comuni-unioni`, `moduli/m-fl02-regioni-province-citta-metropolitane`, `moduli/m-fl03-camere-commercio`, `moduli/m-fl04-polizia-locale` | `vol-02-enti-locali-polizia-locale` |
| VOL-03 | standard | M-FC01, M-FC02, M-FC03 | `moduli/m-fc01-ministeri`, `moduli/m-fc02-agenzie-fiscali`, `moduli/m-fc03-enti-non-economici` | — |
| VOL-04 | standard | M-FC04 | `moduli/m-fc04-giustizia` | — *(vedi D2)* |
| VOL-05 | premium | M-FC05 | `moduli/m-fc05-authority-indipendenti` | — *(vedi D2)* |
| VOL-06 | standard | M-IR01…M-IR04 | `moduli/m-ir01-scuola`, `moduli/m-ir02-universita-afam`, `moduli/m-ir03-enti-ricerca`, `moduli/m-ir04-cultura-beni-culturali` | — |
| VOL-07 | vertical | M-SA01…M-SA04 | `moduli/m-sa01-…`, `m-sa02-…`, `m-sa03-…`, `m-sa04-…` | — |
| VOL-08 | vertical | M-TR01 | `moduli/m-tr01-ict-trasformazione-digitale` | — |
| VOL-09 | vertical | M-TR02 | `moduli/m-tr02-appalti-pnrr-fondi-ue` | — |
| VOL-10 | vertical | M-TR03 | `moduli/m-tr03-tecnico-ingegneristico` | — |
| VOL-11 | vertical | M-TR04 | `moduli/m-tr04-ambiente-protezione-civile` | — |
| **VOL-12** | **premium** | **M-SP01…M-SP04** | `moduli/m-sp01-forze-ordine`, `moduli/m-sp02-vigili-fuoco`, `moduli/m-sp03-magistratura-avvocatura-notariato`, `moduli/m-sp04-prefettizia-diplomatica` | — |

Ogni `bookId` dichiarato nel catalogo corrisponde a una cartella esistente. Nessun modulo è orfano, duplicato, mancante o assegnato al volume sbagliato.

## Coerenza dei frontmatter

Verificati `book_id`, `module_code` e `module_family` su tutti e 25 gli `index.md` dei moduli:

- `book_id` coincide con il nome della cartella in **25 casi su 25**;
- `module_code` segue lo schema `M-XXNN` senza salti né duplicati;
- `module_family` è coerente con il prefisso del codice in **25 casi su 25** (`funzioni-centrali`, `funzioni-locali`, `istruzione-ricerca`, `sanita`, `carriere-speciali`, `trasversali`).

**Nessuna discrepanza.**

## Discrepanze rilevate

### D1 — Due convenzioni diverse per i volumi aggregatori 🟠

I volumi aggregatori esistono in due posizioni incompatibili:

| Percorso | Volumi | `type` dichiarato |
| --- | --- | --- |
| `wiki/books/volumi/<slug>/` | VOL-03, VOL-07, **VOL-12** | `volume` |
| `wiki/books/<slug>/` | VOL-04, VOL-05 | `commercial_volume`, `book` |

Tre oggetti che rappresentano la stessa cosa hanno tre valori di `type` diversi: `volume`, `commercial_volume`, `book`. VOL-12 è stato creato nella posizione e con il `type` della convenzione più recente e più popolata (`volumi/`, `type: volume`), coerente con VOL-03 e VOL-07.

**Non applico la migrazione di VOL-04 e VOL-05**: spostare due cartelle rompe i wikilink in ingresso e riguarda volumi fuori dal perimetro di questa pipeline.

### D2 — Tre libri non referenziati dal catalogo 🟡

| Libro | `type` | `status` | Capitoli | Valutazione |
| --- | --- | --- | ---: | --- |
| `vol-04-giustizia-upp` | `commercial_volume` | `drafting` | 0 | non orfano in senso proprio: è l'aggregatore di VOL-04, non ancora agganciato via `orientationBookId` |
| `vol-05-authority-regolazione` | `book` | `source_ready` | 0 | idem per VOL-05 |
| `manuale-concorso-funzionari-enti-locali` | `book` | `draft` | 2 (521 parole) | **residuo storico**: non corrisponde ad alcun volume del catalogo v4 |

Il campo `orientationBookId` è stato introdotto da lavoro in corso non committato e per ora valorizza solo VOL-02. VOL-04 e VOL-05 hanno l'aggregatore ma non l'aggancio: è un completamento naturale di quel lavoro, **non una correzione di competenza di questa pipeline**.

`manuale-concorso-funzionari-enti-locali` contiene 2 capitoli per 521 parole complessive ed è l'unico oggetto realmente estraneo alla mappa v4.

### D3 — M-FC01 con 13 capitoli su 15 allo stato di stub 🟠

Già rilevato allo step 01. Rilevante qui perché il modulo è dichiarato nel catalogo sotto VOL-03 come modulo a pieno titolo, mentre contiene 8.855 parole totali contro le 67.000-80.000 dei moduli comparabili. Qualsiasi metrica di copertura che conti i file invece delle parole classifica VOL-03 come più avanzato di quanto sia.

Fuori perimetro VOL-12. **Segnalato allo staff VOL-03.**

## Applicazione della logica di copertura v4 a VOL-12

| Livello | Collocazione decisa | Verifica |
| --- | --- | --- |
| Contenuti comuni (metodo, diritto amministrativo, competenze generali) | VOL-01 | ✅ nessuna duplicazione prevista nei moduli M-SP |
| Contenuti di famiglia (carriere speciali) | moduli M-SP01…M-SP04 | ✅ |
| Sottoprofili non omogenei | binari interni al modulo, non moduli nuovi | ✅ M-SP03 a tre binari, M-SP04 a due |
| Altre famiglie | rinvio preciso | ✅ polizia locale → M-FL04; funzionari MinInterno/MAECI → famiglia funzioni centrali |

Il perimetro negativo del volume è dichiarato in `wiki/books/volumi/vol-12-carriere-speciali-premium/index.md` e nei quattro `index.md` di modulo: Forze armate, polizia locale, abilitazione forense, magistratura onoraria, contabile e amministrativa per vie diverse dal concorso ordinario, dirigenza pubblica generale.

## Patch applicate in questo step

Nessuna. Le due correzioni di catalogo pertinenti a VOL-12 — `audience` della voce VOL-12 e `description` della regola `premium` — erano già state applicate e sono documentate nel verbale dello step 02.

Le discrepanze D1, D2 e D3 **non sono non ambigue** ai sensi del prompt: riguardano volumi fuori perimetro e intersecano lavoro non committato di altri flussi. Diagnosticate, non patchate.

## Decisioni che richiedono approvazione umana

1. **D1** — unificare la collocazione e il `type` dei volumi aggregatori: migrare VOL-04 e VOL-05 sotto `wiki/books/volumi/` con `type: volume`, oppure formalizzare le due convenzioni come distinte e documentarle.
2. **D2** — agganciare `vol-04-giustizia-upp` e `vol-05-authority-regolazione` come `orientationBookId` di VOL-04 e VOL-05, coordinandosi con il flusso che ha introdotto il campo.
3. **D2** — decidere la sorte di `manuale-concorso-funzionari-enti-locali`: archiviarlo, assorbirne i 2 capitoli in un modulo esistente, o dichiararlo esplicitamente fuori catalogo.
4. **D3** — pianificare il completamento o la ridichiarazione dei 13 stub di M-FC01.

Nessuna di queste decisioni blocca la prosecuzione di VOL-12.

## Esito

Catalogo **coerente** sul perimetro VOL-12. Nessun blocker. Si procede allo step 04.
