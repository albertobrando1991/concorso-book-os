# Riconciliazione catalogo — VOL-10

## Mappa definitiva

| Volume | Moduli | book_id |
|---|---|---|
| VOL-01 | B-PA01/B-PA11 | `il-metodo-bando` |
| VOL-02 | M-FL01, M-FL02, M-FL03, M-FL04 | `moduli/m-fl01-comuni-unioni`, `moduli/m-fl02-regioni-province-citta-metropolitane`, `moduli/m-fl03-camere-commercio`, `moduli/m-fl04-polizia-locale` |
| VOL-03 | M-FC01, M-FC02, M-FC03 | `moduli/m-fc01-ministeri`, `moduli/m-fc02-agenzie-fiscali`, `moduli/m-fc03-enti-non-economici` |
| VOL-04 | M-FC04 | `moduli/m-fc04-giustizia` |
| VOL-05 | M-FC05 | `moduli/m-fc05-authority-indipendenti` |
| VOL-06 | M-IR01, M-IR02, M-IR03, M-IR04 | cartelle canoniche omonime sotto `moduli/` |
| VOL-07 | M-SA01, M-SA02, M-SA03, M-SA04 | cartelle canoniche omonime sotto `moduli/` |
| VOL-08 | M-TR01 | `moduli/m-tr01-ict-trasformazione-digitale` |
| VOL-09 | M-TR02 | `moduli/m-tr02-appalti-pnrr-fondi-ue` |
| VOL-10 | M-TR03 | `moduli/m-tr03-tecnico-ingegneristico` |
| VOL-11 | M-TR04 | `moduli/m-tr04-ambiente-protezione-civile` |
| VOL-12 | M-SP01, M-SP02, M-SP03, M-SP04 | cartelle canoniche omonime sotto `moduli/` |

## Diagnosi

- Catalogo: 12 volumi commerciali e 25 moduli specialistici unici.
- M-TR03 appartiene correttamente a VOL-10, famiglia `trasversali`, con `book_id: m-tr03-tecnico-ingegneristico` nei capitoli.
- Nessun modulo orfano, duplicato, mancante o assegnato al volume errato.
- La copertura v4 di M-TR03 mantiene il nucleo comune in VOL-01, il delta tecnico nel modulo e rinvii cross-family qualificati.

## Patch applicate

Nessuna: non sono emerse correzioni di catalogo non ambigue da applicare.

## Decisioni umane

Nessuna decisione richiesta per la collocazione di VOL-10/M-TR03.

Verifica automatica: `tests/text-volumes.test.ts` e `tests/editorial-layout.test.ts`, 4 test superati.
