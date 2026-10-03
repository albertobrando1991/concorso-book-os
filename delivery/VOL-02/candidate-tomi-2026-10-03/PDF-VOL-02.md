# Produzione e verifica correttiva — VOL-02, due tomi

## 1. Sintesi editoriale

Il candidato unitario aggiornato contava 967 pagine. È stato distribuito in due interni autonomi per percorso: **Tomo I — Comuni, Regioni, area vasta e Camere di commercio, 700 pagine**; **Tomo II — Polizia locale, 268 pagine**. Il formato resta 6,69 × 9,61 pollici, senza smarginatura. Corpo 11 pt; indice e tabelle 9,5 pt; nessuna riduzione tipografica per rientrare nel limite. Il croquis PL è stato ingrandito a 9,5 pt nell'export dedicato.

Le prove sono in `artifacts/correzioni-collana-2026-10-02/vol02-tomi/`; la copia reviewabile, con manifest e istruzioni, in `delivery/VOL-02/candidate-tomi-2026-10-03/`. Il pacchetto conserva aperti preliminari commerciali, copertine e signoff24. Non sostituisce né sovrascrive il precedente candidato storico.

## 2. Punti applicati della checklist

Questo rapporto sviluppa gli aspetti 1–4, 7–8, 13–15, 23–29 della checklist, applicati a indici, rinvii, schemi, simulazioni derivate e impaginazione. La verifica dei restanti punti testuali è documentata nel [report21](../pipeline/VOL-02/21-vol-02.md) e nei quattro audit specialistici. Il punto5 e il giudizio complessivo30 restano subordinati ai preliminari comuni. Non viene attribuita a una miniatura la prova della correttezza di ogni parola.

Misure sui candidati esatti: 177 voci di indice nel Tomo I e 95 nel Tomo II, tutte riconciliate con il capitolo/nucleo e la pagina effettiva; nessun overflow DOM o testo fuori pagina; nessun marcatore wiki/source_refs nei testi esportati. I font nominali sono confermati dagli span PDF: Garamond circa10,99 pt e Arial circa9,49 pt, differenza dovuta alla conversione di stampa. Font e relativi programmi incorporati sono registrati nel manifest tecnico.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| P02-10 | Edizione unitaria precedente e prova aggiornata967p | Limite di produzione | grave | Superato il massimo828 del formato/carta considerato. | Due tomi per percorsi completi, con propri indici e chiusure. | Corretto localmente:700/268p; nessuna verifica KDP online dichiarata |
| P02-01 | Tomo I, capitoli8–17; tavole pp257/292/297 | Rinvii e numerazione | media | Persistenza dei numeri locali FL01 nel volume assemblato. | Riallineati59 blocchi/celle; mantenuti riferimenti al Metodo BANDO e numeri/importi dei capitoli di bilancio. | Corretto e verificato; manifest reference-alignment.json e ingrandimenti |
| P02-02 | Tomo I p181 | Tabelle | media | Tabella obiettivi troppo fitta nella precedente prova. | Separazione coerente delle dimensioni in tabelle leggibili, senza restringere il font. | Corretto; pagina ingrandita esaminata |
| P02-03 | Tomo I p141, apertura welfare | Duplicazione | media | Apertura ripetuta. | Eliminata la duplicazione nel sorgente; mantenuti obiettivo e sviluppo. | Corretto; apertura verificata |
| P02-04 | Tomo II p102; Tomo I p659 | Chiusure di capitolo | lieve | Riferimenti isolati su pagina quasi vuota. | Riordinati i riferimenti senza eliminare fonti; cap32 chiude a659 anziché lasciare tre righe a660. | Corretto; contact e ingrandimento659 verificati |
| P02-05 | Tomo I, schemi18.1–18.5 e30.1–30.5 | Leggibilità figure | media | Dieci raster con microtesti. | Sostituiti da tabelle e sequenze native; originali conservati fuori dall'export. | Corretto; tutte dieci tavole lette negli ingrandimenti |
| P02-06 | Apparati e pagine finali | Contenuti interni | media | Rinvii a materiali di lavorazione non adatti al lettore. | Rinvii a capitoli, soluzioni stampate e fonti istituzionali; pulizia dei preliminari di modulo. | Corretto; ricerca su intero testo esportato senza occorrenze interne |
| P02-07 | Tomo I pp329–330, schema18.4 | Sovrapposizione | media | Elementi del diagramma regionale si sovrapponevano. | Sequenza nativa con numeri, ruoli e verifiche; intestazione ripetuta nel seguito. | Corretto; nessuna sovrapposizione negli ingrandimenti |
| P02-08 | Tomo I, schemi camerali pp610–619 | Accenti e microtesti | lieve | Accenti mancanti e resa irregolare nelle immagini. | Testo nativo con ortografia riesaminata. | Corretto; tutti gli schemi camerali ingranditi |
| P02-09 | Tomo I p615, schema30.3 | Relazioni camerali | media | Rete rappresentata come una gerarchia ambigua. | Relazioni nominate: appartenenza, rappresentanza/raccordo, consultazione e servizi; nessuna sovraordinazione generale inventata. | Corretto; confronto con Statuto Unioncamere artt1–3 |

## 4. Osservazioni per capitolo

Le dieci tavole sono state controllate a piena leggibilità su pp324,325,327,329–330,332 e610–612,615,617,619. Le tabelle native possono proseguire sulla pagina successiva mantenendo intestazione e numerazione. Non hanno più un requisito di risoluzione raster.

La simulazione del Tomo I contiene quiz1–15 e percorsi1–3, dei quali se ne sceglie uno; quella del Tomo II quiz16–20 e percorso4. La numerazione coordinata è spiegata nella consegna. Durate e punteggi sono stati ricalcolati, non copiati dal master unitario. Le soluzioni sono paragrafi leggibili, evitando due colonne quasi vuote di una tabella a tre colonne. Controllate pp696–699 e265–267.

Nel capitolo47 il croquis di p222 resta orientativo e non in scala: quote della tabella distinte dalle distanze grafiche, rilievo distinto da ricostruzione della dinamica. L'ingrandimento del font non modifica coordinate o calcoli. Nel cap32 gli intervalli3-5,8-10,13-14 del D.M.93/2017 sono stati ripristinati dopo il controllo visivo; hash del freeze aggiornato come delta tipografico.

## 5. Coerenza globale

Tomo I: orientamento1–3, Comune4–17, Regione18–29, Camera30–34, simulazione50 e conclusione51. Tomo II: orientamento1–3, PL35–49, simulazione50 e conclusione51. I capitoli specialistici non sono divisi fra tomi; i cinque comuni/di chiusura sono riproposti e adattati. Il corpo del libro è invariato come dimensione.

Tutte le pagine sono state scorse nelle61 tavole di contatto:44 per il Tomo I e17 per il Tomo II. Dopo le ultime due correzioni del Tomo I, i confronti di testo/pagina hanno isolato le sole pagine292 e659, riesaminate in ingrandimento; conteggio e pagine degli indici non sono cambiati. I controlli geometrici sono stati ripetuti sul PDF finale.

## 6. Contenuto da verificare

La [specifica ufficiale KDP](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6), ricontrollata il3 ottobre2026, ammette24–828 pagine per6,69×9,61 pollici con inchiostro nero e carta bianca. Il rispetto del limite non prova da solo accettazione del file: Print Previewer, copertina, dati commerciali e copia fisica restano fuori da questa verifica locale.

La fonte camerale è lo [Statuto Unioncamere, norme generali artt1–3](https://www.unioncamere.gov.it/chi-siamo/statuto/i-norme-generali-art-1-3), consolidata in `wiki/sources/vol-02-camerale-verifica-2026-10-03.md`. Non si estende il riscontro a parti dello Statuto non consultate.

Le condizioni digitali e i dati definitivi dei preliminari restano dipendenza comune non verificata, già sottoposta al coordinatore. Nessuna promessa aggiuntiva è stata inventata.

## 7. Suggerimenti facoltativi (non errori)

Verificare il comfort delle griglie workbook su una copia fisica. La stampa in nero convertirà gli accenti cromatici del profilo comune: gli schemi corretti si leggono per testo e struttura, senza affidare significati essenziali al colore.

## 8. Priorità degli interventi

1. Confermare/correggere i preliminari comuni e rigenerare i candidati interessati.
2. Eseguire formalmente gate21–23 sui file esatti quando la dipendenza è risolta.
3. Preparare copertine e metadati separati dei tomi secondo la decisione editoriale, prima del controllo esterno di stampa.
4. Nessun signoff24 o caricamento eseguito in questo mandato.

## 9. Giudizio di pubblicabilità

**Non pubblicabile allo stato attuale per i preliminari comuni ancora da confermare.** I dieci rilievi PDF storici sono corretti nei due interni reviewabili. Le prove tecniche locali supportano leggibilità, numero di pagine e coerenza degli indici; non costituiscono un'approvazione commerciale o KDP.

## 10. Limiti di questa revisione

La scansione visiva a miniature copre tutte le pagine e individua difetti macroscopici; gli ingrandimenti riguardano i punti critici, le tavole e un insieme esplicito di pagine dense. Non è dichiarata una lettura visiva a piena risoluzione di tutte968 pagine. Non sono stati modificati i raster originali né il renderer condiviso. Builder, payload, manifest e report tecnici restano disponibili per riprodurre la composizione; una successiva variazione ai master richiede nuovi hash, export e controlli.
