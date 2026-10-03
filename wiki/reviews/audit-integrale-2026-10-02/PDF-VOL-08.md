# VOL-08 — Controllo visivo del PDF, 2 ottobre 2026

PDF: `delivery/VOL-08/candidate/vol-08-interior-kdp.pdf`. 231 pagine; SHA-256 `78c20cd78374432a0a9d7b9f64b33325eb670def84d68a0724d697955697daea`. Hash coincidente con l’inventario: sì.

## Copertura e metodo

Scorse tutte le 231 pagine nelle 10 tavole panoramiche. Margini, testatine e numerazione risultano regolari alla scala osservata. Gli esempi SQL ingranditi a pagina 63 mantengono indentazione e simboli leggibili. Il capitolo finale termina con le avvertenze a pagina 231; non è una pagina bianca tecnica.

Viste tutte le 10 tavole, 24 pagine per tavola salvo l’ultima. Ingrandite separatamente a scala 2 le pagine 6, 63, 157, 211, 223, 231. I numeri riportati sono le pagine fisiche del PDF, coincidenti con la numerazione visibile. Applicata la skill PDF per il controllo visivo.

## Rilievi

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P08-01 | pp. 6–7 | Leggibilità | medio | L’indice completo usa testo di circa 6,75 punti, con etichette anche a 6,6 punti: è molto fitto per la consultazione su carta. | Aumentare il corpo e distribuire l’indice su più pagine; verificare una prova in dimensioni reali. | Non applicato |
| P08-02 | pp. 157 | Tabelle | medio | La timeline spezza parole senza sillabazione, per esempio Responsa/bile e amministrati/vo. La tabella soprastante ripete quattro volte le medesime intestazioni sulla stessa pagina. | Ridisegnare larghezze e righe, ridurre i campi per tabella e ripetere l’intestazione solo quando utile alla continuazione. | Non applicato |
| P08-03 | pp. 223 | Apparati compilabili | grave | Il Diario degli errori ha otto colonne strette, intestazioni spezzate e una sola riga bianca alta pochi millimetri: non consente una compilazione manuale utile. | Fornire una pagina di lavoro con righe alte e più spazio oppure una scheda separata chiaramente accessibile; preservare una struttura leggibile nel volume. | Non applicato |
| P08-04 | pp. 9 e aperture successive; dettaglio 211 | Gerarchia | lieve | Il titolo del capitolo compare due volte a distanza ravvicinata, prima in nero e poi in rosso. Il piccolo nastro BANDO occupa la zona intermedia. | Eliminare la duplicazione o distinguere titolo e sottotitolo; conservare una gerarchia editoriale uniforme. | Non applicato |
| P08-05 | pp. 231 | Impaginazione | lieve | Una breve avvertenza conclusiva occupa una pagina quasi vuota. | Valutare il recupero alla fine della pagina precedente senza comprimere il testo; mantenere la nuova pagina solo se scelta editoriale intenzionale. | Non applicato |

## Esito e limiti

Richiesto un nuovo export dopo le correzioni. Nessun PDF è stato modificato.

- Copertura panoramica di tutte le pagine per geometria e ritmo; non equivale alla lettura del testo minuto di ogni pagina rasterizzata.
- Lettura puntuale e controllo grafico ingrandito limitati alle pagine elencate; il testo originale completo è documentato nel rapporto separato.
- Nessuna prova cartacea, verifica cromatica, certificazione PDF/X o collaudo di tutti i link. Non controllate qui copertine e materiali commerciali esterni.
- Metriche automatiche di supporto: nessun oggetto testuale oltre il foglio, nessuna pagina bianca e nessun carattere sostitutivo segnalato nell’inventario; tali esiti non eliminano difetti semantici o di impaginazione.

Ledger di copertura: `artifacts/review-integrale-2026-10-02/PDF-VOL-08-ledger.json`. Le tavole esaminate e i dettagli sono conservati negli artefatti dell’audit.
