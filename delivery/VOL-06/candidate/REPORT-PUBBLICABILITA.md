# Report di pubblicabilità — VOL-06

## Giudizio editoriale

Il volume è **pubblicabile con correzioni minori già chiuse**, dal punto di vista editoriale e tecnico locale. La revisione finale non ha rilevato criticità gravi o importanti aperte; i controlli successivi hanno confermato la coerenza del corpus, la copertura didattica e l'esportazione dell'interno.

Il candidato tecnico non equivale ad approvazione o pubblicazione: restano obbligatori la conferma umana, il controllo del canale di vendita e l'esito del KDP Previewer nello step 24.

## Perimetro verificato

- quattro moduli: M-IR01 Scuola e sistema di istruzione, M-IR02 Università e AFAM, M-IR03 Enti di ricerca, M-IR04 Cultura e beni culturali;
- revisione macroeditoriale, contenutistica, stilistica, grammaticale, terminologica e specialistica, con report di modulo;
- coerenza fra indice, matrici didattiche, manifest di text freeze e metadati;
- 4 matrici e 50 righe di copertura complete, senza blocker o warning;
- build di produzione, typecheck e 554 test completati con esito positivo;
- PDF paperback no-bleed di 530 pagine, 6,69 × 9,61 pollici, con font incorporati.

## Evidenze principali

- Revisione editoriale finale: `wiki/reviews/pipeline/VOL-06/21-vol-06.md`.
- Preflight tecnico-editoriale: `wiki/reviews/pipeline/VOL-06/22-vol-06-preflight.md`.
- Manifest di text freeze: cartelle `planning` dei moduli M-IR01, M-IR02, M-IR03 e M-IR04.
- Stato di esecuzione: `pipeline/VOL-06/run-state.json`.

## Limiti e decisione

Il controllo `git diff --check` ha segnalato soltanto hard break Markdown intenzionali nelle opzioni di quiz M-IR02 e un avviso CRLF in un manifest VOL-11 fuori perimetro; non costituiscono un difetto del PDF VOL-06 e non sono stati modificati per preservare layout e lavoro altrui. Le pagine campione 1, 265 e 530 sono state renderizzate per verifica tecnica; l'ispezione interattiva delle immagini non era disponibile nella sandbox. Il KDP Previewer non è disponibile localmente e non viene dichiarato eseguito.

**Decisione:** candidato pronto per lo step 24, senza autorizzazione implicita alla pubblicazione.
