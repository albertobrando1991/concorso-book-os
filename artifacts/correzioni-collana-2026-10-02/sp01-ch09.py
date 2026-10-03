from pathlib import Path
import re,shutil
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/09-errori-casi-guidati.md');t=p.read_text(encoding='utf8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-09.md');assert not a.exists();shutil.copyfile(p,a)
cases='''## Caso guidato — Quattro decisioni con dati completi

I casi seguenti sono simulazioni: date, termini e punteggi sono forniti nella consegna, non regole trasferibili a un concorso reale. Prima di leggere le soluzioni, scrivi per ciascuno l’azione, il termine e il documento che prova la scelta.

**1. Certificato alla convocazione.** Il bando simulato richiede un certificato agonistico in corso di validità il giorno delle prove; precisa che un certificato scaduto impedisce di sostenerle e non consente rinvio per regolarizzarlo. Luca è convocato il 18 giugno. Il suo certificato scade il 15 giugno; una nuova visita è disponibile il 12 giugno. Può presentarsi con il vecchio certificato perché era valido al momento della domanda?

**Soluzione.** No. Il momento rilevante indicato è il 18 giugno: il vecchio documento non soddisfa la condizione. Luca prenota la visita del 12, senza presumere che il professionista rilascerà necessariamente un nuovo certificato, e controlla l’esito prima della convocazione. Se ottiene un certificato valido per la disciplina richiesta, lo porta nel formato prescritto; se non lo ottiene, la consegna esclude la prova e non prevede una sanatoria. Il risultato non dipende dalla preparazione ai quiz. Data di possesso del requisito, data del documento e giorno del suo impiego sono tre controlli distinti.

**2. Annullamento e nuovo invio.** La procedura simulata chiude il 7 aprile alle 23:59. Una domanda già inviata non è modificabile: il portale consente di annullarla e inviarne una nuova entro il termine. Sara scopre un errore nel contingente il 6 aprile. Alle 18:00 annulla la domanda e alle 18:20 salva una nuova bozza. Nessuna nuova ricevuta è prodotta. È iscritta?

**Soluzione.** Non sulla base dei dati forniti. La prima domanda è annullata; la seconda è soltanto una bozza. Sara deve completare e inviare la nuova domanda entro il 7 aprile alle 23:59, quindi salvare la ricevuta e controllare lo stato di invio. Conservare la vecchia ricevuta prova un invio poi annullato, non la partecipazione attuale. Non basta una schermata con i campi compilati. Il percorso da annotare è errore → annullamento → nuova compilazione → invio → nuova ricevuta: l’interruzione dopo il terzo passaggio lascia il procedimento incompleto.

**3. Avviso che cambia sede.** Il calendario del 2 maggio indica prova il 20 maggio alle 8:00 nella sede A. Un avviso ufficiale del 10 maggio sostituisce soltanto la sede con B e mantiene data e ora. Marco conserva il primo PDF e legge in una chat che l’ora sarebbe 9:00. Il viaggio verso B richiede 70 minuti; per l’esercizio egli sceglie un margine personale di 30 minuti. Quando parte?

**Soluzione.** Il dato ufficiale corrente è B, 20 maggio, ore 8:00. Il messaggio informale non modifica l’ora. Sottraendo 70 minuti di viaggio e 30 di margine, la partenza pianificata è alle 6:20. Marco salva entrambi gli avvisi con data e annota quale elemento è sostituito. I 30 minuti sono una scelta prudenziale del caso, non una prescrizione del bando; traffico e modalità di accesso possono richiedere un margine diverso. Un cambio di sede non autorizza a cambiare anche data o orario.

**4. Penalità e soglia.** Il test simulato contiene 60 quesiti: +1 per risposta esatta, −0,25 per errore, 0 per omissione. Per superarlo occorrono almeno 40 punti. Elena registra 44 risposte esatte, 12 errate e 4 omesse. Paolo ha 42 esatte, 12 errate e 6 omesse. Chi supera? Una graduatoria limitata ai migliori 100 è sufficiente per sapere chi accederà alla fase successiva?

**Soluzione.** Elena totalizza 44 − 3 = 41: supera la soglia. Paolo totalizza 42 − 3 = 39: non la supera. Entrambi i conteggi coprono tutti i 60 quesiti. Non conosciamo la posizione di Elena fra i migliori 100: occorrono i risultati degli altri candidati e la disciplina degli eventuali pari merito. Superamento della soglia e ammissione entro un contingente non coincidono. Nel diario, Paolo corregge gli errori per materia e causa; non attribuisce il risultato alle sole omissioni, perché rispondere a caso potrebbe aggiungere penalità.

**Consegna finale.** Per ogni caso identifica il punto irreversibile: giorno della prova per il certificato, termine di invio per la domanda, presentazione nella sede corrente per l’avviso, calcolo regolamentare per il test. La correzione utile deve intervenire prima di quel punto e produrre un’evidenza controllabile. Nei primi tre casi l’evidenza è documentale; nell’ultimo è un conteggio ripetibile. Questa distinzione aiuta a scegliere l’azione appropriata senza confondere un problema di studio con un adempimento.

'''
t=re.sub(r'## Caso guidato\n.*?(?=## Domanda da commissario)',lambda _:cases,t,flags=re.S)
questions=[
('Nel caso 1, quale momento decide la validità richiesta del certificato?', ['Il giorno della domanda.','Il giorno in cui Luca ha iniziato lo studio.','Il giorno delle prove, 18 giugno.','Il giorno della pubblicazione del bando.'],'C','La consegna richiede validità alla prova. Domanda, inizio dello studio e pubblicazione non sono il momento prescritto; il certificato che scade il 15 non basta il 18.'),
('Nel caso 2, annullata la vecchia domanda e salvata una nuova bozza, quale azione manca?', ['Inviare la nuova domanda entro il termine e verificarne la ricevuta.','Conservare soltanto la vecchia ricevuta.','Aspettare il calendario delle prove.','Inviare la bozza dopo la scadenza.'],'A','La bozza non è un invio e la ricevuta precedente riguarda la domanda annullata. Il calendario non sospende il termine; un invio successivo non soddisfa la consegna.'),
('Nel caso 3, quale combinazione corrisponde agli atti ufficiali?', ['Sede A, ore 8:00.','Sede A, ore 9:00.','Sede B, ore 9:00.','Sede B, ore 8:00.'],'D','Il secondo avviso sostituisce A con B e conserva le 8:00. La chat non modifica l’ora; trattenere A ignorerebbe la rettifica.'),
('Con 70 minuti di viaggio e 30 di margine, quale partenza corrisponde all’arrivo alle 8:00?', ['6:50.','6:20.','7:30.','7:00.'],'B','8:00 meno 100 minuti dà 6:20. Le altre ore non coprono insieme viaggio e margine: 6:50 copre soltanto i 70 minuti di viaggio.'),
('Qual è il punteggio di Elena nel caso 4?', ['41.','44.','47.','40.'],'A','44 esatte meno 12 × 0,25 dà 41; le 4 omissioni valgono zero. 44 ignora la penalità; 47 la somma; 40 non deriva dai dati.'),
('Elena ha superato 40 punti. Che cosa sappiamo sull’ammissione dei migliori 100?', ['È certamente ammessa.','È certamente esclusa.','Servono graduatoria e regole dei pari merito.','Basta il numero delle sue omissioni.'],'C','Superare la soglia è necessario ma non prova il rango utile. Non possiamo affermare ammissione o esclusione senza confronto; le omissioni isolate non danno la posizione.'),
('Paolo ha 42 esatte, 12 errori e 6 omissioni. Qual è l’esito rispetto a 40?', ['42, supera.','39, non supera.','40, supera.','45, supera.'],'B','42 − 12 × 0,25 = 39. Non si cancellano le penalità e non le si aggiunge al punteggio; le omissioni non aumentano il totale.'),
('Quale elemento del caso 3 è una scelta personale e non un dato dell’avviso?', ['La sede B.','La data del 20 maggio.','L’ora delle 8:00.','Il margine di 30 minuti.'],'D','Sede, data e ora derivano dagli atti della consegna. Il margine è pianificato da Marco: può aumentarlo, ma non cambiare unilateralmente la convocazione.')]
q='## ▣ Verifica 09.A · Quiz ragionati\n\n'
for n,(stem,opts,key,comment) in enumerate(questions,1):q+=f'{n}. {stem}\n\n'+ '\n'.join(f'{chr(65+i)}. {opt}' for i,opt in enumerate(opts))+f'\n\n**Risposta corretta: {key}.** {comment}\n\n'
t=re.sub(r'## ▣ Verifica 09.A.*?(?=## ▣ Verifica 09.B)',lambda _:q,t,flags=re.S)
t=re.sub(r'\| Elemento \| Dati essenziali \| Verifica o azione \|\n\| ---.*?(?=\n\n)', 'Voce da controllare: ________________________________________\n\nRegola della procedura e fonte: _______________________________\n\nErrore possibile e conseguenza: ______________________________\n\nCorrezione, termine ed evidenza: ______________________________',t,flags=re.S)
p.write_text(t,encoding='utf8')
print('SP01/09 corrected')
