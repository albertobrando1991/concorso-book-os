from pathlib import Path
import re,json
module=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane')
files={n:next((module/'chapters').glob(n+'-*.md')) for n in ['07','08']}
for n,p in files.items():
 t=p.read_text(encoding='utf8').replace('review_required: false','review_required: true',1)
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
 refs=['sources/vol-02-coesione-pnrr-verifica-2026-10-03.md']
 if n=='08':refs+=['sources/vol-09-pnrr-architettura-chiusura-regis-2026-10-03.md','sources/vol-09-dnsh-cam-casi-verificati-2026-10-03.md']
 for key,entries in [('source_refs',refs),('topics',['topics/vol-02-coesione-pnrr-casi.md']),('last_compiled_from',['wiki/'+x for x in refs]+['wiki/topics/vol-02-coesione-pnrr-casi.md'])]:
  for entry in entries:
   line=re.search(r'^'+key+r':.*$',t,re.M).group()
   if entry not in line:t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m[1]+', "'+entry+'"]',t,count=1,flags=re.M)
 p.write_text(t,encoding='utf8')
changes={
'V02-27':('07','Esplicitati regolamenti 1060/1058/1057/1056/1059, AdG/AdA e funzione contabile; costi reali/unitari/somme/tassi, limiti e tre esempi con quiz; test aiuti107TFUE.','RDC consolidato 1luglio2026 artt53/54/71–77 letti via browser; calcoli22000−2000=20000,180×100=18000,40000×7%=2800.'),
'V02-28':('08','Titolarità centrale della misura distinta da attuazione/coordinamento regionale in tabella e risposta modello; chiarita titolarità del progetto.','DL77/2021 artt8–9 riscontrati Camera e soggetti attuatori Ministero salute; circolare4/2022 chiarisce lessico.'),
'V02-29':('08','Corretto quiz doppio finanziamento senza condizione fonti incompatibili; esempio quote60/40 e duplicazione100/100; basi DNSH; scadenze2026, ReGiS e caso92/100.','Art9RRF nel raw acquisito; note VOL09 chiusura/DNSH verificate e riusate; data aggiornamento3ottobre, termini agosto/settembre presentati trascorsi.')}
statepath=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');state=json.loads(statepath.read_text(encoding='utf8'))
for fid,(n,change,evidence) in changes.items():state['changes'][fid]={'files':[files[n].as_posix()],'change':change,'evidence':evidence,'status':'Applicato; audit specialistico M-FL02 ancora aperto'}
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
matrix=module/'planning/02-matrice-copertura-didattica.md';t=matrix.read_text(encoding='utf8')
for fid,(n,change,evidence) in changes.items():
 if '| '+fid+' |' not in t:t+=f'| {fid} | {n} | {change} | {evidence} | Applicato, audit15 aperto |\n'
matrix.write_text(t,encoding='utf8')
print('Registrati V02-27–29')
