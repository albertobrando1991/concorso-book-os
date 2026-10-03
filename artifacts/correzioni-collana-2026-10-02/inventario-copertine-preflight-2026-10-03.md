# Copertine, preflight e consegna: inventario del 3 ottobre 2026

Ricognizione in sola lettura degli asset e dei requisiti. Non sono stati modificati copertine, master, renderer, API o stati della pipeline. Non sono stati effettuati staging, caricamenti su KDP, ordini o pubblicazioni. I pacchetti locali dei volumi 6, 7 e 12 conservano i PDF già verificati.

## Esito concreto

Nel repository è stata individuata una sola copertina completa della collana: `delivery/VOL-04/candidate/vol-04-cover-kdp.pdf`. È il candidato storico, dimensionato per 303 pagine fisiche e 304 pagine KDP. Non è una copertina finale valida per il nuovo interno corretto del volume 4. Non sono state trovate copertine finali associate agli altri candidati correnti. Il volume 2 dispone di due interni distinti: occorrono due confezioni coerenti con i rispettivi tomi.

| Volume | Copertina completa trovata | Stato per il candidato corrente |
| --- | --- | --- |
| VOL-01 | Nessuna | Da produrre dopo stabilizzazione di pagine e dati editoriali |
| VOL-02, tomo I | Nessuna | Da produrre con dati e dorso propri |
| VOL-02, tomo II | Nessuna | Da produrre con dati e dorso propri |
| VOL-03 | Nessuna | Da produrre |
| VOL-04 | PDF storico per 303/304 pagine | Da riallineare al nuovo interno; non riutilizzabile come file finale senza ricalcolo e controllo |
| VOL-05 | Nessuna | Da produrre |
| VOL-06 | Nessuna | Da produrre; il pacchetto corrente contiene l'interno di 617 pagine |
| VOL-07 | Nessuna | Da produrre; il pacchetto corrente contiene l'interno di 456 pagine |
| VOL-08 | Nessuna | Da produrre; il nome citato nella vecchia checklist non corrisponde a un asset presente |
| VOL-09 | Nessuna | Da produrre |
| VOL-10 | Nessuna | Da produrre |
| VOL-11 | Nessuna | Da produrre |
| VOL-12 | Nessuna | Da produrre; il pacchetto corrente contiene l'interno di 492 pagine |

I conteggi degli interni sono uno snapshot di lavorazione, non i parametri definitivi di un ordine. Eventuali correzioni dei preliminari possono cambiare le pagine e richiedere un nuovo dorso. Questa ricognizione non sceglie autore, ISBN, prezzo o variante grafica.

## Asset esistente e materiali esclusi

Il PDF storico VOL-04 è stato aperto, estratto e renderizzato per ispezione visiva. Contiene quarta, dorso e prima in una pagina, con titolo «Giustizia e Ufficio per il processo», marchio Capitale Personale e area chiara destinata al codice a barre. La tavola misura circa 1030,652 × 709,920 pt, pari a 14,314608 × 9,86 in. La specifica allegata dichiara formato di taglio 6,69 × 9,61 in, nero su carta bianca, abbondanza esterna di 0,125 in e dorso di 0,684608 in. La resa a schermo non certifica taglio, colore o rilegatura reali.

- SHA-256 del PDF: `4f0ca664dc62b5eeb0001db2a428111b8e1b8ff284b2d9b6c4e905d80b7cdb42`.
- Specifica: `delivery/VOL-04/candidate/COVER-SPEC.md`.
- Metadati storici: `delivery/VOL-04/candidate/METADATA-KDP.md`, con autore, ISBN, diritti e altre scelte ancora da confermare.
- Immagine di sola ispezione: `artifacts/correzioni-collana-2026-10-02/VOL-04-old-cover-inventory.png`; non è un nuovo asset di stampa.

`artifacts/Capitale-Personale-Design-System-Copertine-Blue-Navi.md` e `artifacts/Capitale-Personale-Design-System-Copertine-Carta-Antica.md` dichiarano `status: draft`, `canonical: false`, `review_required: true`, aggiornamento 28 maggio 2026. Descrivono una precedente architettura di libro base e moduli M1–M24: sono indicazioni progettuali, non 12 copertine pronte. Non si sceglie automaticamente fra le due varianti.

`tmp/study-plan-final-cover.png`, ispezionato visivamente, mostra «DEMO — Pacchetto del metodo Capitale Personale», «Il tuo piano personale di studio», con indicazioni di dimostrazione e bozza. È la prima pagina di un piano di studio dimostrativo, non una copertina completa della collana.

## Quale requisito appartiene a quale fase

La distinzione seguente deriva dai prompt canonici 21–24 in `wiki/templates/prompt-staff-revisione-completa-volumi.md`, non introduce nuovi gate.

| Fase | Verifica effettiva | Conseguenza operativa |
| --- | --- | --- |
| 21 — Revisione dell'impaginato | Contenuti e 30 controlli, copertura v4, rinvii, fonti e cut-off, audit specialistici, immagini, impaginazione, indice/pagine; nessun errore grave | Promesse digitali non dimostrate o dati editoriali inesatti nel PDF sono rilievi reali. La sola assenza della copertina commerciale non deve diventare un errore grave del manoscritto |
| 22 — Preflight | Copertura, link, source_refs, frontmatter, asset, file mancanti, duplicati, tabelle, caratteri, diff, test pertinenti, typecheck, build, export, font, dimensioni, bleed, margini, pagine ed eventuali warning Previewer | Registrare comando, versione, esito e limiti. Un vecchio PASS non vale per un PDF rigenerato; un controllo non eseguito non diventa PASS |
| 23 — Consegna | Verifica remoto/staff, selezione dei soli file pertinenti, staging selettivo e controllo diff cached, nuovi gate tecnici, versione, cut-off, rapporto, manifest, changelog, limiti e manutenzione | Il candidato deve essere completo e riproducibile prima della conferma finale. Per una consegna KDP comprensiva di stampa, associare interno, copertina, specifica del dorso e metadati effettivi. L'associazione è una necessità del canale, non una voce testuale aggiunta al prompt 21 |
| 24 — Conferma umana | Conferma o rifiuto del pacchetto già completo | Non rinviare a questo passaggio scrittura, riparazione di quiz, copertina da creare o preflight ancora da svolgere |

Le cartelle `candidate-2026-10-03` sono consegne locali revisionabili e non attestano, per il solo nome, il superamento dello step 23. Nessuno stato è stato avanzato da questo inventario. L'autorizzazione alla pubblicazione resta distinta dal caricamento di una bozza o dall'acquisto di una copia di prova.

## Requisiti del canale KDP verificati

La copertina caricata come file deve essere un PDF unico comprendente quarta, dorso e prima. Formato, carta e pagine determinano la misura del dorso; la copertina richiede abbondanza anche se l'interno è senza bleed. Vanno controllati zone di sicurezza, corrispondenza dei dati editoriali, font incorporati e assenza di protezioni o segni tecnici. Per i valori finali utilizzare il generatore ufficiale con i parametri dell'edizione effettiva. [KDP — Create a Paperback Cover](https://kdp.amazon.com/en_US/help/topic/G201953020), consultato il 3 ottobre 2026.

Print Previewer per il cartaceo si avvia nella procedura online KDP, dopo il caricamento dei contenuti. Controlla errori prima dell'invio alla pubblicazione; non è l'applicazione locale Kindle Previewer per eBook. Le formule storiche «KDP Previewer non installato» o «comando locale non disponibile» non descrivono correttamente la dipendenza: serve accesso alla bozza KDP e un caricamento autorizzato. [KDP — Upload and Preview Book Content](https://kdp.amazon.com/en_US/help/topic/G200641240), sezione Paperback and Hardcover, consultato il 3 ottobre 2026.

La copia di prova si può ordinare con il libro in stato Draft dopo l'approvazione in Print Previewer. Non occorre pubblicare il libro per provarlo fisicamente. L'ordine costituisce un acquisto distinto e non è stato effettuato. [KDP — How do I order a proof or author copy?](https://kdp.amazon.com/en_US/help/topic/GVEG4YA9G2T7N6DR), consultato il 3 ottobre 2026.

Nei fascicoli esaminati non sono presenti esiti documentati di upload/Print Previewer o prove fisiche dei nuovi candidati. Le checklist storiche riportano caselle non spuntate. Questo non prova che un account o un ordine esterno non esistano: tali ambienti non sono stati aperti. La verifica fisica dovrà includere leggibilità, margini interni, dorso/taglio, contrasto, figure e compilabilità a penna dei worksheet; in VOL-12 il rilievo P12-04 resta quindi parzialmente verificato.

## Dati da consolidare per la consegna finale

Per ciascuna edizione o tomo servono un riferimento univoco a interno e copertina, conteggio finale, carta e formato; titolo/sottotitolo, autore o contributori effettivi, numero del volume/tomo ed edizione; scelta ISBN, diritti e territori; descrizione dello store, categorie, parole chiave, mercato, prezzo e finitura; esiti tecnici e, quando svolti, Previewer e prova fisica collegati agli stessi hash. L'inventario non trasforma valori candidati del 2026 precedente in decisioni definitive.

Per i volumi 6, 7 e 12 le promesse digitali e i dati dei preliminari rimangono aperti nei rapporti correnti. Le copertine assenti e la prova fisica sono dipendenze ulteriori della produzione, tenute separate dai rilievi testuali e dai gate già eseguiti.

## Metodo e limiti della ricognizione

Ricerca dei nomi con `rg --files`, ripetuta con `--hidden --no-ignore`, escludendo dipendenze e Git; filtro per cover/copertina/dorso e PDF, PNG, JPG/JPEG, SVG, PSD, AI, INDD. Esaminati i pacchetti `delivery`, i metadati, le specifiche e le checklist pertinenti; cercati i riferimenti alla prova nel materiale di consegna. Sono state ispezionate le due immagini candidate rilevate, distinguendo la demo dal PDF di copertina. Non sono stati aperti account remoti, drive esterni o tutti i bitmap dal nome privo di qualsiasi riferimento alla copertina. «Nessuna trovata» significa assenza di asset identificato e associato all'edizione nel perimetro locale ricercato, non prova assoluta dell'inesistenza su altri dispositivi.

I report e i preflight storici in `delivery/VOL-XX/candidate/` restano conservati. I loro conteggi, calcoli del dorso e affermazioni di PASS non vanno trasferiti automaticamente ai candidati del 3 ottobre 2026. Nessun asset o documento storico è stato alterato per questa ricognizione.
