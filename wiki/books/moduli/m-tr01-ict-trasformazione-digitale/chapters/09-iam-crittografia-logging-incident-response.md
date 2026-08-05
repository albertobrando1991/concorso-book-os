---
id: chapter-m-tr01-09
type: book_chapter
title: "IAM, crittografia, logging e incident response"
status: reviewed-draft
domain: "concorsi pubblici italiani"
topics: ["iam", "crittografia", "logging", "incident response"]
entities: ["Agenzia per la cybersicurezza nazionale"]
source_refs: ["sources/iam-crittografia-logging-incident-response-fonti-primarie", "sources/sicurezza-informatica-privacy-nis2-pa", "sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/campione-bandi-ict-pa-vol-08-2024-2026", "sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08"]
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.86
updated_at: 2026-08-05
created_at: 2026-07-28
review_required: false
canonical: true
tags: ["chapter", "m-tr01"]
book_id: m-tr01-ict-trasformazione-digitale
outline_section: 9
draft_stage: cross-reviewed
last_compiled_from: ["sources/iam-crittografia-logging-incident-response-fonti-primarie", "topics/iam-crittografia-logging-incident-response", "topics/sicurezza-informatica"]
---

# IAM, crittografia, logging e incident response

## Obiettivo e Mappa BANDO

Un servizio pubblico digitale è affidabile se l'ente sa chi opera, che cosa può fare, quali tracce lascia e come reagire alle anomalie. IAM, crittografia, logging e incident response sono strettamente collegati: governano gli accessi, proteggono le informazioni e permettono di riconoscere e gestire gli incidenti. Il volume base introduce MFA e sicurezza; qui si sviluppano ciclo delle identità, privilegi, chiavi, qualità dei log, triage e playbook.

| Area | Nucleo | Output |
| --- | --- | --- |
| Accesso | identità, autenticazione, autorizzazione | matrice ruolo-risorsa-permesso |
| Protezione | crittografia e chiavi | checklist del ciclo delle chiavi |
| Osservabilità | log, correlazione, alert | matrice sorgente-evento-alert |
| Risposta | triage, contenimento, recupero | playbook e timeline |

## Identità, account e ciclo di vita

L'identità digitale rappresenta una persona, un'applicazione, un servizio, un dispositivo o un workload. L'**account** è il contenitore operativo; la **credenziale** lega l'identità a elementi riconosciuti; l'**autenticatore** dimostra il controllo della credenziale; la **sessione** mantiene l'esito dell'autenticazione; un **attributo** descrive soggetto o contesto. Disabilitare l'account principale, però, non revoca necessariamente token, sessioni, account amministrativi o chiavi API.

L'identity proofing stabilisce chi sia il soggetto; l'enrollment lo registra; il provisioning crea account e accessi. Nel **joiner** una fonte autorevole attesta il rapporto e il ruolo. Quando la persona cambia mansione (**mover**), occorre rimuovere i diritti che non servono più, non soltanto aggiungerne di nuovi. Con il **leaver** si revocano account, sessioni, token, chiavi e deleghe. Ogni fase lascia richiesta, approvazione, esecuzione ed evidenza.

Gli account nominativi rendono attribuibile l'azione. Quelli condivisi indeboliscono l'accountability e richiedono controlli compensativi. Gli account di servizio hanno proprietario, scopo, privilegi minimi e rotazione. Gli account di emergenza devono essere pochi, protetti, monitorati e revisionati dopo l'uso.

## Autenticazione, autorizzazione e privilegi

L'**identificazione** presenta un'identità; l'**autenticazione** verifica l'autenticatore; l'**autorizzazione** decide se l'identità possa agire sulla risorsa; l'**accounting** registra l'attività. Un login riuscito non prova il diritto a consultare una pratica o autorizzare un pagamento.

La MFA combina fattori indipendenti: due password non sono due fattori. Resta comunque necessario proteggere l'intero processo, perché un recupero account debole, il furto della sessione o il phishing in tempo reale possono aggirarla. Servono enrollment protetto, recupero governato e revoca delle sessioni. Nella federazione il servizio si affida alle asserzioni di un identity provider, ma resta responsabile dell'autorizzazione locale.

Nel **RBAC** i permessi sono associati ai ruoli. Nell'**ABAC** la decisione usa attributi di soggetto, risorsa, azione e contesto. Una **ACL** associa soggetti e permessi a una risorsa. Il minimo privilegio assegna soltanto i diritti necessari, per il tempo necessario; la separazione dei compiti evita attività incompatibili. Just-in-time e just-enough limitano durata e ampiezza dei privilegi.

In un ufficio contributi, il RBAC può assegnare al ruolo istruttore la lettura e l'aggiornamento delle pratiche, riservando l'approvazione al responsabile. L'ABAC può aggiungere condizioni: la pratica appartiene all'ufficio del soggetto, il rapporto di lavoro è attivo e l'operazione avviene nel contesto previsto. Una ACL può infine concedere un accesso eccezionale a una singola pratica. Il RBAC semplifica l'amministrazione di permessi stabili; l'ABAC esprime decisioni più contestuali, ma dipende dalla qualità degli attributi; le ACL sono immediate sul singolo oggetto, ma diventano difficili da governare su larga scala. L'autorizzazione deve negare l'operazione quando nessuna regola la consente e deve essere verificata dal servizio, non soltanto dall'interfaccia.

## Crittografia e gestione delle chiavi

| Meccanismo | Funzione prevalente | Errore da evitare |
| --- | --- | --- |
| cifratura simmetrica | riservatezza con chiave condivisa | distribuire la chiave con i dati |
| cifratura asimmetrica | coppia pubblica e privata | considerarla sempre più efficiente |
| hash | impronta non reversibile | chiamarlo cifratura |
| MAC | integrità e autenticità con segreto | confonderlo con firma |
| firma digitale | integrità e autenticità dell'origine | presumere che renda segreto il contenuto |
| certificato | lega chiave pubblica e soggetto | confonderlo con la firma |

La cifratura del disco protegge soprattutto il supporto fuori dal sistema autorizzato, non da un account abilitato. Quella del canale protegge il trasferimento, non un endpoint compromesso. Crittografia, IAM, hardening e logging sono complementari.

Anche una chiave robusta offre una protezione soltanto apparente se viene gestita male. Il ciclo comprende generazione, inventario, distribuzione, conservazione, uso, rotazione, revoca, eventuale recupero e distruzione. Per ogni elemento occorrono almeno scopo, proprietario, custode, sistemi dipendenti, stato e scadenza. Chi genera o custodisce il materiale non dovrebbe poter autorizzare da solo ogni operazione sensibile: la separazione dei ruoli riduce errore e abuso.

La **rotazione** sostituisce periodicamente o per rischio una chiave ancora affidabile; la **revoca** dichiara che non deve più essere considerata valida, per esempio dopo una compromissione. Distribuzione e conservazione devono impedire divulgazione e modifiche non autorizzate; backup e recupero, quando necessari, devono essere protetti e provati. I secret non vanno nel codice. HSM e servizi di key management aiutano, ma non sostituiscono policy e inventario.

Se un secret usato da un'applicazione viene esposto, il responsabile individua servizi, ambienti e dati dipendenti, ne limita l'uso, revoca o sostituisce il materiale, distribuisce il nuovo secret e controlla i log per stimare l'uso precedente. Cambiare la chiave senza aggiornare tutte le dipendenze può interrompere il servizio; cambiarla senza valutare le copie esposte lascia irrisolto l'incidente.

## Logging, rilevazione e triage

Un **evento** è un fatto osservabile; un **log** ne è la registrazione; un **audit trail** ricostruisce attività; un **alert** è una segnalazione prodotta da regole o analisi; un **incidente** compromette o minaccia obiettivi. L'alert, dunque, apre una verifica: non prova da solo che vi sia un incidente.

Le sorgenti includono identity provider, sistemi, reti, applicazioni, database, API e cloud. Un record utile contiene timestamp, identità, azione, risorsa, esito, origine, contesto e identificatore di sessione. Non deve contenere segreti o dati personali non necessari. Orologi incoerenti falsano la timeline; i log devono essere protetti da modifica e cancellazione. La conservazione dipende da finalità, rischio e obblighi: non esiste una durata universale.

Il SIEM raccoglie, normalizza e correla i dati. Non può però correggere log incompleti né sostituire il lavoro degli analisti. Regole troppo sensibili producono falsi positivi; regole permissive falsi negativi. Il triage chiarisce attendibilità, identità e servizi coinvolti, impatto e decisore. Il registro separa fatti documentati e ipotesi da verificare.

## Incident response

La risposta a un incidente comincia prima dell'incidente: servono policy, contatti, ruoli, strumenti, accessi di emergenza ed esercitazioni. Il modello NIST corrente la integra nel CSF 2.0: Govern, Identify e Protect preparano; Detect, Respond e Recover sostengono la gestione operativa.

Il playbook chiarisce chi coordina, chi analizza, chi risponde del servizio, chi valuta privacy e obblighi e chi interagisce con vertice e fornitori. L'analisi definisce perimetro, vettore, identità, privilegi, sistemi, dati e timeline. Il contenimento limita impatto mediante revoca di sessioni, sospensione di account o isolamento, bilanciando continuità ed evidenze. L'eradicazione rimuove causa e persistenza; attività forensi non vanno improvvisate.

Il recupero verifica identità, configurazioni, integrità, chiavi e monitoraggio. La chiusura richiede servizio stabile, evidenze custodite, comunicazioni svolte e azioni assegnate. Il riesame finale traduce quanto è accaduto in interventi misurabili, ciascuno con un responsabile e una verifica.

## PA, NIS2, CSIRT e privacy

Il d.lgs. 138/2024 recepisce la NIS2. ACN esercita le funzioni nazionali attribuite e CSIRT Italia opera nel sistema di gestione degli incidenti. L'ente verifica se rientra nella disciplina, valuta la significatività e applica procedure e canali vigenti. In parallelo, il referente privacy valuta l'eventuale violazione dei dati personali. Incidente cyber e data breach possono sovrapporsi, ma non coincidono. Procedure, tassonomie e scadenze devono essere controllate sulle fonti ufficiali al momento dell'applicazione.

## Caso guidato: account privilegiato compromesso

Alle 08:20 l'identity provider segnala l'accesso di un amministratore da una sorgente insolita. Poco dopo l'applicazione registra un'esportazione anomala. Il titolare nega di essere operativo.

**Triage:** si conservano alert e log, si verifica il tempo e si correlano identità, sessione, origine e azioni. **Contenimento:** si revocano sessioni e account, controllando token e recupero. **Analisi:** si cercano modifiche ai privilegi, persistenze, accessi laterali ed esportazioni e si attivano i referenti privacy e istituzionali. **Eradicazione e recupero:** si rimuove la causa, si ruotano credenziali e chiavi e si ripristina con privilegi minimi e monitoraggio rafforzato. **Miglioramento:** si introducono elevazione temporanea, revoca centralizzata ed esercitazioni.

## Laboratorio: playbook e timeline

| Campo | Contenuto |
| --- | --- |
| Trigger | evidenza che avvia il triage |
| Severità | servizio, privilegi, dati, diffusione |
| Coordinatore | ruolo che tiene decisioni e situazione |
| Azioni | validazione, evidenze, contenimento |
| Escalation | tecnica, servizio, privacy, istituzionale |
| Recupero | condizioni per il rientro |
| Chiusura | criteri e azioni residue |

La timeline separa i fatti dalle ipotesi e collega ogni decisione alla fonte disponibile.

| Ora | Fatto o ipotesi | Fonte | Decisione | Responsabile | Esito |
| --- | --- | --- | --- | --- | --- |
| 08:20 | accesso amministrativo anomalo | log IdP | aprire il triage | analista SOC | caso preso in carico |
| 08:27 | esportazione anomala confermata | log applicativo | elevare la severità | incident manager | referenti attivati |
| 08:35 | il titolare nega l'accesso | contatto verificato | revocare sessioni e sospendere l'account | responsabile IAM | contenimento eseguito |
| da compilare | fatto o ipotesi | evidenza | decisione motivata | ruolo | risultato |

## Domanda da commissario

**«Come imposteresti la risposta alla compromissione di un account privilegiato?»**

Validerei il segnale e preserverei i log; identificherei account, sessioni, privilegi, sistemi e dati; valuterei impatto e propagazione; attiverei i referenti. Conterrei senza distruggere evidenze, rimuoverei causa e persistenze, ruoterei il materiale interessato e ripristinerei con monitoraggio rafforzato. Chiuderei con timeline e lesson learned.

## Domande-trappola ed errore tipico

Autenticazione riuscita non significa autorizzazione corretta; cifratura non elimina il controllo degli accessi; un log presente non è automaticamente integro; un alert non è automaticamente un incidente; isolare subito non è sempre corretto; notifica cyber e data breach non coincidono.

L'errore tipico è affidarsi a un solo controllo. Una MFA con recupero debole, una cifratura con chiave esposta o un SIEM alimentato da log incompleti danno un falso senso di sicurezza.

## Mini-esercizi e checklist

1. Classifica identificazione, autenticazione, autorizzazione e accounting in un login.
2. Per un cambio di ufficio, elenca accessi da aggiungere e rimuovere.
3. Associa riservatezza, impronta, MAC e firma al meccanismo corretto.
4. Ordina generazione, uso, rotazione, revoca e distruzione di una chiave.
5. Progetta i campi del log di elevazione privilegi.

Checklist: proprietari e riesami degli account; evidenze joiner-mover-leaver; inventario di chiavi e secret; log con tempo, integrità e accessi governati; triage e ruoli predefiniti; timeline con fatti, ipotesi e decisioni; criteri di recupero; valutazioni cyber e privacy separate.

## Da sapere in 5 righe

IAM governa identità, account e privilegi lungo il ciclo di vita. Autenticare non significa autorizzare. La crittografia protegge proprietà specifiche soltanto se le chiavi sono governate. I log sono utili quando completi, coerenti e protetti. L'incident response coordina triage, contenimento, recupero, comunicazione e apprendimento.

## Riferimenti consolidati

- [[sources/iam-crittografia-logging-incident-response-fonti-primarie]]
- [[sources/sicurezza-informatica-privacy-nis2-pa]]
- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]]
- [[sources/campione-bandi-ict-pa-vol-08-2024-2026]]
- [[sources/modulo-m-tr01-ict-digitale-cybersecurity-dati-vol-08]]
- [[topics/iam-crittografia-logging-incident-response]]
- [[topics/sicurezza-informatica]]
- [[entities/agenzia-cybersicurezza-nazionale]]

## Note di review

- Audit specialistico concluso: d.lgs. 138/2024 e atti ACN sono verificati al cut-off; gli elementi mobili vanno ricontrollati sulle fonti ufficiali per casi successivi.
- Far validare IAM e privilegi da identity/PAM architect e key management da specialista crittografico.
- Far verificare log, triage e playbook da SOC/SIEM engineer e incident response lead.
- Far distinguere obblighi cyber e data breach da esperto ACN/NIS2 e DPO.