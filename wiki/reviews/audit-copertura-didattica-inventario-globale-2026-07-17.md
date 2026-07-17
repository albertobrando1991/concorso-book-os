---
id: review-audit-copertura-didattica-inventario-globale-2026-07-17
type: review
title: "Inventario globale della copertura didattica - 12 volumi e 25 moduli"
status: completed
domain: "concorsi pubblici italiani"
topics: ["copertura didattica integrale", "catalogo editoriale", "moduli specialistici"]
entities: ["Metodo BANDO", "ConcorsoBook OS"]
source_refs: ["sources/principio-copertura-didattica-integrale-2026-07-17.md", "sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["books/moduli/architettura-moduli-specialistici.md"]
confidence: 0.96
updated_at: 2026-07-17T00:00:00+02:00
created_at: 2026-07-17T00:00:00+02:00
review_required: true
canonical: false
tags: ["review", "inventory", "didactic-coverage"]
issue_type: structural-inventory
severity: critical
affected_pages: ["books/volumi", "books/moduli", "books/il-metodo-bando"]
---

# Inventario globale della copertura didattica

## Perimetro e metodo

Questo documento censisce lo stato reale su disco dei **12 volumi** commerciali e dei **25 moduli** canonici al 17 luglio 2026. E' un inventario strutturale, **non un audit semantico**: parole, file, frontmatter e fonti dichiarate non dimostrano che i concetti siano spiegati in modo completo. In particolare, file esistente non equivale a copertura completa e `source_ready` non equivale a contenuto pubblicabile.

La working tree era sporca durante il censimento. Sono stati letti anche file modificati o non tracciati presenti su disco, senza modificarli; i conteggi sono quindi una fotografia operativa, non necessariamente dello stato dell'ultimo commit. Non sono state lette fonti `raw/` e non sono state valutate accuratezza normativa, profondita teorica o mantenimento delle promesse formative.

Legenda: **assenza filesystem** = nessuna cartella/index dedicata; **scaffold** = index e piano, senza capitoli sostanziali; **source-ready** = fonti dichiarate e struttura pronta, non testo finale; **draft/revised** = capitoli presenti in lavorazione; **aggregatore commerciale** = record che compone moduli; **pubblicabile** = stato concedibile solo dopo audit semantico e review, qui mai assegnato.

## Catalogo dei volumi commerciali

Le parole sono conteggi indicativi su token non vuoti nei capitoli propri. I riferimenti sono source ref distinti dichiarati nei capitoli; i riferimenti dell'index sono indicati separatamente. Per "matrice" si intende esclusivamente una matrice didattica dedicata conforme al nuovo gate. Tabelle o matrici editoriali preesistenti sono censite come strumenti da riallineare, non come matrici conformi.

| ID | Titolo/famiglia e moduli | Cartella/index | Capitoli propri | Stati capitoli | Parole | Placeholder/source-ready | Source refs | Matrice | Classificazione strutturale |
| --- | --- | --- | ---: | --- | ---: | --- | ---: | --- | --- |
| VOL-01 | Manuale base PA; B-PA01/B-PA11 + ricettario | `books/il-metodo-bando/index.md` presente | 54 | revised_draft 53; professional_draft 1 | 191.026 | draft/revised | 129 | assente | contenuto esteso, non pubblicabilita verificata |
| VOL-02 | Enti locali, Camere di commercio e Polizia locale; M-FL01/04 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; moduli scaffold |
| VOL-03 | Funzioni centrali, Fisco, Previdenza e Ispettivo; M-FC01/03 | cartella/index presente | 1 | revised_draft 1 | 3.607 | source-ready + draft | 6 nei capitoli (2 dichiarati nell'index) | assente | aggregatore con contenuto proprio iniziale |
| VOL-04 | Giustizia e UPP; M-FC04 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; modulo scaffold |
| VOL-05 | Authority e regolazione; M-FC05 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; modulo scaffold |
| VOL-06 | Scuola, Universita, Ricerca, Cultura; M-IR01/04 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; moduli scaffold |
| VOL-07 | Sanita amministrativa e professioni sanitarie; M-SA01/04 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; moduli scaffold |
| VOL-08 | ICT, digitale, cybersecurity e dati; M-TR01 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; modulo scaffold |
| VOL-09 | Appalti, PNRR e procurement; M-TR02 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; modulo scaffold |
| VOL-10 | Tecnico-ingegneristico, territorio, lavori pubblici; M-TR03 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; modulo scaffold |
| VOL-11 | Ambiente, protezione civile e sostenibilita; M-TR04 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; modulo scaffold |
| VOL-12 | Carriere speciali premium; M-SP01/04 | cartella/index volume assente | 0 | - | 0 | aggregatore | 0 | assente | aggregatore commerciale; moduli scaffold |

Un aggregatore senza capitoli propri non e' automaticamente mancante quando identifica i moduli aggregati. Resta pero un aggregatore, non una copertura verificata. Totale contenuto proprio dei volumi: 55 capitoli e circa 194.633 parole; il dato non include i capitoli dei moduli aggregati.

## Catalogo dei moduli canonici

`Refs` somma i riferimenti distinti dichiarati nei capitoli; tra parentesi sono indicati quelli dichiarati nell'index quando utili. Il capitolo `00-piano-editoriale.md` non e' contato come capitolo sostanziale.

| ID | Titolo/famiglia | Cartella/index | Cap. | Distribuzione stati | Parole | Stato strutturale | Refs | Matrice |
| --- | --- | --- | ---: | --- | ---: | --- | ---: | --- |
| M-FC01 | Ministeri e Presidenza del Consiglio - Funzioni Centrali | presente | 15 | structure 13; to_expand 1; revised_draft 1 | 8.902 | source-ready/draft | 28 (13 index) | assente |
| M-FC02 | Agenzie fiscali - Funzioni Centrali | presente | 14 | revised_draft 11; source_ready 2; draft 1 | 43.147 | source-ready/draft/revised | 27 (12 index) | assente |
| M-FC03 | Enti pubblici non economici - Funzioni Centrali | presente | 19 | revised_draft 18; structure 1 | 58.790 | source-ready/draft/revised | 10 (6 index) | no; matrice materie preesistente da riallineare |
| M-FC04 | Giustizia - Funzioni Centrali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-FC05 | Authority indipendenti - Funzioni Centrali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-FL01 | Comuni e Unioni - Funzioni Locali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-FL02 | Regioni, Province e Citta metropolitane - Funzioni Locali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-FL03 | Camere di commercio - Funzioni Locali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-FL04 | Polizia locale - Funzioni Locali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-IR01 | Scuola - Istruzione e Ricerca | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-IR02 | Universita e AFAM - Istruzione e Ricerca | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-IR03 | Enti di ricerca - Istruzione e Ricerca | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-IR04 | Cultura e beni culturali - Istruzione e Ricerca | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SA01 | Sanita amministrativa - Sanita | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SA02 | Professioni sanitarie - Sanita | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SA03 | Dirigenza medica e sanitaria - Sanita | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SA04 | Tecnici sanitari e prevenzione - Sanita | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-TR01 | ICT e trasformazione digitale - Trasversali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-TR02 | Appalti, PNRR e fondi UE - Trasversali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-TR03 | Tecnico-ingegneristico - Trasversali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-TR04 | Ambiente e protezione civile - Trasversali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SP01 | Polizia, Carabinieri e Guardia di Finanza - Carriere Speciali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SP02 | Vigili del Fuoco - Carriere Speciali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SP03 | Magistratura, Avvocatura e Notariato - Carriere Speciali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |
| M-SP04 | Prefettizia e diplomatica - Carriere Speciali | presente | 0 | - | 0 | scaffold | 0 (2 index) | assente |

Totale moduli: 25/25 cartelle e index presenti; 48 capitoli sostanziali; circa 110.839 parole. Distribuzione strutturale: 3 moduli source-ready con capitoli in lavorazione e 22 scaffold senza capitoli sostanziali. Matrici didattiche dedicate conformi al nuovo gate: 0. L'Appendice F di VOL-01 e la matrice materie di M-FC03 sono strumenti preesistenti da classificare e riallineare; non provano conformita al nuovo schema.

## Blocker e priorita

1. **P0 - matrici:** manca una matrice didattica dedicata conforme per tutti gli elementi; l'Appendice F di VOL-01 e la matrice materie di M-FC03 vanno riallineate al nuovo template.
2. **P0 - audit semantico:** nessun volume o modulo puo essere dichiarato pubblicabile sulla base di questo inventario.
3. **P1 - scaffold:** 22 moduli hanno index e piano ma zero capitoli sostanziali.
4. **P1 - aggregatori:** dieci volumi non hanno cartella/index dedicata; la relazione commerciale e' documentata soltanto nell'architettura canonica.
5. **P1 - stati:** M-FC01 contiene 13 capitoli `structure`; M-FC02 conserva due `source_ready` e un `draft`; M-FC03 conserva un `structure`.
6. **P2 - tracciabilita:** VOL-03 dichiara 6 source refs nel capitolo proprio e 2 nell'index; completezza, qualita e rinvii ai moduli non sono stati verificati semanticamente.

## Conclusione

Il catalogo strutturale e' riconciliato a 12 volumi e 25 moduli. Questa riconciliazione non certifica copertura teorica, autonomia didattica o pubblicabilita. Il gate resta quello definito in [[sources/principio-copertura-didattica-integrale-2026-07-17]] e illustrato in [[topics/copertura-didattica-integrale]].
