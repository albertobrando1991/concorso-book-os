from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-project-management-esempi-2026-10-03.md'
slug='13-project-management-pubblico';t=u.read(slug)
t=t.replace('| Risultato atteso | Descrive il prodotto finale verificabile. | Confondere il risultato con una generica attività. |','| Output e cambiamento atteso | Distingue prodotto consegnato, uso effettivo e beneficio misurabile. | Scambiare il collaudo del prodotto con la prova del beneficio. |')
t=t.replace("La Work Breakdown Structure, o WBS, scompone il risultato in parti gestibili.","La Work Breakdown Structure, o WBS, scompone il lavoro necessario al progetto in parti gestibili. In questo volume adottiamo una struttura organizzata per deliverable e, al livello inferiore, per pacchetti di lavoro. Altre convenzioni possono organizzare la WBS per fasi o unità: ciò che conta è una scomposizione completa del lavoro, non un semplice organigramma.")
t=t.replace('## N-TR02-13-02 · ▣ Verifica N-TR02-13-02 - Mandato, WBS e baseline','## N-TR02-13-02 · Pianificazione, dipendenze e baseline')
t=t.replace('non si forma il personale su una procedura ancora instabile','la formazione pratica richiede un ambiente sufficientemente stabile, ma può procedere in parallelo ad alcuni test se i vincoli lo consentono')
t=t.replace('- [ ] Il risultato atteso è descritto come prodotto verificabile.','- [ ] Sono distinti output consegnato, outcome atteso e beneficio misurabile.')
t=t.replace('Consegna: il Gantt prevede formazione del personale prima del completamento dei test. Individua il problema e proponi una correzione.','Consegna: il contratto di questo caso richiede che la formazione sulla procedura definitiva inizi soltanto dopo il verbale positivo dei test. Il Gantt anticipa quella formazione ai test. Individua il problema e correggi la dipendenza.')
t=t.replace("Schema di risposta: spiegare la dipendenza logica tra test e formazione, proporre lo spostamento della formazione dopo la stabilizzazione del servizio, verificare impatto su data finale e comunicare la modifica se incide sulla baseline.","Soluzione: in questo caso il vincolo contrattuale impone test → formazione. Si sposta la formazione dopo il verbale positivo, si ricalcola la data finale e si sottopone l’eventuale variazione al livello competente. Una formazione generale o su ambiente già stabile potrebbe invece svolgersi prima della fine di tutti i test se gli atti lo ammettono, come nel laboratorio numerico di questo capitolo. L’errore è violare la dipendenza dichiarata, non anticipare sempre e comunque la formazione.")
anchor='### WBS, Gantt e baseline'
t=t.replace(anchor,'''### Output, outcome e beneficio: tre verifiche diverse

Nel metodo PM² della Commissione europea, l’output è il prodotto o servizio consegnato; l’outcome è il cambiamento che il suo utilizzo produce; il beneficio è il miglioramento misurabile conseguente. Uno sportello digitale collaudato è un output. L’uso effettivo dello sportello da parte di cittadini e uffici è un outcome. La riduzione del tempo medio di trattamento delle pratiche è un beneficio.

Il charter può fissare un obiettivo didattico di riduzione da 20 a 12 minuti per pratica, cioè 8 minuti e il 40%, da misurare dopo tre mesi su campioni comparabili. Il verbale di collaudo non dimostra da solo tale riduzione: occorrono dati di utilizzo e di processo. La chiusura del progetto può precedere la misurazione dei benefici, purché responsabilità e rilevazione successiva siano assegnate.

'''+anchor)
anchor='### Checklist operativa'
t=t.replace(anchor,'''### Soluzione completa: sportello digitale in nove giorni

Il progetto è un esempio didattico circoscritto: si assume già disponibile il contratto necessario. Inizia martedì 6 ottobre 2026; si lavora dal lunedì al venerdì, senza altre chiusure nel periodo. Tutte le dipendenze sono fine-inizio, senza tempi di attesa aggiuntivi. Le attività parallele dispongono di persone distinte. Durata e risorse sono ipotesi del caso, non standard per un vero progetto informatico.

Il livello 1 della WBS è **1 — Sportello digitale pronto all’uso**. Il livello 2 ha tre deliverable: **1.1 Soluzione configurata**, **1.2 Dati e verifica**, **1.3 Adozione e avvio**. Il terzo livello comprende i sei pacchetti seguenti.

| Pacchetto e lavoro | Responsabile | Evidenza e accettazione |
| --- | --- | --- |
| 1.1.1 — A: definizione requisiti | Responsabile del servizio | Specifica approvata; copertura delle funzioni richieste. |
| 1.1.2 — B: configurazione ambiente | Tecnico del fornitore | Registro di configurazione; ambiente stabile disponibile. |
| 1.2.1 — C: bonifica dati | Referente dati dell’ente | Rapporto anomalie; record del campione coerenti con le regole definite. |
| 1.2.2 — D: caricamento e test | Gruppo di verifica | Report di prova; tutti i test obbligatori del caso superati. |
| 1.3.1 — E: manuale e formazione | Referente formazione | Manuale validato, presenze ed esercitazione completata. |
| 1.3.2 — F: accettazione e avvio | Responsabile del servizio | Verbale di accettazione e consegna alla gestione ordinaria. |

Le evidenze non sono ulteriori livelli WBS: sono criteri associati ai pacchetti. Le lettere A–F identificano le attività nel calendario; i codici 1.1.1 ecc. ne mostrano la gerarchia. Tutto il perimetro dichiarato è coperto, senza contare due volte lo stesso lavoro.

| Attività | Durata lavorativa | Predecessori | Date di esecuzione |
| --- | --- | --- | --- |
| A | 2 giorni | Nessuno | 6–7 ottobre |
| B | 4 giorni | A | 8–13 ottobre |
| C | 3 giorni | A | 8–12 ottobre |
| D | 2 giorni | B e C | 14–15 ottobre |
| E | 1 giorno | B | 14 ottobre |
| F | 1 giorno | D ed E | 16 ottobre |

E può sovrapporsi a D perché la formazione usa l’ambiente stabile disponibile dopo B; l’avvio F attende invece sia test sia formazione. Se fosse necessaria la conclusione dei test prima della formazione, andrebbe dichiarata anche D come predecessore di E e il piano cambierebbe.

![Gantt originale dello sportello digitale, attività A–F e percorso critico](books/moduli/m-tr02-appalti-pnrr-fondi-ue/assets/correzioni-2026-10/gantt-sportello-digitale.png)

*Figura — Le colonne rappresentano giorni lavorativi, non tutti i giorni del calendario. A–F corrispondono alla tabella precedente; nero indica il percorso critico, grigio le attività con un giorno di margine.*

### Calcolo del percorso critico e dei margini

Il metodo del percorso critico cerca il cammino di **durata maggiore** fra inizio e fine nella rete delle dipendenze. Questo cammino determina la minima durata possibile del progetto nelle ipotesi dichiarate. Non si sommano tutte le attività, perché alcune si svolgono in parallelo.

Usiamo un asse di tempi lavorativi con inizio uguale a 0. Il più presto inizio, ES, di ogni attività è il massimo delle fini dei predecessori; la più presto fine, EF, è ES più durata. Partendo dalla fine si calcolano LF, più tardi fine senza ritardare il progetto, e LS = LF − durata. Il margine totale è LS − ES.

| Attività | ES → EF | LS → LF | Margine totale |
| --- | --- | --- | --- |
| A | 0 → 2 | 0 → 2 | 0 giorni |
| B | 2 → 6 | 2 → 6 | 0 giorni |
| C | 2 → 5 | 3 → 6 | 1 giorno |
| D | 6 → 8 | 6 → 8 | 0 giorni |
| E | 6 → 7 | 7 → 8 | 1 giorno |
| F | 8 → 9 | 8 → 9 | 0 giorni |

D attende il massimo fra EF di B, pari a 6, ed EF di C, pari a 5: parte a 6. F attende il massimo fra 8 e 7: parte a 8. Il percorso critico **A–B–D–F** dura 2 + 4 + 2 + 1 = **9 giorni lavorativi**. A–C–D–F e A–B–E–F durano entrambi 8. La somma di tutte le durate, 13 giorni, non è la durata del progetto.

Il margine non è una riserva indipendente spendibile più volte: dopo un ritardo va ricalcolata l’intera rete. Se C passa da 3 a 4 giorni, consuma il proprio margine e la fine resta il 16 ottobre; nasce un ulteriore percorso critico. Se C passa a 5 giorni, D parte un giorno dopo, il progetto dura 10 giorni e finisce lunedì 19 ottobre. Se B dura invece 6 giorni, il progetto dura 11 giorni e termina martedì 20 ottobre. Questi confronti mostrano quali azioni di recupero incidono sulla data finale.

### Registro rischi, issue e decisione: esempio compilato

**Rischio R1.** Causa: regole di qualità dei dati non condivise. Evento: la bonifica C potrebbe richiedere più di tre giorni. Effetto: oltre un giorno aggiuntivo, ritardo dell’avvio. Responsabile: referente dati. Risposta: campione preliminare e validazione delle regole durante A. Segnale: anomalie irrisolte alla fine del secondo giorno di C. Probabilità e impatto sono valutati con la scala adottata dall’ente; non si inventa una percentuale senza dati.

**Issue I1, 12 ottobre.** Il campione presenta anomalie e C richiederà cinque giorni complessivi. Stato: problema già accaduto, non semplice rischio. Previsione senza recupero: fine 19 ottobre. Azione proposta: affiancare un secondo addetto alla bonifica, previa disponibilità autorizzata, e verificare entro la giornata se la durata può scendere a quattro giorni. L’aggiunta di una persona non dimezza automaticamente i tempi: si controllano attività divisibili e costi.

**Nota al dirigente.** «La bonifica dati richiede due giorni aggiuntivi rispetto alla baseline. Un giorno è assorbito dal margine, l’altro sposta l’avvio al 19 ottobre. Propongo un affiancamento autorizzato e una verifica di recupero entro oggi; in alternativa occorre approvare il nuovo calendario e informare gli utenti. Non modifico il contratto con il solo Gantt. Conservo baseline, issue, decisione e report aggiornato».

**Verifica.** Quale attività è utile accelerare se C resta di tre giorni e B accumula due giorni di ritardo? Soluzione: B o un’altra attività del cammino critico, compatibilmente con risorse e qualità; anticipare soltanto C non recupera la fine, perché D continuerebbe ad attendere B. Il criterio di scelta è l’effetto sulla rete, non l’attività apparentemente più facile.

'''+anchor)
t+='\n### Riferimento metodologico\n\nCommissione europea, DG DIGIT, *The PM² Project Management Methodology Guide*, versione 3.1 (2023), §2.1.3, §6.4 e appendice C, §§C.5–C.13, DOI 10.2799/970188. WBS, dati, calendario e Gantt del laboratorio sono esempi originali costruiti per questo volume.\n'
u.save(slug,t,['V09-32','V09-33','V09-34'],u.REF);u.record()
