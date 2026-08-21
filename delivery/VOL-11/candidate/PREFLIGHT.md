# Preflight tecnico ed editoriale — VOL-11

## Esito

PASS locale, registrato allo step 22 della pipeline. Il gate automatico `preflight` non è implementato; la chiusura è stata eseguita con accettazione manuale motivata e resta distinta dalla conferma umana dello step 24.

## Evidenze

- 14 capitoli, 90 nuclei nel testo e 90 nell'indice;
- audit su 37 file: copertura, wikilink, `source_refs` e frontmatter senza errori;
- 89 tabelle Markdown parseabili; nessuna immagine reader-facing mancante o duplicata;
- Book Studio: 223 pagine, zero overflow, zero sovrapposizioni, zero asset mancanti;
- PDF: 223 pagine, 481,92 × 691,92 pt, testo estraibile in ogni pagina, font incorporati, non cifrato;
- E21-01 risolto: le 14 aperture mostrano un titolo unico;
- 58 test pertinenti, typecheck e build produzione superati;
- `git diff --check` privo di errori di whitespace.

## Limite di canale

KDP Previewer non è installato nell'ambiente. Il controllo proprietario deve essere eseguito dallo staff dopo il caricamento del candidato.

Riferimento completo: `wiki/reviews/pipeline/VOL-11/22-vol-11.md`.
