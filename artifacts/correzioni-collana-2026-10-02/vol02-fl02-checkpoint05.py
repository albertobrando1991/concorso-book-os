from pathlib import Path
import re,json
base=Path('artifacts/correzioni-collana-2026-10-02')
module=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane')
files={n:next((module/'chapters').glob(n+'-*.md')) for n in ['09','10','11','12']}
p=files['12'];t=p.read_text(encoding='utf8')
if '### Elaborato completo: liquidazione del saldo' not in t:
 t=t.replace('### Laboratorio 2: profilo legislativo regionale',(base/'vol02-atto-regionale.txt').read_text(encoding='utf8')+'\n### Laboratorio 2: profilo legislativo regionale')
 t=t.replace('formalizzare progetto, responsabilità e identificativi richiesti;','nominare il RUP nel primo atto di avvio e formalizzare progetto e identificativi richiesti;')
 p.write_text(t,encoding='utf8')
for n,p in files.items():
 t=p.read_text(encoding='utf8').replace('review_required: false','review_required: true',1)
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
 refs=['sources/vol-02-area-vasta-organi-verifica-2026-10-03.md'] if n=='09' else ['sources/vol-02-scuole-espropri-spl-verifica-2026-10-03.md','sources/vol-09-governance-contratti-verifica-2026-10-03.md']
 topic='topics/vol-02-area-vasta-organi.md' if n=='09' else 'topics/vol-02-area-vasta-procedimenti-servizi.md'
 if n=='12':refs+=['sources/vol-02-coesione-pnrr-verifica-2026-10-03.md','sources/vol-02-contabilita-regionale-verifica-2026-10-03.md']
 for key,entries in [('source_refs',refs),('topics',[topic]),('last_compiled_from',['wiki/'+x for x in refs]+['wiki/'+topic])]:
  for entry in entries:
   line=re.search(r'^'+key+r':.*$',t,re.M).group()
   if entry not in line:t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m[1]+', "'+entry+'"]',t,count=1,flags=re.M)
 # Microcorrezione dei soli accostamenti lettera/numero nelle nuove frasi; non opera su ID, frontmatter o URL.
 head,body=t.split('\n---\n',1)
 for a,b in [('articolo107','articolo 107'),('articolo177','articolo 177'),('articolo16','articolo 16'),('articolo17','articolo 17'),('articolo20','articolo 20'),('articolo30','articolo 30'),('articolo27','articolo 27'),('articolo13','articolo 13'),('articolo21','articolo 21'),('comma60','comma 60'),('comma55','comma 55'),('comma67','comma 67'),('comma78','comma 78'),('comma22','comma 22'),('comma3','comma 3'),('comma5','comma 5'),('commi8','commi 8'),('commi1','commi 1'),('RegioneAlba','Regione Alba')]:body=body.replace(a,b)
 body=re.sub(r'\b(anni|al|dal|il|del|di|a|su|oltre|fino|supera|ne ha|Con)(?=\d)',r'\1 ',body)
 body=re.sub(r'(\d)(milioni|mila|sindaci|punti|anni|ottobre|settembre|gennaio|aprile)',r'\1 \2',body)
 body=body.replace('Legge11gennaio1996','Legge 11 gennaio 1996').replace('il2026','il 2026').replace('2026 e2027','2026 e 2027')
 p.write_text(head+'\n---\n'+body,encoding='utf8')
changes={
'V02-30':(['09'],'Organi provinciali e metropolitani: elettorato, durate, composizione, assemblea/conferenza, statuto e bilancio, caso numerico e quiz; deroga18mesi2025–2027.','L56 commi pertinenti e nota24 letti; controllo quorum10/30 e260000/500000; distinta durata4/2/5anni.'),
'V02-31':(['10','12'],'Anticipata nomina RUP al primo atto di avvio in tabelle, casi, sequenze, esercizi e soluzioni.','Confronto con art15 consolidato VOL09; ricerca nelle sequenze e verifica posizione prima della progettazione.'),
'V02-32':(['10'],'Riparto edilizia scolastica L23/1996; espropri con vincolo, PU, indennità, decreto condizionato a notifica/esecuzione e tre termini distinti.','L23art3 e DPR327art8/9/12/13/23/24 letti integralmente; prorogaPU vigente4anni, notifica7giorni con eccezione contestuale, esecuzione2anni.'),
'V02-33':(['11'],'Concessione e rischio operativo; in house con tre requisiti e caso80%; ambitoSPL; ricognizioni annuali e piano correttivo vigente, quiz.','D36art177,D175art2/16/20,D201art2/4/14/17/27/30/32 letti integralmente;83? no:8,2/10=82%; soglia oltre80 rigorosa.'),
'V02-34':(['12'],'Traccia digitalizzazione qualificata espressamente PNRR con obblighi ReGiS/DNSH dati e titolarità centrale distinta.','Coerenza con cap08 e fonte PNRR consolidata; non estesa disciplina a generico FESR.')}
sp=base/'VOL-02-changes.json';state=json.loads(sp.read_text(encoding='utf8'))
for fid,(ns,change,evidence) in changes.items():state['changes'][fid]={'files':[files[n].as_posix() for n in ns],'change':change,'evidence':evidence,'status':'Applicato; audit specialistico M-FL02 ancora aperto'}
x=state['changes']['V02-20'];x['files']=list(dict.fromkeys(x['files']+[files['12'].as_posix()]));x['change']+='; M-FL02/12: elaborato completo di liquidazione regionale con traccia, calcoli, premesse, dispositivo e griglia20punti.';x['evidence']+='; Contributo48000×80%=38400, anticipo16000, saldo22400 e riduzione1600 già disposta dopo contraddittorio.';x['status']='Parziale: laboratori comunale e regionale applicati; restano PL e simulazioni finali del volume'
sp.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
matrix=module/'planning/02-matrice-copertura-didattica.md';t=matrix.read_text(encoding='utf8')
for fid,(ns,change,evidence) in changes.items():
 if '| '+fid+' |' not in t:t+=f'| {fid} | {", ".join(ns)} | {change} | {evidence} | Applicato, audit15 aperto |\n'
t+='| V02-20 regionale | 12 | Elaborato completo liquidazione saldo regionale | Calcoli, presupposti, dispositivo, griglia20punti | Applicato, audit15 aperto |\n'
matrix.write_text(t,encoding='utf8')
mp=base/'normattiva-fl02/manifest.json';rows=json.loads(mp.read_text(encoding='utf8'))
for x in rows:
 if x['name'].startswith(('l23-','d327-','d201-','d175-','d36-art177')):x['readComplete']=True
 if x['name']=='l56-art1':x['readComplete']=False;x['readSections']='commi1–38,40–46,50–80; aggiornamento24'
mp.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Registrati V02-30–34 e V02-20 regionale')
