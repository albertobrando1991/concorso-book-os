---
id: chapter-m-tr01-05
type: book_chapter
title: "Reti, sistemi operativi e infrastrutture"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["reti", "sistemi operativi", "infrastrutture", "troubleshooting"]
entities: ["IETF", "Linux Kernel", "IPv4", "IPv6", "TCP", "UDP", "DNS"]
source_refs: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/reti-web-protocolli-concorsi", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/reti-sistemi-infrastrutture-fonti-tecniche"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.8
updated_at: 2026-08-09
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01", "reti", "sistemi-operativi", "infrastrutture"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 5
format_version: 2
dati_operativi: false
draft_stage: written
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/reti-web-protocolli-concorsi", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/reti-sistemi-infrastrutture-fonti-tecniche", "topics/reti-e-protocolli", "topics/sistemi-operativi-e-gestione-file", "topics/internet-web-posta-elettronica", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-05-piano-completamento"]
---

# Reti, sistemi operativi e infrastrutture

Di fronte a un servizio che non risponde si accusa spesso la rete. Il guasto può invece trovarsi nel collegamento, nell’indirizzamento, nel DNS, nella porta, nel processo, nei permessi oppure nelle risorse del sistema. La diagnosi parte dalla separazione di questi livelli e dalla raccolta di evidenze.

Il troubleshooting è il punto di incontro fra reti e sistemi operativi: il modello tecnico serve a localizzare il guasto.

## Obiettivo, inquadramento e confine con il VOL-01

Il VOL-01, capitolo 10, §§ 2, 4 e 5, introduce sistema operativo, file, directory, LAN/WAN, client/server, IP, TCP/IP, DNS, HTTP e dispositivi di rete. Qui tali concetti diventano strumenti di analisi.

Dopo lo studio del capitolo dovrai saper:

- leggere una comunicazione per livelli;
- distinguere MAC, IP, porta e nome DNS;
- interpretare un prefisso IPv4 e una sottorete semplice;
- confrontare switching, routing, TCP e UDP;
- collocare i principali servizi di rete;
- spiegare processi, thread, memoria virtuale e file system;
- distinguere ridondanza, disponibilità e backup;
- costruire una sequenza di troubleshooting basata su test.

Architettura della CPU e gerarchia hardware della memoria sono nel capitolo 2. API e interoperabilità sono nel capitolo 6; virtualizzazione, cloud e continuità nel capitolo 7; sicurezza operativa, IAM e incident response nei capitoli 8-9.

## Mappa BANDO di reti e sistemi

| Passaggio | Domanda da porsi | Azione |
| --- | --- | --- |
| **B — Bando** | Sono richiesti concetti, comandi, apparati o uno specifico sistema operativo? | Separare il modello comune dai dettagli di prodotto. |
| **A — Aree** | Il problema riguarda collegamento, rete, trasporto, servizio, processo o risorsa? | Collocare sintomo e test al livello corretto. |
| **N — Nuclei** | Quali protocolli, servizi e risorse devo saper distinguere? | Costruire una mappa funzione-livello-evidenza. |
| **D — Diario** | Quale ipotesi era errata e quale test l’ha esclusa? | Registrare sintomo, prova, risultato e correzione. |
| **O — Output** | La prova chiede quiz, orale, mappa o caso tecnico? | Allenare la diagnosi nel formato richiesto. |

## N-TR01-05-01 · Livelli, incapsulamento e rete locale

Una rete collega interfacce e sistemi affinché possano scambiare dati secondo regole condivise. I **protocolli** definiscono formato dei messaggi, significato dei campi e comportamento dei partecipanti.

La divisione in livelli riduce la complessità: ogni livello offre servizi a quello superiore e usa il livello inferiore. Il modello **OSI** descrive sette livelli concettuali; l’architettura **TCP/IP** raggruppa funzioni in un numero minore di livelli. Le due strutture aiutano a ragionare, ma non corrispondono perfettamente voce per voce.

| Funzione | Esempi | Domanda diagnostica |
| --- | --- | --- |
| accesso alla rete | Ethernet, Wi-Fi, frame, MAC | il collegamento locale funziona? |
| rete | IPv4, IPv6, routing | esiste un percorso verso la destinazione? |
| trasporto | TCP, UDP, porte | il servizio è raggiungibile sulla porta prevista? |
| applicazione | DNS, HTTP, SMTP, SSH | il protocollo applicativo risponde correttamente? |

### Incapsulamento

Durante l’invio, ogni livello aggiunge informazioni necessarie alla propria funzione. I dati applicativi diventano unità del trasporto, poi pacchetti IP e infine frame sul collegamento locale. Il destinatario compie il percorso inverso.

MAC, IP, porta e nome DNS rispondono a domande diverse e non sono intercambiabili: ciascuno descrive un livello distinto della comunicazione.

### Ethernet, switching e reti locali

Ethernet è una famiglia di tecnologie per reti locali. Sul collegamento, le interfacce usano indirizzi **MAC**. Uno **switch** inoltra frame fra porte della rete locale sulla base delle informazioni apprese; un **router** inoltra pacchetti fra reti IP differenti.

Una **VLAN** separa logicamente domini di rete sulla stessa infrastruttura di switching. La comunicazione fra VLAN richiede una funzione di livello rete. La segmentazione può ridurre il dominio di broadcast e separare gruppi di sistemi, ma non sostituisce da sola autorizzazioni e controlli di sicurezza.

Il dispositivo deve essere descritto per funzione, non per forma. Un apparato reale può integrare switching, routing, accesso wireless e filtraggio, ma le funzioni restano concettualmente distinte.

Per leggere una comunicazione si segue il dato lungo il percorso. Un browser produce una richiesta applicativa, il trasporto la associa a due estremità, IP individua il percorso fra le reti ed Ethernet o Wi-Fi gestiscono il passaggio sul collegamento locale. A ogni tratto possono cambiare il frame e gli indirizzi di collegamento; la destinazione IP resta quella prevista, salvo funzioni intermedie come la traduzione degli indirizzi. Il “pacchetto”, dunque, non è un oggetto identico a ogni livello.

Queste differenze contano quando si raccolgono le evidenze. Il collegamento attivo prova che l’interfaccia vede il mezzo, ma non dice nulla sulla configurazione IP. Un indirizzo assegnato non garantisce l’esistenza di una rotta. Anche una porta raggiungibile lascia aperta una domanda: l’applicazione restituisce il contenuto atteso? Ogni test copre un tratto preciso.

| Evidenza osservata | Che cosa sostiene | Che cosa non dimostra |
| --- | --- | --- |
| collegamento attivo | interfaccia e mezzo sono operativi a livello locale | indirizzamento, routing e servizio |
| MAC appreso dallo switch | è avvenuto traffico sul segmento locale | raggiungibilità di una rete remota |
| risposta dal gateway | il percorso locale fino al router funziona | raggiungibilità della destinazione finale |
| connessione alla porta | trasporto e listener rispondono | correttezza della risposta applicativa |

**Nella prova.** Elencare OSI, switch e router serve a poco senza collegare ogni livello a una funzione, a un sintomo possibile e a un test discriminante. Più uffici comunicano nella stessa VLAN ma non raggiungono altre reti? Il collegamento locale è meno sospetto del gateway o del routing. È isolato un solo ufficio? Il confronto parte da link, VLAN e configurazione locale.

Il traffico broadcast resta confinato nel relativo dominio di collegamento; una VLAN può separare logicamente tali domini anche quando gli apparati fisici sono condivisi. Questa separazione migliora ordine e controllo del traffico, ma la comunicazione fra VLAN richiede routing e regole coerenti. In un caso d’esame bisogna perciò distinguere isolamento di livello 2, percorso di livello 3 e autorizzazione: sono decisioni collegate, non sinonimi.

## N-TR01-05-02 · Indirizzamento, subnetting e routing

Un indirizzo IP identifica un’interfaccia nel contesto della rete. Il prefisso indica la parte usata per individuare la rete; i bit restanti distinguono le interfacce all’interno di quella rete.

In IPv4 un indirizzo contiene 32 bit. La notazione CIDR associa un prefisso, per esempio `192.0.2.64/26`. Un `/26` lascia 6 bit per la parte host: il blocco contiene 64 indirizzi, da `192.0.2.64` a `192.0.2.127`. Nel modello IPv4 tradizionale dell’esercizio:

- indirizzo di rete: `192.0.2.64`;
- indirizzo di broadcast: `192.0.2.127`;
- intervallo host: `192.0.2.65`–`192.0.2.126`.

Il calcolo va sempre riferito al prefisso. Non basta confrontare le prime cifre scritte in decimale.

IPv6 usa indirizzi di 128 bit e una rappresentazione esadecimale. Introduce un formato di intestazione diverso e non usa il broadcast IPv4. In una prova generale conta distinguere ampiezza, notazione e principi; configurazioni avanzate ed extension header richiedono uno studio specifico.

### Gateway e routing

Se la destinazione appartiene alla rete locale, l’host cerca il recapito sul collegamento. Se appartiene a un’altra rete, invia il pacchetto al **gateway** previsto dalla tabella di routing. Il router sceglie un percorso usando prefissi e regole.

La tabella di routing può contenere rotte specifiche e una rotta predefinita. La presenza di un indirizzo IP corretto non garantisce quindi la raggiungibilità: possono mancare gateway, rotta di ritorno o instradamento intermedio.

Nelle reti IPv4, **ARP** consente di associare un indirizzo IPv4 locale a un indirizzo di collegamento. IPv6 usa meccanismi propri di neighbor discovery. I dettagli operativi differiscono, ma l’esigenza diagnostica resta la stessa: raggiungere il prossimo nodo sul collegamento locale.

### Verificare una sottorete senza intuizioni decimali

Il prefisso stabilisce la dimensione dei blocchi. Con `/26`, i primi 26 bit appartengono al prefisso e restano 6 bit: ogni blocco contiene quindi 2 elevato alla sesta, cioè 64 indirizzi. Nell’ultimo ottetto i blocchi iniziano a 0, 64, 128 e 192. L’indirizzo `192.0.2.70` cade nel blocco 64-127; nel modello IPv4 tradizionale dell’esercizio, 64 è l’indirizzo di rete e 127 quello di broadcast.

La stessa tecnica permette di confrontare due host. `192.0.2.70/26` e `192.0.2.120/26` appartengono allo stesso blocco; `192.0.2.130/26` appartiene al blocco successivo. Nel primo caso la consegna locale avviene sul collegamento; nel secondo serve un dispositivo capace di instradare fra le reti. La verifica riguarda indirizzi e prefisso di ciascuna interfaccia, non la somiglianza visiva delle prime tre cifre.

Nella tabella di routing si cerca la rotta più specifica compatibile con la destinazione. La rotta predefinita raccoglie il traffico che non trova una corrispondenza più precisa. La diagnosi comprende anche il percorso di ritorno e gli eventuali filtri: il pacchetto può arrivare a destinazione mentre la risposta non riesce a tornare al mittente.

| Domanda | Dato da controllare | Errore ricorrente |
| --- | --- | --- |
| La destinazione è locale? | indirizzo e prefisso di entrambe le interfacce | confrontare solo la notazione decimale |
| Qual è il prossimo nodo? | tabella di routing e gateway | ritenere sufficiente la presenza di un gateway |
| Il recapito locale è possibile? | risoluzione del vicino sul collegamento | confondere ARP con DNS |
| La risposta può tornare? | rotte e filtri nel verso inverso | osservare soltanto il percorso di andata |

**Nella prova.** Una postazione raggiunge i sistemi della propria sottorete ma non un servizio remoto. Si verificano prefisso e gateway, scelta della rotta, percorso e ritorno. Cambiare DNS non risolve un errore di instradamento già dimostrato con una prova diretta sull’indirizzo IP.

Quando il problema interessa soltanto una direzione, il controllo del ritorno è decisivo. Rotte asimmetriche possono essere legittime, ma ogni verso deve restare praticabile e compatibile con i controlli intermedi. L’assenza della risposta non prova quindi, da sola, che la richiesta non sia arrivata.

## N-TR01-05-03 · Trasporto e servizi di rete

TCP e UDP operano sopra IP e usano numeri di porta per distinguere le comunicazioni applicative.

**TCP** stabilisce una connessione logica e fornisce un flusso ordinato, con controllo degli errori e ritrasmissione secondo il protocollo. **UDP** invia datagrammi senza offrire le stesse garanzie di consegna e ordinamento. L’applicazione può aggiungere i meccanismi di cui ha bisogno.

L’etichetta “più veloce” non basta a descrivere UDP: contano rete, carico, dimensione dei messaggi e comportamento applicativo. TCP è adatto quando serve un flusso affidabile; UDP quando l’applicazione preferisce datagrammi, latenza contenuta o una gestione autonoma delle perdite.

Una comunicazione è descritta, in forma semplificata, da indirizzi e porte delle due estremità. Un **socket** è l’astrazione usata dal sistema operativo per accedere alla comunicazione.

### Servizi principali

| Servizio o protocollo | Funzione |
| --- | --- |
| DNS | risolve nomi e pubblica informazioni di dominio |
| DHCP | assegna parametri di configurazione di rete |
| HTTP/HTTPS | trasferisce richieste e risposte per risorse e servizi web |
| SMTP | trasferisce messaggi di posta |
| IMAP | consente accesso e gestione della casella sul server |
| SSH | offre accesso remoto protetto e altri servizi sicuri |
| NTP | sincronizza gli orologi dei sistemi |

Il **DNS** è gerarchico e distribuito. La risoluzione può coinvolgere cache e più server. Record differenti svolgono funzioni diverse: `A` e `AAAA` associano nomi a indirizzi, `CNAME` indica un alias, `MX` riguarda la posta e `NS` i server autorevoli della zona.

Se un servizio è raggiungibile mediante indirizzo IP ma non mediante nome, DNS diventa un’ipotesi concreta. Se il nome si risolve correttamente ma la porta non risponde, la diagnosi deve spostarsi verso trasporto, processo, ascolto o filtraggio.

Il **NAT** modifica informazioni di indirizzamento durante l’attraversamento di un dispositivo; un **proxy** agisce per conto di un client o di un server a livello applicativo o intermedio. Né NAT né proxy è, per definizione, sinonimo di firewall.

### Dalla risoluzione del nome alla risposta applicativa

Quando un utente apre un servizio web, più passaggi devono riuscire. Il client ricava dal nome una destinazione tramite DNS; sceglie una rotta; apre o usa una comunicazione di trasporto verso la porta prevista; infine scambia messaggi applicativi. HTTPS aggiunge la protezione della sessione e la verifica del certificato secondo il contesto. Un errore mostrato dal browser può quindi derivare da livelli diversi.

La diagnosi separa quattro esiti. Un nome che non produce indirizzi porta a controllare resolver, record e cache. Un indirizzo esistente ma irraggiungibile riporta a configurazione e routing. Quando l’host risponde ma la porta rifiuta o non completa la connessione, si verificano listener, servizio e filtraggio. Se invece la connessione riesce ma la risposta è errata, l’attenzione passa al protocollo applicativo, alla configurazione e ai log correlati.

| Sintomo | Prima ipotesi utile | Evidenza discriminante |
| --- | --- | --- |
| nome non risolto | DNS o configurazione del resolver | risposta alla richiesta per il record atteso |
| timeout verso l’indirizzo | percorso, ritorno o filtro | test progressivi di raggiungibilità e rotta |
| connessione rifiutata | nessun listener o rifiuto esplicito | stato della porta sul server |
| risposta HTTP inattesa | applicazione, proxy o configurazione | codice, intestazioni, contenuto e log |

TCP non rende automaticamente corretta l’applicazione: garantisce proprietà del flusso, non il significato dei dati scambiati. Analogamente, l’uso di UDP non implica assenza di affidabilità complessiva, perché un protocollo applicativo può introdurre conferme, ripetizioni o controllo degli errori. In sede concorsuale la scelta si motiva partendo dai requisiti: ordine, perdita tollerabile, latenza, dimensione e gestione applicativa.

**Nella prova.** Davanti a un portale intermittente, la risposta distingue la risoluzione DNS dalla connessione alla porta e dalla risposta HTTP. Orari, client coinvolti, indirizzi restituiti e codici osservati impediscono di attribuire al DNS un errore applicativo o al server un problema di percorso.

Le prove vanno eseguite nello stesso intervallo del sintomo: cache, indirizzi e stato del servizio possono cambiare, rendendo poco attendibile un confronto raccolto troppo tardi.

## N-TR01-05-04 · Sistema operativo, processi e servizi

Il sistema operativo gestisce CPU, memoria, dispositivi, file, identità e comunicazioni. Il **kernel** opera con privilegi elevati e media l’accesso alle risorse. Le applicazioni lavorano nello spazio utente e richiedono servizi al kernel attraverso interfacce definite.

Un **programma** è un insieme di istruzioni e dati conservati; un **processo** è un’istanza in esecuzione, con stato e risorse. Un **thread** è un flusso di esecuzione all’interno di un processo e condivide parte delle sue risorse con gli altri thread dello stesso processo.

Il sistema operativo assegna tempo di CPU tramite lo **scheduling**. I processi possono essere in esecuzione, pronti o in attesa; le denominazioni precise cambiano fra sistemi. Un processo che non usa CPU può essere in attesa di I/O, di un lock o di un evento: il basso consumo non prova da solo che sia guasto.

### Servizi e dipendenze

Un **servizio** o **demone** esegue una funzione in background, per esempio un server web o un resolver locale. Per diagnosticare un servizio occorre distinguere:

- configurazione presente;
- processo avviato;
- porta in ascolto;
- dipendenze disponibili;
- permessi sufficienti;
- log privi di errori bloccanti;
- risposta effettiva alla richiesta.

Riavviare il servizio può rimuovere temporaneamente il sintomo e cancellare indizi utili. Prima dell’intervento conviene acquisire stato, messaggi e condizioni riproducibili.

### Dallo stato del processo all’erogazione del servizio

Lo stato “attivo” descrive solo una parte della situazione. L’istanza può essere ancora in inizializzazione, bloccata su una dipendenza, priva dei permessi necessari oppure configurata per ascoltare su un’interfaccia diversa. Il controllo prosegue dalla supervisione del servizio fino alla risorsa effettivamente offerta.

Un thread può attendere I/O mentre altri thread dello stesso processo continuano a lavorare. Lo scheduler assegna la CPU alle unità eseguibili, ma una coda di richieste può crescere anche con CPU moderata se il collo di bottiglia è altrove. Per questo stato, utilizzo e latenza vanno letti insieme.

| Controllo | Esito utile | Passo successivo |
| --- | --- | --- |
| configurazione caricata | file e parametri sono leggibili e coerenti | verificare avvio e dipendenze |
| processo presente | esiste un’istanza | controllare stato, thread e messaggi |
| socket in ascolto | il processo espone l’estremità prevista | provare localmente e poi da remoto |
| richiesta locale riuscita | applicazione e percorso locale rispondono | verificare rete e filtri esterni |
| log correlato | l’evento è associato all’orario e alla richiesta | formulare una modifica mirata |

I log hanno valore quando sono correlati a una prova precisa. Una lunga sequenza di messaggi senza riferimento temporale o identificativo può confondere causa ed effetti. Prima di modificare il sistema si annotano ora, richiesta, nodo, configurazione rilevante e risultato. Dopo la modifica si ripete la stessa prova: il confronto rende verificabile il ripristino.

**Caso breve.** Un servizio risulta “running”, ma la porta prevista non appare in ascolto. Il tecnico controlla il log di avvio e trova un errore di binding dovuto a un indirizzo non più assegnato. Corregge un solo parametro, riavvia in modo controllato, verifica il listener, esegue una richiesta locale e poi una remota. L’evidenza collega sintomo, causa e soluzione; un riavvio iniziale senza raccolta dati non avrebbe dimostrato nulla.

Le dipendenze richiedono lo stesso rigore. Un servizio applicativo può dipendere da un database, da un resolver, da uno storage o da un altro processo locale. La presenza del processo principale non dimostra che tali componenti siano disponibili né che le credenziali e i percorsi configurati siano validi. Il controllo segue la catena fino alla prima evidenza incoerente.

Anche la terminazione di un processo va qualificata. Può essere volontaria, causata da un errore non gestito oppure conseguire a un limite di risorse. Stato di uscita, messaggi e condizioni del sistema nello stesso intervallo aiutano a separare queste ipotesi. Avviare ripetutamente l’istanza senza capire perché termina aumenta il rumore e può aggravare il carico.

**Schema per l’orale.** Il servizio si descrive come una catena: configurazione, processo, dipendenze, socket, richiesta e risposta. A ogni passaggio corrisponde un’evidenza osservabile. La struttura mostra la comprensione del sistema operativo e non riduce la diagnosi al comando usato.

## N-TR01-05-05 · Memoria virtuale, file system e risorse

La **memoria virtuale** assegna a ogni processo uno spazio di indirizzamento. Il sistema traduce indirizzi virtuali in memoria fisica mediante strutture come le tabelle delle pagine. Le pagine possono contenere memoria anonima, codice o dati di file.

La **page cache** conserva in memoria dati letti dai file per ridurre accessi più costosi allo storage. La **swap** può ospitare pagine espulse dalla RAM secondo le politiche del sistema. La sua presenza non garantisce prestazioni adeguate: una pressione di memoria elevata può aumentare l’I/O e la latenza.

Una diagnosi distingue memoria libera, memoria disponibile, cache recuperabile, swap usata e processi responsabili. Un singolo numero, isolato dal carico, non basta.

### File system

Il file system organizza nomi, directory, contenuti e metadati. Un **mount** rende un file system accessibile in un punto della gerarchia. I metadati includono, secondo il sistema, proprietà, permessi, dimensione e tempi.

Nei sistemi di tipo Unix, proprietario, gruppo e permessi concorrono a determinare le operazioni consentite. Per attraversare una directory serve un’autorizzazione diversa dalla sola lettura del suo elenco. Il controllo deve coprire l’intero percorso, oltre al file finale.

Un errore di scrittura può dipendere da:

- permessi insufficienti;
- file system montato in sola lettura;
- spazio o metadati esauriti;
- quota raggiunta;
- percorso errato;
- errore del dispositivo o del file system.

### Diagnosi delle risorse senza affidarsi a un solo numero

La memoria “usata” comprende componenti con comportamento diverso. Parte può appartenere direttamente ai processi, parte può essere cache recuperabile, parte può essere impegnata dal kernel. La memoria disponibile è quindi più informativa della sola memoria libera, ma anch’essa va collegata a pressione, recupero delle pagine, swap, latenze e carico. Un picco breve non equivale a un esaurimento persistente.

Sul file system occorre distinguere capacità dei dati e disponibilità dei metadati. Un volume può avere spazio nominale ma non consentire nuove scritture per quota, esaurimento delle strutture necessarie, mount in sola lettura o permessi lungo il percorso. La prova deve riprodurre l’operazione con la stessa identità e sullo stesso percorso usati dal servizio.

| Sintomo | Misure da correlare | Ipotesi da distinguere |
| --- | --- | --- |
| servizio lento | memoria disponibile, swap, I/O, code e latenza | pressione di memoria, storage o lock |
| processo terminato | eventi di sistema, limiti e consumo per processo | esaurimento, limite o errore applicativo |
| scrittura fallita | spazio, quota, mount, permessi e percorso | capacità, autorizzazione o errore del supporto |
| file non trovato | percorso effettivo, mount e identità | nome errato, volume non montato o visibilità diversa |

I permessi vanno letti come una catena. Per creare un file in una directory servono autorizzazioni sulla directory e accesso alle componenti del percorso; possedere il file finale non risolve un blocco su una directory superiore. Nei sistemi che applicano controlli aggiuntivi, i permessi tradizionali possono non essere l’unico fattore: la risposta concorsuale deve ammettere l’esistenza di più livelli senza inventare una configurazione specifica.

**Nella prova.** Se un’applicazione smette di produrre documenti, si confrontano identità del processo, percorso configurato, mount, spazio, quota e messaggi. Una prova minima controllata precede la modifica di un solo fattore. Attribuire tutto allo “spazio disco” porta a ignorare permessi e file system in sola lettura.

Una pressione di memoria persistente può manifestarsi come aumento della latenza prima che il servizio fallisca. Se il sistema recupera continuamente pagine e sposta dati fra RAM e storage, le richieste restano in attesa anche con CPU non satura. Occorre correlare andamento temporale delle metriche e tempi di risposta, evitando soglie universali prive di contesto.

La cache richiede una lettura altrettanto prudente: occupare memoria per conservare dati usati di recente può essere utile e quella memoria può diventare recuperabile. Liberarla indiscriminatamente non risolve la causa di una crescita applicativa e può peggiorare temporaneamente le prestazioni. La domanda corretta è se la risorsa rimane disponibile per il carico e con quale latenza.

Nel caso di un file system pieno, la correzione non coincide automaticamente con la cancellazione del primo file grande. Si identifica chi produce i dati, quali regole di conservazione valgono, se esistono file ancora aperti e quale misura impedisce la ricorrenza. L’intervento deve preservare integrità, autorizzazioni e tracciabilità.

## N-TR01-05-06 · Disponibilità e troubleshooting infrastrutturale

La **disponibilità** descrive la capacità di offrire il servizio quando richiesto. A determinarla concorre l’intera catena: alimentazione, rete, calcolo, storage, applicazione, dati e dipendenze esterne.

La **ridondanza** duplica componenti o percorsi per evitare che un singolo guasto interrompa il servizio. La **fault tolerance** mira a continuare l’erogazione nonostante determinati guasti. Un **singolo punto di guasto** è un elemento la cui indisponibilità interrompe la funzione senza alternativa.

Il RAID combina dischi secondo schemi che possono aumentare disponibilità o prestazioni rispetto al guasto contemplato. Non sostituisce il backup: una cancellazione, una corruzione logica o un errore applicativo può propagarsi anche sulle copie ridondanti.

L’**affidabilità** riguarda la probabilità di funzionare senza guasti in un intervallo; la **manutenibilità** riguarda la facilità e rapidità di ripristino. Entrambe incidono sulla disponibilità osservata.

### Capacità e colli di bottiglia

La capacità va valutata con misure:

- latenza delle operazioni;
- throughput o lavoro completato nell’unità di tempo;
- utilizzo e saturazione delle risorse;
- lunghezza delle code;
- errori, ritrasmissioni e timeout.

Una CPU poco utilizzata non esclude un collo di bottiglia: il sistema può attendere storage, rete, lock o servizio esterno. Le metriche devono essere correlate nel tempo con il sintomo.

### Troubleshooting per livelli

Una diagnosi ripetibile segue questa sequenza:

1. descrivere il sintomo in termini osservabili;
2. definire perimetro e momento del problema;
3. raccogliere una configurazione di riferimento;
4. formulare ipotesi ordinate per livello e probabilità;
5. eseguire un test che distingua almeno due ipotesi;
6. registrare evidenza e risultato;
7. applicare una modifica controllata;
8. verificare servizio e assenza di effetti collaterali.

### Ordine dei controlli

Per un servizio remoto non raggiungibile:

| Controllo | Domanda | Evidenza |
| --- | --- | --- |
| collegamento | l’interfaccia è attiva? | stato del link e contatori |
| configurazione | indirizzo, prefisso e gateway sono corretti? | configurazione locale |
| rete | la destinazione o il gateway risponde? | test di percorso e routing |
| nomi | il nome si risolve nel valore atteso? | risposta DNS |
| trasporto | la porta prevista è raggiungibile? | test di connessione |
| sistema | il processo è avviato e in ascolto? | stato servizio e socket |
| applicazione | la richiesta riceve risposta valida? | codice, contenuto e log |

Gli strumenti cambiano fra sistemi. `ping`, `traceroute` o `tracert`, `ip`, `ss`, `netstat`, `nslookup`, `dig`, `curl`, visualizzatori di eventi e log sono esempi. Un comando ha valore solo se è chiaro quale ipotesi verifica e come interpretarne il risultato.

### Caso guidato: portale interno non raggiungibile

Gli utenti segnalano che `portale.ente.interno` non risponde. Il server risulta acceso.

La diagnosi procede senza saltare subito alla configurazione applicativa:

1. un client ottiene un indirizzo e raggiunge il gateway;
2. il nome DNS restituisce un indirizzo non più assegnato al server;
3. collegandosi all’indirizzo corretto, la porta del servizio risponde;
4. i log applicativi non mostrano errori per le richieste di prova.

L’evidenza localizza il problema nel dato DNS. La correzione consiste nell’aggiornare il record previsto e verificare la propagazione nelle cache pertinenti. Riavviare il server non avrebbe corretto la causa.

### Domanda da commissario

**Come affronta il malfunzionamento di un servizio di rete?**

Parto da un sintomo osservabile e ne delimito utenti, sistemi e momento di insorgenza. I controlli procedono dal collegamento alla risposta applicativa, passando per configurazione IP, percorso, DNS, porta e processo. Ogni prova deve discriminare un’ipotesi. Solo dopo raccolgo l’evidenza, applico una modifica controllata e verifico il ripristino senza effetti collaterali.

### Domanda-trappola

**Un RAID rende inutile il backup?**

No. Il RAID può mantenere il servizio o i dati disponibili in presenza di alcuni guasti dei dischi, secondo il livello adottato. Non crea automaticamente una copia storica indipendente e non protegge da ogni cancellazione, corruzione o errore applicativo.

### Errore tipico

Cambiare più configurazioni insieme. Se il servizio torna disponibile, non si sa quale modifica abbia risolto il problema; se peggiora, diventa difficile tornare allo stato precedente. Una diagnosi riproducibile usa test mirati e varia una condizione alla volta.

## Apparato di verifica dei nuclei

La tabella collega ogni nucleo a un apparato esistente nello stesso capitolo. Il collegamento rende controllabile la tracciabilità senza attribuire automaticamente un esito positivo.

| Nucleo ID | Apparato di verifica |
| --- | --- |
| `N-TR01-05-01` | Micro-verifica: livelli e rete locale |
| `N-TR01-05-02` | Esercizio 1 — Sottorete |
| `N-TR01-05-03` | Quiz 3 |
| `N-TR01-05-04` | Esercizio 3 — Sistema |
| `N-TR01-05-05` | Quiz 5 |
| `N-TR01-05-06` | Quiz 6 |

## ▣ Verifica

### Micro-verifica: livelli e rete locale

Una workstation invia una richiesta web a un server in un’altra rete. Ordina messaggio HTTP, segmento TCP, pacchetto IP e frame Ethernet; poi indica quale apparato inoltra il frame nella rete locale e quale instrada verso l’altra rete.

**Soluzione:** il messaggio HTTP è incapsulato in un segmento TCP, poi in un pacchetto IP e infine in un frame Ethernet. Lo switch inoltra il frame nella rete locale; il router instrada il pacchetto IP verso una rete diversa.



### Esercizio 1 — Sottorete

Per `192.0.2.70/26`, indica rete e broadcast nel modello IPv4 tradizionale.

**Soluzione:** il blocco `/26` contiene 64 indirizzi. `192.0.2.70` appartiene al blocco `192.0.2.64`–`192.0.2.127`; rete `192.0.2.64`, broadcast `192.0.2.127`.

### Esercizio 2 — Diagnosi

Il client raggiunge `192.0.2.10`, ma `servizio.ente.it` non viene risolto. Quale controllo viene prima?

**Soluzione:** verificare la configurazione e la risposta DNS per il nome. Il test IP indica che almeno un percorso verso quell’indirizzo esiste, ma non dimostra che il nome sia configurato correttamente.

### Esercizio 3 — Sistema

Il processo è avviato, ma nessuna porta risulta in ascolto. Indica due ipotesi.

**Soluzione:** il servizio può aver fallito il binding per configurazione o conflitto di porta; può anche essere avviato in una modalità che non espone il listener previsto. Vanno controllati configurazione e log.

### Quiz 1

Quale affermazione è corretta?

- A. DNS assegna sempre gli indirizzi IP ai client.
- B. Uno switch e un router svolgono necessariamente la stessa funzione.
- C. Un processo può essere in attesa senza utilizzare molta CPU.
- D. Swap e RAM hanno identiche prestazioni.

**Risposta corretta: C.** A descrive una funzione tipica di DHCP; B confonde switching e routing; D ignora la diversa natura delle risorse.

### Quiz 2

Due host IPv4 hanno indirizzi `192.0.2.70/26` e `192.0.2.130/26`. Quale affermazione è corretta?

- A. Appartengono necessariamente alla stessa sottorete perché i primi tre ottetti coincidono.
- B. Appartengono a blocchi `/26` diversi e la comunicazione richiede instradamento.
- C. Il prefisso `/26` indica 26 indirizzi utilizzabili.
- D. Il secondo indirizzo è sempre un broadcast.

**Risposta corretta: B.** Il primo indirizzo cade nel blocco 64-127, il secondo nel blocco 128-191. A ignora il prefisso; C confonde bit e indirizzi; D è falsa perché il broadcast del secondo blocco è `.191` nel modello tradizionale.

### Quiz 3

Un nome DNS restituisce l’indirizzo previsto, ma la connessione alla porta del servizio viene rifiutata. Qual è il controllo più mirato?

- A. Sostituire immediatamente il server DNS.
- B. Verificare listener, stato del servizio e binding sul nodo destinatario.
- C. Cambiare il prefisso IP del client.
- D. Aumentare la swap del server.

**Risposta corretta: B.** La risoluzione del nome è già riuscita e il rifiuto orienta verso l’estremità di trasporto o il servizio. Le altre modifiche non discendono dall’evidenza raccolta.

### Quiz 4

Quale situazione dimostra da sola che un’applicazione web funziona correttamente?

- A. L’interfaccia di rete è attiva.
- B. Il server risponde al gateway.
- C. La porta TCP accetta una connessione.
- D. Nessuna delle precedenti.

**Risposta corretta: D.** Ogni evidenza copre solo una parte della catena. Per dimostrare il funzionamento applicativo serve una richiesta valida con risposta attesa, oltre ai controlli sottostanti.

### Quiz 5

Un servizio non riesce a creare un file, sebbene il volume mostri spazio disponibile. Quale spiegazione resta plausibile?

- A. Quota raggiunta, mount in sola lettura o permessi insufficienti.
- B. Il DNS non contiene un record `MX`.
- C. TCP usa ritrasmissioni.
- D. Lo switch ha appreso un indirizzo MAC.

**Risposta corretta: A.** La capacità libera non esclude altri vincoli del file system. B, C e D descrivono aspetti non pertinenti alla scrittura locale indicata.

### Quiz 6

Quale intervento rende un troubleshooting più verificabile?

- A. Cambiare contemporaneamente rete, DNS e configurazione applicativa.
- B. Riavviare ogni componente prima di raccogliere dati.
- C. Formulare un’ipotesi, eseguire un test discriminante e modificare una condizione alla volta.
- D. Considerare il primo messaggio di errore come causa certa.

**Risposta corretta: C.** La sequenza conserva il legame fra ipotesi, evidenza e risultato. Le altre opzioni cancellano informazioni o impediscono di attribuire l’effetto a una causa.

## Checklist finale

| Competenza | Riconosco | Spiego | Applico |
| --- | --- | --- | --- |
| Leggere una comunicazione per livelli | ☐ | ☐ | ☐ |
| Distinguere MAC, IP, porta e DNS | ☐ | ☐ | ☐ |
| Interpretare un prefisso IPv4 | ☐ | ☐ | ☐ |
| Confrontare switch, router, TCP e UDP | ☐ | ☐ | ☐ |
| Collocare i principali servizi | ☐ | ☐ | ☐ |
| Spiegare processi, thread e servizi | ☐ | ☐ | ☐ |
| Diagnosticare memoria e file system | ☐ | ☐ | ☐ |
| Distinguere RAID e backup | ☐ | ☐ | ☐ |
| Individuare un singolo punto di guasto | ☐ | ☐ | ☐ |
| Costruire un piano di troubleshooting | ☐ | ☐ | ☐ |

## Da sapere in 5 righe

- I livelli separano funzioni e rendono diagnosticabile la comunicazione.
- MAC, IP, porta e nome DNS identificano elementi diversi.
- Processi, memoria e file system possono produrre sintomi simili a un guasto di rete.
- Ridondanza, disponibilità e backup rispondono a rischi differenti.
- Il troubleshooting procede per ipotesi, test, evidenza, modifica e verifica.

## Riferimenti professionali essenziali

- IETF/RFC Editor, RFC 8200 per IPv6 e RFC 4632 per il Classless Inter-Domain Routing (CIDR).
- IETF/RFC Editor, RFC 9293 per TCP e RFC 768 per UDP.
- IETF/RFC Editor, RFC 1034 e RFC 1035 per l’architettura e il funzionamento del DNS.
- IETF/RFC Editor, RFC 2131 per DHCP e RFC 9110 per la semantica HTTP.
- Linux Kernel Documentation, sezioni dedicate alla gestione della memoria, ai file system e al file system `/proc`, consultate per i concetti trasferibili di memoria virtuale, processi e file system.
- *Il Metodo BANDO*, capitolo 10, §§ 2, 4 e 5, per i prerequisiti di informatica e reti richiamati nel confine iniziale.
