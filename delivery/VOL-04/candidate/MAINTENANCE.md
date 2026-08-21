# Piano di manutenzione editoriale

## Cadenza ordinaria

- Riesame trimestrale delle fonti normative, dei riferimenti organizzativi e dei collegamenti esterni.
- Verifica semestrale di metadati commerciali, descrizione, parole chiave e categorie KDP.
- Nuovo preflight e nuova prova di stampa a ogni modifica dell'impaginato o della copertina.

## Eventi che impongono un aggiornamento

- riforme del processo civile, penale, amministrativo o tributario richiamate nel volume;
- variazioni normative o organizzative relative a Ufficio per il processo, cancellerie, UNEP, DAP o DGMC;
- modifica di URL, denominazioni istituzionali, concorsi o profili professionali citati;
- correzione che alteri la paginazione;
- cambio di formato di taglio, carta, colore di stampa, rilegatura o finitura;
- segnalazione documentata di un errore da parte di lettori o staff.

## Procedura di aggiornamento

1. Aprire una nuova versione candidata e aggiornare il cutoff normativo.
2. Annotare ogni intervento nel changelog e nei report di revisione.
3. Rigenerare l'interno e, se varia la paginazione, ricalcolare il dorso e rigenerare la copertina.
4. Aggiornare `VERSION.json` e `MANIFEST.sha256`.
5. Ripetere preflight, Print Previewer, revisione umana e controllo della copia di prova.

Conservare separatamente ogni versione già pubblicata per consentire tracciabilità e ripristino.
