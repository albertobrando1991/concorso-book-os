# Dashboard Volume Default Preview Design

## Problema

I volumi compositi espongono per primi i front matter generati. `BookStudioPanel` usa attualmente `chapters[0]` come selezione iniziale, quindi VOL-07 e gli altri volumi si aprono sulla pagina generica `Servizi digitali inclusi`. La lista può essere aggiornata correttamente mentre l'anteprima iniziale continua a sembrare identica.

## Comportamento approvato

Quando non è richiesto esplicitamente un `chapterPath`, lo Studio seleziona nell'ordine:

1. il primo capitolo non generato con stato editoriale diverso da `structure`;
2. il primo capitolo non generato;
3. il primo elemento disponibile, incluso il front matter generato;
4. stringa vuota se non esistono capitoli.

Un `chapterPath` esplicito e valido mantiene sempre la precedenza. Dopo l'apertura, la selezione manuale e la riconciliazione dei refresh continuano a preservare il capitolo corrente quando è ancora valido.

Per VOL-07 il risultato atteso è `Professioni sanitarie: profili, requisiti e prove`.

## Architettura

La scelta predefinita viene estratta in una funzione pura dentro `app/components/book-studio-state.ts`. `BookStudioPanel` usa la funzione esclusivamente per lo stato iniziale; non cambiano API, ordinamento dei capitoli, front matter, routing o pipeline.

## Verifica

Il test deve dimostrare prima il difetto e poi il nuovo comportamento con un payload simile a VOL-07:

- front matter generato in prima posizione;
- capitolo strutturale non generato;
- capitolo editoriale reale non generato;
- selezione attesa sul capitolo editoriale reale.

Sono inoltre verificati il percorso esplicito valido e i fallback. La consegna richiede test mirato, suite completa, typecheck e controllo del record VOL-07 restituito dall'API.

## Vincoli

- Nessun polling o rimontaggio forzato.
- Nessuna modifica all'API o alla pipeline VOL-07.
- Nessuna nuova dipendenza.
- Nessun commit: i commit restano riservati allo step 23 della pipeline.
