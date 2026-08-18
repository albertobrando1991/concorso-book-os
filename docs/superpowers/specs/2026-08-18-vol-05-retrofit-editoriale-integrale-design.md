# Disegno editoriale — retrofit integrale VOL-05

## Scopo

Portare `VOL-05 — Authority e regolazione` da bozza professionale a prodotto editoriale completo, autonomo per lo studente e tecnicamente pronto per il sign-off umano conclusivo della pipeline.

Il progetto conserva l'architettura in quindici capitoli e la voce dell'autore. Interviene invece in profondità su copertura didattica, aggiornamento normativo, apparato delle fonti, formato editoriale, appendici, conclusione, figure e controlli di produzione.

Questa specifica sostituisce, per la fase di pubblicabilità, il precedente disegno source-ready del 24 luglio 2026. Il dossier e le acquisizioni già esistenti restano validi come base storica e documentale.

## Decisione approvata

L'utente ha approvato il **retrofit editoriale integrale**, preferendolo sia all'edizione conservativa sia alla ricostruzione totale.

La decisione comporta:

- mantenimento dei quindici capitoli esistenti;
- adeguamento di tutti i capitoli al formato editoriale a nuclei;
- integrazione delle lacune sostanziali emerse nella revisione del 18 agosto 2026;
- produzione delle cinque appendici già promesse nell'indice;
- creazione di una vera introduzione d'uso e di una conclusione;
- rimozione dal prodotto di ogni residuo di lavorazione interno;
- revisione selettiva, non meccanica, delle figure;
- collaudo finale per carta ed ebook;
- avanzamento esclusivo mediante il CLI della pipeline.

## Stato di partenza

Il corpus contiene quindici capitoli completi come bozza, settantacinque figure referenziate e un apparato interno di fonti e review. Non è però pubblicabile perché:

1. le appendici A–E sono annunciate ma non esistono;
2. il testo del lettore espone note di review, schede di lavoro e collegamenti wiki interni;
3. manca una conclusione e la premessa non svolge ancora la funzione di guida d'uso;
4. alcuni nuclei specialistici sono assenti o troppo brevi, in particolare nei capitoli 3, 7, 10, 12 e 14;
5. tutti i capitoli sono in formato legacy e non rispettano il contratto corrente del formato 2;
6. fonti, didascalie, figure e servizi digitali non sono ancora chiusi come prodotto;
7. il run-state di `VOL-05` non è inizializzato.

Il report operativo di partenza è `wiki/reviews/vol-05-revisione-editoriale-finale-2026-08-18.md`.

## Principi non negoziabili

### Autonomia dello studente

Rimuovendo frontmatter e accesso al wiki, ogni capitolo deve restare comprensibile, studiabile ed esercitabile. Una fonte interna non sostituisce mai una spiegazione nel corpo.

### Copertura didattica integrale

Ogni promessa dell'indice o della matrice deve risultare:

- `completo`, con teoria, applicazione e verifica;
- oppure `rinviato`, ma solo verso una destinazione precisa, esistente e completa.

Gli stati `parziale`, `solo-nominato` e `mancante` impediscono il freeze.

### Voce dell'autore

Le revisioni devono preservare tono, lessico professionale e impostazione operativa. La riscrittura integrale di un capitolo è ammessa soltanto se la struttura esistente impedisce di chiudere la copertura; negli altri casi si procede per integrazione e ricomposizione chirurgica.

### Fonti prima del testo

Le informazioni normative o tecniche nuove entrano nel capitolo soltanto dopo verifica su fonte primaria ufficiale e consolidamento in source note. Il writer non usa direttamente i file `raw/` per il testo finale.

### Separazione editoriale

`chapters/` e le appendici pubblicabili contengono esclusivamente testo destinato al lettore. Matrici, piani, note di review, checklist staff, audit e registri tecnici rimangono in `planning/` o `wiki/reviews/`.

## Architettura del prodotto finale

### Front matter

Il volume apre una sola volta con:

1. frontespizio;
2. copyright e avvertenza editoriale;
3. descrizione verificata degli eventuali servizi digitali;
4. sommario;
5. `Come usare questo volume`, con pubblico, prerequisiti, percorsi giuridico/economico/misto, uso dei box e strategia di aggiornamento;
6. elenco delle abbreviazioni essenziali.

I servizi digitali privi di destinazione reale, accessibile e mantenibile vengono rimossi dalla promessa commerciale.

### Corpo in quindici capitoli

Restano invariati numerazione, tema portante e collocazione dei capitoli. Ogni capitolo lavorato dichiara `format_version: 2` e contiene:

- almeno cinque nuclei reali con ID `N-M-FC05-<CAP>-<NN>`;
- almeno 600 parole per nucleo e almeno 3.000 parole complessive, salvo soglia più alta indicata dalla scheda pipeline;
- obiettivo didattico e mappa iniziale;
- teoria sufficiente per le promesse assegnate;
- almeno un caso ragionato;
- errori tipici e output di prova;
- un blocco `▣ Verifica` con almeno sei quiz commentati;
- riferimenti normativi e professionali leggibili, senza path o wikilink interni;
- didascalie specifiche per le sole figure mantenute.

La sequenza interna non deve essere identica in tutti i capitoli: casi, mappe, tabelle, esempi numerici e domande da commissario vengono dosati in funzione della materia.

### Priorità di intervento

#### Fascia A — integrazione strutturale

- Capitolo 3: REMIT II, poteri ACER, SSM, distinzione fra reti, agenzie e autorità europee.
- Capitolo 7: economia industriale, indicatori ed evidenza, econometria minima, contabilità regolatoria con calcoli svolti.
- Capitolo 10: DMA, confini con DSA e disciplina settoriale, memo professionale in inglese.
- Capitolo 12: pagamenti, ABF, AAS, Solvency II, MiCAR, DORA e riparto SSM.
- Capitolo 14: perimetro whistleblowing, facilitatori, ritorsioni, presunzione/onere probatorio, sanzioni e misure di sostegno.

#### Fascia B — rafforzamento specialistico

- Capitolo 2: organi, nomine, incompatibilità, accountability e personale.
- Capitolo 4: confronto documentato di consultazione, AIR e VIR fra authority.
- Capitolo 6: matrice autorità–atto–giudice–rito–termine con avvertenza sul cut-off.
- Capitolo 8: artt. 101 e 102 TFUE, concentrazioni, esenzioni, leniency, consumer enforcement e procedura.
- Capitolo 11: TUF, emittenti e prospetti, servizi e mercati, procedimenti e ACF.
- Capitolo 15: almeno tre svolgimenti completi, memo inglese modello, rubriche e strumenti di autovalutazione.

#### Fascia C — revisione e normalizzazione

- Capitoli 1, 5, 9 e 13: copertura, coerenza, aggiornamento e naturalezza senza espansioni sproporzionate.
- Tutti i capitoli: rimozione dei residui interni, migrazione al formato 2, quiz, fonti, uniformità terminologica e proofreading.

## Appendici operative

Le appendici seguono esattamente la promessa pubblica già presente nell'indice:

### Appendice A — Atlante comparativo delle authority

Tavole su fonti istitutive, organi, poteri, reti europee, personale e controllo giurisdizionale. Le celle non omogenee non vengono forzate: le differenze di fonte, rito o competenza sono esplicitate.

### Appendice B — Tavole dei procedimenti

Schemi per consultazione, AIR/VIR, istruttoria, ispezione, impegni, sanzione e ricorso. Ogni tavola indica ambito e cut-off; termini variabili o non verificati non vengono presentati come regola generale.

### Appendice C — Toolkit Bando Decoder

Strumenti cartacei autosufficienti: scheda Bando Decoder, matrice materie, registro fonti, checklist dell'output e diario delle lacune.

### Appendice D — Lessico inglese regolatorio e modelli di memo

Glossario essenziale contestualizzato, strutture fraseologiche utili e almeno due memo modello completi. L'inglese non è un elenco decorativo: viene collegato alle prove del capitolo 10 e del capitolo 15.

### Appendice E — Registro aggiornamenti normativi e concorsuali

Registro compilabile con fonte, oggetto, data, impatto sui capitoli e decisione editoriale. Non promette aggiornamento automatico.

## Conclusione

La conclusione chiude il percorso senza introdurre nuova teoria. Deve:

- ricomporre la catena fonte–potere–procedura–garanzia–output;
- mostrare come adattare il metodo a un nuovo bando;
- proporre una sequenza operativa finale di ripasso e simulazione;
- rinviare agli strumenti cartacei pertinenti;
- lasciare al lettore un criterio professionale memorabile, non una ripetizione dell'indice.

## Apparato delle fonti e cut-off

Il cut-off editoriale del retrofit è fissato al **18 agosto 2026**. Ogni fonte dinamica riporta la propria data di verifica.

Per le integrazioni si usano prioritariamente:

- EUR-Lex e Normattiva/Gazzetta Ufficiale;
- siti e atti ufficiali delle authority;
- BCE, EBA, ESMA, EIOPA, ACER, Commissione europea ed EDPB per il livello europeo;
- documenti ufficiali dei sistemi ADR e delle procedure richiamate.

Ogni claim centrale deve essere tracciabile nel frontmatter o nella matrice. Nel corpo le fonti sono nominate in forma editoriale leggibile. Se manca una conferma sufficiente si usa la formula: `DA VERIFICARE — non dispongo di elementi sufficienti per confermarlo`, e il nucleo resta aperto.

## Sistema visuale

Le settantacinque figure esistenti non costituiscono una quota da conservare. L'audit valuta per ciascuna figura:

- necessità didattica;
- leggibilità al formato paperback 6,69 × 9,61 pollici;
- contrasto in bianco e nero;
- dimensione del testo interno;
- rapporto con il paragrafo e con la didascalia;
- comportamento nel reflow ebook.

Si mantengono indicativamente due o tre figure realmente utili per capitolo. Una figura debole viene corretta o sostituita; una figura ridondante viene esclusa dal libro. Gli asset sorgente inutilizzati non vengono cancellati durante il retrofit. Prima di creare o ridisegnare immagini viene adottata e documentata una filosofia visuale coerente con la collana.

## Flusso operativo e artefatti

### Inizializzazione

1. creare la scheda pipeline canonica di `VOL-05`, ricavata dal template vigente;
2. validarla con i controlli del repository;
3. inizializzare lo stato tramite CLI e leggere sempre gli esiti con `--json`;
4. non modificare mai manualmente `pipeline/VOL-05/run-state.json`.

### Esecuzione

Il lavoro procede nell'ordine imposto dai venticinque step. Prima di ogni step LLM viene richiamata `LocalAgentMemory` con scope `VOL-05`; dopo ogni flusso importante viene registrata una traccia sintetica.

Gli artefatti interni principali sono:

- scheda pipeline;
- matrice di copertura formato 2;
- registro delle criticità globali;
- report di audit specialistico e normativo;
- report humanizer;
- report visuale e pagina per pagina;
- revisione editoriale totale aggiornata;
- pacchetto di consegna pre-sign-off.

## Gestione degli errori e dei gate

- Un gate fallito interrompe il lavoro a valle fino alla correzione.
- `gate-not-implemented` non equivale a esito positivo: richiede verifica manuale documentata e chiusura con `--accept --note` soltanto se l'evidenza è disponibile.
- Una fonte primaria mancante mantiene il claim e il relativo nucleo aperti.
- Un rinvio verso file o heading inesistente è bloccante.
- Un asset mancante o illeggibile viene corretto prima del preflight.
- Lo step 24 resta un sign-off umano: il sistema può predisporre un pacchetto completo, ma non può dichiarare acquisita una firma non ricevuta.

## Verifiche

### Test editoriali automatici

- validità del frontmatter;
- presenza e univocità degli ID dei nuclei;
- almeno cinque nuclei e soglie minime per capitolo;
- almeno sei quiz commentati e un caso ragionato per capitolo;
- assenza di sezioni interne nel corpo lettore;
- assenza di wikilink verso `sources/`, `topics/`, `entities/`, `planning/`, `raw/` o `reviews/` nel corpo;
- risoluzione di link, immagini e rinvii;
- matrice senza righe `parziale`, `solo-nominato` o `mancante`;
- terminologia, numerazione e titoli coerenti;
- test e typecheck del repository verdi.

### Controlli editoriali

- fact-check su fonti primarie al cut-off;
- humanization selettiva;
- revisione editoriale totale con checklist a trenta punti;
- secondo controllo indipendente “zero errori”;
- similarity/originality check indicato come controllo editoriale, senza dichiarazioni di plagio non provate.

### Controlli di produzione

- Book Studio senza overflow, note interne o pagine improprie;
- PDF KDP verificato pagina per pagina;
- prova di stampa logica su margini, gerarchie e leggibilità delle figure;
- ebook/reflow verificato su almeno due viewport;
- pacchetto di consegna con checksum e limiti residui dichiarati.

## Definizione di completamento

Il retrofit è completato quando:

1. i quindici capitoli e le cinque appendici esistono nel formato previsto;
2. tutte le promesse dell'indice sono complete o rinviate in modo preciso e verificato;
3. non restano residui redazionali nel prodotto;
4. introduzione, conclusione, fonti, quiz, casi e strumenti risultano coerenti;
5. gli audit normativi, editoriali, visuali e tecnici non presentano blocker;
6. PDF ed ebook superano il preflight;
7. il volume raggiunge lo step precedente al sign-off umano con pacchetto completo;
8. l'eventuale pubblicazione definitiva avviene soltanto dopo la conferma umana prevista dallo step 24.

## Fuori perimetro

- Modifica del contenuto comune di `VOL-01`.
- Copertura di AIFA, già esclusa dalla tassonomia del volume.
- Garanzia commerciale di copertura di ogni futuro bando.
- Promessa di aggiornamento automatico.
- Cancellazione massiva degli asset sorgente non utilizzati.
- Sostituzione del controllo editoriale e normativo umano conclusivo.

