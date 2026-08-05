# Report editoriale - M-FC02 Agenzie fiscali

## 1. Sintesi editoriale
- Genere editoriale: manuale-workbook specialistico per concorsi nelle Agenzie fiscali.
- Pubblico target: candidati AE, ADM, AdER, Territorio/SPI e profili amministrativo-contabili collegati.
- Perimetro di questa revisione: indice, front matter, matrice, 14 capitoli numerati, intercalari 5A/5B e report individuali.
- Stato generale in una frase: il modulo ha una copertura ampia e una progressione solida; la promessa formativa scoperta nel capitolo 9 è stata corretta, mentre restano interventi editoriali trasversali di media entità.

## 2. Punti applicati della checklist
Sono stati applicati i punti 1-26 e 28-30: indice, struttura, progressione, gerarchia, coerenza interna e trasversale, terminologia, completezza, definizioni, errori concettuali e normativi osservabili, casi, tabelle, figure, fonti, sintassi, tono, ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout markdown, leggibilità e qualità complessiva.

Il punto 27 non è pienamente applicabile perché non è stato esaminato un PDF impaginato. Sono stati applicati anche copertura didattica integrale e regola v4. La matrice registra 80 nuclei completi, ma la revisione ha individuato una promessa interna al capitolo 9 che deve essere esplicitata nella matrice o coperta nel testo.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| G01 | Cap. 9, `Obiettivo del capitolo`, punto 8; parr. 7-9 | Completezza delle spiegazioni e copertura didattica | Grave | Il capitolo prometteva di distinguere monopolio fiscale, concessione e gestione diretta. Concessione e gestione diretta erano spiegate; il monopolio fiscale era solo richiamato nella rete dei tabacchi. | Inserita una spiegazione fontata che distingue l'uso del termine nei tabacchi e nei giochi, il titolo concessorio e la gestione diretta; matrice riallineata. | Corretto |
| M01 | `index.md`, Perimetro e Prossimo passo | Coerenza globale e struttura vs indice | Media | L'indice dichiara ancora 18 blocker didattici, mentre la matrice ne registra zero. Il prossimo passo è quindi obsoleto. | Aggiornare stato e prossimo passo: copertura completa, correzioni trasversali, review specialistiche e preflight ancora aperti. | Aperto |
| M02 | Capp. 7-14 e passaggi sparsi nei capp. precedenti | Ortografia e uniformità grafica | Media | Il modulo alterna accenti italiani e grafie ASCII (`e'`, `puo`, `piu`, `perche`, nomi astratti senza accento). L'alternanza è visibile tra capitoli e dentro lo stesso capitolo. | Eseguire una normalizzazione controllata, preservando codice, URL, anchor e termini tecnici; ripetere poi lint e controllo citazioni. | Aperto |
| M03 | Capp. 5, 6 e 7, `asset_refs` | Apparato, figure e layout | Media | I tre capitoli dichiarano cinque asset ciascuno, tutti esistenti, ma non incorporano alcuna figura nel corpo. L'apparato promesso non raggiunge il lettore. | Inserire le figure nelle sezioni didattiche corrispondenti con didascalie e ordine di lettura; eseguire preflight KDP. | Aperto |
| M04 | Cap. 3, figure 3.1-3.5 | Coerenza tra testo e apparato | Media | Più figure risultano spostate di una sezione: lo schema MEF è sotto `Le tre funzioni`, la mappa delle tre funzioni sotto AE e la rete territoriale sotto la sezione sulla commissione. | Ricollocare le figure accanto alla sezione descritta dalla didascalia, senza modificare il testo tecnico. | Aperto |
| M05 | Cap. 8, figure 8.1-8.5 | Gerarchia e layout | Media | L'ordine di comparsa è 8.1, 8.2, 8.5, 8.3, 8.4. | Spostare la checklist 8.5 dopo la 8.4 oppure rinumerare coerentemente asset e didascalie. | Aperto |
| M06 | Cap. 4, `Livello 3 - Quadro UE fiscale, IVA e dogane` | Gerarchia dei titoli | Media | Il titolo introduce un livello 3 senza livelli 1 e 2 nel capitolo. | Rinominare in `Quadro UE fiscale, IVA e dogane` e aggiornare gli anchor entranti. | Aperto |
| M07 | Capp. 1, 2 e 3, frontmatter | Metadati e coerenza editoriale | Media | I tre capitoli non dichiarano `companion_to: il-metodo-bando`, presente negli altri tredici capitoli. | Aggiungere il campo senza cambiare gli altri metadati. | Aperto |
| L01 | Cap. 14, figure 14.4-14.5 | Layout | Lieve | Le due figure sono consecutive e possono risultare poco mediate in pagina. | Valutare una frase di raccordo o una distribuzione su due sottosezioni nel preflight. | Proposto |

## 4. Osservazioni per capitolo
### Capitolo 1 - Mappa delle Agenzie fiscali e dei profili concorsuali
- Punti di forza: perimetro, profili e criteri dentro/fuori sono chiari.
- Criticità: manca il campo `companion_to`; dati istituzionali mobili da verificare.

### Capitolo 2 - Bando Decoder fiscale
- Punti di forza: trasforma il bando in una scheda e in output di prova.
- Criticità: manca il campo `companion_to`; bandi e prove restano mobili.

### Capitolo 3 - Ordinamento e organizzazione di AE, ADM e AdER
- Punti di forza: distingue natura, funzioni e relazioni tra enti.
- Criticità: M04 e M07; assetti e regolamenti richiedono review ufficiale.

### Capitolo 4 - Diritto tributario e teoria dell'imposta
- Punti di forza: base teorica del modulo e raccordo con redditi, IVA e UE.
- Criticità: M06; vigenza tributaria e fonti UE da verificare.

### Capitolo 5 - Accertamento, controlli e compliance fiscale
- Punti di forza: sequenza controllo-istruttoria-contraddittorio-atto e profilo ACFI completi.
- Criticità: cinque asset dichiarati ma non incorporati; review tributaria necessaria.

### Capitolo 5A - Sanzioni amministrative e reati tributari
- Punti di forza: separa illecito amministrativo, reato e recupero del tributo.
- Criticità: disciplina temporale e raccordi penalistici richiedono review specialistica.

### Capitolo 5B - Tutela e processo tributario
- Punti di forza: progressione da atto e tutela fino a impugnazioni ed esecuzione.
- Criticità: termini, processo telematico e disciplina transitoria da verificare.

### Capitolo 6 - Adempimenti fiscali: redditi, IVA, dichiarazioni
- Punti di forza: integra qualificazione reddituale, ciclo IVA e dichiarazioni.
- Criticità: cinque asset dichiarati ma non incorporati; modelli, canali e termini mobili.

### Capitolo 7 - Riscossione nazionale e lavoro in AdER
- Punti di forza: distingue imposizione, accertamento, riscossione e front-office.
- Criticità: M02 e M03; soglie, rateizzazione e misure esecutive da verificare.

### Capitolo 8 - Dogane e procedure doganali ADM
- Punti di forza: fonti, triade tecnica, regimi, debito e controlli sono coordinati.
- Criticità: M02 e M05; CDU, TARIC e sistemi telematici da verificare.

### Capitolo 9 - Accise, giochi e monopoli
- Punti di forza: accise, sospensione, filiere, giochi e controlli sono applicati a casi e quiz.
- Criticità: G01 corretto; resta M02. Riordino giochi, aliquote e procedure ADM da verificare.

### Capitolo 10 - Catasto, cartografia, estimo e pubblicità immobiliare
- Punti di forza: distingue catasto, estimo, cartografia e SPI con applicazioni.
- Criticità: M02; DOCFA, PREGEO, OMI e procedure tecniche da review.

### Capitolo 11 - Contabilità aziendale ed economia d'impresa per il fisco
- Punti di forza: teoria, scritture, bilancio, indici e ponte utile-imponibile sono coordinati.
- Criticità: M02; principi contabili e fiscalità d'impresa da verificare.

### Capitolo 12 - Civile e commerciale applicati a fisco, dogane e riscossione
- Punti di forza: selezione coerente con il profilo e casi applicativi.
- Criticità: M02; codice civile, leggi speciali e crisi richiedono review.

### Capitolo 13 - Casi pratici, quiz e orale nelle Agenzie fiscali
- Punti di forza: casi AE/ADM/AdER/Territorio, quiz, orale e simulazione chiudono il percorso.
- Criticità: M02; risposte specialistiche e regole dei bandi da verificare.

### Capitolo 14 - Appendici operative
- Punti di forza: glossario di 80 voci, tavole, flussi, routing e protocollo privacy.
- Criticità: L01; preflight delle tabelle e review GDPR.

## 5. Coerenza globale
- Terminologia: nel complesso coerente. G01 è stato corretto; resta l'alternanza ortografica M02.
- Struttura vs indice: l'elenco dei 14 capitoli più 5A/5B corrisponde ai 16 file; lo stato dei blocker nell'indice è obsoleto (M01).
- Promesse dell'introduzione mantenute: sì, dopo la correzione G01.
- Progressione: corretta da profilo e bando alla teoria, alle materie settoriali, alla performance e agli strumenti finali.
- Rinvii: 320 wikilink controllati; nessun target o anchor mancante nei 16 capitoli e nell'indice.
- Copertura v4: nessuna duplicazione grave del VOL-01; rinvii cross-family coerenti verso M-TR01, M-TR02, M-TR03 e M-FC03.
- Matrice: 80 righe su 80 in stato `completo`; la riga su riserva statale, concessione e filiera è stata riconciliata con G01.

## 6. Contenuto da verificare
- Tutte le review normative elencate nella colonna `Review normativa` della matrice.
- Vigenza di TUIR, IVA, accertamento, sanzioni, reati, processo e riscossione al cut-off.
- CDU, atti delegati/esecutivi, TARIC, TUA, EMCS/e-AD, giochi e procedure ADM.
- DOCFA, PREGEO, OMI, pubblicità immobiliare e prassi Territorio/SPI.
- OIC, diritto societario, crisi d'impresa e raccordi fiscali.
- GDPR, policy degli enti, bandi, avvisi, CCNL, canali, modelli, software, soglie e termini mobili.
- Resa KDP delle 55 figure attualmente incorporate, delle 15 ancora da incorporare, delle tabelle e dei canvas.

## 7. Suggerimenti facoltativi (non errori)
- Valutare una tabella iniziale `profilo -> capitoli prioritari -> capitoli opzionali` dopo la chiusura delle correzioni.
- Uniformare nel text freeze la resa tipografica di `Istruzioni`, `Esempio`, `Errore tipico`, `Rinvio` e `Note di review`.
- Valutare sottosezioni separate nell'appendice F del capitolo 14 solo se migliorano il preflight.

## 8. Priorità degli interventi
1. Correggere M01-M07: indice, accenti, figure, titolo UE e metadati.
2. Eseguire le review normative e tecniche indicate nella sezione 6.
3. Eseguire preflight KDP e risolvere L01.
4. Ripetere controllo di link, lint, copertura e report prima del text freeze.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.

Motivazione: G01 è stato corretto con fonte consolidata e non restano promesse formative scoperte. Gli interventi M01-M07 sono circoscritti e non richiedono una nuova architettura del modulo, ma devono essere chiusi prima della review umana e del text freeze.

## 10. Limiti di questa revisione
La revisione ha esaminato markdown, frontmatter, indice, matrice, report individuali, file e anchor dei wikilink e stato degli asset. Non è stato ispezionato un PDF impaginato e non sono state rieseguite verifiche web di vigenza normativa o delle procedure degli enti. Il report non sostituisce review umana tributaria, doganale, catastale, contabile, civilistica, penal-tributaria, processuale, organizzativa e privacy.
