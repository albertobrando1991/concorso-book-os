# Preflight tecnico ed editoriale — VOL-10

## Esito

PASS locale, registrato allo step 22 della pipeline. Il gate automatico `preflight` non è implementato; la chiusura è stata eseguita con accettazione manuale motivata e resta distinta dalla conferma umana dello step 24.

## Evidenze

- 13 capitoli, 88 nuclei nel testo e nell’indice;
- copertura canonica senza blocker o warning; wikilink, 71 `source_refs` e frontmatter senza errori;
- tabelle Markdown parseabili; nessuna immagine reader-facing mancante o duplicata;
- Book Studio: 100 pagine, zero overflow, zero sovrapposizioni e zero asset mancanti;
- PDF: 100 pagine, 481,92 × 691,92 pt, font incorporati e documento non cifrato;
- regressione parser risolta e coperta da test;
- sei suite pertinenti e 52 test superati, oltre a typecheck e build di produzione;
- `git diff --check` privo di errori di whitespace;
- tutte le 100 pagine renderizzate e ispezionate visivamente.

## Limite di canale

KDP Previewer non è installato nell’ambiente. Il controllo proprietario deve essere eseguito dallo staff dopo il caricamento del candidato.

Riferimento completo: `wiki/reviews/pipeline/VOL-10/22-vol-10.md`.
