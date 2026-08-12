# Step 15 ? Audit atomico nuclei, batch B (capitoli 05?09)

- Data di controllo e cutoff: **2026-08-12**.
- Revisore: `codex-step15-batch-b`; gate: `step-15`.
- Perimetro: 30 nuclei (capitoli 05?09). Dossier di sola evidenza: non modifica capitoli, manifest, matrice o run-state e non promuove automaticamente i nuclei.
- Regola Q/C/E: gli apparati finali di capitolo restano **chapter-level non-atomic** quando il testo non li collega espressamente a un singolo nucleo; non sono retroattribuiti.

## Esito sintetico

- Record e ID unici: **30/30**.
- Quote letterali complete con riscontro nel nucleo: **30/30**.
- Teoria: **30 PASS** sulla citazione letterale e sulla fonte consolidata indicata.
- Applicazione: **6 nuclei con sottosezione esplicita; 24 senza applicazione atomica.
- Output concorsuale e Q/C/E: **30 FAIL di tracciabilit?** ? i conteggi disponibili sono chapter-level e non vengono inventati o promossi.
- Fonti: capitolo 05 IETF/kernel; 06 AgID PDND/OpenAPI; 07 Cloud Italia/ACN; 08 NIST/FIRST/OWASP; 09 NIST/Normattiva. Nessuna ricerca estesa aggiuntiva; controllo riferito alle fonti consolidate del checkpoint.

## N-TR01-05-01

- **heading:** `## N-TR01-05-01 · Livelli, incapsulamento e rete locale`

- **sourceLocation:** `chapters/05-reti-sistemi-operativi-infrastrutture.md#n-tr01-05-01` ? ? heading `## N-TR01-05-01 · Livelli, incapsulamento e rete locale`, riga 58.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Una rete collega interfacce e sistemi affinché possano scambiare dati secondo regole condivise. I **protocolli** definiscono formato dei messaggi, significato dei campi e comportamento dei partecipanti.

- **Fonti consolidate:** `sources/reti-sistemi-infrastrutture-fonti-tecniche`; IETF RFC 9110 ? https://www.rfc-editor.org/rfc/rfc9110.
- **Verifica fonte:** IETF RFC Editor e Linux Kernel. Fonti tecniche consolidate; nessun dato mobile nel testo verificato. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-05-02

- **heading:** `## N-TR01-05-02 · Indirizzamento, subnetting e routing`

- **sourceLocation:** `chapters/05-reti-sistemi-operativi-infrastrutture.md#n-tr01-05-02` ? ? heading `## N-TR01-05-02 · Indirizzamento, subnetting e routing`, riga 100.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Un indirizzo IP identifica un’interfaccia nel contesto della rete. Il prefisso indica la parte usata per individuare la rete; i bit restanti distinguono le interfacce all’interno di quella rete.

- **Fonti consolidate:** `sources/reti-sistemi-infrastrutture-fonti-tecniche`; IETF RFC 4632 (CIDR) ? https://www.rfc-editor.org/rfc/rfc4632.
- **Verifica fonte:** IETF RFC Editor e Linux Kernel. Fonti tecniche consolidate; nessun dato mobile nel testo verificato. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-05-03

- **heading:** `## N-TR01-05-03 · Trasporto e servizi di rete`

- **sourceLocation:** `chapters/05-reti-sistemi-operativi-infrastrutture.md#n-tr01-05-03` ? ? heading `## N-TR01-05-03 · Trasporto e servizi di rete`, riga 141.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> L’etichetta “più veloce” non basta a descrivere UDP: contano rete, carico, dimensione dei messaggi e comportamento applicativo. TCP è adatto quando serve un flusso affidabile; UDP quando l’applicazione preferisce datagrammi, latenza contenuta o una gestione autonoma delle perdite.

- **Fonti consolidate:** `sources/reti-sistemi-infrastrutture-fonti-tecniche`; IETF RFC 9293 (TCP) e RFC 768 (UDP) ? https://www.rfc-editor.org/rfc/rfc9293 ; https://www.rfc-editor.org/rfc/rfc768.
- **Verifica fonte:** IETF RFC Editor e Linux Kernel. Fonti tecniche consolidate; nessun dato mobile nel testo verificato. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-05-04

- **heading:** `## N-TR01-05-04 · Sistema operativo, processi e servizi`

- **sourceLocation:** `chapters/05-reti-sistemi-operativi-infrastrutture.md#n-tr01-05-04` ? ? heading `## N-TR01-05-04 · Sistema operativo, processi e servizi`, riga 188.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Il sistema operativo gestisce CPU, memoria, dispositivi, file, identità e comunicazioni. Il **kernel** opera con privilegi elevati e media l’accesso alle risorse. Le applicazioni lavorano nello spazio utente e richiedono servizi al kernel attraverso interfacce definite.

- **Fonti consolidate:** `sources/reti-sistemi-infrastrutture-fonti-tecniche`; Linux Kernel documentation ? https://docs.kernel.org/.
- **Verifica fonte:** IETF RFC Editor e Linux Kernel. Fonti tecniche consolidate; nessun dato mobile nel testo verificato. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-05-05

- **heading:** `## N-TR01-05-05 · Memoria virtuale, file system e risorse`

- **sourceLocation:** `chapters/05-reti-sistemi-operativi-infrastrutture.md#n-tr01-05-05` ? ? heading `## N-TR01-05-05 · Memoria virtuale, file system e risorse`, riga 234.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La **memoria virtuale** assegna a ogni processo uno spazio di indirizzamento. Il sistema traduce indirizzi virtuali in memoria fisica mediante strutture come le tabelle delle pagine. Le pagine possono contenere memoria anonima, codice o dati di file.

- **Fonti consolidate:** `sources/reti-sistemi-infrastrutture-fonti-tecniche`; Linux Kernel memory management ? https://docs.kernel.org/mm/index.html.
- **Verifica fonte:** IETF RFC Editor e Linux Kernel. Fonti tecniche consolidate; nessun dato mobile nel testo verificato. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** PASS locale ? sottosezione/i: Diagnosi delle risorse senza affidarsi a un solo numero.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-05-06

- **heading:** `## N-TR01-05-06 · Disponibilità e troubleshooting infrastrutturale`

- **sourceLocation:** `chapters/05-reti-sistemi-operativi-infrastrutture.md#n-tr01-05-06` ? ? heading `## N-TR01-05-06 · Disponibilità e troubleshooting infrastrutturale`, riga 280.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La **disponibilità** descrive la capacità di offrire il servizio quando richiesto. A determinarla concorre l’intera catena: alimentazione, rete, calcolo, storage, applicazione, dati e dipendenze esterne.

- **Fonti consolidate:** `sources/reti-sistemi-infrastrutture-fonti-tecniche`; NIST SP 800-34 Rev.1 ? https://csrc.nist.gov/pubs/sp/800/34/r1/final.
- **Verifica fonte:** IETF RFC Editor e Linux Kernel. Fonti tecniche consolidate; nessun dato mobile nel testo verificato. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** PASS locale ? sottosezione/i: Caso guidato: portale interno non raggiungibile; Esercizio 2 — Diagnosi.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-06-01

- **heading:** `## N-TR01-06-01 · Requisiti e ciclo di vita verificabile`

- **sourceLocation:** `chapters/06-ingegneria-software-api-interoperabilita-pa.md#n-tr01-06-01` ? ? heading `## N-TR01-06-01 · Requisiti e ciclo di vita verificabile`, riga 59.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Un **bisogno** descrive il risultato atteso da un soggetto. Un **requisito** traduce quel bisogno in una proprietà o capacità che il sistema deve possedere. Un **vincolo** limita le soluzioni ammissibili: può derivare da norme, standard, tecnologie già presenti, tempi, budget o organizzazione. Il **criterio di accettazione** indica invece una condizione osservabile con cui stabilire se il requisito è soddisfatto.

- **Fonti consolidate:** `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; SWEBOK ? https://www.computer.org/education/bodies-of-knowledge/software-engineering.
- **Verifica fonte:** AgID/PDND, RFC Editor e OpenAPI Initiative. Interoperabilit? PA e contratti API: fonte istituzionale/primaria, cutoff 2026-08-12. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-06-02

- **heading:** `## N-TR01-06-02 · Architettura e qualità del software`

- **sourceLocation:** `chapters/06-ingegneria-software-api-interoperabilita-pa.md#n-tr01-06-02` ? ? heading `## N-TR01-06-02 · Architettura e qualità del software`, riga 102.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> L’**architettura software** descrive elementi significativi, responsabilità, relazioni e decisioni che condizionano l’evoluzione del sistema. Un **componente** racchiude una responsabilità; un’**interfaccia** espone modalità di interazione; una **dipendenza** indica che un elemento necessita di un altro.

- **Fonti consolidate:** `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; ISO/IEC/IEEE 42010 overview ? https://www.iso.org/standard/74393.html.
- **Verifica fonte:** AgID/PDND, RFC Editor e OpenAPI Initiative. Interoperabilit? PA e contratti API: fonte istituzionale/primaria, cutoff 2026-08-12. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-06-03

- **heading:** `## N-TR01-06-03 · Verifica, validazione, test e configurazione`

- **sourceLocation:** `chapters/06-ingegneria-software-api-interoperabilita-pa.md#n-tr01-06-03` ? ? heading `## N-TR01-06-03 · Verifica, validazione, test e configurazione`, riga 142.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La **verifica** controlla che il prodotto sia costruito secondo specifiche e progetto. La **validazione** controlla che il prodotto risponda al bisogno d’uso.

- **Fonti consolidate:** `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; SWEBOK Verification and Validation ? https://www.computer.org/education/bodies-of-knowledge/software-engineering.
- **Verifica fonte:** AgID/PDND, RFC Editor e OpenAPI Initiative. Interoperabilit? PA e contratti API: fonte istituzionale/primaria, cutoff 2026-08-12. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-06-04

- **heading:** `## N-TR01-06-04 · API come contratto`

- **sourceLocation:** `chapters/06-ingegneria-software-api-interoperabilita-pa.md#n-tr01-06-04` ? ? heading `## N-TR01-06-04 · API come contratto`, riga 189.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Un’**API** definisce come un sistema può richiedere capacità o dati a un altro. Il contratto comprende operazioni, indirizzamento, parametri, rappresentazioni, precondizioni, risposte, errori e vincoli di utilizzo. L’implementazione interna può cambiare senza rompere i fruitori finché il comportamento promesso resta compatibile.

- **Fonti consolidate:** `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; RFC 9110 / OpenAPI ? https://www.rfc-editor.org/rfc/rfc9110 ; https://spec.openapis.org/oas/latest.html.
- **Verifica fonte:** AgID/PDND, RFC Editor e OpenAPI Initiative. Interoperabilit? PA e contratti API: fonte istituzionale/primaria, cutoff 2026-08-12. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-06-05

- **heading:** `## N-TR01-06-05 · Evoluzione e gestione delle API`

- **sourceLocation:** `chapters/06-ingegneria-software-api-interoperabilita-pa.md#n-tr01-06-05` ? ? heading `## N-TR01-06-05 · Evoluzione e gestione delle API`, riga 237.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Una modifica è **compatibile** quando i fruitori conformi al contratto precedente possono continuare a funzionare. Aggiungere un campo opzionale può essere compatibile se i client ignorano elementi sconosciuti; rinominare un campo obbligatorio o cambiarne il tipo può rompere il contratto.

- **Fonti consolidate:** `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; OpenAPI Specification ? https://spec.openapis.org/oas/latest.html.
- **Verifica fonte:** AgID/PDND, RFC Editor e OpenAPI Initiative. Interoperabilit? PA e contratti API: fonte istituzionale/primaria, cutoff 2026-08-12. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-06-06

- **heading:** `## N-TR01-06-06 · Interoperabilità PA ed e-service`

- **sourceLocation:** `chapters/06-ingegneria-software-api-interoperabilita-pa.md#n-tr01-06-06` ? ? heading `## N-TR01-06-06 · Interoperabilità PA ed e-service`, riga 275.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> L’interoperabilità consente a organizzazioni e sistemi differenti di scambiare informazioni e usarle correttamente. Può essere letta sui livelli **giuridico**, **organizzativo**, **semantico** e **tecnico**.

- **Fonti consolidate:** `sources/ingegneria-software-api-interoperabilita-fonti-tecniche`; AgID Linee guida PDND ? https://www.agid.gov.it/sites/agid/files/2025-06/Linee_guida_Infrastruttura_Interoperabilita_PDND_v2_maggio_2025.pdf.
- **Verifica fonte:** AgID/PDND, RFC Editor e OpenAPI Initiative. Interoperabilit? PA e contratti API: fonte istituzionale/primaria, cutoff 2026-08-12. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** PASS locale ? sottosezione/i: Caso guidato: verifica di un requisito anagrafico.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-07-01

- **heading:** `## N-TR01-07-01 · Quadro, modelli cloud e responsabilità`

- **sourceLocation:** `chapters/07-cloud-pa-virtualizzazione-container-devops.md#n-tr01-07-01` ? ? heading `## N-TR01-07-01 · Quadro, modelli cloud e responsabilità`, riga 64.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Il modello cloud va letto come un insieme di caratteristiche operative e di confini di responsabilità. La risposta utile non si limita alle sigle: collega servizio, dati, soggetti coinvolti e conseguenze per l'ente.

- **Fonti consolidate:** `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; NIST SP 800-145 ? https://csrc.nist.gov/pubs/sp/800/145/final.
- **Verifica fonte:** Cloud Italia/ACN, NIST e Kubernetes. Qualificazione cloud PA e fonti tecniche controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-07-02

- **heading:** `## N-TR01-07-02 · Virtualizzazione, container e orchestrazione`

- **sourceLocation:** `chapters/07-cloud-pa-virtualizzazione-container-devops.md#n-tr01-07-02` ? ? heading `## N-TR01-07-02 · Virtualizzazione, container e orchestrazione`, riga 123.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Qui la questione decisiva è capire che cosa viene isolato, come viene distribuito e quali dati devono sopravvivere al riavvio. La tecnologia scelta deve rendere l'esercizio più controllabile, non soltanto più rapido da avviare.

- **Fonti consolidate:** `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; Kubernetes concepts ? https://kubernetes.io/docs/concepts/overview/.
- **Verifica fonte:** Cloud Italia/ACN, NIST e Kubernetes. Qualificazione cloud PA e fonti tecniche controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-07-03

- **heading:** `## N-TR01-07-03 · Cloud PA e percorso di migrazione`

- **sourceLocation:** `chapters/07-cloud-pa-virtualizzazione-container-devops.md#n-tr01-07-03` ? ? heading `## N-TR01-07-03 · Cloud PA e percorso di migrazione`, riga 169.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Una migrazione ordinata parte dalla funzione pubblica, non dalla piattaforma. Ogni scelta deve lasciare una motivazione, una prova e una via di ritorno praticabile.

- **Fonti consolidate:** `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; Cloud Italia / ACN ? https://cloud.italia.it/qualificazione-servizi-cloud/.
- **Verifica fonte:** Cloud Italia/ACN, NIST e Kubernetes. Qualificazione cloud PA e fonti tecniche controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-07-04

- **heading:** `## N-TR01-07-04 · DevOps, CI/CD e Infrastructure as Code`

- **sourceLocation:** `chapters/07-cloud-pa-virtualizzazione-container-devops.md#n-tr01-07-04` ? ? heading `## N-TR01-07-04 · DevOps, CI/CD e Infrastructure as Code`, riga 238.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La pipeline è una catena di responsabilità, non un semplice automatismo. Il codice viene associato a una richiesta, trasformato in un artefatto identificabile e sottoposto ai controlli adatti al suo impatto. L'artefatto verificato non dovrebbe cambiare mentre attraversa gli ambienti: altrimenti non si sa più se la produzione esegue ciò che è stato provato. Quando un controllo fallisce, il flusso deve fermarsi e produrre un'evidenza utile alla correzione.

- **Fonti consolidate:** `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; NIST SP 800-218 SSDF ? https://csrc.nist.gov/pubs/sp/800/218/final ; OpenTelemetry ? https://opentelemetry.io/docs/concepts/signals/.
- **Verifica fonte:** Cloud Italia/ACN, NIST e Kubernetes. Qualificazione cloud PA e fonti tecniche controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-07-05

- **heading:** `## N-TR01-07-05 · Operabilità, osservabilità, capacità e costi`

- **sourceLocation:** `chapters/07-cloud-pa-virtualizzazione-container-devops.md#n-tr01-07-05` ? ? heading `## N-TR01-07-05 · Operabilità, osservabilità, capacità e costi`, riga 285.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La capacità non riguarda soltanto il numero di server. Comprende connessioni, code, spazio, limiti imposti da servizi esterni e persone in grado di intervenire. Un piano di capacità confronta il profilo storico con gli eventi attesi, dichiara quale margine è necessario e stabilisce cosa fare quando il margine si riduce. Questo evita sia il sovradimensionamento costoso sia una reazione tardiva durante una scadenza.

- **Fonti consolidate:** `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; NIST SP 800-34 Rev.1 ? https://csrc.nist.gov/pubs/sp/800/34/r1/final.
- **Verifica fonte:** Cloud Italia/ACN, NIST e Kubernetes. Qualificazione cloud PA e fonti tecniche controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-07-06

- **heading:** `## N-TR01-07-06 · Resilienza, backup, disaster recovery e continuità operativa`

- **sourceLocation:** `chapters/07-cloud-pa-virtualizzazione-container-devops.md#n-tr01-07-06` ? ? heading `## N-TR01-07-06 · Resilienza, backup, disaster recovery e continuità operativa`, riga 320.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La scelta delle copie e delle architetture deve quindi essere proporzionata: non tutti i servizi richiedono la stessa rapidità di recupero, ma nessun servizio essenziale può basarsi su un ripristino mai eseguito.

- **Fonti consolidate:** `sources/cloud-virtualizzazione-container-devops-continuita-fonti-primarie`; NIST SP 800-34 Rev.1 ? https://csrc.nist.gov/pubs/sp/800/34/r1/final.
- **Verifica fonte:** Cloud Italia/ACN, NIST e Kubernetes. Qualificazione cloud PA e fonti tecniche controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** PASS locale ? sottosezione/i: Caso ragionato: migrazione di un servizio comunale.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-08-01

- **heading:** `## N-TR01-08-01 · Obiettivi di sicurezza e asset`

- **sourceLocation:** `chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md#n-tr01-08-01` ? ? heading `## N-TR01-08-01 · Obiettivi di sicurezza e asset`, riga 60.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Si aggiungono, secondo il contesto, autenticità, tracciabilità e accountability. Il non ripudio riguarda la capacità di impedire che un soggetto neghi in modo plausibile una determinata azione, quando il sistema e il quadro applicabile lo consentono. Queste proprietà non sono intercambiabili: la cifratura può sostenere la riservatezza, ma non garantisce da sola disponibilità o correttezza del processo.

- **Fonti consolidate:** `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; NIST CSF 2.0 ? https://www.nist.gov/cyberframework.
- **Verifica fonte:** NIST, FIRST e OWASP. Quadri e tassonomie tecniche controllati al cutoff; nessuna soglia operativa resa universale. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-08-02

- **heading:** `## N-TR01-08-02 · Minacce, vulnerabilità e scenari`

- **sourceLocation:** `chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md#n-tr01-08-02` ? ? heading `## N-TR01-08-02 · Minacce, vulnerabilità e scenari`, riga 105.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Una **minaccia** è una circostanza o causa potenziale capace di produrre un evento dannoso. Il **threat actor** è il soggetto che può agire intenzionalmente; non tutte le minacce, però, hanno un attore ostile: esistono errori, guasti ed eventi ambientali.

- **Fonti consolidate:** `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; NIST SP 800-30 Rev.1 ? https://csrc.nist.gov/pubs/sp/800/30/r1/final.
- **Verifica fonte:** NIST, FIRST e OWASP. Quadri e tassonomie tecniche controllati al cutoff; nessuna soglia operativa resa universale. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-08-03

- **heading:** `## N-TR01-08-03 · Valutazione e trattamento del rischio`

- **sourceLocation:** `chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md#n-tr01-08-03` ? ? heading `## N-TR01-08-03 · Valutazione e trattamento del rischio`, riga 150.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La probabilità stima quanto sia plausibile lo scenario, considerando capacità dell’attore, esposizione, frequenza, vulnerabilità e controlli. L’impatto considera conseguenze su servizi, dati, persone, finanze, conformità e fiducia istituzionale.

- **Fonti consolidate:** `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; NIST SP 800-30 Rev.1 ? https://csrc.nist.gov/pubs/sp/800/30/r1/final.
- **Verifica fonte:** NIST, FIRST e OWASP. Quadri e tassonomie tecniche controllati al cutoff; nessuna soglia operativa resa universale. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-08-04

- **heading:** `## N-TR01-08-04 · Controlli e difesa per livelli`

- **sourceLocation:** `chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md#n-tr01-08-04` ? ? heading `## N-TR01-08-04 · Controlli e difesa per livelli`, riga 215.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Le tassonomie possono variare; la classificazione chiarisce la funzione del controllo, non aggiunge etichette fini a sé stesse.

- **Fonti consolidate:** `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; NIST CSF 2.0 ? https://www.nist.gov/cyberframework.
- **Verifica fonte:** NIST, FIRST e OWASP. Quadri e tassonomie tecniche controllati al cutoff; nessuna soglia operativa resa universale. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-08-05

- **heading:** `## N-TR01-08-05 · Threat modeling e gestione delle vulnerabilità`

- **sourceLocation:** `chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md#n-tr01-08-05` ? ? heading `## N-TR01-08-05 · Threat modeling e gestione delle vulnerabilità`, riga 275.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> STRIDE è una tassonomia possibile: spoofing, tampering, repudiation, information disclosure, denial of service ed elevation of privilege. Non è l’unico metodo e non deve diventare un elenco scollegato dal sistema.

- **Fonti consolidate:** `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; OWASP Threat Modeling ? https://owasp.org/www-community/Threat_Modeling ; FIRST CVSS ? https://www.first.org/cvss/.
- **Verifica fonte:** NIST, FIRST e OWASP. Quadri e tassonomie tecniche controllati al cutoff; nessuna soglia operativa resa universale. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-08-06

- **heading:** `## N-TR01-08-06 · Secure SDLC e software supply chain`

- **sourceLocation:** `chapters/08-cybersecurity-rischio-controlli-vulnerabilita.md#n-tr01-08-06` ? ? heading `## N-TR01-08-06 · Secure SDLC e software supply chain`, riga 339.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Il NIST SSDF integra pratiche di sicurezza nel ciclo di sviluppo. Le pratiche di sicurezza accompagnano requisiti, progettazione, implementazione, verifica, rilascio, esercizio e dismissione.

- **Fonti consolidate:** `sources/cyber-risk-vulnerabilita-secure-software-supply-chain-fonti-primarie`; NIST SP 800-218 SSDF ? https://csrc.nist.gov/pubs/sp/800/218/final ; OWASP ASVS ? https://owasp.org/www-project-application-security-verification-standard/.
- **Verifica fonte:** NIST, FIRST e OWASP. Quadri e tassonomie tecniche controllati al cutoff; nessuna soglia operativa resa universale. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** PASS locale ? sottosezione/i: Caso guidato: portale per le domande.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-09-01

- **heading:** `## N-TR01-09-01 · Identità, account e ciclo di vita`

- **sourceLocation:** `chapters/09-iam-crittografia-logging-incident-response.md#n-tr01-09-01` ? ? heading `## N-TR01-09-01 · Identità, account e ciclo di vita`, riga 42.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Un'identità digitale rappresenta una persona, un'applicazione, un servizio, un dispositivo o un workload. L'account è il contenitore operativo usato dal sistema; una credenziale è un elemento associato all'identità; un autenticatore dimostra il controllo della credenziale; la sessione conserva l'esito dell'accesso; un attributo descrive soggetto, ruolo o contesto. Distinguere questi elementi evita un errore frequente: disabilitare un account non revoca automaticamente sessioni, token, chiavi applicative o account amministrativi collegati.

- **Fonti consolidate:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; NIST SP 800-63-4 ? https://csrc.nist.gov/pubs/sp/800/63/4/final.
- **Verifica fonte:** NIST e Normattiva. Fonti NIST e disciplina italiana/NIS2 controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-09-02

- **heading:** `## N-TR01-09-02 · Autenticazione, autorizzazione e privilegi`

- **sourceLocation:** `chapters/09-iam-crittografia-logging-incident-response.md#n-tr01-09-02` ? ? heading `## N-TR01-09-02 · Autenticazione, autorizzazione e privilegi`, riga 63.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> L'identificazione presenta un'identità; l'autenticazione verifica un autenticatore; l'autorizzazione decide se quell'identità possa eseguire un'azione; l'accounting registra l'attività. Un login riuscito non prova il diritto a consultare una pratica o a disporre un pagamento. Questa sequenza permette di individuare dove nasce il problema: un'identità non verificata, una sessione sottratta, un'autorizzazione eccessiva oppure un'azione non tracciata richiedono risposte diverse.

- **Fonti consolidate:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; NIST SP 800-63-4 ? https://csrc.nist.gov/pubs/sp/800/63/4/final.
- **Verifica fonte:** NIST e Normattiva. Fonti NIST e disciplina italiana/NIS2 controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-09-03

- **heading:** `## N-TR01-09-03 · Crittografia e gestione delle chiavi`

- **sourceLocation:** `chapters/09-iam-crittografia-logging-incident-response.md#n-tr01-09-03` ? ? heading `## N-TR01-09-03 · Crittografia e gestione delle chiavi`, riga 84.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La crittografia protegge proprietà specifiche; non sostituisce IAM, hardening, gestione delle vulnerabilità o continuità. La cifratura simmetrica usa una chiave condivisa e tutela soprattutto la riservatezza. Quella asimmetrica usa una coppia di chiavi ed è utile in scenari diversi, ma non è una scelta automaticamente più efficace. Un hash produce un'impronta non reversibile; un MAC usa un segreto per sostenere integrità e autenticità; una firma digitale consente verifiche con la chiave pubblica corrispondente; un certificato collega una chiave pubblica a un soggetto. Confondere questi strumenti porta a promettere proprietà che non offrono.

- **Fonti consolidate:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; NIST SP 800-57 Part 1 ? https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final.
- **Verifica fonte:** NIST e Normattiva. Fonti NIST e disciplina italiana/NIS2 controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-09-04

- **heading:** `## N-TR01-09-04 · Logging, rilevazione e triage`

- **sourceLocation:** `chapters/09-iam-crittografia-logging-incident-response.md#n-tr01-09-04` ? ? heading `## N-TR01-09-04 · Logging, rilevazione e triage`, riga 101.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Un evento è un fatto osservabile; un log è la sua registrazione; un audit trail permette di ricostruire attività rilevanti; un alert è una segnalazione prodotta da una regola o da un'analisi; un incidente compromette o minaccia obiettivi di sicurezza o servizio. Un alert apre quindi una verifica: non prova da solo l'esistenza di un incidente. La distinzione evita sia allarmi ignorati sia escalation che paralizzano l'ente senza evidenze sufficienti.

- **Fonti consolidate:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; NIST SP 800-92 ? https://csrc.nist.gov/pubs/sp/800/92/final.
- **Verifica fonte:** NIST e Normattiva. Fonti NIST e disciplina italiana/NIS2 controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-09-05

- **heading:** `## N-TR01-09-05 · Incident response e continuità del servizio`

- **sourceLocation:** `chapters/09-iam-crittografia-logging-incident-response.md#n-tr01-09-05` ? ? heading `## N-TR01-09-05 · Incident response e continuità del servizio`, riga 124.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> La risposta a un incidente inizia prima dell'incidente. Policy, contatti, ruoli, accessi di emergenza, capacità di logging e prove di coordinamento fanno parte della preparazione. Il NIST CSF 2.0 collega la risposta alla governance, all'identificazione e alla protezione: rilevare, rispondere e recuperare non sono una sequenza isolata dal rischio e dalla continuità. Il modello locale può cambiare, ma deve chiarire decisioni, responsabilità, evidenze e condizioni di chiusura.

- **Fonti consolidate:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; NIST SP 800-61 Rev.2 ? https://csrc.nist.gov/pubs/sp/800/61/r2/final.
- **Verifica fonte:** NIST e Normattiva. Fonti NIST e disciplina italiana/NIS2 controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** FAIL ? nessuna applicazione identificabile in modo atomico nel perimetro del nucleo.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## N-TR01-09-06

- **heading:** `## N-TR01-09-06 · PA, ACN, CSIRT, NIS2 e privacy`

- **sourceLocation:** `chapters/09-iam-crittografia-logging-incident-response.md#n-tr01-09-06` ? ? heading `## N-TR01-09-06 · PA, ACN, CSIRT, NIS2 e privacy`, riga 149.
- **reviewer/gate:** `codex-step15-batch-b` / `step-15`.
- **quote letterale completa:**
> Nel quadro italiano, il d.lgs. 138/2024 recepisce la direttiva NIS2; ACN esercita le funzioni nazionali attribuite dalla disciplina e CSIRT Italia opera nel sistema di gestione degli incidenti. Il candidato deve mostrare che l'ente verifica il proprio inquadramento, la significatività dell'evento e le procedure applicabili. Non deve trasformare un riferimento tecnico volontario, come NIST, in un obbligo generale della PA né inventare soglie, canali o termini operativi.

- **Fonti consolidate:** `sources/iam-crittografia-logging-incident-response-fonti-primarie`; Normattiva d.lgs. 138/2024 ? https://www.normattiva.it/ ; ACN/CSIRT Italia ? https://www.acn.gov.it/.
- **Verifica fonte:** NIST e Normattiva. Fonti NIST e disciplina italiana/NIS2 controllate al cutoff. Controllo/cutoff: 2026-08-12.
- **Teoria:** PASS ? citazione letterale completa e fonte coerente con il contenuto del nucleo.
- **Applicazione:** PASS locale ? sottosezione/i: Caso guidato: account privilegiato compromesso.
- **Output concorsuale:** FAIL ? non attribuito atomically; il testo non collega un output/esercizio specifico a questo solo nucleo.
- **Q/C/E:** FAIL ? chapter-level non-atomic; nessun conteggio viene assegnato al nucleo.
- **Esito individuale:** FAIL di tracciabilit? ? non promuovere il nucleo nello step 15.
- **Correzione proposta:** inserire o richiamare nel nucleo un quiz, caso o esercizio con ID proprio; poi registrare la mappatura atomica nel ledger.

## Conteggio di controllo

- Record attesi/prodotti: 30/30.
- ID unici: 30.
- Quote esatte da verificare contro i capitoli: 30.
- FAIL Q/C/E: 30/30 (chapter-level non-atomic).
- Conclusione: batch B resta non promotabile fino alla mappatura atomica degli apparati.