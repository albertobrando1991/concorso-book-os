---
id: chapter-m-tr01-09
type: book_chapter
title: "IAM, crittografia, logging e incident response"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["iam", "crittografia", "key management", "logging", "incident response"]
entities: ["NIST", "Agenzia per la cybersicurezza nazionale", "CSIRT Italia"]
source_refs: ["sources/iam-crittografia-logging-incident-response-fonti-primarie", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08"]
book_refs: ["m-tr01-ict-trasformazione-digitale", "il-metodo-bando"]
confidence: 0.86
updated_at: 2026-08-11
created_at: 2026-07-28
review_required: true
canonical: true
tags: ["chapter", "m-tr01", "iam", "incident-response"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 9
draft_stage: format-2-retrofit
format_version: 2
dati_operativi: []
last_compiled_from: ["sources/iam-crittografia-logging-incident-response-fonti-primarie", "topics/iam-crittografia-logging-incident-response", "topics/sicurezza-informatica", "books/moduli/m-tr01-ict-trasformazione-digitale/planning/08-capitolo-09-piano-completamento"]
---

# IAM, crittografia, logging e incident response

Un servizio pubblico digitale è affidabile quando l'ente sa chi opera, che cosa può fare, quali tracce lascia e come reagire a un'anomalia. IAM, crittografia, logging e incident response formano una catena: l'identità rende attribuibile l'azione, l'autorizzazione la limita, la crittografia protegge proprietà definite, i log rendono osservabile il sistema e la risposta coordina decisioni, continuità ed evidenze.

## Obiettivo e confine del capitolo

Il volume base tratta password, MFA, phishing e nozioni di sicurezza. Qui il lettore impara a collegare ciclo di vita degli accessi, privilegi, chiavi, rilevazione e gestione di un incidente. Il capitolo 7 tratta continuità, backup, RPO, RTO e disaster recovery; il capitolo 8 tratta rischio, vulnerabilità e controlli; il capitolo 10 tratta governance del dato. Questo capitolo non sostituisce un playbook locale né stabilisce termini di notifica: tali decisioni dipendono dal soggetto, dal caso e dalle fonti ufficiali vigenti.

## Mappa BANDO

| Formula nel bando | Domanda utile | Output concorsuale |
| --- | --- | --- |
| IAM, accessi, privilegi | chi accede, per quale scopo e per quanto tempo? | matrice ruolo-risorsa-permesso |
| crittografia, certificati, chiavi | quale proprietà proteggo e come governo il materiale? | checklist key management |
| logging, SIEM, monitoraggio | quali evidenze servono per qualificare un segnale? | matrice sorgente-evento-alert |
| incidente cyber, CSIRT, NIS2 | chi decide, contiene, comunica e recupera? | playbook e timeline |

## N-TR01-09-01 · Identità, account e ciclo di vita

### Inquadramento e principi

Un'identità digitale rappresenta una persona, un'applicazione, un servizio, un dispositivo o un workload. L'account è il contenitore operativo usato dal sistema; una credenziale è un elemento associato all'identità; un autenticatore dimostra il controllo della credenziale; la sessione conserva l'esito dell'accesso; un attributo descrive soggetto, ruolo o contesto. Distinguere questi elementi evita un errore frequente: disabilitare un account non revoca automaticamente sessioni, token, chiavi applicative o account amministrativi collegati.

L'identity proofing stabilisce con un livello proporzionato di fiducia chi sia il soggetto. L'enrollment registra identità e autenticatori. Il provisioning crea account, gruppi e autorizzazioni; il deprovisioning li rimuove o li sospende. Nel modello joiner-mover-leaver, la fonte autorevole comunica l'ingresso, il cambio di funzione o la cessazione. Il passaggio più rischioso è il mover: aggiungere nuovi accessi senza rimuovere quelli precedenti accumula privilegi che non corrispondono più al compito.

Ogni fase deve produrre una richiesta, un'approvazione, un'esecuzione e un'evidenza verificabile. Un responsabile di servizio non dovrebbe scoprire solo dopo un incidente chi avesse accesso a una pratica. La revisione periodica confronta ruoli effettivi, assegnazioni tecniche, eccezioni e account non usati. L'obiettivo non è avere un elenco perfetto, ma rendere governabile la domanda: chi può accedere a quale servizio, per quale motivo e fino a quando?

Gli account nominativi facilitano attribuzione e accountability. Gli account condivisi rendono difficile capire chi abbia compiuto un'azione e, se inevitabili per una transizione controllata, richiedono misure compensative, durata breve e tracciamento rafforzato. Gli account di servizio hanno proprietario, scopo, privilegi minimi, scadenza e meccanismo di rotazione. Gli account di emergenza devono essere pochi, protetti, monitorati e riesaminati subito dopo l'uso. Non sono scorciatoie permanenti per aggirare il processo ordinario.

In prova, una risposta solida distingue identità, account e autorizzazione prima di parlare di strumenti. Per esempio, quando un istruttore cambia ufficio, l'ente aggiorna ruolo e ambito, revoca i diritti non più necessari, controlla deleghe e sessioni ancora attive e conserva l'evidenza. Dire soltanto «disattivare l'utente» lascia irrisolte dipendenze e privilegi indiretti. L'errore tipico è trattare l'IAM come un elenco di account: è invece un processo che lega organizzazione, identità, sistemi e riesame.

Un registro delle identità deve anche distinguere titolare dell'identità, proprietario dell'account e responsabile dell'autorizzazione. Nelle identità tecniche queste figure possono essere diverse: un'applicazione usa l'account, un responsabile di servizio ne giustifica lo scopo e un team operativo ne amministra la configurazione. La separazione rende possibile riesaminare l'accesso quando cambia il servizio o il fornitore. Una scadenza è utile solo se qualcuno riceve l'evento, valuta il rinnovo e può revocare senza lasciare eccezioni invisibili.

La federazione può ridurre la duplicazione delle credenziali, ma introduce dipendenze da asserzioni, attributi, disponibilità e configurazioni tra sistemi. Prima di fidarsi di un'informazione ricevuta occorre definire quali attributi sono necessari, quale sistema li governa e che cosa accade quando sono assenti o obsoleti. Non occorre conoscere un prodotto per esporre questo punto: ogni integrazione di identità deve avere confini, proprietario, evidenze e procedura di revoca. L'esame valuta la capacità di collegare una scelta tecnica all'effetto sul servizio.

Un riesame ben progettato non chiede genericamente «tieni ancora l'accesso?». Confronta ruolo organizzativo, mansione, risorse assegnate, privilegi tecnici, eccezioni e attività recente. Il responsabile conferma o corregge una situazione documentata; il sistema registra la decisione e l'esecuzione. Così l'IAM sostiene anche continuità: in caso di assenza improvvisa, l'ente sa quali ruoli devono essere coperti senza condividere indiscriminatamente credenziali personali.

Una procedura di cessazione efficace include anche deleghe, caselle funzionali, dispositivi e rapporti con fornitori. Ogni elemento deve avere un proprietario che confermi la revoca e un'evidenza dell'esecuzione. In questo modo l'uscita di una persona non lascia capacità tecniche attive senza responsabilità.
## N-TR01-09-02 · Autenticazione, autorizzazione e privilegi

L'identificazione presenta un'identità; l'autenticazione verifica un autenticatore; l'autorizzazione decide se quell'identità possa eseguire un'azione; l'accounting registra l'attività. Un login riuscito non prova il diritto a consultare una pratica o a disporre un pagamento. Questa sequenza permette di individuare dove nasce il problema: un'identità non verificata, una sessione sottratta, un'autorizzazione eccessiva oppure un'azione non tracciata richiedono risposte diverse.

La MFA combina fattori indipendenti, non due copie dello stesso segreto. Riduce alcuni rischi ma non elimina la necessità di un enrollment affidabile, di un recupero account governato e di revocare sessioni e token quando serve. Anche nella federazione, in cui un servizio accetta un'asserzione di un identity provider, il servizio deve decidere localmente quali operazioni autorizzare. Confondere autenticazione federata e autorizzazione applicativa espone a privilegi concessi per inerzia.

Nel RBAC i permessi sono associati a ruoli; nell'ABAC la decisione usa attributi di soggetto, risorsa, azione e contesto; una ACL associa direttamente soggetti e permessi a una risorsa. Il RBAC è utile per compiti stabili e ripetibili. L'ABAC esprime regole contestuali, ma dipende dalla qualità e dall'aggiornamento degli attributi. Le ACL risolvono eccezioni puntuali, ma diventano difficili da governare se sostituiscono un modello generale. Nessun modello è automaticamente migliore: la scelta dipende da processo, frequenza dei cambiamenti e bisogno di dimostrare la decisione.

Il minimo privilegio assegna solo ciò che serve, per il tempo necessario. La separazione dei compiti evita che una persona svolga da sola attività incompatibili. Privilegi just-in-time e just-enough limitano durata e ampiezza dell'elevazione; il controllo degli accessi amministrativi richiede proprietario, approvazione, sessione tracciata e riesame. Il principio operativo è deny by default: quando nessuna regola consente l'azione, il servizio la nega. Il controllo deve stare lato servizio; nasconderne un pulsante nell'interfaccia non impedisce chiamate dirette.

In un ufficio contributi, un istruttore può leggere e aggiornare pratiche della propria unità, mentre l'approvazione appartiene a un responsabile diverso. Il ruolo spiega il permesso base; attributi come ufficio, rapporto attivo e stato della pratica possono limitarne l'uso; un'eccezione circoscritta richiede motivazione e scadenza. L'errore tipico è chiamare «sicuro» un accesso perché protetto da MFA: la MFA verifica il soggetto, non dimostra che il privilegio sia appropriato.

L'autorizzazione va verificata vicino alla risorsa e all'azione sensibile. Un portale può mostrare una pratica a un utente, ma il servizio deve controllare di nuovo identità, ruolo, ambito e stato quando riceve la richiesta di modifica o approvazione. Il controllo lato server riduce il rischio che una pagina nascosta o una chiamata costruita dall'esterno aggiri la logica dell'interfaccia. Le decisioni più rilevanti devono lasciare un'evidenza sufficiente a ricostruire regola applicata, esito e soggetto.

La gestione dei privilegi richiede anche una procedura per le eccezioni. Un accesso temporaneo può essere necessario per un'emergenza o per una verifica tecnica; deve però avere motivo, approvazione, durata, risorsa limitata e riesame successivo. Un'eccezione senza scadenza diventa spesso un ruolo parallelo non controllato. La disponibilità del servizio non giustifica il mantenimento indefinito di un accesso amministrativo.

Quando il sistema usa attributi, deve gestire anche la loro qualità. Un attributo di ufficio non aggiornato può autorizzare una pratica fuori contesto; un attributo mancante può bloccare un'operazione legittima. Per questo RBAC e ABAC non si valutano con una sigla: occorre chiedere quale fonte alimenta i dati, chi la mantiene, come si gestiscono conflitti e ritardi e quale sia il comportamento sicuro in caso di dubbio. La risposta concorsuale diventa concreta quando include questa catena di responsabilità.

La scelta del modello deve essere documentata con esempi di operazioni consentite e negate. Test di autorizzazione ripetibili dimostrano che il privilegio atteso funziona e che una modifica non ha ampliato involontariamente l'accesso.

Ogni autorizzazione significativa deve poter essere spiegata, testata e riesaminata in modo proporzionato.
## N-TR01-09-03 · Crittografia e gestione delle chiavi

La crittografia protegge proprietà specifiche; non sostituisce IAM, hardening, gestione delle vulnerabilità o continuità. La cifratura simmetrica usa una chiave condivisa e tutela soprattutto la riservatezza. Quella asimmetrica usa una coppia di chiavi ed è utile in scenari diversi, ma non è una scelta automaticamente più efficace. Un hash produce un'impronta non reversibile; un MAC usa un segreto per sostenere integrità e autenticità; una firma digitale consente verifiche con la chiave pubblica corrispondente; un certificato collega una chiave pubblica a un soggetto. Confondere questi strumenti porta a promettere proprietà che non offrono.

La cifratura del disco protegge principalmente il supporto quando esce dal sistema autorizzato; non impedisce a un account legittimamente abilitato di leggere il dato. La cifratura del canale protegge il trasferimento; non risolve da sola un endpoint compromesso. Dati in transito, a riposo e in uso hanno esposizioni diverse e richiedono un'architettura proporzionata. La pseudonimizzazione non coincide con la cifratura: riduce la riconducibilità diretta ma può richiedere informazioni aggiuntive governate separatamente. Il capitolo 10 affronta la governance del dato; qui interessa collegare la scelta tecnica alla proprietà da proteggere.

La sicurezza della chiave è parte della sicurezza del dato. Il ciclo di vita comprende generazione, inventario, distribuzione, conservazione, uso, rotazione, revoca, eventuale recupero, archiviazione e distruzione. Per ogni chiave, certificato o secret servono almeno scopo, proprietario, custode, sistemi dipendenti, stato e scadenza. Un servizio HSM o di key management può ridurre errori operativi, ma non decide da sé chi autorizza l'uso, quali copie esistono o quando un materiale deve essere revocato.

Rotazione e revoca non sono sinonimi. La rotazione sostituisce un materiale ancora ritenuto affidabile secondo la politica o il rischio; la revoca dichiara che non deve più essere accettato, ad esempio dopo una compromissione. Distribuire un nuovo secret senza aggiornare tutte le dipendenze può interrompere il servizio. Cambiarlo senza valutare copie, log e possibili usi precedenti può lasciare irrisolto l'incidente. La separazione di ruoli limita il rischio che chi custodisce il materiale possa autorizzare da solo ogni operazione sensibile.

Se un secret applicativo risulta esposto, il primo compito è capire quali servizi, ambienti e dati dipendano da esso. Il team limita l'uso, preserva le evidenze, valuta revoca o sostituzione, distribuisce il nuovo materiale in modo controllato e osserva i log per stimare l'impatto. Non occorrono dettagli di prodotto per esporre il ragionamento. L'errore tipico è credere che un algoritmo robusto compensi un inventario assente o un secret inserito nel codice.

Un inventario non è una lista di valori segreti da copiare in un foglio. Registra riferimenti, proprietà e dipendenze senza esporre il materiale sensibile. Deve consentire di rispondere a domande pratiche: quale servizio usa questa chiave, quale certificato sta per scadere, chi autorizza un rinnovo, quale componente si ferma se il secret viene revocato? Senza queste informazioni, la rotazione diventa una modifica rischiosa e la risposta a una compromissione procede per tentativi.

Proteggere il materiale crittografico comprende controllo degli accessi, separazione di ambienti, registrazione degli usi sensibili e backup coerenti con il rischio. Il recupero di una chiave può essere necessario per continuità o obblighi di conservazione, ma amplia il numero di copie e soggetti da governare. Non è quindi un dettaglio tecnico isolato: è una decisione di processo, con proprietario, autorizzazione e test. Il candidato non deve proporre algoritmi o parametri senza un contesto aggiornato.

Anche il certificato richiede ciclo di vita. Scadenza, rinnovo, sostituzione e revoca possono interrompere integrazioni se non sono pianificati. La continuità non consiste nel ignorare una scadenza, ma nel predisporre inventario, allerta, prova del rinnovo e rollback controllato. L'errore opposto è conservare lo stesso materiale troppo a lungo per timore del disservizio: in quel caso un'esigenza di esercizio annulla la possibilità di reagire correttamente a una perdita di fiducia.
## N-TR01-09-04 · Logging, rilevazione e triage

Un evento è un fatto osservabile; un log è la sua registrazione; un audit trail permette di ricostruire attività rilevanti; un alert è una segnalazione prodotta da una regola o da un'analisi; un incidente compromette o minaccia obiettivi di sicurezza o servizio. Un alert apre quindi una verifica: non prova da solo l'esistenza di un incidente. La distinzione evita sia allarmi ignorati sia escalation che paralizzano l'ente senza evidenze sufficienti.

Le sorgenti includono identity provider, sistemi operativi, reti, applicazioni, database, API, cloud e dispositivi. Un record utile contiene timestamp, identità o soggetto tecnico, azione, risorsa, esito, origine, contesto e un identificatore di correlazione. Il dato registrato deve essere pertinente: inserire password, token o dati personali non necessari nei log crea un nuovo rischio. Orologi incoerenti rendono fragile una timeline; accessi, modifica e cancellazione dei log devono essere governati; la conservazione dipende da finalità, rischio e obblighi applicabili, non da una durata universale.

La centralizzazione aiuta a correlare dati che resterebbero isolati. Un SIEM raccoglie, normalizza e mette in relazione eventi, ma non corregge log incompleti né sostituisce l'analista. Una regola troppo sensibile genera falsi positivi e consuma capacità di triage; una regola permissiva produce falsi negativi e ritarda la rilevazione. Baseline, soglie e casi d'uso devono essere legati ai servizi e riesaminati quando cambiano utenti, architettura o processi.

Il triage separa fatti documentati e ipotesi da verificare. Chiarisce attendibilità del segnale, identità coinvolte, privilegi, servizio, possibile diffusione, dati interessati e decisore. Un registro essenziale annota fonte, orario, azione, responsabile e risultato. È preferibile dichiarare «origine da verificare» piuttosto che trasformare una correlazione in una certezza. La qualità del ragionamento conta più della velocità di attribuire una causa.

Per un'elevazione anomala di privilegi, il team confronta log dell'identità, dell'applicazione e della risorsa interessata; verifica orari, sessione, origine, cambiamenti di ruolo e operazioni successive; poi valuta severità e attiva i ruoli necessari. L'errore tipico è installare un SIEM e considerare concluso il problema: servono scopo, sorgenti, campi, integrità, accesso governato, analisi ed esercitazioni.

La progettazione del logging parte dai casi d'uso: accessi privilegiati, modifiche di autorizzazione, operazioni su dati rilevanti, errori ripetuti, integrazioni fallite e azioni amministrative richiedono campi e correlazioni diversi. Registrare tutto senza criterio aumenta costo, rumore e rischio privacy; registrare troppo poco rende impossibile ricostruire una decisione. Una matrice sorgente-evento-campo-responsabile aiuta a rendere esplicita questa scelta prima dell'incidente.

L'integrità non significa soltanto impedire la cancellazione. Occorre definire chi può accedere ai log, chi può configurarli, chi può esportarli e quali tracce restano di queste stesse operazioni. Se chi compie un'azione può alterare liberamente la sua registrazione, l'audit trail perde affidabilità. I privilegi sul sistema di logging devono quindi essere separati, riesaminati e collegati a un processo di conservazione e dismissione.

Un alert utile è spiegabile. La regola indica quali condizioni hanno generato il segnale e quali dati servono per controllarlo; l'analista annota perché lo ha confermato, escluso o elevato. Questo feedback migliora la regola e la baseline. L'errore tipico è misurare il numero di alert invece della qualità delle decisioni: molte segnalazioni non dimostrano una capacità di rilevazione se nessuno può qualificarle entro un tempo coerente con il servizio.

La disponibilità dei log è anch'essa una dipendenza di servizio: una raccolta interrotta nel momento critico impedisce di valutare l'evento. Il monitoraggio deve quindi controllare anche copertura e salute delle sorgenti, non solo il loro contenuto. Il responsabile verifica periodicamente che i campi siano ancora prodotti dopo aggiornamenti o cambi di configurazione.

La verifica periodica deve produrre un esito, una correzione assegnata e una nuova prova di efficacia, non soltanto un controllo dichiarato.

Il controllo periodico mantiene attendibili le fonti e le correlazioni necessarie.
## N-TR01-09-05 · Incident response e continuità del servizio

La risposta a un incidente inizia prima dell'incidente. Policy, contatti, ruoli, accessi di emergenza, capacità di logging e prove di coordinamento fanno parte della preparazione. Il NIST CSF 2.0 collega la risposta alla governance, all'identificazione e alla protezione: rilevare, rispondere e recuperare non sono una sequenza isolata dal rischio e dalla continuità. Il modello locale può cambiare, ma deve chiarire decisioni, responsabilità, evidenze e condizioni di chiusura.

L'analisi definisce perimetro, vettore plausibile, identità, privilegi, sistemi, dati, dipendenze e timeline. La severità considera servizio, diffusione, impatto, urgenza e incertezza residua. Il contenimento limita danno e propagazione: può includere revoca di sessioni, sospensione di account o isolamento di componenti. Non è una reazione automatica. Isolare un sistema può preservare sicurezza ma interrompere un servizio essenziale o modificare evidenze; la decisione richiede un responsabile e una motivazione registrata.

L'eradicazione rimuove causa e persistenza; il recupero verifica identità, configurazioni, integrità, chiavi, dipendenze e monitoraggio. Le attività forensi non vanno improvvisate: acquisizione, conservazione e trattamento delle evidenze seguono competenze, autorizzazioni e procedure applicabili. Il capitolo 7 tratta backup e disaster recovery; qui il raccordo consiste nel chiedere se il servizio può rientrare in condizioni controllate e se il recupero reintroduce credenziali, configurazioni o dati compromessi.

Il playbook assegna ruoli: coordinatore dell'incidente, analista tecnico, responsabile del servizio, funzione di sicurezza, privacy, comunicazione, vertice e fornitori quando pertinenti. Una buona escalation distingue piano tecnico, decisioni sul servizio, valutazione privacy e interlocuzione istituzionale. La comunicazione non è un messaggio generico: deve dichiarare ciò che è noto, ciò che è ancora un'ipotesi, il canale e il prossimo aggiornamento. La timeline conserva fatti, fonti, decisioni e responsabili.

La chiusura richiede servizio stabile, evidenze custodite, comunicazioni svolte e azioni residue assegnate. Il riesame finale trasforma l'incidente in miglioramenti verificabili: correzione dei privilegi, rotazione di materiali, regole di rilevazione, esercitazioni, formazione o modifica del playbook. L'errore tipico è chiudere appena il servizio torna disponibile: recupero tecnico e apprendimento organizzativo sono entrambi necessari.

La continuità modifica le decisioni di risposta ma non le sostituisce. Se un servizio è essenziale, il coordinatore può scegliere un contenimento graduale, una modalità degradata o un ripristino da un ambiente controllato; deve però dichiarare quale rischio rimane e quali evidenze occorre preservare. Backup e replica possono aiutare a recuperare, ma non garantiscono che dati, configurazioni o credenziali ripristinate siano affidabili. L'analisi dell'incidente precede il rientro pieno in esercizio.

Il rapporto con i fornitori deve essere preparato prima dell'evento. Contatti, ruoli, accessi, evidenze disponibili e canali di escalation devono essere conosciuti senza trasferire automaticamente all'esterno la responsabilità dell'ente. Durante l'incidente il fornitore può fornire dati tecnici o intervenire su un componente, mentre il responsabile del servizio mantiene la visione delle conseguenze amministrative e della comunicazione. Il capitolo 12 approfondisce SLA e requisiti contrattuali; qui basta rendere esplicita la dipendenza.

Le esercitazioni verificano se numeri di reperibilità, privilegi di emergenza, log e ruoli funzionano davvero. Un playbook mai provato tende a contenere passaggi ambigui scoperti quando il tempo è scarso. Dopo l'esercitazione o l'incidente, le azioni di miglioramento devono avere responsabile, priorità ed evidenza di chiusura. «Fare formazione» è troppo generico se non indica a chi, su quale decisione e con quale verifica.

Una decisione di contenimento va riesaminata se cambiano le evidenze. Per esempio, una sospensione inizialmente limitata può diventare più ampia se emergono privilegi aggiuntivi, oppure essere ridotta se una verifica esclude la propagazione. Documentare il perché consente di bilanciare sicurezza, continuità e proporzionalità.

Il piano indica anche chi autorizza il rientro, quali controlli restano rafforzati e quando il riesame conferma la chiusura.

Una procedura aggiornata riduce ritardi e contraddizioni tra team, evidenze e decisioni.

La documentazione consente inoltre un riesame indipendente delle scelte adottate durante l'emergenza.
## N-TR01-09-06 · PA, ACN, CSIRT, NIS2 e privacy

Nel quadro italiano, il d.lgs. 138/2024 recepisce la direttiva NIS2; ACN esercita le funzioni nazionali attribuite dalla disciplina e CSIRT Italia opera nel sistema di gestione degli incidenti. Il candidato deve mostrare che l'ente verifica il proprio inquadramento, la significatività dell'evento e le procedure applicabili. Non deve trasformare un riferimento tecnico volontario, come NIST, in un obbligo generale della PA né inventare soglie, canali o termini operativi.

Un incidente cyber e una violazione dei dati personali possono sovrapporsi, ma non coincidono. Il primo riguarda un evento che può compromettere sicurezza o continuità; la seconda richiede una valutazione specifica sul trattamento di dati personali e sui rischi per le persone fisiche. Una stessa evidenza può interessare team tecnico, responsabile del servizio e funzione privacy, ma le decisioni non diventano automaticamente identiche. Il playbook deve indicare chi valuta ciascun perimetro, usando fonti ufficiali aggiornate.

La governance non è delegabile alla sola funzione tecnica. Il vertice e i responsabili organizzativi devono disporre di informazioni affidabili per decidere su continuità, comunicazioni, fornitori, rischio residuo e miglioramenti. Il team tecnico conserva e interpreta evidenze; il responsabile del servizio valuta conseguenze sull'erogazione; la funzione privacy considera dati e persone interessate; gli interlocutori istituzionali sono attivati quando il caso e la disciplina lo richiedono. L'escalation è quindi una struttura di responsabilità, non una catena di e-mail.

Il confine con il capitolo 8 è netto: lì si costruiscono scenario, rischio e trattamento; qui si applicano a identità, chiavi, log e gestione dell'evento. Il confine con il capitolo 7 riguarda il ripristino: continuità e disaster recovery rendono possibile tornare operativi, mentre incident response decide come farlo senza perdere il controllo di evidenze, privilegi e causa dell'evento. Il confine con il capitolo 10 riguarda dati, classificazione e governance; qui il punto è che minimizzazione e accesso autorizzato ai log sono requisiti del processo.

In una risposta orale, è prudente dire: «verificherei subito il perimetro del soggetto, la natura e la significatività dell'evento, attivando in modo distinto le valutazioni cyber e privacy secondo le fonti ufficiali vigenti». È più corretto che recitare scadenze senza conoscere il caso. L'errore tipico è confondere la notifica con la gestione: la notifica, quando dovuta, è un esito di valutazioni documentate, non sostituisce contenimento, recupero e comunicazione interna.

Le fonti mobili richiedono una disciplina editoriale precisa. Il manuale può spiegare il metodo di valutazione e i ruoli, ma non può cristallizzare una procedura locale o un atto aggiornabile come se fosse universale. Per un caso reale, il playbook consulta testo vigente, istruzioni ACN applicabili e valutazione privacy competente. Questa cautela non riduce l'utilità della preparazione: insegna al candidato a distinguere un principio stabile dalla regola operativa da verificare.

La gestione delle comunicazioni richiede accuratezza. Un messaggio interno deve evitare di trasformare ipotesi in fatti; una comunicazione esterna deve rispettare competenze, canali e verifiche. Conservare una cronologia delle decisioni non serve solo a giustificare il passato: aiuta il vertice a comprendere opzioni, impatti e condizioni per riprendere il servizio. Le informazioni tecniche vengono tradotte in effetti sul servizio senza nascondere l'incertezza.

In un ente pubblico, la qualità della risposta si riconosce dalla capacità di mantenere insieme responsabilità, evidenze e tutela dell'utenza. Non è necessario promettere che ogni incidente sarà evitato. Occorre dimostrare che l'organizzazione sa rilevare, decidere, contenere, recuperare e apprendere, rispettando i confini fra competenze tecniche, organizzative e giuridiche. Questo è il criterio utile anche nella prova orale.

Il piano di risposta deve inoltre definire come raggiungere i responsabili fuori dall'orario ordinario e come sostituirli in caso di indisponibilità. Senza questa informazione, la catena di responsabilità resta teorica proprio quando il servizio richiede decisioni rapide e documentate.
## ▣ Verifica

### Caso guidato: account privilegiato compromesso

Alle 08:20 l'identity provider segnala l'accesso di un amministratore da una sorgente insolita. Poco dopo l'applicazione registra un'esportazione anomala; il titolare nega di essere operativo.

Il team conserva alert e log, controlla l'allineamento temporale e correla identità, sessione, origine, privilegi e azioni. Il coordinatore decide il contenimento: revoca sessioni e sospende l'account, controllando token, recupero e account tecnici collegati. L'analisi cerca modifiche ai privilegi, persistenze ed esportazioni; il responsabile del servizio valuta l'impatto; la funzione privacy valuta separatamente l'eventuale violazione di dati personali. Il recupero include rimozione della causa, rotazione del materiale coinvolto, ripristino con privilegi minimi e monitoraggio rafforzato. Il riesame introduce elevazione temporanea, revoca centralizzata ed esercitazioni.

### Laboratorio: playbook e timeline

| Campo | Domanda da compilare |
| --- | --- |
| Trigger | quale evidenza avvia il triage? |
| Severità | quali servizio, privilegi, dati e diffusione sono coinvolti? |
| Coordinatore | chi mantiene decisioni e quadro di situazione? |
| Azioni | quali validazioni, evidenze e contenimenti servono? |
| Escalation | quali piani tecnico, servizio, privacy e istituzionale vanno valutati? |
| Recupero | quali condizioni permettono il rientro? |
| Chiusura | quali evidenze e azioni residue confermano la stabilità? |

| Ora | Fatto o ipotesi | Fonte | Decisione | Responsabile | Esito |
| --- | --- | --- | --- | --- | --- |
| 08:20 | accesso amministrativo anomalo | log IdP | aprire il triage | analista SOC | caso preso in carico |
| 08:27 | esportazione anomala confermata | log applicativo | elevare la severità | coordinatore | referenti attivati |
| 08:35 | il titolare nega l'accesso | contatto verificato | revocare sessioni e sospendere l'account | responsabile IAM | contenimento eseguito |
| da compilare | fatto o ipotesi | evidenza | decisione motivata | ruolo | risultato |

### Sei quiz commentati

1. **Un login riuscito dimostra automaticamente che l'utente può approvare una pratica?** Risposta corretta: no. Il login riguarda autenticazione; l'approvazione richiede un'autorizzazione verificata dal servizio.
2. **Due password costituiscono MFA?** Risposta corretta: no. I fattori devono essere indipendenti; duplicare un segreto non aggiunge una categoria di prova distinta.
3. **Hash e cifratura sono equivalenti?** Risposta corretta: no. L'hash produce un'impronta non reversibile; la cifratura mira alla riservatezza mediante una chiave.
4. **Un alert equivale a un incidente?** Risposta corretta: no. È un segnale da qualificare con fonti, contesto, impatto e controlli prima dell'escalation.
5. **La revoca è una semplice rotazione?** Risposta corretta: no. La rotazione sostituisce materiale ancora affidabile; la revoca ne dichiara la non validità, ad esempio dopo sospetta compromissione.
6. **Una notifica cyber coincide sempre con un data breach?** Risposta corretta: no. I presupposti possono concorrere ma restano distinti; il caso richiede valutazioni documentate e fonti ufficiali vigenti.

### Domanda da commissario

**«Come imposteresti la risposta alla compromissione di un account privilegiato?»**

Validerei il segnale e preserverei le evidenze; identificherei account, sessioni, privilegi, sistemi e dati; valuterei impatto e propagazione; attiverei i ruoli pertinenti. Conterrei senza distruggere evidenze, rimuoverei causa e persistenze, ruoterei il materiale interessato e ripristinerei con monitoraggio rafforzato. Chiuderei con timeline, azioni assegnate e lesson learned.

### Errore tipico

Affidarsi a un solo controllo: una MFA con recupero debole, una cifratura con chiave esposta o un SIEM alimentato da log incompleti danno un falso senso di sicurezza.

### Da sapere in 5 righe

IAM governa identità, account e privilegi lungo il ciclo di vita. Autenticare non significa autorizzare. La crittografia protegge proprietà definite solo se chiavi e secret sono governati. I log sono utili quando completi, coerenti e protetti. Incident response coordina triage, contenimento, recupero, comunicazione e apprendimento.

## Riferimenti normativi e professionali essenziali

- NIST SP 800-63-4, per identità, autenticazione e federazione.
- NIST SP 800-57 Part 1 rev. 5, per concetti di key management.
- NIST SP 800-92 e progetto di revisione, per log management.
- NIST SP 800-61 rev. 3 e NIST CSF 2.0, per raccordo tra risposta, recupero e gestione del rischio.
- D.lgs. 4 settembre 2024, n. 138 e atti ACN/CSIRT Italia applicabili, da verificare al cut-off sul caso concreto.
- GDPR e fonti del Garante, per la distinta valutazione delle violazioni di dati personali.