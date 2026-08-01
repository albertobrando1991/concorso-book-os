---
id: prompt-staff-revisione-completa-volumi
type: workflow-template
title: Prompt cronologici per revisione completa e pubblicazione dei volumi
status: active
domain: editoriale
topics:
  - workflow-editoriale
  - moduli-specialistici
  - pubblicazione-kdp
entities:
  - ConcorsoBook OS
source_refs:
  - "[[sources/logica-volumi-copertura-concorsobook-v4]]"
  - "[[sources/principio-copertura-didattica-integrale-2026-07-17]]"
book_refs:
  - "[[books/moduli/architettura-moduli-specialistici]]"
confidence: high
updated_at: 2026-07-27
created_at: 2026-07-27
review_required: false
canonical: true
tags:
  - staff
  - prompt
  - revisione
  - kdp
---

# Prompt cronologici per revisione completa e pubblicazione dei volumi

## Come usare il protocollo

I prompt devono essere eseguiti nell'ordine indicato. Non saltare un gate e non iniziare il prompt successivo finché l'output richiesto non è stato verificato.

Sostituire sempre:

- `[VOLUME_CODE]`: codice del volume, per esempio `VOL-03`;
- `[VOLUME_TITLE]`: titolo commerciale;
- `[MODULE_CODE]`: codice del modulo, per esempio `M-FC02`;
- `[MODULE_ID]`: slug/cartella del modulo;
- `[CHAPTER_FILE]`: percorso del capitolo;
- `[CHAPTER_NUMBER]`: numero o codice del capitolo;
- `[CUT_OFF_DATE]`: data di chiusura delle fonti;
- `[RESPONSABILE]`: referente umano dell'attività.

Ordine delle ripetizioni:

1. i prompt 00-03 si eseguono una volta per l'intero catalogo;
2. i prompt 04-07 si ripetono per ogni volume e modulo;
3. i prompt 08-12 si ripetono per ogni capitolo, in ordine;
4. i prompt 13-23 si eseguono sul modulo o volume completo;
5. il prompt 24 avvia la manutenzione successiva alla pubblicazione.

Ogni agente deve leggere `AGENTS.md` e `wiki/AGENTS.md`, richiamare `LocalAgentMemory` e preservare il lavoro umano e degli altri agenti. Norme, date e fatti devono derivare dal wiki consolidato; la memoria non è una fonte normativa.

---

## Prompt 00 — Presa in carico e regole operative

```text
Stai lavorando nel progetto ConcorsoBook OS.

Prima di qualsiasi modifica:
1. leggi integralmente AGENTS.md e wiki/AGENTS.md;
2. richiama tramite LocalAgentMemory le memorie pertinenti a [VOLUME_CODE], [MODULE_CODE], revisione editoriale, copertura didattica, Humanizer, immagini e KDP;
3. leggi l'architettura canonica dei moduli e il design system editoriale;
4. controlla lo stato Git senza modificare o cancellare file;
5. dichiara quali skill userai e in quale ordine.

Regole vincolanti:
- preserva il lavoro umano e degli altri agenti;
- non usare raw/ come fonte del testo editoriale finale;
- non inventare norme, articoli, date, dati o fonti;
- non procedere se il target non è identificato con certezza;
- non eseguire reset, checkout distruttivi o cancellazioni;
- non dichiarare completo un contenuto con nuclei parziali, solo nominati o mancanti.

Output richiesto:
- target identificato;
- file canonici coinvolti;
- memoria richiamata;
- stato Git;
- rischi o collisioni;
- piano operativo strettamente limitato all'incarico.

Non modificare ancora i contenuti.
```

Gate: target, perimetro e condizioni Git devono essere chiari.

## Prompt 01 — Raccolta sicura del lavoro dello staff

```text
Esegui un censimento completo del lavoro dello staff relativo a tutti i volumi e moduli.

Controlla:
- branch, commit e modifiche disponibili;
- file locali modificati o non tracciati;
- capitoli, front matter, planning, matrici, fonti, quiz, immagini e report;
- eventuali versioni concorrenti dello stesso file;
- contenuti presenti solo come scaffold;
- contenuti che sembrano completi ma non hanno fonti o frontmatter valido.

Non sovrascrivere e non integrare ancora nulla.

Produci una tabella con:
Volume | Modulo | File | Autore/branch se rilevabile | Stato contenuto | Stato fonti | Stato immagini | Possibile collisione | Azione proposta.

Classifica ogni elemento come:
utilizzabile / da consolidare / da completare / duplicato / conflitto / scaffold / da verificare.

Segnala separatamente tutto ciò che non è ancora presente nel branch principale.
```

Gate: ogni contributo dello staff deve avere una destinazione o una decisione esplicita.

## Prompt 02 — Consolidamento dei contributi senza perdita di lavoro

```text
Integra nel ramo di lavoro i contributi approvati dal censimento del Prompt 01.

Procedi con patch chirurgiche:
- conserva il testo umano valido;
- unisci solo sezioni compatibili;
- non scegliere arbitrariamente fra versioni in conflitto;
- sposta piani interni in planning/ e non nei capitoli destinati al lettore;
- mantieni la provenienza nei log o nelle note di review;
- non duplicare capitoli, sezioni, tabelle o immagini;
- non cancellare una versione sostituita senza una traccia verificabile.

Per ogni file modificato indica:
origine del contributo | integrazione applicata | contenuto preservato | conflitti rimasti.

Esegui git diff --check e mostra il riepilogo delle modifiche. Non fare commit o push.
```

Gate: nessuna collisione irrisolta e nessun contributo approvato perso.

## Prompt 03 — Riconciliazione del catalogo e dei perimetri

```text
Verifica la coerenza fra:
- src/catalog/text-volumes.ts;
- wiki/books/moduli/architettura-moduli-specialistici.md;
- cartelle reali in wiki/books/moduli/;
- book_id, module_code e module_family dei capitoli;
- numero canonico di 12 volumi commerciali e 25 moduli.

Individua moduli orfani, duplicati, mancanti o assegnati al volume sbagliato.
Applica la logica di copertura v4: contenuti comuni nel VOL-01, contenuti di famiglia nel modulo corretto, sottoprofili in appendice o verticale necessario, altre famiglie tramite rinvio preciso.

Produci prima la diagnosi. Applica soltanto le correzioni di catalogo non ambigue e documentate.

Output:
- mappa definitiva Volume -> moduli -> book_id;
- discrepanze rilevate;
- patch applicate;
- decisioni che richiedono approvazione umana.
```

Gate: catalogo applicativo, architettura wiki e filesystem devono coincidere.

---

## Prompt 04 — Scheda di apertura del volume

```text
Apri il ciclo editoriale di [VOLUME_CODE] — [VOLUME_TITLE].

Leggi indice, introduzione, moduli assegnati, capitoli presenti, piani editoriali, source notes, topic pages, entity pages, quiz, recensioni e matrici esistenti.

Definisci:
- pubblico e profili concorsuali;
- promessa editoriale verificabile;
- materie e nuclei inclusi;
- contenuti comuni già coperti dal VOL-01;
- rinvii ammessi;
- esclusioni;
- dipendenze fra moduli;
- review umane necessarie;
- ordine definitivo di lavorazione.

Costruisci una Bibbia del Volume con terminologia canonica, tono, livello di profondità, struttura ricorrente, regole dei box e criteri per esempi, casi ed esercizi.

Non completare ancora i capitoli.
```

Gate: perimetro e promessa devono essere misurabili e privi di duplicazioni con il Volume 1.

## Prompt 05 — Audit dei bandi rappresentativi

```text
Per [MODULE_CODE] raccogli e analizza 5-6 bandi rappresentativi per ciascun cluster prioritario.

Usa fonti ufficiali o istituzionali. Registra:
- ente;
- profilo e sottoprofilo;
- requisiti;
- materie;
- peso o ricorrenza delle materie;
- tipologia delle prove;
- output richiesti;
- strumenti o competenze specialistiche;
- elementi mobili da ricontrollare.

Non trasferire direttamente il testo del bando nel capitolo.
Salva ogni fonte secondo la policy di ingest: raw immutabile se necessario, source note consolidata, topic/entity aggiornati, collegamenti ai capitoli impattati e log append-only.

Output:
- corpus dei bandi;
- tabella delle ricorrenze;
- differenze tra profili;
- lacune dell'attuale indice;
- data di controllo [CUT_OFF_DATE].
```

Gate: corpus rappresentativo e fonti consolidate disponibili.

## Prompt 06 — Audit e consolidamento delle fonti

```text
Controlla tutte le fonti necessarie per [MODULE_CODE].

Per ogni nucleo previsto verifica:
- presenza di una source note consolidata;
- autorevolezza e data;
- collegamenti a topic ed entity;
- vigenza normativa o necessità di review;
- eventuali conflitti fra fonti;
- parti mobili che non devono essere presentate come stabili.

Non scrivere il capitolo se una fonte indispensabile manca.
Se devi effettuare ricerca web, usa fonti primarie e trasformale in source notes consolidate prima di usarle editorialmente.

Produci:
Nucleo | Fonte consolidata | Autorità | Ultimo controllo | Rischio di aggiornamento | Capitolo impattato | Stato.
```

Gate: ogni nucleo ha fonti sufficienti oppure è formalmente bloccato.

## Prompt 07 — Matrice di copertura didattica v4

```text
Costruisci o aggiorna la matrice di copertura didattica di [MODULE_CODE].

Per ogni nucleo registra:
profilo | materia | concetto | priorità | fonti | collocazione | teoria | esempio/caso | uso nella prova | verifica/esercizio | stato | review normativa | note.

Usa esclusivamente questi stati:
- completo;
- parziale;
- solo-nominato;
- rinviato;
- mancante.

Un rinvio è valido solo se la destinazione è precisa, completa, aggiornata e verificata.
Non dedurre la completezza dalla lunghezza, dal numero di titoli, dai quiz o dalla presenza di casi.

Calcola i totali e genera l'elenco ordinato dei blocker:
1. alta priorità;
2. media priorità;
3. bassa priorità.

Non dichiarare il modulo pubblicabile finché esiste almeno un parziale, solo-nominato o mancante.
```

Gate: matrice completa, coerente con i bandi e con il contenuto reale.

---

## Prompt 08 — Piano operativo del singolo capitolo

```text
Prepara il piano di completamento di [CHAPTER_FILE], capitolo [CHAPTER_NUMBER] di [MODULE_CODE].

Leggi:
- specifica del capitolo;
- matrice di copertura;
- Bibbia del Volume;
- fonti, topic, entity e quiz collegati;
- capitoli precedenti e successivi;
- contenuti del VOL-01 ai quali è consentito rinviare.

Elenca:
- nuclei assegnati con Nucleo ID stabile;
- nuclei già completi;
- nuclei da sviluppare;
- sezioni da conservare;
- duplicazioni da evitare;
- esempi, casi, domande ed esercizi necessari;
- fonti da usare;
- review umane richieste.

Proponi la struttura H1/H2/H3, 5-7 nuclei per blocco di verifica e il budget parole/quiz/casi previsto dalla scheda pipeline.
Non modificare ancora il capitolo.
```

Gate: piano approvabile e collegato riga per riga alla matrice.

## Prompt 09 — Scrittura o completamento professionale del capitolo

```text
Usa la skill concorso-book-professional-writer per completare [CHAPTER_FILE].

Obiettivo canonico: scrivi un capitolo didattico autosufficiente per lo studente che prepara un concorso pubblico e non dispone della wiki, della dashboard o delle note editoriali interne. Il testo deve trasmettere integralmente le conoscenze assegnate al capitolo e renderle utilizzabili nelle prove.

Scrivi il vero testo destinato al lettore, non un riepilogo del lavoro.
Preserva e integra il testo umano valido. Non cancellare sezioni fuori dal perimetro.

Il capitolo deve sviluppare, quando pertinenti:
- apertura editoriale;
- obiettivo;
- Mappa BANDO;
- spiegazione progressiva: definizione, funzione, inquadramento, elementi, distinzioni e conseguenze;
- box "Da sapere in 5 righe";
- esempio o caso guidato;
- domanda da commissario;
- domanda-trappola;
- errore tipico;
- mini-esercizio o checklist;
- riferimenti normativi e professionali essenziali, espressi in forma leggibile;
- un blocco ▣ Verifica ogni 5-7 nuclei;
- almeno 6 quiz con risposta commentata e un caso ragionato;
- note di review in un report separato, mai nel testo del lettore.

Vincoli:
- un solo H1;
- gerarchia H2/H3 coerente;
- paragrafi brevi e impaginabili;
- nessun claim privo di fonte;
- nessuna norma, data o soglia inventata;
- nessuna duplicazione del nucleo comune del VOL-01;
- nessun placeholder o meta-commento dell'agente;
- nessun wikilink nel corpo verso sources/, topics/, entities/, raw/, planning/ o reviews/;
- nessuna formula che chieda allo studente di consultare source note, fonti consolidate, corpus interni, wiki o report;
- le fonti consolidate sono input editoriali: nel capitolo devi sviluppare direttamente definizioni, quadro, elementi, distinzioni, conseguenze, esempi e uso concorsuale;
- ogni promessa formativa deve avere spiegazione o rinvio preciso.
- ogni nucleo usa l'heading `N-<MODULO>-<CAP>-<NN> · <titolo>` e sviluppa teoria essenziale, schema/tabella e applicazione al profilo;
- almeno 5 nuclei, 600 parole per nucleo e 3.000 parole per capitolo, salvo soglie più alte nella scheda;
- i dati clinici o tecnici operativi usano il box `Dato operativo` con fonte ufficiale, ambito, versione, data di verifica e revisore; niente dosi, energie o sequenze eseguibili.

Aggiorna frontmatter, `format_version: 2`, `dati_operativi`, last_compiled_from, source_refs, draft_stage e review_required in modo veritiero. Registra gli eventuali punti aperti nell'evidenza o nel report di review della pipeline, non come parte della lezione destinata allo studente.
```

Gate: testo editoriale effettivo, autosufficiente per lo studente, tracciabile nel frontmatter e completo rispetto al piano.

## Prompt 09-R — Retrofit del capitolo legacy

```text
Esegui il retrofit di [CHAPTER_FILE] senza introdurre claim nuovi.

1. Archivia Scheda di lavoro e Note di review editoriale in wiki/reviews/retrofit/.
2. Appiattisci il contenitore Testo editoriale senza perdere contenuto destinato al lettore.
3. Proponi e fai approvare la mappatura heading → Nucleo ID.
4. Raggruppa l'apparato esistente nei blocchi ▣ Verifica e deriva quiz solo dal testo consolidato.
5. Compila la checklist dimensionale: ogni lacuna sostanziale scala il nucleo da livello A a livello B.
6. Imposta format_version: 2 soltanto quando gate quantitativo e checklist qualitativa sono entrambi conformi.
```

Gate: nessuna perdita di contenuto; ogni promozione al formato 2 è provata dalla matrice e dal gate.

## Prompt 10 — Controllo di copertura del capitolo

```text
Confronta [CHAPTER_FILE] con tutte le righe della matrice che gli sono assegnate.

Per ogni Nucleo ID compila nella matrice la checklist dimensionale con `✓` e evidenza, `✗` e motivo oppure `n/a`:
- definizione;
- funzione;
- inquadramento;
- elementi;
- distinzioni;
- conseguenze;
- esempio/caso;
- uso nella prova;
- errore tipico;
- verifica;
- tracciabilità nel frontmatter e riferimenti leggibili nel corpo.

Non considerare casi, quiz o checklist sostitutivi della teoria.
Non considerare un wikilink, una source note o un rinvio a materiale interno come prova di copertura.
Classifica ogni nucleo e cita heading o passaggio che prova la copertura. Una dimensione applicabile vuota o negativa produce `dimensione-mancante`.

Applica le integrazioni necessarie soltanto se supportate dal wiki consolidato.
Aggiorna la matrice con lo stato reale e produci il delta:
nucleo | stato prima | intervento | stato dopo | evidenza.
```

Gate: nessun blocker assegnato al capitolo.

## Prompt 11 — Humanizer del capitolo

```text
Applica la skill humanizer a [CHAPTER_FILE], ora stabile sul piano contenutistico.

Preserva integralmente:
- significato;
- terminologia tecnica;
- riferimenti normativi;
- citazioni e riferimenti professionali leggibili;
- struttura didattica;
- source_refs e last_compiled_from nel frontmatter;
- rinvii didattici verso altri capitoli pubblicabili;
- esempi, casi, quiz e istruzioni operative.

Rimuovi dal corpo eventuali wikilink verso sources/, topics/, entities/, raw/, planning/ o reviews/ e ogni formula redazionale interna. Non introdurre nuovi link interni. La loro tracciabilità resta nel frontmatter e nei report.

Correggi:
- formule palesemente generate da AI;
- tono promozionale o enfatico;
- frasi tutte uguali;
- gerundi e participi aggiunti senza funzione;
- vaghe attribuzioni;
- ripetizioni e regola del tre artificiale;
- meta-commenti da chatbot;
- eccesso di grassetto, titoli meccanici e conclusioni generiche;
- sintassi passiva o contorta quando l'attivo è più chiaro.

Esegui la doppia passata obbligatoria:
1. individua ciò che rende ancora il testo riconoscibile come AI;
2. correggi tali segnali senza rendere il manuale colloquiale o impreciso.

Non aggiungere opinioni personali, umorismo o prima persona se incompatibili con un manuale professionale per concorsi.

Output:
- file aggiornato;
- segnali AI rimossi;
- conferma che significato, source_refs e riferimenti normativi non sono cambiati;
- conferma che il corpo non dipende da collegamenti o strumenti interni;
- eventuali punti che richiedono controllo umano.
```

Gate: voce naturale, autorevole e coerente con la collana.

## Prompt 12 — Revisione editoriale del capitolo

```text
Usa la skill revisore-editoriale-totale su [CHAPTER_FILE].

Applica in ordine:
1. struttura;
2. coerenza del capitolo;
3. contenuto e didattica;
4. frase e paragrafo;
5. grammatica, ortografia, punteggiatura e refusi.

Controlla anche la copertura v4 e i rinvii al VOL-01 o ad altri moduli.
Non riscrivere silenziosamente il testo.

Esegui il test dello studente: valuta il capitolo senza frontmatter e senza accesso a wiki, dashboard, source note o report. Se una definizione, distinzione, conseguenza, procedura concorsuale o spiegazione necessaria manca in queste condizioni, classifica il problema come errore grave e proponi l'integrazione nel testo.

Produci una tabella:
ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato.

Separa:
- errori oggettivi;
- fatti o norme da verificare;
- suggerimenti facoltativi.

Applica direttamente solo correzioni oggettive e inequivoche autorizzate. Per interventi strutturali formula una proposta verificabile.
Aggiorna la matrice se la revisione dimostra che un nucleo non è realmente completo.
```

Gate: nessun errore grave aperto nel capitolo.

---

## Prompt 13 — Revisione trasversale del modulo completo

```text
Ora che tutti i capitoli di [MODULE_CODE] hanno superato i gate individuali, esegui una revisione trasversale.

Leggi prima indice, introduzione e tutti i capitoli. Costruisci o aggiorna la Bibbia del Modulo.

Verifica:
- progressione logica;
- dipendenze tra capitoli;
- coerenza terminologica;
- ripetizioni;
- contraddizioni;
- promesse dell'introduzione;
- corrispondenza indice/capitoli;
- rinvii;
- esempi e casi distribuiti;
- equilibrio fra teoria e workbook;
- coerenza dei profili;
- assenza di duplicazioni con VOL-01 e altre famiglie;
- corrispondenza integrale con la matrice.

Produci il report nel template fisso del Revisore Editoriale Totale.
Non dichiarare ancora il modulo pubblicabile se restano errori gravi o nuclei bloccanti.
```

Gate: struttura e contenuti del modulo coerenti nel loro insieme.

## Prompt 14 — Correzione del report editoriale

```text
Applica le correzioni del report editoriale di [MODULE_CODE] in questo ordine:
1. errori gravi strutturali e contenutistici;
2. errori normativi o fattuali verificati;
3. incoerenze tra capitoli;
4. chiarezza e stile;
5. refusi e uniformità grafica.

Per ogni ID registra:
ID | file modificato | correzione | fonte/evidenza | stato finale.

Non applicare come obbligatori i suggerimenti facoltativi.
Se una correzione cambia sostanzialmente un passaggio, ripeti su quel passaggio:
- controllo di copertura;
- Humanizer;
- micro-revisione editoriale.

Aggiorna matrice, frontmatter e report senza falsificare gli stati.
```

Gate: tutte le voci obbligatorie chiuse o formalmente assegnate a verifica umana.

## Prompt 15 — Review umana specialistica

```text
Prepara il pacchetto di review umana di [MODULE_CODE] per [RESPONSABILE].

Non chiedere una lettura generica. Estrai una checklist precisa con:
- claim normativi e articoli;
- definizioni tecniche;
- procedure;
- soglie, termini e dati mobili;
- casi ed esercizi che applicano regole specialistiche;
- punti già marcati review_required;
- conflitti o incertezze emersi.

Per ogni voce indica:
file e posizione | affermazione | fonte consolidata | domanda al revisore | esito | eventuale correzione.

Il contratto dello step aggiunge automaticamente una riga per ogni box `Dato operativo` rilevato nei capitoli. Queste righe sono obbligatorie: non eliminarle, completa l'esito con attribuzione al revisore indicato nel box.

Integra soltanto gli esiti firmati o chiaramente attribuiti al revisore umano.
Registra data, perimetro e limiti della review.
```

Gate: nulla osta specialistico completato per tutti i punti ad alto rischio.

## Prompt 16 — Congelamento del testo

```text
Verifica che [MODULE_CODE] possa entrare in text freeze.

Condizioni:
- tutti i capitoli presenti;
- zero parziale, solo-nominato o mancante;
- rinvii precisi e verificati;
- Humanizer completato;
- errori gravi e medi obbligatori chiusi;
- review umana completata;
- indice coerente;
- fonti e cut-off dichiarati.

Produci un manifest con elenco file, stato, data e hash/commit di riferimento.
Da questo momento sono ammesse solo correzioni controllate; ogni modifica sostanziale riapre i gate 10-15.
```

Gate: text freeze formalmente approvato.

---

## Prompt 17 — Filosofia visiva del volume

```text
Usa la skill canvas-design per definire la filosofia visiva di [VOLUME_CODE].

Prima di creare immagini, scrivi un file .md con:
- nome del movimento visivo;
- 4-6 paragrafi su spazio, forma, colore/materiale, scala/ritmo, composizione, equilibrio e gerarchia;
- ruolo minimo del testo;
- standard di meticolosa esecuzione professionale;
- compatibilità con il design system ConcorsoBook OS e il formato KDP 6,69 x 9,61 in.

La filosofia deve guidare diagrammi, mappe, schede ed esercizi senza diventare un template rigido.
Non creare ancora asset.
```

Gate: filosofia visiva approvata e coerente con la collana.

## Prompt 18 — Audit e ottimizzazione delle immagini

```text
Usa canvas-design per revisionare tutte le immagini di [MODULE_CODE] nel contesto del Book Studio.

Per ogni asset controlla:
- funzione didattica;
- correttezza del testo;
- ordine di lettura;
- allineamenti;
- margini di sicurezza;
- contrasto in bianco e nero;
- risoluzione;
- proporzioni;
- coerenza di palette, tratti e icone;
- rapporto con didascalia e testo vicino;
- asset path;
- overflow, collisioni, ritagli e sovrapposizioni;
- immagini consecutive prive di raccordo;
- tabelle o esercizi troppo densi.

Correggi soprattutto ciò che esiste: elimina rumore, riallinea, riequilibra e semplifica.
Non aggiungere grafica decorativa.
Non usare più di tre colonne compatte negli esercizi; dividi le griglie dense invece di ridurre il carattere.

Esegui una seconda passata esclusivamente su precisione e uniformità.

Output:
asset | problema | correzione | verifica nel Book Studio | esito.
```

Gate: zero sovrapposizioni, testi tagliati, path rotti o immagini fuori scala.

## Prompt 19 — Impaginazione KDP

```text
Applica a [VOLUME_CODE] il master editoriale canonico:
- pagina 6,69 x 9,61 in, 16,99 x 24,41 cm;
- bianco e nero su carta bianca, senza bleed;
- corpo Garamond 11 pt, interlinea 1,15-1,20, testo giustificato;
- H1 Arial Bold 20 pt, H2 14 pt, H3 12 pt;
- strumenti, box, tabelle e quiz Arial 9,5-10 pt;
- colonna singola;
- margini speculari e gutter compatibili con il conteggio finale;
- pagine singole numerate;
- front matter canonico;
- indice analitico con capitoli e numeri decimali dei nuclei (es. 5.4), derivati dai Nucleo ID;
- blocchi ▣ Verifica visivamente distinti, leggibili in bianco e nero e senza spezzature ambigue;
- nessun titolo orfano;
- nessun blocco oltre i margini.

Non eliminare testo o immagini per far rientrare il layout.
Intervieni su riflusso, spaziatura, divisione delle tabelle, dimensione controllata degli asset e page break motivati.
```

Gate: master coerente e interamente renderizzato.

## Prompt 20 — Audit pagina per pagina

```text
Controlla nel Book Studio ogni pagina di [VOLUME_CODE], dalla prima all'ultima.

Registra:
pagina | tipo di problema | elemento | gravità | correzione | esito.

Verifica:
- numerazione progressiva;
- front matter;
- titoli e gerarchie;
- testo giustificato;
- font e dimensioni;
- righe vedove e orfane;
- spazi bianchi anomali;
- pagine quasi vuote non motivate;
- tabelle spezzate o non formattate;
- pipe Markdown o linee residue visibili;
- box ed esercizi;
- immagini e didascalie;
- immagini consecutive;
- margini e gutter;
- overflow;
- asset mancanti;
- coerenza recto/verso.

Correggi e ripeti il controllo sulle pagine impattate. Non limitarti a un campione.
```

Gate: zero anomalie gravi e nessuna pagina non verificata.

## Prompt 21 — Revisore Editoriale Totale sull'impaginato finale

```text
Esegui la revisione finale completa di [VOLUME_CODE] usando revisore-editoriale-totale.

Leggi l'intero indice e tutti i capitoli, quindi applica i 30 controlli:
- macrostruttura;
- livello di capitolo;
- frase e paragrafo;
- superficie e layout.

Aggiungi il gate di copertura v4 e verifica:
- zero nuclei bloccanti;
- rinvii reali;
- fonti e cut-off;
- review umane;
- immagini;
- impaginazione KDP;
- corrispondenza fra indice e pagine.

Usa il template report fisso e formula uno dei tre giudizi:
- Pubblicabile con correzioni minori;
- Pubblicabile dopo intervento medio;
- Non pubblicabile allo stato attuale.

Motiva il giudizio con gli ID della tabella errori.
```

Gate: il giudizio deve essere "Pubblicabile con correzioni minori" e non devono esistere errori gravi.

## Prompt 22 — Preflight tecnico ed editoriale

```text
Esegui il preflight finale di [VOLUME_CODE].

Controlli minimi:
- audit di copertura;
- link wiki;
- source_refs;
- frontmatter;
- asset path;
- file mancanti;
- immagini duplicate;
- tabelle anomale;
- caratteri corrotti;
- git diff --check;
- test pertinenti;
- typecheck;
- build;
- export PDF;
- font incorporati;
- dimensione pagina;
- bleed;
- margini;
- conteggio pagine;
- eventuali warning del KDP Previewer.

Non correggere un errore tecnico eliminando contenuto editoriale.
Produci una checklist pass/fail con evidenza e comando o verifica usata.
```

Gate: tutti i controlli obbligatori passano.

## Prompt 23 — Consegna, commit e pubblicazione controllata

```text
Prepara la consegna di [VOLUME_CODE].

Prima del commit:
- verifica lo stato remoto e le modifiche dello staff;
- assicurati di non includere file estranei, cache, log temporanei o artifact non richiesti;
- esegui staging selettivo;
- controlla git diff --cached e git diff --cached --check;
- ripeti i gate tecnici finali.

Registra:
- versione editoriale;
- cut-off normativo;
- report di pubblicabilità;
- manifest dei file;
- changelog;
- limiti e review future.

Esegui commit e push soltanto dopo l'approvazione prevista dal flusso.
Confronta SHA locale e remoto e comunica il risultato esatto.

Non dichiarare pubblicato ciò che è soltanto committato localmente.
```

Gate: consegna tracciata, remoto allineato e pacchetto di pubblicazione identificabile.

## Prompt 24 — Manutenzione post-pubblicazione

```text
Apri il ciclo di manutenzione di [VOLUME_CODE].

Definisci:
- data di prossima revisione;
- fonti e norme ad alta volatilità;
- bandi da ricampionare;
- capitoli sensibili;
- responsabili umani;
- scadenza della review semestrale;
- criteri che riaprono il gate di pubblicazione.

Ogni nuova fonte deve seguire ingest, consolidamento, topic/entity, capitoli impattati, review_required, matrice, revisione e nuovo preflight.

Aggiorna dashboard, log append-only e memoria LocalAgentMemory con una sintesi operativa, senza usare la memoria come fonte normativa.
```

Gate: volume inserito nel ciclo di aggiornamento e responsabilità assegnate.

---

## Sequenza iniziale raccomandata

Con la fotografia attuale del progetto, dopo i prompt globali 00-03:

1. applicare 04-07 a `VOL-03`;
2. chiudere con 08-12 i 14 nuclei parziali di `M-FC02`;
3. completare `M-FC01`;
4. sviluppare `M-FC03`;
5. eseguire 13-23 sull'intero `VOL-03`;
6. ripetere la pipeline su `VOL-09`, `VOL-02`, `VOL-06`, `VOL-07`, `VOL-08`, `VOL-10`, `VOL-04`, `VOL-11`, `VOL-05`, `VOL-12`, salvo diversa priorità emersa dal censimento dello staff.

Non tenere più di un volume nel gate finale di revisione e impaginazione. Lo staff può preparare fonti e matrici del volume successivo, ma il text freeze, la revisione totale e il preflight restano seriali.
