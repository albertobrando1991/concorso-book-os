# Report editoriale — Procurement ICT e gestione dei fornitori

## 1. Sintesi editoriale

- Genere e pubblico: capitolo specialistico/workbook per candidati ai concorsi pubblici ICT.
- Perimetro: retrofit Format 2 dell'11 agosto 2026, con sette nuclei su fabbisogno, capitolato, SLA, esecuzione, sicurezza, continuità e uscita dal contratto.
- Stato generale: il capitolo è autosufficiente per il lettore; contiene caso guidato, strumenti compilabili, sei quiz commentati e domanda orale.
- Test dello studente: superato. Senza frontmatter né materiali interni, il lettore può distinguere requisito, criterio di accettazione, SLA, SLI, KPI, portabilità e reversibilità e applicarli al caso cloud.
- Confini: non sostituisce la disciplina generale delle procedure contrattuali né fissa soglie, penali o clausole universali.

## 2. Punti applicati della checklist

1. H1 unico e gerarchia H2/H3 leggibile.
2. Titolo coerente con procurement ICT e governo dei fornitori.
3. Apertura dal bisogno pubblico, non dalla tecnologia.
4. Progressione: scelta, requisiti, livelli di servizio, esecuzione, rischio, continuità, uscita.
5. Sette nuclei Format 2 con identificativi stabili.
6. Ogni nucleo integra definizione, funzione, distinzione, conseguenza e applicazione.
7. La teoria precede strumenti e caso.
8. La Mappa BANDO collega attori, documenti e output.
9. Il lessico requisito/accettazione/criterio/SLA è distinto.
10. Funzionali e non funzionali sono resi verificabili.
11. La matrice requisito-test-evidenza è utilizzabile.
12. SLA, SLI e KPI non sono trattati come sinonimi.
13. Finestra, fonte, esclusioni e severità completano la misura.
14. Penali e service credit non sono presentati come rimedio automatico.
15. RUP, DEC, owner e referenti sono descritti senza attribuzioni normative inventate.
16. Il governo dell'esecuzione conserva evidenze, decisioni e responsabilità.
17. Non conformità ed escalation hanno una sequenza operativa chiara.
18. Sicurezza, dati e supply chain diventano requisiti ed evidenze.
19. Privacy e subfornitura restano correttamente dipendenti dal caso.
20. Change request, versioni, cutover e rollback sono distinti.
21. Backup, ripristino, RPO e RTO non sono confusi.
22. Obsolescenza e dipendenze entrano nel monitoraggio.
23. Lock-in tecnico, dati, contrattuale, economico e organizzativo sono distinti.
24. Portabilità e reversibilità sono spiegate senza semplificazioni.
25. L'exit plan è trattato lungo il ciclo di vita.
26. Il caso cloud collega bisogno, controllo ed uscita.
27. Sei quiz riportano risposta e motivazione leggibile.
28. Domande-trappola ed esercizi verificano l'uso concorsuale.
29. Nessun collegamento interno o dipendenza editoriale è rimasto nel corpo lettore.
30. Tabelle e checklist sono leggibili in Markdown; la resa paperback richiede controllo separato.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Intero capitolo | Autonomia didattica | Lieve | Il testo precedente esponeva riferimenti interni non accessibili al lettore. | Rimossi i collegamenti dal corpo e sostituiti con riferimenti professionali leggibili. | Risolto |
| E02 | N-TR01-12-01–07 | Struttura/densità | Lieve | Il retrofit iniziale non conteneva un blocco di verifica né nuclei tutti sopra la soglia prevista. | Inseriti blocco `▣ Verifica`, sei quiz commentati e approfondimenti per ciascun nucleo. | Risolto |
| E03 | N-TR01-12-02 e N-TR01-12-04 | Accuratezza normativa | Lieve | La formulazione iniziale usava «collaudo» come termine generale per servizi e forniture ICT e «responsabile del procedimento» per il RUP. | Corretto in «verifica di conformità» per servizi e forniture, con distinzione dal collaudo dei lavori, e in «responsabile unico del progetto». | Risolto |
| E04 | Apertura e avvertenze operative | Autonomia didattica/proofread | Lieve | Il rinvio avanzato era generico; una frase esponeva il workflow interno e il testo conteneva apostrofi duplicati e tre refusi. | Ripristinato il rinvio lettore a VOL-09/M-TR02; eliminati workflow interno, apostrofi duplicati e refusi; riallineata la matrice Q6 al nucleo 07. | Risolto |
| V01 | Quadro contrattuale | Fatto/norma da verificare | Lieve | Testo vigente del Codice, allegati, indicazioni ANAC e dati del ciclo digitale possono cambiare. | Riesame documentato con fonti istituzionali nel controllo normativo. | Da verificare allo step 15 |
| V02 | Strumenti e cloud PA | Fatto/norma da verificare | Lieve | Indicazioni AgID, Consip, qualificazione cloud e strumenti di acquisto applicabili dipendono dal contesto e dal cut-off. | Verificare fonti ufficiali e pertinenza al caso prima del text freeze. | Da verificare allo step 15 |
| V03 | Sicurezza, dati e filiera | Fatto/norma da verificare | Lieve | Ruoli privacy, subfornitura, trasferimenti, cancellazione e condizioni di sicurezza dipendono dal caso concreto. | Riesame specialistico senza introdurre clausole o termini universali. | Da verificare allo step 15 |
| V04 | Tabelle, checklist e quiz | Layout | Lieve | Gli strumenti sono leggibili in Markdown ma non ancora ispezionati nella gabbia paperback KDP. | Provare PDF e dividere le tabelle se il corpo risulta troppo piccolo. | Da verificare allo step 20 |

## 4. Osservazioni per capitolo

### Capitolo 12 — Procurement ICT e gestione dei fornitori

- Punti di forza: trasforma il procurement in governo verificabile della prestazione; collega esigenza, requisito, prova, misura, azione correttiva e uscita.
- Coerenza: evita di ripetere la procedura contrattuale generale, la teoria cyber o cloud; usa quei confini solo per non confondere il candidato.
- Copertura v4: i sette nuclei risultano completi nella matrice; il caso e gli strumenti non sostituiscono la teoria, ma la mettono alla prova.
- Correzioni oggettive applicate: rimossi i link interni dal corpo, resa esplicita la verifica Format 2, corretta la terminologia di verifica di conformità e RUP, ripristinato il rinvio avanzato e completato il proofread.

## 5. Coerenza globale

La terminologia è coerente: requisito, criterio di accettazione, criterio di valutazione, obbligo, SLA, SLI, KPI, non conformità, portabilità, reversibilità ed exit plan sono distinti. Il capitolo conserva i confini verso il ciclo generale dei contratti e verso i contenuti tecnici senza dipendere da testi esterni per capire la lezione. Il corpo lettore non contiene wikilink né rinvii a strumenti editoriali interni; le verifiche di fonti mobili sono formulate in modo pubblico e leggibile.

## 6. Contenuto da verificare

- V01: testo consolidato del Codice, allegati e indicazioni ANAC applicabili.
- V02: indicazioni AgID e Consip, strumenti di acquisto e qualificazione cloud al cut-off.
- V03: privacy, subfornitura, sicurezza, trattamento dati e uscita nel caso concreto.
- V04: impaginazione KDP degli strumenti compilabili e del blocco di verifica.

## 7. Suggerimenti facoltativi

- In impaginazione, rendere la matrice requisito-evidenza e la scheda SLA due pagine di lavoro distinte se la tabella risulta densa.
- Nel laboratorio del capitolo 13, usare il caso cloud per una simulazione orale di escalation senza duplicare il contenuto teorico.

## 8. Priorità degli interventi

1. Riesaminare V01–V03 negli step 13–18 con fonti istituzionali aggiornate e dati del caso.
2. Verificare V04 nell'impaginato KDP agli step 19–20.
3. Conservare il confine tra governo tecnico della prestazione e disciplina procedurale generale.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori.**

Motivazione: non sono emersi errori gravi aperti né lacune didattiche nel testo lettore. Restano controlli mobili su fonti e layout, già assegnati ai gate successivi; questo giudizio non sostituisce né anticipa lo step 24 di conferma umana.

## 10. Limiti della revisione

La revisione ha esaminato Markdown, matrice e fonti già dichiarate nel progetto. Non sostituisce il controllo giuridico al cut-off, la valutazione DPO del caso concreto, la verifica tecnica delle condizioni cloud o l'ispezione di un PDF impaginato.