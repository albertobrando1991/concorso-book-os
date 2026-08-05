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
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01", "data-governance", "open-data", "interoperabilita"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 10
draft_stage: cross-reviewed
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/data-governance-open-data-interoperabilita-fonti-primarie", "topics/data-governance-qualita-metadati-open-data", "planning/08-capitolo-10-piano-completamento"]
---

# Data governance, open data, interoperabilità e qualità

Un'amministrazione può disporre di banche dati estese e non sapere chi ne cura il significato, quali controlli ne attestino l'affidabilità o se possano essere condivise. Il problema non è soltanto informatico. Un dato errato può produrre un pagamento indebito; un dato non aggiornato può rallentare un procedimento; un dato pubblicato senza valutazione può ledere diritti.

La **data governance** dà ordine al patrimonio informativo: chiarisce chi decide, chi opera, quali regole si applicano e quali prove documentano le attività lungo il ciclo di vita. Qualità, interoperabilità e riuso dipendono da questo presidio.

## Obiettivo e confine con il volume base

Il capitolo permette di distinguere governance, gestione e architettura, assegnare i ruoli e costruire un inventario con la relativa scheda dataset. Mostra inoltre come tradurre un problema di qualità in una regola misurabile e come separare pubblicazione web, trasparenza, accesso, scambio interoperabile e open data.

Il capitolo 4 spiega basi dati e vincoli; il capitolo 6 tratta API, ModI, PDND ed e-service; il capitolo 9 approfondisce accessi, log e sicurezza. Qui questi elementi sono ricondotti alle decisioni di governo.

## Mappa BANDO: governare il dato

- **B — Base:** finalità, dominio, fonte e significato.
- **A — Attori:** owner, steward, custode, produttori e fruitori.
- **N — Nodi:** qualità, protezione, segreti, diritti di terzi e dipendenze.
- **D — Documenti:** inventario, glossario, scheda, regole e log delle decisioni.
- **O — Output:** uso interno, condivisione autorizzata, servizio interoperabile o pubblicazione aperta.

La scelta dell'output viene dopo l'analisi di finalità, responsabilità e vincoli.

## Il dato come patrimonio informativo

### Dato, informazione, dataset e dominio

Un **dato** è una rappresentazione elementare. Diventa informazione quando è interpretato in un contesto. Un **dataset** è una raccolta organizzata, con struttura e significato definiti. Il **dominio** raggruppa dati riferiti a un ambito coerente, come tributi, personale o mobilità.

La quantità, da sola, non produce valore. Un dataset è utile quando se ne conoscono significato e provenienza, la qualità è adeguata all'uso e le condizioni d'impiego sono chiare.

### Governance, gestione e architettura

La **governance** stabilisce chi decide e secondo quali principi. La **gestione** esegue acquisizione, controllo, correzione, conservazione e distribuzione. L'**architettura** descrive sistemi, flussi, modelli e integrazioni.

Esempio: la governance decide che il codice pratica è l'identificatore ufficiale; la gestione corregge i duplicati; l'architettura realizza il controllo nei sistemi. Senza la prima decisione, due applicazioni possono essere efficienti ma semanticamente incompatibili.

## Ruoli e responsabilità

Owner, steward e custodian descrivono funzioni organizzative. Non sono, per il solo fatto di essere qui richiamati, qualifiche giuridiche obbligatorie.

### Owner, steward e custodian

Il **data owner** presidia le decisioni sul dominio: finalità, usi ammessi, priorità di qualità e autorizzazioni. Deve essere vicino alla responsabilità del processo, non limitarsi all'amministrazione tecnica del database.

Il **data steward** cura definizioni, metadati, regole di qualità ed eccezioni. Il **data custodian** assicura disponibilità, backup, protezione e attuazione tecnica degli accessi, ma non decide autonomamente nuovi usi.

### Produttori, fruitori e responsabili del processo

Il produttore crea o acquisisce il dato; il fruitore lo usa; il responsabile del servizio assicura l'erogazione. RTD, sicurezza, DPO, trasparenza e process owner intervengono per le rispettive competenze. La loro partecipazione non sposta, di per sé, la responsabilità della decisione.

### Decisioni, RACI ed evidenze

Una matrice RACI può indicare chi esegue, chi risponde della decisione, chi è consultato e chi informato. Diventa utile quando a ogni decisione corrisponde un'evidenza, come un verbale, un'autorizzazione, l'esito di un controllo o una versione della scheda.

| Decisione | Decide | Cura | Evidenza |
| --- | --- | --- | --- |
| definizione ufficiale | owner | steward | glossario approvato |
| regola di completezza | owner | steward | specifica e report |
| accesso tecnico | owner autorizza | custodian attua | richiesta e log |
| apertura del dataset | funzione competente | gruppo multidisciplinare | valutazione e licenza |

## Ciclo di vita del dato

### Creazione e acquisizione

Prima della raccolta si definiscono finalità, fonte, base che legittima il trattamento, dati minimi, formato e controlli iniziali. Acquisire dati “perché potrebbero servire” aumenta costi e rischi.

### Validazione, uso e condivisione

Il dato viene validato, trasformato e integrato. Ogni passaggio significativo lascia traccia di origine, trasformazione, data, versione e responsabile. Uso interno e condivisione con un altro ente sono decisioni diverse, fondate su finalità e autorizzazioni specifiche.

### Archiviazione e dismissione

Occorre stabilire criteri di conservazione, archiviazione, anonimizzazione quando appropriata e cancellazione sicura. Copie, estratti e dataset derivati devono essere inclusi: eliminare la tabella principale lasciando repliche non risolve il problema.

## Inventario, catalogo e glossario

L'**inventario** censisce dataset, responsabili, finalità, fonti, sistemi e classificazione. Il **catalogo** li rende ricercabili e comprensibili con metadati uniformi. Può essere interno o pubblico. Catalogare non significa rendere il contenuto accessibile: si può descrivere una risorsa riservata senza esporne i record.

Il **glossario** associa un termine a definizione, dominio e responsabile. “Pratica chiusa” può significare provvedimento adottato, comunicazione inviata o pagamento concluso. Senza definizione comune, gli indicatori non sono confrontabili.

Il **data lineage** ricostruisce provenienza e trasformazioni. Se un errore a monte alimenta più servizi, permette di seguirne la propagazione. Versioni e dipendenze indicano quale struttura era valida e quali sistemi aggiornare dopo una modifica.

## Metadati e scheda dataset

I metadati comprendono:

- **descrittivi:** titolo, descrizione, parole chiave e copertura;
- **strutturali:** campi, tipi, relazioni e codifiche;
- **amministrativi:** titolare, contatti, condizioni d'uso e licenza;
- **tecnici:** formato, interfaccia, versione e frequenza;
- **di qualità:** controlli, indicatori, esiti e ultima verifica.

Una scheda dataset minima riporta identificativo stabile, finalità, descrizione, fonte, owner e steward, struttura, classificazione, aggiornamento, qualità, accessi, conservazione, licenza se applicabile, distribuzioni e contatto.

**Errore tipico:** compilare i metadati solo alla pubblicazione. Se non sono curati durante il ciclo di vita, il catalogo perde rapidamente affidabilità.

## Qualità del dato

### Dimensioni e adeguatezza all'uso

La qualità è l'adeguatezza del dato allo scopo. Le dimensioni ricorrenti sono:

- **accuratezza:** corrispondenza alla realtà o alla fonte autorevole;
- **completezza:** presenza dei valori necessari, non raccolta indiscriminata;
- **coerenza:** assenza di contraddizioni fra campi o sistemi;
- **tempestività:** aggiornamento entro il tempo utile;
- **validità:** conformità a formato, dominio e regole;
- **unicità:** assenza di duplicati non giustificati.

Un indirizzo completo può essere vecchio; un codice formalmente valido può appartenere alla pratica sbagliata. Nessuna dimensione esaurisce la qualità.

### Regole, metriche, soglie e controlli

“I dati devono essere buoni” non è verificabile; “ogni pratica attiva deve avere un responsabile valorizzato” lo è. La metrica può essere la percentuale di record conformi. La soglia va motivata in relazione a rischio e uso, non inventata o copiata.

| Problema | Regola | Metrica | Controllo |
| --- | --- | --- | --- |
| responsabile mancante | pratica attiva con responsabile | percentuale conforme | giornaliero |
| codice duplicato | identificativo univoco | duplicati rilevati | al salvataggio |
| stato incoerente | chiusa implica data chiusura | record incoerenti | periodico |

### Anomalie, remediation e monitoraggio

Il registro delle anomalie riporta origine, impatto, priorità, assegnatario, rimedio e verifica di chiusura. Quando il difetto nasce da un'interfaccia, da un processo o da un'integrazione, correggere il singolo record non basta. Il monitoraggio evidenzia andamento, recidive e dataset dipendenti.

## Open data e riuso

### Formato, leggibilità meccanica, licenza e accessibilità

Un open data è destinato al riutilizzo secondo il quadro applicabile. Il riuso effettivo richiede un formato aperto e leggibile meccanicamente, metadati, licenza e condizioni chiare, oltre a un canale di accesso, aggiornamento e documentazione.

Un PDF può essere consultabile ma non facilmente elaborabile. Un CSV senza descrizione dei campi e licenza resta ambiguo. L'apertura è un processo, non un pulsante.

La **pubblicazione web** rende un contenuto disponibile online. La **trasparenza** risponde a specifici obblighi di conoscibilità stabiliti dalla disciplina applicabile. L'**accesso** nasce invece da una richiesta e segue presupposti, oggetto e limiti propri. Gli **open data** sono predisposti per il riuso, con formati, metadati e condizioni adeguati. Le quattro situazioni possono sovrapporsi, ma non coincidono: pubblicare un documento per trasparenza non lo trasforma automaticamente in un dataset aperto.

### Dataset, distribuzioni e cataloghi

Il dataset è la risorsa logica; una **distribuzione** è una modalità di accesso, per esempio CSV, JSON, API o download massivo. Il catalogo espone metadati. Le Linee guida AgID adottano il profilo nazionale DCAT-AP_IT per la descrizione nei cataloghi.

La direttiva (UE) 2019/1024 disciplina open data e riuso dell'informazione del settore pubblico. Il regolamento di esecuzione (UE) 2023/138 individua dataset di elevato valore nelle categorie geospaziale, osservazione della Terra e ambiente, meteorologia, statistiche, imprese e proprietà delle imprese, mobilità. Per quelli concretamente compresi prevede modalità comprendenti leggibilità meccanica, API e, quando indicato, download massivo. L'applicabilità va verificata sull'allegato e sul titolare.

### Limiti alla pubblicazione

Non tutto ciò che un ente detiene è pubblicabile. Occorre verificare dati personali, segreti, sicurezza, diritti di terzi, finalità e disciplina settoriale. Anonimizzazione, pseudonimizzazione e aggregazione non sono sinonimi: la pseudonimizzazione conserva la possibilità di ricondurre i dati a una persona con informazioni aggiuntive.

| Operazione | Destinatari | Scopo |
| --- | --- | --- |
| uso interno | personale autorizzato | procedimento o funzione |
| condivisione | soggetti determinati | cooperazione autorizzata |
| interoperabilità | sistemi autorizzati | scambio strutturato |
| open data | pubblico e riutilizzatori | riuso secondo licenza |

## Interoperabilità

### Quattro livelli

L'interoperabilità è la capacità di organizzazioni e sistemi di cooperare preservando significato e regole. Ha livelli **giuridico** (basi e condizioni compatibili), **organizzativo** (processi e ruoli coordinati), **semantico** (termini e codici condivisi) e **tecnico** (protocolli, interfacce e formati).

Un'API affronta una parte del livello tecnico. Non stabilisce, però, se lo scambio sia lecito, chi debba correggere un dato o cosa significhi “residente attivo”. Vocabolari, schemi e identificatori stabili riducono ambiguità; le mappature devono avere regole, versione e responsabile.

### Raccordo con ModI, PDND ed e-service

Per contratti API, ModI, PDND ed e-service si rinvia al **capitolo 6, sezione “Interoperabilità nella PA”**. Qui la domanda è organizzativa: chi autorizza, quale finalità giustifica lo scambio, quale versione è valida, quali controlli attestano qualità e chi gestisce errori e revoche.

Il principio *once only* mira a evitare richieste ripetute di informazioni già disponibili presso la PA, ma non autorizza accessi indiscriminati. Disponibilità tecnica e legittimazione restano distinte.

Il regolamento (UE) 2024/903 rafforza il quadro per l'interoperabilità dei servizi pubblici digitali transeuropei. Valutazioni e adempimenti vanno applicati al preciso campo previsto, non estesi automaticamente a ogni progetto locale.

## Privacy, sicurezza e responsabilizzazione

Prima di usare, scambiare o pubblicare dati si verificano finalità, base giuridica, minimizzazione, classificazione, destinatari, conservazione e misure. Gli accessi seguono necessità e autorizzazione; operazioni e decisioni rilevanti sono tracciate. Con privacy by design e security by design, questi vincoli entrano nella progettazione. Schede, valutazioni, autorizzazioni e registri documentano la responsabilizzazione.

## Caso guidato: occupazioni di suolo pubblico

Un comune gestisce autorizzazioni per occupazione di suolo pubblico. I dati provengono dalle istanze, sono aggiornati dall'ufficio, usati da polizia locale e tributi e potrebbero alimentare una mappa aperta.

1. **Finalità:** istruttoria, controllo ed entrate; l'apertura è valutata separatamente.
2. **Ruoli:** dirigente come owner, referente come steward, ICT come custode; polizia e tributi sono fruitori autorizzati.
3. **Lineage:** portale, protocollo, gestionale e sistema cartografico; ogni campo ha una fonte.
4. **Qualità:** identificativo univoco; fine non precedente all'inizio; geometria presente se necessaria; stato coerente col provvedimento.
5. **Classificazione:** nominativi e contatti non confluiscono automaticamente nella distribuzione aperta.
6. **Interoperabilità:** scambi con finalità, attributi, contratto e gestione degli errori definiti.
7. **Open data:** si valutano campi necessari, limiti, licenza, formato, frequenza, versione e contatto.
8. **Monitoraggio:** scarti, ritardi, reclami e aggiornamenti alimentano la revisione.

## Laboratorio: inventario e scheda dataset

### Inventario essenziale

| Campo | Compilazione |
| --- | --- |
| dominio e dataset | nome e identificativo |
| finalità | usi autorizzati e processi |
| fonte e sistemi | origine, copie e dipendenze |
| responsabilità | owner, steward e custode |
| classificazione | pubblico, interno o riservato; dati personali |
| stato | attivo, in revisione o dismesso |

### Scheda dataset

Compila: descrizione; copertura; struttura e codifiche; glossario; fonte; frequenza; lineage; regole e indicatori di qualità; accessi; conservazione; distribuzioni; licenza; contatto; data e versione della revisione.

### Albero decisionale

1. Serve a un processo interno? Definire accessi e controlli.
2. Va condiviso con soggetti determinati? Verificare finalità, base, destinatari e accordi.
3. Serve uno scambio automatico? Aggiungere livelli semantico, organizzativo e tecnico.
4. È destinato al riuso pubblico? Effettuare una distinta valutazione open data.

## Domanda da commissario

**Come imposteresti la governance di un dataset destinato allo scambio tra enti e al possibile riuso come open data?**

Partirei da finalità, dominio e fonti; assegnerei owner, steward e custode; costruirei inventario, glossario, lineage e scheda; definirei regole e indicatori di qualità. Tratterei separatamente scambio autorizzato e apertura: per il primo fisserei base, destinatari, semantica e servizio; per la seconda verificherei limiti, formato leggibile meccanicamente, metadati, licenza, distribuzioni e aggiornamento. Documenterei decisioni, accessi, anomalie e revisioni.

## Domande-trappola

- **Un dato in banca dati è automaticamente di qualità?** No: deve essere adeguato all'uso.
- **Catalogare significa pubblicare?** No: il catalogo può descrivere risorse non accessibili.
- **Interoperabilità significa accesso libero?** No: può riguardare solo sistemi autorizzati.
- **Un PDF online è sempre open data?** No: consultabilità, leggibilità meccanica, licenza e riuso sono distinti.
- **Completezza significa raccogliere più dati possibile?** No: significa avere i dati necessari, rispettando minimizzazione.
- **Owner e amministratore del database coincidono?** Non necessariamente: decisione di dominio e custodia tecnica sono funzioni diverse.

## Mini-esercizi e soluzioni

**1.** Il 12% delle pratiche attive è privo del codice ufficio. Formula regola e metrica.
**Soluzione:** ogni pratica attiva deve avere un codice appartenente al dominio autorizzato; metrica: percentuale conforme. La soglia va motivata.

**2.** Un ente espone un CSV senza descrizione dei campi né licenza. È sufficiente?
**Soluzione:** no. Servono metadati, condizioni di riuso, aggiornamento e verifica di limiti e qualità.

**3.** Due enti scambiano il campo “stato”, ma usano codici diversi. Quale livello manca?
**Soluzione:** principalmente quello semantico; occorre una mappatura versionata e governata.

**4.** Ordina: dismissione, acquisizione, definizione della finalità, validazione, uso.
**Soluzione:** finalità, acquisizione, validazione, uso, dismissione.

## Checklist finale

- [ ] Finalità, dominio e fonte sono definiti.
- [ ] Owner, steward, custode, produttori e fruitori sono identificati.
- [ ] Inventario, glossario, lineage e scheda sono aggiornati.
- [ ] Le regole di qualità hanno metrica, controllo e responsabile.
- [ ] Anomalie e remediation sono tracciate.
- [ ] Uso interno, condivisione, interoperabilità e apertura sono valutati separatamente.
- [ ] Privacy, sicurezza, conservazione e diritti di terzi sono verificati.
- [ ] Metadati, distribuzioni, licenza e aggiornamento sostengono il riuso.
- [ ] Versioni, decisioni e revisioni lasciano evidenza.

## Da sapere in 5 righe

La data governance assegna decisioni, responsabilità, regole ed evidenze sul dato.
Inventario, catalogo, glossario e lineage hanno funzioni diverse.
La qualità è adeguatezza all'uso, misurata con regole e indicatori.
Interoperabilità autorizzata e open data non sono sinonimi.
Ogni uso, scambio o pubblicazione richiede finalità, limiti, protezione e aggiornamento.

## Riferimenti consolidati

- [[sources/data-governance-open-data-interoperabilita-fonti-primarie]]
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]]
- [[sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026]]
- [[sources/ingegneria-software-api-interoperabilita-fonti-tecniche]]
- [[sources/basi-dati-sql-nosql-qualita-fonti-tecniche]]
- [[topics/data-governance-qualita-metadati-open-data]]

## Note di review

Audit specialistico concluso: Linee guida, DCAT-AP_IT, licenze, dataset di elevato valore e caso applicativo sono verificati al cut-off. Le versioni mobili vanno ricontrollate sulle fonti ufficiali; le tabelle saranno controllate nel PDF.
