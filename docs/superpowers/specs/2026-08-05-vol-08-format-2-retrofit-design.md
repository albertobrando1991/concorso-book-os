# VOL-08 Format 2 Retrofit Design

## Stato e obiettivo

VOL-08 contiene M-TR01 con 13 capitoli editorialmente congelati in formato legacy. Il Book Studio applica correttamente il master KDP a 139 pagine, ma rileva zero Nucleo ID, zero voci di indice analitico per nucleo e zero heading `▣ Verifica`. L'obiettivo è portare il volume allo stato tecnico `ready_for_human_signoff`, lasciando obbligatoriamente pendente lo step umano 24.

Il retrofit deve rispettare il CLI come unica autorità sul run-state, preservare il testo umano valido, usare soltanto conoscenza consolidata nel wiki e rieseguire tutti i gate impattati. Nessuna deroga legacy e nessuna modifica manuale a `pipeline/VOL-08/run-state.json` sono ammesse.

## Scelta architetturale

L'intervento usa due livelli separati:

1. aggiungere al CLI una riapertura esplicita, testata e tracciabile degli step già terminali;
2. convertire M-TR01 capitolo per capitolo al formato 2, poi rieseguire le fasi di modulo e volume.

La riapertura non modifica i contenuti editoriali. Il retrofit editoriale non modifica il motore della pipeline. Questa separazione consente di verificare e, se necessario, respingere ciascun livello indipendentemente.

## Comando CLI di riapertura

Il CLI espone:

```text
npm run pipeline -- reopen VOL-08 --step 08 --module M-TR01 --cascade --note "Retrofit formato 2 autorizzato dall'utente"
```

Regole:

- `--step` è obbligatorio e indica il primo step da riaprire;
- `--module` o `--chapter` restringono il primo perimetro quando necessario;
- `--cascade` riporta a `pending` tutti gli step dipendenti e successivi del volume, seguendo l'ordine reale del run-state;
- `--note` è obbligatorio e viene conservato nelle evidenze dello step riaperto;
- il comando rifiuta una riapertura senza cascata se esistono step terminali a valle che dipendono dal target;
- lo step 24 non può essere impostato a `done` dal comando;
- owner, agent, provider, timestamp di esecuzione e gate precedenti vengono rimossi dagli step riaperti, mentre la motivazione resta tracciata;
- l'output `--json` elenca esattamente chiavi precedenti e nuove, senza dedurre il successo dal testo formattato;
- nessun altro volume o modulo viene modificato.

La funzione di dominio produce un nuovo `RunState` immutabile. I test coprono selezione, cascata, isolamento del volume, rifiuto delle richieste ambigue e impossibilità di completare automaticamente lo step 24.

## Perimetro editoriale del retrofit

Ogni capitolo dichiarato nella scheda VOL-08 viene lavorato attraverso gli step 08-12 del CLI. Prima di modificare un capitolo, `next` deve aprire il relativo step e generare il contratto con soglie effettive.

Per ciascun capitolo:

- il frontmatter dichiara `format_version: 2`;
- la matrice assegna ogni riga a un Nucleo ID stabile `N-TR01-CC-NN`;
- il testo contiene almeno cinque nuclei numerati, salvo una soglia più alta nel contratto;
- ogni nucleo raggiunge la soglia di parole esposta dal CLI e copre definizione, funzione, elementi, distinzioni, conseguenze, applicazione, modalità d'esame, errore e verifica quando pertinenti;
- almeno un blocco `▣ Verifica` compare ogni 5-7 nuclei;
- il capitolo contiene almeno sei quiz commentati e un caso ragionato, o le soglie superiori dichiarate dal contratto;
- i rinvii a VOL-01 hanno file e heading esistenti;
- il corpo non espone wikilink o riferimenti a source note, planning e review;
- le fonti restano nel frontmatter e negli artefatti interni;
- il contenuto umano valido viene riorganizzato e ampliato, non sostituito senza traccia.

La conversione segue l'ordine 01-13 della scheda. Il capitolo 13 resta il laboratorio conclusivo e viene allineato dopo la stabilizzazione dei nuclei 01-12.

## Matrice e indice analitico

`planning/02-matrice-copertura-didattica.md` di M-TR01 diventa la chiave di riconciliazione. Ogni promessa formativa deve avere collocazione, Nucleo ID, teoria, applicazione, output, verifica, fonti, stato e review normativa.

Lo stato `completo` è ammesso soltanto quando il nucleo è autosufficiente. `parziale`, `solo-nominato` e `mancante` impediscono il passaggio; `rinviato` richiede una destinazione precisa, esistente e completa.

Il Book Studio deriva i numeri decimali dai Nucleo ID e deve mostrare lo stesso insieme di nuclei nel testo e nell'indice analitico. Non viene introdotta numerazione sintetica nel renderer.

## Riesecuzione dei gate

Dopo ogni conversione:

1. step 10: copertura, dimensioni didattiche, densità dei nuclei e rinvii;
2. step 11: Humanizer, aperto prima della modifica per conservare lo snapshot;
3. step 12: Revisore Editoriale Totale sul capitolo.

Dopo i 13 capitoli:

1. step 13: revisione trasversale del modulo;
2. step 14: applicazione delle correzioni;
3. step 15: audit specialistico automatico ICT, cyber, cloud, dati/AI, procurement e privacy;
4. step 16: nuovo text freeze;
5. step 17-18: riconferma della filosofia e audit immagini;
6. step 19: nuova impaginazione KDP;
7. step 20: audit pagina per pagina;
8. step 21: revisione finale del volume;
9. step 22: preflight;
10. step 23: pacchetto di consegna.

Lo step 24 resta `awaiting-human` o `pending` e non viene accettato automaticamente.

## Sicurezza editoriale e concorrenza

Il lavoro avviene sul branch operativo esistente senza includere modifiche concorrenti di VOL-03 o della memoria in commit editoriali. Ogni commit usa path espliciti. Prima di integrazioni o commit si controllano `git status`, diff per path e `git diff --check`.

Le fonti mobili restano vincolate al cut-off registrato. Se un nucleo richiede un aggiornamento non consolidato, il capitolo non viene dichiarato completo: si crea prima la source note ufficiale o si registra un blocker.

## Verifica e criteri di successo

Il risultato tecnico è accettabile soltanto se:

- tutti i gate automatici 08-23 interessati risultano passati nel run-state;
- 13 capitoli dichiarano formato 2 e rispettano le soglie CLI;
- matrice e capitoli contengono lo stesso insieme di Nucleo ID;
- Book Studio mostra nuclei nel testo e nell'indice analitico in quantità uguale e maggiore di zero;
- i blocchi `▣ Verifica` sono riconosciuti e non presentano spezzature ambigue;
- il layout KDP ha numerazione progressiva, zero overflow, zero collisioni e nessun asset mancante;
- Revisore Editoriale Totale e audit specialistico non lasciano blocker;
- il preflight e il pacchetto di consegna sono completi;
- lo stato finale è `ready_for_human_signoff`, con step 24 ancora non completato.

## Gestione degli errori

Un gate fallito arresta la lavorazione sullo stesso target. Si corregge il difetto e si ripete il gate; non si avanza e non si usa `--accept` per gate implementati. Un conflitto Git sullo stesso step richiede confronto dei due blocchi, mai scelta cieca. Un errore normativo o una fonte non verificabile resta blocker fino alla consolidazione.

## Esclusioni

- Nessuna revisione umana simulata o eliminata.
- Nessuna pubblicazione o push automatico.
- Nessuna riscrittura dei capitoli da fonti raw.
- Nessuna numerazione fittizia generata dal renderer.
- Nessuna modifica di contenuti o run-state di altri volumi.
- Nessun completamento dello step 24.
