# VOL-07 Step 20 Page-by-Page Audit Design

## Contesto

Lo step 20 della pipeline VOL-07 deve controllare nel Book Studio tutte le pagine del volume, dalla prima all'ultima, e chiudere il gate manuale `page-fill` soltanto dopo aver corretto e ricontrollato ogni pagina impattata. Lo step 19 ha consegnato un master KDP di 381 pagine con numerazione continua, 6 sezioni di front matter, 4 aperture di modulo, 25 capitoli, 7 nuclei indicizzati e zero overflow o sovrapposizioni strutturali. Lo step 20 amplia quella verifica alla qualità pagina-per-pagina.

La filosofia visiva resta `Precisione Vitale`, già approvata nello step 17. Non viene definita una nuova estetica e non vengono generati nuovi contenuti editoriali o immagini. L'audit valuta la resa del volume esistente e applica soltanto correzioni tecniche o tipografiche necessarie.

## Obiettivi

- Ispezionare automaticamente e visivamente tutte le 381 pagine, senza campionamento.
- Registrare per ogni pagina: pagina, tipo di problema, elemento, gravità, correzione ed esito.
- Verificare numerazione, front matter, gerarchie, giustificazione, font, vedove/orfane, spazi bianchi, tabelle, residui Markdown, box, esercizi, immagini, didascalie, margini, gutter, overflow, asset e alternanza recto/verso.
- Correggere chirurgicamente le anomalie bloccanti o significative.
- Rieseguire il controllo sulle pagine impattate e poi sull'intero volume.
- Produrre evidenze ripetibili sufficienti per la chiusura manuale del gate `page-fill`.

## Non-obiettivi

- Non generare il PDF: l'output resta la preview del Book Studio.
- Non modificare i 25 capitoli congelati salvo che un'anomalia non possa essere risolta nel renderer e richieda una correzione editoriale puntuale, esplicitamente documentata.
- Non creare nuove immagini o decorazioni.
- Non svolgere la revisione editoriale totale dello step 21.
- Non dichiarare pubblicabilità finale, riservata agli step successivi e alla conferma umana dello step 24.

## Approccio scelto

Viene creato un auditor dedicato e riutilizzabile, separato dal legacy `verify-volume01-page-fill.mjs`. L'alternativa di estendere lo script VOL-01 è stata scartata perché manterrebbe nomi, default e assunzioni specifiche del volume base. Un controllo one-off è stato scartato perché non sarebbe ripetibile né adeguato a un gate di pipeline.

L'auditor combina tre prove:

1. diagnostica DOM esaustiva su ogni pagina;
2. tavole-contatto PNG che mostrano l'intera sequenza;
3. screenshot singoli delle sole pagine segnalate.

## Componenti

### Regole pure di classificazione

Un modulo indipendente riceve la diagnostica di una pagina e restituisce una lista di problemi normalizzati. Ogni problema contiene:

- `page`;
- `problemType`;
- `element`;
- `severity` (`bloccante`, `media`, `lieve`, `nessuna`);
- `correction`;
- `outcome`.

Le regole pure sono testate senza browser. Il modulo non legge file, non apre pagine e non modifica il DOM.

### Auditor Playwright

Lo script apre `volumi/vol-07` nel Book Studio, seleziona la modalità Libro, attende font, immagini e stabilizzazione della paginazione, poi scorre i 381 elementi `.bookPage` nell'ordine editoriale. Per ogni pagina raccoglie:

- numero assegnato e indice DOM;
- percorso capitolo, titolo, tipo sezione, layout front matter e codice modulo;
- classe recto/verso;
- dimensioni fisiche e padding calcolati;
- rettangolo utile, altezza occupata, spazio libero, overflow e collisioni;
- primo e ultimo blocco visibile;
- heading presenti e loro posizione;
- paragrafi, numero di righe visive e stato di continuazione;
- tabelle, frammenti continuati e presenza delle intestazioni;
- callout, quiz, esercizi e box;
- immagini, didascalie, stato di caricamento e dimensioni naturali;
- testo visibile sospetto per pipe o separatori Markdown;
- famiglie, dimensioni e peso dei font effettivamente applicati;
- `text-align`, `orphans` e `widows` calcolati dal browser.

Il renderer espone solo gli attributi diagnostici strettamente necessari, senza aggiungere testo visibile o cambiare il contenuto del volume.

### Registro Markdown

L'auditor genera `wiki/reviews/pipeline/VOL-07/20-vol-07-audit-pagina-per-pagina.md` con frontmatter canonico e quattro sezioni:

1. sintesi e conteggi;
2. tabella delle anomalie;
3. registro di tutte le 381 pagine;
4. correzioni e riesecuzioni.

Il registro usa le colonne richieste dal prompt:

```text
pagina | tipo di problema | elemento | gravità | correzione | esito
```

Una pagina conforme riceve comunque una riga esplicita con `nessuno`, `pagina`, `nessuna`, `nessuna`, `conforme`. In questo modo l'evidenza dimostra il controllo dell'intera sequenza e non soltanto delle anomalie.

### Tavole-contatto

Sulla baseline vengono prodotte 20 tavole PNG in `artifacts/`, con 20 pagine per tavola e l'ultima tavola contenente la pagina 381. Ogni miniatura mostra chiaramente il numero pagina; l'ordine è da sinistra a destra e dall'alto in basso. Se una correzione cambia il totale finale, il numero di tavole diventa `ceil(pageCount / 20)`. Le tavole servono alla seconda passata visiva su ritmo, vuoti, densità, front matter, aperture, alternanza recto/verso, tabelle, box e immagini.

Le pagine segnalate ricevono anche uno screenshot PNG singolo a risoluzione originale. Nessun PDF e nessun JSON aggiuntivo costituiscono deliverable dello step 20.

## Regole di audit

### Bloccanti

- pagina mancante, duplicata o con numero non progressivo;
- dimensioni pagina diverse da 6,69 × 9,61 pollici oltre la tolleranza di rendering;
- gutter o margini non speculari: recto con 23 mm interni a sinistra e verso con 23 mm interni a destra;
- overflow oltre 8 px o collisione significativa tra blocchi/footer;
- asset mancante, immagine non caricata, crop o didascalia fuori pagina;
- testo Markdown grezzo visibile, compresi pipe o separatori di tabella fuori da codice;
- heading isolato come ultimo blocco della pagina;
- frammento di tabella senza intestazione, tabella tagliata o oltre margine;
- font o dimensioni fuori dal master canonico;
- prosa ordinaria non giustificata;
- sequenza di immagini consecutive priva di blocco testuale o strutturale motivante.

### Significativi

- frammento continuato di paragrafo con meno di tre righe all'inizio o alla fine della pagina;
- pagina interna quasi vuota senza causa strutturale;
- spazio bianco anomalo rispetto alla distribuzione del volume;
- box, esercizio o callout separato dal proprio titolo o dal primo contenuto;
- incoerenza visiva tra pagine recto e verso.

### Eccezioni motivate

- frontespizio e altre pagine di front matter possono usare intenzionalmente più spazio bianco;
- l'ultima pagina di un capitolo o di una sezione può essere poco piena;
- un'apertura di modulo può essere centrata verticalmente;
- una tabella può continuare su più pagine se ogni frammento conserva intestazione e leggibilità;
- l'assenza di immagini non è un problema: lo step 18 ha già accertato che VOL-07 non contiene asset editoriali obbligatori.

Le eccezioni non nascondono errori meccanici: numerazione, dimensioni, margini, overflow, font, asset e residui Markdown restano sempre verificati.

## Soglie per spazio e riempimento

L'auditor calcola la distribuzione dello spazio libero sulle pagine non terminali. Una pagina viene proposta per revisione visiva quando supera il maggiore tra 180 px e la mediana del volume più 120 px. Viene inoltre segnalata se il contenuto utile occupa meno del 35% dell'area disponibile e la pagina non è un frontespizio, un'apertura di modulo o la pagina terminale della sezione.

Queste soglie generano candidati, non condanne automatiche: la tavola-contatto e lo screenshot singolo determinano se il vuoto è anomalo o motivato.

## Flusso di esecuzione

1. Eseguire test e typecheck di baseline.
2. Avviare il Book Studio su una porta dedicata.
3. Eseguire l'auditor su VOL-07 e produrre il primo registro e le 20 tavole-contatto.
4. Ispezionare tutte le tavole in ordine e classificare ogni candidato.
5. Applicare correzioni minime al renderer o, solo se inevitabile, al contenuto interessato.
6. Rieseguire gli screenshot singoli delle pagine impattate.
7. Rieseguire l'audit completo delle 381 pagine.
8. Aggiornare il registro con correzione ed esito finale.
9. Eseguire typecheck, suite completa e `git diff --check`.
10. Tentare `complete` senza forzature; poiché `page-fill` è dichiarato non implementato, usare `--accept --note` soltanto dopo il ritorno JSON `gate-not-implemented` e con nota fondata sulle evidenze.

## Gestione degli errori

- Se il Book Studio non raggiunge uno stato stabile, l'auditor fallisce senza produrre un report conforme.
- Se il numero di pagine cambia durante la sessione, l'audit viene invalidato e ripetuto.
- Se una tavola-contatto non contiene la sequenza attesa, l'esecuzione fallisce.
- Se un'immagine non si carica, l'errore resta bloccante anche quando la pagina non va in overflow.
- Se una correzione cambia il numero totale di pagine, vengono rigenerate tutte le tavole e ricontrollata l'intera sequenza.
- Il server temporaneo viene arrestato in ogni percorso di uscita.

## Test

### Test delle regole pure

- overflow e collisioni diventano bloccanti;
- numero pagina errato diventa bloccante;
- heading orfano diventa bloccante;
- frammento di paragrafo con meno di tre righe diventa significativo;
- pagina interna quasi vuota viene segnalata;
- pagina terminale o frontespizio con lo stesso vuoto non viene segnalata;
- immagine rotta e pipe Markdown diventano bloccanti;
- una pagina conforme produce una riga `conforme`.

### Test di integrazione

- lo script risolve il book ID, il prefisso artefatti e il percorso report;
- le 381 pagine producono 381 righe nel registro;
- 20 tavole coprono esattamente le pagine 1–381 senza duplicati o salti;
- i conteggi del registro coincidono con il DOM;
- nessun deliverable PDF viene creato.

### Verifica finale

- typecheck exit 0;
- suite completa verde;
- audit Playwright exit 0;
- numero di righe pagina uguale al conteggio finale del DOM, atteso 381 se la paginazione resta invariata;
- `ceil(pageCount / 20)` tavole-contatto ispezionate, attese 20 se la paginazione resta invariata;
- zero problemi bloccanti o significativi irrisolti;
- zero overflow, collisioni, asset mancanti o residui Markdown;
- numerazione completa da 1 a `pageCount`;
- report senza placeholder;
- pipeline con step 20 completato e prossimo step 21.

## Criteri di completamento

Lo step 20 è completabile soltanto quando ogni pagina compare nel registro, ogni tavola è stata ispezionata, tutte le anomalie hanno correzione ed esito, le pagine impattate sono state ricontrollate, l'audit completo finale è verde e il gate manuale viene accettato con una nota verificabile. Le tavole-contatto e il report restano evidenze dello step; non sostituiscono la revisione editoriale totale dello step 21.
