# VOL-07 — Estensione progressiva M-SA02 al capitolo 03

## Stato di partenza

Il run VOL-07 ha concluso i 22 step dichiarati nelle fasi A, B e C. Il capitolo 01 M-SA02 ha completato il ciclo 08-12; `pipeline status` e `pipeline next` non presentano blocker né nuovi step perché la scheda dichiara soltanto quel capitolo.

## Decisione approvata

La fase C viene estesa a un solo nuovo target:

- modulo: `M-SA02`;
- capitolo: `chapters/03-discipline-professionali-autonomia-responsabilita.md`;
- titolo editoriale: `Discipline professionali: autonomia, responsabilità e deontologia`;
- matrice: `planning/02-matrice-copertura-didattica.md`;
- nucleo assegnato: `Discipline professionali specifiche`;
- stato di copertura richiesto: `completo`.

La numerazione segue la collocazione già stabilita nella matrice (`cap. 03`). Non viene creato un capitolo 02 in questo ciclo: il nucleo comune del Metodo BANDO resta nel VOL-01 e non deve essere duplicato.

## Modifica della specifica

La scheda VOL-07 continua a dichiarare:

- fasi globali `[A, B, C]`;
- M-SA02 in `A,B,C`;
- M-SA01, M-SA03 e M-SA04 in `A,B`.

Nella tabella `Capitoli M-SA02` viene aggiunta soltanto la riga 03. Il test della specifica deve aspettarsi esattamente i capitoli 01 e 03.

## Flusso CLI

1. Aggiornare test e scheda con TDD.
2. Eseguire `pipeline sync VOL-07 --json`.
3. Verificare che `sync` aggiunga esattamente le cinque chiavi 08-12 del capitolo 03, senza `dropped`.
4. Usare il ciclo canonico `next → lavoro → gate → complete`.
5. Fermarsi dopo lo step 12 del capitolo 03.

Il file `pipeline/VOL-07/run-state.json` non viene mai modificato manualmente.

## Contenuto del capitolo

Il capitolo applica il Metodo BANDO alle discipline professionali specifiche di infermiere, ostetrica, fisioterapista, TPALL e OSS, distinguendo:

- fonte del profilo e campo professionale;
- autonomia, responsabilità e limiti;
- deontologia e collaborazione multiprofessionale;
- differenza fra professioni sanitarie ordinistiche e OSS;
- output concorsuali: confronto, domanda orale e caso deontologico;
- informazioni che dipendono dal bando, dal setting o dalla review professionale.

Non contiene procedure cliniche esecutive, attribuzioni inventate o duplicazioni delle materie comuni del VOL-01.

## Gate e skill

- Step 08: piano del capitolo, verifica manuale e chiusura motivata se il gate resta non automatizzato.
- Step 09: scrittura con `concorso-book-professional-writer`.
- Step 10: copertura didattica sulla riga `cap. 03`.
- Step 11: revisione con `humanizer`.
- Step 12: revisione con `revisore-editoriale-totale`.

Le cinque review professionali esterne restano differite allo step 15 e non vengono simulate.

## Verifica

Prima di chiudere il ciclo:

- test della specifica e dei build-step;
- gate 07 M-SA02 ancora verde;
- cinque nuovi step soltanto per il capitolo 03;
- test mirati, suite e typecheck;
- `git diff --check`;
- stato pipeline senza blocker;
- traccia sintetica tramite `LocalAgentMemory`.

## Vincoli

- Nessuna fase D, E o F.
- Nessun altro capitolo dichiarato.
- Nessun commit intermedio: consegna e commit restano riservati allo step 23.
- Conservare tutte le modifiche già presenti nel worktree condiviso.
