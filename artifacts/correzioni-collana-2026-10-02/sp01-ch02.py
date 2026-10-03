from pathlib import Path
import re,shutil
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/02-posizione-prima-domanda.md'); t=p.read_text(encoding='utf-8'); a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-02.md'); assert not a.exists();shutil.copyfile(p,a)
start=t.index('## N-SP01-04-02');end=t.index('## N-SP01-04-04',start)
t=t[:start]+'''## N-SP01-04-02 · Età, diploma e parametri fisici: leggere la formula esatta

### Requisito, categoria e data

Un limite di età ha significato soltanto se sono identificati il concorso, la categoria del candidato e la data alla quale deve essere rispettato. Non esiste un limite unico per la famiglia delle forze di polizia. Anche nello stesso bando possono coesistere una soglia ordinaria, un’elevazione collegata al servizio e un’esenzione per personale già appartenente all’amministrazione. L’elevazione non va sommata a un numero che la comprende già: questo errore allargherebbe indebitamente la platea dei partecipanti.

Le espressioni usate negli atti non sono sinonimi. «Non aver compiuto il ventiseiesimo anno» esclude chi compie ventisei anni proprio alla data di riferimento. «Non aver superato il giorno del ventiseiesimo compleanno» comprende quel giorno ma non il successivo. «Età non superiore a venticinque anni compiuti» richiede ancora un’altra lettura, da conservare nella formulazione del bando. Registrare soltanto «massimo26» cancella l’informazione decisiva e non permette un controllo affidabile.

### Cinque esempi ufficiali del 2026

Le righe seguenti sono esempi datati, verificati sugli articoli dei rispettivi bandi, e non anticipazioni dei requisiti di future selezioni.

| Procedura e categoria | Formula anagrafica alla scadenza |
| --- | --- |
| Polizia di Stato, 4.400 allievi agenti, civili e bilinguisti; art. 2 | Diciotto compiuti e ventisei non compiuti |
| Stessa procedura, volontari in ferma prefissata | Venticinque non compiuti; condizioni di servizio dell’art. 1 |
| Polizia di Stato, 1.000 vice ispettori; art. 3 | Ventotto non compiuti, con regimi specifici per personale già in servizio |
| Carabinieri, 3.081 allievi, civili; art. 2 | Non superato il giorno del ventiquattresimo compleanno; domanda possibile dai diciassette con consenso prescritto |
| Carabinieri, 898 marescialli, cittadini; art. 2 | Diciassette compiuti e non superato il giorno del ventiseiesimo compleanno |
| Guardia di finanza, 983 marescialli, cittadini; art. 2 | Diciassette compiuti e non superato il giorno del ventiseiesimo compleanno |

Per i due bandi della Polizia di Stato l’elevazione è pari all’effettivo servizio militare, entro tre anni: non spettano automaticamente tre anni a chi ha prestato un servizio più breve. Nei vice ispettori si prescinde dal limite per personale PS con almeno tre anni di effettivo servizio alla data del bando; per appartenenti ai ruoli civili dell’Interno il limite è trentatré anni. Sono fattispecie differenti, da non estendere a qualsiasi dipendente pubblico.

Per i 3.081 Carabinieri, ai VFP si applica la formula «età non superiore a venticinque anni compiuti» e occorrono le condizioni di servizio previste. Per gli 898 marescialli il servizio militare qualificato dall’articolo 2 può elevare il limite fino al giorno del ventottesimo compleanno; per le categorie del personale dell’Arma elencate dal bando vale il giorno del trentesimo. Per i 983 marescialli GdF le categorie militari del Corpo indicate nell’articolo 2 hanno invece il limite del giorno del trentacinquesimo compleanno. Non basta essere militare di un’altra amministrazione per applicarlo.

### Caso con compleanno alla scadenza

Anna, civile senza elevazioni, è nata il 29 maggio 2000. Per i 4.400 agenti PS con scadenza 29 maggio 2026 compie ventisei anni proprio quel giorno: non rispetta il limite di ventisei non compiuti. Paolo, nato il 23 marzo 2000, considera invece i 983 marescialli GdF con scadenza 23 marzo 2026: compie ventisei anni quel giorno e non lo ha ancora superato. Il solo requisito anagrafico è soddisfatto; gli altri requisiti restano da verificare. Le due conclusioni diverse dipendono dalle formule, non da una preferenza dell’interprete.

### Titolo di studio e salute sono controlli distinti

Anche il diploma richiede una data. Nei due esempi PS il bando consente il conseguimento entro la prima prova secondo la specifica clausola; nei bandi Carabinieri e GdF citati è prevista la possibilità di conseguirlo nell’anno scolastico 2025/2026. Queste eccezioni non autorizzano a partecipare a ogni concorso prima del diploma. Esistono inoltre discipline particolari per determinate categorie di volontari con servizio risalente: occorre leggere la categoria completa, non sostituire sempre il titolo con la licenza media.

Il superamento dei limiti generali di statura, con legge 2/2015 e D.P.R. 207/2015 per le procedure successive al 13 gennaio 2016 nel relativo ambito, non elimina gli altri requisiti fisici e sanitari. Composizione corporea, forza muscolare e massa metabolicamente attiva sono parametri diversi dall’altezza e dalle prestazioni atletiche. Superare la corsa non dimostra automaticamente idoneità sanitaria. L’accertamento compete agli organi previsti dalla procedura.

**Esercizio.** Scrivi una riga con corpo, ruolo, categoria, data di nascita, data limite, formula letterale ed eventuale elevazione documentata. Per Anna indica «età non soddisfatta»; per Paolo «età soddisfatta, altri requisiti da controllare». Non compilare l’esito generale usando soltanto la casella anagrafica.

## N-SP01-04-03 · Condotta, cause ostative e accertamenti personali

### Tre domande diverse

La verifica della condotta riguarda il comportamento del candidato in relazione all’accesso al ruolo. L’idoneità psichica appartiene alla valutazione sanitaria prevista dalla procedura. L’idoneità attitudinale riguarda invece la compatibilità delle caratteristiche personali con le funzioni del profilo. Sono controlli distinti: nessuno sostituisce automaticamente gli altri. Un certificato sportivo valido non attesta la condotta e un buon risultato culturale non dimostra l’idoneità attitudinale.

L’articolo 26 della legge 53/1989 richiede le qualità morali e di condotta stabilite per l’ammissione ai concorsi della magistratura ordinaria. Questo rinvio deve essere coordinato con l’ordinamento del corpo e con le singole disposizioni del bando. Nella lettura occorre separare il requisito generale di condotta dalle cause ostative specifiche. Sarebbe sbagliato concludere che ogni episodio personale comporti esclusione; sarebbe altrettanto sbagliato affermare che nessuna situazione possa più avere una conseguenza prevista espressamente dalla legge.

### Che cosa ha deciso la Corte costituzionale

La sentenza 40/2024 riguarda una precisa disposizione del reclutamento nella Guardia di finanza: l’articolo 6, comma 1, lettera i), del D.Lgs. 199/1995. La Corte ha eliminato la previsione della guida in stato di ebbrezza costituente reato come causa automatica di esclusione. Il trattamento differenziato rispetto ad altre forze di polizia non era giustificato. L’effetto è circoscritto a quella clausola: la condotta deve essere valutata individualmente, senza l’automatismo dichiarato incostituzionale.

La decisione non comporta che il comportamento sia irrilevante o che l’ammissione sia garantita. Non cancella indistintamente tutte le condizioni ostative degli ordinamenti di polizia, non riguarda ogni reato e non autorizza a omettere una dichiarazione richiesta. La distinzione fra norma colpita e altre disposizioni è necessaria anche quando la motivazione contiene principi più ampi: un principio interpretativo non permette di fingere inesistenti tutte le norme non oggetto della pronuncia.

### Come leggere una clausola del bando

Il controllo si svolge in quattro passaggi. Prima si identifica la situazione richiesta dal testo: condanna, procedimento, misura o altra condizione, senza sostituire categorie giuridiche diverse. Poi si verifica la disposizione richiamata e l’eventuale qualificazione del fatto. Si controllano quindi la data rilevante e le modalità di dichiarazione. Infine si considera se il caso richieda un accertamento individuale o ricada in una previsione specifica, tenendo conto delle decisioni applicabili. La sola lettura di un commento online non risolve quest’ultimo passaggio.

Per esempio, il bando PS 4.400 del 2026 distingue il requisito di condotta dell’articolo 2, comma 1, dalle situazioni elencate nei commi successivi; il bando Carabinieri 3.081 articola più condizioni nell’articolo 2. Non è corretto sostituire tutte quelle disposizioni con «si decide sempre caso per caso». In presenza di una situazione personale controversa occorre ricostruire atti e date e ottenere un chiarimento qualificato, senza affidare la compilazione a una rassicurazione generica.

### Dove si colloca il D.M. 198/2003

Il D.M. Interno 198/2003 concerne i requisiti fisici, psichici e attitudinali della Polizia di Stato nel proprio ambito. Non è la fonte generale della condotta e non si estende automaticamente all’Arma o alla Guardia di finanza. La sostituzione dei limiti di statura non ha cancellato l’intero decreto né gli altri requisiti sanitari. Per gli altri corpi si leggono le rispettive disposizioni e gli atti tecnici richiamati dal concorso.

Questa collocazione evita anche una confusione pratica. La valutazione sanitaria non si prepara imparando risposte rassicuranti; richiede documentazione corretta e accertamenti degli organi competenti. L’attitudine non si dimostra recitando una biografia ideale. Una presentazione coerente di esperienze, motivazioni e limiti è diversa dal tentativo di alterare l’esito mediante risposte costruite a memoria.

### Caso risolto e risposta orale

Elena legge la sentenza 40/2024 e conclude: «Qualunque precedente deve ormai essere ignorato». La conclusione è errata due volte. La sentenza riguarda una clausola specifica del reclutamento GdF e, per quella condotta, sostituisce l’automatismo con la valutazione individuale; non impone di ignorare il fatto. Elena deve identificare il proprio concorso, la dichiarazione richiesta e la disposizione pertinente. Se il suo episodio è differente da quello deciso, non può attribuirgli automaticamente lo stesso effetto.

**Domanda da commissario.** La pronuncia elimina tutti gli automatismi di esclusione? **Risposta:** no. Occorre citare la disposizione e il fatto oggetto della dichiarazione di illegittimità, distinguere la valutazione della condotta dalle altre cause ostative e non trasformare la sentenza in una garanzia di ammissione. L’errore tipico è generalizzare il dispositivo; la verifica consiste nel spiegare, in due frasi, ciò che la decisione cambia e ciò che non decide.

''' +t[end:]
t=t.replace('il limite anagrafico della tornata 2026','il requisito anagrafico della specifica procedura').replace('il limite anagrafico della tornata','il requisito anagrafico della specifica procedura')
start=t.index('## Da sapere in 5 righe');end=t.index('## Domanda da commissario',start)
t=t[:start]+'''## Da sapere in 5 righe

1. Identifica corpo, ruolo e categoria prima di verificare età e titoli.
2. «Non compiuti» e «non superato il giorno del compleanno» producono esiti diversi.
3. Il superamento della statura minima non elimina altri parametri o requisiti sanitari.
4. La sentenza 40/2024 colpisce una specifica clausola GdF, non tutte le cause ostative.
5. Ricevuta della domanda, possesso dei requisiti e superamento degli accertamenti sono fatti distinti.

## Caso guidato

Alessia confronta i bandi 2026 di due concorsi. Nel fascicolo separa la formula anagrafica, l’eventuale elevazione e la data del diploma. Per ciascuno annota l’articolo; non scrive «requisiti delle forze di polizia». Se il diploma può essere conseguito entro una prova, registra sia l’eccezione sia la data da rispettare. La ricezione della domanda non dimostra che quel diploma sia già stato acquisito.

Per la condotta distingue le dichiarazioni richieste dagli accertamenti dell’amministrazione e non usa una sentenza su una diversa clausola per escludere l’obbligo di dichiarare. Conserva infine domanda definitiva e ricevuta. Se modifica la domanda secondo la procedura prevista, salva anche la nuova ricevuta: il file precedente non dimostra il successivo invio.

''' +t[end:]
start=t.index('Il secondo errore è memorizzare');end=t.index('Il quinto errore',start)
t=t[:start]+'''Il secondo errore è usare un’età unica per tutti i corpi o sommare due volte un’elevazione. Occorre applicare la formula del proprio bando alla categoria corretta.

Il terzo errore è confondere la sostituzione dei limiti di statura con l’abolizione degli accertamenti sanitari.

Il quarto errore è generalizzare la sentenza 40/2024 a qualsiasi precedente personale o applicare il D.M. 198/2003 a tutti i corpi.

''' +t[end:]
start=t.index('2. Il limite di 29');end=t.index('3. Per i concorsi',start)
t=t[:start]+'''2. Anna compie ventisei anni alla scadenza della domanda PS 4.400 del 2026, partecipa come civile e non ha elevazioni. Quale conclusione è corretta?

A. Rispetta il requisito perché il compleanno è incluso.
B. Può ignorare il limite se il portale accetta l’invio.
C. Non rispetta il requisito di ventisei anni non compiuti.
D. Ha sempre tre anni aggiuntivi, anche senza servizio militare.

**Risposta corretta: C.**
Il requisito esclude chi ha già compiuto ventisei anni alla data rilevante. A confonde una diversa formula; B confonde ricezione tecnica e ammissibilità; D attribuisce un’elevazione senza il servizio che la giustifica.

''' +t[end:]
start=t.index('4. La condotta del candidato deve');end=t.index('6. La ricevuta',start)
t=t[:start]+'''4. La sentenza costituzionale 40/2024:

A. Elimina tutte le cause di esclusione da tutti i concorsi.
B. Elimina lo specifico automatismo GdF relativo alla guida in stato di ebbrezza costituente reato.
C. Dichiara irrilevante ogni condotta pregressa.
D. Sostituisce il D.M. 198/2003 per tutti i corpi.

**Risposta corretta: B.**
Il dispositivo riguarda la clausola dell’art. 6, comma 1, lettera i), D.Lgs. 199/1995. A amplia indebitamente l’ambito; C confonde valutazione individuale e irrilevanza; D associa alla sentenza un regolamento sanitario che non ne è l’oggetto.

5. Quale descrizione del D.M. 198/2003 è corretta?

A. Disciplina ogni corpo e sostituisce le norme sulla condotta.
B. Riguarda requisiti fisici, psichici e attitudinali della Polizia di Stato nel proprio ambito.
C. È stato abrogato integralmente con il superamento della statura minima.
D. Stabilisce un’età unica per le forze di polizia.

**Risposta corretta: B.**
La disciplina è riferita alla Polizia di Stato e conserva gli altri contenuti applicabili. A generalizza e confonde oggetti diversi; C scambia la modifica di un requisito con l’abrogazione dell’atto; D attribuisce al decreto una regola anagrafica inesistente.

''' +t[end:]
t=t.replace('Spiega perché il dato “29 anni non compiuti” deve essere collegato alla tornata 2026 e verificato sul bando.','Confronta le formule anagrafiche degli esempi PS 4.400 e GdF 983 e risolvi il caso del compleanno alla scadenza.')
t=t.replace('Spiega perché la condotta richiede valutazione caso per caso secondo l’articolo 26 della legge 53/1989.','Delimita gli effetti della sentenza 40/2024 e distingui condotta e cause ostative specifiche.')
t=t.replace('Articolo 26 della legge 53/1989, per la valutazione caso per caso della condotta.','Articolo 26 della legge 53/1989; Corte costituzionale, sentenza 40/2024, nel suo preciso ambito.')
t=t.replace('Decreto ministeriale 198/2003, per i profili pertinenti all’idoneità psichica e attitudinale.','D.M. Interno 198/2003: requisiti fisici, psichici e attitudinali della Polizia di Stato; legge 2/2015 e D.P.R. 207/2015.')
assert '29 anni' not in t
p.write_text(t,encoding='utf-8');print('SP01/02 corretto: età, condotta, ambito sanitario, quiz')
