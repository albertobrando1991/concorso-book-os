from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
comments={
'01':[
'La mappa identifica amministrazione, ruolo e fasi, poi orienta il piano. Non sostituisce il bando, non rende identiche le procedure e non elimina le materie giuridiche: questi sono gli errori delle altre opzioni.',
'La Polizia di Stato ha ordinamento civile nell’Amministrazione della pubblica sicurezza. Le alternative confondono status militare, specializzazione economico-finanziaria e polizia locale; nessuna descrive correttamente questo corpo.',
'Ruolo e output richiesti possono cambiare. Le altre risposte cancellano indebitamente prove scritte, requisiti o valore vincolante del bando, invece di leggere le differenze effettive.',
'La sequenza orienta la pianificazione ma va verificata: il bando PS 1.000 del 2026 consente anche di riorganizzare gli accertamenti. Non è immutabile, non è irrilevante e non riguarda soltanto lo studio.',
'Le fasi eliminatorie richiedono il proprio superamento. Un buon punteggio non compensa automaticamente un’inidoneità; gli accertamenti hanno conseguenze e anche la domanda può presentare cause di esclusione.',
'Trascurare le fasi residue espone a esclusioni o mancati adempimenti. Monitorare avvisi, preparare documenti e ripassare le differenze sono invece attività coerenti con la prosecuzione.'
],
'03':[
'Coprire la banca significa studiare tutti i quesiti ufficiali pertinenti e classificare gli errori. Selezionare solo quelli ritenuti frequenti lascia lacune; memorizzare la posizione è fragile; eliminare la teoria impedisce di capire gli errori.',
'L’esempio permette di pianificare una finestra breve tra banca e prova. Non stabilisce il calendario delle tornate future, non rende superfluo il bando e non trasforma il livello del ruolo.',
'Le frasi pronte non risolvono una traccia nuova. Testi completi, scaletta e revisione di punteggiatura e coerenza sono invece strumenti pertinenti alla composizione prevista, per esempio, dalla GdF 983 del 2026.',
'Un’opinione senza struttura perde pertinenza e nessi. Definire l’oggetto, scegliere esempi e mantenere un registro sobrio sono invece azioni utili per la prova discorsiva indicata nella domanda.',
'La preselezione svolge una funzione di filtro. Non è priva di conseguenze, non coincide necessariamente con lo scritto successivo e richiede allenamento nel formato previsto.',
'Il doppio binario distingue accesso base e ispettivo. Non impone due scritti, non trasferisce una banca fra corpi e non sostituisce automaticamente una composizione con una preselezione.',
'Il dato va ricavato dagli atti della specifica procedura. Ricordi, forum e precedenti possono suggerire una verifica, ma non provano durata, soglia o numero di quesiti attuali.',
'Scaletta, testo e revisione esercitano produzione e coerenza. Liste memorizzate, sole crocette e sole percentuali misurano prestazioni diverse e non dimostrano la capacità di costruire l’elaborato.'
],
'05':[
'Il bando e gli atti successivi della procedura definiscono l’orale. Forum, programmi precedenti e manuali generali non sostituiscono quella disciplina e possono riferirsi a prove diverse.',
'Una risposta collega contenuto e applicazione in modo pertinente. Lunghezza e lessico difficile non provano padronanza; eliminare ogni riferimento al ruolo può togliere il contesto necessario.',
'Il titolo produce l’effetto attribuito dalla specifica procedura. Non sostituisce le prove obbligatorie, non ha un valore identico in tutti i bandi e non elimina un orale previsto.',
'Le lingue elencate sono opzioni di quella procedura. Non valgono automaticamente altrove; il prestigio non è un criterio di punteggio; una facoltativa non diventa obbligatoria per il nome della lingua.',
'Confrontare punteggio ottenibile, tempo e competenza già posseduta misura la convenienza. Prestigio, preferenze altrui e scelta automatica dell’inglese non svolgono questo confronto; resta da rispettare il termine per l’opzione.',
'Dichiarare il limite e rispondere sul contenuto certo evita di aggiungere un errore. Inventare, cambiare argomento o negare il valore dei dettagli non risolve la domanda; una risposta incompleta può comunque incidere sulla valutazione.'
],
'06':[
'Il volume base tratta il nucleo comune; la specializzazione richiede il delta e le destinazioni indicate nel capitolo. Un modulo scelto a caso, i soli quiz o le sole appendici non garantiscono quella copertura.',
'Il rinvio indicato riguarda il metodo di studio della banca e il diario degli errori. Non insegna da solo TULPS, ordinamento di ogni corpo o direttive della Procura: sono oggetti diversi.',
'L’ordinamento individua soggetti, strutture, funzioni e coordinamento. Non determina da solo il reato, la frequenza di un quiz o una sanzione valida in ogni caso.',
'Una possibile notizia di reato richiede di individuare il piano dell’accertamento penale e le regole applicabili. Un controllo o un titolo amministrativo non coincide sempre con quel piano; la lacuna del candidato non attiva alcuna funzione.',
'Il TULPS è un riferimento di pubblica sicurezza e polizia amministrativa. Non disciplina il metodo delle banche dati, la contabilità generale o una prova linguistica.',
'Separare i tre piani permette di identificare competenza, titolo amministrativo ed eventuale notizia di reato. Ridurre tutto al solo penale o amministrativo perde parte del caso; attribuire ogni potere all’operatore ignora le competenze.'
],
'07':[
'Corpo e binario individuano la procedura da decodificare. Lunghezza del PDF, popolarità di un gruppo o vendite di un manuale non identificano requisiti e prove.',
None,
'Posti, riserve, età, soglie, date e punteggi richiedono fonte e controllo. Le risposte che limitano la registrazione al nome, alla difficoltà o alle simulazioni omettono vincoli decisivi.',
'L’idoneità accerta il requisito o standard previsto. Non attribuisce necessariamente un punteggio classificatorio, non sostituisce lo scritto e non rende inutile la lettura del bando.',
'La soglia non può essere inventata: controlla bando, allegati e atti successivi e registra precisamente ciò che manca. Una media storica non è una regola; l’assenza nel primo documento non impone da sola di scartare il concorso.',
'Attendere, partecipare e scartare possono essere scelte motivate, purché l’attesa non faccia perdere un termine già aperto. Nessuna delle tre è sbagliata in astratto: conta il dato che giustifica la decisione.',
'Prove, materie, funzioni e aspettative possono differire fra i livelli. Non è vero che l’ispettivo abbia sempre meno prove o non richieda teoria; appartiene alla famiglia considerata.',
'Una scheda utile distingue dati verificati, assenti, non reperiti e da controllare. Riempire celle con ipotesi, copiare tutto o omettere le date riduce la possibilità di controllare le decisioni.'
]
}
keys={}
for p in sorted(B.glob('*.md')):
 t=p.read_text(encoding='utf8');c=p.name[:2]
 t=t.replace('### Apertura editoriale\n\n','')
 if c=='02':
  t=t.replace('3. Per i concorsi banditi dopo il 13 gennaio 2016, il requisito di statura:','3. Nei concorsi delle forze di polizia rientranti nel D.P.R. 207/2015 e banditi dopo il 13 gennaio 2016, il precedente requisito generale di statura:')
  t=t.replace('Il requisito di statura è abolito per i concorsi banditi dopo il 13 gennaio 2016. Questo non elimina gli altri eventuali accertamenti di idoneità.','Nell’ambito del D.P.R. 207/2015 il precedente limite generale di altezza è sostituito dai parametri previsti. Non vengono eliminati gli altri accertamenti; le alternative mantengono il vecchio limite o inventano una distinzione fra binari.')
 if c=='04':t=t.replace('3. Per i concorsi banditi dopo il 13 gennaio 2016, quale criterio ha sostituito la statura come requisito generale?','3. Nei concorsi delle forze di polizia rientranti nel D.P.R. 207/2015 e banditi dopo il 13 gennaio 2016, che cosa sostituisce il precedente requisito generale di statura?')
 if c=='10':
  t=t.replace('## N-SP01-15-04', '''**Controllo applicato.** Un certificato valido alla domanda ma scaduto alla convocazione richiede la verifica della data di validità prescritta, non una deduzione dall’invio già riuscito. Una visita prenotata non equivale a un certificato rilasciato. Annota per ciascun documento il professionista o ente abilitato, la disciplina richiesta, la data di rilascio, la validità e il formato da presentare. Se un referto ha una finestra temporale breve, prenotarlo troppo presto può renderlo inutilizzabile: il calendario degli adempimenti deve partire dalla convocazione e dalle istruzioni specifiche, senza inventare proroghe.

## N-SP01-15-04''')
 # Normalize only quiz indentation, retaining meaning; identify every four-option question.
 t=re.sub(r'^   (?=[A-D]\. |\*\*Risposta corretta:)', '',t,flags=re.M)
 pat=r'(?P<opts>^A\. [^\n]+\nB\. [^\n]+\nC\. [^\n]+\nD\. [^\n]+\n)\s*\*\*Risposta corretta: (?P<key>[A-D])\.\*\*(?P<comment>.*?)(?=\n\s*\n(?:\*\*)?\d+\. |\n## |\Z)'
 idx=[0];seq=[]
 def fix(m):
  i=idx[0];idx[0]+=1;opts=re.findall(r'^[A-D]\. (.+)$',m['opts'],re.M);old=m['key'];comment=m['comment'].strip()
  if c in comments and i<len(comments[c]) and comments[c][i]:comment=comments[c][i]
  target='ABCD'[(i+int(c))%4];shift=(ord(target)-ord(old))%4;mapping={chr(65+n):chr(65+(n+shift)%4) for n in range(4)}
  out=['']*4
  for n,opt in enumerate(opts):out[(n+shift)%4]=opt
  comment=re.sub(r'\b[A-D]\b',lambda x:mapping[x[0]],comment)
  seq.append(target)
  return '\n'.join(f'{chr(65+n)}. {opt}' for n,opt in enumerate(out))+f'\n\n**Risposta corretta: {target}.** {comment}\n'
 t=re.sub(pat,fix,t,flags=re.M|re.S)
 assert idx[0]==len(re.findall(r'Risposta corretta:',t)),(p,idx[0])
 keys[c]=seq;p.write_text(t,encoding='utf8')
(A/'M-SP01-quiz-keys.json').write_text(json.dumps(keys,indent=2),encoding='utf8')
print(keys)
