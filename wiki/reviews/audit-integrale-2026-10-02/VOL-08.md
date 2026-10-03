# VOL-08 — Revisione integrale del testo, 2 ottobre 2026

## 1. Sintesi editoriale

Letti integralmente tutti i 13 capitoli originali di M-TR01, comprese domande, risposte, casi e fonti finali. La struttura è leggibile e gli esempi di SQL, pseudocodice, subnetting e le chiavi dei quiz risultano coerenti. Il volume non è ancora pronto per la pubblicazione: il livello tecnico varia molto e alcuni nuclei normativi centrali sono sostituiti da rinvii alla verifica delle fonti. Nessuna correzione è stata applicata.

## 2. Punti applicati della checklist

Applicati i 30 punti della skill revisore-editoriale-totale al perimetro testuale: forma, sintassi, lessico, coerenza, struttura, contenuto, fonti, didattica, esempi e apparati. Il punto relativo alla resa grafica è demandato al rapporto PDF separato. Non equivale a validazione integrale di tutte le norme né delle appendici delle matrici.

## 3. Tabella errori e integrazioni necessarie

Le righe si riferiscono agli originali identificati con SHA-256 nel ledger. Gravità grave = ostacolo sostanziale alla preparazione promessa; medio = errore locale o miglioramento necessario; lieve = refuso.

| ID | Posizione | Categoria | Gravità | Descrizione ed estratto | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| V08-01 | Indice modulo, r.1 | Stato editoriale | medio | «publication-ready»: L’indice dichiara la pubblicabilità ma il suo Stato editoriale rinvia ancora agli step 13–24; M-TR02 è descritto come incompleto. | Riconciliare indice, matrice e stato effettivo senza trasformare il metadato in certificazione. | Non applicato |
| V08-02 | Cap. 10, r.35 | Coerenza del metodo | grave | «Base; Attori; Nodi; Documenti»: BANDO cambia significato nei capitoli 10, 11 (r. 35) e 12 (r. 47), rispetto a Bando, Aree, Nuclei, Diario, Output usato nel resto della collana. | Ripristinare le cinque voci canoniche e ricollocare attori/documenti al loro interno. | Non applicato |
| V08-03 | Cap. 01, r.1 | Destinazione editoriale | medio | «Apparato di verifica dei nuclei»: Tutti i capitoli mantengono apparati di tracciabilità e formule rivolte al verificatore, non al candidato. | Conservare la tracciabilità nei file di lavoro; rendere il riepilogo per il lettore una mappa di studio senza linguaggio di audit. | Non applicato |
| V08-04 | Cap. 02, r.137 | Precisione tecnica | medio | «rappresentazione»: Complemento a due non nominato né mostrato; la virgola mobile è descritta con grandezza invece di esponente e significando. | Dare nomi corretti, intervalli e un esempio breve di rappresentazione e overflow; distinguere il modello dalla precisione effettiva. | Non applicato |
| V08-05 | Cap. 03, r.367 | Precisione tecnica | medio | «memoria aggiuntiva»: La complessità spaziale è identificata con la sola memoria ausiliaria. | Distinguere spazio totale, spazio dell’input e spazio ausiliario, dichiarando la convenzione degli esercizi. | Non applicato |
| V08-06 | Cap. 03, r.381 | Precisione tecnica | medio | «cresce linearmente»: O grande è definito come limite superiore ma poi interpretato come crescita esatta, anche nel raddoppio quadratico del quiz 5. | Usare Theta per l’ordine stretto oppure dichiarare il termine dominante e l’ipotesi semplificata del quiz. | Non applicato |
| V08-07 | Cap. 03, r.561 | Fonti | medio | «materiali didattici universitari»: Le fonti di algoritmi non sono identificabili. | Indicare autore, titolo, edizione o documentazione primaria e sezioni usate. | Non applicato |
| V08-08 | Cap. 04, r.97 | Esempio tecnico | medio | «id_ufficio»: Lo schema non impone NOT NULL sulla chiave esterna benché ogni pratica debba appartenere a un ufficio; l’esempio Assegnazione a r. 169 ragiona inoltre su un attributo non riportato nello schema. | Allineare vincoli e schema alla cardinalità dichiarata; esplicitare gli attributi dell’esempio di normalizzazione. | Non applicato |
| V08-09 | Cap. 04, r.305 | Copertura didattica | grave | «livelli di isolamento»: L’isolamento è promesso ma mancano i quattro livelli e le anomalie che permettono di distinguerli. | Aggiungere una tabella di livelli/anomalie e una sequenza di due transazioni; segnalare differenze del DBMS scelto. | Non applicato |
| V08-10 | Cap. 05, r.377 | Precisione tecnica | medio | «richiesta HTTP»: L’incapsulamento presume TCP senza precisare la versione di HTTP. | Dichiarare HTTP/1.1 o HTTP/2 nell’esempio; ricordare HTTP/3 su QUIC. | Non applicato |
| V08-11 | Cap. 06, r.146 | Coerenza tecnica | medio | «Livello»: La regressione compare fra i livelli di test; a r. 415 il capitolo spiega correttamente che è uno scopo trasversale. | Separare livelli e finalità del test in tabella. | Non applicato |
| V08-12 | Cap. 06, r.357 | Esercitazione | medio | «veloce»: La soluzione dell’esercizio sul requisito misurabile dice cosa specificare ma non formula un requisito verificabile. | Fornire un esempio con soglia e carico dichiarati come ipotetici e relativo test di accettazione. | Non applicato |
| V08-13 | Cap. 06, r.1 | Copertura didattica | medio | «API»: La progettazione di API resta descrittiva: mancano un payload, codici di risposta e un contratto minimo concreto. | Aggiungere un esempio end-to-end, con autorizzazione, errore e versionamento; spiegare i vincoli REST prima delle scelte implementative. | Non applicato |
| V08-14 | Cap. 07, r.177 | Copertura normativa | grave | «strategici, critici e ordinari»: Le classi cloud sono nominate senza i criteri di impatto; il regolamento 2024 resta privo di estremi e regime. | Inserire tabella classi/impatti/esempi e riferimento al decreto 21007/24, separando quadro stabile e verifica corrente della qualificazione. | Non applicato |
| V08-15 | Cap. 08, r.287 | Terminologia | medio | «STRIDE»: Le sei categorie sono elencate in inglese senza spiegazione applicativa. | Tradurre e associare a ciascuna una minaccia e un controllo sul caso della PA. | Non applicato |
| V08-16 | Cap. 08, r.530 | Esercitazione | medio | «risposta aperta»: Due soluzioni si limitano al criterio generale di correzione. | Mostrare una risposta svolta con asset, minaccia, rischio e controllo motivato. | Non applicato |
| V08-17 | Cap. 09, r.149 | Copertura normativa | grave | «verificare»: NIS2 è ridotta al richiamo del d.lgs. 138/2024 e alla verifica futura: non insegna essenziali/importanti, obblighi di governance, criteri e sequenza delle notifiche; manca il raccordo con legge 90/2024. | Sviluppare il nucleo normativo datato con presupposti, soggetti, atti ACN e decorrenze per coorte; distinguere 24/72 ore e relazione finale, GDPR e altri regimi senza universalizzare. | Non applicato |
| V08-18 | Cap. 09, r.86 | Copertura tecnica | grave | «crittografia»: Per un percorso cyber specialistico la trattazione non rende operative le differenze tra chiavi simmetriche/asimmetriche, firma, hash, certificati e catena di fiducia. | Aggiungere schema delle chiavi, esempi di cifratura/firma, proprietà del digest, PKI/TLS e password hashing, distinguendo concetti da prescrizioni di algoritmo. | Non applicato |
| V08-19 | Cap. 09, r.218 | Qualità dei quiz | medio | «NO»: Tutte le sei domande dei capitoli 9 e 10 hanno risposta negativa prevedibile; nel 9 la domanda 6 confronta una notifica con un evento data breach. | Alternare casi e opzioni plausibili; confrontare incidente cyber e violazione di dati, poi i rispettivi obblighi di notifica. | Non applicato |
| V08-20 | Cap. 09, r.100 | Refuso | lieve | «nel ignorare»: Preposizione articolata errata. | Sostituire con nell’ignorare. | Non applicato |
| V08-21 | Cap. 10, r.192 | Definizione normativa | grave | «quando pertinente»: La definizione di open data rende eventuale il formato leggibile meccanicamente e non espone i tre requisiti cumulativi del CAD art. 1 l-ter. | Esporre licenza/uso anche commerciale, formato aperto utilizzabile automaticamente con metadati, gratuità o regole di costo ammesse; distinguere dalle esclusioni di pubblicazione. | Non applicato |
| V08-22 | Cap. 10, r.196 | Copertura normativa | medio | «possono includere»: Gli obblighi HVD sono formulati come possibilità indistinta. | Indicare per quali serie e condizioni sono richiesti API, formato e download massivo secondo regolamento 2023/138 e allegato; non generalizzare oltre il campo di applicazione. | Non applicato |
| V08-23 | Cap. 10, r.223 | Rinvio insufficiente | medio | «procedure di adesione»: Il rinvio al capitolo 6 promette procedure e dettagli PDND che quel capitolo non contiene. | Aggiungere una spiegazione sufficiente o rinviare a una sezione effettiva e a documentazione ufficiale puntuale, correggendo la promessa. | Non applicato |
| V08-24 | Cap. 10, r.111 | Refuso | lieve | «usare interno»: Forma verbale al posto del sostantivo. | Sostituire con uso interno. | Non applicato |
| V08-25 | Cap. 11, r.169 | Copertura normativa | grave | «calendario»: La compliance non sviluppa definizioni dei ruoli, criteri di rischio, principali obblighi PA né calendario; la legge 132/2025 resta un titolo, senza art. 14. | Inserire casi classificati, responsabilità del deployer e regole PA; ricostruire il calendario dal testo vigente comprensivo delle modifiche 2026 e distinguere obblighi già applicabili/futuri. | Non applicato |
| V08-26 | Cap. 11, r.102 | Copertura didattica | grave | «F1»: Il profilo data/AI non è sostenuto da algoritmi spiegati né da un calcolo completo di metriche; il cap. 3 r. 46 promette algoritmi ML nel cap. 11. | Aggiungere almeno un metodo supervisionato e uno non supervisionato con esempio e una matrice di confusione svolta con precision/recall/F1; oppure delimitare esplicitamente la promessa del profilo. | Non applicato |
| V08-27 | Cap. 12, r.65 | Copertura normativa ICT | grave | «riuso»: La scelta sviluppare/acquistare/riusare non espone valutazione comparativa e riuso degli artt. 68–69 CAD; il richiamo Consip non spiega gli obblighi specifici ICT. | Sviluppare CAD 68–69 e linee guida Ag ID con una decisione motivata; verificare e integrare legge 208/2015 commi 512 ss. con ambito/eccezioni e rinvio preciso al VOL 09. | Non applicato |
| V08-28 | Cap. 12, r.115 | Esercitazione | medio | «valore»: Nessun esempio numerico consente di calcolare disponibilità, SLA o scostamento, nonostante la promessa misurativa. | Dare un dataset minimo e calcolo svolto con periodo, esclusioni e soglia ipotetica, evitando numeri presentati come obblighi universali. | Non applicato |
| V08-29 | Cap. 12, r.216 | Ruoli | medio | «quando previsto»: La funzione di direzione dell’esecuzione appare eventuale, senza distinguere esercizio da parte del RUP e nomina separata del DEC. | Spiegare la distinzione e rinviare al presupposto normativo preciso per il DEC distinto dal RUP. | Non applicato |
| V08-30 | Cap. 12, r.263 | Ruoli privacy | medio | «validazione»: La necessaria validazione del DPO è formulata come potere autorizzativo, in tensione con il cap. 10 che ne descrive il ruolo consultivo. | Attribuire la decisione al titolare e qualificare informazione/consulenza/sorveglianza del DPO secondo il caso, senza creare un visto generale obbligatorio. | Non applicato |
| V08-31 | Cap. 13, r.475 | Esercitazione | grave | «Caso autonomo»: Il caso autonomo ha una rubrica ma non una soluzione modello; lo scritto tecnico a r. 445 offre una scaletta senza un elaborato effettivo. | Fornire architettura motivata, alternative, assunzioni, test e criteri di punteggio con esempi di risposte; inserire una simulazione tecnica con artefatti verificabili. | Non applicato |
| V08-32 | Cap. 07, r.238 | Stile e progressione | medio | «DevOps»: Ripetizioni additive estese nei capitoli 7–13; nel 10 le definizioni arrivano dopo applicazioni e riprese. | Accorpare i paragrafi che non aggiungono concetti; usare spazio recuperato per teoria, esempi e soluzioni mancanti. | Non applicato |

## 4. Osservazioni per capitolo

Tutti i capitoli sono stati letti integralmente, con controllo di quiz, commenti e casi. Le note analitiche di lettura restano nel ledger.

- **Capitolo 1 — Lavorare come ICT nella PA: ruoli, enti e prove**: Orientamento utile; il rapporto con i diversi profili va sostenuto da percorsi e prove più differenziati.
- **Capitolo 2 — Informatica specialistica: cosa serve oltre il VOL-01**: Le nozioni di base sono coerenti, ma diversi concetti specialistici sono solo accennati e richiedono esempi applicati.
- **Capitolo 3 — Programmazione, algoritmi e strutture dati**: Pseudocodice ed esercizi elementari risultano coerenti. Ampliare le spiegazioni degli algoritmi e delle strutture richiamate dal programma.
- **Capitolo 4 — Basi dati, SQL/No SQL e qualità del dato**: Query e casi SQL controllati; completare le distinzioni su transazioni, anomalie e livelli di isolamento.
- **Capitolo 5 — Reti, sistemi operativi e infrastrutture**: I calcoli di subnetting verificati sono corretti. Precisare le versioni dei protocolli e sviluppare i livelli e i servizi richiesti dal profilo.
- **Capitolo 6 — Ingegneria software, API e interoperabilità PA**: Il metodo di analisi è utile; occorrono requisiti, test e artefatti compilati che dimostrino l’applicazione.
- **Capitolo 7 — Cloud PA, virtualizzazione, container e DevOps**: Il quadro del cloud pubblico deve includere classificazione e qualificazione dei servizi, con fonti e date identificabili.
- **Capitolo 8 — Cybersecurity operativa: rischio, controlli e vulnerabilità**: Approccio al rischio coerente; rendere più concrete le tecniche, le metriche e le verifiche dei controlli.
- **Capitolo 9 — IAM, crittografia, logging e incident response**: Ampliare obblighi NIS2, gestione degli incidenti e distinzione fra identità, autenticazione e autorizzazione con casi operativi.
- **Capitolo 10 — Data governance, open data, interoperabilità e qualità**: Correggere la definizione dei dati aperti e la rimappatura di BANDO; rafforzare qualità, governance e interoperabilità.
- **Capitolo 11 — AI/ML nella PA: modelli, rischi e compliance**: Completare categorie e ruoli dell’AI Act, disciplina italiana della PA e calendario applicativo; aggiungere formule e casi per le metriche.
- **Capitolo 12 — Procurement ICT e gestione dei fornitori**: Integrare valutazione comparativa e riuso del software, obblighi di acquisto ICT e misure del servizio; correggere la rappresentazione del ruolo del DPO.
- **Capitolo 13 — Laboratorio prove ICT: quiz, scritto tecnico, orale e casi**: I quiz verificati risultano coerenti. Il laboratorio richiede soluzioni complete e prove SQL, algoritmiche, di rete e metriche, oltre alle scalette di metodo.

## 5. Coerenza globale

Il metodo BANDO deve mantenere un significato unico. Le note di tracciabilità non devono occupare il testo destinato al candidato. Le ripetizioni su rischio, evidenze, responsabilità e necessità di verifica sono numerose, mentre mancano esempi che dimostrino come applicare la regola. I rinvii alla parte comune sono legittimi solo se individuano una destinazione che contiene davvero il concetto promesso. Il campione di sette bandi offre un buon orientamento, ma non dimostra da solo la copertura di ogni profilo data/AI o cyber specialistico.

## 6. Contenuto verificato e da verificare

- [Livelli di isolamento e anomalie; differenze Postgre SQL esplicite](https://www.postgresql.org/docs/current/transaction-iso.html): Conferma integrazione necessaria, non errore delle query esistenti.
- [HTTP/3 usa QUIC](https://www.rfc-editor.org/rfc/rfc9114.html): Conferma necessità di dichiarare versione nell’esempio TCP.
- [Classificazione cloud per impatto](https://cloud.italia.it/strategia-cloud-pa/classificazione-di-dati-e-servizi/): Definizioni ufficiali disponibili, assenti nel corpo.
- [Regolamento cloud 21007/24 e regime agosto 2024](https://cloud.italia.it/qualificazione-servizi-cloud/): Confermato quadro; catalogo e successive modifiche non certificati integralmente.
- [OWASP Top 10 2025 è release finale](https://owasp.org/projects/top-ten): Confermato; non segnalato come riferimento futuro.
- [Sequenza notifiche NIS2 e governance](https://www.mimit.gov.it/images/stories/digitale/seminari/23_ottobre_2025/SintesiNIS2.pdf): Conferma quadro 24/72 ore/mese e obblighi governance; documento 2025 non certifica tutte le decorrenze delle coorti 2026.
- [Definizione CAD dati aperti](https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2026-04-20/_rst/capo1_sezione1_art1.html): Tre requisiti cumulativi confermati, lettera l-ter.
- [Legge 132/2025 art 14 PA](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.codiceRedazionale=25G00143&art.dataPubblicazioneGazzetta=2025-09-25&art.flagTipoArticolo=0&art.idArticolo=14&art.idGruppo=2&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.progressivo=0&art.versione=1): Confermati conoscibilità, tracciabilità, supporto alla decisione umana e misure tecniche/organizzative/formative nel testo originario; Normattiva riporta aggiornamento 2026, consultazione intero atto fallita.
- [AI Act calendario modificato 2026](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai): La Commissione segnala Omnibus in vigore 27 luglio 2026, alto rischio allegato III dal 2 dicembre 2027 e prodotti 2 agosto 2028; link al testo 1744/2026 bloccato da controllo browser. Non certificata ricostruzione articolo per articolo.
- [Percorso comparativo acquisizione/riuso software PA](https://docs.italia.it/italia/developers-italia/lg-acquisizione-e-riuso-software-per-pa-docs/it/stabile/attachments/allegato-e-tabella-sinottica-degli-elementi-necessari-al-percorso-decisionale.html): Percorso ufficiale disponibile e non sviluppato nel capitolo.

Letti inoltre gli indici di modulo e volume, la nota campione bandi, le cinque note consolidate cloud, IAM/incidenti, dati aperti, AI e procurement; della matrice sono state controllate le righe canoniche e i blocchi pertinenti. Le note stesse dichiarano review ancora necessaria: questo spiega la lacuna, non la risolve. Restano da verificare puntualmente i nuovi atti ACN, il raccordo legge 90/2024, obblighi Consip ICT, HVD e interoperabilità europea, ruoli DEC/DPO e tutte le revisioni NIST/FIRST non riscontrate esternamente. Le fonti tecniche e normative non controllate non sono dichiarate aggiornate.

## 7. Suggerimenti facoltativi (non errori)

- Ampliare OOP con incapsulamento, ereditarietà e polimorfismo se richiesto dal profilo; aggiungere i sette livelli OSI, permessi Unix e sincronizzazione soltanto raccordandoli al programma dichiarato.
- Offrire quiz con distrattori tecnici plausibili e separare fascicolo delle prove da soluzioni, evitando risposte prevedibili o sempre negative.
- Rendere omogenee le rubriche con descrittori di punteggio e distinguere esempi elementari da prove specialistiche.

## 8. Priorità degli interventi

Prima completare NIS2, AI/compliance, acquisizione/riuso ICT, open data e cloud PA. Poi aggiungere teoria tecnica essenziale e soluzioni svolte. Correggere insieme acronimo BANDO, definizioni, schemi e rinvii. Infine snellire ripetizioni, rimuovere backstage e riallineare indici e matrici.

## 9. Giudizio di pubblicabilità

**Da revisionare prima della pubblicazione.** Base introduttiva valida e numerosi esempi corretti, ma copertura specialistica e normativa non ancora sufficiente alla promessa del volume. Una semplice pulizia di refusi non basta.

## 10. Limiti di questa revisione

- Lettura integrale dei 13 capitoli correnti; matrici lette nelle righe canoniche e nei blocchi pertinenti, non integralmente in ogni appendice.
- Controlli esterni mirati, non certificazione di ogni fonte, versione tecnica o norma. Atti ACN 2026 e testo UE 1744/2026 richiedono controllo ulteriore.
- PDF separato: questo rapporto non certifica geometria, stampa o leggibilità delle pagine.
- Nessun contenuto editoriale modificato; le proposte restano da applicare.

Ledger: `artifacts/review-integrale-2026-10-02/VOL-08-ledger.json`. Tutti i 13 hash sono stati ricontrollati alla chiusura; nessuna lettura incompleta è conteggiata come completa.
