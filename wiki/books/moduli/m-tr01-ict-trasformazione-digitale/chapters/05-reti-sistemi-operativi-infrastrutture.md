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
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "reti", "sistemi-operativi", "infrastrutture"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 5
draft_stage: cross-reviewed
last_compiled_from: ["sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08", "sources/reti-web-protocolli-concorsi", "sources/informatica-operativa-office-sistemi-hardware", "sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27", "sources/reti-sistemi-infrastrutture-fonti-tecniche", "topics/reti-e-protocolli", "topics/sistemi-operativi-e-gestione-file", "topics/internet-web-posta-elettronica", "books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-05-piano-completamento"]
---

# Reti, sistemi operativi e infrastrutture

Di fronte a un servizio che non risponde si accusa spesso la rete. Il guasto può invece trovarsi nel collegamento, nell’indirizzamento, nel DNS, nella porta, nel processo, nei permessi oppure nelle risorse del sistema. La diagnosi parte dalla separazione di questi livelli e dalla raccolta di evidenze.

Il troubleshooting è il punto di incontro fra reti e sistemi operativi: il modello tecnico serve a localizzare il guasto.

## Obiettivo e confine con il VOL-01

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

## Comunicare per livelli

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

## Ethernet, switching e reti locali

Ethernet è una famiglia di tecnologie per reti locali. Sul collegamento, le interfacce usano indirizzi **MAC**. Uno **switch** inoltra frame fra porte della rete locale sulla base delle informazioni apprese; un **router** inoltra pacchetti fra reti IP differenti.

Una **VLAN** separa logicamente domini di rete sulla stessa infrastruttura di switching. La comunicazione fra VLAN richiede una funzione di livello rete. La segmentazione può ridurre il dominio di broadcast e separare gruppi di sistemi, ma non sostituisce da sola autorizzazioni e controlli di sicurezza.

Il dispositivo deve essere descritto per funzione, non per forma. Un apparato reale può integrare switching, routing, accesso wireless e filtraggio, ma le funzioni restano concettualmente distinte.

## Indirizzamento e routing

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

## Trasporto e servizi di rete

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

## Sistema operativo, processi e servizi

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

## Memoria virtuale e file system

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

## Infrastruttura e disponibilità

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

## Troubleshooting per livelli

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

## Caso guidato: portale interno non raggiungibile

Gli utenti segnalano che `portale.ente.interno` non risponde. Il server risulta acceso.

La diagnosi procede senza saltare subito alla configurazione applicativa:

1. un client ottiene un indirizzo e raggiunge il gateway;
2. il nome DNS restituisce un indirizzo non più assegnato al server;
3. collegandosi all’indirizzo corretto, la porta del servizio risponde;
4. i log applicativi non mostrano errori per le richieste di prova.

L’evidenza localizza il problema nel dato DNS. La correzione consiste nell’aggiornare il record previsto e verificare la propagazione nelle cache pertinenti. Riavviare il server non avrebbe corretto la causa.

## Domanda da commissario

**Come affronta il malfunzionamento di un servizio di rete?**

Parto da un sintomo osservabile e ne delimito utenti, sistemi e momento di insorgenza. I controlli procedono dal collegamento alla risposta applicativa, passando per configurazione IP, percorso, DNS, porta e processo. Ogni prova deve discriminare un’ipotesi. Solo dopo raccolgo l’evidenza, applico una modifica controllata e verifico il ripristino senza effetti collaterali.

## Domanda-trappola

**Un RAID rende inutile il backup?**

No. Il RAID può mantenere il servizio o i dati disponibili in presenza di alcuni guasti dei dischi, secondo il livello adottato. Non crea automaticamente una copia storica indipendente e non protegge da ogni cancellazione, corruzione o errore applicativo.

## Errore tipico

Cambiare più configurazioni insieme. Se il servizio torna disponibile, non si sa quale modifica abbia risolto il problema; se peggiora, diventa difficile tornare allo stato precedente. Una diagnosi riproducibile usa test mirati e varia una condizione alla volta.

## Mini-esercizi e quiz

### Esercizio 1 — Sottorete

Per `192.0.2.70/26`, indica rete e broadcast nel modello IPv4 tradizionale.

**Soluzione:** il blocco `/26` contiene 64 indirizzi. `192.0.2.70` appartiene al blocco `192.0.2.64`–`192.0.2.127`; rete `192.0.2.64`, broadcast `192.0.2.127`.

### Esercizio 2 — Diagnosi

Il client raggiunge `192.0.2.10`, ma `servizio.ente.it` non viene risolto. Quale controllo viene prima?

**Soluzione:** verificare la configurazione e la risposta DNS per il nome. Il test IP indica che almeno un percorso verso quell’indirizzo esiste, ma non dimostra che il nome sia configurato correttamente.

### Esercizio 3 — Sistema

Il processo è avviato, ma nessuna porta risulta in ascolto. Indica due ipotesi.

**Soluzione:** il servizio può aver fallito il binding per configurazione o conflitto di porta; può anche essere avviato in una modalità che non espone il listener previsto. Vanno controllati configurazione e log.

### Quiz

Quale affermazione è corretta?

- A. DNS assegna sempre gli indirizzi IP ai client.
- B. Uno switch e un router svolgono necessariamente la stessa funzione.
- C. Un processo può essere in attesa senza utilizzare molta CPU.
- D. Swap e RAM hanno identiche prestazioni.

**Risposta corretta: C.** A descrive una funzione tipica di DHCP; B confonde switching e routing; D ignora la diversa natura delle risorse.

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

## Riferimenti consolidati

- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, §§ 2, 4 e 5;
- [[topics/reti-e-protocolli]];
- [[topics/sistemi-operativi-e-gestione-file]];
- [[topics/internet-web-posta-elettronica]];
- [[sources/reti-web-protocolli-concorsi]];
- [[sources/informatica-operativa-office-sistemi-hardware]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[sources/reti-sistemi-infrastrutture-fonti-tecniche]];
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]].

## Note di review

- Verificare con un network engineer livelli, subnetting, routing, protocolli e caso DNS.
- Verificare con un system administrator processi, memoria, file system, permessi e servizi.
- Consolidare fonti più granulari per Ethernet, VLAN, RAID e disponibilità.
- Validare sui bandi ufficiali sistemi operativi, apparati, protocolli e comandi richiesti.
- Mantenere sicurezza, cloud e continuità nei capitoli dedicati.
- Verificare nel renderer KDP tabelle, blocchi tecnici e caselle della checklist.
