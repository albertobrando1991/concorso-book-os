# Task 17b — Ledger semantico fail-closed

## Esito

- Stato del ledger: **aperto**, non attestato.
- Nuclei riconciliati: 82 su 13 capitoli; matrice e indice restano controllati bilateralmente.
- Righe complete: **0**.

## Decisione

Il validatore non classifica semanticamente frasi estratte dai capitoli. Il renderer genera esclusivamente stati `open`; Q/C/E restano non attribuiti per nucleo. Un futuro stato `verified` è ammesso soltanto con una attestazione curata nel manifest contenente `nucleusId`, `evidenceQuote`, `sourceLocation`, `reviewer` e `gateId` fra step 13 e 18, oltre alla corrispondenza puntuale della citazione con il nucleo.

## Debiti aperti

- Audit specialistico e attribuzione delle fonti: step 15.
- Revisione trasversale, correzioni e freeze: step 13-16.
- Verifiche visive: step 17-18.
- Q/C/E per nucleo: mapping strutturato da produrre in un audit successivo.

## Limite dichiarato

Il report non dichiara completati audit, freeze, impaginazione o conferma umana. Lo step 24 non è stato modificato.