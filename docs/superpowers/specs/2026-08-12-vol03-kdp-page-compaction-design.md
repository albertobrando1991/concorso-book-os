# VOL-03 — Compattazione KDP controllata

## Contesto

La composizione aggiornata del VOL-03 produce 832 pagine nel Book Studio. Il limite del profilo paperback KDP adottato dal progetto è 828 pagine. Il contenuto editoriale non deve essere eliminato o abbreviato per superare il limite.

## Obiettivo

Portare il VOL-03 a non più di 828 pagine, preservando:

- formato pagina 6,69 × 9,61 pollici;
- margini speculari 23/13 mm e margini superiore/inferiore da 18 mm;
- corpo Garamond 11 pt con testo giustificato;
- gerarchia Arial 20/14/12 pt;
- contenuto, immagini, tabelle e ordine delle sezioni;
- impaginazione invariata per ogni altro volume.

## Soluzione approvata

Il contenitore del Book Studio riceve una classe CSS specifica quando `bookId` è `volumi/vol-03`. La classe applica una compattazione verticale minima ai soli blocchi di contenuto del VOL-03:

- interlinea del corpo da 1,18 a 1,16, entro l'intervallo editoriale ammesso 1,15–1,20;
- margine inferiore dei paragrafi da 4 pt a 3,5 pt;
- margini verticali di H3/H4/H5 e liste ridotti in misura contenuta;
- dimensioni dei caratteri, margini pagina e geometria delle tabelle invariati.

La stessa classe deve essere presente anche sul contenitore di misurazione nascosto, affinché calcolo e resa usino identiche metriche.

## Alternative escluse

1. Ridurre il corpo sotto 11 pt: comprometterebbe lo standard editoriale.
2. Ridurre i margini: altererebbe il profilo KDP e la sicurezza di rilegatura.
3. Eliminare o abbreviare testo: violerebbe il vincolo di preservazione dei contenuti.
4. Applicare la compattazione globalmente: introdurrebbe variazioni non richieste negli altri volumi.

## Verifica

La modifica è accettabile soltanto se:

1. un test dimostra che la classe compatta è assegnata esclusivamente al VOL-03;
2. typecheck, test pertinenti e build terminano con exit code 0;
3. il Book Studio produce al massimo 828 pagine;
4. l'audit DOM non rileva overflow, collisioni, tabelle fuori area, immagini mancanti o gerarchia tipografica errata;
5. il PDF conserva pagina 6,69 × 9,61 pollici, assenza di bleed e font incorporati;
6. il report dello step 22 registra evidenze e nuovo SHA-256.

## Gestione dell'insuccesso

Se la prima compattazione non basta o produce anomalie, non si elimina contenuto. Si correggono soltanto gli spazi verticali specifici del VOL-03, restando nei limiti tipografici canonici, e si ripete l'intero preflight.
