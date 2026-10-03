from pathlib import Path
import shutil
p=next(Path('wiki/books/moduli/m-sp04-prefettizia-diplomatica/chapters').glob('05-*.md'));a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp04-05.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=t.replace('economia e cooperazione;', 'economia politica, politica economica, economia internazionale e finanziaria e commercio internazionale;')
t=t.replace('Se esistono orientamenti, distingue.','Se esistono orientamenti, distingui.').replace('offre prima la regola','offri prima la regola').replace('delimita il profilo e riparte','delimita il profilo e riparti')
t=t.replace('Per informatica, le istruzioni vengono lette una sola volta e poi eseguite; il debrief distingue incomprensione, operazione e controllo.','Per informatica, leggi le istruzioni, identifica i risultati richiesti e torna a controllarle durante e dopo l’esecuzione, salvo diversi vincoli ufficiali. L’obiettivo è eseguire correttamente, non memorizzare una consegna vista una sola volta. Il debrief distingue incomprensione, operazione e controllo.')
anchor='## N-SP04-09-04'
s=t.index(anchor)
t=t[:s]+'''### Dossier orale chiuso: una decisione con dati incerti

Il dossier seguente è una simulazione originale con dati interamente ipotetici, fissati alla data convenzionale del 1° settembre 2026. Non descrive una procedura reale né sostituisce la disciplina delle competenze e degli acquisti. Un ufficio riceve 120 richieste mensili di informazione; 30 riguardano documenti già spiegati sul sito. Propone una pagina informativa più chiara, una traduzione controllata e un punto di assistenza telefonica. Sono disponibili 20 ore di lavoro interno al mese, senza nuovo personale. La pagina richiede 6 ore iniziali e 2 ore mensili di aggiornamento; la traduzione 4 ore iniziali e 1 ora mensile di controllo; il telefono 3 ore settimanali. Per il solo esercizio ogni mese ha quattro settimane. Non sono noti i tempi medi per richiesta né l’effetto delle tre misure.

**Domanda.** “Quale proposta presenteresti e come ne controlleresti l’esito?” Prima formula una risposta da novanta secondi, poi rispondi all’obiezione: “Perché non aprire subito tutti i canali?”

**Risposta possibile.** “Proporrei una sperimentazione graduata, misurando prima quante richieste possono essere evitate da informazioni più chiare. Pagina e traduzione richiedono 10 ore iniziali e 3 ore di manutenzione nel primo mese: 13 ore, lasciandone 7 entro il limite. Il telefono a regime richiede 12 ore mensili; insieme alle altre attività porterebbe il primo mese a 25 ore. Non è quindi compatibile con le 20 ore disponibili senza ridurre o rinviare qualcosa. Nel secondo mese pagina, traduzione e telefono richiederebbero invece 15 ore ordinarie, se le stime si confermassero. Prima di estendere, registrerei numero e tipo di contatti, tempo di risposta, aggiornamenti necessari e reclami. Non prometterei una riduzione di 30 richieste: quel numero individua un gruppo potenzialmente interessato, non un effetto già dimostrato.”

**Obiezione e replica.** “Aprire tutto subito potrebbe rendere il servizio più accessibile, ma il vincolo iniziale è documentato. Posso proporre una partenza differita del telefono o un numero di ore ridotto, verificando che i canali esistenti garantiscano comunque accesso alle informazioni. Non eliminerei l’assistenza per chi non usa il digitale. La scelta va motivata, autorizzata nell’ambito delle competenze e riesaminata con dati.” La replica distingue accessibilità, risorse e competenza: non attribuisce al candidato il potere di istituire da solo un servizio.

**Passaggio diplomatico in inglese.** “How would you explain the delay to users?” — “I would state when each service will become available, explain the temporary arrangements and provide a reliable contact point. I would avoid promising an immediate reduction in waiting times, because we have not measured the effect yet.” Il contenuto resta identico al dossier; cambiano lingua e destinatario.

**Passaggio prefettizio.** “Qual è il profilo organizzativo?” — “Occorre distinguere il carico iniziale da quello ricorrente, assegnare responsabile e tempi dell’aggiornamento, conservare un canale accessibile e verificare gli esiti. Le venti ore sono il vincolo del caso, non una regola nazionale. La decisione richiede inoltre di controllare le competenze dell’ufficio e le procedure applicabili prima dell’attuazione.”

### Compito informatico con soluzione controllabile

Usa un foglio elettronico, senza vincoli di marca, e inserisci quattro colonne: attività, ore iniziali, ore mensili, totale primo mese. Le righe sono: pagina 6/2; traduzione 4/1; telefono 0/12. Calcola l’ultima colonna con la somma delle due precedenti, poi il totale complessivo. Il risultato è 8, 5, 12 e totale 25. Aggiungi “margine rispetto alle 20 ore”: 20 − 25 = −5. Per il mese successivo usa soltanto la colonna mensile: 2 + 1 + 12 = 15, margine +5. Non confondere ore iniziali una tantum e manutenzione ricorrente.

Esporta una breve nota leggibile con titolo, ipotesi delle quattro settimane, proposta e due risultati. Salva il file con un nome che identifichi data e versione. Riaprilo e controlla valori, unità e assenza di colonne troncate. Per il retest cambia la disponibilità a 24 ore: il primo mese resta oltre il limite di un’ora, mentre quello successivo conserva nove ore di margine. Rileggere la consegna è parte del controllo; l’esercizio non impone né anticipa funzioni della piattaforma concorsuale.

**Griglia di debrief.** La risposta è riuscita se espone il vincolo, calcola correttamente, distingue stima ed effetto osservato, formula una proposta condizionata e conserva accessibilità e competenze. È incompleta se si limita a “digitalizzare”; è errata se dichiara 30 richieste sicuramente eliminate o somma ogni mese le 10 ore iniziali. Il foglio è corretto solo se le formule riflettono queste distinzioni, non se presenta un totale esteticamente plausibile.

'''+t[s:]
p.write_text(t,encoding='utf8')
