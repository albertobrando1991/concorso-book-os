---
id: architettura-moduli-specialistici
type: module_architecture
title: "Architettura moduli specialistici Metodo BANDO"
status: canonical
domain: "concorsi pubblici italiani"
topics: ["moduli specialistici","famiglie concorsuali","metodo bando","capitale personale"]
entities: ["Metodo BANDO","Capitale Personale"]
source_refs: ["sources/metodo-bando-progetto-editoriale.md","sources/struttura-madre-il-metodo-bando.md","sources/idea-business-vendita-libri-capitale-personale-2026-07-03.md","sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.82
updated_at: 2026-07-14T00:00:00+02:00
created_at: 2026-06-27T19:56:28+02:00
review_required: true
canonical: true
tags: ["book-architecture","specialist-modules","metodo-bando"]
module_families: 6
module_count: 25
commercial_volumes: 12
---

# Architettura moduli specialistici Metodo BANDO

## Decisione
Il prodotto Metodo BANDO usa tre livelli:

1. Libro principale autonomo: metodo, materie comuni, prove, adattamento ai profili e kit finale.
2. Ricettario operativo digitale: i capitoli 25-47 gia scritti, riclassificati come protocolli, casi, schede, checklist e laboratori.
3. Moduli specialistici: percorsi separati per famiglia concorsuale, selezionabili come libri di lavoro nella dashboard.

## Normalizzazione della nuova architettura
Il file esterno "NUOVA ARCHITETTURA PROGETTO LIBRO.txt" contiene etichette numeriche non coerenti tra loro: parla di "5 Famiglie x 23 Moduli" e in altri punti di 27 moduli. La tabella effettiva fornita elenca 6 famiglie e 25 moduli. Questa nota rende canonica la tabella effettiva: 6 famiglie, 25 moduli.

## Aggiornamento commerciale 2026-07-03
Il documento strategico [[sources/idea-business-vendita-libri-capitale-personale-2026-07-03|Idea di business e vendita libri Capitale Personale - aggiornamento catalogo 12 volumi]] conferma la tassonomia a 25 moduli, ma cambia il modo in cui la dashboard e la vendita devono presentarli: non una lista piatta di moduli, ma 12 volumi editoriali riconoscibili dal cliente.

La gerarchia operativa diventa:

1. Volume base: `Il Metodo BANDO`, con nucleo comune B-PA01/B-PA11 e ricettario digitale collegato.
2. Volumi commerciali specialistici: 11 volumi che aggregano i 25 moduli per affinita editoriale e commerciale.
3. Verticali e appendici: innesti profondi per profili tecnici, sanitari, ispettivi, ICT/cyber, premium o ad alta barriera.

Nota di riconciliazione: nella descrizione dei 12 volumi il documento non cita esplicitamente M-FC01 e M-FL03, pur confermando 25 moduli. Per non lasciare moduli orfani, M-FC01 e' collocato in VOL-03 e M-FL03 in VOL-02.

## Regola madre di copertura v4 - vincolante
La fonte [[sources/logica-volumi-copertura-concorsobook-v4|Logica dei volumi e della copertura ConcorsoBook v4]] e' la base obbligatoria per sviluppo, catalogazione, vendita e revisione. La sua applicazione e' semplice: contenuto comune solo in `VOL-01`; contenuto di famiglia nel relativo specialistico; sottoprofilo in appendice/verticale soltanto se esiste una specializzazione reale; contenuto di altra famiglia con rinvio al volume corretto, mai duplicato.

`VOL-01` conserva esclusivamente il nucleo B-PA01/B-PA11. Ogni modulo dichiara quindi cosa applica di quel nucleo, cosa aggiunge per la famiglia, quali eventuali appendici richiede e quali materiali non sono necessari al candidato. Il Ricettario digitale ospita allenamento, casi, quiz, simulazioni, correzioni ed aggiornamenti: non e' una ragione per svuotare il libro base.

Per coerenza con la tassonomia a 25 moduli, M-FL03 resta in `VOL-02`. M-FC01 resta in `VOL-03`, ma non e' proponibile indistintamente: il percorso dipende dal profilo (amministrativo, tecnico, ICT o statistico-economico) e deve indirizzare verso `VOL-10`, `VOL-08` o un approfondimento mirato quando necessario.

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
- Prima di scrivere o revisionare un modulo compilare la scheda di copertura: famiglia, profilo, B-PA gia' coperti dal base, specialistico, sottoprofilo, rinvio ad altra famiglia, pacchetto minimo ed esclusioni.
- Un errore di famiglia, una duplicazione B-PA o una lacuna su una materia ricorrente/pesata del profilo e' un errore grave di architettura e blocca la pubblicazione.
- La dashboard deve mostrare i moduli dentro i 12 volumi commerciali, ma lo Studio e il Writer continuano a lavorare sul singolo book_id del modulo.
- Il pacchetto cliente standard e': libro base + 1 modulo di famiglia. I pacchetti verticali aggiungono un modulo/appendice profonda. I pacchetti premium richiedono pricing e review piu rigorosi.
- Le carriere speciali e i moduli sanitari richiedono source notes settoriali e review umana prima della pubblicazione.
- La promessa corretta e': riusabile, aggiornabile, modulare. Evitare formule come copertura totale garantita o aggiornamento normativo automatico.

## Catalogo commerciale 12 volumi
| Volume | Titolo operativo | Moduli | Pacchetto |
| --- | --- | --- | --- |
| VOL-01 | Manuale base PA | B-PA01/B-PA11 + ricettario digitale | Base |
| VOL-02 | Enti locali, Camere di commercio e Polizia locale | M-FL01, M-FL02, M-FL03, M-FL04 | Standard |
| VOL-03 | Funzioni centrali, Fisco, Previdenza e Ispettivo | M-FC01, M-FC02, M-FC03 | Standard |
| VOL-04 | Giustizia e UPP | M-FC04 | Standard |
| VOL-05 | Authority e regolazione | M-FC05 | Premium |
| VOL-06 | Scuola, Universita, Ricerca, Cultura | M-IR01, M-IR02, M-IR03, M-IR04 | Standard |
| VOL-07 | Sanita amministrativa e professioni sanitarie | M-SA01, M-SA02, M-SA03, M-SA04 | Verticale |
| VOL-08 | ICT, digitale, cybersecurity e dati | M-TR01 | Verticale |
| VOL-09 | Appalti, PNRR e procurement | M-TR02 | Verticale |
| VOL-10 | Tecnico-ingegneristico, territorio, lavori pubblici | M-TR03 | Verticale |
| VOL-11 | Ambiente, protezione civile e sostenibilita | M-TR04 | Verticale |
| VOL-12 | Carriere speciali premium | M-SP01, M-SP02, M-SP03, M-SP04 | Premium |

## Roadmap
- Prima ondata 3-6 mesi: libro base, ricettario digitale MVP, M-FL01, M-IR01, M-FC03, M-SA02, M-TR02.
- Seconda ondata 6-12 mesi: M-FC01, M-FC02, M-FL04, M-IR02, M-SA01, M-TR01, M-TR03.
- Terza ondata 12-18 mesi: M-FC05, M-FC04, M-FL02, M-FL03, M-IR03, M-IR04, M-SA03, M-SA04, M-TR04, M-SP01, M-SP02, M-SP03, M-SP04.
- Ondata continua: audit bandi verso 150+ fonti, obiettivo 5-6 bandi per cluster, aggiornamento normativo su piattaforma e revisione semestrale dei moduli.

## Protocollo obbligatorio per i prossimi passi
1. Per ogni modulo e volume commerciale aggiornare la scheda di copertura prevista dalla regola v4.
2. Confrontare ogni cluster prioritario con 5-6 bandi rappresentativi e registrare materie mancanti, rinvii e contenuti da aggiornare.
3. Sviluppare un capitolo solo dopo fonti consolidate, topic/entity pages e decisione di copertura.
4. Prima della pubblicazione eseguire il gate di copertura e poi il Revisore Editoriale Totale: checklist a 30 punti piu' controllo di non duplicazione, corretta famiglia, lacune e pacchetto minimo.

## Catalogo moduli
| Famiglia | Codice | Modulo | Fase | Stato |
| --- | --- | --- | --- | --- |
| Funzioni Centrali | M-FC01 | [[books/moduli/m-fc01-ministeri/index|Ministeri e Presidenza del Consiglio]] | 2 | scaffold |
| Funzioni Centrali | M-FC02 | [[books/moduli/m-fc02-agenzie-fiscali/index|Agenzie fiscali]] | 2 | source_ready |
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

Tutti i moduli condividono il [[books/il-metodo-bando/design-system-editoriale|design system editoriale della collana]]: titoli Arial Bold 20/14/12 pt, corpo Garamond Regular 11 pt con interlinea 1,15-1,20, tabelle/quiz/schemi/box Arial 9,5-10 pt. La regola vale sia per i capitoli gia scritti sia per ogni nuova scrittura o revisione.

## Gate di copertura didattica integrale

La non duplicazione opera insieme a [[sources/principio-copertura-didattica-integrale-2026-07-17]]. Il Metodo BANDO rende la teoria operativa ma non la sostituisce. Ogni materia assegnata deve essere insegnata e ogni concetto promesso spiegato o rinviato a una destinazione precisa, completa e verificata.

Ogni modulo mantiene una matrice con materia, concetti, fonti, collocazione, teoria, applicazione, output, verifica, stato e review normativa. `solo-nominato` e `mancante` bloccano la pubblicazione; `parziale` richiede integrazione; `rinviato` e' valido solo dopo verifica della destinazione.

Non duplicazione e completezza non sono alternative: un rinvio sostituisce la duplicazione soltanto quando la destinazione insegna davvero il concetto.
