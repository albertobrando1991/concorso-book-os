from pathlib import Path
import json
s='vol-04-cancelleria-verifica-2026-10-03'
delta=f'''\n\n## Registri, accesso e dati — 3 ottobre 2026

Fonte: [[sources/{s}]]. Registri SICID/SIECIC/SICP e modelli21/44/45/45-bis distinti; accesso civile76disp.att.CPC e copie116CPP dipendono da titolo e competenza; art475 comprende copia conforme o duplicato informatico. Dati9/10GDPR distinti, D.Lgs51/2018 applicabile secondo autorità e finalità. Capitolo08: [[books/moduli/m-fc04-giustizia/chapters/08-servizi-cancelleria-registri-comunicazioni-certificazioni]].
'''
for f in ['wiki/topics/giustizia-e-upp.md','wiki/entities/ministero-della-giustizia.md','wiki/entities/ufficio-per-il-processo.md']:
 p=Path(f);t=p.read_text('utf-8')
 if s not in t:p.write_text(t.replace('source_refs: [',f'source_refs: ["sources/{s}.md", ',1)+delta,'utf-8')
p=Path('wiki/index.md');t=p.read_text('utf-8')
if s not in t:p.write_text(t+f'\n- [[sources/{s}]] — registri, accesso processuale, copie e dati personali.\n','utf-8')
with Path('wiki/log.md').open('a',encoding='utf-8') as f:f.write('\n\n## 2026-10-03 — Fonti cancelleria VOL04\n\nConsolidati artt76disp.att.CPC,116CPP,475CPCconduplicato,GDPR9/10eD.Lgs51. Distinti registri e applicativi, modello45bis aggiornato. Sezioni storiche2016 utilizzate per tassonomia senza trasferire le regole processuali superate.\n')
p=Path('wiki/sources/vol-04-aggiornamento-normativo-2026-08-18.md');t=p.read_text('utf-8')
t=t.replace('siano formati in copia attestata conforme all\'originale per valere','siano rilasciati in copia attestata conforme all\'originale o in duplicato informatico per valere')
if s not in t:t+=f'\nIntegrazione del3ottobre2026: [[sources/{s}]] verifica il testo attuale dell’art.475, comprendente il duplicato informatico.\n'
p.write_text(t,'utf-8')
A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol04')
for name in ['manifest.json','manifest-cancelleria-extra.json']:
 p=A/name;rows=json.loads(p.read_text('utf-8'))
 for r in rows:
  if (r['name']=='privacy-penale' or (r['name']=='cpp' and r.get('article')==116) or (r['name']=='cpc' and r.get('article')==475) or (r['name']=='disp-cpc' and r.get('article')==76)):r['readComplete']=True
  if r['name']=='registri-penali-circolare2016':r['readScope']='Sezioni8–14a; tassonomia, non regole processuali storiche'
  if r['name']=='registri-civili-statistiche':r['readScope']='Definizioni SICID/SIECIC annualità2025'
  if r['name']=='sistema-sicp':r['readScope']='Definizione e componenti; cronoprogramma storico non riutilizzato'
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
print('Collegamenti e rettifica475 consolidati')
