# Piano di completamento — Capitolo 06

## Target

`chapters/06-ingegneria-software-api-interoperabilita-pa.md`

## Impostazione approvata

Il capitolo adotta una progressione equilibrata:

1. requisiti e ciclo di vita del software;
2. architettura, qualità, test e versionamento;
3. progettazione e gestione delle API;
4. e-service e interoperabilità nella PA.

Questa impostazione collega il metodo di sviluppo all’output richiesto dalla matrice — disegno API e caso e-service — senza ridurre il capitolo a un catalogo di tecnologie o, al contrario, a una trattazione astratta di project management.

## Esito della ricognizione

Il capitolo contiene soltanto frontmatter, titolo e specifica della struttura madre. La riga «Software e interoperabilità» della matrice è `parziale`: ciclo di vita, API ed e-service non dispongono ancora di testo destinato al lettore.

Il VOL-01, capitolo 10, § 16, introduce interoperabilità, PDND, open data e API. Il capitolo 6 deve assumere tali concetti come prerequisiti e sviluppare il livello specialistico: requisiti, ciclo di vita, architetture applicative, qualità, test, gestione delle modifiche, contratti API, versionamento, osservabilità ed e-service nel Modello di interoperabilità della PA.

Il confine con i capitoli adiacenti deve restare netto. Programmazione, algoritmi e strutture dati sono nel capitolo 3; basi dati e qualità del dato nel capitolo 4; rete e protocolli nel capitolo 5; infrastruttura cloud, container e DevOps nel capitolo 7; sicurezza operativa nel capitolo 8; IAM, crittografia e incident response nel capitolo 9; data governance, open data e interoperabilità semantica nel capitolo 10; procurement e fornitori nel capitolo 12.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: ICT e Data/AI | Teoria e casi calibrati su progettazione, integrazione e gestione evolutiva di servizi software pubblici. |
| Materia: Software e interoperabilità | Trattazione coordinata di ciclo di vita, qualità, API ed e-service. |
| Concetti: ciclo vita, API, e-service | Perimetro ampliato secondo la specifica a requisiti, architetture, test e versionamento. |
| Frequenza/peso: da validare | Nessuna frequenza quantitativa; profondità, linguaggi, framework e piattaforme dipendono dal bando. |
| Fonte consolidata: dossier M-TR01 | Il dossier definisce collocazione e perimetro, ma non sostiene da solo i claim tecnici e regolatori. |
| Collocazione: capitolo 06 | Ingegneria software e interoperabilità applicativa restano qui; cloud, cyber e data governance ricevono rinvii precisi. |
| Copertura teorica: da sviluppare | Ogni nucleo riceverà definizione, funzione, elementi, distinzioni, conseguenze ed esempio. |
| Applicazione: disegno API | Dall’esigenza amministrativa al contratto, agli errori, al versionamento e ai requisiti di servizio. |
| Output: caso e-service | Scheda di progettazione e risposta orale motivata su erogatore, fruitore, dati, finalità e livelli di servizio. |
| Verifica: caso | Caso guidato, esercizi, domanda-trappola, quiz e checklist. |
| Stato: parziale | Potrà passare a `completo` soltanto dopo verifica del testo reale allo step 10. |
| Review: AgID e UE | Servono fonti aggiornate AgID/PDND, riferimenti europei e review tecnica e giuridico-organizzativa. |

## Nuclei assegnati

1. Confine fra nozioni introduttive del VOL-01 e livello specialistico del VOL-08.
2. Software come sistema evolutivo: stakeholder, bisogno, requisito, vincolo e criterio di accettazione.
3. Requisiti funzionali e non funzionali; qualità, sicurezza, accessibilità, prestazioni e manutenibilità.
4. Tracciabilità dal requisito al test e alla modifica.
5. Ciclo di vita: analisi, progettazione, sviluppo, verifica, rilascio, esercizio, manutenzione e dismissione.
6. Modelli sequenziali, iterativi e incrementali; Agile a livello concettuale, senza trasformare il capitolo in manuale di certificazione.
7. Ruoli e responsabilità: committente, utenti, product owner o responsabile del servizio, analisti, sviluppatori, tester, operations e fornitori.
8. Architettura software: componenti, moduli, interfacce, dipendenze, coesione e accoppiamento.
9. Architetture monolitiche, a livelli, client-server e a servizi; criteri di scelta e trade-off.
10. Separazione fra contratto esterno e implementazione interna.
11. Qualità del software: correttezza rispetto ai requisiti, affidabilità, usabilità, efficienza, sicurezza, manutenibilità e portabilità, con terminologia da consolidare.
12. Verifica e validazione; test unitari, di integrazione, di sistema, di accettazione e regressione.
13. Casi di test, precondizioni, input, risultato atteso, esito ed evidenza.
14. Difetto, errore, failure, gravità, priorità e ciclo di correzione.
15. Gestione della configurazione e controllo di versione; repository, commit, branch, merge, tag e release a livello trasferibile.
16. Code review, integrazione continua e automazione dei controlli, mantenendo pipeline di delivery e infrastruttura nel capitolo 7.
17. API come contratto fra sistemi: operazione, risorsa o servizio, input, output, errori e precondizioni.
18. API sincrone e asincrone; richiesta-risposta, evento e messaggio a livello concettuale.
19. REST e SOAP per principi e contesti d’uso, senza equivalenze semplicistiche né dipendenza da prodotto.
20. Metodi HTTP, URI, header, rappresentazioni e codici di stato nei casi REST.
21. Formati e schemi: JSON, XML, validazione e compatibilità.
22. Descrizione formale del contratto tramite specifiche e IDL, con OpenAPI come esempio per API HTTP.
23. Versionamento compatibile e non compatibile; deprecazione, migrazione e documentazione coordinata.
24. Idempotenza, paginazione, filtraggio, limiti d’uso, timeout e gestione degli errori.
25. Requisiti di servizio: disponibilità, latenza, capacità, SLO/SLA e osservabilità.
26. API management a livello concettuale: catalogo, pubblicazione, accesso, throttling, logging e accounting.
27. Interoperabilità tecnica, sintattica, semantica e organizzativa; distinzione fra i livelli.
28. Modello di interoperabilità della PA e ruolo di standard, pattern di interazione, pattern di sicurezza e profili.
29. Erogatore, fruitore, e-service, API, finalità, accordi o attributi richiesti e livelli di servizio nel contesto PDND, da verificare sulla documentazione vigente.
30. Principio once only come obiettivo amministrativo, senza presentarlo come accesso indiscriminato ai dati.
31. Protezione dei dati, autorizzazione, minimizzazione e tracciabilità come requisiti di progetto, con rinvio ai capitoli 8-10 per la trattazione specialistica.
32. Interoperabilità europea: European Interoperability Framework e Regolamento (UE) 2024/903 come inquadramento, previo controllo della versione vigente e dell’applicabilità.
33. Produzione di specifica essenziale API, caso e-service, quiz, risposta orale e checklist.

## Nuclei già completi

Nessun nucleo specialistico è completo nel capitolo 6.

Nel VOL-01, capitolo 10, § 16, sono già completi i prerequisiti:

- definizione generale di interoperabilità;
- ruolo introduttivo della PDND;
- API come interfacce di comunicazione fra sistemi;
- distinzione fra scambio autorizzato e pubblicazione open data;
- collegamento fra interoperabilità, regole comuni, standard, sicurezza, qualità dei dati e responsabilità.

Il rinvio non copre requisiti, ciclo di vita, architetture, qualità, test, gestione della configurazione, progettazione del contratto API, compatibilità, API management, pattern del ModI o costruzione di un e-service.

## Nuclei da sviluppare

- trasformazione di un bisogno amministrativo in requisiti verificabili;
- confronto fra modelli di ciclo di vita;
- tracciabilità requisito-progetto-test-rilascio;
- criteri architetturali e gestione delle dipendenze;
- strategia di test e prova di accettazione;
- controllo di versione e gestione delle modifiche;
- struttura di un contratto API;
- errori, compatibilità, idempotenza e versionamento;
- qualità operativa, livelli di servizio e osservabilità;
- distinzione fra API, servizio applicativo ed e-service;
- ruoli di erogatore e fruitore;
- interoperabilità tecnica, sintattica, semantica e organizzativa;
- raccordo fra ModI, PDND, finalità, autorizzazioni e tracciabilità;
- disegno di API e caso di interoperabilità completo.

## Sezioni da conservare

- frontmatter e identificativi;
- H1 esistente;
- specifica della struttura madre come vincolo editoriale;
- collocazione nella Parte II del volume;
- output previsti: disegno API e caso di interoperabilità;
- review AgID e UE.

## Duplicazioni da evitare

- definizioni introduttive di API, interoperabilità, PDND e open data già complete nel VOL-01;
- sintassi di programmazione, algoritmi, strutture dati e debugging di codice, trattati nel capitolo 3;
- modellazione dei dati, SQL/NoSQL e qualità del dato, trattati nel capitolo 4;
- protocolli di rete, porte, DNS e HTTP come trasporto, trattati nel capitolo 5;
- orchestrazione, container, CI/CD operativa, infrastruttura e deployment cloud, assegnati al capitolo 7;
- threat modeling, vulnerabilità, hardening e sicurezza delle API, assegnati al capitolo 8;
- IAM, token, crittografia, logging di sicurezza e incident response, assegnati al capitolo 9;
- cataloghi semantici, metadati, open data e data governance, assegnati al capitolo 10;
- capitolati, SLA contrattuali, sourcing e gestione dei fornitori, assegnati al capitolo 12;
- dettagli di framework, linguaggi, prodotti o piattaforme non richiesti dal bando.

## Esempi, casi, domande ed esercizi necessari

- trasformazione della richiesta «verificare un requisito anagrafico» in requisiti funzionali e non funzionali;
- matrice requisito-criterio di accettazione-test;
- confronto ragionato fra sviluppo sequenziale e iterativo;
- scomposizione di un servizio in componenti e interfacce;
- classificazione di test unitario, integrazione, sistema, accettazione e regressione;
- esempio di modifica incompatibile e strategia di versionamento;
- progettazione di un endpoint con operazione, input, output, errori e codici di stato;
- caso di retry su operazione idempotente e rischio di duplicazione su operazione non idempotente;
- lettura di una specifica OpenAPI essenziale, senza dipendenza da un linguaggio;
- caso e-service fra amministrazione erogatrice e fruitrice con finalità, dato minimo, autorizzazione, evidenza e livello di servizio;
- domanda da commissario sul percorso dal requisito al rilascio;
- domanda-trappola «un’API pubblicata è automaticamente accessibile a chiunque?»;
- errore tipico: progettare il payload prima di chiarire finalità, attori e requisiti;
- quiz su ciclo di vita, test, versionamento, API ed e-service;
- checklist finale «specifico, progetto, verifico, pubblico, osservo, evolvo».

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro editoriale;
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]];
- [[sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026]];
- [[sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[topics/open-data-interoperabilita-cloud-pa]];
- [[topics/pa-digitale]];
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 16;
- [[books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica]].

### Fonti tecniche e istituzionali da consolidare prima o durante lo step 09

- AgID, Linee guida sull’interoperabilità tecnica delle Pubbliche Amministrazioni e relativi allegati;
- AgID, Linee guida tecnologie e standard per la sicurezza dell’interoperabilità tramite API;
- AgID, Linee guida sull’infrastruttura tecnologica della PDND e allegati vigenti;
- documentazione ufficiale PDND per ciclo di pubblicazione e fruizione degli e-service;
- Regolamento (UE) 2024/903, Interoperable Europe Act, su EUR-Lex;
- European Interoperability Framework e documentazione Interoperable Europe;
- standard o guide primarie per ciclo di vita, requisiti, qualità e testing del software, con verifica delle condizioni di accesso e citazione;
- specifiche ufficiali HTTP, JSON, XML, OpenAPI e, se trattato, SOAP;
- documentazione ufficiale Git per il modello di controllo di versione, mantenendo i comandi fuori dal nucleo teorico;
- bandi ufficiali del campione VOL-08 per validare metodologie, linguaggi, framework, standard e piattaforme richiesti.

Le fonti attuali sono adeguate per il perimetro introduttivo di interoperabilità e PDND, ma non bastano a dichiarare completi ingegneria software, testing, contratti API e funzionamento operativo degli e-service. Le nuove fonti dovranno essere trasformate in una source note consolidata prima di sostenere il testo finale.

## Topic, entity e quiz collegati

- `topics/open-data-interoperabilita-cloud-pa.md` è pertinente ma orientato al livello introduttivo e al capitolo 10 del VOL-01;
- `topics/pa-digitale.md` offre il quadro amministrativo generale;
- le entity già censite includono AgID, PDND e API, ma vanno collegate a fonti più granulari;
- non risultano topic specialistici consolidati su ingegneria software, testing o progettazione API;
- non risultano quiz specialistici consolidati su ciclo di vita, versionamento, contratti API ed e-service;
- i nuovi esempi e quiz richiedono verifica tecnica e istituzionale.

## Review umane richieste

- software architect: requisiti, architetture, dipendenze e trade-off;
- senior developer o software engineer: ciclo di vita, versionamento e manutenibilità;
- QA/test engineer: livelli di test, criteri di accettazione e regressione;
- API designer: contratti, compatibilità, idempotenza, errori e documentazione;
- esperto AgID/ModI/PDND: terminologia, ruoli, pattern ed e-service;
- DPO o privacy specialist: finalità, minimizzazione, autorizzazioni e tracciabilità;
- esperto di diritto digitale europeo: Interoperable Europe Act e raccordi con il quadro nazionale;
- responsabile del campione bandi: profondità e tecnologie effettivamente richieste;
- responsabile editoriale: confini con VOL-01 e capitoli 3-5 e 7-12;
- revisore didattico: coerenza fra teoria, disegno API, caso e-service, quiz e risposta orale;
- revisore fonti: vigenza e granularità dei riferimenti AgID, PDND, UE e standard tecnici.

## Struttura proposta e budget KDP

# Ingegneria software, API e interoperabilità PA

## Obiettivo e confine con il VOL-01 — 170 parole

## Mappa BANDO dal requisito all’e-service — 190 parole

## Dal bisogno ai requisiti verificabili — 380 parole

### Stakeholder, requisiti e vincoli

### Criteri di accettazione e tracciabilità

## Ciclo di vita e organizzazione dello sviluppo — 430 parole

### Modelli sequenziali, iterativi e incrementali

### Ruoli, modifiche e configurazione

## Architettura e qualità del software — 430 parole

### Componenti, interfacce e dipendenze

### Attributi di qualità e trade-off

## Verifica, validazione e test — 390 parole

### Livelli di test e regressione

### Caso di test ed evidenza

## API come contratto — 520 parole

### Operazioni, dati, errori e rappresentazioni

### REST, SOAP e descrizione formale

## Evoluzione e gestione delle API — 390 parole

### Compatibilità, versionamento e deprecazione

### Catalogo, limiti d’uso, livelli di servizio e osservabilità

## Interoperabilità ed e-service nella PA — 500 parole

### Livelli di interoperabilità e ModI

### Erogatore, fruitore, PDND e principio once only

## Caso guidato: verifica di un requisito anagrafico — 300 parole

## Laboratorio: disegno essenziale di un’API — 300 parole

## Domanda da commissario e domanda-trappola — 160 parole

## Errore tipico — 80 parole

## Mini-esercizi e quiz — 300 parole

## Checklist finale — 150 parole più tabella

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 100 parole

Budget orientativo: 4.400-4.800 parole, tabelle, schemi, caso ed esercizi inclusi. Il budget non comprende programmazione di dettaglio, deployment cloud, sicurezza offensiva, IAM specialistico, data governance o procurement.

## Criteri di approvabilità per lo step 09

- ogni elemento della specifica e della matrice riceve teoria e verifica;
- il rinvio al VOL-01 resta preciso e limitato ai prerequisiti;
- requisito, vincolo e criterio di accettazione restano distinti;
- ciclo di vita e metodologie non sono ridotti a una sequenza rigida universale;
- architetture e attributi di qualità sono presentati mediante trade-off;
- verifica, validazione e livelli di test ricevono esempi controllati;
- l’API è trattata come contratto prima che come endpoint o tecnologia;
- REST, SOAP, JSON, XML e OpenAPI sono descritti senza equivalenze scorrette;
- versionamento, compatibilità, errori, idempotenza e livelli di servizio ricevono copertura autonoma;
- ModI, PDND ed e-service usano terminologia verificata sulle fonti vigenti;
- interoperabilità non è confusa con open data né con accesso indiscriminato;
- il caso dichiara attori, finalità, dati minimi, autorizzazione, evidenze ed esito;
- cloud, cyber, IAM, data governance e procurement restano nei capitoli dedicati;
- esempi e casi applicano concetti già spiegati;
- fonti tecniche mancanti e review specialistiche restano aperte finché non eseguite.

## Addendum retrofit Format 2 — 2026-08-10

Questo addendum sostituisce, per il nuovo ciclo degli step 08-12, le valutazioni legacy sullo stato del capitolo. Il testo destinato al lettore esiste già: contiene circa 3.080 parole e costituisce la base da conservare. Lo step 09 dovrà riorganizzarlo nel Format 2 e colmare i delta misurabili, non riscriverlo da zero.

### Stato reale e criterio di intervento

- Il capitolo sviluppa già requisiti, ciclo di vita, architetture, qualità, test, controllo di versione, contratti API, evoluzione, ModI, PDND ed e-service.
- Sono presenti Mappa BANDO, matrice requisito-test-evidenza, caso guidato, laboratorio API, domanda da commissario, domanda-trappola, errore tipico, tre esercizi, un quiz e checklist.
- La source note `sources/ingegneria-software-api-interoperabilita-fonti-tecniche` consolida riferimenti IEEE, IETF, OpenAPI, AgID, PDND e Unione europea; processi PDND, versioni operative e applicazione puntuale del Regolamento (UE) 2024/903 restano da verificare al text freeze.
- Il retrofit deve introdurre Nucleo ID stabili, almeno 600 parole per nucleo, una verifica dopo 5-7 nuclei e almeno sei quiz commentati.
- La riga `Software e interoperabilità` della matrice resta `completo` sul piano aggregato, ma lo step 10 dovrà dimostrare la copertura atomica dei sei nuclei Format 2.

### Nuclei Format 2 assegnati

| Nucleo ID | Titolo operativo | Stato attuale | Sviluppo previsto allo step 09 | Confini principali |
| --- | --- | --- | --- | --- |
| `N-TR01-06-01` | Requisiti e ciclo di vita verificabile | parziale-avanzato | Integrare bisogno, stakeholder, requisiti, vincoli, criteri di accettazione, tracciabilità, modelli di ciclo e ruoli in una progressione unica. | Programmazione al cap. 3; capitolato e accettazione contrattuale al cap. 12. |
| `N-TR01-06-02` | Architettura e qualità del software | parziale-avanzato | Collegare componenti, interfacce, coesione, accoppiamento, forme architetturali e attributi di qualità a trade-off verificabili. | Reti al cap. 5; cloud, container e deployment al cap. 7. |
| `N-TR01-06-03` | Verifica, validazione, test e configurazione | parziale-avanzato | Consolidare livelli di test, casi, evidenze, difetti, regressione, versionamento del codice e gestione controllata delle modifiche. | CI/CD operativa al cap. 7; Secure SDLC e vulnerabilità al cap. 8. |
| `N-TR01-06-04` | API come contratto | parziale-avanzato | Sviluppare operazioni, dati, precondizioni, errori, sincrono/asincrono, REST/SOAP, HTTP, JSON/XML e OpenAPI con disegno essenziale. | Protocolli come trasporto al cap. 5; modellazione dei dati al cap. 4. |
| `N-TR01-06-05` | Evoluzione e gestione delle API | parziale-avanzato | Integrare compatibilità, versionamento, deprecazione, idempotenza, paginazione, limiti d’uso, livelli di servizio, osservabilità e API management. | IAM e logging di sicurezza al cap. 9; SLA contrattuali al cap. 12. |
| `N-TR01-06-06` | Interoperabilità PA ed e-service | parziale-avanzato | Coordinare livelli di interoperabilità, ModI, erogatore, fruitore, PDND, e-service, finalità, minimizzazione, once only e raccordo europeo; assorbire caso e output concorsuali. | Open data e semantica al cap. 10; privacy specialistica e sicurezza nei capp. 8-10. |

I sei nuclei devono superare autonomamente il test dello studente: definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, esempio e verifica. Nessun nucleo è dichiarato completo in Format 2 prima del controllo dello step 10.

### Struttura H1/H2/H3 prevista

# Ingegneria software, API e interoperabilità PA

## Obiettivo, confine con il VOL-01 e Mappa BANDO

## N-TR01-06-01 · Requisiti e ciclo di vita verificabile

### Bisogni, requisiti, vincoli e criteri di accettazione

### Tracciabilità, modelli di ciclo e ruoli

## N-TR01-06-02 · Architettura e qualità del software

### Componenti, interfacce e dipendenze

### Forme architetturali e attributi di qualità

## N-TR01-06-03 · Verifica, validazione, test e configurazione

### Livelli di test, casi ed evidenze

### Difetti, regressione e controllo delle modifiche

## N-TR01-06-04 · API come contratto

### Operazioni, dati, errori e interazioni

### REST, SOAP, rappresentazioni e OpenAPI

## N-TR01-06-05 · Evoluzione e gestione delle API

### Compatibilità, versionamento e deprecazione

### Idempotenza, requisiti operativi e API management

## N-TR01-06-06 · Interoperabilità PA ed e-service

### Livelli di interoperabilità, ModI e PDND

### Caso guidato, laboratorio e output concorsuali

### Domanda da commissario, domanda-trappola ed errore tipico

## ▣ Verifica

### Tre o più esercizi applicativi

### Sei o più quiz commentati

## Checklist finale

## Da sapere in 5 righe

## Riferimenti professionali essenziali

### Budget e prove previste

- Corpo complessivo: **4.700-5.700 parole**, escluso frontmatter.
- Densità: **600-900 parole per ciascun Nucleo ID**; eventuali scostamenti richiedono motivazione didattica.
- Verifiche: **un unico blocco dopo i sei nuclei**, entro il limite di 5-7 nuclei consecutivi.
- Quiz: **almeno sei**, con risposta corretta e commento sui distrattori o sull’errore tipico.
- Esercizi: **almeno tre** — requisito-test, compatibilità/versionamento e caso e-service.
- Casi: **almeno uno completo**, con attori, finalità, dato minimo, autorizzazione, evidenze e criterio di chiusura.
- Output: matrice requisito-test-evidenza, specifica essenziale API, scheda e-service e risposta orale motivata.

### Fonti, topic, entity e rinvii da preservare

- Conservare tutti i `source_refs` e i `last_compiled_from` attuali, inclusa la source note tecnica-istituzionale.
- Usare `topics/open-data-interoperabilita-cloud-pa` e `topics/pa-digitale` come raccordi introduttivi, non come sostituti delle fonti specialistiche.
- Conservare le entity IEEE Computer Society, IETF, OpenAPI Initiative, AgID, PDND e Unione europea solo nei punti sostenuti dalle fonti dichiarate.
- Mantenere il rinvio preciso al VOL-01, capitolo 10, § 16, per i prerequisiti su API, PDND e interoperabilità.
- Conservare i confini con i capp. 3-5 e 7-12 fissati dal piano e dalla Bibbia del volume.

### Audit specialistici richiesti

1. `chapter-lint` e controllo di densità didattica Format 2.
2. Audit software engineering su requisiti, ciclo di vita, architettura, qualità e configurazione.
3. Audit QA su verifica, validazione, livelli di test, casi, regressione ed evidenze.
4. Audit API su HTTP, REST/SOAP, errori, OpenAPI, compatibilità, idempotenza e versionamento.
5. Audit AgID/PDND su terminologia, ruoli, ModI, e-service, finalità e processi mobili.
6. Audit giuridico-organizzativo sul raccordo con CAD, once only, minimizzazione e Regolamento (UE) 2024/903.
7. Controllo dei confini con VOL-01 e con i capitoli 3-5 e 7-12.
8. Citation guard su `source_refs`, `last_compiled_from`, riferimenti normativi e professionali.
9. Revisione editoriale a 30 punti, test dello studente e controllo KDP su tabelle, schemi e blocchi tecnici.

### Criterio di uscita aggiornato

Lo step 09 è approvabile quando i sei Nucleo ID compaiono nel capitolo, ogni nucleo supera la soglia e il test dello studente, la verifica contiene almeno sei quiz commentati e tre esercizi, il caso e-service dichiara attori, finalità, dati, autorizzazione ed evidenze e il corpo non dipende da materiali interni. Lo step 10 dovrà dimostrare la copertura reale nella matrice; gli step 11-12 completeranno Humanizer e revisione editoriale senza anticipare la conferma umana dello step 24.
