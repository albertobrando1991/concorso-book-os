# Report editoriale — Casi pratici, quiz e orale nelle Agenzie fiscali

## 1. Sintesi editoriale
- Genere editoriale: laboratorio conclusivo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili AE, ADM, AdER e ai profili con competenze catastali, contabili o di front-office.
- Perimetro di questa revisione: capitolo 13, matrice M-FC02, copertura v4, rinvii al VOL-01 e al capitolo 14, source note consolidate, dodici quiz, casi applicativi, simulazioni e cinque asset visuali.
- Stato generale in una frase: capitolo strutturalmente consolidato e didatticamente completo, pubblicabile dopo normalizzazione ortografica, verifiche specialistiche e preflight KDP.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: indice; struttura; progressione; gerarchia; pubblicabilità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto concettuale e normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown e sugli asset disponibili, poiché non era presente un PDF KDP definitivo. Applicati anche il gate di copertura didattica integrale e la verifica v4 dei rinvii.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Intero capitolo, frontmatter e corpo | Ortografia e qualità editoriale | Media | Il testo usa diffusamente grafie ASCII (`e'`, `puo`, `capacita`, `attivita`, `penalita`, `priorita`) non adatte all'edizione tipografica finale. | Eseguire una normalizzazione controllata degli accenti italiani, distinguendo apostrofi, accenti e congiunzioni; ripetere poi lint e controllo dei riferimenti. | Aperto |
| E02 | Frontmatter | Uniformità editoriale e metadati | Lieve | `updated_at` è fermo al 18 luglio 2026, benché il capitolo incorpori consolidamento e revisione successivi; `review_required: true` resta corretto finché le verifiche sono aperte. | Aggiornare `updated_at` e lo stato di review soltanto dopo la chiusura documentata delle verifiche V01-V05. | Proposto |
| V01 | Apertura, obiettivi, quiz e simulazioni | Accuratezza procedurale concorsuale | Media | Formato delle prove, materie, soglie, penalità, banca dati e criteri sono correttamente dichiarati mobili, ma devono coincidere con bando e avvisi della procedura usata nell'edizione. | Verificare ogni parametro sulla documentazione ufficiale del concorso e registrare fonte, data e versione. | Da verificare |
| V02 | Casi AE, ADM, AdER e Territorio | Accuratezza settoriale | Media | I casi applicano correttamente le griglie, ma contengono qualificazioni tributarie, doganali, di riscossione, catastali e civilistiche che richiedono revisione incrociata con i capitoli teorici e le fonti vigenti. | Far validare scenario, soluzione, competenza, sequenza, lessico e conseguenze dai revisori delle rispettive materie. | Da verificare |
| V03 | Batteria di quiz trasversali | Qualità dei quesiti | Media | I dodici quesiti sono dichiarati originali e hanno soluzione motivata; prima della stampa resta necessario controllare unicità della risposta, assenza di ambiguità e aggiornamento dei distrattori. | Eseguire una review indipendente domanda per domanda e documentare chiave, fonte e motivazione di ciascuna risposta. | Da verificare |
| V04 | Front-office e caso situazionale | Privacy e comunicazione istituzionale | Media | Le condotte proposte sono prudenti e coerenti con il ruolo, ma identificazione, delega, accesso ai dati, sicurezza e gestione dell'utente dipendono da GDPR, normativa nazionale e policy dell'ente. | Verificare il blocco con fonte privacy consolidata e procedure ufficiali dell'ente; mantenere distinta l'applicazione dalla teoria generale. | Da verificare |
| V05 | Mini-simulazione, griglia e piani | Validità didattica dei parametri | Media | Durata di 90 minuti, numero di quiz, tempi dei casi, risposte da 90 secondi e scansioni 30/60/90 o 14/7 sono presentati come modelli adattabili, non come regole; la resa dipende però dal profilo e dal bando. | Confermare che didascalie e layout rendano evidente il carattere esemplificativo; adattare i parametri nell'edizione collegata a uno specifico concorso. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 13 — Casi pratici, quiz e orale nelle Agenzie fiscali
- Punti di forza: il capitolo ora presenta un solo corpo editoriale e una progressione leggibile: dalla materia alla prestazione, quindi quiz, casi, orale, front-office, diario, simulazione e recupero. La spiegazione metodologica precede sempre l'esercizio. Le griglie rendono verificabili classificazione della traccia, competenza, sequenza, garanzie e output. I casi coprono AE, ADM, AdER, Territorio e situazioni ibride; i dodici quiz sono accompagnati da risposta; l'orale include durate diverse, rilanci e protocollo anti-invenzione. I cinque nuclei della matrice risultano completi.
- Criticità: non emergono errori concettuali certi o lacune didattiche bloccanti. E01 richiede una normalizzazione diffusa; E02 va chiuso insieme alle review. V01-V05 richiedono verifica specialistica e produttiva. Le cinque figure esistono, seguono l'ordine di lettura e sono collocate presso i rispettivi strumenti.

## 5. Coerenza globale
- Terminologia: coerente nelle distinzioni fra AE, ADM e AdER; quiz, caso, orale e situazionale; dichiarazione, controllo, accertamento e riscossione; catasto e titolarità; risposta sicura, incerta, lenta, errata e fortunata. Resta la grafia ASCII indicata in E01.
- Struttura vs indice: coerente. Il capitolo mantiene un solo H1, heading univoci e una gerarchia H2/H3 leggibile. Le Figure 13.1-13.5 seguono l'ordine didattico.
- Promesse dell'introduzione mantenute: sì. I sette obiettivi trovano metodo, applicazione e verifica; nessun nucleo assegnato risulta `parziale`, `solo-nominato` o `mancante`.
- Copertura v4 e rinvii: le cinque righe assegnate al capitolo 13 nella matrice M-FC02 sono `completo`. Il capitolo applica al perimetro specialistico il metodo generale del VOL-01 senza duplicarne integralmente i capitoli su quiz, scritto, orale, diario e piano. Il Ricettario digitale è richiamato nei riferimenti; il capitolo 14 resta la destinazione per canvas, tavole e appendici. La presenza di un caso front-office non sostituisce né promette una trattazione sistematica della privacy. Non occorre declassificare la matrice.

## 6. Contenuto da verificare
- Bando, avvisi, piattaforma, calendario, prove, materie, soglie, penalità, titoli e banca dati dell'edizione concreta.
- Casi AE su dichiarazioni, fatture, ricavi, banca, compliance, controllo e accertamento.
- Casi ADM su classificazione, origine, valore, prova, contraddittorio e conseguenze.
- Casi AdER su ente creditore, sospensione, rateizzazione, pagamento e orientamento dell'utente.
- Caso Territorio su visura, titolo, planimetria, catasto, pubblicità e regolarità urbanistica.
- Condotte di front-office, delega, identificazione, accesso ai dati, sicurezza e riservatezza.
- Unicità e aggiornamento delle dodici risposte ai quiz.
- Parametri e criteri della simulazione e dei piani temporali.
- Resa delle cinque figure, delle numerose tabelle e degli spazi compilabili nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare una banca digitale separata di ulteriori casi e quiz, mantenendo nel cartaceo soltanto gli esercizi necessari a mostrare il metodo.
- Nel render KDP, evitare spezzature nelle tabelle dei casi, del diario e della simulazione; lasciare spazio di compilazione reale nel mini-esercizio.
- Valutare un codice grafico uniforme per distinguere `metodo`, `caso`, `soluzione`, `errore` e `verifica`.

## 8. Priorità degli interventi
1. Chiudere V01-V05 con fonti ufficiali, review specialistiche e controllo indipendente dei quiz.
2. Normalizzare accenti e grafie italiane nell'intero capitolo (E01).
3. Riallineare data e stato di review nel frontmatter dopo la chiusura delle verifiche (E02).
4. Eseguire il preflight del PDF KDP, con particolare attenzione a cinque figure, tabelle e strumenti compilabili.
5. Valutare soltanto dopo i controlli obbligatori i suggerimenti facoltativi.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione, copertura didattica, casi, quiz, orale, simulazione, figure e rinvii non presentano errori gravi o blocker. Prima della pubblicazione occorrono tuttavia le verifiche V01-V05, la normalizzazione ortografica E01 e il riallineamento finale dei metadati E02.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo Markdown, la matrice M-FC02, le source note e i topic presenti nel repository, i riferimenti incrociati e l'esistenza dei cinque asset. Non ha svolto una nuova verifica web di ogni bando, norma, procedura o policy al 30 luglio 2026; non sostituisce review tributarie, doganali, di riscossione, catastali, privacy o concorsuali e non ha ispezionato un PDF KDP impaginato. Il controllo di impaginazione è quindi limitato al sorgente e non sostituisce la review umana specialistica e produttiva prevista dal progetto.
