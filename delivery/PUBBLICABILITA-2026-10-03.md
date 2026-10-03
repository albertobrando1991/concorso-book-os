# Chiusura tecnica della collana — 3 ottobre 2026

**Precisazione successiva dell'utente: destinazione prioritaria digitale sul sito.** Questo documento conserva gli esiti della lavorazione PDF/stampa; i requisiti KDP e la prova fisica non sono il criterio di pubblicabilità dell'edizione online. Per il percorso digitale effettivo vedere il [rapporto dedicato](../wiki/reviews/correzioni-collana-2026-10-02/DIGITALE.md), che distingue capitoli online e PDF scaricabili.

I dodici pacchetti contengono tredici interni corretti e tredici copertine complete, una per ciascun interno. **La pubblicabilità complessiva resta aperta per i dati editoriali, le condizioni digitali e le verifiche finali del canale e della copia fisica.** Nessuna pubblicazione o conferma conclusiva è stata eseguita.

- [Indice dei pacchetti correnti](COLLANA-REVISIONATA-2026-10-03.md).
- [Copertine, misure e specifiche](copertine-2026-10-03/README.md); [panorama della collana](copertine-2026-10-03/copertine-collana-panorama.pdf).
- [Schede in scala reale per la prova a penna](prova-compilazione-2026-10-03/README.md).

## Lavoro completato

| Ambito | Risultato verificato |
|---|---|
| Revisione precedente | 582 rilievi originari riconciliati: 577 verificati, 4 parziali, 1 facoltativo aperto. Restano separati i 13 rilievi aggiuntivi precedenti. |
| Copertine | 13 PDF di quarta, dorso e prima, per carta bianca e stampa in nero, formato 6,69 × 9,61 in. Controllo visivo completo, font incorporati, colori CMYK, margine del testo sul dorso almeno 4,5 pt. Area barcode riservata, nessun ISBN inventato. |
| Volume 1 | 19 figure portate ad almeno 300 ppi attraverso la dimensione di collocazione, senza interpolazione. Conservate 686 pagine; verificati testo, 25 pagine modificate e tutte le 437 destinazioni dell'indice. Le altre 661 pagine sono identiche nel rendering alla versione precedente. La normalizzazione delle pp. 51–52 conserva le pagine già verificate ed evita un titolo orfano. |
| Volume 6 | «Università» corretto nel catalogo e nelle sette pagine interessate. Altre 610 pagine identiche nel rendering. |
| Volume 9 | Gantt di p. 240 rigenerato dal PDF vettoriale a oltre 370 ppi effettivi; dati conservati, altre 266 pagine identiche nel rendering. |
| Volume 10 | Fotografia di p. 123 collocata leggermente più piccola per raggiungere almeno 300 ppi senza ricampionamento; altre 126 pagine identiche nel rendering. |
| Tutti gli interni | Nessun font non incorporato, testo fuori pagina, protezione o immagine sotto 300 ppi nei 13 PDF correnti. Questo controllo non sostituisce il Print Previewer. |
| Integrità | 2.580 file verificati nei dodici pacchetti; zero hash o dimensioni difformi. |
| Schede del volume 12 | Estratto delle pp. 127–128 pronto per la stampa al 100%, identico alla fonte per testo, geometria e rendering; istruzioni per documentare la prova. La prova fisica non è stata simulata. |

Le quattro rifiniture degli interni e la creazione delle copertine sono documentate separatamente: non aumentano artificialmente il numero dei 582 rilievi iniziali risolti.

## Informazioni necessarie per chiudere i preliminari

1. Nome effettivo dell'autore o curatore e dati editoriali da riportare; recapito reale per assistenza ed errata.
2. Scelta tra ISBN propri e assegnazione KDP, con gli eventuali identificativi disponibili. Il volume 2 ha due tomi e richiede metadati distinti.
3. Condizioni delle risorse digitali: libro autonomo con eventuali servizi separati, oppure servizi inclusi con URL, attivazione, durata e materiali effettivamente disponibili. Nei file attuali rimangono promesse da risolvere; non possono essere dichiarate verificate senza riscontro.

Le domande sono state presentate all'editore e non hanno ancora ricevuto risposta. L'assenza di risposta non vale come scelta commerciale o conferma dei dati. Ricevuti questi elementi, occorre aggiornare i master e le proiezioni, rigenerare gli interni interessati, ricontrollare indici e paginazione e riallineare eventuali dorsi modificati.

## Verifiche successive

Restano il collaudo nel canale scelto, la verifica della copia fisica e la compilazione a penna delle schede. P12-07, relativo al bianco di p. 129, è una rifinitura facoltativa; non è un blocco alla pubblicazione. I gate della pipeline non sono stati forzati: lo step 22 di Giustizia mantiene i limiti già documentati, e nessuno step 24 è dichiarato concluso.

Il typecheck è stato ripetuto dopo la correzione del catalogo ed è superato. Gli altri controlli software già eseguiti sono descritti nel [rapporto di preflight di Giustizia](VOL-04/candidate-2026-10-03/reports/22-vol-04.md), che conserva anche gli esiti non superati e le limitazioni; build e test precedenti non sono presentati come nuove esecuzioni. Le verifiche editoriali e normative rimangono riferite alle fonti e al cut-off documentati.

## Evidenze correnti

- [Integrità dei dodici pacchetti](../artifacts/correzioni-collana-2026-10-02/registro-package-verification.json).
- [Proprietà tecniche dei tredici interni](../artifacts/correzioni-collana-2026-10-02/publication-pdf-preflight.json).
- [Manifest delle copertine e associazioni agli interni](../artifacts/correzioni-collana-2026-10-02/cover-qa/cover-manifest.json).
- [Verifica della riconciliazione dei rilievi](../artifacts/correzioni-collana-2026-10-02/registro-consolidato-verification.json).

I quattro pacchetti aggiornati includono `publication-refinements/` con payload, helper e confronti visivi. Usare i comandi di riproduzione specifici: l'export generico dell'API non equivale ai PDF controllati. Il server temporaneo sulla porta 3021 è stato arrestato dopo gli export; per riprodurli va avviato come indicato negli helper, con una cartella Next isolata.
