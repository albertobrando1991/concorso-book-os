# Piano di completamento — Capitolo 05

## Target

`chapters/05-reti-sistemi-operativi-infrastrutture.md`

## Esito della ricognizione

Il capitolo contiene soltanto frontmatter, titolo e specifica della struttura madre. La riga «Reti e sistemi» della matrice è `parziale`: nessun nucleo specialistico dispone ancora di testo destinato al lettore.

La matrice richiede teoria su protocolli, sistemi operativi e infrastrutture, applicazione mediante troubleshooting, output di caso tecnico e verifica tramite caso. La specifica amplia il perimetro a modelli di rete, indirizzamento, servizi, processi, memoria, file system e disponibilità.

Il VOL-01, capitolo 10, §§ 2, 4 e 5, copre già a livello introduttivo sistema operativo, file e directory, LAN/WAN, client/server, indirizzo IP, TCP/IP, DNS, HTTP, SMTP e dispositivi di rete. Il capitolo 5 deve assumere queste nozioni come prerequisiti e sviluppare il livello specialistico: livelli e incapsulamento, subnet e routing, servizi di rete, diagnosi, processi e memoria virtuale, file system, permessi, ridondanza, capacità e disponibilità.

Il confine con i capitoli adiacenti va mantenuto netto. Architettura dell’elaboratore e gerarchia di memoria sono nel capitolo 2; API nel capitolo 6; virtualizzazione, cloud, backup e continuità nel capitolo 7; firewall, vulnerabilità e risposta agli incidenti nei capitoli 8-9.

## Collegamento riga per riga alla matrice

| Campo della matrice | Presa in carico nel piano |
| --- | --- |
| Famiglia/profilo: ICT, Cyber, Cloud | Teoria e casi calibrati sulla diagnosi di servizi e infrastrutture, non sul solo riconoscimento di acronimi. |
| Materia: Reti e sistemi | Trattazione coordinata di comunicazione, servizi, sistema operativo e disponibilità. |
| Concetti: protocolli, OS, infrastrutture | Perimetro ampliato secondo la specifica a indirizzamento, routing, processi, memoria, file system e affidabilità. |
| Frequenza/peso: da validare | Nessuna frequenza quantitativa; profondità, comandi e prodotti dipendono dal bando. |
| Fonte consolidata: dossier M-TR01 | Il dossier definisce collocazione e perimetro, ma non sostiene da solo i claim tecnici. |
| Collocazione: capitolo 05 | Reti, servizi e sistema operativo restano qui; cloud, cyber e API ricevono rinvii precisi. |
| Copertura teorica: da sviluppare | Ogni nucleo avrà definizione, funzione, elementi, distinzioni, conseguenze ed esempio. |
| Applicazione: troubleshooting | Diagnosi per livelli, sintomo, ipotesi, test, evidenza e azione. |
| Output: caso tecnico | Mappa protocolli, piano diagnostico e risposta orale motivata. |
| Verifica: caso | Casi, quiz, domanda-trappola, errore tipico e checklist. |
| Stato: parziale | Potrà passare a `completo` soltanto dopo verifica del testo reale allo step 10. |
| Review: fonti tecniche | Servono standard IETF, documentazione OS e revisione specialistica. |

## Nuclei assegnati

1. Confine fra nozioni introduttive del VOL-01 e livello specialistico del VOL-08.
2. Rete, nodo, interfaccia, collegamento, pacchetto, frame, segmento e flusso.
3. Modelli a livelli: OSI come modello concettuale e suite TCP/IP come architettura operativa.
4. Incapsulamento e responsabilità dei livelli.
5. LAN, WAN, VLAN e segmentazione a livello concettuale.
6. Ethernet, indirizzo MAC e ruolo dello switch.
7. IPv4 e IPv6; indirizzo, prefisso, rete, host, gateway e routing.
8. Subnetting IPv4 essenziale, CIDR e verifica di appartenenza alla stessa sottorete.
9. ARP o meccanismo equivalente di risoluzione locale, limitato alla funzione.
10. TCP e UDP: connessione, affidabilità, ordinamento, ritrasmissione, overhead e casi d’uso.
11. Porte, socket e distinzione fra indirizzo del nodo e servizio applicativo.
12. DNS: gerarchia, risoluzione, record principali, caching e diagnosi.
13. DHCP: assegnazione dei parametri di rete.
14. HTTP/HTTPS, SMTP, IMAP, SSH e NTP per funzione e collocazione.
15. NAT e proxy a livello concettuale, senza confonderli con il firewall.
16. Sistema operativo: kernel, spazio utente, chiamate di sistema, driver e servizi.
17. Programma, processo, thread, stati e scheduling a livello introduttivo-specialistico.
18. Memoria virtuale, spazio di indirizzamento, paginazione e swap; confine con la memoria hardware del capitolo 2.
19. File system: file, directory, metadati, percorsi, mount e permessi.
20. Identità, proprietario, gruppo e autorizzazioni sul file system, senza duplicare IAM.
21. Servizi e demoni, avvio, stato, log e dipendenze.
22. Storage e ridondanza: volume, RAID a livello concettuale e differenza dal backup.
23. Disponibilità, affidabilità, ridondanza, fault tolerance e singolo punto di guasto.
24. Capacità e prestazioni: latenza, throughput, saturazione e colli di bottiglia.
25. Osservabilità di base: metriche, log, eventi e test di connettività.
26. Troubleshooting strutturato dal fisico all’applicazione.
27. Produzione di mappa protocolli, diagnosi, caso tecnico, quiz e risposta orale.

## Nuclei già completi

Nessun nucleo specialistico è completo nel capitolo 5.

Nel VOL-01 sono già completi i prerequisiti:

- funzioni generali del sistema operativo;
- file, cartella, percorso, estensione e operazioni elementari;
- LAN, WAN, Internet, intranet, client/server e peer-to-peer;
- indirizzo IP e famiglia TCP/IP a livello concettuale;
- funzione generale di router, switch, modem e firewall;
- riconoscimento di HTTP, HTTPS, DNS, SMTP, POP3/IMAP, TCP e UDP.

Il rinvio non copre livelli, incapsulamento, subnetting, routing, servizi, processi, memoria virtuale, file system tecnico, disponibilità o metodo di diagnosi.

## Nuclei da sviluppare

- lettura di una comunicazione per livelli;
- distinzione fra MAC, IP, porta e nome DNS;
- calcolo essenziale di rete e host da un prefisso IPv4;
- differenza fra switching e routing;
- scelta motivata fra TCP e UDP;
- percorso di una richiesta DNS e HTTP;
- distinzione fra processo, thread e servizio;
- collegamento fra memoria virtuale, pagine e swap;
- diagnosi di spazio, permessi e mount nel file system;
- differenza fra RAID, replica e backup;
- individuazione di un singolo punto di guasto;
- lettura coordinata di sintomi, metriche e log;
- costruzione di un piano di troubleshooting ripetibile.

## Sezioni da conservare

- frontmatter e identificativi;
- H1 esistente;
- specifica della struttura madre come vincolo editoriale;
- collocazione nella Parte II del volume;
- output previsti: mappa protocolli e troubleshooting.

## Duplicazioni da evitare

- definizioni introduttive già complete nel VOL-01;
- CPU, ciclo di istruzione e gerarchia hardware della memoria, sviluppati nel capitolo 2;
- strutture dati e complessità, trattate nel capitolo 3;
- basi dati e query, trattate nel capitolo 4;
- architetture applicative, API ed e-service, assegnati al capitolo 6;
- macchine virtuali, container, cloud, CI/CD, backup e continuità, assegnati al capitolo 7;
- minacce, vulnerabilità, hardening e firewall come controllo di sicurezza, assegnati al capitolo 8;
- IAM, crittografia, logging di sicurezza e incident response, assegnati al capitolo 9;
- comandi specifici di un sistema operativo quando il bando non li richiede.

## Esempi, casi, domande ed esercizi necessari

- mappa livelli/protocolli/dispositivi per una richiesta a un portale;
- distinzione fra indirizzo MAC, IPv4/IPv6, porta e nome DNS;
- esercizio CIDR semplice con rete, broadcast e intervallo host;
- diagnosi «raggiungo l’IP ma non il nome»;
- diagnosi «il servizio risponde localmente ma non da remoto»;
- confronto TCP/UDP su trasferimento file, streaming e DNS;
- tabella di record DNS essenziali;
- processo bloccato, memoria esaurita o file system pieno come casi OS;
- errore di permesso su file o directory;
- differenza fra servizio inattivo, porta non in ascolto e traffico filtrato;
- caso di singolo punto di guasto e proposta di ridondanza;
- domanda da commissario sul metodo di troubleshooting;
- domanda-trappola su RAID e backup oppure switch e router;
- esercizio di costruzione di una sequenza diagnostica;
- quiz su livelli, protocolli, processi e disponibilità;
- checklist finale «localizzo, misuro, testo, correggo, verifico».

## Fonti da usare

### Fonti e pagine già consolidate

- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]] — per perimetro editoriale;
- [[sources/reti-web-protocolli-concorsi]] — per RFC e concetti di rete già acquisiti;
- [[sources/informatica-operativa-office-sistemi-hardware]];
- [[sources/informatica-concorsi-corpus-fonti-ufficiali-2026-05-27]];
- [[topics/reti-e-protocolli]];
- [[topics/sistemi-operativi-e-gestione-file]];
- [[topics/internet-web-posta-elettronica]];
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]], capitolo 10, §§ 2, 4 e 5;
- [[books/moduli/m-tr01-ict-trasformazione-digitale/planning/02-matrice-copertura-didattica]].

### Fonti tecniche da consolidare prima o durante lo step 09

- RFC e documentazione IETF per IPv4/IPv6, CIDR, TCP, UDP, DNS, DHCP, HTTP e protocolli effettivamente trattati;
- documentazione ufficiale Linux o materiale universitario autorevole per processi, thread, memoria virtuale, file system, permessi e servizi;
- riferimento tecnico primario per Ethernet, switching, VLAN e indirizzamento MAC;
- documentazione autorevole su routing, NAT e strumenti diagnostici;
- fonte tecnica su disponibilità, ridondanza, RAID e distinzione dal backup;
- bandi ufficiali del campione VOL-08 per validare profondità, sistemi operativi, protocolli e comandi richiesti.

Le fonti esistenti sono adeguate per i prerequisiti e parte dei protocolli, ma non bastano a dichiarare completi sistema operativo specialistico, subnetting, infrastrutture e disponibilità. Le nuove fonti dovranno essere consolidate in una source note prima di sostenere il testo finale.

## Topic, entity e quiz collegati

- `topics/reti-e-protocolli.md` e `topics/sistemi-operativi-e-gestione-file.md` sono pertinenti ma orientati al livello introduttivo;
- `topics/internet-web-posta-elettronica.md` sostiene i servizi applicativi;
- le entità tecniche già censite includono IETF, TCP, IPv4, IPv6, DNS e HTTP;
- non risultano quiz consolidati specialistici su subnetting, processi, memoria virtuale e disponibilità;
- i nuovi casi e quiz richiedono verifica tecnica manuale.

## Review umane richieste

- network engineer: livelli, indirizzamento, subnetting, routing, servizi e diagnosi;
- system administrator Linux/Windows: processi, memoria, file system, permessi e servizi;
- infrastructure specialist: storage, ridondanza, disponibilità e capacità;
- docente di sistemi e reti: progressione didattica e accuratezza delle semplificazioni;
- responsabile editoriale: confini con VOL-01 e capitoli 2, 6, 7, 8 e 9;
- responsabile del campione bandi: profondità, sistemi e comandi realmente richiesti;
- revisore didattico: coerenza fra teoria, mappa, casi, quiz e troubleshooting;
- revisore fonti: granularità e tracciabilità degli standard.

## Struttura proposta e budget KDP

# Reti, sistemi operativi e infrastrutture

## Obiettivo e confine con il VOL-01 — 170 parole

## Mappa BANDO di reti e sistemi — 180 parole

## Comunicare per livelli — 330 parole

### Modello OSI e suite TCP/IP

### Incapsulamento e dispositivi

## Ethernet, switching e reti locali — 280 parole

### MAC, switch e VLAN

## Indirizzamento e routing — 480 parole

### IPv4, IPv6, prefissi e gateway

### Subnetting essenziale e instradamento

## Trasporto e servizi di rete — 470 parole

### TCP, UDP, porte e socket

### DNS, DHCP, HTTP, posta, SSH e NTP

## Sistema operativo e processi — 360 parole

### Kernel, spazio utente, processi e thread

### Servizi, stato e dipendenze

## Memoria virtuale e file system — 360 parole

### Pagine, swap e pressione di memoria

### Directory, mount, metadati e permessi

## Infrastruttura e disponibilità — 340 parole

### Storage, RAID e ridondanza

### Affidabilità, capacità e punti di guasto

## Troubleshooting per livelli — 430 parole

### Sintomo, ipotesi, test ed evidenza

### Strumenti e ordine dei controlli

## Caso guidato: portale non raggiungibile — 260 parole

## Domanda da commissario e domanda-trappola — 150 parole

## Errore tipico — 70 parole

## Mini-esercizi e quiz — 300 parole

## Checklist finale — 150 parole più tabella

## Da sapere in cinque righe — 60 parole

## Riferimenti consolidati e note di review — 90 parole

Budget orientativo: 4.000–4.300 parole, tabelle, mappe, casi ed esercizi inclusi. Il budget non comprende cloud, cybersecurity operativa o amministrazione avanzata di prodotto.

## Criteri di approvabilità per lo step 09

- ogni elemento della specifica e della matrice riceve teoria e verifica;
- il rinvio al VOL-01 resta preciso e limitato ai prerequisiti;
- OSI e TCP/IP non sono presentati come sovrapposizione perfetta;
- MAC, IP, porta e DNS restano distinti;
- subnetting e routing includono un esempio verificato;
- protocolli e servizi sono spiegati per funzione prima dei dettagli;
- processi, thread, memoria virtuale e file system ricevono teoria autonoma;
- RAID, replica e backup non sono trattati come sinonimi;
- disponibilità e prestazioni sono collegate a misure e punti di guasto;
- il troubleshooting segue una sequenza esplicita e non una lista casuale di comandi;
- esempi e casi applicano concetti già spiegati;
- fonti tecniche mancanti e review specialistiche restano aperte finché non eseguite.

## Addendum retrofit Format 2 — 2026-08-09

Questo addendum sostituisce, per il nuovo ciclo degli step 08-12, le valutazioni legacy sullo stato del capitolo. Il testo destinato al lettore esiste già ed è una base editoriale da conservare: lo step 09 dovrà riorganizzarlo nel Format 2, colmare i delta misurabili e non riscriverlo da zero. Restano validi i confini, le fonti e i criteri tecnici del piano originario, salvo quanto precisato qui.

### Stato reale e criterio di intervento

- Il capitolo copre già livelli, Ethernet e VLAN, IPv4/IPv6, routing, TCP/UDP, servizi di rete, processi, memoria virtuale, file system, disponibilità e troubleshooting.
- Sono già presenti una Mappa BANDO, un caso guidato, una domanda da commissario, una domanda-trappola, un errore tipico, tre esercizi, un quiz e una checklist.
- La source note `sources/reti-sistemi-infrastrutture-fonti-tecniche` consolida RFC e documentazione Linux; i limiti dichiarati su Ethernet/VLAN, RAID, disponibilità e dettagli dipendenti dal prodotto non vanno occultati.
- Il retrofit deve introdurre Nucleo ID stabili, densità didattica sufficiente, una verifica dopo 5-7 nuclei e almeno sei quiz commentati, preservando esempi e formulazioni tecnicamente corrette.
- La riga `Reti e sistemi` della matrice resta da ricontrollare sul testo effettivo allo step 10; lo step 08 non ne promuove lo stato.

### Nuclei Format 2 assegnati

| Nucleo ID | Titolo operativo | Stato attuale | Sviluppo previsto allo step 09 | Confini principali |
| --- | --- | --- | --- | --- |
| `N-TR01-05-01` | Livelli, incapsulamento e rete locale | parziale-avanzato | Riunire OSI/TCP-IP, incapsulamento, MAC, Ethernet, switching e VLAN in una progressione funzione-evidenza; aggiungere almeno un confronto applicato. | Non trasformare Ethernet/VLAN in manuale di configurazione né anticipare i controlli cyber del cap. 8. |
| `N-TR01-05-02` | Indirizzamento, subnetting e routing | parziale-avanzato | Consolidare IPv4/IPv6, CIDR, gateway, routing e risoluzione locale; mantenere e spiegare il calcolo `/26` con verifica del risultato. | Limitare IPv6 e routing al livello trasferibile richiesto da una prova generalista. |
| `N-TR01-05-03` | Trasporto e servizi di rete | parziale-avanzato | Collegare TCP/UDP, porte e socket a DNS, DHCP, HTTP(S), posta, SSH e NTP; rendere esplicita la diagnosi nome-porta-processo. | API ed e-service al cap. 6; filtraggio e firewall come controllo al cap. 8. |
| `N-TR01-05-04` | Sistema operativo, processi e servizi | parziale-avanzato | Sviluppare kernel/spazio utente, processo/thread, scheduling, servizi, dipendenze, listener e log con un caso breve verificabile. | CPU e gerarchia hardware della memoria al cap. 2; IAM e logging di sicurezza al cap. 9. |
| `N-TR01-05-05` | Memoria virtuale, file system e risorse | parziale-avanzato | Integrare pagine, cache, swap, mount, metadati, permessi, spazio e quote in una sequenza diagnostica; distinguere sintomo, metrica e causa. | Evitare amministrazione avanzata specifica di Linux o Windows. |
| `N-TR01-05-06` | Disponibilità e troubleshooting infrastrutturale | parziale-avanzato | Coordinare ridondanza, fault tolerance, RAID, capacità e colli di bottiglia con il metodo sintomo-ipotesi-test-evidenza-azione-verifica; assorbire caso e output concorsuali. | Backup, RPO/RTO, cloud e continuità al cap. 7; incident response al cap. 9. |

I sei nuclei sono assegnati al capitolo e devono risultare tutti autonomi nel test dello studente: definizione, spiegazione, distinzione, conseguenza, esempio e verifica. Nessun nucleo è dichiarato completo prima degli step 09-10.

### Struttura H1/H2/H3 prevista

# Reti, sistemi operativi e infrastrutture

## Obiettivo, confine con il VOL-01 e Mappa BANDO

## N-TR01-05-01 · Livelli, incapsulamento e rete locale

### OSI e TCP/IP come strumenti di lettura

### Ethernet, MAC, switching e VLAN

## N-TR01-05-02 · Indirizzamento, subnetting e routing

### IPv4, IPv6 e prefissi

### Gateway, routing e risoluzione sul collegamento

## N-TR01-05-03 · Trasporto e servizi di rete

### TCP, UDP, porte e socket

### DNS, DHCP e protocolli applicativi

## N-TR01-05-04 · Sistema operativo, processi e servizi

### Kernel, spazio utente, processi e thread

### Servizi, listener, dipendenze e log

## N-TR01-05-05 · Memoria virtuale, file system e risorse

### Pagine, cache, swap e pressione di memoria

### Mount, metadati, permessi, spazio e quote

## N-TR01-05-06 · Disponibilità e troubleshooting infrastrutturale

### Ridondanza, RAID, capacità e punti di guasto

### Caso guidato e sequenza diagnostica

### Domanda da commissario, domanda-trappola ed errore tipico

## ▣ Verifica

### Tre o più esercizi applicativi

### Sei o più quiz commentati

## Checklist finale

## Da sapere in 5 righe

## Riferimenti professionali essenziali

### Budget e prove previste

- Corpo complessivo: **4.700-5.700 parole**, escluso frontmatter.
- Densità: **500-900 parole per ciascun Nucleo ID**, con tolleranza soltanto se giustificata dalla leggibilità di tabelle o codice.
- Verifiche: **un unico blocco dopo i sei nuclei**, nel rispetto del limite di 5-7 nuclei consecutivi.
- Quiz: **almeno sei**, con risposta corretta e commento sui distrattori o sull'errore tipico.
- Esercizi: **almeno tre** — subnetting, localizzazione del guasto e diagnosi di processo/file system o capacità.
- Casi: **almeno uno completo**, in contesto PA plausibile, con sintomo, ipotesi, test, evidenze, intervento controllato e verifica finale.
- Output: mappa livelli-protocolli-evidenze, piano di troubleshooting e risposta orale motivata.

### Fonti, topic, entity e rinvii da preservare

- Conservare tutti i `source_refs` e i `last_compiled_from` attuali, inclusa la source note tecnica primaria.
- Usare i topic `reti-e-protocolli`, `sistemi-operativi-e-gestione-file` e `internet-web-posta-elettronica` come raccordo, non come sostituti delle fonti tecniche.
- Conservare le entity IETF, Linux Kernel, IPv4, IPv6, TCP, UDP e DNS; aggiungerne solo se realmente usate e sostenute.
- Mantenere il rinvio preciso al VOL-01, capitolo 10, §§ 2, 4 e 5, per le nozioni introduttive.
- Conservare i confini con i capp. 2, 6, 7, 8 e 9 indicati nel piano legacy e nella Bibbia del volume.

### Audit specialistici richiesti

1. `chapter-lint` e controllo di densità didattica del Format 2.
2. Verifica manuale degli esempi CIDR/subnetting e della terminologia IPv4/IPv6.
3. Audit reti su livelli, switching, routing, TCP/UDP, DNS e sequenza diagnostica.
4. Audit sistemi operativi su processi, thread, memoria virtuale, file system, permessi e servizi.
5. Audit infrastrutture su RAID, ridondanza, fault tolerance, disponibilità e metriche di capacità.
6. Controllo dei confini con VOL-01 e con i capitoli 2, 6, 7, 8 e 9.
7. Citation guard su `source_refs`, `last_compiled_from` e riferimenti professionali.
8. Verifica editoriale a 30 punti, test dello studente e controllo KDP su tabelle, formule, comandi e blocchi didattici.

### Criterio di uscita aggiornato

Lo step 09 è approvabile quando i sei Nucleo ID compaiono nel capitolo, ciascun nucleo supera il test dello studente, la verifica contiene almeno sei quiz commentati e tre esercizi, il caso tecnico chiude una diagnosi basata su evidenze e i limiti delle fonti restano espliciti. Lo step 10 dovrà poi dimostrare la copertura reale nella matrice; gli step 11-12 completeranno Humanizer e revisione editoriale senza anticipare la conferma umana dello step 24.
