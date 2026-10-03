# Correzioni del sistema comune di esportazione

Mandato del 2 ottobre 2026; esecuzione proseguita il 3 ottobre. Perimetro: selezione del testo, ordinamento, parser, renderer, CSS e relative verifiche. Nessun commit, push o pubblicazione. Il diff preesistente che introduce `parseStudentChapterForExport` è stato preservato.

## Interventi e collegamenti agli audit

| Rilievo | Intervento applicato | Evidenza | Stato e limite |
|---|---|---|---|
| EXP-01 | Il filtro del fallback non elimina più Spiegazione, Punti chiave, Esempi, Errori frequenti e Obiettivo didattico. Le intestazioni inequivocabilmente interne restano escluse. | Test fallito con zero nuclei, poi superato con tutti e cinque; proiezione corrente IR02/09: N-IR02-09-01…05, numerati 22.1…22.5. | Corretto nel codice; la collazione del PDF definitivo VOL-06 resta al pacchetto finale. |
| EXP-02 | Aggiornamenti, colophon e premessa generati si rivolgono al candidato. Sostituite le promesse staff dei cataloghi VOL-07 e VOL-10. | Test dei preliminari VOL-07/10; estrazioni PDF di prova. | Corretto nei generatori; i preliminari redatti manualmente restano responsabilità del rispettivo volume. |
| EXP-03 | I PDF di prova sono distinti dai candidati in delivery e accompagnati da metriche. | `vol-03-proof.pdf`, `vol-11-proof.pdf`, `vol-12-proof.pdf`. | Il manifest finale dei dodici volumi richiede sorgenti editoriali stabilizzati; non è sostituito da queste prove. |
| P03-04; ordine IR04 | Ordinamento numerico anche per «Capitolo 02» e suffissi 5a/5b. | Test RED→GREEN; proiezione reale FC02: 05, 05a, 05b, 06; IR04: 01…13. PDF VOL-03: sanzioni da p. 300, tutela da p. 314, prima dei capitoli successivi. | Corretto nel codice e nel PDF di prova. |
| P12-02 e analoghi | I tag di interruzione nelle celle diventano nuove righe; il renderer usa elementi `br`, senza interpretare HTML arbitrario. | Test con `<br>`/`<br />`; VOL-12 passa dalle 299 occorrenze letterali del vecchio candidato a zero nel PDF di prova. | Corretto. |
| P01-02 e analoghi | Didascalie esplicite in corsivo o callout vengono associate all’immagine e stampate una sola volta. L’alt resta disponibile come descrizione accessibile. | Due regressioni per i formati reali; il figcaption è nello stesso blocco indivisibile della figura. | Corretto nel parser/renderer; verificare tutte le figure dei candidati finali dopo gli interventi grafici. |
| P08-04, P12-06 e analoghi | Il titolo di apertura duplicato H1/H2 viene rimosso anche quando preceduto da una nota; la nota resta intatta. | Test dedicato. | Corretto; non si eliminano titoli delle sezioni successive. |
| P01-01, P03-01, P08-01, P09-05, P12-01 e analoghi | Indice portato ad almeno 9,5 pt; voci capitolo 10 pt; didascalie 9,5 pt. Griglia tipografica preesistente mantenuta. | Misura browser: prima 6,6/6,75/7,5 pt, dopo minimo 9,5 pt. PDF VOL-03/11/12 con indice minimo 9,5 pt. | Corretto; l’aumento di pagine è intenzionale. Nessuna compressione del font. |
| P01-03, P03-02, P08-03, P11-01 e analoghi | Tabelle valide con più di quattro colonne suddivise in pannelli: prima colonna ripetuta come chiave, altri campi conservati. Righe compilabili vuote alte almeno 10 mm. | Test ricostruisce tutti i valori di una tabella a otto colonne; dettagli VOL-11 pp. 188–189, 205–208 e VOL-12 pp. 183, 362, 364. | Corretto il difetto comune. Una tabella semanticamente errata o precompilata senza spazio richiede correzione del manoscritto, per esempio P12-03. |
| P09-06 e analoghi | Eliminato lo spazio di 6 px fra frammenti contigui della stessa tabella sulla stessa pagina. | Prova browser: 6 px prima, 0 px dopo. | Corretto senza sopprimere le intestazioni necessarie a inizio pagina. |
| P12-05 | Se ID di nuclei distinti generano lo stesso numero visibile, la sequenza stampata diventa progressiva; gli ID restano invariati. Le numerazioni univoche preesistenti restano intatte. | Test dedicato e indice VOL-12 p. 6: 1.1…1.5. | Corretto nell’assemblaggio di volume. |
| P09-01/02, V03-025 | Nessuno spostamento semantico dei titoli inseriti nel manoscritto dentro tabelle/quiz. Corretto invece un difetto indipendente: senza righe bianche, il parser poteva anticipare il commento rispetto alle opzioni. | Test ordine domanda→opzioni→soluzione, fallito e poi superato. | Ordine del parser corretto; i confini editoriali errati restano assegnati agli owner dei testi. |
| Conservazione aggiuntiva | Eliminato il limite silenzioso di 520 blocchi nella sorgente della stampa; tokenizzazione delle tabelle rispetta pipe in codice, wikilink ed escape. Le celle eccedenti le intestazioni in tabelle malformate non vengono eliminate. | Test capitolo di 540 blocchi; test simboli e conservazione del dato eccedente. | Corretto; le tabelle malformate conservate richiedono comunque revisione editoriale. |

## Verifiche eseguite

- Dodici nuove regressioni del parser e una del renderer: cicli RED→GREEN documentati negli output della sessione. Le verifiche mirate finali comprendono 52 test in nove file, tutti superati.
- `npm run typecheck`: superato, log `typecheck-final.log`.
- `npm test`: eseguito integralmente; ultimo risultato 612 superati e quattro fallimenti in tre file relativi a VOL-07. Riguardano il titolo SA01/04 modificato, il nuovo stato/nucleo di SA02/05 e le due nuove source note non ancora incluse nel packaging basato su `git ls-files`. Owner VOL-07 e coordinatore informati; quei test non sono stati indeboliti o modificati dal revisore export.
- Prove complete: VOL-03 746 pagine; VOL-11 227; VOL-12 470. Per tutti: zero tag `br` letterali, massimo quattro colonne e nessun blocco oltre il footer nelle misure DOM. La prova VOL-12 precede gli ultimi affinamenti alle didascalie e alla distanza fra frammenti; resta una verifica del recupero dei tag, della numerazione e dello spazio compilabile, non il candidato definitivo.
- VOL-03: dettagli raster letti pp. 6, 198, 203, 300, 314, 496; immagini rigenerate dal PDF corrente dopo la verifica di un dettaglio precedente. VOL-12: dettagli raster letti pp. 6, 17, 127, 183, 362, 364. VOL-11: pp. 188, 189, 205, 206, 207, 208. I controlli misurati di tutte le pagine non equivalgono a lettura visiva di ogni testo minuto.

## Limiti e lavoro residuo

Le matrici larghe ora conservano dati e font, ma restano da rifinire a livello di manoscritto intestazioni come «Risorsa/dipendenza» (VOL-11, p. 189 della prova) e schede prive di veri campi vuoti. I contenuti giuridici, i rinvii, i titoli interposti nelle verifiche e gli errori interni alle figure sono fuori dalla correzione automatica del renderer.

Il server di sviluppo può ripristinare la vista Capitolo durante un live reload. Lo script diagnostico rifiuta una prova priva di indice o con la vista Libro disattivata. Per la consegna usare un build stabile e il controllo del numero di pagine atteso, non una sessione di sviluppo in modifica.

Non viene dichiarata la pubblicabilità dei volumi sulla base di queste prove. Occorrono i testi corretti, la rigenerazione finale, la collazione dei candidati e i gate della pipeline. Evidenze in `artifacts/correzioni-collana-2026-10-02/`; piano in `docs/superpowers/plans/2026-10-02-correzioni-export-collana.md`.

## Delta coordinatore — 3 ottobre 2026, figure e pagine finali

Prove VOL-10: 126 pagine prima della correzione delle dimensioni; 127 dopo. La CSS limitava tutte le figure a 238 px di altezza e 420 px di larghezza: la planimetria con testo a 18 punti nel file sorgente risultava troppo piccola. Ora le figure occupano la colonna, con limite di altezza 600 px; didascalia sull'intera colonna. Viste nel PDF le quattro figure alle pagine 28, 31, 122, 123: etichette, reazioni, diagrammi, quote, percorso e natura illustrativa leggibili. Nessun overflow misurato né asset mancante. Font estratti: corpo Garamond circa 11 pt, tabelle Arial circa 9,5 pt; lo scarto di 0,01 deriva dall'export browser.

Aggiunta regressione per il recupero congiunto di un titolo finale e del suo paragrafo, quando entrambi entrano nella pagina precedente: test prima fallito, poi passato. I 24 test mirati di paginazione, tipografia ed export passano. Il PDF successivo resta di 127 pagine: la correzione unitaria non basta ancora a dimostrare la risoluzione delle pagine finali quasi vuote; analisi DOM in corso. Nessuna dichiarazione di problema risolto basata soltanto sul test.

Prova VOL-09: 266 pagine con tutti i quattordici capitoli, indice minimo 9,5 pt, nessun tag br letterale, massimo quattro colonne, nessun overflow DOM. Nuovi preliminari e controllo visivo completo restano da completare. File di prova con suffisso 20261003 in artifacts; nessuna copia in delivery.


## Aggiornamento prove e approvazioni — 3 ottobre 2026

VOL-01: nuova prova di666pagine, indice minimo9,5pt, zero br letterali, immagini mancanti e overflow DOM; controllo visivo in corso. VOL-09: prova corrente265pagine, Gantt a pagina238 visto a dimensione piena, con unica didascalia e calcoli leggibili. VOL-10: prova125pagine, esaminata anche pagina78 della tabella DL; successiva rettifica della sola data NTC richiede rigenerazione finale.

La riapertura a cascata della pipeline ora invalida anche lo step24, senza concedere una nuova approvazione:38test di stato e CLI superati, typecheck superato. Le vecchie conferme di VOL-02 e VOL-08 sono state invalidate tramite reopen23--cascade; per VOL-09 sync ha aggiunto lo step24 che mancava. Nessun run-state modificato a mano e nessun signoff simulato.
