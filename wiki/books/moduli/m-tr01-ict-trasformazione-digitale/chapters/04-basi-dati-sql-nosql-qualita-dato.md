---
id: chapter-m-tr01-04
type: book_chapter
title: "Basi dati, SQL/NoSQL e qualità del dato"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["basi dati", "sql", "nosql", "qualità dati"]
entities: ["PostgreSQL", "MongoDB"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/database-programmazione-formati-concorsi", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/basi-dati-sql-nosql-qualita-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.8
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: true
canonical: true
format_version: 2
dati_operativi: []
tags: ["chapter", "m-tr01", "database", "sql", "nosql", "qualita-dati"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 4
draft_stage: professional-draft
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/database-programmazione-formati-concorsi", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/basi-dati-sql-nosql-qualita-fonti-tecniche", "topics/database-e-sql", "topics/informatica", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-04-piano-completamento"]
---

# Basi dati, SQL/NoSQL e qualità del dato

La struttura di una base dati stabilisce quali informazioni si possono registrare, quali errori vengono bloccati e con quale difficoltà si ottiene una risposta. Nelle prove tecniche il candidato può dover leggere uno schema, scegliere una chiave, completare una query, riconoscere un’anomalia o motivare l’uso di un modello relazionale o NoSQL.

Il caso di riferimento segue la gestione delle pratiche di un ente. Lo stesso scenario collega requisiti, schema, query e controlli di qualità lungo tutto il capitolo.

## Obiettivo e confine con il VOL-01

Il VOL-01, capitolo 10, § 7, definisce database, DBMS, tabella, riga, colonna, chiave, relazione e query. Introduce anche i principali comandi SQL. Queste nozioni costituiscono i prerequisiti.

Dopo lo studio del capitolo dovrai saper:

- tradurre un requisito informativo in entità, attributi e relazioni;
- riconoscere chiavi, cardinalità e vincoli;
- diagnosticare anomalie e applicare la normalizzazione di base;
- leggere e scrivere query con filtri, join e aggregazioni;
- spiegare transazioni, proprietà ACID e isolamento;
- distinguere indice, chiave e vincolo;
- confrontare modello relazionale e principali famiglie NoSQL;
- definire controlli misurabili di qualità del dato;
- motivare ruoli e privilegi di accesso.

Le API e l’interoperabilità applicativa sono sviluppate nel capitolo 6. Cybersecurity, IAM e logging sono trattati nei capitoli 8 e 9. Ruoli di data governance, metadati, cataloghi e open data appartengono al capitolo 10.

## Mappa BANDO delle basi dati

| Passaggio | Domanda da porsi | Azione |
| --- | --- | --- |
| **B — Bando** | Sono richiesti concetti, SQL, modellazione o uno specifico DBMS? | Separare il nucleo generale dalla sintassi di prodotto. |
| **A — Aree** | La voce riguarda modello, query, transazioni, prestazioni, NoSQL, qualità o sicurezza? | Collocarla nell’area corretta. |
| **N — Nuclei** | Quale operazione devo spiegare o realizzare? | Preparare uno schema minimo e query verificabili. |
| **D — Diario** | L’errore nasce da modello, sintassi, cardinalità, dati o permessi? | Registrare causa, effetto e correzione. |
| **O — Output** | La prova chiede quiz, SQL, schema, orale o diagnosi? | Allenare il formato richiesto, non soltanto le definizioni. |

Se il bando nomina PostgreSQL, Oracle, SQL Server, MySQL o un prodotto NoSQL, affianca la relativa documentazione. Gli esempi del capitolo usano un sottoinsieme semplice di SQL e non presumono che ogni DBMS implementi nello stesso modo tutte le funzioni.

## N-TR01-04-01 · Dai requisiti al modello relazionale

Un **modello dei dati** stabilisce come rappresentare informazioni, relazioni, vincoli e operazioni. Lo **schema** descrive la struttura prevista; l’**istanza** è l’insieme dei dati presenti in un determinato momento.

Consideriamo questo requisito:

> Ogni pratica ha un identificativo, una data di presentazione, uno stato e un ufficio responsabile. Un ufficio gestisce più pratiche. Una pratica può riguardare più soggetti e uno stesso soggetto può comparire in più pratiche.

Le entità principali sono `Pratica`, `Ufficio` e `Soggetto`. Gli attributi descrivono le entità: per `Pratica`, per esempio, identificativo, data e stato. Le relazioni esprimono i collegamenti.

### Cardinalità

La **cardinalità** indica quante istanze possono partecipare a una relazione:

- uno-a-uno: a un’istanza corrisponde al massimo un’altra istanza;
- uno-a-molti: un ufficio può gestire molte pratiche, mentre ogni pratica ha un ufficio responsabile;
- molti-a-molti: una pratica può coinvolgere più soggetti e un soggetto può comparire in più pratiche.

Nel modello relazionale, una relazione molti-a-molti richiede normalmente una tabella associativa. `PraticaSoggetto` può contenere le chiavi di `Pratica` e `Soggetto`, oltre a eventuali attributi del collegamento, come il ruolo del soggetto nella pratica.

### Il modello relazionale

Il modello relazionale organizza i dati in relazioni, rappresentate operativamente come tabelle. Una riga, o **tupla**, descrive un’occorrenza; una colonna, o **attributo**, rappresenta una proprietà; il **dominio** delimita i valori ammessi.

Uno schema essenziale può essere descritto così:

```text
Ufficio(
    id_ufficio PK,
    nome UNIQUE
)

Pratica(
    id_pratica PK,
    data_presentazione,
    stato,
    id_ufficio FK → Ufficio.id_ufficio
)

Soggetto(
    id_soggetto PK,
    denominazione
)

PraticaSoggetto(
    id_pratica FK → Pratica.id_pratica,
    id_soggetto FK → Soggetto.id_soggetto,
    ruolo,
    PK(id_pratica, id_soggetto)
)
```

### Chiavi e vincoli

Una **chiave candidata** è un insieme minimo di attributi capace di identificare univocamente una riga. Fra le chiavi candidate se ne sceglie una come **chiave primaria**. Una chiave formata da più attributi è **composta**.

La **chiave esterna** collega una tabella a una chiave della tabella referenziata. Il vincolo impedisce, secondo le regole dichiarate, che una pratica faccia riferimento a un ufficio inesistente.

I vincoli hanno funzioni diverse:

| Vincolo | Funzione |
| --- | --- |
| `PRIMARY KEY` | identifica univocamente la riga e non ammette valori nulli |
| `FOREIGN KEY` | tutela il collegamento fra tabelle |
| `UNIQUE` | impedisce duplicati nella chiave dichiarata |
| `NOT NULL` | rende obbligatorio un valore |
| `CHECK` | impone una condizione sui valori |

`NULL` indica l’assenza o la non disponibilità di un valore, non il numero zero e non una stringa vuota. I confronti con valori nulli seguono una logica specifica: per verificarli si usa normalmente `IS NULL` o `IS NOT NULL`, non `= NULL`.

### Dal requisito allo schema

La modellazione parte dalle domande alle quali il sistema deve rispondere e dalle regole che non può violare. Da qui emergono le entità, cioè gli oggetti di interesse, e i loro attributi pertinenti. Relazioni e cardinalità diventano quindi tabelle, chiavi e vincoli. Partire direttamente dalle colonne rischia di incorporare nello schema abitudini dell’ufficio non dichiarate o dati che appartengono a concetti diversi.

La cardinalità esprime quante istanze possono partecipare a una relazione. Se un ufficio gestisce molte pratiche e ogni pratica appartiene a un solo ufficio, la relazione è uno-a-molti e la chiave esterna può stare in `Pratica`. Se una pratica coinvolge molti soggetti e un soggetto può comparire in molte pratiche, la relazione è molti-a-molti e richiede una tabella associativa. Questa tabella può avere attributi propri, come ruolo, data di partecipazione o ordine di firma: non è un semplice espediente tecnico.

Scegli la chiave valutando stabilità, unicità e semplicità d’uso. Un identificativo artificiale può evitare che cambiamenti di denominazione modifichino i collegamenti; una chiave naturale può invece esprimere una regola del dominio. La scelta non elimina la necessità di proteggere con `UNIQUE` gli altri identificatori che devono restare univoci. Nella prova, uno schema convincente dichiara anche l’opzionalità: una relazione obbligatoria richiede un vincolo diverso da una relazione che ammette temporaneamente l’assenza del collegamento.

## N-TR01-04-02 · Vincoli, `NULL` e normalizzazione

Una tabella unica con dati della pratica, nome dell’ufficio e tutti i soggetti ripetuti può sembrare comoda. Produce però ridondanza e anomalie:

- **inserimento**: non si può registrare un nuovo ufficio finché non esiste una pratica;
- **aggiornamento**: cambiare il nome di un ufficio richiede modifiche in molte righe;
- **cancellazione**: eliminando l’ultima pratica si può perdere anche l’unica informazione sull’ufficio.

La **normalizzazione** organizza le relazioni per ridurre dipendenze indesiderate e anomalie, preservando i collegamenti necessari.

### Prima forma normale

In **prima forma normale** ogni posizione contiene un valore appartenente al dominio previsto, non un elenco ripetuto nello stesso campo. Un campo `soggetti = "12, 18, 31"` rende difficili vincoli, join e aggiornamenti. La tabella `PraticaSoggetto` rappresenta ogni collegamento con una riga.

### Seconda forma normale

La **seconda forma normale** riguarda le tabelle con chiave composta: ogni attributo non chiave deve dipendere dall’intera chiave. In `PraticaSoggetto(id_pratica, id_soggetto, denominazione_soggetto, ruolo)`, la denominazione dipende soltanto da `id_soggetto`. Va quindi collocata in `Soggetto`.

### Terza forma normale

In **terza forma normale**, gli attributi non chiave non devono dipendere transitivamente dalla chiave attraverso un altro attributo non chiave. Se `Pratica` contenesse sia `id_ufficio` sia `nome_ufficio`, il nome dipenderebbe dall’identificativo dell’ufficio. Separare `Ufficio` evita ripetizioni.

Il progetto determina fin dove spingere la normalizzazione. Requisiti, carico e DBMS possono giustificare una denormalizzazione, purché sia motivata e accompagnata da controlli che mantengano coerenti le copie.

### Dipendenze e percorso di normalizzazione

Una **dipendenza funzionale** esprime che il valore di uno o più attributi determina il valore di altri. Nell’insieme delle pratiche, `id_ufficio` determina il nome dell’ufficio se ogni identificativo designa un solo ufficio. Riconoscere questa dipendenza spiega perché ripetere il nome in ogni pratica crea ridondanza: il dato dipende dall’ufficio, non dalla singola pratica.

Normalizzare significa analizzare le dipendenze, non dividere tabelle finché diventano piccole. Per ogni attributo si individua la chiave dalla quale dipende. La 1NF elimina gruppi ripetuti e valori multipli nella stessa posizione. La 2NF rimuove dipendenze soltanto da una parte di una chiave composta. La 3NF separa dipendenze transitive fra attributi non chiave. Ogni separazione conserva il collegamento mediante una chiave e deve permettere di ricostruire le informazioni necessarie con join corrette.

Considera `Assegnazione(id_pratica, id_dipendente, nome_dipendente, ruolo, nome_ufficio)`. Se la chiave è composta da pratica e dipendente, `nome_dipendente` dipende solo da `id_dipendente`: è un problema di 2NF. Se il dipendente appartiene a un ufficio e il nome dell’ufficio dipende dall’identificativo dell’ufficio, conservarlo nella stessa tabella introduce una dipendenza transitiva. Le tabelle `Dipendente`, `Ufficio` e `Assegnazione` rendono esplicite le responsabilità dei dati.

### Vincoli e dati già esistenti

Aggiungere un vincolo a una base popolata richiede una ricognizione. Se esistono chiavi duplicate, riferimenti orfani o stati fuori dominio, il DBMS può rifiutare il vincolo oppure l’amministratore può essere tentato di cancellare dati senza comprenderli. Il lavoro parte dalla misura delle anomalie, ne individua la causa, definisce una regola di correzione e conserva evidenza delle trasformazioni.

Anche `NULL` va deciso nel modello. Può significare dato non ancora noto, non applicabile o non acquisito: significati diversi che una sola rappresentazione rischia di confondere. Rendere un campo obbligatorio impedisce assenze future, ma non garantisce che il valore inserito sia vero. Vincoli strutturali, controlli applicativi e verifiche sul processo si completano a vicenda.

La denormalizzazione può ridurre join o sostenere letture frequenti, ma introduce copie da sincronizzare. La decisione richiede query critiche, volume, frequenza degli aggiornamenti, meccanismo di allineamento e controllo delle divergenze. “È più veloce” senza carico e misura non è una motivazione tecnica.

Dopo la trasformazione, collauda lo schema con inserimenti, aggiornamenti e cancellazioni rappresentativi. Il controllo verifica che i vincoli blocchino gli stati impossibili, che le join ricostruiscano l’informazione richiesta e che nessuna dipendenza significativa sia stata persa.

## N-TR01-04-03 · SQL per interrogare e modificare

SQL è un linguaggio dichiarativo: la query specifica il risultato richiesto, mentre il DBMS sceglie un piano di esecuzione compatibile.

### Selezione, filtro e ordinamento

```sql
SELECT id_pratica, data_presentazione, stato
FROM Pratica
WHERE stato = 'DA_VERIFICARE'
ORDER BY data_presentazione;
```

`SELECT` sceglie le colonne del risultato, `FROM` la sorgente, `WHERE` filtra le righe e `ORDER BY` ordina l’output. Senza `ORDER BY`, il risultato non ha un ordine stabile garantito.

Per cercare pratiche senza ufficio associato, se lo schema lo consente:

```sql
SELECT id_pratica
FROM Pratica
WHERE id_ufficio IS NULL;
```

### Join

Una join combina righe sulla base di una condizione:

```sql
SELECT p.id_pratica, p.stato, u.nome AS ufficio
FROM Pratica AS p
JOIN Ufficio AS u
  ON u.id_ufficio = p.id_ufficio
WHERE p.stato = 'DA_VERIFICARE';
```

La `INNER JOIN` restituisce le combinazioni che soddisfano la condizione. Una `LEFT JOIN` conserva tutte le righe della tabella a sinistra e completa con valori nulli quando non trova corrispondenza.

Una join errata o incompleta può moltiplicare le righe. Se una pratica è collegata a tre soggetti, la join con `PraticaSoggetto` produce tre righe per quella pratica. `DISTINCT` può eliminare duplicati dal risultato, ma non corregge automaticamente un modello o una condizione di join sbagliati.

### Aggregazioni

```sql
SELECT u.nome, COUNT(*) AS numero_pratiche
FROM Ufficio AS u
JOIN Pratica AS p
  ON p.id_ufficio = u.id_ufficio
GROUP BY u.nome
HAVING COUNT(*) >= 10
ORDER BY numero_pratiche DESC;
```

`GROUP BY` forma gruppi; `COUNT` calcola un valore per gruppo; `HAVING` filtra i gruppi dopo l’aggregazione. `WHERE`, invece, filtra le righe prima del raggruppamento.

### Sottoquery

Una sottoquery produce un risultato usato da un’altra query. Per individuare pratiche appartenenti a uffici selezionati:

```sql
SELECT id_pratica, stato
FROM Pratica
WHERE id_ufficio IN (
    SELECT id_ufficio
    FROM Ufficio
    WHERE nome LIKE 'Servizio%'
);
```

Join e sottoquery possono talvolta esprimere richieste equivalenti, ma leggibilità e piano di esecuzione dipendono dal caso e dal DBMS.

### Modifica dei dati

```sql
UPDATE Pratica
SET stato = 'ARCHIVIATA'
WHERE id_pratica = 1042;
```

```sql
DELETE FROM Pratica
WHERE id_pratica = 1042;
```

Omettere `WHERE` estende l’operazione a tutte le righe della tabella. Una modifica massiva richiede quindi il controllo preventivo della condizione, delle autorizzazioni, degli effetti dei vincoli e delle possibilità di ripristino.

### Semantica della query e cardinalità

Scrivere SQL significa prevedere il significato del risultato, oltre a produrre una sintassi valida. Prima della query si stabilisce quale unità rappresenta ogni riga attesa. Se l’output deve contenere una riga per ufficio, una join con pratiche e soggetti può moltiplicare le righe prima dell’aggregazione. Il conteggio dipende allora dalla domanda: pratiche, soggetti, collegamenti o valori distinti non sono la stessa misura.

L’ordine logico aiuta a leggere una query: si individuano sorgenti e join, si applicano i filtri sulle righe, si formano i gruppi, si calcolano le aggregazioni, si filtrano i gruppi e infine si ordina il risultato. Questa sequenza spiega perché una condizione su `COUNT(*)` appartiene normalmente a `HAVING`, mentre una condizione sullo stato della singola pratica appartiene a `WHERE`.

I valori nulli incidono sulle query. Una `INNER JOIN` esclude le righe prive di corrispondenza; una `LEFT JOIN` le conserva dal lato sinistro. Molte funzioni aggregate ignorano i valori nulli, mentre `COUNT(*)` conta le righe. Perciò `COUNT(colonna)` e `COUNT(*)` possono produrre risultati diversi. La risposta concorsuale deve dichiarare quale popolazione si vuole misurare.

### Modifiche controllate e portabilità

Prima di un `UPDATE` o `DELETE` significativo si può eseguire una `SELECT` con la stessa condizione, controllare il numero e il contenuto delle righe, quindi operare dentro una transazione quando il DBMS e il contesto lo consentono. I vincoli possono impedire una modifica oppure propagare effetti secondo regole configurate: queste conseguenze vanno comprese prima dell’esecuzione.

Il nucleo SQL del capitolo usa costrutti ampiamente condivisi, ma tipi, funzioni, gestione delle date, sintassi di limitazione dei risultati e dettagli delle transazioni possono variare. Se il bando nomina un prodotto, il candidato deve studiarne il dialetto e gli strumenti. La conoscenza generale resta utile per spiegare il procedimento e riconoscere ciò che dipende dall’implementazione.

## N-TR01-04-04 · Transazioni, concorrenza e indici

Una **transazione** raggruppa operazioni che devono essere trattate come un’unità. Se l’archiviazione di una pratica richiede sia l’aggiornamento dello stato sia la registrazione di un evento, non è accettabile salvare una sola delle due modifiche.

```sql
BEGIN;

UPDATE Pratica
SET stato = 'ARCHIVIATA'
WHERE id_pratica = 1042;

INSERT INTO EventoPratica(id_pratica, tipo_evento)
VALUES (1042, 'ARCHIVIAZIONE');

COMMIT;
```

Se una condizione impedisce di completare il lavoro, `ROLLBACK` annulla le modifiche della transazione non confermata.

Le proprietà **ACID** esprimono quattro obiettivi:

- **atomicità**: le operazioni riescono come unità oppure non producono effetti parziali;
- **consistenza**: la transazione porta la base dati da uno stato valido a un altro, nel rispetto dei vincoli dichiarati;
- **isolamento**: le transazioni concorrenti non devono interferire in modo incompatibile con il livello scelto;
- **durabilità**: dopo il commit, gli effetti devono sopravvivere ai guasti contemplati dal sistema.

I DBMS realizzano l’isolamento con livelli e meccanismi diversi, bilanciando concorrenza e fenomeni osservabili. In prova, la risposta parte dal problema: due operazioni simultanee possono leggere o modificare dati sovrapposti e richiedono un controllo adeguato al rischio.

### Indici e prestazioni

Un **indice** è una struttura ausiliaria che può permettere al DBMS di trovare determinate righe senza esaminare l’intera tabella. Può sostenere filtri, join o ordinamenti compatibili con la sua struttura.

Ogni indice comporta costi:

- occupa spazio;
- deve essere aggiornato quando cambiano i dati;
- può rallentare inserimenti e modifiche;
- non viene necessariamente usato per ogni query.

Una chiave primaria identifica una riga; un vincolo tutela una regola; un indice serve principalmente all’accesso. Un DBMS può creare indici per attuare alcuni vincoli, ma i concetti non sono sinonimi.

Le query reali guidano la progettazione degli indici. Un indice su `Pratica(stato)` può essere poco selettivo se quasi tutte le righe hanno lo stesso stato; un indice composto è utile solo per pattern compatibili. Le misure sul DBMS, sui dati e sul carico effettivi ne mostrano le prestazioni.

### Concorrenza e fenomeni osservabili

L’isolamento serve quando più transazioni lavorano sugli stessi dati. Senza garanzie adeguate, una transazione può leggere modifiche non ancora confermate, ottenere due risultati diversi ripetendo la stessa lettura oppure vedere comparire righe che prima non soddisfacevano una condizione. I DBMS descrivono questi fenomeni e offrono livelli di isolamento, ma il comportamento concreto dipende dal prodotto e dal meccanismo di concorrenza.

Un isolamento più forte non è gratuito: può aumentare attese, conflitti o annullamenti. La scelta parte dal rischio del processo. Per assegnare una risorsa unica, perdere un aggiornamento può essere inaccettabile; per una statistica esplorativa può essere tollerabile una vista meno rigida. Il candidato deve collegare la garanzia al requisito, evitando di presentare il livello massimo come soluzione automatica per ogni carico.

Anche una transazione ben delimitata deve gestire gli errori. Dopo un’eccezione, l’applicazione deve sapere se annullare, riprovare o segnalare l’operazione. I tentativi ripetuti richiedono attenzione: un comando non progettato per essere ripetuto può duplicare effetti. La registrazione dell’esito e l’identificazione univoca dell’operazione aiutano a distinguere un nuovo evento dalla ripetizione dello stesso.

### Scegliere e verificare un indice

La scelta di un indice nasce da query concrete: colonne usate nei filtri, nelle join, negli ordinamenti e nelle aggregazioni; selettività dei valori; frequenza di letture e scritture. In un indice composto conta anche l’ordine delle colonne, perché non tutte le combinazioni di ricerca sfruttano allo stesso modo la struttura. Inserire molti indici “per sicurezza” aumenta spazio e lavoro di manutenzione e può confondere l’ottimizzatore.

Il piano di esecuzione mostra come il DBMS intende accedere ai dati: scansioni, indici, join e stime. È una previsione legata a statistiche, parametri, distribuzione dei valori e volume, tutti fattori che possono cambiare la scelta. La verifica professionale confronta piano previsto, misure e carico rappresentativo. In una prova basta spiegare che un indice è candidato quando sostiene un pattern frequente e selettivo; il contesto reale ne dimostrerà l’utilità.

## N-TR01-04-05 · Famiglie NoSQL e criteri di scelta

**NoSQL** raccoglie modelli non riconducibili a un’unica struttura relazionale. Non significa “senza query” né “senza schema”: anche un modello flessibile richiede decisioni su struttura, identificazione, validazione e accesso.

| Famiglia | Rappresentazione prevalente | Uso concettuale |
| --- | --- | --- |
| chiave-valore | associazione chiave → valore | accesso diretto mediante una chiave |
| documentale | documenti con campi e strutture annidate | dati aggregati letti spesso insieme |
| wide-column | righe con famiglie di colonne | grandi volumi distribuiti e accessi orientati alla chiave |
| grafo | nodi, archi e proprietà | relazioni e percorsi complessi |

Nel modello documentale, dati collegati possono essere incorporati nello stesso documento oppure referenziati. L’incorporamento riduce alcune letture multiple e può rendere atomico l’aggiornamento di un aggregato, ma può anche duplicare informazioni o produrre documenti difficili da gestire. I pattern di accesso e aggiornamento determinano quale soluzione è adatta.

### Relazionale o NoSQL?

Il confronto può partire da queste domande:

- le relazioni e i vincoli sono centrali?
- i dati hanno struttura stabile o molto variabile?
- quali elementi vengono letti e aggiornati insieme?
- servono join articolate o attraversamenti di relazioni?
- quali garanzie di consistenza richiede il processo?
- quali volumi, distribuzione e tempi di risposta sono previsti?

La velocità o la capacità di scala non derivano dall’etichetta “documentale” o “relazionale”. Vanno valutate rispetto al modello, all’implementazione, ai dati e al carico.

### Aggregati, riferimenti e aggiornamenti

Nel modello documentale conviene individuare l’**aggregato**, cioè l’insieme di dati che viene letto e aggiornato come unità. Incorporare nello stesso documento informazioni usate insieme può semplificare alcune operazioni. Se però lo stesso dato è condiviso da molti documenti e cambia spesso, la duplicazione rende più difficile mantenere coerenza. Il riferimento separa le informazioni, ma può richiedere più letture o elaborazioni applicative.

La scelta fra incorporare e referenziare dipende quindi dalla direzione delle relazioni, dalla frequenza degli aggiornamenti e dalle garanzie richieste. Una relazione uno-a-pochi stabile può adattarsi all’incorporamento; una relazione molti-a-molti con entità autonome suggerisce spesso riferimenti. Non è una regola assoluta: il modello va provato sui casi d’uso principali.

Le altre famiglie rispondono a esigenze diverse. Un archivio chiave-valore privilegia l’accesso mediante chiave e non offre automaticamente interrogazioni ricche sul contenuto. Un sistema wide-column organizza grandi insiemi distribuiti attorno a chiavi e famiglie di colonne. Una base a grafo rende centrali relazioni e attraversamenti. Chiamarle tutte “NoSQL” non cancella le differenze di modello, query e consistenza.

### Consistenza e distribuzione

In un sistema distribuito, replica e partizionamento introducono decisioni su dove si trovano i dati, come vengono aggiornate le copie e che cosa può osservare un client durante un guasto o un ritardo. Formule come “NoSQL è eventualmente consistente” sono troppo generiche: prodotti e configurazioni possono offrire garanzie differenti, talvolta selezionabili per operazione.

Stabilisci quale anomalia il processo può tollerare. Una vista statistica può accettare un breve ritardo; l’assegnazione esclusiva di una pratica richiede regole più forti. Anche il modello relazionale può essere distribuito, e un database documentale può offrire transazioni: le etichette non sostituiscono l’analisi delle garanzie effettive. La decisione dipende dal comportamento richiesto in lettura, scrittura e durante i guasti.

### Una decisione verificabile

Per motivare la tecnologia, il candidato può costruire una matrice: struttura dei dati, relazioni, operazioni dominanti, volumi, distribuzione, consistenza, latenza, evoluzione dello schema, competenze e gestione. Ogni requisito deve collegarsi a una conseguenza progettuale. Se servono vincoli forti e join articolate, il modello relazionale è un candidato naturale; se l’unità di lettura è un documento variabile e autonomo, un modello documentale può ridurre trasformazioni.

Un sistema può affiancare al database relazionale un motore specializzato per ricerca, cache o relazioni complesse. L’architettura ibrida aumenta però integrazione, monitoraggio, backup e competenze necessarie. La pluralità di strumenti ha senso quando un requisito misurabile giustifica il costo operativo aggiuntivo e quando il gruppo sa gestire consistenza, errori e ripristino fra componenti diversi.

## N-TR01-04-06 · Qualità, accessi e output concorsuale

Un dato è di qualità quando è adeguato allo scopo dichiarato. Non esiste una qualità astratta e perfetta: occorrono dimensioni, regole, metriche e soglie motivate.

| Dimensione | Domanda | Controllo possibile |
| --- | --- | --- |
| accuratezza | il valore rappresenta correttamente il fenomeno? | confronto con fonte autorevole o campionamento |
| completezza | i valori necessari sono presenti? | percentuale di campi obbligatori valorizzati |
| coerenza | valori collegati rispettano le stesse regole? | controlli incrociati e integrità referenziale |
| validità | il dato rispetta formato, dominio e regole? | tipo, `CHECK`, elenco ammesso |
| unicità | la stessa entità è registrata più volte? | chiavi, regole di matching e deduplicazione |
| tempestività | il dato è aggiornato entro il tempo utile? | differenza fra evento e aggiornamento |

Una regola operativa deve essere verificabile. “Lo stato deve essere corretto” è vago; “lo stato appartiene all’insieme `PRESENTATA`, `IN_ISTRUTTORIA`, `CHIUSA`” è controllabile.

I vincoli del DBMS prevengono alcuni errori, ma non garantiscono l’accuratezza del mondo reale. Una data formalmente valida può essere associata alla pratica sbagliata. Servono quindi controlli all’ingresso, riconciliazioni, gestione delle anomalie e responsabilità definite. Il capitolo 10 sviluppa questi aspetti nel ciclo di governance.

Per ogni regola di qualità specifica popolazione osservata, formula, frequenza di misura e azione conseguente. Per esempio, la completezza dei campi obbligatori può essere espressa come rapporto fra pratiche complete e pratiche esaminate in un intervallo dichiarato. Il valore acquista significato quando sono definiti i campi obbligatori, il momento della rilevazione e la soglia che attiva una verifica.

Collega la misura alla causa. Un’anomalia può derivare dal modello, da una validazione assente, da un’importazione, da un processo manuale o da una fonte esterna. Correggere le sole righe senza intervenire sull’origine produce recidive. Il ciclo tecnico comprende rilevazione, classificazione, correzione controllata, prevenzione e nuova misura. Ogni passaggio deve lasciare evidenza sufficiente a spiegare che cosa è cambiato e perché.

### Sicurezza, accessi e ripristino

Il DBMS deve permettere soltanto le operazioni necessarie al ruolo. Un utente che produce statistiche può ricevere `SELECT` senza poter cancellare righe; un servizio applicativo può ottenere privilegi su un insieme circoscritto di oggetti.

Il **principio del privilegio minimo** riduce l’impatto di errori e abusi. Proprietà degli oggetti, ruoli, concessione e revoca dei privilegi devono essere documentati. Autenticazione, autorizzazione, cifratura, audit, backup e ripristino concorrono alla protezione, ma rispondono a problemi distinti.

Il backup non equivale alla disponibilità immediata e non dimostra da solo la possibilità di recupero. Un ripristino controllato mette alla prova le procedure. I capitoli 8 e 9 approfondiscono rischio, IAM e logging; il capitolo 7 tratta continuità e infrastruttura.

### Caso guidato: diagnosticare una base dati delle pratiche

Un ufficio conserva una tabella con queste colonne:

```text
id_pratica | stato | id_ufficio | nome_ufficio | soggetti
```

La colonna `soggetti` contiene identificativi separati da virgole. Il nome dell’ufficio è ripetuto in ogni pratica. Alcune righe hanno uno stato non previsto.

La diagnosi procede così:

1. separare `Ufficio` da `Pratica`, collegandole con una chiave esterna;
2. creare `Soggetto` e `PraticaSoggetto` per la relazione molti-a-molti;
3. definire un dominio o un vincolo per gli stati ammessi;
4. scegliere chiavi che impediscano duplicati;
5. migrare e validare i dati, senza eliminare silenziosamente le anomalie;
6. aggiungere indici soltanto dopo aver esaminato le query;
7. misurare completezza, validità e unicità dopo la migrazione.

La normalizzazione corregge la struttura, ma non rende automaticamente esatti i dati già presenti. Le anomalie devono essere classificate, corrette quando possibile e tracciate.

### Domanda da commissario

**Come progetterebbe una base dati per gestire pratiche e uffici?**

Partirei dai requisiti, individuando entità, attributi, relazioni e cardinalità. Userei chiavi stabili, una chiave esterna per il rapporto uno-a-molti e una tabella associativa per le relazioni molti-a-molti. Dopo la verifica delle anomalie definirei vincoli e transazioni; query e indici verrebbero progettati sul carico reale. Infine aggiungerei regole di qualità e privilegi coerenti con i ruoli.

### Domanda-trappola

**Una base NoSQL non richiede uno schema?**

No. Può consentire una struttura più flessibile o demandare parte della validazione all’applicazione, ma campi, identificatori, relazioni, documenti incorporati, regole di accesso e pattern di aggiornamento devono comunque essere progettati. “Schema flessibile” non significa “assenza di modello”.

### Errore tipico

Usare `DISTINCT` per nascondere righe duplicate prodotte da una join errata. Prima di eliminare duplicati dal risultato, controlla cardinalità, condizione di join e significato delle righe. Più righe possono essere corrette se rappresentano collegamenti diversi.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento consente di verificare la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-04-01` | Esercizio 1 — Schema |
| `N-TR01-04-02` | Quiz 3 |
| `N-TR01-04-03` | Esercizio 2 — Query |
| `N-TR01-04-04` | Quiz 5 |
| `N-TR01-04-05` | Quiz 6 |
| `N-TR01-04-06` | Caso guidato: diagnosticare una base dati |

## ▣ Verifica

### Esercizio 1 — Schema

Un dipendente può partecipare a più progetti e ogni progetto può coinvolgere più dipendenti. Proponi le tabelle minime.

**Soluzione:** `Dipendente`, `Progetto` e una tabella associativa `DipendenteProgetto`, con chiave composta dalle due chiavi esterne. Eventuali attributi come ruolo o data di assegnazione appartengono alla relazione.

### Esercizio 2 — Query

Scrivi una query che restituisca il numero di pratiche per stato, mostrando soltanto gli stati con almeno cinque pratiche.

```sql
SELECT stato, COUNT(*) AS numero_pratiche
FROM Pratica
GROUP BY stato
HAVING COUNT(*) >= 5
ORDER BY numero_pratiche DESC;
```

`HAVING` filtra i gruppi prodotti da `GROUP BY`.

### Esercizio 3 — Diagnosi

Una transazione aggiorna lo stato della pratica, poi fallisce prima di registrare l’evento associato. Quale proprietà è a rischio?

**Soluzione:** l’atomicità. Le operazioni devono essere confermate insieme oppure annullate.

### Quiz 1

Quale affermazione è corretta?

- A. Una chiave esterna accelera sempre ogni query.
- B. `WHERE` filtra i gruppi dopo `GROUP BY`.
- C. Un indice può accelerare letture ma introduce costi di manutenzione.
- D. `NULL` equivale sempre a zero.

**Risposta corretta: C.** A confonde vincolo e prestazione; B descrive `HAVING`; D confonde assenza del valore e valore numerico.

### Quiz 2

Quale situazione indica una relazione molti-a-molti?

- A. Ogni pratica appartiene a un solo ufficio e un ufficio gestisce molte pratiche.
- B. Ogni dipendente può lavorare su più progetti e ogni progetto può coinvolgere più dipendenti.
- C. Ogni ufficio ha un solo identificativo.
- D. Ogni pratica ha una sola data di presentazione.

**Risposta corretta: B.** La partecipazione è multipla in entrambe le direzioni e richiede normalmente una tabella associativa. A descrive una relazione uno-a-molti; C e D descrivono attributi o vincoli, non una relazione molti-a-molti.

### Quiz 3

Quale dipendenza segnala un problema di seconda forma normale in una tabella con chiave composta?

- A. Un attributo non chiave dipende dall’intera chiave.
- B. Un attributo non chiave dipende soltanto da una parte della chiave.
- C. La chiave primaria non ammette valori nulli.
- D. Una chiave esterna riferisce un’altra tabella.

**Risposta corretta: B.** La 2NF richiede che gli attributi non chiave dipendano dall’intera chiave composta. A è la condizione desiderata; C e D riguardano vincoli diversi.

### Quiz 4

Quale clausola filtra i gruppi dopo il calcolo di un’aggregazione?

- A. `WHERE`.
- B. `ORDER BY`.
- C. `HAVING`.
- D. `FROM`.

**Risposta corretta: C.** `HAVING` applica condizioni ai gruppi e può usare risultati aggregati. `WHERE` filtra le righe prima del raggruppamento; `ORDER BY` ordina il risultato; `FROM` indica le sorgenti.

### Quiz 5

Una procedura aggiorna lo stato di una pratica e registra un evento, ma deve evitare che resti salvata una sola operazione. Quale proprietà è centrale?

- A. Atomicità.
- B. Selettività.
- C. Normalizzazione.
- D. Indicizzazione.

**Risposta corretta: A.** L’atomicità tratta le operazioni come un’unità: tutte confermate oppure tutte annullate. Le altre risposte riguardano prestazioni o struttura dei dati.

### Quiz 6

Quale affermazione sui modelli NoSQL è corretta?

- A. Tutti eliminano la necessità di progettare lo schema.
- B. Tutti offrono le stesse query e garanzie di consistenza.
- C. Comprendono famiglie diverse, da valutare rispetto a dati e pattern di accesso.
- D. Sono sempre preferibili quando il volume dei dati cresce.

**Risposta corretta: C.** Chiave-valore, documentale, wide-column e grafo adottano modelli e operazioni differenti. Flessibilità, scala o consistenza non derivano automaticamente dall’etichetta NoSQL.

## Checklist finale

| Competenza | Riconosco | Spiego | Applico |
| --- | --- | --- | --- |
| Distinguere modello, schema e istanza | ☐ | ☐ | ☐ |
| Individuare entità, attributi e cardinalità | ☐ | ☐ | ☐ |
| Usare chiavi e vincoli | ☐ | ☐ | ☐ |
| Diagnosticare anomalie di normalizzazione | ☐ | ☐ | ☐ |
| Scrivere filtri, join e aggregazioni | ☐ | ☐ | ☐ |
| Spiegare transazioni e ACID | ☐ | ☐ | ☐ |
| Distinguere indice, chiave e vincolo | ☐ | ☐ | ☐ |
| Confrontare relazionale e NoSQL | ☐ | ☐ | ☐ |
| Definire una regola di qualità misurabile | ☐ | ☐ | ☐ |
| Motivare ruoli e privilegi | ☐ | ☐ | ☐ |

## Da sapere in 5 righe

- Il modello traduce requisiti in strutture, relazioni e vincoli.
- La normalizzazione riduce ridondanza e anomalie.
- SQL interroga e modifica dati; join e aggregazioni richiedono cardinalità chiare.
- Transazioni e indici risolvono problemi diversi e comportano compromessi.
- NoSQL e qualità si valutano rispetto a scopo, dati, accessi e controlli.

## Riferimenti professionali essenziali

- *Il Metodo BANDO*, capitolo 10, paragrafo 7, per i prerequisiti su database, tabelle, chiavi e SQL elementare.
- Documentazione ufficiale PostgreSQL per query, vincoli, transazioni, controllo della concorrenza, indici, ruoli e privilegi.
- Documentazione ufficiale MongoDB per modello documentale, incorporamento, riferimenti e operazioni sui documenti.
- NIST Dictionary of Algorithms and Data Structures e materiali universitari di basi dati per terminologia, modelli e strutture.
- Programma del singolo bando e documentazione del DBMS nominato, necessari per dialetto, profondità e strumenti specifici della prova.
