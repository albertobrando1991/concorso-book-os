from pathlib import Path
import json,re
base=Path('wiki/books/moduli/m-fl01-comuni-unioni/chapters')
source='vol-02-servizi-comunali-verifica-2026-10-02';topic='vol-02-servizi-comunali-documenti-welfare'
for n in (5,6,7,8):
 p=next(base.glob(f'{n:02d}-*.md'));s=p.read_text(encoding='utf8')
 s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M)
 s=re.sub(r'^review_required:.*$','review_required: true',s,flags=re.M)
 for key,refs in [('source_refs',[f'sources/{source}.md']),('last_compiled_from',[f'wiki/sources/{source}.md',f'wiki/topics/{topic}.md'])]:
  for ref in refs:s=re.sub(rf'^({key}: \[)(.*)(\])$',lambda m:m[1]+m[2]+(', '+json.dumps(ref) if ref not in m[2] else '')+m[3],s,flags=re.M)
 p.write_text(s,encoding='utf8')
p=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');d=json.loads(p.read_text(encoding='utf8'))
changes={
'V02-07':([5,8],'Divieto art26c4 specifico per salute/disagio e distinzione pubblicazione/comunicazione/accesso.','Garante2014 e2025; casi anonimizzazione e accesso civico semplice confrontati.'),
'V02-08':([6],'Definiti documento informatico, forma/prova e copie; separati effetti e obblighi documentali.','CAD20 DocsItalia versione20aprile2026; controesempio omissione protocollo senza annullamento automatico istanza.'),
'V02-09':([7],'Decertificazione come regola obbligatoria, coordinata in teoria, risposta e soluzione stato famiglia.','Funzione pubblica artt40/43; riesame della richiesta insistita del cittadino.'),
'V02-10':([7],'Dimora abituale,2giorni/45giorni/decorrenza; AIRE90giorni, revisioni elettorali, estratti e copie con casi.','Fonti Interno/MAECI/DAIT; calendario5–7ottobre2026 e distinzione assenza occasionale/dimora; copia minore motivata.'),
'V02-11':([8],'Separate decadenza/revoca/annullamento e rapporti appalto/accreditamento/CTS55/56; due casi risolti.','DM72/2021 e ANACart6; riesame APS iscritta2mesi e acquisto2000ore; revoca vantaggio non per mero ripensamento.')}
for fid,(ns,change,evidence) in changes.items():d['changes'][fid]={'files':[str(next(base.glob(f'{n:02d}-*.md'))).replace('\\','/') for n in ns],'change':change,'evidence':evidence,'status':'applicato'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
