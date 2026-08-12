# VOL-10 Format 2 Retrofit Design

## Obiettivo

Portare i tredici capitoli di M-TR03 dal formato legacy al formato 2 della pipeline aggiornata, rieseguire i gate editoriali e consegnare VOL-10 nello stato `ready_for_human_signoff`. Lo step 24 resta aperto perché costituisce la conferma umana conclusiva non delegabile.

## Baseline verificata

Il Book Studio renderizza 93 pagine, 6 sezioni di front matter, 1 apertura di modulo e 13 capitoli. Tipografia Arial/Garamond, numerazione, margini, overflow e collisioni sono conformi. Il blocker è strutturale: `nuclei: 0`, `indexNuclei: 0`, `verificationHeadings: 0`.

M-TR03 ha già superato copertura legacy, Humanizer, revisioni di capitolo, revisione trasversale e audit specialistico. Il retrofit deve preservare questa conoscenza e la tracciabilità, non rigenerare il volume da zero.

## Approccio approvato

Riaprire con il CLI gli step 08-15 interessati. Ogni capitolo viene trattato come unità autonoma e completa:

1. piano di completamento aggiornato;
2. snapshot tramite `next` prima della modifica;
3. conversione al formato 2;
4. copertura e densità;
5. Humanizer;
6. revisione editoriale totale;
7. verifica e chiusura dei gate.

Dopo i tredici capitoli si ripetono revisione trasversale, correzioni, audit specialistico, text freeze, audit immagini e fasi volume 19-23.

## Contratto del capitolo formato 2

Ogni capitolo deve:

- dichiarare `format_version: 2` e `dati_operativi: []` salvo dati realmente censiti;
- contenere almeno cinque nuclei con ID stabile `N-TR03-CC-NN`, dove `CC` è il numero capitolo e `NN` il progressivo;
- rendere ogni nucleo come heading riconoscibile dal Book Studio e dall'indice analitico;
- raggiungere almeno 600 parole per nucleo, salvo soglia più severa dichiarata dal prompt prodotto dal CLI;
- collocare una verifica vicino ai nuclei precedenti;
- includere almeno sei quiz commentati e un caso ragionato;
- mantenere obiettivo, Mappa BANDO, teoria, distinzioni, conseguenze, esempio, uso in prova ed errore tipico;
- conservare source refs e riferimenti normativi leggibili;
- non esporre dipendenze interne del wiki al lettore;
- usare rinvii soltanto verso destinazioni precise, complete e verificate.

## Strategia editoriale

La conversione è conservativa. Il testo esistente viene prima mappato sui nuclei; si spostano sezioni senza alterarne il significato e si scrive contenuto nuovo soltanto quando una dimensione didattica manca davvero. Non si gonfiano nuclei con ripetizioni per raggiungere una soglia.

Ogni nucleo copre, quando pertinente: definizione, funzione, quadro, elementi, distinzioni, conseguenze, caso o esempio, uso concorsuale, errore e controllo dell'apprendimento. La matrice viene aggiornata sulla base del contenuto reale.

## Grafo dei nuclei

Gli ID seguono la sequenza del capitolo e non vengono riutilizzati altrove. Il Book Studio deve mostrare lo stesso insieme non vuoto nel testo e nell'indice analitico. I blocchi `▣ Verifica` devono essere riconosciuti dal renderer e non spezzarsi in modo ambiguo.

La progressione resta quella della Bibbia del Volume:

1. profili e ufficio tecnico;
2. costruzioni, territorio ed edilizia;
3. ciclo tecnico dell'opera pubblica;
4. infrastrutture e patrimonio digitale;
5. laboratorio integrato.

## Riapertura e stato

Il run-state non viene modificato a mano. La versione corrente del CLI non espone `reopen`: il primo intervento implementa quindi un comando testato `pipeline reopen`, seguendo il modello già progettato per VOL-08. Il comando deve riaprire un intervallo dichiarato di step e invalidare deterministicamente gli step dipendenti senza alterare target estranei. Solo dopo il passaggio dei test il comando viene usato su VOL-10.

Lo snapshot di ogni capitolo deve essere creato prima della modifica dello step 09. Ogni modifica sostanziale successiva al nuovo freeze riapre nuovamente 10-15.

## Verifica

Per ogni capitolo:

- gate step 09 `chapter-lint`;
- gate step 10 copertura, densità e rinvii;
- gate step 11 `citation-guard`;
- report step 12 nel template fisso;
- controllo di ID, verifiche, quiz, casi, source refs e autonomia del lettore;
- `git diff --check` sui file interessati.

Per il modulo e il volume:

- revisione trasversale e specialistica con zero errori gravi o medi aperti;
- manifest di freeze con nuovi SHA-256;
- Book Studio con 13 capitoli, nuclei non nulli, `nuclei === indexNuclei`, verifiche non nulle, zero overflow e collisioni;
- audit pagina per pagina;
- typecheck e suite pipeline/editoriale;
- preflight e pacchetto di consegna agli step 21-23.

## Gestione degli errori

Un gate fallito arresta il lavoro sul target. La correzione avviene nello stesso step e il gate viene ripetuto. Non si usa `--accept` per gate automatici falliti. `--accept --note` è ammesso soltanto per verifiche manuali effettivamente eseguite e documentate.

Claim normativi o tecnici non sostenuti vengono corretti o rimossi; non sono trasformati in rinvii a futura revisione umana. I limiti d'uso professionale restano distinti dalle lacune didattiche.

## Fuori perimetro

- Nessun redesign generale del Book Studio.
- Nessuna immagine decorativa.
- Nessuna modifica ai volumi concorrenti.
- Nessun commit o push cumulativo di modifiche estranee già presenti nel worktree.
- Nessuna chiusura automatica dello step 24.

## Criteri di accettazione

- Tutti i tredici capitoli sono formato 2 e superano i gate 08-12.
- La matrice non contiene nuclei `parziale`, `solo-nominato` o `mancante`.
- Gli step 13-23 risultano completati con evidenze.
- Il Book Studio mostra nuclei e verifiche non nulli, pagine conformi e nessun difetto bloccante.
- Il run-state indica come unico passaggio residuo la conferma umana dello step 24.
