# Report editoriale — M-TR03 Tecnico-ingegneristico

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi tecnici nella Pubblica Amministrazione.
- Pubblico target: candidati ingegneri, architetti/urbanisti, geometri/istruttori tecnici e specialisti di infrastrutture.
- Perimetro di questa revisione: indice, piano editoriale, Bibbia del Modulo, matrice v4, tredici capitoli e report individuali dello step 12.
- Stato generale in una frase: progressione e contenuti sono solidi; i due blocchi scoperti sono stati risolti, mentre restano correzioni trasversali medie per lo step 14.

La sequenza profili–ufficio–fondamenti–discipline–ciclo dell'opera–dati–laboratorio è coerente. Tutti i capitoli adottano il Format 2 e contengono sei nuclei, per un totale di 78. Il confronto iniziale aveva restituito soltanto 72 ID nella matrice e quattro wikilink nel corpo del capitolo 1: entrambi i problemi sono stati corretti e verificati nella revisione. Restano disuniformità ortografiche, di metadati e di indice da correggere allo step 14.

## 2. Punti applicati della checklist

| N. | Controllo | Esito | Nota |
|---:|---|---|---|
| 1 | Indice e struttura reale | Non conforme | Il titolo del capitolo 6 non coincide integralmente con H1 e frontmatter. |
| 2 | Struttura logica e completezza | Conforme | Tredici capitoli ordinati e nessun capitolo orfano. |
| 3 | Progressione logica | Conforme | Le dipendenze 3→4, 5→6 e 7→12 sono rispettate. |
| 4 | Gerarchia dei titoli | Conforme con rilievo | Sei nuclei numerati per capitolo; resta E05 sull'indice. |
| 5 | Idoneità alla pubblicazione | Intervento medio richiesto | I blocchi E01-E02 sono risolti; restano E03-E05. |
| 6 | Coerenza interna dei capitoli | Conforme | I report individuali non mostrano lacune interne residue. |
| 7 | Coerenza tra capitoli | Conforme | Ruoli, documenti e fasi restano distinti lungo il ciclo dell'opera. |
| 8 | Coerenza terminologica | Conforme con rilievi | Lessico tecnico stabile; metadati e grafia richiedono uniformazione. |
| 9 | Completezza delle spiegazioni | Conforme | Gli esempi applicano teoria già sviluppata. |
| 10 | Accuratezza delle definizioni | Conforme con verifica mobile | Le definizioni sono coerenti; resta l'audit specialistico dello step 15. |
| 11 | Errori concettuali | Nessuno rilevato | Non emergono contraddizioni concettuali trasversali. |
| 12 | Errori normativi o contenutistici | Da verificare | Le fonti mobili sono elencate nella sezione 6. |
| 13 | Esempi | Conforme | Distribuiti tra profili, edificio scolastico, infrastrutture e patrimonio. |
| 14 | Tabelle, box e schemi | Conforme nel Markdown | Da controllare nel PDF KDP. |
| 15 | Apparato normativo | Conforme con verifica mobile | Riferimenti leggibili e tracciabilità nel frontmatter. |
| 16 | Sintassi | Conforme con rilievo | E03 riguarda grafia, non struttura sintattica. |
| 17 | Chiarezza espositiva | Conforme | Catene decisionali e limiti sono espliciti. |
| 18 | Tono editoriale | Conforme | Professionale e prudente. |
| 19 | Stile didattico | Conforme | Teoria, controllo, quiz e casi sono bilanciati. |
| 20 | Ripetizioni inutili | Nessuna trasversale bloccante | Le riprese del caso-scuola cambiano fase e funzione. |
| 21 | Contraddizioni | Nessuna rilevata | Non emergono conflitti centrali tra capitoli. |
| 22 | Grammatica | Conforme con rilievo | Correggere le forme senza accento censite in E03. |
| 23 | Ortografia | Non conforme | E03 è esteso a cinque capitoli. |
| 24 | Punteggiatura | Conforme | Nessuna anomalia trasversale sistematica. |
| 25 | Refusi | Non conforme | Le omissioni d'accento sono sistematiche, non isolate. |
| 26 | Uniformità grafica | Non conforme | E03 ed E04 producono disomogeneità. |
| 27 | Impaginazione | Non applicabile | PDF impaginato non disponibile in questo step. |
| 28 | Layout | Conforme nel sorgente | Resta necessario il preflight di tabelle e box. |
| 29 | Leggibilità complessiva | Conforme con correzioni | La grafia di E03 riduce la qualità percepita. |
| 30 | Qualità editoriale complessiva | Non conforme allo stato attuale | Correzioni trasversali necessarie prima dell'audit. |

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| E01 | `planning/02-matrice-copertura-didattica.md` | Copertura didattica integrale | Grave | I capitoli contengono 78 ID Format 2, mentre la matrice ne registrava 72 univoci: erano assenti `N-TR03-09-01`–`N-TR03-09-06`. | Aggiunte copertura, checklist delle undici dimensioni e delta con evidenze reali per ciascuno dei sei nuclei; riconciliazione 78/78 verificata. | Risolto |
| E02 | Cap. 1, nuclei 02-03 | Contratto dello studente e linking interno | Grave | Il corpo esponeva quattro wikilink verso M-TR04, M-TR02 e M-FL01. | Sostituiti con denominazioni editoriali leggibili, preservando confini e cautele degli instradamenti; nessun wikilink resta nel corpo dei capitoli. | Risolto |
| E03 | Capp. 6-8, 10-11 | Ortografia e uniformità grafica | Media | In cinque capitoli sono diffuse forme italiane prive dell'accento obbligatorio, tra cui `è`, `può`, `più`, `perché`, `qualità`, `attività`, `conformità`, `contabilità`, `priorità` e `viabilità`; anche alcuni titoli ne risentono. | Eseguire una sostituzione lessicale controllata sul testo naturale, escludendo slug, ID, URL, codice e riferimenti; rieseguire poi lint e lettura contestuale. | Aperto |
| E04 | Frontmatter capp. 1-13 | Coerenza dei metadati | Media | `draft_stage`, `review_required` e `dati_operativi` usano valori differenti; `module_code` manca nei capp. 11-12, `module_family` manca nei capp. 10-12 e nel cap. 13 vale `tecnico-ingegneristico` anziché `trasversali`. | Uniformare i campi secondo la Bibbia del Modulo, senza alterare tracciabilità e date di compilazione. | Aperto |
| E05 | `index.md` | Indice, promesse e workflow | Media | Il titolo del capitolo 6 è abbreviato rispetto a H1/frontmatter; stato e prossimo passo parlano ancora di review umana specialistica, mentre la pipeline aggiornata assegna l'audit automatico allo step 15 e la sola conferma umana allo step 24. | Allineare il titolo a “Edilizia privata, SUE, titoli abilitativi e vigilanza” e aggiornare le formule di stato al workflow vigente. | Aperto |
| E06 | Capp. 4, 6-13 | Layout | Lieve | Tabelle, formule, checklist e blocchi di casi sono leggibili in Markdown, ma non ancora verificati nel paperback KDP. | Eseguire il preflight PDF e convertire in schede verticali le tabelle che eccedono la gabbia. | Da verificare |

## 4. Osservazioni per capitolo

### Capitolo 1 — Il concorso tecnico nella PA: profili, enti e prove
- Punti di forza: orienta profili, materie e output e stabilisce i confini di collana.
- Criticità: i wikilink interni sono stati sostituiti con denominazioni leggibili (E02 risolto).

### Capitolo 2 — Ufficio tecnico pubblico, responsabilità e atti tecnici
- Punti di forza: collega fatto, istruttoria, documento e decisione senza duplicare VOL-01.
- Criticità: nessuna trasversale contenutistica; metadati da uniformare (E04).

### Capitolo 3 — Scienza e tecnica delle costruzioni per concorsi
- Punti di forza: costruisce il lessico necessario prima del quadro NTC.
- Criticità: restano le verifiche professionali su formule, segni e unità.

### Capitolo 4 — NTC, sismica, geotecnica e sicurezza strutturale
- Punti di forza: progressione prestazionale coerente con capitoli 3 e 9.
- Criticità: audit di vigenza e preflight delle tabelle (E06).

### Capitolo 5 — Urbanistica e governo del territorio
- Punti di forza: distingue livelli di piano, conformità, vincoli, espropriazione e paesaggio.
- Criticità: disciplina regionale e locale da mantenere separata dal quadro nazionale.

### Capitolo 6 — Edilizia privata, SUE, titoli abilitativi e vigilanza
- Punti di forza: confine urbanistica-edilizia e percorso opera–regime–controllo chiari.
- Criticità: titolo dell'indice, grafia e metadati (E03-E05).

### Capitolo 7 — Progettazione di opere pubbliche
- Punti di forza: catena bisogno–DIP–PFTE–esecutivo–verifica–validazione leggibile.
- Criticità: grafia e metadati (E03-E04).

### Capitolo 8 — Direzione lavori, esecuzione e cantieri
- Punti di forza: distingue RUP, DL e CSE e collega tecnica, contratto e sicurezza.
- Criticità: grafia e metadati (E03-E04).

### Capitolo 9 — Collaudo, verifica, manutenzione e gestione dell'opera
- Punti di forza: separa controlli finali, presa in consegna e ciclo di vita.
- Criticità: i sei nuclei sono stati riconciliati nelle undici dimensioni della matrice (E01 risolto).

### Capitolo 10 — Computi, capitolati e contabilità dei lavori
- Punti di forza: segue la lavorazione dal progetto al conto finale.
- Criticità: grafia e metadati (E03-E04).

### Capitolo 11 — Infrastrutture, viabilità, ponti e monitoraggio
- Punti di forza: distingue evidenza, diagnosi, rischio e decisione.
- Criticità: grafia e metadati (E03-E04).

### Capitolo 12 — BIM, GIS, rilievi, catasto e patrimonio pubblico
- Punti di forza: il ciclo del dato unifica strumenti diversi senza confonderli.
- Criticità: metadati incompleti (E04).

### Capitolo 13 — Laboratorio delle prove tecniche
- Punti di forza: integra gli output e trasforma gli errori in prove di recupero.
- Criticità: `module_family` incoerente e metadati da uniformare (E04).

## 5. Coerenza globale

- Terminologia: RUP, DL, CSE, verifica, validazione, collaudo, stato dei luoghi e dato tecnico sono usati in modo coerente; E03 riguarda la grafia, non il significato.
- Struttura vs indice: la sequenza 1-13 è completa; resta il disallineamento puntuale del titolo del capitolo 6 (E05).
- Promesse dell'introduzione: profili, prove, materie specialistiche, casi, checklist e laboratorio sono mantenuti.
- Copertura integrale: 78 nuclei effettivi e 78 ID univoci riconciliati nella matrice dopo la risoluzione di E01.
- Rinvii: quelli interni fra capitoli sono comprensibili; dopo la risoluzione di E02 nessun corpo di capitolo espone wikilink.
- Equilibrio teoria/workbook: adeguato; i capitoli 1-12 insegnano la materia e il capitolo 13 la integra in prestazioni.
- Profili e confini: ingegnere, architetto/urbanista, geometra/istruttore e infrastrutture sono riconoscibili; non emerge duplicazione sistematica con VOL-01 o altre famiglie.

## 6. Contenuto da verificare

- Vigenza e campo di applicazione di NTC, Circolare, emendamenti e disciplina delle costruzioni esistenti.
- Disciplina nazionale, regionale e locale di urbanistica, edilizia, titoli, tolleranze, regolarizzazioni e vigilanza.
- D.Lgs. 36/2023 e allegati applicabili a progettazione, esecuzione, contabilità e collaudo.
- Titolo IV del D.Lgs. 81/2008, ruoli e poteri nella sicurezza dei cantieri.
- Codice della strada, norme geometriche, Linee guida ponti e atti ANSFISA.
- BIM, interoperabilità, RNDT/INSPIRE, catasto, inventario e contabilità patrimoniale.
- Correttezza professionale di formule, unità, calcoli, casi e soluzioni campione.

Le verifiche sono assegnate all'audit specialistico automatico dello step 15 e non sono confuse con gli errori certi E01-E05.

## 7. Suggerimenti facoltativi (non errori)

- Inserire nell'edizione digitale una mappa dei percorsi consigliati per profilo.
- Collegare il Diario degli errori del capitolo 13 ai capitoli da ripassare.
- Valutare una legenda unica degli acronimi tecnici nella versione cartacea.

## 8. Priorità degli interventi

1. E01 ed E02: risolti e verificati nello step 13.
2. Correggere sistematicamente la grafia nei capitoli 6-8, 10-11 (E03).
3. Uniformare metadati e indice al workflow corrente (E04-E05).
4. Eseguire allo step previsto audit specialistico e preflight (E06 e sezione 6).

## 9. Giudizio di pubblicabilità

**Pubblicabile dopo intervento medio.**

Motivazione: E01 ed E02, inizialmente gravi, sono stati risolti direttamente e verificati. Restano aperte le correzioni medie E03-E05, circoscritte a grafia, metadati e indice, che lo step 14 deve applicare prima dell'audit specialistico; E06 resta un controllo di produzione.

## 10. Limiti di questa revisione

La revisione ha esaminato i sorgenti Markdown, la matrice, l'indice, la Bibbia del Modulo e i report individuali. Non ha ispezionato un PDF impaginato e non ha sostituito l'audit articolo per articolo delle fonti mobili, previsto allo step 15. Le verifiche tecniche su casi, formule e procedure richiedono le competenze specialistiche instradate dalla pipeline.
