# Specifica di ricostruzione ex novo del VOL-03

## 1. Obiettivo

Ricostruire e sostituire integralmente il volume canonico **VOL-03 - Fisco, Dogane, Previdenza e Ispettivo**, mantenendo la compatibilita con la collana Metodo BANDO e con la knowledge base ConcorsoBook OS.

Il nuovo volume deve coprire tutte le materie specialistiche richieste dai profili fiscali, doganali, previdenziali, ispettivi e amministrativi EPNE individuati dal dossier v4 e dai bandi ufficiali verificati. Il risultato di questa fase e un apparato editoriale e normativo `source_ready`, non la stesura integrale dei capitoli.

## 2. Decisioni approvate

- Ricostruzione ex novo, senza assumere l'indice attuale come struttura vincolante.
- Sostituzione dei file canonici del VOL-03 e dei due moduli collegati.
- Conservazione delle raw sources gia archiviate, che restano immutabili.
- Uso dei materiali persistenti precedenti solo dopo audit di pertinenza, vigenza e autorevolezza.
- Cut-off della ricerca: **17 luglio 2026**.
- Lingua italiana e tono formale, professionale, didattico e orientato ai concorsi pubblici.
- Stato finale previsto: `source_ready`, `review_required: true` per dati mobili e interpretazioni che richiedono controllo umano.

## 3. Perimetro editoriale

### 3.1 Modulo M-FC02 - Agenzie fiscali

Il modulo copre almeno:

- Agenzia delle Entrate;
- Agenzia delle Dogane e dei Monopoli;
- Agenzia delle Entrate-Riscossione;
- diritto tributario sostanziale e procedurale;
- imposte dirette, IVA, registro e adempimenti;
- accertamento, controlli, compliance e riscossione;
- sanzioni e reati tributari al livello richiesto dalle prove;
- processo tributario essenziale;
- dogane, Codice doganale dell'Unione, accise, giochi e monopoli;
- contabilita aziendale, bilancio, audit e profili ACFI;
- nuclei selettivi di diritto civile e commerciale funzionali alla fiscalita;
- catasto, pubblicita immobiliare ed estimo quando giustificati dai bandi;
- servizi digitali fiscali e output tipici delle prove.

### 3.2 Modulo M-FC03 - Previdenza, INAIL, EPNE e vigilanza

Il modulo copre almeno:

- INPS, INAIL, Ispettorato nazionale del lavoro ed EPNE rappresentativi;
- architettura della previdenza e dell'assistenza sociale;
- contribuzione e posizione assicurativa;
- prestazioni pensionistiche e sostegno al reddito;
- invalidita, prestazioni assistenziali e ISEE;
- assicurazione contro infortuni e malattie professionali;
- procedimento e ricorsi amministrativi previdenziali;
- legislazione sociale e lavoro rilevante per la vigilanza;
- tecniche ispettive, accesso, acquisizione documentale e verbalizzazione;
- diffida, prescrizione e sistema sanzionatorio;
- sicurezza sul lavoro in chiave ispettiva;
- contabilita e documentazione aziendale per i controlli;
- ordinamento, governance, bilancio, personale, procedimenti e servizi degli EPNE;
- PIAO, performance, anticorruzione, controlli interni, compliance e risk-based supervision;
- servizi digitali previdenziali, interoperabilita e tutela dei dati nel solo delta specialistico.

### 3.3 Esclusioni e rinvii

Il VOL-03 non duplica i nuclei comuni B-PA sviluppati nel VOL-01. Le materie ICT, procurement/PNRR, sanitarie e delle carriere speciali sono trattate solo per il raccordo indispensabile e rinviate rispettivamente ai volumi competenti.

## 4. Architettura del risultato

La struttura canonica sostitutiva comprende:

1. volume commerciale VOL-03;
2. modulo M-FC02 autonomo ma coordinato;
3. modulo M-FC03 autonomo ma coordinato;
4. front matter completo del volume e dei moduli;
5. indice analitico multilivello;
6. piano editoriale e matrice profilo-materia-prova-fonte;
7. appendici operative e strumenti condivisi;
8. source notes, topic pages ed entity pages necessarie alla tracciabilita.

Le sezioni editoriali obbligatorie sono:

- Servizi digitali inclusi;
- Frontespizio;
- Copyright e note editoriali;
- Sommario;
- Premessa;
- Indice.

Il loro stile deve essere coerente con il libro base, adattato al carattere specialistico del VOL-03 e privo di promesse assolute di completezza o aggiornamento automatico.

## 5. Metodo di acquisizione e consolidamento

Per ogni materia si applica questa sequenza:

1. censimento delle fonti persistenti;
2. verifica di autorita, vigenza, data e pertinenza;
3. ricerca delle lacune su fonti ufficiali;
4. download della fonte in `wiki/raw/` con nome stabile e metadati di provenienza;
5. creazione di una source note autonoma in `wiki/sources/`;
6. collegamento a topic, entity, moduli e capitoli;
7. registrazione dell'ingest in `wiki/log.md`;
8. aggiornamento del catalogo `wiki/index.md`;
9. segnalazione di conflitti, dati mobili e verifiche umane residue.

Ordine di preferenza delle fonti:

1. Normattiva, EUR-Lex e Gazzetta Ufficiale;
2. siti istituzionali degli enti e amministrazioni competenti;
3. bandi, allegati, PIAO, statuti, regolamenti, circolari e messaggi ufficiali;
4. Corte costituzionale, Corte di cassazione, giustizia amministrativa e Corte dei conti;
5. ARAN e contrattazione collettiva ufficiale;
6. manualistica e dottrina autorevole soltanto come supporto editoriale, mai come sostituto della fonte primaria.

## 6. Criteri dell'indice dettagliato

Ogni capitolo deve dichiarare almeno:

- finalita concorsuale;
- profili destinatari;
- materie e nuclei trattati;
- sottosezioni previste;
- output di prova;
- casi, errori tipici, quiz o strumenti;
- fonti consolidate principali;
- rinvii al VOL-01 e agli altri volumi;
- dati mobili o punti soggetti a review.

L'indice deve evitare capitoli-contenitore e duplicazioni. La granularita deve permettere la successiva assegnazione delle fonti e la scrittura professionale di ogni capitolo.

## 7. Sostituzione controllata

La ricostruzione puo riscrivere i file editoriali canonici sotto:

- `wiki/books/volumi/vol-03-fisco-dogane-previdenza-ispettivo/`;
- `wiki/books/moduli/m-fc02-agenzie-fiscali/`;
- `wiki/books/moduli/m-fc03-enti-non-economici/`.

Non sono cancellate o sovrascritte le raw sources. Le source notes precedenti possono essere sostituite soltanto quando la nuova nota ne assume esplicitamente la funzione canonica; negli altri casi vengono aggiornate chirurgicamente o deprecate con tracciabilita. Le modifiche non pertinenti gia presenti nel worktree restano intatte.

## 8. Controlli di qualita

La consegna e accettabile soltanto se:

- tutte le materie del dossier risultano coperte, rinviate motivatamente o marcate come gap;
- ogni capitolo ha fonti consolidate sufficienti;
- gli atti normativi principali sono verificati nella versione vigente al cut-off;
- bandi e profili rappresentativi sostengono le scelte di copertura;
- non vi sono duplicazioni sostanziali con VOL-01 o collocazioni cross-family errate;
- i link interni e il frontmatter sono coerenti;
- `wiki/index.md` e `wiki/log.md` riflettono il nuovo corpus;
- dati mobili, aliquote, soglie, requisiti, termini, circolari e CCNL sono identificati;
- un gap report finale distingue copertura completa, parziale e da validare;
- la memoria locale registra una traccia sintetica del flusso.

## 9. Verifica e collaudo

Il collaudo comprende:

- inventario comparato dossier-fonti-capitoli;
- scansione dei riferimenti mancanti e dei link interni;
- controllo dei frontmatter canonici;
- verifica dei file scaricati e delle relative source notes;
- controllo dei rinvii tra volume e moduli;
- revisione editoriale dell'indice e del front matter;
- esecuzione dei test o lint disponibili nel repository pertinenti alle modifiche;
- report conclusivo con file modificati, fonti acquisite, lacune residue e punti di review umana.

## 10. Limiti

La ricostruzione non equivale a consulenza fiscale, previdenziale o legale. La completezza e valutata rispetto ai bandi e al perimetro editoriale approvato, non rispetto a ogni possibile specializzazione professionale. La giurisprudenza e la prassi sono selezionate per rilevanza concorsuale e devono essere nuovamente controllate alla data effettiva di pubblicazione.
