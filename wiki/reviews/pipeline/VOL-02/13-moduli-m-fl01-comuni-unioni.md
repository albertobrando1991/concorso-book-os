# Report editoriale — M-FL01 Comuni e Unioni

## 1. Sintesi editoriale

- Genere editoriale: modulo specialistico e workbook per concorsi comunali.
- Pubblico target: candidati a profili amministrativi, contabili, tecnico-amministrativi e di servizi locali.
- Perimetro di questa revisione: indice, piano, matrice e quattordici capitoli dichiarati.
- Stato generale in una frase: progressione, copertura e autonomia del lettore sono coerenti dopo la correzione tracciata dei residui legacy nei capitoli 01-07.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30 ai file Markdown: indice, struttura, progressione, gerarchia, coerenza interna e trasversale, terminologia, completezza, definizioni, contenuti, casi, tabelle, riferimenti normativi, sintassi, chiarezza, tono, didattica, ripetizioni, contraddizioni, grammatica, ortografia, punteggiatura, refusi, uniformità grafica, layout testuale e leggibilità. Applicato il gate di copertura v4 confrontando matrice e capitoli. Il punto 27 non è applicabile perché non è disponibile un PDF impaginato del modulo.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Capitoli 01-07, corpo | Autonomia didattica e struttura | Grave | I sette capitoli legacy esponevano involucri e wikilink editoriali. | Involucri archiviati in `wiki/reviews/retrofit/m-fl01-comuni-unioni/`; testo lettore promosso e riferimenti convertiti in forma leggibile. | Chiuso |
| E02 | Indice, `Capitoli di lavoro` e `Note di review` | Indice e navigazione | Media | L'elenco includeva il piano e la nota finale era obsoleta. | Piano rimosso dall'indice studente; nota aggiornata. | Chiuso |
| E03 | Indice, piano e frontmatter capitoli | Coerenza metadati | Media | Gli stati del modulo non riflettevano la revisione trasversale. | Indice e piano aggiornati; `review_required` resta attivo sui capitoli fino all'audit. | Chiuso |
| E04 | Matrice, `Esito del gate` | Coerenza documentale | Lieve | La chiusa dichiarava righe parziali inesistenti. | Esito aggiornato a tutte le righe didattiche complete. | Chiuso |

## 4. Osservazioni per capitolo

### Capitoli 01-03 — Ente, fonti e organizzazione

- Punti di forza: costruiscono correttamente la progressione Comune/Unione, autonomia normativa, organi, uffici e gestioni associate.
- Criticità: E01 risolta; materiale interno archiviato fuori dal corpo.

### Capitoli 04-06 — Atti, procedimento e digitale

- Punti di forza: collegano competenza, atto, istruttoria, fascicolo e servizio digitale senza contraddizioni sostanziali.
- Criticità: E01 risolta; riferimenti interni e note di review rimossi dal corpo.

### Capitolo 07 — Servizi demografici ed elettorali

- Punti di forza: distingue anagrafe, stato civile ed elettorale e li raccorda con ANPR, documentazione e protezione dati.
- Criticità: E01 risolta; il capitolo ora espone soltanto materiale destinato al lettore.

### Capitoli 08-09 — Servizi alla persona e programmazione

- Punti di forza: nuclei in Formato 2, teoria prima dei casi e chiaro collegamento tra servizi, obiettivi, risorse e responsabilità.
- Criticità: nessuna trasversale certa; materie normative assegnate allo step 15.

### Capitoli 10-11 — Gestione finanziaria, entrate e patrimonio

- Punti di forza: distinguono programmazione, gestione, rendiconto, entrate, inventario ed economato; i raccordi sono funzionali e non duplicativi.
- Criticità: nessuna trasversale certa.

### Capitoli 12-13 — Procurement e territorio

- Punti di forza: mantengono il perimetro operativo comunale e rinviano agli specialistici per gli approfondimenti avanzati.
- Criticità: nessuna trasversale certa; i rinvii devono essere ricontrollati dal gate automatico.

### Capitolo 14 — Laboratorio per profili

- Punti di forza: ricompone i tredici capitoli in quattro profili, cinque simulazioni, griglia e diario errori; non introduce una nuova materia.
- Criticità: nessuna.

## 5. Coerenza globale

- Terminologia: coerente nei concetti centrali; la Bibbia del Modulo fissa le forme preferite per Comune, Unione, organo, responsabile, atti, procedimento, SUAP/SUE e RUP.
- Struttura vs indice: i quattordici file e i quattordici capitoli coincidono; E02 riguarda soltanto la commistione con il piano staff.
- Promesse dell'introduzione mantenute: sì sul piano sostanziale. Ordinamento, fonti locali, organizzazione, atti, procedimenti, servizi, risorse e simulazioni sono sviluppati.
- Ripetizioni: politica/gestione, competenza, fascicolo e controllo ricorrono con applicazioni diverse; non emergono contraddizioni sostanziali.
- Copertura v4: il delta locale è presente; procurement, vigilanza e territorio avanzati restano nei moduli specialistici indicati.

## 6. Contenuto da verificare

- TUEL e riparto aggiornato delle competenze locali.
- Procedimento, accesso, trasparenza e protezione dati.
- CAD, ANPR/ANSC e servizi demografici.
- Welfare, ISEE e servizi educativi.
- Ordinamento finanziario, entrate, patrimonio ed economato.
- Contratti pubblici, digitalizzazione, MEPA, CIG e fase esecutiva.
- SUAP, SUE, edilizia e vigilanza nel solo perimetro amministrativo.

Queste aree appartengono all'audit automatico dello step 15 e non sostituiscono la correzione editoriale E01-E04.

## 7. Suggerimenti facoltativi (non errori)

In impaginazione si può assegnare un segno grafico ricorrente ai quattro profili del laboratorio, purché resti leggibile in bianco e nero.

## 8. Priorità degli interventi

1. Rieseguire lint, controllo link e copertura sul modulo corretto.
2. Eseguire l'audit specialistico automatico dello step 15.
3. Controllare tabelle e apparati nel preflight.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori: nessuna correzione editoriale residua identificata.** E01-E04 sono chiusi e verificabili nei file; restano gli audit automatici, il freeze e il preflight previsti dalla pipeline prima della pubblicazione finale.

## 10. Limiti di questa revisione

La revisione riguarda Markdown, indice, piano e matrice. Non è stato ispezionato un PDF impaginato. La validità normativa puntuale sarà verificata dallo step 15 automatico; la conferma umana resta allo step 24 sul pacchetto completo.
