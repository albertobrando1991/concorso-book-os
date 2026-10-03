# VOL-11 — Controllo visivo del PDF, 2 ottobre 2026

PDF: `delivery/VOL-11/candidate/vol-11-interior-kdp.pdf`. 225 pagine; SHA-256 `83f89a8ac7c9bc950cdd6a7df79526a97dea3641c7a34cc8314da8e5c7f8bdcf`. Hash coincidente con l’inventario: sì.

## Copertura e metodo

Scorse tutte le 225 pagine nelle 10 tavole panoramiche. La geometria generale mantiene margini e numerazione regolari alla scala osservata, ma le matrici con molte colonne sono faticose da leggere anche ingrandite. Il PDF termina con quiz e caso ulteriore a pagina 225; ricerca testuale e sommario non individuano appendici. A pagina 159 è visibile anche la formulazione sull’allerta rossa già trattata in V11-29, senza duplicarla fra i rilievi grafici.

Viste tutte le 10 tavole, 24 pagine per tavola salvo l’ultima. Ingrandite separatamente a scala 2 le pagine 6, 151, 159, 163, 188, 204, 206, 225. I numeri riportati sono le pagine fisiche del PDF, coincidenti con la numerazione visibile. Applicata la skill PDF per il controllo visivo.

## Rilievi

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P11-01 | pp. 188 e 206; anche 204 e 151 | Tabelle | grave | Le matrici a nove e undici colonne spezzano quasi ogni parola su più righe, anche DNSH e intestazioni: la ricostruzione dei rapporti fra requisiti ed evidenze diventa molto faticosa. Il corpo della tabella è circa 9,49 punti; il problema principale è la larghezza insufficiente delle colonne. | Convertire le righe in schede, dividere la matrice in due tabelle collegate oppure usare un layout più largo; preservare parole e sigle ed eseguire una prova di stampa. | Non applicato |
| P11-02 | pp. 163; anche 82 e 174 in panoramica | Apparati interni | medio | Il testo pubblico contiene ID di dato operativo, area dell’audit automatico e istruzione da ricontrollare al text freeze. Conferma V11-44. | Rimuovere dal prodotto commerciale le istruzioni interne e sostituirle con data di aggiornamento e riferimento ufficiale leggibili. | Non applicato |
| P11-03 | pp. 6–7 e chiusura 225 | Apparati mancanti | grave | Le appendici A–E previste dall’indice analitico non compaiono nel sommario né in coda al PDF. Conferma V11-42. | Produrre e includere le appendici operative oppure rivedere la promessa e collocare i nuclei necessari nei capitoli, aggiornando tutti i rimandi. | Non applicato |
| P11-04 | pp. 6–7 | Leggibilità | medio | L’indice usa testo di circa 6,75 punti, con etichette a 6,6 punti; la duplicazione Cap. 1 / Capitolo 01 consuma ulteriore spazio. | Semplificare le etichette, aumentare il corpo e distribuire l’indice su più pagine. | Non applicato |
| P11-05 | pp. 151 e altre tabelle | Continuità delle tabelle | medio | La matrice conclusiva del caso è spezzata in due blocchi sulla stessa pagina, con parole divise senza sillabazione nelle intestazioni. | Mantenere una struttura unitaria e rivedere larghezze e intestazioni prima del nuovo export. | Non applicato |

## Esito e limiti

Richiesto un nuovo export dopo le correzioni. Nessun PDF è stato modificato.

- Copertura panoramica di tutte le pagine per geometria e ritmo; non equivale alla lettura del testo minuto di ogni pagina rasterizzata.
- Lettura puntuale e controllo grafico ingrandito limitati alle pagine elencate; il testo originale completo è documentato nel rapporto separato.
- Nessuna prova cartacea, verifica cromatica, certificazione PDF/X o collaudo di tutti i link. Non controllate qui copertine e materiali commerciali esterni.
- Metriche automatiche di supporto: nessun oggetto testuale oltre il foglio, nessuna pagina bianca e nessun carattere sostitutivo segnalato nell’inventario; tali esiti non eliminano difetti semantici o di impaginazione.

Ledger di copertura: `artifacts/review-integrale-2026-10-02/PDF-VOL-11-ledger.json`. Le tavole esaminate e i dettagli sono conservati negli artefatti dell’audit.
