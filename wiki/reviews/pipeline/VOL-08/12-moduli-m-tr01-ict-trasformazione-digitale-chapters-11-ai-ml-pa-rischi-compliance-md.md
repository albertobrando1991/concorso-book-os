# Report editoriale — AI/ML nella PA: modelli, rischi e compliance

## 1. Sintesi editoriale

- Genere: capitolo specialistico/workbook per concorsi pubblici, destinato a candidati ICT e Data/AI.
- Perimetro: retrofit Format 2 dell'11 agosto 2026, con confronto tra capitolo 11, matrice, fonte AI/ML, topic collegato e confini con i capitoli 03, 04, 06, 08, 09, 10 e 12.
- Stato generale: sette nuclei autosufficienti, caso ragionato, microcaso generativo, quiz commentati e griglia di rischio rendono il capitolo utilizzabile senza strumenti interni.
- Test dello studente: superato. Le definizioni e le distinzioni necessarie sono nel corpo; il lettore può motivare finalità, dati, metriche, controllo umano, lifecycle e quadro applicabile senza accedere a fonti interne.

## 2. Punti applicati della checklist

1. Indice e gerarchia: un H1, H2 coerenti e sette nuclei Format 2.
2. Progressione: sistema e modello, paradigmi, dati, metriche, responsible AI, lifecycle e quadro giuridico sono in ordine funzionale.
3. Copertura didattica: ogni nucleo ha definizione, funzione, elementi, distinzioni, conseguenze, applicazione, errore e verifica nella matrice atomica.
4. Coerenza con il modulo: evita la duplicazione di algoritmi, data governance, sicurezza, logging e procurement; conserva i necessari confini.
5. Esempi e strumenti: il caso sulle segnalazioni, il microcaso generativo e la griglia di rischio richiedono una scelta motivata, non una mera ripetizione.
6. Accuratezza: AI Act, legge italiana, AgID e NIST sono distinti; il testo non attribuisce date o classificazioni al caso senza verifica ufficiale.
7. Stile: Humanizer applicato dopo lo snapshot; tono tecnico, sobrio e impaginabile.
8. Superficie: nessun refuso, incoerenza terminologica o meta-commento rilevante nel Markdown controllato.
9. Layout: le tabelle non sono state provate in PDF; verifica rimandata alla fase KDP, senza dichiarare l'esito nel capitolo.
10. Gate aggiuntivo di copertura v4: applicato; nessun nucleo risulta parziale, solo nominato o mancante.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | N-TR01-11-07, quadro UE e italiano | Accuratezza normativa | Media | Un calendario AI Act dettagliato sarebbe mobile e non risulterebbe verificabile dal capitolo. | Mantenere l'attuale metodo prudente: testo vigente, atti applicabili, ruolo e caso concreto prima di date o classificazioni. | Risolto |
| V01 | Quadro UE e italiano | Fatto/norma da verificare | Lieve | Testo consolidato, atti modificativi, calendario applicativo, linee guida definitive e campo concreto della legge n. 132/2025 possono mutare. | Riesame documentato al cut-off negli step 13-18 con fonti ufficiali. | Da verificare allo step 15 |
| V02 | Lifecycle e MLOps | Riferimento tecnico | Lieve | Stato ed edizione del NIST AI RMF e del profilo Generative AI richiedono controllo prima del text freeze. | Confermare versione e stato della fonte; mantenere il framework come riferimento volontario. | Da verificare allo step 15 |
| V03 | Tabelle e strumenti | Layout | Lieve | La griglia è leggibile in Markdown ma non è stata ispezionata in gabbia paperback KDP. | Verificare nel Book Studio e dividere la tabella se necessario. | Da verificare allo step 20 |

## 4. Osservazioni per capitolo

### Capitolo 11 — AI/ML nella PA: modelli, rischi e compliance

- Punti di forza: distingue con chiarezza automazione, modello e sistema; spiega leakage e metriche in rapporto agli effetti; tratta bias, spiegabilità e controllo umano senza scorciatoie; collega versioni, drift e rollback a responsabilità concrete.
- Criticità residue: non sono emersi errori gravi nel testo; restano verifiche mobili e di impaginazione, correttamente esterne alla pretesa didattica del capitolo.
- Copertura v4: collocazione corretta in M-TR01. Il capitolo sviluppa il delta AI/ML e rinvia ai capitoli tecnici senza duplicare il nucleo comune di VOL-01.

## 5. Coerenza globale

Terminologia coerente: algoritmo, sistema AI, modello, feature, label, addestramento, inferenza, accuracy, precision, recall, bias, fairness, spiegabilità, controllo umano, drift e rollback sono distinti. I rinvii ai capitoli 03, 04, 06, 08, 09, 10 e 12 sono di confine e non sostituiscono teoria promessa. Non sono presenti wikilink o dipendenze da wiki, dashboard, report o source note nel testo lettore.

## 6. Contenuto da verificare

- V01: AI Act e legge n. 132/2025 al testo vigente, inclusi calendario e atti applicabili.
- V02: fonti AgID e NIST, con particolare riguardo a versioni e stato dei documenti.
- V03: privacy, procedimento, cybersicurezza, procurement e ruoli nel caso concreto; il capitolo non li universalizza.
- V04: resa KDP della griglia e delle sezioni di verifica.

## 7. Suggerimenti facoltativi

- Nel layout finale, rendere la griglia di rischio una pagina di lavoro staccabile se lo spazio lo consente.
- Aggiungere nel capitolo 13 una simulazione che chieda di motivare una soglia e un override, senza duplicare la teoria di questo capitolo.

## 8. Priorità degli interventi

1. Riesaminare le fonti mobili AI Act, legge italiana, AgID e NIST negli step 13-18.
2. Verificare griglia e blocco di quiz nell'impaginato KDP agli step 19-20.
3. Conservare la distinzione tra classificazione giuridica, rischio tecnico e controllo organizzativo.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori.**

Motivazione: il testo è strutturalmente completo e autonomo; non lascia rilievi gravi aperti. Le sole attività residue sono verifiche di fonti mobili e layout, già assegnate ai successivi gate automatici. Questo giudizio non sostituisce né anticipa lo step 24 di conferma umana.

## 10. Limiti della revisione

La revisione riguarda Markdown, matrice e fonti consolidate già disponibili. Non sostituisce la verifica giuridica al cut-off né l'ispezione di un PDF impaginato. Gli altri capitoli sono stati consultati solo per controllare confini e rinvii, non revisionati ex novo.