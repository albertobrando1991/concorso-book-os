# VOL-07 — Avvio progressivo della fase C per M-SA01

## Obiettivo

Correggere lo stato obsoleto mostrato dalla dashboard e abilitare la scrittura
dei cinque capitoli M-SA01 già previsti dalla matrice di copertura. I target
vengono dichiarati insieme nella scheda di volume, ma il protocollo 08-12 viene
eseguito in ordine, un capitolo alla volta, iniziando dal capitolo 04.

## Diagnosi

Lo step 07 di `moduli/m-sa01-sanita-amministrativa` risulta `done` nel
run-state e la matrice M-SA01 contiene 8 nuclei `completo`, senza blocker di
copertura preparatoria. La dashboard mostra comunque “Non avviato” perché:

1. `chapters/00-piano-editoriale.md` e l'indice del modulo contengono ancora il
   testo precedente al completamento dello step 07;
2. la scheda di pipeline assegna a M-SA01 soltanto le fasi A e B;
3. nessun capitolo M-SA01 è dichiarato nella scheda, quindi il CLI non genera
   lo step 08.

La correzione deve agire sulle fonti canoniche, non sulla sola resa della
dashboard.

## Capitoli da attivare

| Ordine | File | Nuclei assegnati |
| --- | --- | --- |
| 1 | `chapters/04-atti-procedimenti-flussi-informativi.md` | Atti e procedimenti delle aziende sanitarie; flussi informativi sanitari |
| 2 | `chapters/05-documentazione-accesso-conservazione.md` | Documentazione sanitaria; accesso; privacy; FSE; dossier; conservazione |
| 3 | `chapters/06-front-office-comunicazione-utenza.md` | Front-office, comunicazione istituzionale, reclami, accessibilità e riservatezza |
| 4 | `chapters/09-contabilita-budget-controllo-gestione.md` | Contabilità economico-patrimoniale, budget, reporting e controllo di gestione |
| 5 | `chapters/10-procurement-farmaci-dispositivi-magazzino.md` | Procurement sanitario, farmaci, dispositivi, magazzino e ciclo passivo |

La numerazione segue le destinazioni già fissate nella matrice M-SA01. Non
vengono creati capitoli riempitivi per i numeri non assegnati.

## Modifiche dichiarative

La scheda VOL-07:

- abilita M-SA01 alle fasi `A,B,C`;
- aggiunge una tabella esplicita con i cinque capitoli nell'ordine sopra;
- dichiara che la fase C procede progressivamente e che le review normative,
  contabili, privacy e procurement dello step 15 restano obbligatorie.

Il test della specifica deve verificare i cinque percorsi, il loro ordine, la
matrice associata e l'abilitazione della fase C.

## Sincronizzazione dello stato

Il run-state non viene modificato a mano. Dopo la validazione della scheda si
esegue:

```text
npm run pipeline -- sync VOL-07 --json
```

La sincronizzazione è accettabile soltanto se:

- preserva tutti gli step già conclusi;
- non rimuove alcuna chiave;
- aggiunge esattamente i cinque step 08-12 per ciascuno dei cinque capitoli
  M-SA01;
- indica come prossimo target lo step 08 del capitolo 04.

Qualunque differenza diversa interrompe l'avanzamento e richiede una nuova
diagnosi.

## Stato editoriale e dashboard

L'indice M-SA01 e `00-piano-editoriale.md` passano da “source audit complete /
non avviato” a “ready for writing / scrittura autorizzata”. Il testo deve
distinguere con precisione:

- step 07 superato;
- cinque capitoli autorizzati alla fase C;
- primo target: piano del capitolo 04;
- nessun capitolo M-SA01 ancora dichiarato scritto o pubblicabile.

La dashboard continuerà a leggere i file canonici e mostrerà quindi lo stato
corretto senza introdurre una seconda fonte di verità.

## Primo ciclo editoriale

Dopo la sincronizzazione si esegue il ciclo CLI sul capitolo 04:

1. `next --json` genera il contratto dello step 08;
2. si redige il piano capitolo collegando ogni nucleo a teoria, applicazione,
   output, verifica, fonti e review;
3. lo step 08 viene chiuso solo dopo verifica manuale documentata, perché il
   gate `chapter-plan` non è automatizzato;
4. lo step 09 usa `concorso-book-professional-writer` e produce il testo
   autosufficiente per lo studente;
5. il nuovo `chapter-lint` deve passare senza dipendenze da wiki o source note
   nel corpo.

I capitoli successivi restano ordinati dal CLI e non vengono anticipati.

## Criteri di accettazione

- La scheda dichiara M-SA01 in fase C con esattamente cinque capitoli.
- I test della specifica e della costruzione degli step passano.
- `pipeline sync --json` aggiunge 25 step, ne rimuove zero e preserva lo stato
  esistente.
- La dashboard non mostra più il messaggio obsoleto “Non avviato”.
- `pipeline next --json` restituisce lo step 08 del capitolo 04.
- Nessun run-state è modificato manualmente.
- Nessun capitolo viene definito completo prima del relativo ciclo 08-12.
- Le review specialistiche dello step 15 restano esplicitamente aperte.

## Vincoli

- Nessun commit o push in questa fase senza autorizzazione esplicita.
- Nessun salto o accettazione fittizia di gate.
- Nessuna norma, procedura locale o dato mobile viene inventato.
- Le modifiche non pertinenti già presenti nella worktree vengono preservate.
