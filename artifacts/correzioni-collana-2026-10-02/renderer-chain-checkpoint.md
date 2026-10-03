# Impaginazione — catene di apertura, 3 ottobre 2026

Il PDF del VOL-01 mostrava 20 schemi con titolo e breve descrizione nella pagina precedente alla tabella o alla sequenza. La misurazione e il fallback riservavano soltanto una coppia di blocchi; i successivi controlli potevano separare di nuovo titolo, introduzione e apparato. Il recupero dello spazio poteva riportare indietro la sola introduzione.

Tre regressioni hanno riprodotto il problema prima della modifica. La correzione centralizza le catene in `src/book/pagination.ts`: titolo, fino a tre paragrafi brevi (48 parole ciascuno e 72 complessive), primo blocco strutturato. I frammenti continuati restano separabili. Se il gruppo supera la capacità di una pagina, il vincolo viene allentato: non si forza un overflow. La riserva iniziale, il controllo dell'overflow e il recupero dello spazio usano questa struttura. Il corpo del codice passa da 11 px (8,25 pt) a 9,5 pt.

Verifiche eseguite:

- `npm test -- tests/book-studio tests/book-preview`: 21 file, 127 test superati, inclusi indice, continuazioni e otto test delle nuove catene.
- `npm run typecheck`: superato dopo che il proprietario del pacchetto VOL-02 ha corretto un import nel suo script di riproduzione.
- `git diff --check` sui file del renderer: nessun errore di whitespace.

La prova release `vol-01-native-release-20261003-proof.pdf` conta 687 pagine sia nel DOM sia nel PDF: zero overflow e testo fuori pagina. Tutti i 133 schemi iniziano con titolo e primo contenuto nella stessa pagina; i 20 raccordi segnalati e i cinque aggiuntivi sono risolti. Il registro visivo distingue confronto esatto del rendering e ispezione diretta. Le prove precedenti restano immutate. Nessun gate 24 eseguito.
