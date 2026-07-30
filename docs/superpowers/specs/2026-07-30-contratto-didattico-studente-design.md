# Contratto didattico dello studente — Design

## Obiettivo canonico

Ogni capitolo deve essere un testo didattico autosufficiente, destinato allo
studente che prepara un concorso pubblico e non dispone della wiki, della
dashboard o delle note editoriali interne. Deve trasmettere integralmente le
conoscenze assegnate al modulo e permettere di comprenderle, memorizzarle e
applicarle nelle prove concorsuali.

## Problema

Il prompt dello step 09 richiede già il testo destinato al lettore, ma il gate
automatico controlla soltanto forma, frontmatter, segnaposto e meta-commenti.
Di conseguenza può passare un capitolo che rinvia ripetutamente a source note,
corpus o fonti consolidate non disponibili al lettore.

Lo step 11 protegge inoltre tutti i wikilink del corpo come se fossero
citazioni destinate alla pubblicazione. Questa regola rende permanenti anche i
collegamenti interni `[[sources/...]]`, che appartengono invece alla
tracciabilità editoriale.

## Contratto del capitolo

Un capitolo supera lo step 09 solo se:

1. è leggibile senza wiki, dashboard, source note o documenti di lavorazione;
2. conserva `source_refs` e `last_compiled_from` nel frontmatter;
3. non espone nel corpo wikilink verso `sources/`, `topics/` o `entities/`;
4. non usa il lessico redazionale interno come sostituto della spiegazione;
5. presenta obiettivo didattico, Mappa BANDO, teoria progressiva, applicazione,
   errore tipico e verifica dell'apprendimento;
6. esprime nel corpo i riferimenti normativi o professionali necessari in
   forma leggibile per lo studente;
7. spiega ogni nucleo assegnato dalla matrice secondo il gate di copertura
   integrale.

I link editoriali interni restano ammessi nel frontmatter, nei report di
review, nelle matrici e nei piani. Nel corpo del libro sono ammessi link
editoriali verso altri capitoli della collana quando costituiscono un rinvio
didattico preciso e la destinazione è completa.

## Modifiche alla pipeline

### Step 09

Il `chapter-lint` diventa anche gate del contratto dello studente. Blocca:

- wikilink interni di conoscenza nel corpo;
- formule redazionali che chiedono al lettore di affidarsi a source note,
  corpus auditati o fonti consolidate;
- assenza delle evidenze didattiche minime.

Il controllo delle evidenze usa famiglie di heading equivalenti, non titoli
rigidi, così i capitoli conservano una voce editoriale naturale.

### Step 10

Il prompt rende esplicito che un riferimento alla fonte o a un altro materiale
non prova la copertura. Ogni riga della matrice deve essere insegnata nel testo
o rinviata a una destinazione editoriale completa e accessibile allo studente.

### Step 11

Il `citation-guard` continua a proteggere:

- `source_refs` del frontmatter;
- riferimenti normativi del corpo;
- wikilink didattici verso capitoli pubblicabili.

Non protegge i wikilink interni verso `sources/`, `topics/` ed `entities/`,
perché la loro rimozione dal corpo è una correzione editoriale ammessa. Se
l'Humanizer ne introduce di nuovi, il gate li blocca.

### Step 12

La revisione esegue il test dello studente: il capitolo, considerato senza
frontmatter e senza accesso al wiki, deve restare completo, comprensibile e
utilizzabile per la prova.

## Riscrittura retroattiva

Nel modulo M-SA02 i due capitoli attualmente visibili sono:

- `01-mappa-profili-e-prove.md`;
- `03-discipline-professionali-autonomia-responsabilita.md`.

Entrambi manterranno la tracciabilità nel frontmatter. Il corpo sarà ripulito
da collegamenti e formule interne; i riferimenti finali saranno presentati con
denominazioni normative e professionali leggibili. Il capitolo 03 richiede la
correzione più estesa; il capitolo 01 richiede un audit e correzioni mirate.

## Criteri di accettazione

- Un capitolo esemplificativo completo e autosufficiente supera
  `chapter-lint`.
- Un capitolo che contiene `[[sources/...]]` nel corpo viene bloccato.
- Un capitolo che usa “source note consolidata” come destinazione didattica
  viene bloccato.
- Un capitolo privo di obiettivo, Mappa BANDO, applicazione, errore o verifica
  viene bloccato con codici diagnostici specifici.
- Il `citation-guard` consente la rimozione dei link interni di conoscenza,
  conserva i rinvii didattici e blocca nuovi link interni.
- I capitoli M-SA02 01 e 03 superano il nuovo gate.
- Test completi e typecheck restano verdi.
