---
id: chapter-m-tr01-10
type: book_chapter
title: "Data governance, open data, interoperabilità e qualità"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["data governance", "open data", "qualità dati", "metadati", "interoperabilità"]
entities: ["AgID", "Unione europea", "PDND", "dati.gov.it"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/data-governance-open-data-interoperabilita-fonti-primarie", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026", "sources/ingegneria-software-api-interoperabilita-fonti-tecniche", "sources/basi-dati-sql-nosql-qualita-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "vol-08-ict-digitale-cybersecurity-dati"]
confidence: 0.89
updated_at: 2026-08-11
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01", "data-governance", "open-data", "interoperabilita"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 10
draft_stage: format-2-draft
format_version: 2
dati_operativi: []
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/data-governance-open-data-interoperabilita-fonti-primarie", "topics/data-governance-qualita-metadati-open-data", "planning/08-capitolo-10-piano-completamento"]
---

# Data governance, open data, interoperabilità e qualità

Un'amministrazione può possedere molti archivi e continuare a non sapere quale sia il dato affidabile, chi ne decida il significato e quale uso sia consentito. Quando il codice di una pratica cambia in un applicativo ma non nell'altro, il problema non è soltanto tecnico: può produrre istruttorie lente, pagamenti errati o risposte incoerenti al cittadino. Governare i dati significa rendere queste decisioni esplicite, verificabili e ripetibili.

## Obiettivo didattico

Al termine del capitolo saprai distinguere governo, gestione e architettura del dato; assegnare ruoli e responsabilità; progettare inventario, glossario e scheda dataset; trasformare un difetto in una regola di qualità; distinguere open data, trasparenza, accesso e interoperabilità. Saprai inoltre argomentare perché uno scambio tra enti e una pubblicazione per il riuso richiedono valutazioni diverse.

## Mappa BANDO: governare il dato

- **B — Base:** finalità, dominio, fonte e significato del dato.
- **A — Attori:** chi decide, chi cura, chi custodisce e chi usa.
- **N — Nodi:** qualità, classificazione, diritti, dipendenze e limiti.
- **D — Documenti:** inventario, glossario, scheda dataset, regole e decisioni.
- **O — Output:** uso interno, scambio autorizzato, e-service o distribuzione aperta.

## Spiegazione teorica

Ogni scelta sul dato deve collegare significato, finalità, responsabilità, controllo e conseguenza. I nuclei del capitolo mostrano come rendere questa catena verificabile nel lavoro dell'ente e nella risposta concorsuale.

## N-TR01-10-01 · Il dato come asset informativo e le decisioni di governo
### Dalla decisione al servizio

Un asset informativo va letto anche per le sue conseguenze: se una definizione cambia, possono cambiare calcoli, comunicazioni, indicatori, controlli e servizi collegati. Per questo la governance individua il dominio, stabilisce una fonte autorevole quando occorre risolvere un conflitto e rende visibile la versione valida. L'obiettivo non è centralizzare ogni decisione, ma evitare che ciascun ufficio costruisca una propria verità senza dichiararlo.

Un esempio utile riguarda l'indirizzo del richiedente. Il dato può essere usato per comunicazioni, istruttoria territoriale o statistiche aggregate; questi usi richiedono livelli diversi di aggiornamento, accesso e verifica. Il governo del dato esplicita tale differenza prima che l'applicativo la nasconda dietro un unico campo. Quando la stessa informazione alimenta più servizi, l'ente deve valutare effetto, priorità e dipendenze della modifica.

In una risposta scritta, distingui sempre principio e realizzazione. Dire che serve una piattaforma è insufficiente se non si indica quale decisione la piattaforma debba sostenere e quale evidenza permetta di controllarla. Un candidato mostra maturità quando collega definizione, responsabilità, controllo ed esito per il cittadino.

Un dato è una rappresentazione elementare: una data, un codice, un indirizzo, un importo. Diventa informazione quando qualcuno conosce il contesto in cui leggerlo. Il valore `CHIUSA`, per esempio, non è utile se non si sa quale procedimento descriva, chi l'abbia aggiornato e se indichi l'adozione del provvedimento, l'invio della comunicazione o il pagamento concluso. Un dataset è una raccolta organizzata di dati con struttura e significato definiti; un dominio riunisce dataset collegati a un ambito, come tributi, personale o occupazioni di suolo pubblico.

Parlare di dato come asset informativo non significa attribuirgli un prezzo automatico. Significa riconoscere che il dato sostiene decisioni, servizi, controlli e diritti, quindi richiede responsabilità paragonabili a quelle applicate agli altri beni necessari al funzionamento dell'ente. Un dato senza proprietario semantico può essere tecnicamente disponibile e insieme inutilizzabile: due uffici possono impiegare la stessa parola con definizioni incompatibili, oppure una procedura può conservare un identificativo che nessun servizio considera autorevole.

La data governance stabilisce chi decide sul dominio, con quali principi e attraverso quali evidenze. Riguarda finalità, usi ammessi, definizioni, priorità, qualità, classificazione, condivisione e dismissione. La gestione operativa esegue le decisioni: acquisisce, corregge, conserva, distribuisce e controlla. L'architettura descrive sistemi, modelli, flussi, interfacce e dipendenze. Sono piani collegati ma non equivalenti. La governance può stabilire che il codice pratica sia un identificativo unico; la gestione elimina i duplicati; l'architettura realizza il vincolo o il controllo nel servizio.

Un buon governo non impone lo stesso apparato documentale a ogni foglio di calcolo. Parte da rischio, impatto e riuso. Un dataset che alimenta un pagamento, un indicatore pubblico o un servizio rivolto a molte persone richiede definizioni, controlli e responsabilità più robuste di un elenco temporaneo usato da un singolo ufficio. La proporzionalità non è un permesso per restare vaghi: richiede di motivare perché una regola, un controllo o una revisione sono adeguati allo scopo.

Le decisioni diventano affidabili quando lasciano traccia. Una policy, una definizione approvata, un esito di controllo, una richiesta di accesso, una versione della scheda o una decisione di dismettere una distribuzione sono evidenze diverse. Non servono a costruire burocrazia aggiuntiva; permettono di ricostruire perché il dato è stato usato in un certo modo e di correggere un errore senza affidarsi alla memoria delle persone. Il Piano Triennale per l'informatica nella PA richiama proprio il legame tra organizzazione, processi, qualità dei dati e servizi digitali.

**Errore tipico:** confondere la governance con il possesso del database. L'amministratore tecnico custodisce un sistema; non può decidere da solo un nuovo uso di dati o il significato istituzionale di un campo.

**Uso in prova:** davanti a una domanda generica, parti da finalità e dominio, poi spiega decisione, attuazione ed evidenza. Questa sequenza evita una risposta ridotta a strumenti o sigle.

## N-TR01-10-02 · Ruoli, decisioni, RACI ed evidenze
### Come assegnare responsabilità senza creare etichette vuote

Una mappa di ruoli parte dalle decisioni ricorrenti: chi approva una definizione, chi autorizza un nuovo fruitore, chi valuta un difetto di qualità, chi cambia la frequenza di aggiornamento, chi sospende una distribuzione. Solo dopo si collegano persone o uffici alle funzioni. Questo ordine evita che la matrice RACI diventi un organigramma cosmetico, pieno di sigle ma incapace di risolvere un conflitto reale.

Prendi il caso di un campo usato da tributi e polizia locale. Se il produttore segnala che il valore non è più attendibile, lo steward raccoglie l'anomalia e verifica la regola; l'owner valuta impatto e priorità; il custodian applica la correzione tecnica; i fruitori ricevono la comunicazione sulle conseguenze. Se invece si deve ampliare l'uso del campo a un nuovo servizio, intervengono anche processo, privacy e sicurezza. La stessa persona può partecipare a più passaggi, ma le evidenze devono mostrare quale funzione ha svolto.

Le responsabilità devono essere comprensibili anche in caso di assenza, cambio di personale o affidamento a un fornitore. Perciò la documentazione indica funzione, recapito organizzativo, sostituzione e momento di riesame. Un contratto esterno può affidare attività tecniche, ma non cancella il dovere dell'ente di governare finalità e controlli.

I nomi data owner, data steward e data custodian descrivono funzioni organizzative frequenti. Non sono qualifiche giuridiche automaticamente obbligatorie né sostituiscono gli incarichi previsti dalla normativa. Sono utili se chiariscono chi può decidere, chi cura il significato e chi assicura l'attuazione tecnica. In un ente piccolo una persona può svolgere più funzioni; ciò non elimina la necessità di separare le decisioni dalle attività che le eseguono.

Il data owner presidia le decisioni sul dominio: finalità, priorità di qualità, usi consentiti, definizioni rilevanti e autorizzazioni organizzative. Deve conoscere il processo amministrativo cui il dato si riferisce. Il data steward cura il linguaggio comune, i metadati, le regole di qualità, le eccezioni e il dialogo tra uffici. Il custodian assicura disponibilità, backup, protezione, configurazioni e attuazione tecnica degli accessi. Il produttore crea o acquisisce il dato; il fruitore lo utilizza entro le autorizzazioni ricevute; il responsabile del servizio presidia l'erogazione verso utenti e altri uffici.

Queste funzioni si raccordano con RTD, responsabili di processo, sicurezza, DPO, trasparenza, archivio e procurement secondo le rispettive competenze. Il DPO non autorizza per definizione ogni trattamento; la funzione sicurezza non decide da sola la finalità; il tecnico non stabilisce il significato amministrativo. Quando sono coinvolti dati personali, accessi o diffusione, il confronto tra ruoli è necessario, ma ciascuno deve contribuire alla domanda che gli compete.

Una matrice RACI può rendere leggibile la distribuzione. R significa chi svolge l'attività; A chi risponde della decisione; C chi deve essere consultato; I chi deve essere informato. Il modello non vale perché ha quattro lettere: serve quando è collegato a una decisione concreta e a una prova dell'esecuzione. Per la definizione di “occupazione attiva”, ad esempio, l'owner approva il significato, lo steward cura il glossario, il custodian applica la modifica nei sistemi e gli uffici interessati sono informati.

| Decisione | Responsabilità di governo | Cura operativa | Evidenza utile |
| --- | --- | --- | --- |
| definizione di un campo | owner | steward | glossario approvato |
| regola di completezza | owner | steward | specifica e risultato del controllo |
| accesso tecnico | owner autorizza | custodian attua | richiesta, autorizzazione e log |
| distribuzione aperta | funzione competente | gruppo multidisciplinare | valutazione, metadati e licenza |

La responsabilità non si esaurisce con la prima assegnazione. Un cambio di processo, fornitore, sistema o finalità può rendere inadeguata una vecchia matrice. Perciò occorre prevedere riesami e un canale per le eccezioni: un'anomalia segnalata senza assegnatario resta soltanto un'informazione, non diventa un rimedio.

**Errore tipico:** usare owner e steward come sinonimi. Il primo decide sul dominio; il secondo rende applicabili e controllabili le decisioni. In prova è preferibile descrivere la funzione invece di attribuire titoli non previsti nell'ente.

**Applicazione:** costruisci una riga “decisione–responsabile–evidenza” prima di disegnare un organigramma. Mostra subito che sai collegare responsabilità e controllabilità.

## N-TR01-10-03 · Ciclo di vita, classificazione e lineage
### Il dato cambia prima del database e dopo l'uso

Ogni fase del ciclo deve avere un punto di ingresso e uno di uscita riconoscibile. L'acquisizione registra una fonte; la validazione decide se un record può essere usato; la trasformazione produce una nuova versione; la condivisione individua destinatari; l'archiviazione modifica disponibilità e tempi di recupero; la dismissione interrompe accessi e dipendenze. Questa lettura aiuta a evitare che un cambiamento apparentemente locale si propaghi in moduli, cruscotti e comunicazioni.

Il lineage è particolarmente utile quando due risultati non coincidono. Non si parte accusando l'altro ufficio di avere dati sbagliati: si confrontano definizione, fonte, data di estrazione, trasformazioni e regole applicate. Può emergere che una tabella usi la data di protocollo e l'altra la data di conclusione, oppure che una riconciliazione sia avvenuta solo in uno dei due sistemi. La causa diventa così discutibile e correggibile.

La classificazione va aggiornata quando cambiano contenuto, destinatari o contesto. Un dataset interno può contenere un estratto idoneo alla pubblicazione solo dopo una nuova valutazione; una distribuzione precedentemente aperta può richiedere sospensione se cambia la composizione. La governance registra queste decisioni, ne individua il responsabile e stabilisce come informare i fruitori.

Il ciclo di vita del dato inizia prima dell'inserimento nel database. Nella fase di pianificazione si chiariscono finalità, fonte, dati necessari, durata, formati, classificazione e controlli iniziali. Raccogliere informazioni “perché potrebbero servire” aumenta costi, errori e rischi. La domanda corretta è: quali dati servono a questo processo, con quale significato, per quanto tempo e con quale livello di affidabilità?

Nella creazione o acquisizione si registrano origine, data, responsabile e regole di validazione. Nella trasformazione possono cambiare struttura, codici o granularità: una lista di pratiche diventa un indicatore; più fonti vengono riconciliate; un archivio produce una distribuzione. Senza traccia di tali passaggi, un risultato non è verificabile. Il lineage ricostruisce provenienza e trasformazioni: non coincide con un diagramma tecnico completo, ma consente di capire da quale fonte deriva un campo, quale versione è stata applicata e quali dataset dipendono da esso.

Validazione, uso e condivisione sono fasi diverse. Validare controlla che i dati rispettino regole definite; usare interno richiede che gli addetti siano autorizzati e che la finalità sia pertinente; condividere con un altro soggetto richiede di definire destinatari, attributi, responsabilità e condizioni. La disponibilità tecnica di un archivio non rende automatico alcun passaggio. In particolare, il principio once only mira a evitare richieste ripetute di informazioni già disponibili, ma non autorizza accessi indiscriminati.

La classificazione accompagna l'intero ciclo. Un dataset può essere pubblico, interno o riservato; può contenere dati personali, informazioni soggette a limitazioni o dati la cui diffusione danneggerebbe la sicurezza o interessi di terzi. La classificazione non è un'etichetta decorativa: orienta accessi, canali, misure, conservazione e valutazione di eventuale pubblicazione. Pseudonimizzazione, anonimizzazione e aggregazione non sono sinonimi. La pseudonimizzazione riduce il collegamento immediato alla persona ma conserva la possibilità di riconnessione con informazioni aggiuntive; l'anonimizzazione richiede una valutazione più rigorosa del rischio di reidentificazione.

La conservazione comprende archivi principali, copie, estratti, cache e dataset derivati. Dismettere una tabella lasciando una replica usata per elaborazioni periodiche non conclude il ciclo. Occorre individuare dipendenze, stabilire cosa archiviare o cancellare secondo la disciplina applicabile e verificare l'esito. Una dismissione ben governata produce un'evidenza: chi ha deciso, che cosa è stato dismesso, quali servizi sono stati aggiornati e quale accesso deve cessare.

**Errore tipico:** considerare il lineage una funzione riservata ai data engineer. Anche il candidato che non progetta pipeline deve saper chiedere origine, trasformazioni, versioni e dipendenze prima di fidarsi di un indicatore.

**Uso in prova:** per descrivere il ciclo di vita, collega ogni fase a una domanda: perché raccogliamo, da dove arriva, chi controlla, chi usa, cosa condividiamo, quanto conserviamo e come dismettiamo.

## N-TR01-10-04 · Inventario, catalogo, glossario e metadati
### Metadati che aiutano davvero a decidere

Un metadato utile risponde a una domanda concreta. L'identificativo stabile evita che una risorsa venga confusa con una copia; la frequenza indica se un dato è adatto a un controllo giornaliero; il contatto evita che il fruitore corregga da sé un valore ambiguo; la licenza chiarisce se e come il riuso sia consentito. Anche la data di ultima revisione conta: una descrizione elegante ma obsoleta può essere più dannosa dell'assenza di catalogo.

Nel costruire un inventario, non limitarti ai dataset ufficiali. Chiedi quali estratti, fogli di lavoro, interfacce, file di scambio e copie vengono davvero usati dal processo. L'obiettivo non è censire ogni file personale, ma individuare risorse che condizionano un servizio, un obbligo o una decisione. Poi collega ogni risorsa al dominio, alla fonte e alla funzione che la presidia.

Il glossario richiede una disciplina semplice: definizione, contesto, esempi di inclusione o esclusione, responsabile e versione. Questa struttura rende il termine riusabile da uffici diversi e permette di riconoscere quando una modifica semantica impone aggiornamenti a schemi, istruzioni o indicatori. Senza questa cura, l'interoperabilità tecnica può moltiplicare rapidamente un equivoco invece di risolverlo.

Inventario, catalogo, glossario e scheda dataset si sostengono a vicenda, ma rispondono a domande diverse. L'inventario censisce ciò che l'ente possiede o utilizza: dominio, dataset, finalità, fonti, sistemi, responsabili, classificazione e stato. È utile anche per risorse non pubbliche, perché rende visibili archivi dimenticati, repliche e dipendenze. Il catalogo rende le risorse ricercabili e comprensibili attraverso metadati coerenti. Può essere interno o pubblico. Catalogare non significa rendere accessibili i record.

Il glossario stabilisce il significato dei termini. “Pratica chiusa” può indicare un provvedimento adottato, una comunicazione inviata o un pagamento concluso. Se uffici diversi usano la stessa etichetta per eventi diversi, non basta uniformare il formato: occorre decidere la definizione, il dominio di validità e il responsabile del suo aggiornamento. Un vocabolario condiviso, codici stabili e regole di mappatura sostengono anche l'interoperabilità semantica.

I metadati descrivono il dato e il suo contesto. Quelli descrittivi comprendono titolo, descrizione, parole chiave e copertura. Quelli strutturali indicano campi, tipi, relazioni e codifiche. Quelli amministrativi riportano titolare, contatti, condizioni d'uso e licenza; quelli tecnici formato, interfaccia, versione e frequenza; quelli di qualità regole, indicatori, esiti e data dell'ultima verifica. Il profilo nazionale DCAT-AP_IT è un riferimento per descrivere dataset e distribuzioni nei cataloghi pubblici: non sostituisce l'analisi del caso né rende obbligatoria la pubblicazione.

Una scheda dataset minima deve permettere a una persona competente di capire cosa sia la risorsa, a quale processo serva e come trattarla. Include identificativo stabile, finalità, descrizione, fonte, owner e steward, struttura, classificazione, frequenza, lineage, regole di qualità, accessi, conservazione, distribuzioni, licenza se pertinente e contatto. Una distribuzione è una modalità concreta di accesso, per esempio file CSV, JSON, API o download; il dataset è invece la risorsa logica. Confondere i due piani produce cataloghi poco chiari e richieste tecniche mal formulate.

| Artefatto | Domanda a cui risponde | Esempio |
| --- | --- | --- |
| inventario | quali risorse esistono e chi le presidia? | archivio autorizzazioni e sistemi collegati |
| catalogo | come trovo e comprendo una risorsa? | descrizione ricercabile di un dataset |
| glossario | che cosa significa un termine? | definizione di “occupazione attiva” |
| lineage | da dove proviene e come cambia? | istanza, protocollo, gestionale, mappa |
| scheda dataset | quali regole valgono per questa risorsa? | frequenza, qualità, accessi e versione |

**Errore tipico:** compilare metadati solo quando si pubblica un file. Se definizioni, frequenza e responsabilità non sono curate durante il ciclo di vita, il catalogo diventa presto un elenco non affidabile.

**Applicazione:** nel laboratorio finale usa prima l'inventario e poi la scheda. Il primo dà la vista d'insieme; la seconda consente di governare il singolo dataset.

## N-TR01-10-05 · Qualità del dato: regole, metriche, anomalie e rimedio
### Dal controllo alla responsabilità di miglioramento

Una regola di qualità deve indicare anche il punto in cui viene applicata. Un controllo al salvataggio previene l'errore; un controllo notturno intercetta dati già caricati; una riconciliazione periodica confronta fonti diverse. La scelta dipende dalle conseguenze: bloccare un'istruttoria per un campo secondario può essere sproporzionato, mentre consentire un pagamento con un identificativo duplicato può essere rischioso. Il candidato deve saper motivare questo equilibrio.

Le anomalie non hanno tutte lo stesso peso. Un valore mancante può impedire una comunicazione ma non la registrazione iniziale; un codice errato può propagarsi a più servizi; un ritardo nell'aggiornamento può essere tollerabile per statistiche mensili e inaccettabile per una situazione operativa. Perciò il registro distingue gravità, impatto, dataset dipendenti, scadenza e verifica di chiusura. La priorità deriva dalla finalità e dal danno possibile.

Il monitoraggio deve produrre apprendimento. Se una regola fallisce spesso, l'ente può rivedere l'interfaccia, aggiornare le codifiche, correggere l'integrazione o formare chi inserisce i dati. In ogni caso conserva l'evidenza della decisione. Limitarsi a inviare un elenco di errori senza assegnazione e riesame equivale a misurare il problema senza governarlo.

La qualità del dato è l'adeguatezza allo scopo. Non coincide con l'assenza di celle vuote, con la pulizia grafica o con un numero molto grande di informazioni raccolte. Un indirizzo può essere formalmente completo ma non aggiornato; un codice può rispettare il formato e riferirsi alla pratica sbagliata. Perciò una valutazione seria sceglie dimensioni e controlli in rapporto all'uso amministrativo del dataset.

Le dimensioni ricorrenti sono accuratezza, completezza, coerenza, tempestività, validità e unicità. L'accuratezza riguarda la corrispondenza alla realtà o a una fonte autorevole. La completezza indica la presenza dei valori necessari, non la raccolta indiscriminata di ogni possibile valore. La coerenza cerca contraddizioni fra campi, record o sistemi. La tempestività valuta se l'aggiornamento avviene entro il tempo utile. La validità verifica formato, dominio e regole; l'unicità individua duplicati non giustificati. Nessuna di queste dimensioni basta da sola.

Una regola di qualità deve essere controllabile. “I dati devono essere buoni” non consente alcuna verifica. “Ogni autorizzazione attiva deve avere codice ufficio valorizzato e appartenente al dominio approvato” permette invece di definire popolazione, controllo e risultato. La metrica può essere percentuale di record conformi, numero di duplicati o tempo tra evento e aggiornamento. La soglia va motivata in base a rischio, volume e conseguenze; non va inventata perché una percentuale sembri rassicurante.

| Problema | Regola | Metrica | Presidio |
| --- | --- | --- | --- |
| responsabile mancante | pratica attiva con responsabile | percentuale conforme | controllo periodico |
| codice duplicato | identificativo unico | duplicati rilevati | controllo al salvataggio |
| stato incoerente | chiusa implica data di chiusura | record incoerenti | riconciliazione |

Il controllo non termina quando individua uno scarto. Il registro delle anomalie associa origine, impatto, priorità, assegnatario, rimedio, data di chiusura e verifica successiva. Se la stessa anomalia ricompare, occorre chiedersi se il difetto nasca dall'interfaccia, dalla formazione, dalla regola di processo o da un'integrazione. Correggere un singolo record può essere necessario, ma non risolve una causa sistemica.

Il capitolo sulle basi dati sviluppa vincoli e qualità a livello tecnico. Qui l'attenzione è sul governo: chi definisce la regola, chi verifica l'esito, chi accetta un'eccezione e come l'ente dimostra di aver corretto il problema. Un indicatore senza proprietario e senza azione prevista è una misura descrittiva, non un controllo.

**Errore tipico:** fissare una soglia senza spiegare che cosa accade se non viene raggiunta. Una soglia utile deve attivare un responsabile, un approfondimento o una decisione proporzionata.

**Uso in prova:** formula sempre la catena regola–metrica–evidenza–responsabile–rimedio. È più convincente di un elenco di dimensioni imparato a memoria.



Quando una metrica peggiora, l'ente confronta periodo, fonte e cambiamenti di processo prima di attribuire la colpa a chi inserisce i dati. Questa analisi distingue un errore occasionale da una regola ormai inadatta e consente di programmare un rimedio verificabile.

## N-TR01-10-06 · Open data, riuso, distribuzioni e limiti
### Riuso utile, non semplice esposizione

Un dataset aperto è utile quando una persona diversa dall'ente può capirlo, ottenerlo e riutilizzarlo senza ricostruirne ogni volta il significato. Per questo le descrizioni dei campi, le codifiche, la frequenza e la versione fanno parte della qualità del riuso. Se un codice territoriale cambia senza avviso, una distribuzione formalmente disponibile può produrre analisi errate. Il governo dell'apertura include quindi un canale per aggiornamenti, correzioni e cessazione della distribuzione.

La valutazione dei limiti non è una formalità da svolgere all'ultimo momento. Si analizzano contenuto, granularità, collegabilità con altre fonti, destinatari prevedibili, finalità e diritti coinvolti. Una tabella apparentemente anonima può diventare problematica se combina luogo, data, evento raro e altri attributi. Aggregare o eliminare un campo può ridurre il rischio, ma occorre verificare che la risorsa resti corretta e non induca interpretazioni sbagliate.

Nelle risposte d'esame, evita formule assolute. Spiega il metodo: prima si determina se il quadro applicabile consente la pubblicazione, poi si definiscono contenuto e distribuzione, infine si curano metadati, condizioni, aggiornamento e controllo degli effetti.

Gli open data sono dati predisposti per il riuso secondo il quadro applicabile. Per essere effettivo, il riuso richiede almeno condizioni comprensibili: formato aperto e leggibile meccanicamente quando pertinente, metadati, licenza o condizioni d'uso, canale di accesso, aggiornamento e documentazione. Un PDF può essere utile alla consultazione; difficilmente consente elaborazioni automatiche. Un CSV senza descrizione dei campi e senza indicazioni sul riuso lascia invece il fruitore nell'incertezza.

Occorre distinguere situazioni che spesso vengono confuse. La pubblicazione web rende un contenuto disponibile online. La trasparenza risponde a specifici obblighi di conoscibilità previsti dalla disciplina applicabile. L'accesso segue una richiesta, un oggetto e limiti propri. La condivisione mette dati a disposizione di soggetti determinati per una finalità autorizzata. L'open data destina una risorsa al riuso del pubblico con formati, metadati e condizioni adeguati. Le situazioni possono sovrapporsi, ma nessuna si trasforma automaticamente nell'altra.

La direttiva (UE) 2019/1024 disciplina il riutilizzo dell'informazione del settore pubblico. Il regolamento di esecuzione (UE) 2023/138 individua categorie di dataset di elevato valore: geospaziale, osservazione della Terra e ambiente, meteorologia, statistiche, imprese e proprietà delle imprese, mobilità. Per le serie concretamente comprese, il regolamento prevede requisiti che possono includere leggibilità meccanica, API e download massivo. Non basta però riconoscere una parola chiave: occorre verificare allegato, titolare, campo di applicazione e limiti del caso.

Dataset e distribuzione restano distinti. Il dataset “occupazioni di suolo pubblico” può avere una distribuzione CSV per il download, una JSON per elaborazioni e una visualizzazione cartografica. Ogni distribuzione richiede versione, frequenza, descrizione dei campi e condizioni d'uso coerenti. La scelta della licenza e le indicazioni operative devono essere ricontrollate sul quadro vigente prima della pubblicazione: non è prudente trasformare una raccomandazione tecnica in un obbligo universale.

Non tutto ciò che un ente detiene può essere reso aperto. Vanno valutati dati personali, segreti, sicurezza, diritti di terzi, finalità e disciplina settoriale. Una selezione di campi o un'aggregazione può ridurre il rischio, ma non autorizza automaticamente la diffusione. La valutazione dell'apertura è separata da quella dell'uso interno o dello scambio autorizzato; coinvolge competenze amministrative, tecniche, privacy e sicurezza.

**Errore tipico:** affermare che un file già online sia automaticamente open data. Senza metadati, condizioni di riuso, qualità e valutazione dei limiti, la sola pubblicazione non basta.

**Applicazione:** prima di proporre l'apertura, verifica finalità, classificazione, campi, qualità, formato, aggiornamento, licenza, contatto e canale di distribuzione. Solo dopo scegli se il riuso pubblico sia appropriato.



Il riuso richiede anche continuità informativa. Se il dataset cambia struttura, l'ente avvisa i fruitori, conserva una descrizione della versione e valuta tempi ragionevoli di transizione. Pubblicare senza comunicare una modifica può compromettere analisi e applicazioni altrui.

## N-TR01-10-07 · Interoperabilità, privacy, sicurezza e responsabilizzazione
### Lo scambio corretto è anche una decisione di processo

Prima di attivare uno scambio automatico, l'ente descrive evento che lo attiva, finalità, attributi necessari, erogatore, fruitore, risposta attesa, errori possibili e responsabilità di correzione. Questo non è ancora il contratto tecnico dell'API: è il requisito organizzativo che il contratto dovrà rappresentare. Se manca, la tecnologia rischia di trasferire campi superflui o semanticamente ambigui con grande efficienza.

La semantica va verificata con esempi reali. Due enti possono usare la data inizio occupazione con riferimento alla richiesta, al provvedimento o all'effettiva occupazione. Un vocabolario, una regola di codifica e una versione condivisa rendono lo scambio controllabile. Quando il significato cambia, occorre comunicare la modifica, gestire la compatibilità e verificare gli effetti sui fruitori. È il punto in cui governance, interoperabilità e qualità si incontrano.

Responsabilizzazione significa poter spiegare, dopo un controllo o un reclamo, quale dato è stato usato, con quale finalità, da quale fonte, sotto quale autorizzazione e con quali misure. Non promette assenza di errori; rende invece gli errori individuabili, limitabili e correggibili. Questo è il collegamento pratico tra data governance, tutela dei diritti e affidabilità dei servizi digitali.

L'interoperabilità è la capacità di organizzazioni e sistemi di cooperare preservando significato, responsabilità e regole. Non coincide con un'API né con l'accesso libero. Un'API riguarda principalmente il livello tecnico; non decide se lo scambio sia legittimo, chi corregga un errore o quale definizione debba essere usata per un attributo come “residente attivo”.

I quattro livelli aiutano a ordinare il ragionamento. Il livello giuridico verifica basi, condizioni e limiti compatibili. Quello organizzativo chiarisce processi, ruoli, accordi e gestione delle eccezioni. Il livello semantico allinea significati, vocabolari, schemi, codici e identificatori. Il livello tecnico riguarda protocolli, formati, sicurezza dell'interfaccia e modalità di scambio. Un progetto può funzionare sul piano tecnico e fallire sugli altri: due sistemi possono scambiarsi il campo `stato` senza condividere il significato dei codici.

ModI, PDND ed e-service disciplinano aspetti di interoperabilità della PA che il candidato deve saper collocare. Per contratti API, ruoli di erogatore e fruitore, procedure di adesione e dettagli di piattaforma il rinvio è al capitolo 06, sezione “N-TR01-06-06 · Interoperabilità PA ed e-service”. Qui resta la domanda di governo: quale finalità giustifica lo scambio, quali attributi sono necessari, chi autorizza, quale versione è valida, come si gestiscono errori e revoche, quali evidenze dimostrano i controlli svolti.

Il regolamento (UE) 2024/903, noto come Interoperable Europe Act, considera l'interoperabilità dei servizi pubblici digitali transeuropei anche sotto profili organizzativi, semantici e giuridici. Le valutazioni previste dal regolamento vanno applicate nel loro preciso campo soggettivo e oggettivo; non è corretto trasferirle automaticamente a ogni progetto locale. In prova, questa cautela è preferibile a dichiarazioni assolute su obblighi e piattaforme.

Privacy e sicurezza accompagnano ogni scelta di uso, scambio o apertura. Si verificano finalità, base giuridica, minimizzazione, classificazione, destinatari, conservazione e misure. Gli accessi seguono necessità e autorizzazione; operazioni e decisioni rilevanti devono lasciare evidenza. Privacy by design e security by design significano che tali requisiti entrano nella progettazione e nei cambiamenti, non che vengano controllati soltanto dopo un incidente. IAM, crittografia, logging e gestione degli incidenti sono sviluppati nel capitolo 09; qui servono a sostenere responsabilizzazione e governo del dataset.

**Errore tipico:** applicare il principio once only come se autorizzasse ogni amministrazione a interrogare qualsiasi archivio. Evitare richieste ripetute non elimina finalità, autorizzazioni, minimizzazione e tracciabilità.

**Uso in prova:** descrivi lo scambio in quattro livelli e concludi separando interoperabilità autorizzata e apertura al riuso. Questa distinzione evita di confondere cooperazione amministrativa e pubblicazione indiscriminata.



La sicurezza dello scambio include controllo degli accessi, protezione delle comunicazioni, registrazione delle operazioni e gestione delle anomalie. Il livello di dettaglio tecnico dipende dal servizio, ma la governance deve stabilire chi valuta il rischio, chi approva le eccezioni e come si verifica l'efficacia dei controlli.

## Caso guidato: occupazioni di suolo pubblico

Un comune gestisce autorizzazioni per occupazione di suolo pubblico. Le istanze arrivano dal portale, l'ufficio aggiorna il gestionale, polizia locale e tributi usano alcuni dati e l'ente valuta una mappa aperta.

1. Definisce finalità: istruttoria, controllo ed entrate. L'eventuale apertura resta una decisione distinta.
2. Assegna ruoli: il responsabile del processo presidia il dominio; uno steward cura glossario e qualità; la funzione ICT custodisce sistemi e accessi.
3. Registra lineage: portale, protocollo, gestionale e sistema cartografico. Ogni campo rilevante ha fonte e versione.
4. Fissa regole: identificativo unico, data finale non precedente all'inizio, stato coerente con il provvedimento, geometria presente quando necessaria.
5. Classifica i dati: nominativi e contatti non confluiscono automaticamente in una distribuzione aperta.
6. Per lo scambio con altri uffici, definisce finalità, attributi, semantica, responsabilità e gestione degli errori.
7. Per l'open data, valuta separatamente campi, limiti, formato, metadati, licenza, frequenza e contatto.
8. Riesamina scarti, ritardi, reclami, versioni e decisioni di dismissione.

## Laboratorio: inventario e scheda dataset

| Campo dell'inventario | Compilazione richiesta |
| --- | --- |
| dominio e dataset | nome e identificativo stabile |
| finalità | processi e usi autorizzati |
| fonti e sistemi | origine, copie e dipendenze |
| responsabilità | owner, steward, custodian e fruitori |
| classificazione | pubblico, interno o riservato; dati personali |
| stato | attivo, in revisione o dismesso |

Per la scheda dataset aggiungi descrizione, copertura, struttura e codifiche, glossario, frequenza, lineage, regole e indicatori di qualità, accessi, conservazione, distribuzioni, licenza quando applicabile, contatto, data e versione di revisione. Poi percorri l'albero decisionale: serve al processo interno? Va condiviso con soggetti determinati? Richiede uno scambio automatico? È destinato al riuso pubblico? Ogni risposta apre una valutazione diversa.

## Domanda da commissario

**Come imposteresti la governance di un dataset destinato allo scambio tra enti e al possibile riuso come open data?**

Partirei da finalità, dominio e fonti. Assegnerei responsabilità, costruirei inventario, glossario, lineage e scheda dataset, poi definirei regole e indicatori di qualità. Per lo scambio fisserei base, destinatari, semantica, versione e gestione degli errori. Per l'apertura verificherei separatamente limiti, formato leggibile meccanicamente, metadati, licenza, distribuzioni e aggiornamento. Documenterei decisioni, accessi, anomalie e riesami.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento rende controllabile la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-10-01` | Quiz 1. La governance del dato coincide con l'amministrazione tecnica del database? |
| `N-TR01-10-02` | Quiz 2. Il data steward può sostituire il responsabile di processo nella scelta di un nuovo uso dei dati? |
| `N-TR01-10-03` | Quiz 3. Il lineage serve solo a documentare una pipeline tecnica? |
| `N-TR01-10-04` | Quiz 4. Catalogare una risorsa significa pubblicarne i record? |
| `N-TR01-10-05` | Quiz 5. Una percentuale di record conformi è già una regola di qualità completa? |
| `N-TR01-10-06` | Quiz 6. Un CSV disponibile sul sito è sempre un open data riutilizzabile? |
| `N-TR01-10-07` | Laboratorio: inventario e scheda dataset |

## ▣ Verifica

**Quiz 1.** La governance del dato coincide con l'amministrazione tecnica del database?
**Risposta corretta:** no. La governance decide finalità, significati, responsabilità e regole; la custodia tecnica attua controlli e assicura disponibilità.

**Quiz 2.** Il data steward può sostituire il responsabile di processo nella scelta di un nuovo uso dei dati?
**Risposta corretta:** no. Lo steward cura definizioni, metadati e qualità; la decisione sull'uso richiede la funzione competente per il processo e gli altri raccordi necessari.

**Quiz 3.** Il lineage serve solo a documentare una pipeline tecnica?
**Risposta corretta:** no. Aiuta anche a ricostruire origine, trasformazioni, versioni e dipendenze di un dato usato in un procedimento o in un indicatore.

**Quiz 4.** Catalogare una risorsa significa pubblicarne i record?
**Risposta corretta:** no. Un catalogo può descrivere una risorsa riservata. Inventario, catalogo e accesso sono piani diversi.

**Quiz 5.** Una percentuale di record conformi è già una regola di qualità completa?
**Risposta corretta:** no. Occorrono popolazione, regola, metrica, soglia motivata, responsabile, evidenza e azione in caso di anomalia.

**Quiz 6.** Un CSV disponibile sul sito è sempre un open data riutilizzabile?
**Risposta corretta:** no. Devono essere valutati anche metadati, condizioni di riuso, aggiornamento, qualità, limiti e canale di distribuzione.

## Da sapere in 5 righe

La data governance rende esplicite decisioni, ruoli, regole ed evidenze sul patrimonio informativo.
Inventario, catalogo, glossario, lineage e scheda dataset sono strumenti diversi.
La qualità nasce da regole misurabili e da rimedi assegnati.
Open data, trasparenza, accesso, condivisione e interoperabilità non sono sinonimi.
Uno scambio corretto richiede finalità, semantica, responsabilità, sicurezza e tracciabilità.

## Riferimenti normativi e professionali essenziali

- Codice dell'amministrazione digitale, decreto legislativo 7 marzo 2005, n. 82.
- AgID, Linee guida recanti regole tecniche per l'apertura dei dati e il riutilizzo dell'informazione del settore pubblico, versione 1.0.
- Direttiva (UE) 2019/1024 relativa all'apertura dei dati e al riutilizzo dell'informazione del settore pubblico.
- Regolamento di esecuzione (UE) 2023/138 sulle serie di dati di elevato valore.
- Regolamento (UE) 2024/903 sull'interoperabilità dei servizi pubblici digitali nell'Unione.
- AgID, Piano Triennale per l'informatica nella PA 2024-2026, Aggiornamento 2026.

## Errori da evitare

Non usare dato aperto, dato online e dato condivisibile come sinonimi. Non assegnare la qualità a una funzione senza darle regole, poteri e tempi. Non confondere la fonte tecnica con la fonte autorevole del significato. Non progettare un'interoperabilità partendo dal payload: prima chiarisci finalità, semantica, responsabilità e limiti.
