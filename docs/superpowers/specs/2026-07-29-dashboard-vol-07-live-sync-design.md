# Dashboard VOL-07 — sincronizzazione automatica della lista capitoli

## Contesto

La dashboard legge correttamente il vault del worktree corrente. L'endpoint `GET /api/book-studio?bookId=volumi/vol-07` restituisce il capitolo 01 M-SA02 e il riepilogo aggiornato, ma la lista visibile può rimanere ferma al payload precedente quando una navigazione Next.js fornisce nuovi dati per lo stesso `bookId`.

La causa è nello stato locale di `BookStudioPanel`: il componente inizializza `data` da `initialData`, ma l'effetto di sincronizzazione dipende soltanto da `initialData.bookId` e `initialChapterPath`. Se cambia il contenuto di `initialData` mentre `bookId` resta `volumi/vol-07`, l'effetto non viene eseguito e la lista conserva i capitoli precedenti.

## Obiettivo

Quando il server consegna un nuovo payload `BookStudioData` per il volume già aperto, lo Studio deve aggiornare automaticamente riepilogo, lista dei capitoli e anteprima senza richiedere il pulsante di refresh.

Il comportamento deve preservare il capitolo selezionato se il suo percorso esiste ancora nel nuovo payload. Se non esiste più, deve selezionare il primo capitolo disponibile.

## Non obiettivi

- Non aggiungere polling periodico.
- Non modificare l'API `book-studio`, che restituisce già dati corretti e usa `cache: no-store` nel workspace.
- Non forzare il rimontaggio completo del componente.
- Non cambiare la struttura editoriale o lo stato della pipeline VOL-07.
- Non introdurre un sistema globale di stato client.

## Approcci considerati

### 1. Sincronizzare il payload aggiornato — scelto

Il componente reagisce alle variazioni effettive di `initialData`, aggiorna lo stato locale e riconcilia la selezione.

Vantaggi:

- corregge la causa nel punto in cui nasce;
- conserva la vista e il capitolo aperto;
- non genera richieste aggiuntive;
- mantiene il comportamento del pulsante di refresh.

### 2. Forzare il rimontaggio con una `key` — scartato

Il parent potrebbe assegnare una chiave derivata dal payload. Questo aggiornerebbe la lista, ma azzererebbe anche vista, messaggi e selezione, introducendo un effetto più ampio del necessario.

### 3. Polling dell'API — scartato

Aggiornerebbe il volume anche senza navigazione, ma produrrebbe richieste ricorrenti e non serve al caso osservato, nel quale il server ha già fornito il payload corretto.

## Disegno

### Sincronizzazione dello Studio

`BookStudioPanel` deve applicare il nuovo `initialData` ogni volta che il prop cambia, non soltanto quando cambia `bookId`.

Durante la sincronizzazione:

1. sostituisce lo stato locale `data` con il nuovo payload;
2. usa `initialChapterPath` se è esplicitamente richiesto ed esiste;
3. in assenza di un percorso esplicito valido, mantiene `selectedPath` se quel percorso è presente nei nuovi capitoli;
4. altrimenti seleziona il primo capitolo disponibile;
5. azzera soltanto gli stati derivati dall'anteprima precedente che non sono più validi, come la paginazione misurata.

La riconciliazione della selezione deve essere estratta in una funzione pura per poter essere verificata senza montare l'intera dashboard.

### Altri pannelli

`ManualWriterPanel` riceve già `initialChapters` aggiornati e dispone di un effetto dipendente dal relativo array. Non richiede modifiche per questo bug.

`EditorialReviewerPanel` non determina la lista principale dello Studio. La sua selezione locale non rientra nel difetto segnalato e non viene modificata in questo intervento.

## Flusso dati atteso

1. Il server legge `wiki/` dal worktree corrente.
2. `buildBookStudioData` costruisce il volume aggregato.
3. `EssentialEditorialWorkspace` riceve il payload aggiornato dall'API o dalla navigazione server.
4. `BookStudioPanel` riconosce la variazione di `initialData` anche a `bookId` invariato.
5. La lista visualizza immediatamente i nuovi capitoli e conserva, quando possibile, la selezione corrente.

## Gestione degli errori

La modifica non introduce nuove operazioni asincrone. Restano valide le gestioni esistenti per errori API e refresh manuale. Un payload senza capitoli produce una selezione vuota senza eccezioni.

## Strategia di test

Il test di regressione copre la funzione pura di riconciliazione:

- stesso `bookId`, lista precedente senza capitolo 01 e lista successiva con capitolo 01: il nuovo payload deve essere considerato e la selezione valida deve essere preservata;
- percorso selezionato assente nel nuovo payload: viene scelto il primo capitolo;
- `initialChapterPath` valido: ha precedenza sulla selezione precedente;
- lista vuota: restituisce stringa vuota.

Il ciclo TDD deve mostrare il test rosso prima della modifica del componente, poi verde dopo l'implementazione minima. La verifica finale comprende test mirato, suite completa, typecheck e risposta dell'API VOL-07 contenente il capitolo aggiornato.

## Criteri di accettazione

- Aprendo nuovamente VOL-07, la lista dello Studio riflette il payload più recente anche se il `bookId` non cambia.
- Il capitolo attualmente selezionato resta aperto quando esiste ancora.
- Un percorso non più presente non lascia la UI in uno stato incoerente.
- Il pulsante di refresh continua a funzionare.
- Nessun polling e nessun rimontaggio forzato vengono introdotti.
- Test e typecheck passano senza regressioni.
