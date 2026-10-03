from pathlib import Path
import re,json
module=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane');files={n:next((module/'chapters').glob(n+'-*.md')) for n in ['04','05','06']}
for p in files.values():
 t=p.read_text(encoding='utf8').replace('review_required: false','review_required: true',1)
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
 for key,entry in [('source_refs','sources/vol-02-contabilita-regionale-verifica-2026-10-03.md'),('topics','topics/vol-02-ciclo-finanziario-regionale.md')]:
  t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m[1]+', "'+entry+'"]',t,count=1,flags=re.M)
 p.write_text(t,encoding='utf8')
statepath=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');state=json.loads(statepath.read_text(encoding='utf8'))
changes={
'V02-23':('04','Sequenza esplicita del saldo con controllo prima della liquidazione, poi mandato e pagamento; eventualità di integrazione/revoca; imperativi uniformati.','Art57/58D118 acquisiti e letti, soluzione ordinata confrontata con caso e tabella.'),
'V02-24':('05','Calendario regionale con DEFR, bilancio, doppia fase rendiconto, assestamento e consolidato31ottobre; liquidazione distinta da ordinazione/pagamento; caso numerico saldo.','Artt18/36/39/50/57/58/63/68D118 letti; paginaistituzionaleDEFR; saldo18000−8000=10000, confrontoComune/Regione.'),
'V02-25':('06','Ripristinati A=Aree,D=Diario,O=Output e raccordo metodologico Diario/Output.','Confronto con struttura madre e mappa BANDO degli altri capitoli.'),
'V02-26':('06','Clausola finanziaria con ipotesi esplicite, importi peranno e mezzo di copertura; termine90giorni con decorrenza; transitorio comprende data iniziale.','Art81Cost e fonte contabilità consolidata; modello100000/80000/60000 con riduzione corrispondente, totale240000; distinzione diritto/tetto discrezionale.')}
for fid,(n,change,evidence) in changes.items():state['changes'][fid]={'files':[str(files[n]).replace('\\','/')],'change':change,'evidence':evidence,'status':'Applicato; audit specialistico M-FL02 ancora aperto'}
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
manifest=Path('artifacts/correzioni-collana-2026-10-02/normattiva-fl02/manifest.json');rows=json.loads(manifest.read_text(encoding='utf8'))
for x in rows:
 if x['name'].startswith('d118-'):x['readComplete']=True
manifest.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
matrix=module/'planning/02-matrice-copertura-didattica.md';t=matrix.read_text(encoding='utf8')
for fid,(n,change,evidence) in changes.items():t+=f'| {fid} | {n} | {change} | {evidence} | Applicato, audit15 aperto |\n'
matrix.write_text(t,encoding='utf8')
print('Registrati V02-23–26')
