# Conversazione sintetica - 2026-06-27T19:56:28+02:00

## Contesto
L'utente ha deciso di applicare la nuova architettura del progetto libro, mantenendo il volume principale e il ricettario digitale e predisponendo anche i moduli specialistici divisi per famiglia.

## Decisione registrata
- Il Metodo BANDO usa tre livelli: libro principale, ricettario operativo digitale, moduli specialistici.
- I moduli specialistici sono normalizzati in 6 famiglie e 25 moduli, secondo la tabella effettiva del file esterno analizzato.
- Ogni modulo vive in `wiki/books/moduli/<module-id>/`, con `index.md`, capitoli in `chapters/` e `book_id` uguale allo slug della cartella.
- I primi moduli MVP sono M-FL01, M-IR01, M-FC03 e M-SA02.
- La promessa pubblica corretta e' riusabile, aggiornabile e modulare; evitare copertura totale garantita o aggiornamento automatico.

## Artefatti
- `wiki/books/moduli/architettura-moduli-specialistici.md`
- 25 cartelle modulo sotto `wiki/books/moduli/`
- `wiki/books/moduli/_template-modulo/`
- Aggiornamenti a `wiki/AGENTS.md`, struttura madre, index del libro, dashboard/writer.
