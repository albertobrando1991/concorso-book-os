# Standard di completezza delle slide

Le slide non sono uno schema vuoto. Devono **insegnare il concetto**, non solo nominarlo.

## Ogni concetto in slide

Almeno tre di questi quattro:

1. **Che cos’è** (definizione operativa)
2. **Come funziona / a che serve in prova**
3. **Esempio o caso**
4. **Errore tipico o distinzione**

Una card con solo titolo + una riga è insufficiente.

## Densità

- 16–22 slide se il capitolo è denso; non restare a 15 se si perde contenuto.
- Testo di corpo: frasi complete, non elenchi di parole.
- Titoli corti; spiegazione sotto, non nel titolo.
- Almeno **una mappa** (`.map`) e **una nota** (`.note` o `.warn`) per capitolo.

## Da dove viene il testo

Solo dal file wiki in `capitolo.json` → `source`. Niente norme inventate. Niente path wiki visibili.

## Immagini (obbligatorie se esistono)

1. Copiare i PNG del capitolo wiki in `images/` della cartella slide.
   - VOL-01: `wiki/books/il-metodo-bando/assets/chapter-NN/*.png` (preferire `*-v3.png` se c’è).
   - Moduli: `wiki/books/moduli/<id>/assets/` se presente.
2. Inserire **almeno 2 slide con figura** quando il capitolo ha mappe: `.figure img` + `.caption`, oppure `.split-visual` testo+immagine.
3. L’immagine insegna (mappa, schema, confronto). Niente stock fotografici generici, niente download a caso da internet.
4. Se il wiki non ha figure, usare `.map` CSS; generare un diagramma brand (Navy/Ivory/Pearl, Playfair+Montserrat) solo se serve davvero.

## Blocchi CSS

- `.lead` paragrafo pieno
- `.note` nota didattica
- `.warn` errore / attenzione
- `.map` + `.node` + `.arrow` mappa di flusso
- `table.dense` tabelle di concetti
- `.figure` / `.caption` / `.split-visual` figure del capitolo
