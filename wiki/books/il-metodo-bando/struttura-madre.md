---
id: struttura-madre-il-metodo-bando
type: book_structure
title: "Struttura madre - Il Metodo BANDO"
status: canonical
domain: "concorsi pubblici italiani"
topics: ["metodo bando","struttura libro","nucleo comune concorsi pubblici","prove concorsuali","mappe profilo","moduli integrativi","ricettario digitale","moduli specialistici"]
entities: ["Metodo BANDO","Bando Decoder","Moduli Profilo","Piano 30/60/90 giorni","Diario degli errori"]
source_refs: ["sources/struttura-madre-il-metodo-bando.md","sources/metodo-bando-progetto-editoriale.md","sources/vol-01-il-metodo-bando-struttura-2026-07-14.md","sources/logica-volumi-copertura-concorsobook-v4.md"]
book_refs: ["il-metodo-bando","moduli-specialistici"]
confidence: 0.96
updated_at: 2026-07-14T19:00:00+02:00
created_at: 2026-05-10T11:45:00+02:00
review_required: false
canonical: true
tags: ["book-structure","outline","metodo-bando"]
---

# Struttura madre - Il Metodo BANDO

## Titolo e promessa
**Il Metodo BANDO**

Il sistema pratico per preparare concorsi pubblici diversi senza ricominciare da zero.

Il libro insegna a leggere il bando, costruire il piano, studiare le materie comuni, allenarsi sulle prove e adattare il metodo al proprio profilo.

## Architettura editoriale attuale
Decisione del 2026-06-27: il prodotto si divide in volume principale autonomo piu [[books/il-metodo-bando/ricettario-digitale|Ricettario operativo digitale]].

Il volume principale mantiene introduzione e capitoli 1-24 senza riduzione strutturale. Deve restare un manuale-workbook completo: metodo, materie comuni essenziali, allenamento alle prove, adattamento ai profili e kit finale.

I capitoli gia scritti dal 25 al 47 non vengono eliminati e non diventano una seconda meta del cartaceo. Vengono riclassificati come moduli digitali di applicazione avanzata: protocolli, checklist, casi, schede, simulazioni, laboratori e strumenti duplicabili collegati ai capitoli del libro.

Terzo livello: [[books/moduli/architettura-moduli-specialistici|moduli specialistici per famiglia concorsuale]]. I moduli sono libri di lavoro separati nella dashboard, con `book_id` autonomo, e servono a sviluppare profili, prove, materie specialistiche e casi tipici senza appesantire il volume principale.

La specifica strutturale del 14 luglio 2026 rende vincolanti per VOL-01 le undici aree `B-PA01/B-PA11`, l'introduzione, i capitoli 1-24 e le appendici A-F. Il target di circa 130.000 parole e una misura di lavorazione da ridurre in editing: completezza, leggibilita e utilita operativa prevalgono sul conteggio meccanico.

## Moduli specialistici collegati
La tassonomia canonica dei moduli specialistici normalizza la nuova architettura in 6 famiglie e 25 moduli effettivamente elencati:

- Funzioni Centrali: M-FC01 Ministeri, M-FC02 Agenzie fiscali, M-FC03 Enti pubblici non economici, M-FC04 Giustizia, M-FC05 Authority indipendenti.
- Funzioni Locali: M-FL01 Comuni e Unioni, M-FL02 Regioni/Province/Citta Metropolitane, M-FL03 Camere di Commercio, M-FL04 Polizia locale.
- Istruzione e Ricerca: M-IR01 Scuola, M-IR02 Universita e AFAM, M-IR03 Enti di ricerca, M-IR04 Cultura e beni culturali.
- Sanita: M-SA01 Sanita amministrativa, M-SA02 Professioni sanitarie, M-SA03 Dirigenza medica e sanitaria, M-SA04 Tecnici sanitari e prevenzione.
- Trasversali: M-TR01 ICT e trasformazione digitale, M-TR02 Appalti/PNRR/Fondi UE, M-TR03 Tecnico-ingegneristico, M-TR04 Ambiente e protezione civile.
- Carriere Speciali: M-SP01 Polizia/Carabinieri/GdF, M-SP02 Vigili del Fuoco, M-SP03 Magistratura/Avvocatura/Notariato, M-SP04 Prefettizia/Diplomatica.

I moduli MVP da sviluppare per primi sono M-FL01, M-IR01, M-FC03 e M-SA02.

## Design system editoriale
Il design system canonico e':

`books/il-metodo-bando/design-system-editoriale.md`

Decisione: il master di scrittura, revisione e anteprima deve essere impaginato in A4 verticale, con corpo Garamond Regular 11 pt e interlinea 1,15-1,20; titoli Arial Bold 20/14/12 pt; tabelle, quiz, schemi e box Arial 9,5-10 pt; colonna singola, strumenti compilabili e box operativi ricorrenti. Questa gerarchia si applica a tutti i libri gia scritti e a ogni sviluppo successivo. Il formato 17 x 24 cm circa e la derivazione commerciale compatta successiva.

Ogni capitolo deve essere scritto pensando alla pagina: spiegazione, box, caso, esercizio, errore tipico, riferimenti e note di review non sono accessori, ma parti della struttura didattica.

## Introduzione - Perche questo libro e' diverso
Deve spiegare che il libro non e' una raccolta di quiz e non e' un manuale per un solo concorso. E' un sistema universale di preparazione.

Deve contenere: promessa del libro, problema dei candidati, differenza tra studiare tutto e studiare con priorita, capitale riutilizzabile, spiegazione semplice del metodo BANDO, uso in 30/60/90 giorni, QR code opzionali ma non necessari.

Messaggio chiave: questo libro non da solo contenuti; insegna a costruire un metodo trasferibile da un concorso all'altro.

## Parte I - Capire il concorso prima di studiare
Questa parte evita l'errore di partire da manuali e quiz senza aver letto il bando.

### Capitolo 1 - Il nuovo candidato pubblico
Obiettivo: far capire che il candidato vincente sa orientarsi, selezionare, pianificare e allenarsi.

Contenuti: evoluzione dei concorsi, perche molti studiano tanto ma male, tipologie di concorso, aree di accesso, differenze tra concorsi comunali, ministeriali, agenzie fiscali, sanita amministrativa, scuola/universita, tecnici e polizia locale.

Strumenti: errore tipico, principiante vs strategico, mini-test "Che tipo di candidato sei?".

### Capitolo 2 - Anatomia del bando
Obiettivo: insegnare a leggere qualsiasi bando e trasformarlo in piano operativo.

Contenuti: requisiti, profilo, posti, riserve, titoli, scadenze, prove, materie, punteggi, soglie, graduatoria, documenti, materie obbligatorie/probabili/accessorie/killer/orali, compatibilita con il profilo, stima tempo e confronto tra bandi.

Strumenti: Bando Decoder doppia pagina, tabella "Dove trovo cosa", checklist prima della domanda, bando fittizio analizzato.

### Capitolo 3 - Il Metodo BANDO
Obiettivo: presentare il metodo proprietario del libro.

Struttura: B = Bando, A = Aree, N = Nuclei, D = Diario, O = Output.

Contenuti: cinque fasi, esempi su concorso amministrativo, enti locali e ministeriale, metodo lineare vs ciclico, uso con 30/60/90 giorni e piu concorsi.

Strumenti: schema visivo BANDO, mini-mappa dal bando al piano, pagina "Il mio concorso in una pagina".

## Parte II - Il nucleo comune dei concorsi pubblici
Ogni capitolo deve avere: perche la materia serve, mappa concetti, spiegazione operativa, come viene chiesta, errori tipici, domande guidate, mini-caso pratico, checkpoint finale.

### Capitolo 4 - Costituzione e ordinamento dello Stato
Contenuti: principi fondamentali, diritti/doveri, Parlamento, Governo, Presidente della Repubblica, Corte costituzionale, Magistratura, autonomie territoriali, fonti, rapporto Stato-Regioni-enti locali, principi PA.

Strumenti: Stato in una pagina, organi/funzioni/parole chiave, come lo chiede la commissione, 10 domande ragionate.

### Capitolo 5 - Diritto amministrativo operativo
Contenuti: PA, principi azione amministrativa, procedimento, responsabile, avvio, partecipazione, provvedimento, elementi, vizi, nullita/annullabilita, autotutela, silenzio, accessi, conferenza servizi, semplificazione, digitalizzazione, responsabilita.

Strumenti: caso istanza senza risposta, schema risposta orale, tabella procedimento/provvedimento/accesso/silenzio, domanda trappola, griglia procedimento.

### Capitolo 6 - Pubblico impiego e organizzazione della PA
Contenuti: rapporto di lavoro pubblico, accesso, contrattualizzazione, diritti/doveri, codice comportamento, responsabilita, dirigenza, performance, PIAO essenziale, lavoro agile, etica, conflitto interessi, whistleblowing, indirizzo politico vs gestione.

Strumenti: tabella dovere/comportamento/rischio, mini-casi, box orale.

### Capitolo 7 - Trasparenza, anticorruzione e privacy
Contenuti: trasparenza, amministrazione trasparente, accesso civico semplice/generalizzato, anticorruzione, PIAO essenziale, codice comportamento, conflitto interessi, privacy, ruoli privacy, bilanciamento.

Strumenti: tabella accessi, caso dati personali, box "trasparenza non significa pubblicare tutto", domande situazionali.

### Capitolo 8 - Contabilita pubblica essenziale
Contenuti: bilancio PA, entrate/spese, previsione, rendiconto, programmazione, principi base, impegno/liquidazione/ordinazione/pagamento, residui introduttivi, controlli, differenze Stato/enti locali/sanita.

Esclusioni: armonizzazione avanzata, schemi tecnici, contabilita sanitaria, economico-patrimoniale avanzata, fiscalita locale.

### Capitolo 9 - Contratti pubblici essenziali
Contenuti: perche la PA stipula contratti, principi, affidamento, gara, operatore economico, stazione appaltante, RUP, programmazione, esecuzione, controlli, trasparenza, anticorruzione, MEPA, appalti/concessioni/affidamenti introduttivi.

Esclusioni: codice appalti avanzato, soglie dettagliate, PNRR, project management, fondi UE, contenzioso.

### Capitolo 10 - Informatica, PA digitale e competenze digitali
Contenuti: informatica base, hardware/software, sistemi operativi, office automation, internet, posta, PEC, firma digitale, SPID, CIE, CNS, domicilio digitale, sicurezza, cloud, conservazione, protocollo, servizi digitali PA, accessibilita.

### Capitolo 11 - Inglese concorsuale essenziale
Contenuti: lessico amministrativo e lavoro pubblico, email semplici, comprensione brevi testi, grammatica ricorrente, false friends, domande frequenti, mini-brani, frasi per orale.

### Capitolo 12 - Logica, comprensione del testo e ragionamento
Contenuti: logica verbale, comprensione, deduzioni, serie numeriche/alfabetiche, proporzioni, sillogismi, ragionamento critico, tempo, esclusione, lettura domanda, errori da fretta.

## Parte III - Allenarsi come in prova
Questa parte rende il libro una palestra decisionale, non una raccolta di teoria.

### Capitolo 13 - Metodo di studio per concorsi
Contenuti: leggere/sottolineare non basta, active recall, ripetizione dilazionata, blocchi, metodo 25 minuti, alternanza teoria/quiz/casi/ripasso, poco tempo, recupero giorni persi, burnout, calendario, cosa non studiare.

### Capitolo 14 - La prova a quiz
Contenuti: banca dati, quiz senza banca dati, tempo, esclusione, quando saltare, correzione errori, categorie errore, diario errori e ripasso.

### Capitolo 15 - La prova scritta e teorico-pratica
Contenuti: quiz vs risposta sintetica vs elaborato vs caso, schema definizione/norma/funzione/esempio/conclusione, parole chiave, risposta in 10/20/30 righe, lettura traccia.

### Capitolo 16 - La prova orale
Contenuti: preparazione orale, risposta ordinata, inizio, collegamenti, vuoti memoria, domande incrociate, norma senza recitarla, esempi, chiusura, simulazione.

### Capitolo 17 - Casi pratici e problem solving amministrativo
Contenuti: ragionare come funzionario, soggetti, competenza, procedimento, interessi, vincoli, termini, soluzione. Casi: accesso, istanza incompleta, ritardo, informazioni cittadino, graduatoria, competenze, dati, affidamento, riesame.

### Capitolo 18 - Quesiti situazionali e soft skills
Contenuti: cosa sono, perche non sono buon senso, risposta coerente con PA, legalita, imparzialita, trasparenza, collaborazione, responsabilita, orientamento cittadino, riservatezza, proporzionalita.

## Parte IV - Adattare il metodo ai profili concorsuali

### Capitolo 19 - Le famiglie dei concorsi pubblici
Contenuti: amministrativo generale, amministrativo-contabile, enti locali, ministeri, giustizia, tributario, previdenza/lavoro, tecnico, informatico, polizia locale, sanita amministrativa, scuola/ATA/universita, socio-educativo, cultura, comunicazione, ambiente/protezione civile, appalti/PNRR/fondi UE, dirigenza, carriere speciali, corpi uniformati.

### Capitolo 20 - Mappe profilo: cosa resta comune e cosa cambia
Contenuti: per ogni famiglia profili tipici, materie quasi sempre presenti, probabili, eventuali, da modulo, prove frequenti, difficolta, rischio, strategia, cosa studiare prima, cosa non approfondire troppo.

Schede principali: amministrativo generale, amministrativo-contabile, enti locali, ministeri/funzioni centrali, giustizia, agenzie fiscali, previdenza/lavoro, tecnico con prova amministrativa, ICT/digitale, polizia locale, sanita amministrativa, scuola/ATA/universita.

### Capitolo 21 - Come scegliere i moduli integrativi
Contenuti: perche il libro base non contiene tutto, evitare dispersione, scegliere il modulo, combinare core + modulo, esempi profilo.

### Capitolo 22 - Piano 30/60/90 giorni
Contenuti: percorso 30 giorni, 60 giorni, 90 giorni, calendari compilabili, esempi amministrativo/enti locali/ministero, cosa tagliare se restano 15 giorni.

## Parte V - Kit finale del candidato

### Capitolo 23 - Il diario degli errori
Contenuti: correggere non basta, errori di memoria/concetto/distrazione/strategia/ansia, compilazione diario, flashcard, materie peggiorano, ripasso dagli errori.

### Capitolo 24 - Checklist operative
Contenuti: prima di scegliere, prima domanda, dopo domanda, prima scritto, prima orale, ultimi 7 giorni, ultime 24 ore, documenti, ansia/logistica, dopo prova.

## Appendici
- Appendice A: glossario essenziale PA, 100-150 termini.
- Appendice B: 100 parole chiave dei concorsi, con definizione, importanza e uso in risposta.
- Appendice C: template Bando Decoder.
- Appendice D: piano di studio personale.
- Appendice E: schema universale di risposta orale.
- Appendice F: matrice materie/profili.

## Contenuti da non inserire nel libro base
Tributario avanzato; processo civile e penale; codice della strada dettagliato; edilizia e urbanistica avanzata; contabilita enti locali avanzata; contabilita sanitaria; ordinamento scolastico dettagliato; diritto del lavoro e previdenza avanzati; fondi UE e PNRR avanzati; diritto internazionale; magistratura; carriera diplomatica; concorsi militari; prove fisiche; discipline sanitarie professionali; discipline tecniche specialistiche.
