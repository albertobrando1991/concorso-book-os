# VOL-10 — Riconciliazione del catalogo

## Diagnosi

Il catalogo TypeScript, l'architettura canonica e le cartelle reali concordano su 12 volumi commerciali e 25 moduli specialistici univoci. Il test `tests/text-volumes.test.ts` supera 3/3 controlli: nessun codice modulo o book_id duplicato e ogni book_id specialistico risolve a una cartella reale. Per VOL-10 la relazione è univoca: `VOL-10` → `M-TR03` → `moduli/m-tr03-tecnico-ingegneristico`.

## Mappa definitiva

| Volume | Moduli | book_id canonici |
| --- | --- | --- |
| VOL-01 | B-PA01/B-PA11 | `il-metodo-bando` |
| VOL-02 | M-FL01, M-FL02, M-FL03, M-FL04 | `moduli/m-fl01-comuni-unioni`; `moduli/m-fl02-regioni-province-citta-metropolitane`; `moduli/m-fl03-camere-commercio`; `moduli/m-fl04-polizia-locale` |
| VOL-03 | M-FC01, M-FC02, M-FC03 | `moduli/m-fc01-ministeri`; `moduli/m-fc02-agenzie-fiscali`; `moduli/m-fc03-enti-non-economici` |
| VOL-04 | M-FC04 | `moduli/m-fc04-giustizia` |
| VOL-05 | M-FC05 | `moduli/m-fc05-authority-indipendenti` |
| VOL-06 | M-IR01, M-IR02, M-IR03, M-IR04 | quattro book_id `moduli/m-ir*` corrispondenti |
| VOL-07 | M-SA01, M-SA02, M-SA03, M-SA04 | quattro book_id `moduli/m-sa*` corrispondenti |
| VOL-08 | M-TR01 | `moduli/m-tr01-ict-trasformazione-digitale` |
| VOL-09 | M-TR02 | `moduli/m-tr02-appalti-pnrr-fondi-ue` |
| VOL-10 | M-TR03 | `moduli/m-tr03-tecnico-ingegneristico` |
| VOL-11 | M-TR04 | `moduli/m-tr04-ambiente-protezione-civile` |
| VOL-12 | M-SP01, M-SP02, M-SP03, M-SP04 | quattro book_id `moduli/m-sp*` corrispondenti |

## Discrepanze e patch

Nessun modulo orfano, duplicato, mancante o assegnato al volume sbagliato. I 13 capitoli M-TR03 dichiarano `module_code: M-TR03`, famiglia trasversale e book_id coerente. La logica v4 è rispettata: il nucleo comune resta in VOL-01; il delta tecnico è in M-TR03; appalti, ambiente, ICT e altri profili sono raggiunti tramite rinvii precisi.

Non sono necessarie patch di catalogo e non emergono decisioni da sottoporre ad approvazione umana.
