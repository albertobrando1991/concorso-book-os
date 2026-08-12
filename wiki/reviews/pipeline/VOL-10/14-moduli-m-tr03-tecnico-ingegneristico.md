# Applicazione correzioni — M-TR03 Tecnico-ingegneristico

## Sintesi

Le correzioni certe emerse dalla revisione trasversale sono state applicate in ordine di priorità. Non sono stati applicati i suggerimenti facoltativi. Il modulo può passare all'audit specialistico automatico dello step 15; il preflight di E06 resta assegnato alla fase di produzione.

## Registro delle correzioni

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| E01 | `planning/02-matrice-copertura-didattica.md` | Copertura | Grave | I sei nuclei del capitolo 9 erano assenti dalla matrice. | Già aggiunti nello step 13; evidenza: 78 ID univoci su 78 nuclei. | Risolto |
| E02 | Cap. 1 | Linking interno | Grave | Quattro wikilink erano esposti nel corpo. | Già sostituiti nello step 13; evidenza: nessun wikilink nel corpo dei capitoli. | Risolto |
| E03 | Capp. 6-8, 10-11 | Ortografia | Media | Accenti obbligatori omessi nel testo naturale. | Ripristinati con sostituzioni lessicali controllate; codifica verificata senza mojibake. | Risolto |
| E04 | Frontmatter capp. 1-13 | Metadati | Media | Sei campi usavano valori disomogenei o mancanti. | Uniformati ai valori canonici; ricerca dei valori precedenti senza occorrenze. | Risolto |
| E05 | `index.md` | Indice e workflow | Media | Titolo del cap. 6 e descrizione del workflow non erano aggiornati. | Allineati titolo, audit automatico allo step 15 e conferma umana allo step 24. | Risolto |
| E06 | Capp. 4, 6-13 | Layout | Lieve | Resa di tabelle e box non verificabile senza PDF. | Eseguire il preflight nella fase di produzione. | Da verificare |

## Verifiche eseguite

- Contenuti: nessuna modifica normativa o concettuale introdotta.
- Struttura: 13 capitoli e 78 nuclei Format 2 invariati.
- Metadati: schema uniforme su tutti i capitoli.
- Grafia: sostituzioni limitate al testo naturale e controllate nel contesto.
- Workflow: nessun gate dichiarato verde senza verifica.

## Giudizio finale

**Pubblicabile per il passaggio allo step 15.** Non restano errori editoriali certi E01-E05; E06 è un controllo di impaginazione e non può essere chiuso prima della produzione del PDF.
