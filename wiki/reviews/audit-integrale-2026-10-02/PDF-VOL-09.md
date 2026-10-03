# VOL-09 — Controllo visivo del PDF, 2 ottobre 2026

PDF: `delivery/VOL-09/candidate/vol-09-interior-kdp.pdf`. 209 pagine; SHA-256 `0c1fca1dcf32fc27b4d37c198e69bb59723407df699e7f2af394fe78dcf1f676`. Hash coincidente con l’inventario: sì.

## Copertura e metodo

Scorse tutte le 209 pagine nelle 9 tavole panoramiche. Confermata la manifestazione grafica di difetti già individuati nei sorgenti. Il PDF termina a pagina 209 con la checklist del capitolo 14: le appendici A–E promesse nell’indice analitico non sono presenti. I rilievi P09-01, P09-02, P09-03 e P09-04 costituiscono riscontri PDF di rilievi testuali, da non sommare come problemi indipendenti.

Viste tutte le 9 tavole, 24 pagine per tavola salvo l’ultima. Ingrandite separatamente a scala 2 le pagine 11, 68, 85, 127, 168, 183, 209. I numeri riportati sono le pagine fisiche del PDF, coincidenti con la numerazione visibile. Applicata la skill PDF per il controllo visivo.

## Rilievi

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P09-01 | pp. 11 | Tabelle | grave | Dopo il titolo 1.2 Strumenti e applicazioni, le righe Progettazione, Affidamento, Esecuzione e successive sono stampate come un paragrafo con barre verticali, anziché come tabella. Conferma V09-01. | Riparare la struttura Markdown prima di esportare e verificare la continuità dell’intera tabella. | Non applicato |
| P09-02 | pp. 85, 127, 168 | Quiz e titoli | grave | A pagina 85 il titolo 6.3 Quiz 3 è inserito sotto QUIZ 2; a pagina 127 un titolo separa domanda e opzioni; a pagina 168 il titolo 12.3 divide le opzioni C e D. Conferma V09-02. | Spostare i titoli all’esterno delle unità domanda/opzioni/soluzione, rinumerare e ricontrollare sommario e flusso di lettura. | Non applicato |
| P09-03 | pp. 183 | Segnaposto editoriali | medio | Il codice provvisorio N-TR02-XX-04 è stampato sia nel titolo di sezione sia nel riquadro della verifica. Conferma V09-04. | Sostituire il segnaposto con un titolo destinato al lettore; mantenere i codici di audit nei soli metadati interni. | Non applicato |
| P09-04 | pp. 6–7 e chiusura 209 | Apparati mancanti | grave | Il sommario e la chiusura del PDF non contengono le cinque appendici A–E promesse dal progetto editoriale. Conferma il rilievo testuale sulle appendici. | Completare e includere le appendici, oppure riallocare i contenuti indispensabili e correggere coerentemente la promessa editoriale. | Non applicato |
| P09-05 | pp. 6–7 | Leggibilità | medio | L’indice completo è composto con testo inferiore a 7 punti, troppo fitto per una consultazione agevole nel formato stampato. | Aumentare il corpo, distribuire le voci e provare la leggibilità in dimensioni reali. | Non applicato |
| P09-06 | pp. 68 e 183 | Tabelle | medio | Tabelle brevi sono segmentate in più blocchi sulla stessa pagina, con spazi orizzontali fra gruppi di righe; la continuità visiva è indebolita. | Mantenere una tabella unitaria quando resta sulla stessa pagina; usare separazioni solo per gruppi semanticamente distinti. | Non applicato |

## Esito e limiti

Richiesto un nuovo export dopo le correzioni. Nessun PDF è stato modificato.

- Copertura panoramica di tutte le pagine per geometria e ritmo; non equivale alla lettura del testo minuto di ogni pagina rasterizzata.
- Lettura puntuale e controllo grafico ingrandito limitati alle pagine elencate; il testo originale completo è documentato nel rapporto separato.
- Nessuna prova cartacea, verifica cromatica, certificazione PDF/X o collaudo di tutti i link. Non controllate qui copertine e materiali commerciali esterni.
- Metriche automatiche di supporto: nessun oggetto testuale oltre il foglio, nessuna pagina bianca e nessun carattere sostitutivo segnalato nell’inventario; tali esiti non eliminano difetti semantici o di impaginazione.

Ledger di copertura: `artifacts/review-integrale-2026-10-02/PDF-VOL-09-ledger.json`. Le tavole esaminate e i dettagli sono conservati negli artefatti dell’audit.
