# Copertura didattica integrale — Specifica globale

## Decisione

ConcorsoBook OS adotta come regola globale la copertura didattica integrale. Il Metodo BANDO organizza, seleziona e rende operativa la teoria richiesta dai concorsi, ma non la sostituisce.

Ogni materia assegnata a un volume o modulo deve essere realmente insegnata con profondità proporzionata al profilo e al bando. Non è sufficiente dichiarare che il candidato deve conoscere, riconoscere o distinguere un concetto: il contenuto deve spiegarlo oppure rinviare in modo esplicito e preciso a una spiegazione completa già presente nel sistema editoriale.

## Obiettivi vincolanti

Ogni volume, modulo e capitolo deve assicurare:

- progressione logica;
- completezza delle spiegazioni;
- accuratezza e funzione delle definizioni;
- autonomia didattica del capitolo, nei limiti dei rinvii dichiarati;
- coerenza tra promessa formativa e contenuto effettivo;
- presenza di esempi, casi e strumenti operativi;
- copertura teorica dei concetti richiesti dal perimetro editoriale;
- tracciabilità alle fonti consolidate;
- revisione normativa prima della pubblicazione.

## Unità minima di copertura

Per ogni concetto richiesto, il testo deve coprire, quando applicabile:

```text
definizione
-> funzione
-> inquadramento teorico e normativo
-> elementi costitutivi
-> distinzioni da concetti vicini
-> conseguenze applicative
-> esempio o caso
-> modalità d'esame
-> errore tipico
-> verifica dell'apprendimento
-> riferimenti consolidati
```

La profondità varia in base a famiglia, profilo, frequenza nei bandi e peso in prova. La variazione di profondità non autorizza l'omissione dei nuclei necessari alla comprensione.

## Regola dei rinvii

Un rinvio è valido solo se:

- indica un volume, capitolo o paragrafo preciso;
- la destinazione contiene una spiegazione effettiva e aggiornata;
- il capitolo conserva il contesto minimo necessario per comprendere il rinvio;
- il rinvio rispetta la logica di non duplicazione tra volume base, specialistico e verticale.

Formule generiche come “si rinvia al volume base” non soddisfano il gate.

## Matrice didattica obbligatoria

Ogni volume e modulo deve possedere una matrice con almeno questi campi:

| Campo | Funzione |
| --- | --- |
| Famiglia e profilo | Identifica il destinatario concorsuale. |
| Materia | Collega il contenuto al perimetro del volume. |
| Concetto e sotto-concetti | Rende verificabile la granularità della copertura. |
| Frequenza/peso | Regola la profondità sulla base dei bandi consolidati. |
| Fonti consolidate | Indica source, topic ed entity pages utilizzabili. |
| Collocazione | Identifica volume, capitolo e paragrafo responsabili. |
| Copertura teorica | Verifica definizione, funzione, disciplina e distinzioni. |
| Applicazione | Verifica esempio, caso o conseguenza pratica. |
| Output concorsuale | Verifica quiz, orale, scritto o prova situazionale. |
| Verifica apprendimento | Indica esercizio, domanda o checkpoint. |
| Stato | `completo`, `parziale`, `solo-nominato`, `rinviato`, `mancante`. |
| Review normativa | Registra fonte vigente, data e necessità di controllo umano. |

Gli stati `solo-nominato` e `mancante` sono bloccanti. Lo stato `rinviato` è accettabile soltanto se supera la regola dei rinvii. Lo stato `parziale` richiede integrazione prima della pubblicazione.

## Governance da aggiornare

La regola deve essere incorporata in:

1. `wiki/AGENTS.md`, come principio non negoziabile per tutti gli agenti;
2. `.agents/skills/concorso-book-professional-writer/SKILL.md`, come procedura di scrittura e gate;
3. `.agents/skills/revisore-editoriale-totale/SKILL.md` e relativa checklist, come controllo bloccante;
4. `wiki/books/moduli/architettura-moduli-specialistici.md`, come regola di architettura;
5. una nuova source note canonica che consolidi la decisione editoriale;
6. topic e template necessari per rendere la matrice riusabile.

## Audit retroattivo

L'audit copre l'intero catalogo canonico:

- 12 volumi commerciali;
- 25 moduli specialistici;
- volume base e ricettario digitale;
- appendici e verticali già presenti;
- capitoli in stato `source_ready`, `draft`, `revised_draft` o equivalente.

L'audit procede in due passaggi.

### Passaggio 1 — Inventario globale

- censire volumi, moduli, capitoli, stato e dimensione;
- collegare le materie alle schede di copertura e ai bandi consolidati;
- rilevare capitoli mancanti, placeholder e contenuti soltanto predisposti;
- produrre una dashboard globale dei gap.

### Passaggio 2 — Audit semantico per volume

- estrarre le promesse formative;
- confrontarle con spiegazioni, esempi e verifiche realmente presenti;
- classificare ciascun nucleo nella matrice;
- produrre un report di gap per volume e modulo;
- ordinare gli interventi per gravità, frequenza e peso concorsuale.

## Integrazione editoriale

L'integrazione avviene volume per volume. Per ogni gap:

1. verificare se le fonti ufficiali sono già in `wiki/raw/`;
2. creare o aggiornare le source notes consolidate;
3. aggiornare topic ed entity pages;
4. definire la collocazione senza duplicazioni improprie;
5. scrivere o integrare la spiegazione teorica;
6. aggiungere esempi, casi e strumenti di verifica;
7. aggiornare la matrice;
8. eseguire review normativa ed editoriale.

Le fonti raw non alimentano direttamente il testo finale. Ogni informazione deve passare per il wiki consolidato.

## Gate di pubblicazione

Un capitolo non può essere dichiarato completo se:

- contiene promesse formative non mantenute;
- usa concetti necessari senza definirli o rinviarli correttamente;
- ha nuclei `solo-nominato`, `mancante` o `parziale` nella matrice;
- non offre almeno una verifica dell'apprendimento per i nuclei principali;
- dipende da norme mobili non sottoposte a review aggiornata;
- presenta rinvii generici o destinazioni incomplete;
- non è comprensibile al candidato che studia autonomamente.

La lunghezza del capitolo non dimostra la completezza. Il gate valuta la corrispondenza tra perimetro richiesto, concetti insegnati e capacità verificabili.

## Strategia di esecuzione

L'implementazione è progressiva e non dichiara concluso l'intero livello 3 dopo il solo censimento:

1. governance e template;
2. inventario dei 12 volumi e 25 moduli;
3. audit semantico prioritario dei contenuti esistenti;
4. integrazione volume per volume;
5. revisione normativa;
6. gate editoriale finale;
7. commit organizzati e pubblicazione su GitHub.

Il primo audit pilota sarà applicato a M-FC02 e VOL-03, perché possiedono capitoli già sviluppati, fonti consolidate e gap didattici identificati. Il metodo validato sarà poi esteso all'intero catalogo.

## Allineamento GitHub

Alla data della decisione:

- il checkout locale include integralmente `origin/main`;
- il branch locale è avanti rispetto al remoto;
- la working tree contiene modifiche e file non ancora versionati.

Prima della pubblicazione:

- preservare tutte le modifiche preesistenti;
- separare i commit per governance, audit, integrazioni e artefatti;
- eseguire test e controlli editoriali;
- aggiornare `main` soltanto con flusso non distruttivo;
- pubblicare su GitHub e fornire allo staff istruzioni di allineamento.

## Criteri di riuscita

Il livello 3 è realmente adottato quando:

- la regola è persistente nelle istruzioni e nelle skill;
- ogni volume/modulo possiede una matrice;
- l'inventario globale è completo;
- ogni contenuto esistente è stato classificato;
- tutti i gap bloccanti sono chiusi o esplicitamente mantenuti in stato non pubblicabile;
- i capitoli pubblicabili superano copertura didattica, review normativa e revisione editoriale;
- il repository GitHub contiene gli artefatti e lo staff può riallinearsi senza perdere lavoro.
