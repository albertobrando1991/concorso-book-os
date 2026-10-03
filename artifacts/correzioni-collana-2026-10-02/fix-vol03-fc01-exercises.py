from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-fc01-ministeri/chapters'); A=Path('artifacts/correzioni-collana-2026-10-02')
data=json.loads((A/'fc01-quiz.json').read_text(encoding='utf8'));ledger=[]
patterns={'08':'CADBAC','09':'DBACDB','10':'CADBBDAC','11':'ACDCBADB','12':'DBCABADCAC','13':'BDADCCBA','14':'DBACADCB','15':'BDCABD'}
for code,rows in data.items():
 p=next(B.glob(code+'-*.md'));s=p.read_text(encoding='utf8');questions=[];solutions=[]
 for i,(q,right,a,b,c,why) in enumerate(rows):
  idx='ABCD'.index(patterns[code][i]);options=[a,b,c];options.insert(idx,right);letter='ABCD'[idx]
  questions.append('### '+str(i+1)+'. '+q+'\n\n'+'\n'.join('ABCD'[j]+'. '+v for j,v in enumerate(options)))
  solutions.append('**'+str(i+1)+'. Risposta corretta: '+letter+'.** '+why)
  ledger.append({'chapter':code,'number':i+1,'correct':letter,'answer':right,'comment':why,'alternatives':options})
 if code=='14':
  start=s.index('### Otto quesiti originali');end=s.index('### Correzione dei quiz',start)
  s=s[:start]+'### Otto quesiti originali — prova\n\nSegna le otto risposte prima di aprire le soluzioni.\n\n'+'\n\n'.join(questions)+'\n\n### Soluzioni degli otto quesiti\n\n'+'\n\n'.join(solutions)+'\n\n'+s[end:]
 else:
  start=s.index('## ▣ Verifica');end=s.index('### Caso ragionato',start) if code!='15' else s.index('### Checklist finale',start)
  title=s[start:s.index('\n',start)]
  s=s[:start]+title+'\n\nCompleta la batteria annotando le lettere; consulta la correzione soltanto dopo l’ultima risposta.\n\n'+'\n\n'.join(questions)+'\n\n### Soluzioni commentate\n\n'+'\n\n'.join(solutions)+'\n\n'+s[end:]
 if code=='09':
  a=s.index('## Mappa BANDO');b=s.index('## N-FC01',a)
  s=s[:a]+'''## Mappa BANDO

- **B — Bando:** individua il perimetro statale e la profondità contabile richiesta.
- **A — Aree:** separa programmazione, bilancio, gestione e controlli.
- **N — Nuclei:** ricostruisci autorizzazione, fasi, competenza, cassa e residui.
- **D — Diario:** registra confusioni tra documenti, soggetti e momenti della spesa.
- **O — Output:** risolvi calcoli e casi e spiega la sequenza all'orale.

'''+s[b:]
 if code=='11':
  s=s.replace('A — Aree e attori','A — Aree').replace('N — Nucleo normativo','N — Nuclei')
  s=s.replace('| D — Decisione | Quale sequenza di atti è sostenibile? | Soluzione motivata |','| D — Diario | Quali errori di sequenza o competenza devo correggere? | Regola e prova di recupero |')
 if code=='12':s=s.replace('| A — Attori | Chi è coinvolto e quale ruolo esercita? | mappa delle responsabilità |','| A — Aree | Quali materie e responsabilità coinvolge lo scenario? | mappa delle aree e dei ruoli |')
 if code=='15':
  s=s.replace('Applica le quattro tabelle','Applica le cinque tabelle')
  s=s.replace('- **Organo:** soggetto o struttura cui l\'ordinamento imputa atti ed effetti.','- **Organo:** ufficio titolare di una competenza attraverso cui l’ente agisce; gli atti e i relativi effetti sono imputati all’ente secondo l’ordinamento.')
  s=s.replace('- **Competenza:** quota di funzione attribuita da una fonte; va distinta dalla mera esecuzione materiale.','- **Competenza amministrativa:** quota di funzione attribuita da una fonte; va distinta dalla mera esecuzione materiale.\n- **Competenza finanziaria:** criterio riferito alle entrate accertate e alle obbligazioni di spesa imputate all’esercizio secondo le regole contabili.\n- **Cassa:** profilo dei movimenti monetari dell’esercizio; per l’entrata statale distinguere riscossione e versamento.\n- **Residui attivi dello Stato:** entrate accertate non riscosse e riscosse non versate; non sono tutti denaro già disponibile in tesoreria.')
 fm,body=s.split('---',2)[1:]
 for field,value in [('status','revised_draft'),('draft_stage','revision-in-progress'),('review_required','true'),('updated_at','2026-10-03')]:fm=re.sub(r'^'+field+':.*$',field+': '+value,fm,flags=re.M)
 p.write_text('---'+fm+'---'+body,encoding='utf8')
(A/'VOL-03-FC01-quiz-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
print('60 quiz riscritti; soluzioni separate e ledger opzioni/chiavi/commenti salvato.')
