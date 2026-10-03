from pathlib import Path
import re,json
p=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane/chapters/02-statuti-organi-organizzazione-regionale.md')
t=p.read_text(encoding='utf8').replace('review_required: false','review_required: true',1)
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
for key,entry in [('source_refs','sources/vol-02-regioni-statuti-competenze-verifica-2026-10-03.md'),('topics','topics/vol-02-statuti-organi-regionali-casi.md')]:
 t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m[1]+', "'+entry+'"]',t,count=1,flags=re.M)
t=t.replace('- Costituzione della Repubblica italiana, in particolare le disposizioni sullo statuto e sugli organi regionali.','- Costituzione della Repubblica italiana, artt. 121–123 e 126: organi, elezione, procedimento statutario, sfiducia e scioglimento.')
p.write_text(t,encoding='utf8')
statepath=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');state=json.loads(statepath.read_text(encoding='utf8'))
state['changes']['V02-21']={'files':[str(p).replace('\\','/')],'change':'Procedimento statutario123 con quorum, intervallo, ricorso e referendum; elezione122 e crisi126; casi31componenti e sfiducia, due nuovi quiz commentati.','evidence':'PDF ufficiale Quirinale artt122/123/126 letto; caso16voti su31 e intervallo40giorni insufficiente; quiz7C/8D motivati. Fonte/topic consolidati prima della scrittura.','status':'Applicato; audit specialistico M-FL02 ancora aperto'}
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('V02-21 registrato')
