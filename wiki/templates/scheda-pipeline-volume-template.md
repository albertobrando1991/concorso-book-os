---
type: pipeline_spec
volume_code: VOL-00
volume_title: Titolo commerciale del volume
cut_off_date: 2026-01-01
responsabile_normativo: Nome Cognome
responsabile_editoriale: Nome Cognome
writer_provider: codex
phases: [C, D, F]
status: draft
updated_at: 2026-01-01
---

# Scheda di pipeline — VOL-00

Compilare questa scheda prima di aprire il ciclo editoriale. È l'unico input richiesto dalla pipeline: da qui il CLI ricava l'ordine degli step, i target e i valori dei prompt.

Copiare il file in `wiki/books/<percorso-del-volume>/planning/00-scheda-pipeline.md` e sostituire i valori.

## Campi del frontmatter

| Campo | Obbligatorio | Formato | Nota |
| --- | --- | --- | --- |
| `volume_code` | sì | `VOL-NN` | deve coincidere con `src/catalog/text-volumes.ts` |
| `volume_title` | sì | testo | titolo commerciale |
| `cut_off_date` | sì | `AAAA-MM-GG` | data di chiusura delle fonti, non deducibile dal repo |
| `responsabile_normativo` | sì | nome | presidia il cut-off e la tracciabilità normativa durante il lavoro automatico |
| `responsabile_editoriale` | no | nome | se assente vale il responsabile normativo |
| `writer_provider` | no | `codex`, `claude`, `kimi`, `openai`, `hermes`, `local` | se assente vale `WRITER_PROVIDER` dell'ambiente |
| `phases` | sì | elenco fra `A`-`G` | fasi da eseguire: `C` capitoli, `D` modulo, `F` finale |

## Moduli

Un modulo per riga, in ordine di priorità. La colonna `Fasi` è facoltativa: se vuota vale l'elenco dichiarato nel frontmatter.

| Codice | Module id | Priorità | Fasi |
| --- | --- | --- | --- |
| M-XX01 | moduli/m-xx01-nome-cartella | 1 | |
| M-XX02 | moduli/m-xx02-nome-cartella | 2 | |

## Capitoli M-XX01

Tabella facoltativa. Se assente, la pipeline deriva i capitoli dai file presenti in `<module id>/chapters/` e lo dichiara nel run-state come `chaptersSource: derived`. Dichiararli esplicitamente serve quando l'ordine di lavorazione non coincide con l'ordine alfabetico, quando la matrice di copertura non è quella predefinita o quando il file non esiste ancora. In una tabella dichiarata il titolo editoriale destinato al lettore è obbligatorio.

| # | Titolo | File | Matrice | Stato atteso | Min parole | Min quiz | Note |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| 01 | Titolo editoriale destinato al lettore | chapters/01-nome-file.md | planning/02-matrice-copertura-didattica.md | completo | 3000 | 6 | |

## Dopo la compilazione

```
npm run pipeline -- doctor
npm run pipeline -- init VOL-00
npm run pipeline -- next VOL-00
```

Il protocollo dei 25 prompt resta in `[[templates/prompt-staff-revisione-completa-volumi]]`: la pipeline lo legge da lì, non ne conserva una copia.
