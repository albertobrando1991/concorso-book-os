# Applicazione delle correzioni — M-FC03 Enti pubblici non economici

## Esito

Tutti gli errori strutturali, contenutistici, di autonomia, coerenza e lingua individuati nella revisione trasversale sono stati corretti. Le modifiche sostanziali alle appendici hanno superato nuovamente lint, densità didattica, controllo dei riferimenti e revisione; le correzioni linguistiche successive non hanno modificato fonti, significato o struttura.

## Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| TR-01 | Intero modulo | Struttura | Critico | Assenza del Formato 2. | Retrofit dei 19 testi e matrice atomica. | Corretto |
| TR-02 | Appendici A-F | Contenuto | Critico | Appendici non autonome. | Sviluppo completo e verifiche applicative. | Corretto |
| TR-03 | Più capitoli | Autonomia | Importante | Dipendenze da note e strumenti interni. | Rimozione dal corpo; tracciabilità nel frontmatter. | Corretto |
| TR-04 | Intero modulo | Lingua | Importante | Accenti mancanti e apostrofi sostitutivi. | Normalizzazione italiana e seconda scansione. | Corretto |
| TR-05 | Pipeline e matrice | Coerenza | Importante | Appendici senza numerazione stabile. | Numerazione 14-19 e resolver CLI testato. | Corretto |
| TR-06 | Indice e front matter | Metadati | Importante | Stati legacy non coerenti. | Allineamento a `final`/`text_ready`. | Corretto |
| TR-07 | Verifiche | Stile | Lieve | Griglia ricorrente. | Conservata come apparato didattico intenzionale. | Corretto |

## Registro applicativo

| ID | File modificato | Correzione | Fonte/evidenza | Stato finale |
|---|---|---|---|---|
| TR-01 | 19 file in `chapters/`; `planning/02-matrice-copertura-didattica.md` | Cinque nuclei per testo, quiz, caso, verifica e 95 righe atomiche. | Gate 09-12 e audit densità globale. | Chiuso |
| TR-02 | `appendice-a`–`appendice-f` | Teoria, distinzioni, casi, laboratori e controlli aggiunti nel perimetro dichiarato. | Tutte le appendici superano almeno 3.000 parole e 5×600 parole. | Chiuso |
| TR-03 | capitoli 02, 04, 06, 07, 09; appendici B e D; capitolo 13 | Eliminati richiami a wiki, source note, fonti consolidate e note di review. | Chapter-lint su 19/19 file: zero blocker. | Chiuso |
| TR-04 | 19 file in `chapters/` | Corretti apostrofi impropri e termini tronchi; preservati frontmatter e percorsi. | Scansione indipendente: nessun residuo delle forme bersaglio. | Chiuso |
| TR-05 | scheda VOL-03, matrice M-FC03, CLI e test | Appendici dichiarate come capitoli 14-19; risoluzione del numero dichiarato. | `cli-chapter-filter.test.ts`: 3/3 test superati. | Chiuso |
| TR-06 | `index.md`; sei file `front-matter/` | Stati e descrizioni allineati alla fase editoriale reale. | Confronto fra indice, premessa, scheda e run-state. | Chiuso |
| TR-07 | 19 blocchi `▣ Verifica` | Apparato mantenuto e documentato nella Bibbia del Modulo. | Funzione didattica comune; contenuti variabili per capitolo. | Chiuso |

## Controlli ripetuti

- `chapter-lint`: 19/19 testi verdi;
- densità Formato 2: 19/19 testi verdi;
- matrice: 95 nuclei completi con checklist dimensionale;
- report dei capitoli: tutti chiusi senza warning;
- frontmatter: `format_version: 2`, `dati_operativi`, `source_refs` e `last_compiled_from` preservati;
- test del resolver appendici: tre test verdi.

## Giudizio di pubblicabilità

Pubblicabile con correzioni minori.

Il modulo non presenta errori obbligatori aperti. Restano da eseguire l'audit specialistico conclusivo e il manifest di text freeze previsti dagli step successivi; non sono rinvii a revisione umana.
