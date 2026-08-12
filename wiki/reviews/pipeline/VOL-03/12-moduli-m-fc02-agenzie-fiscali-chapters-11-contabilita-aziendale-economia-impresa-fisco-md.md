# Report editoriale — Contabilità aziendale ed economia d'impresa per il fisco

## 1. Sintesi editoriale
- Genere editoriale: capitolo di manuale-workbook per concorsi pubblici, modulo specialistico M-FC02.
- Pubblico target: candidati ai profili contabili, fiscali, ACFI e audit delle Agenzie fiscali.
- Perimetro di questa revisione: capitolo 11, matrice M-FC02, rinvii della matrice VOL-03, source note consolidate, apparati didattici, esempi numerici e cinque asset visuali.
- Stato generale in una frase: capitolo strutturalmente completo e didatticamente autonomo, pubblicabile dopo la normalizzazione ortografica e la review contabile, OIC e tributaria al cut-off.

## 2. Punti applicati della checklist
Applicati tutti i punti 1-30: indice; struttura; progressione; gerarchia; pubblicabilità; coerenza interna e trasversale; terminologia; completezza; definizioni; contenuto concettuale e normativo; esempi; tabelle, box e schemi; fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; impaginazione osservabile dal Markdown; layout; leggibilità e qualità complessiva. Il punto 27 è stato valutato sul sorgente Markdown e sugli asset disponibili, poiché non era presente un PDF KDP definitivo. Applicati anche il gate di copertura didattica integrale e la verifica v4 dei rinvii.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Intero capitolo, frontmatter e corpo | Ortografia e qualità editoriale | Media | Il testo alterna grafie ASCII (`e'`, `contabilita`, `attivita`, `passivita`, `liquidita`, `puo`, `perche`) e forme correttamente accentate. L'alternanza è diffusa e non è adatta alla pubblicazione. | Eseguire una normalizzazione controllata degli accenti italiani, distinguendo apostrofi, accenti e congiunzioni; ripetere poi lint e controllo dei riferimenti. | Aperto |
| E02 | Frontmatter | Uniformità editoriale e metadati | Lieve | `updated_at` è fermo al 18 luglio 2026, mentre il capitolo incorpora revisioni successive; `review_required: true` resta corretto finché le verifiche specialistiche sono aperte. | Aggiornare `updated_at` e lo stato di review soltanto alla chiusura documentata di V01-V05. | Proposto |
| V01 | §§ 3-5 ed esempi numerici | Accuratezza contabile | Media | Logica Dare/Avere, scritture, competenza e assestamento sono coerenti e didatticamente leggibili, ma richiedono revisione specialistica prima della stampa. | Verificare classificazione dei conti, effetti delle scritture, terminologia e ipotesi semplificative, mantenendo esplicita l'esclusione dell'IVA. | Da verificare |
| V02 | §§ 6-11 | Accuratezza civilistica e OIC | Media | Postulati, documenti, schemi e principali poste di bilancio sono coerenti con le source note, ma codice civile, semplificazioni e principi OIC applicabili devono essere verificati al cut-off. | Controllare artt. 2423 e seguenti, schemi, esoneri e principi OIC vigenti; registrare data ed esito. | Da verificare |
| V03 | §§ 12-13 e mini-bilancio | Accuratezza dell'analisi di bilancio | Media | Current ratio e ROS sono formulati in modo chiaro; `leverage = totale fonti / patrimonio netto` è una configurazione dichiarata ma non universale. Tutti gli indici dipendono dallo schema e dalla qualità dei dati. | Far validare formule, denominatori, unità e interpretazioni da un revisore contabile; mantenere sempre dichiarato lo schema adottato. | Da verificare |
| V04 | § 14 e ponte numerico | Accuratezza tributaria | Media | Il ponte utile-variazioni-reddito è aritmeticamente coerente e non usa aliquote, ma derivazione, deducibilità, differenze temporanee e imposte anticipate/differite dipendono dal TUIR e dai principi applicabili. | Verificare il raccordo sul TUIR vigente e sulle fonti contabili, confermando che gli importi restino esempi ipotetici e non regole generali. | Da verificare |
| V05 | § 15 e tabella profili | Accuratezza operativa e istituzionale | Media | Riconciliazioni, segnali di rischio e applicazioni AE/ACFI, AdER e ADM sono formulate con cautela, ma attività, poteri, dati disponibili e mansioni dipendono dal bando e dall'organizzazione corrente. | Confrontare la sezione con fonti ufficiali, bando, profilo e mansioni assunti per l'edizione. | Da verificare |

## 4. Osservazioni per capitolo
### Capitolo 11 — Contabilità aziendale ed economia d'impresa per il fisco
- Punti di forza: la progressione distingue patrimonio, reddito e finanza prima di introdurre conti, partita doppia, competenza, bilancio, indici e raccordo fiscale. Le tre scritture numeriche, il mini-bilancio e il ponte utile-reddito rendono verificabili i nuclei prima parziali. Il caso `utile senza cassa`, la tabella anti-confusione, la domanda orale, la trappola, l'esercizio, il quiz, il glossario, il diario e la checklist applicano teoria già spiegata. Gli otto nuclei assegnati dalla matrice risultano completi.
- Criticità: non emergono errori concettuali certi o lacune didattiche bloccanti. E01 richiede una normalizzazione diffusa prima della pubblicazione; E02 va chiuso insieme alla review umana. V01-V05 richiedono verifica specialistica. Le cinque figure esistono, sono numerate in ordine e collegate ai blocchi pertinenti.

## 5. Coerenza globale
- Terminologia: coerente nelle distinzioni fondamentali: contabilità aziendale/pubblica, patrimonio/reddito/finanza, ricavo/incasso, costo/pagamento, utile/liquidità, bilancio/dichiarazione, imponibile/imposta e indice/prova. Resta l'alternanza grafica indicata in E01.
- Struttura vs indice: coerente. Il capitolo mantiene un solo corpo editoriale, un solo H1 e una gerarchia H2/H3 leggibile. Le Figure 11.1-11.5 seguono l'ordine di lettura.
- Promesse dell'introduzione mantenute: sì. I nove obiettivi trovano spiegazione, applicazione e verifica; nessun nucleo risulta solo nominato, parziale o mancante.
- Copertura v4 e rinvii: le righe 81-88 della matrice M-FC02 sono `completo`. Nella matrice VOL-03, i nuclei 23, 25 e 26 sono `rinviato` verso heading precisi del capitolo, come già avviene per i nuclei 22 e 24; il capitolo evita di duplicare contabilità pubblica e materie comuni del VOL-01. Non occorre declassificare le matrici.

## 6. Contenuto da verificare
- Scritture in partita doppia, classificazione dei conti e ipotesi semplificative.
- Competenza, ratei, risconti, ammortamenti, rimanenze, svalutazioni e fondi.
- Artt. 2423 e seguenti, documenti, schemi e semplificazioni del bilancio.
- Principi OIC vigenti per postulati, poste, rendiconto, imposte e informativa.
- Formule e interpretazione di current ratio, leverage, ROS, capitale circolante e margine di struttura.
- TUIR vigente, derivazione, variazioni, differenze temporanee e imposte anticipate/differite.
- Distinzione e raccordo fra logica reddituale, IVA, dichiarazioni e dati di controllo.
- Poteri, dati, profili e mansioni AE/ACFI, AdER e ADM assunti per l'edizione.
- Resa delle cinque figure, delle tabelle numeriche e della checklist nel PDF KDP definitivo.

## 7. Suggerimenti facoltativi (non errori)
- Valutare, dopo la review specialistica, una scheda digitale separata con ulteriori esercizi di scrittura e analisi, senza appesantire il cartaceo.
- Nel render KDP, evitare che le tabelle delle scritture, degli indici e del ponte fiscale si spezzino tra pagine.
- Valutare un richiamo grafico comune per la sequenza `operazione → conto → bilancio → dichiarazione → controllo`.

## 8. Priorità degli interventi
1. Chiudere V01-V05 sulle fonti ufficiali e con i revisori specialistici al cut-off editoriale.
2. Normalizzare accenti e grafie italiane nell'intero capitolo (E01).
3. Riallineare data e stato di review nel frontmatter dopo la chiusura delle verifiche (E02).
4. Eseguire il preflight del PDF KDP, con particolare attenzione a cinque figure e tabelle numeriche.
5. Valutare soltanto dopo i controlli obbligatori i suggerimenti facoltativi.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.
Motivazione: struttura, progressione, copertura didattica, calcoli, apparati, figure e rinvii non presentano errori gravi o blocker. Prima della pubblicazione occorrono tuttavia la review specialistica V01-V05, la normalizzazione ortografica E01 e il riallineamento finale dei metadati E02.

## 10. Limiti di questa revisione
La revisione ha coperto il capitolo Markdown, le matrici, le source note presenti nel repository, i riferimenti incrociati, i calcoli aritmetici e l'esistenza dei cinque asset. Non ha svolto una nuova verifica web articolo per articolo delle fonti ufficiali al 30 luglio 2026, non sostituisce una review contabile, OIC o tributaria e non ha ispezionato un PDF KDP impaginato. Il controllo di impaginazione è quindi limitato al sorgente e non sostituisce la review umana specialistica e produttiva prevista dal progetto.
