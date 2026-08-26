# Slide Capitale Personale

Deck HTML 16:9 dei 12 volumi, per lo staff. Canone in questa cartella; copia Desktop con `npm run slides:sync`.

## Master visivi

| Master | Classe | Uso |
| --- | --- | --- |
| Navy Premium | `.ancora` | Copertine, citazioni, chiusura |
| Ivory Luxe | `.ivory` | Editoriale, spiegazioni, Q&A |
| Pearl Emerald | `.pearl` | Metodo, step, checklist, esercizi |

Carta Antica è esclusa.

## Ordine VOL-01

Il riferimento al capitolo sta **nelle cartelle e nel codice**, non nel layout delle slide.

Regola cartella: `{numero-pipeline}-{slug-file-wiki}`

Esempio: `wiki/books/il-metodo-bando/chapters/introduzione.md` → `slides/VOL-01/00-introduzione/`

Dentro ogni cartella:

- `index.html` — deck
- `capitolo.json` — volume, numero, titolo, path wiki

Lista completa: `slides/VOL-01/manifest.json`

```
slides/VOL-01/00-introduzione/ … 24-checklist-operative/
(25 cartelle, ordine scheda pipeline M-PA01)
```

## Ordine VOL-02

`slides/VOL-02/01-come-usare-vol-02-insieme-a-vol-01/` … `51-conclusione-vol-02/`

51 cartelle, ordine indice volume: orientamento, M-FL01, M-FL02, M-FL04, M-FL03, finale.

Navigazione deck: frecce, spazio, rotella. Tasto `E` per editare.

## Come aprirle da GitHub

Clone del repo o Download ZIP da GitHub. Apri `slides/index.html` nel browser (doppio clic o «Open with Live Server»). Ogni capitolo è un `index.html` nella sua cartella; CSS, JS e logo stanno in `slides/assets/`. Servono i file vicini: non aprire un deck isolato senza `assets/`.

Volumi: VOL-01 … VOL-12. Catalogo per volume: `slides/VOL-NN/index.html`.
