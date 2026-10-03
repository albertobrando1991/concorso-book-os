from pathlib import Path
import re,json,hashlib,collections
A=Path('artifacts/correzioni-collana-2026-10-02'); B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
extras=[
['Funzione giudicante del pubblico ministero e controllo amministrativo del giudice.','Cancelleria civile, limitatamente al rilascio delle copie dei provvedimenti.','Studiando soltanto le mansioni riportate nell’organigramma dell’ufficio.','Gestione generale del tempo nel volume Giustizia; atti del fascicolo UPP nel manuale base.','Procedimenti disciplinari del personale ministeriale, senza studio dell’esecuzione penale.','La descrizione sintetica pubblicata in una pagina promozionale della selezione.'],
['DAG, DOG, DIT, DAP e Direzione generale degli archivi notarili.','Usarlo come denominazione attuale dell’intero Dipartimento dell’organizzazione giudiziaria.','DAG, in quanto ogni rapporto di lavoro costituisce un affare di giustizia.','DAP, anche per la generalità delle richieste civili internazionali.','DAP per tutti gli interventi sui minorenni; DGMC soltanto per le adozioni internazionali.','DGSTAT per le applicazioni processuali e DGSAP per la sola statistica giudiziaria.'],
['Il tribunale opera sul distretto e la corte d’appello sull’intero territorio nazionale.','Un magistrato togato e sei giudici popolari, mentre il tribunale collegiale ha due togati.','Il dirigente amministrativo della procura, che impartisce le direttive investigative.','Il Ministero approva il programma annuale in sostituzione dei due responsabili dell’ufficio.','Sì, purché il capo dell’ufficio autorizzi ogni spesa anche oltre le risorse assegnate.','È sempre una funzione collegiale della corte d’appello.'],
['Gli addetti amministrativi nominati dal dirigente sostituiscono i magistrati nel coordinamento.','Il Ministero adotta direttamente ogni progetto organizzativo locale senza intervento del capo dell’ufficio.','Sì, perché ogni segreteria del pubblico ministero coincide per legge con un UPP.','La conversione ha effetto soltanto dopo una successiva circolare ministeriale.','Sì, ma le attività di cancelleria diventano la funzione esclusiva di ogni addetto UPP.','L’addetto firma il provvedimento se il magistrato ha approvato oralmente la bozza.'],
['Dimostra da sola la responsabilità del trasportatore per tutti i danni denunciati.','Prova l’estinzione integrale del debito, indipendentemente dall’importo ordinato.','La selezione dipende esclusivamente dalla data di pubblicazione delle sentenze reperite.','L’addetto considera tempestiva ogni memoria presente nel fascicolo senza confrontare le date.','Si ordinano prima i documenti favorevoli all’attore e poi quelli favorevoli al convenuto.','Si registra l’accoglimento della domanda salvo successiva modifica del giudice.'],
['Almeno quaranta giorni prima dell’udienza, in tutti i casi del rito ordinario.','Quaranta, venti e dieci giorni dalla notificazione della citazione.','Sessanta giorni liberi anche quando la notificazione avviene in Italia.','Fa decorrere il termine breve soltanto quando il destinatario legge materialmente la PEC.','Il termine si proroga automaticamente di tanti giorni quanti sono i festivi del mese.','Ordinanza e decreto devono sempre avere la stessa motivazione analitica della sentenza.']]
moves={(1,1),(1,2),(2,1),(2,3),(3,2),(3,5),(4,3),(4,4),(5,4),(5,6),(6,3)}
ledger=[]
for ci,p in enumerate(sorted(B.glob('*.md'))[:6],1):
 t=p.read_text('utf-8'); before=hashlib.sha256(p.read_bytes()).hexdigest()
 start=t.index('### Quiz commentato');end=t.index('\n### ',start+5)
 section=t[start:end]; blocks=re.split(r'(?m)(?=^[1-6]\. \*\*)',section)
 assert len(blocks)==7
 for qi in range(1,7):
  x=blocks[qi]; assert len(re.findall(r'(?m)^   - [A-D]\. ',x))==3
  old=re.search(r'Risposta corretta: ([A-C])',x).group(1);new=old
  extra=extras[ci-1][qi-1]
  if (ci,qi) in moves:
   answer=re.search(r'(?m)^   - '+old+r'\. (.+)$',x).group(1)
   x=re.sub(r'(?m)^(   - '+old+r'\. ).+$',lambda m:m.group(1)+extra,x)
   extra=answer;new='D';x=x.replace('Risposta corretta: '+old,'Risposta corretta: D')
  x=x.replace('   **Risposta corretta:', '   - D. '+extra+'\n   **Risposta corretta:')
  blocks[qi]=x;ledger.append(dict(chapter=ci,question=qi,oldKey=old,newKey=new,addedDistractor=extras[ci-1][qi-1]))
 p.write_text(t[:start]+''.join(blocks)+t[end:],'utf-8')
(A/'VOL-04-quiz-uniformazione.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),'utf-8')
p=Path('wiki/sources/vol-04-digitale-verifica-2026-10-03.md');t=p.read_text('utf-8').replace('PCT: correzione anche della proposta di audit','PCT: aggiornamento della regola temporale').replace("La proposta dell'audit V04-18 centrata sulla sola RdAC va quindi aggiornata, lasciando immutato l'audit storico.","L’ipotesi iniziale di correzione centrata sulla sola RdAC è stata aggiornata dopo il confronto con le specifiche e la rassegna della Cassazione. L’audit storico rimane immutato.");p.write_text(t,'utf-8')
p=A/'VOL-04-text-verifica.json';d=json.loads(p.read_text('utf-8'));keys=[]
for ch in d['chapters']:
 f=Path(ch['path']);t=f.read_text('utf-8');k=[a or b for a,b in re.findall(r'Risposta corretta: ([A-D])|\*\*Risposta ([A-D])\.',t)];ch.update(sha256=hashlib.sha256(f.read_bytes()).hexdigest(),quizKeys=k,words=len(t.split('---',2)[-1].split()));keys+=k
d['keyDistribution']=dict(collections.Counter(keys));assert d['keyDistribution']==dict(A=21,B=21,C=21,D=21)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8');print(d['keyDistribution'])
