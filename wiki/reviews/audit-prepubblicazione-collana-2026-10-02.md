---
id: review-audit-prepubblicazione-collana-2026-10-02
type: review
title: "Collana ConcorsoBook — primo audit indipendente prima della pubblicazione"
status: historical_superseded
domain: "concorsi pubblici italiani"
topics: ["copertura didattica", "accuratezza normativa", "autonomia dello studente"]
entities: []
source_refs: ["sources/logica-volumi-copertura-concorsobook-v4", "sources/principio-copertura-didattica-integrale-2026-07-17"]
book_refs: ["VOL-01", "VOL-02", "VOL-03", "VOL-04", "VOL-05", "VOL-06", "VOL-07", "VOL-08", "VOL-09", "VOL-10", "VOL-11", "VOL-12"]
confidence: medium
updated_at: 2026-10-02
created_at: 2026-10-02
review_required: true
canonical: false
tags: ["prepubblicazione", "audit-collana", "solo-segnalazioni", "revisione-in-corso"]
issue_type: content_and_coverage
severity: high
affected_pages: ["books/vol-02-enti-locali-polizia-locale", "books/moduli/m-fc02-agenzie-fiscali", "books/moduli/m-ir01-scuola", "books/moduli/m-tr03-tecnico-ingegneristico", "books/moduli/m-tr04-ambiente-protezione-civile"]
---

# Report editoriale — Collana ConcorsoBook

**Aggiornamento conclusivo del 2 ottobre 2026:** il presente documento conserva la ricognizione iniziale. La lettura integrale dei 326 capitoli/appendici cartacei è stata successivamente completata: consultare il [dossier conclusivo](audit-integrale-2026-10-02/README.md) e il [registro degli interventi](audit-integrale-2026-10-02/registro-interventi.md). Le limitazioni e gli stati aperti riportati sotto descrivono il primo giro, non lo stato finale della revisione. Correzioni ancora da applicare.


## 1. Sintesi editoriale

- Genere: manuali e workbook per concorsi pubblici, base comune e percorsi specialistici.
- Pubblico: candidati dei profili assegnati ai 12 volumi e ai 25 moduli specialistici.
- Mandato: individuare errori e integrazioni, proporli e applicarli soltanto in una fase successiva.
- Perimetro effettivamente controllato: inventario dei 12 volumi; risoluzione delle fonti dichiarate e dei wikilink sui file di capitolo; estrazione del testo dell'anteprima cartacea; riesecuzione dei gate di copertura disponibili; letture mirate dei passaggi indicati sotto e verifiche esterne selettive.
- Dimensione: 349 file nelle cartelle dei capitoli; 326 capitoli/appendici nel perimetro cartaceo corrente di Book Studio. La differenza comprende i 23 moduli del Ricettario digitale di VOL-01. Le prime pagine non sono comprese nel numero 326.
- Stato generale: **sono presenti problemi sostanziali che impediscono di confermare la prontezza dell'intera collana**. Questo è un primo audit, non una revisione integrale conclusa dei 326 capitoli.
- Nessuna correzione applicata ai manoscritti, alle matrici o allo stato della pipeline. Le proposte seguenti sono da attuare successivamente.

Evidenze riproducibili in `artifacts/review-collana-2026-10-02/`: inventario con SHA-256 dei manoscritti, estrazioni del testo Book Studio per volume, esiti JSON dei gate e script di ricognizione. Il registro per capitolo è [[reviews/registro-audit-collana-2026-10-02]].

## 2. Punti applicati della checklist

La checklist resta aperta. «Parziale» indica un controllo realmente avviato, non un esito positivo esteso al volume.

| Punto | Controllo | Copertura di questo audit |
| --- | --- | --- |
| 1 | Indice e struttura reale | Inventario globale; scarto VOL-02 documentato; titoli non confrontati integralmente. |
| 2 | Completezza strutturale | Parziale: confronto catalogo, schede e capitoli presenti. |
| 3 | Progressione logica | Parziale: passaggi campione scuola, fisco e tecnico. |
| 4 | Gerarchie e titoli | Rinvii controllati; gerarchie non revisionate integralmente. |
| 5 | Pubblicabilità | Giudizio limitato ai problemi accertati; nessun via libera globale. |
| 6 | Coerenza interna | Parziale: capitoli e sezioni discussi al punto 4. |
| 7 | Coerenza tra capitoli | Parziale: introduzione CCIAA, rinvii fiscali e cartaceo/digitale. |
| 8 | Terminologia | Parziale; limite anagrafico Avvocatura ancora da verificare. |
| 9 | Completezza delle spiegazioni | Lacune puntuali accertate; copertura semantica globale ancora aperta. |
| 10 | Definizioni | Parziale; nessuna attestazione globale. |
| 11 | Errori concettuali | Letture mirate; restante corpus da leggere. |
| 12 | Normativa e contenuti | Fonti ufficiali consultate per valutazione scolastica, piano ATA e categorie NTC; altre affermazioni non certificate. |
| 13 | Esempi | Parziale: simulazione VOL-02, laboratorio tecnico, esempio numerico di screening. |
| 14 | Richiami e apparati | Esistenza dei wikilink e fonti; tre ancore non risolte accertate. Non controllati tutti i rinvii in prosa. |
| 15 | Fonti | Esistenza delle source notes dichiarate; non equivalenza tra esistenza e sostegno effettivo al claim. |
| 16 | Sintassi | Solo campione; revisione riga per riga aperta. |
| 17 | Chiarezza | Campione: rinvii a strumenti staff e regole non spiegate. |
| 18 | Tono | Campione: residui editoriali nel testo per lo studente. |
| 19 | Stile didattico | Campione: confronto obiettivo, teoria, esercizio e autocorrezione. |
| 20 | Ripetizioni | Non eseguito sistematicamente. |
| 21 | Contraddizioni locali | Parziale; rinviata la questione anagrafica al punto 6. |
| 22 | Grammatica | Non eseguito sistematicamente. |
| 23 | Ortografia | Non eseguito sistematicamente. |
| 24 | Punteggiatura | Non eseguito sistematicamente. |
| 25 | Refusi | Non eseguito sistematicamente. |
| 26 | Uniformità grafica | Solo testo estratto; non verificata sull'impaginato. |
| 27 | Impaginazione | Non eseguita: i PDF candidati esistono, ma non sono stati ispezionati pagina per pagina in questo audit. |
| 28 | Layout | Non eseguito visivamente. |
| 29 | Leggibilità | Parziale sul testo; non attestata alla dimensione di stampa. |
| 30 | Qualità complessiva | Diagnosi iniziale motivata; revisione completa aperta. |

Gate aggiuntivo di copertura integrale: le matrici sono dichiarazioni da confrontare con il testo. Un esito automatico positivo non verifica ogni definizione, risposta ai quiz, norma o promessa formativa. I capitoli legacy non diventano errati solo perché più brevi di 3.000 parole: la regola locale prevede il warning di retrofit, non un blocco automatico generalizzato.

## 3. Tabella errori

Gli ID E01-E12 sono rilievi verificati nel perimetro descritto, non il numero totale degli errori della collana. Le lacune didattiche sono valutazioni motivate sul testo, distinte dagli errori normativi verificati e dalle anomalie formali dei gate. Le questioni non risolte sono separate al punto 6.

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | VOL-02, raccordo cap. 03 r. 85 e simulazione finale r. 33 | 6, 9, 19 — autonomia didattica | grave | Il lettore è invitato a tornare alla «source note» e a correggere la simulazione sulle source notes, che non fanno parte del libro. La dipendenza è presente anche nel testo estratto da Book Studio. | Indicare capitolo e paragrafo cartacei effettivi; fornire quattro svolgimenti ragionati per le quattro tracce, con ipotesi, criteri di punteggio e motivazione degli errori. Nel piano: «Rileggi il paragrafo indicato nel Diario e ricostruisci regola, ambito ed esempio». | proposto |
| E02 | VOL-06, M-IR01 cap. 06, «Uffici, attività e flussi di lavoro», r. 71; risposta da commissario r. 140 | 9, 12, 19 — copertura del ruolo DSGA | grave | Il piano delle attività viene rinviato genericamente alle fonti e al contesto; non è insegnata la sequenza contrattuale proposta DSGA, adozione dirigente, attuazione DSGA, centrale per il nucleo promesso. | Inserire la sequenza dell'art. 63, c. 1, CCNL 2019-2021, coordinata con il contratto successivo; distinguere regola nazionale e contenuti variabili della singola scuola. Proposta testuale al punto 4. | proposto |
| E03 | VOL-06, M-IR01 cap. 12, «Dall'attività all'evidenza», r. 94; note r. 201 | 12 — aggiornamento normativo | grave | L'O.M. 172/2020 è richiamata come riferimento per la valutazione primaria senza esplicitarne il superamento e senza spiegare l'O.M. 3/2025. La cautela generica sul controllo delle fonti non informa il candidato della disciplina già cambiata. | Sostituire il richiamo corrente con O.M. 3/2025 e legge 150/2024; distinguere valutazione in itinere, periodica/finale e comportamento. Conservare 172/2020 soltanto come antecedente storico datato. Proposta testuale al punto 4. | proposto |
| E04 | VOL-10, M-TR03 cap. 04, N-TR03-04-07, r. 176 | 9, 10, 19 — concetti solo nominati | grave | Riparazione/intervento locale, miglioramento e adeguamento sono elencati come diversi, ma non vengono spiegati i criteri che consentono al candidato di distinguerli. Nessun rinvio preciso chiude la lacuna. | Aggiungere un confronto basato su NTC §8.4: ambito dell'intervento, effetto sulla sicurezza, valutazione richiesta e casi; includere almeno un quesito di classificazione commentato. Proposta al punto 4. | proposto |
| E05 | VOL-02, raccordo cap. 01, r. 180 | 7 — coerenza tra capitoli | media | Il testo dichiara che il modulo Camere di commercio resta da validare prima della scrittura definitiva, mentre il volume corrente comprende i cinque capitoli M-FL03. | Descrivere il percorso effettivamente presente: ordinamento, registro/REA, servizi, organizzazione e laboratorio; eliminare il messaggio di lavorazione e indicare i rinvii pertinenti. | proposto |
| E06 | VOL-03, M-FC02 cap. 06 r. 325; cap. 14 rr. 76 e 417 | 14 — rinvii | media | Tre ancore puntano a titoli non più presenti nel capitolo 04. I file esistono, le sezioni sono state rinominate con gli ID di nucleo. | Cap. 06: usare «N-FC02-04-04 · IVA: operazioni, soggetti, detrazione e adempimenti». Cap. 14: usare «N-FC02-04-02 · Presupposto, soggetti e obbligazione tributaria» e «N-FC02-04-05 · Quadro UE fiscale, IVA e dogane». Ricontrollare anche il rinvio leggibile nell'export. | proposto |
| E07 | VOL-03, M-FC02 cap. 04, «Note di audit automatico», r. 737 | 17, 18, 28 — residui staff | media | Book Studio include nel testo lettore istruzioni come verificare prima della pubblicazione, coordinare i capitoli e ampliare i quiz della bozza. | Spostare l'intera sezione nell'artefatto di review; mantenere nel libro soltanto fonti leggibili, data dell'edizione e limiti pertinenti allo studente. | proposto |
| E08 | VOL-06, M-IR01 capp. 12 e 13, frontmatter e citazioni nel corpo | 15 — tracciabilità | media | Manca il file `sources/valutazione-competenze-digitali-docenti-dlgs-62-2017-om-172-digcompedu.md`, dichiarato in entrambi i capitoli e richiamato sei volte nel corpo complessivo. Non significa che tutte le affermazioni siano false, ma quella dipendenza non è verificabile. | Consolidare fonti ufficiali distinte per valutazione vigente e DigCompEdu, aggiornare riferimenti e verificare i claim uno per uno. Non creare una nota vuota per far passare il controllo. | proposto |
| E09 | VOL-06, M-IR01, es. capp. 02, 06, 12 | 15, 17, 26 — citazioni al lettore | media | Nel testo Book Studio compaiono titoli ricavati dagli slug interni, come «Fonti Ufficiali M Ir01 Scuola 2026 07 24». Nel cap. 12 compare anche «La source note sul digitale...». | Trasformare i richiami in fonti identificabili dallo studente: ente, titolo ufficiale, atto, anno e articolo pertinente; tenere i collegamenti wiki nel frontmatter. Verificare tutto M-IR01 nell'export. | proposto |
| E10 | VOL-10, M-TR03 cap. 13, N-TR03-13-03, r. 135 circa | 7, 14 — cartaceo e digitale | media | Il rinvio a VOL-01 «Risposta sintetica: scrivere poco, dire tutto» conduce a R19 del Ricettario, con outline 43, escluso dal cartaceo base. La destinazione esiste ma la sua collocazione è descritta in modo inesatto. | Usare VOL-01 cap. 15, «La lettura della traccia» e «Lo schema base: definizione, riferimento, funzione, esempio, conclusione», entrambi verificati; segnalare R19 separatamente come approfondimento digitale opzionale. | proposto |
| E11 | VOL-11, M-TR04 cap. 08 r. 98 e cap. 11 r. 182 | 18 — note di processo nel libro | media | Nel corpo leggibile restano «Il text freeze dovrà verificare...» e «da ricontrollare al text freeze». Sono istruzioni per lo staff. | Eseguire e registrare il controllo nel report; nel testo mantenere soltanto data e ambito della verifica effettiva. Non eliminare la frase facendo sembrare eseguita una verifica ancora aperta. | proposto |
| E12 | VOL-02, sei nuclei elencati al punto 4 | 5 — vincolo formale di produzione | lieve | I gate correnti rilevano sei nuclei da 596 a 599 parole, sotto il minimo 600. È un blocco formale riproducibile, non prova di insufficienza semantica. | Verificare conteggio e versione dei sorgenti; dove il deficit è reale, aggiungere un chiarimento utile e rieseguire il gate. Evitare riempitivi introdotti solo per raggiungere la soglia. | aperto |

## 4. Osservazioni per capitolo

### Quadro per volume

I numeri indicano il perimetro cartaceo estratto, comprese appendici e raccordi, non capitoli tutti letti integralmente.

| Volume | Capitoli/appendici | Esito di questa ricognizione e lavoro residuo |
| --- | ---: | --- |
| VOL-01 — Base PA | 32 | Inventariato; la pipeline è già riaperta su integrazioni. Riutilizzare il piano INT-01/04 esistente, senza dichiararlo completato. Verifica integrale di teoria e quiz ancora aperta. |
| VOL-02 — Enti locali | 51 | E01, E05, E12; testi di raccordo da riallineare ai moduli. Lo step 21 storico conta 50 capitoli e quattro raccordi, mentre oggi i raccordi sono cinque, inclusa la conclusione: verificare quale revisione copre la versione corrente. |
| VOL-03 — Funzioni centrali e fisco | 50 | E06-E07; tre ancore errate e istruzioni staff visibili. Audit tributario articolo per articolo ancora da rifare sul testo corrente. |
| VOL-04 — Giustizia | 17 | Inventario e collegamenti controllati. Lo step 10 non è disponibile nel run-state corrente; questo non dimostra l'assenza di revisioni precedenti. Contenuti e transizioni processuali da verificare integralmente. |
| VOL-05 — Authority | 15 | Inventario e gate disponibili positivi. Nessuna attestazione sostanziale globale; da controllare attribuzioni, rimedi, numeri e decorrenze autorità per autorità. |
| VOL-06 — Istruzione e cultura | 50 | E02-E03, E08-E09. Prima priorità M-IR01: correttezza normativa e autonomia didattica, poi IR02/03/04. |
| VOL-07 — Sanità | 25 | Integrazioni INT-05/08 già aperte. Nel campione M-SA03 cap. 05 il calcolo dello screening è aritmeticamente coerente: 18 veri positivi, 49 falsi positivi, VPP circa 26,9%. Non equivale a validazione clinica dell'intero capitolo o volume. |
| VOL-08 — ICT | 13 | Tutti i 13 gate correnti superati. Il primo controllo grezzo sulle tabelle segnalava 210 anomalie: non sono 210 errori del libro, perché includeva tabelle di retrofit non selezionate dal gate canonico. Revisione tecnica e normativa ancora aperta. |
| VOL-09 — Appalti e PNRR | 14 | Inventario e gate disponibili positivi; da verificare l'intero testo su Codice, correttivi, allegati, soglie datate e scadenze dei finanziamenti. |
| VOL-10 — Tecnico | 13 | E04, E10. Capp. 03-04 prevalentemente qualitativi; approfondimento quantitativo da calibrare sui bandi, come indicato al punto 6. Il superamento del gate legacy non prova sufficienza per un profilo ingegneristico. |
| VOL-11 — Ambiente | 14 | E11. Controllo normativo integrale ancora aperto, comprese decorrenze e recepimenti. |
| VOL-12 — Carriere speciali | 32 | Gate disponibili positivi; requisiti e calendario dei bandi vanno verificati per tornata. Il computo dell'età in M-SP03 resta una domanda di audit, non un errore giuridico accertato. |

### VOL-02 — raccordi e simulazione finale

Punto di forza: i quattro scenari permettono di distinguere i percorsi territoriali. Criticità: la griglia valuta metodo e comunicazione, ma non fornisce una soluzione sostanziale completa alle quattro tracce. E01 riguarda soprattutto l'esplicita dipendenza dalle source notes interne. L'integrazione proposta deve rendere possibile autocorreggersi con il libro: dati, assunzioni, competenza, attività, atto eventuale, errori e attribuzione del punteggio.

E12, esito JSON della riesecuzione del gate 10:

| Modulo / capitolo | Nucleo | Parole rilevate | Minimo |
| --- | --- | ---: | ---: |
| M-FL01 / 14 | N-FL01-14-02 | 598 | 600 |
| M-FL04 / 04 | N-FL04-04-02 | 596 | 600 |
| M-FL04 / 06 | N-FL04-06-05 | 598 | 600 |
| M-FL04 / 14 | N-FL04-14-02 | 597 | 600 |
| M-FL03 / 01 | N-FL03-01-02 | 598 | 600 |
| M-FL03 / 03 | N-FL03-03-01 | 599 | 600 |

La pipeline registra tutti gli step VOL-02 come `done`; il nuovo controllo non ha modificato lo stato. Per le correzioni occorrerà usare la riapertura prevista dal CLI.

### VOL-03 — M-FC02, capitoli 04, 06 e 14

Punto di forza: nel capitolo 04 le destinazioni di contenuto esistono. E06 richiede di riallineare i rinvii ai nuovi titoli, non di duplicare la teoria. E07 è stato riscontrato sia nel Markdown sia nei blocchi restituiti da Book Studio, quindi non è una falsa segnalazione dovuta alla lettura dei soli metadati.

### VOL-06 — M-IR01, capitolo 06

Punto di forza: sono distinte attività operative e competenze decisionali. La risposta resta però troppo generica su un oggetto esplicitamente insegnato, il piano ATA.

**Integrazione proposta per E02, non applicata:**

> Per il piano delle attività del personale ATA, l'art. 63, comma 1, del CCNL Istruzione e ricerca 2019-2021 distingue tre passaggi. Il DSGA elabora la proposta attraverso uno specifico incontro con il personale ATA. Il dirigente adotta il piano dopo averne valutato la coerenza con il PTOF e svolto le procedure di relazioni sindacali applicabili. L'attuazione puntuale spetta al DSGA. Le scelte della singola scuola si collocano entro questa ripartizione: non cambiano liberamente chi propone, chi adotta e chi attua.

Verifica proposta: «Chi adotta il piano?» Risposta attesa: dirigente scolastico; commento: il DSGA ne propone il contenuto e ne cura l'attuazione. Coordinare il richiamo alle relazioni sindacali con il contratto successivo, evitando di applicare indiscriminatamente un testo contrattuale storico.

Fonti consultate: [ARAN, CCNL 2019-2021, art. 63](https://www.aranagenzia.it/documento_pubblico/contratto-collettivo-nazionale-di-lavoro-del-personale-del-comparto-istruzione-e-ricerca-periodo-2019-2021/) e [ARAN, CCNL 2022-2024, art. 1, c. 13, continuità delle disposizioni compatibili](https://www.aranagenzia.it/documento_pubblico/contratto-collettivo-nazionale-di-lavoro-del-comparto-istruzione-e-ricerca-triennio-2022-2024/). La proposta è un'integrazione di teoria, non la descrizione di una specifica scuola.

### VOL-06 — M-IR01, capitoli 12 e 13

Punto di forza: obiettivo, attività ed evidenza vengono collegati correttamente sul piano del metodo. E03 riguarda il quadro normativo, E08 la fonte interna mancante, E09 la resa delle citazioni.

**Sostituzione proposta per E03, non applicata:**

> Per la valutazione periodica e finale degli apprendimenti nella scuola primaria, il quadro del D.Lgs. 62/2017 va letto con le modifiche della legge 150/2024 e con l'O.M. 3 del 9 gennaio 2025. Quest'ultima prevede giudizi sintetici correlati alla descrizione dei livelli di apprendimento e si applica dall'ultimo periodo dell'anno scolastico 2024/2025. Dal medesimo periodo cessano gli effetti dell'O.M. 172/2020. La valutazione in itinere conserva la propria funzione formativa; la disciplina del comportamento nella secondaria di primo grado va trattata separatamente.

Completare con una tabella dei giudizi e una domanda che distingua i due ordini di scuola, verificandoli sull'ordinanza e relativo allegato. Fonte ufficiale: [MIM, O.M. 3/2025](https://www.mim.gov.it/en/-/ordinanza-n-3-del-9-gennaio-2025) e [nota applicativa MIM, cessazione degli effetti del regime precedente](https://www.mim.gov.it/documents/7673905/8783413/29516-REG-1737622126100-Nota%2BOM%2B3_9.01.2025_valutazione%2Bprimaria%2Be%2Bsecondaria_Firmato.pdf/a91469a2-4f24-324f-92f0-d211a0120d9e?version=1.0).

### VOL-10 — M-TR03, capitoli 03, 04 e 13

Punto di forza: il testo distingue modello, vincoli, azioni, risposta, verifica e manutenzione; il mini-computo del capitolo 13 è corretto nei dati proposti: 8 × 3,5 × 24 = 672 euro.

**Integrazione proposta per E04, non applicata:** spiegare che l'intervento locale interessa parti o elementi senza modificare significativamente il comportamento complessivo e senza peggiorare la sicurezza; il miglioramento aumenta la sicurezza senza necessariamente raggiungere il livello richiesto per l'adeguamento; l'adeguamento deve raggiungere i livelli previsti dalla disciplina applicabile. Aggiungere i presupposti di obbligatorietà, le conseguenze sulla valutazione e casi commentati. Non basta suggerire di «verificare la disciplina».

Il confronto concettuale è riscontrabile nelle [NTC 2018, capitolo 8, §§8.4-8.4.3, fonte ufficiale](https://www.gazzettaufficiale.it/do/atto/serie_generale/caricaPdf?art.codiceRedazionale=18A00716&art.dataPubblicazioneGazzetta=2018-02-20&art.num=1&art.tiposerie=SG&cdimg=18A0071600100010110009&dgu=2018-02-20). Per la stesura finale completare il coordinamento con gli atti modificativi e applicativi citati nella source note; questo audit non certifica ogni prescrizione tecnica corrente.

E10: le due sezioni proposte del cap. 15 di VOL-01 esistono nel cartaceo; la destinazione R19 appartiene invece al Ricettario. Il rinvio può essere corretto senza duplicare il metodo nel volume specialistico.

## 5. Coerenza globale

**Criterio di sufficienza:** un lettore del profilo dichiarato deve poter ricostruire la regola e rispondere a una domanda pertinente usando il pacchetto previsto, con rinvii realmente accessibili. Un concetto elencato nell'indice o dichiarato `completo` in matrice non soddisfa da solo questo criterio.

La Bibbia operativa per questa revisione è: base comune in VOL-01; teoria di famiglia nello specialistico; approfondimenti di sottoprofilo solo quando necessari; digitale opzionale; fonti interne usate per verificare, non richieste al lettore; cautela su dati variabili dopo aver insegnato la parte stabile. Errori accertati, dubbi di verifica e scelte facoltative restano separati.

Sono stati tentati 321 gate 10 sui capitoli dichiarati nelle schede: **266 superati, 6 non superati, 49 non disponibili nel run-state corrente** (32 VOL-01 e 17 VOL-04). I cinque raccordi di VOL-02 sono nel testo commerciale ma fuori da quei 321 target. Non si deduce che non siano mai stati revisionati: lo step 21 storico ne menziona quattro, da riconciliare con i cinque attuali.

La scansione grezza delle matrici VOL-08 aveva conteggiato 210 anomalie. La funzione canonica `rowsForChapter` seleziona le righe pertinenti; i 13 gate di capitolo passano. **Quelle anomalie grezze non sono state trasformate in errori editoriali.** Analoga cautela vale per gli 869 richiami interni rilevati nei file grezzi: molti appartengono a sezioni staff o digitali. I rilievi E07/E09 sono fondati sul testo effettivamente estratto, non su quel conteggio indiscriminato.

Le revisioni precedenti restano evidenze storiche. Devono essere associate alla versione effettiva dei sorgenti e del PDF per sostenere un giudizio attuale. Il presente audit non riapre o chiude automaticamente nessuno step.

## 6. Contenuto da verificare

1. **Profondità quantitativa VOL-10.** Il cap. 03 introduce equilibrio, sollecitazioni e diagrammi, senza svolgere un calcolo strutturale o mostrare un diagramma risolto; il cap. 04 resta qualitativo su classi d'uso, combinazioni e geotecnica. La matrice limita gli output al riconoscimento qualitativo, mentre il catalogo presenta un verticale profondo per ingegneri e tecnici. Confrontare i bandi rappresentativi e le prove reali per determinare quali esercizi siano necessari. Proposta da valutare: corpo libero con reazioni, diagrammi di una trave semplice, controllo dimensionale e un esempio NTC datato. Non classificare ogni assenza di formula come errore per qualunque profilo.
2. **VOL-12, M-SP03, età per procuratore dello Stato.** Nel cap. 03 e nel cap. 06 compaiono «trentacinque anni non compiuti»; altrove «trentacinquesimo anno non superato». Verificare il computo giuridico e la data rilevante sul D.A.G. 114/2025, sulle fonti regolamentari e sulle indicazioni ufficiali. Non si afferma qui che il candidato di 35 anni compiuti sia ammesso o escluso. Verificare inoltre l'esito successivo del [rinvio pregiudiziale segnalato dalla Cassazione, ordinanza 19847/2025](https://www.cortedicassazione.it/en/civile_dettaglio.page?contentId=SZC45978), senza dedurre che il solo rinvio abbia eliminato il limite.
3. **VOL-01/VOL-07: integrazioni già individuate.** Collegare INT-01/08 di [[reviews/piano-integrazioni-vol-01-vol-07-2026-10-02]] al registro di questo audit. Sono attività in lavorazione, non esiti qui riverificati. Restano le esclusioni già registrate per Campania/ASL Caserta e cultura generale; questo audit non avvia quelle integrazioni.
4. **Copertura rispetto ai bandi.** Per ogni profilo, ricostruire materia → peso/frequenza nel campione dichiarato → nucleo → spiegazione → esercizio/quiz → fonte. Validare la rappresentatività dei campioni; non attribuire una percentuale di esaustività senza denominatore e metodo.
5. **Aggiornamento alla data dell'edizione.** Le schede riportano cut-off differenti, da luglio ad agosto 2026, e alcuni report hanno verifiche successive. Occorre fissare per ciascun volume una data coerente, verificare le modifiche intervenute e distinguere norme vigenti, transizioni e regole di una tornata storica. La data di questo audit non rende automaticamente aggiornato tutto il corpus al 2 ottobre.
6. **Quiz e soluzioni.** Restano da risolvere indipendentemente tutti i quiz: una sola risposta corretta quando prevista, distrattori non ambigui, motivazione compatibile con la teoria e con la fonte, ricalcolo dei risultati numerici. In questo giro non è stato eseguito il censimento integrale dei quesiti.
7. **PDF di consegna.** Verificare corrispondenza ai sorgenti attuali, pagine, indice, rinvii, immagini, leggibilità in bianco e nero, tabelle e box. Nessun vecchio preflight sostituisce il controllo dell'edizione dopo future correzioni.

## 7. Suggerimenti facoltativi (non errori)

- Una pagina iniziale per percorso con prerequisiti, moduli da studiare, prove allenate e limiti effettivi aiuterebbe la scelta del candidato.
- Distinguere visivamente «regola da conoscere», «dato della tornata» e «approfondimento facoltativo» può migliorare lo studio senza aumentare inutilmente il testo.
- Tenere separati nel registro gli interventi che correggono un errore e quelli che ampliano la preparazione oltre il perimetro già promesso.

Queste scelte non sostituiscono le correzioni E01-E12.

## 8. Priorità degli interventi

1. **Errori gravi di autonomia e copertura:** E01, E02, E04; collegare le integrazioni nazionali già in lavorazione senza duplicarle.
2. **Aggiornamento normativo accertato:** E03, con ricostruzione delle fonti E08. Verificare anche gli esercizi che dipendono dal quadro cambiato.
3. **Coerenza e rinvii:** E05, E06, E10; riconciliare il corpus corrente di VOL-02 con i report storici.
4. **Chiarezza del testo destinato al lettore:** E07, E09, E11.
5. **Vincoli formali e rifinitura:** E12, poi revisione linguistica e prova dell'impaginato.

Per completare l'incarico, procedere a blocchi con registro cumulativo: prima i nuclei critici già identificati, poi lettura sostanziale dei capitoli restanti in ordine di volume. Ogni blocco deve registrare copertura effettivamente letta, claim confrontati con fonti, quiz risolti ed eventuali dubbi residui. Le correzioni resteranno proposte finché non si entra nella successiva fase richiesta dall'utente.

## 9. Giudizio di pubblicabilità

**Non pubblicabile allo stato attuale come collana integralmente verificata.** La diagnosi è motivata da E01-E04 e dalle verifiche sostanziali ancora aperte; non è una dichiarazione che ciascuno dei 12 volumi contenga necessariamente errori gravi.

VOL-02, VOL-06 e VOL-10 presentano ostacoli puntuali di autonomia, aggiornamento o completezza da risolvere prima del via libera. Per gli altri volumi il giudizio finale è sospeso fino alla revisione sostanziale e visiva. I gate positivi non permettono di scrivere «perfetto», «esaustivo per ogni bando» o «tutti i contenuti verificati».

La condizione di uscita è: nessun errore grave aperto nel perimetro promesso; nessun nucleo necessario `mancante`, `solo-nominato` o `parziale`; dubbi fattuali risolti con evidenze; tutte le verifiche didattiche controllate; rinvii reali; PDF coerente con i sorgenti revisionati; completamento degli step pertinenti attraverso il CLI e conferma finale prevista dal progetto.

## 10. Limiti di questa revisione

- Non sono stati letti integralmente i 326 capitoli/appendici, né verificati tutti i bandi, tutte le fonti, tutti i quiz o tutti i casi.
- La risoluzione automatica delle ancore usa testo del titolo e normalizzazione; E06 è stato verificato anche leggendo i titoli reali. Non sono stati controllati tutti i rinvii scritti in prosa.
- Il controllo delle fonti rileva l'esistenza del file; non dimostra da solo autorevolezza, attualità, correttezza della sintesi o sostegno al claim.
- Le proposte normative sono limitate ai punti esaminati; prima dell'integrazione stabile occorre consolidare le fonti nel wiki e chiudere il coordinamento normativo pertinente.
- L'estrazione Book Studio è un controllo testuale. Non sono state ispezionate visivamente le pagine dei PDF candidati.
- Nessun manoscritto, matrice, PDF o run-state è stato corretto in questo incarico. Nuovi artefatti: report, registro, evidenze e traccia di memoria/log.
- La revisione complessiva richiesta resta **in corso**. Il registro rende esplicito il lavoro residuo e impedisce di scambiare la ricognizione automatica per una certificazione integrale.
- Il confronto finale degli hash rileva quattro manoscritti cambiati durante la ricognizione, senza interventi di questo incarico: VOL-01 capp. 05 e 06; VOL-07/M-SA01 capp. 04 e 09. Sono i target delle integrazioni già in lavorazione. I loro snapshot iniziali e gli esiti di questo giro non certificano la nuova versione: occorre rileggerla e ripetere i controlli. Gli altri 345 file di capitolo risultavano invariati al controllo delle 20:20 UTC; i rilievi E01-E12 non riguardano i quattro file cambiati.
