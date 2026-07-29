# Piano di completamento — Capitolo 04

## Target

`chapters/04-basi-dati-sql-nosql-qualita-dato.md`

## Esito della ricognizione

Il capitolo contiene soltanto frontmatter, titolo e specifica della struttura madre. La riga assegnata nella matrice è ancora `parziale`: non esiste testo destinato al lettore e nessun nucleo specialistico può essere considerato completo.

La matrice richiede teoria su SQL, NoSQL e qualità del dato, applicazione mediante query e schema, output di scritto tecnico e verifica tramite esercizio. La specifica amplia il perimetro a modelli, normalizzazione, transazioni, indici e sicurezza.

Il VOL-01, capitolo 10, § 7, copre già a livello introduttivo database, DBMS, tabelle, righe, colonne, chiavi, relazioni, query e comandi SQL elementari. Il capitolo 4 deve assumere tali nozioni come prerequisiti e sviluppare il livello richiesto ai profili ICT e Data/AI: modellazione, vincoli, interrogazioni, transazioni, prestazioni, famiglie NoSQL, qualità tecnica e controlli di accesso.

La Bibbia del Volume e l’indice collocano il capitolo nella Parte II, fra programmazione e infrastrutture. Il confine con il capitolo 10 è decisivo: qui la qualità va trattata come proprietà e controllo del dato nella base dati; ruoli, metadati, cataloghi, open data, riuso e governance appartengono al capitolo 10.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: ICT e Data/AI | Teoria e prove calibrate su progettazione, interrogazione e diagnosi di basi dati, non sull’uso elementare di un database d’ufficio. |
| Materia: Basi dati | Distinzione fra dati, base dati, DBMS, modello, schema, istanza e operazioni. |
| Concetti: SQL, NoSQL, qualità | SQL sviluppato oltre il riconoscimento dei comandi; NoSQL organizzato per famiglie e casi d’uso; qualità tradotta in dimensioni e controlli tecnici. |
| Frequenza/peso: da validare | Nessuna frequenza quantitativa sarà dichiarata; profondità e prodotti specifici dipendono dal singolo bando. |
| Fonte consolidata: dossier M-TR01 | Il dossier definisce perimetro e collocazione, ma non è fonte tecnica autosufficiente. |
| Collocazione: capitolo 04 | Modellazione, query, transazioni, indici e controlli sui dati restano nel capitolo 4; API, cybersecurity e data governance ricevono rinvii precisi. |
| Copertura teorica: da sviluppare | Ogni nucleo avrà definizione, funzione, elementi, distinzioni, conseguenze ed esempio. |
| Applicazione: query e schema | Schema relazionale di un procedimento amministrativo, query progressive e diagnosi di anomalie. |
| Output: scritto tecnico | Progettazione motivata, lettura o correzione di query e breve confronto SQL/NoSQL. |
| Verifica: esercizio | Esercizi con soluzione, domanda orale, domanda-trappola, errore tipico, quiz e checklist. |
| Stato: parziale | Potrà diventare `completo` soltanto dopo riscontro nel testo e aggiornamento motivato della matrice allo step 10. |
| Review: fonti tecniche | Servono fonti primarie o universitarie granulari e revisione specialistica di schema, query, transazioni e prestazioni. |

## Nuclei assegnati

1. Confine fra il livello introduttivo del VOL-01 e il livello specialistico del VOL-08.
2. Base dati, DBMS, modello dei dati, schema e istanza.
3. Modello relazionale: relazione/tabella, tupla/riga, attributo/colonna e dominio.
4. Chiavi candidate, chiave primaria, chiave composta e chiave esterna.
5. Relazioni uno-a-uno, uno-a-molti e molti-a-molti; tabella associativa.
6. Modellazione concettuale e logica a livello concorsuale, con entità, attributi e relazioni.
7. Integrità di entità, integrità referenziale, vincoli di dominio, `NULL`, unicità e controlli.
8. Dipendenze e anomalie di inserimento, aggiornamento e cancellazione.
9. Normalizzazione almeno fino a prima, seconda e terza forma normale, senza formalismo eccessivo.
10. SQL dichiarativo e principali famiglie operative: definizione, interrogazione e modifica dei dati.
11. `SELECT`, proiezione, filtro, ordinamento, alias, funzioni aggregate, `GROUP BY` e `HAVING`.
12. Join interne ed esterne a livello operativo, con attenzione a cardinalità e righe duplicate.
13. Sottoquery a livello introduttivo e differenza rispetto a una join.
14. `INSERT`, `UPDATE` e `DELETE`, con condizioni e rischio di modifiche massive.
15. Transazioni e proprietà ACID; `COMMIT`, `ROLLBACK`, concorrenza e isolamento a livello concettuale.
16. Indici: funzione, compromesso fra letture, scritture e spazio; differenza rispetto a chiavi e vincoli.
17. NoSQL come insieme di famiglie, non come singolo modello: chiave-valore, documentale, wide-column e grafo.
18. Criteri di scelta fra relazionale e NoSQL: struttura, relazioni, flessibilità, scala, consistenza e pattern di accesso.
19. Qualità del dato: accuratezza, completezza, coerenza, validità, unicità e tempestività.
20. Controlli tecnici di qualità: tipi, vincoli, validazione, deduplicazione, controlli di dominio e monitoraggio.
21. Sicurezza della base dati: autenticazione, autorizzazione, ruoli, privilegi minimi, cifratura e audit a livello di raccordo.
22. Backup, ripristino e disponibilità soltanto per gli effetti sulla base dati, senza duplicare infrastrutture e continuità.
23. Produzione di schema, query, diagnosi, risposta orale, quiz ed esercizio tecnico.

## Nuclei già completi

Nessun nucleo specialistico è completo nel capitolo 4.

Sono già completi nel VOL-01, capitolo 10, § 7, i prerequisiti:

- definizione introduttiva di database e DBMS;
- tabella, record/riga e campo/colonna;
- chiave primaria, chiave esterna, relazione e query;
- distinzione elementare fra foglio elettronico e database;
- riconoscimento di `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `GROUP BY`, `JOIN`, `INSERT`, `UPDATE` e `DELETE`;
- esempio elementare di interrogazione;
- richiamo generale a correttezza, aggiornamento, coerenza, accesso autorizzato e protezione.

Il rinvio è valido per i prerequisiti, ma non copre modellazione, normalizzazione, join operative, transazioni, indici, NoSQL, dimensioni della qualità o sicurezza tecnica.

## Nuclei da sviluppare

- traduzione di un requisito informativo in entità, attributi, relazioni e vincoli;
- passaggio motivato dal modello concettuale allo schema relazionale;
- riconoscimento di chiavi candidate, composte ed esterne;
- diagnosi delle anomalie prodotte da una tabella non normalizzata;
- applicazione guidata di 1NF, 2NF e 3NF;
- costruzione e lettura di query con filtri, aggregazioni e join;
- distinzione operativa fra `WHERE` e `HAVING`;
- effetti di `NULL` e duplicati sui risultati;
- uso sicuro di `UPDATE` e `DELETE`;
- atomicità, consistenza, isolamento e durabilità;
- scopo e costo degli indici;
- confronto non ideologico fra relazionale e famiglie NoSQL;
- misurazione e correzione di problemi di qualità del dato;
- controllo degli accessi per ruoli e privilegi;
- esposizione scritta e orale di una scelta progettuale.

## Sezioni da conservare

- frontmatter e identificativi;
- H1 esistente;
- specifica della struttura madre come vincolo editoriale durante la lavorazione;
- collocazione nella Parte II del volume;
- collegamento al dossier M-TR01;
- output previsti: query, schema e diagnosi degli errori.

## Duplicazioni da evitare

- definizioni e comandi SQL elementari già completi nel VOL-01, salvo richiamo sintetico;
- algoritmi e strutture dati generali, trattati nel capitolo 3;
- file system, storage, disponibilità infrastrutturale e troubleshooting di rete, assegnati ai capitoli 2 e 5;
- progettazione delle API, e-service e interoperabilità applicativa, assegnate al capitolo 6;
- hardening, vulnerabilità, IAM, crittografia, logging e incident response, assegnati ai capitoli 8 e 9;
- ruoli di data governance, metadati, cataloghi, open data, riuso e interoperabilità semantica, assegnati al capitolo 10;
- prodotti proprietari presentati come standard universali;
- sintassi avanzata specifica di un solo DBMS quando il bando non lo richiede.

## Esempi, casi, domande ed esercizi necessari

- caso guida su pratiche amministrative, uffici e stati di lavorazione;
- schema iniziale non normalizzato e trasformazione progressiva in tabelle coerenti;
- relazione molti-a-molti risolta mediante tabella associativa;
- query di selezione con `WHERE` e `ORDER BY`;
- query con `JOIN` fra pratiche e uffici;
- query aggregata con `GROUP BY` e filtro `HAVING`;
- esempio controllato di `NULL` e di duplicato;
- `UPDATE` o `DELETE` privo di filtro come errore da diagnosticare;
- transazione con due operazioni che devono riuscire o fallire insieme;
- confronto fra ricerca con e senza indice, senza promettere costi assoluti;
- confronto fra schema relazionale e documento JSON per lo stesso caso;
- tabella decisionale SQL/NoSQL basata su requisiti e pattern di accesso;
- scheda di qualità con regola, metrica, soglia, anomalia e azione correttiva;
- domanda da commissario sulla normalizzazione;
- domanda-trappola su indice, chiave primaria o NoSQL;
- esercizio di progettazione di uno schema;
- esercizio di scrittura o correzione di query con soluzione motivata;
- quiz su transazioni, join, vincoli e qualità;
- checklist finale «modello, interrogo, proteggo, verifico».

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro editoriale;
- [[sources/database-programmazione-formati-concorsi]] — per prerequisiti, SQL essenziale e documentazione PostgreSQL/Oracle già acquisita;
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[topics/database-e-sql]];
- [[topics/informatica]];
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, § 7;
- [[books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica]];
- [[books/volumi/vol-08-ict-digitale-cybersecurity-dati/planning/01-indice-completo]].

### Fonti tecniche da consolidare prima o durante lo step 09

- documentazione ufficiale PostgreSQL o equivalente per DDL, vincoli, query, join, funzioni aggregate, transazioni, isolamento, indici, ruoli e privilegi;
- fonte universitaria autorevole per modello relazionale, progettazione concettuale, dipendenze funzionali e normalizzazione;
- documentazione primaria per almeno una base documentale e una fonte comparativa autorevole sulle famiglie NoSQL;
- fonte istituzionale o standard tecnico per dimensioni e misurazione della qualità del dato;
- documentazione ufficiale per backup/ripristino e sicurezza, limitata ai concetti effettivamente sviluppati;
- bandi ufficiali del campione VOL-08 per validare profondità, prodotti nominati e formato delle prove.

Le nuove fonti devono essere trasformate in una source note consolidata e collegate al capitolo prima di sostenere claim specialistici. La documentazione già presente è sufficiente per il richiamo introduttivo, non per dichiarare completa normalizzazione, NoSQL, transazioni, indici, qualità e sicurezza.

## Topic, entity e quiz collegati

- `topics/database-e-sql.md` è pertinente ma ancora sintetico e orientato al VOL-01;
- `topics/informatica.md` fornisce il contesto generale;
- non risultano entity page specialistiche necessarie per il nucleo teorico;
- non risultano quiz consolidati specifici per normalizzazione, transazioni, indici, NoSQL e qualità;
- eventuali quiz nuovi dovranno essere verificati con le fonti tecniche e revisionati prima della pubblicazione.

## Review umane richieste

- database specialist o DBA: schema, normalizzazione, query, transazioni, indici e privilegi;
- docente di basi dati: progressione didattica, correttezza delle definizioni e adeguatezza del formalismo;
- specialista NoSQL: famiglie, compromessi e assenza di generalizzazioni improprie;
- data quality specialist: dimensioni, metriche, controlli e raccordo con il capitolo 10;
- responsabile editoriale: rispetto del delta con VOL-01 e dei confini con i capitoli 3, 6, 8, 9 e 10;
- responsabile del campione bandi: validazione della profondità concorsuale e dei DBMS eventualmente richiesti;
- revisore didattico: coerenza fra teoria, schema, query, caso, esercizi, quiz e orale;
- revisore fonti: granularità e tracciabilità delle fonti tecniche.

## Struttura proposta e budget KDP

# Basi dati, SQL/NoSQL e qualità del dato

## Obiettivo e confine con il VOL-01 — 170 parole

### Prerequisiti già coperti

### Il delta specialistico

## Mappa BANDO delle basi dati — 180 parole

### Nuclei, profondità e output

## Dal requisito al modello dei dati — 320 parole

### Modello, schema e istanza

### Entità, attributi e relazioni

## Il modello relazionale — 360 parole

### Tabelle, domini e chiavi

### Cardinalità e integrità referenziale

## Normalizzazione senza perdere il problema — 360 parole

### Anomalie e dipendenze

### Prima, seconda e terza forma normale

## SQL per interrogare e modificare — 560 parole

### Selezione, filtro e ordinamento

### Join, aggregazioni e sottoquery

### Inserimento, aggiornamento ed eliminazione

## Transazioni e concorrenza — 300 parole

### ACID, `COMMIT` e `ROLLBACK`

### Isolamento a livello concettuale

## Indici e prestazioni — 230 parole

### Che cosa accelera un indice

### Costi su scritture, spazio e manutenzione

## NoSQL: famiglie e criteri di scelta — 390 parole

### Chiave-valore, documentale, wide-column e grafo

### Relazionale o NoSQL?

## Qualità del dato nella base dati — 350 parole

### Dimensioni e regole misurabili

### Vincoli, validazione e deduplicazione

## Sicurezza, accessi e ripristino — 240 parole

### Ruoli e privilegi minimi

### Backup, audit e raccordi con i capitoli specialistici

## Caso guidato: pratiche, uffici e stati — 260 parole

## Domanda da commissario e domanda-trappola — 150 parole

## Errore tipico — 70 parole

## Mini-esercizi e quiz — 300 parole

## Checklist finale — 150 parole più tabella

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 90 parole

Budget orientativo: 3.900–4.200 parole, query, tabelle, schema ed esercizi inclusi. Il budget è coerente con la densità del nucleo e non include data governance, API, cybersecurity avanzata o amministrazione di prodotto.

## Criteri di approvabilità per lo step 09

- ogni elemento della specifica e della riga di matrice riceve teoria e verifica;
- il rinvio al VOL-01 resta preciso e limitato ai prerequisiti;
- modello concettuale, schema relazionale, chiavi e cardinalità sono distinti;
- normalizzazione collega forme normali e anomalie senza ridursi a etichette;
- ogni query usa uno schema dichiarato e viene spiegata;
- join, aggregazioni, `NULL` e modifiche massive includono almeno un errore tipico;
- ACID, transazioni e indici sono descritti senza costi assoluti o garanzie non contestualizzate;
- NoSQL è presentato per famiglie e requisiti, non come alternativa sempre superiore al relazionale;
- qualità del dato ha dimensioni, regole, metriche ed esempi tecnici;
- sicurezza e ripristino restano raccordi circoscritti ai capitoli competenti;
- schema, query, esercizi e soluzioni sono verificati manualmente;
- le fonti tecniche mancanti sono consolidate prima di introdurre claim specialistici;
- le review umane restano aperte finché non vengono realmente eseguite.
