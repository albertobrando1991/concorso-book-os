from pathlib import Path
import re,json
s='vol-04-processo-penale-verifica-2026-10-03'
delta=f'''\n## Processo penale — verifica 3 ottobre 2026

Fonte: [[sources/{s}]]. Distinti indagato/imputato, offeso/parte civile, iscrizione335/annotazione335-quinquies e modello45-bis; consolidate indagini, archiviazione, avviso415-bis e interrogatorio richiesto, filtri425/554-ter, fascicolo dibattimentale selettivo431, riti speciali e termini585. Il supporto UPP ordinario è presso gli uffici giudicanti previsti dalla legge, non presso ogni Procura. Il registro non attribuisce colpevolezza; previsione di condanna non equivale alla prova oltre ogni ragionevole dubbio. Esecuzione655/665 distinta dalla cautela; soglie656 richiedono coordinamento con pronunce costituzionali.

Capitoli: [[books/moduli/m-fc04-giustizia/chapters/07-processo-penale-operativo-upp-cancelleria]], [[books/moduli/m-fc04-giustizia/chapters/08-servizi-cancelleria-registri-comunicazioni-certificazioni]].
'''
for f in ['wiki/topics/giustizia-e-upp.md','wiki/entities/ufficio-per-il-processo.md','wiki/entities/ministero-della-giustizia.md']:
 p=Path(f);t=p.read_text('utf-8')
 if s not in t:
  t=t.replace('source_refs: [',f'source_refs: ["sources/{s}.md", ',1)
  t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1)
  p.write_text(t+delta,'utf-8')
p=Path('wiki/index.md');t=p.read_text('utf-8')
if s not in t:p.write_text(t+f'\n- [[sources/{s}]] — regole processuali penali, riti, termini e registro45-bis.\n','utf-8')
with Path('wiki/log.md').open('a',encoding='utf-8') as f:f.write('\n\n## 2026-10-03 — Consolidamento processo penale VOL04\n\nLetti articoli CPP e circolare7maggio2026; source penale collegata a topic/entità. Rilevata omissione parser del pre-comma533c1, verificato HTML ufficiale. Nuova annotazione45-bis distinta da iscrizione e archiviazione. Preparazione integrazione07–08; nessun gate finale chiuso.\n')
A=Path('artifacts/correzioni-collana-2026-10-02/norme-vol04')
read=set(map(str,[60,61,64,74,90,172,190,192,329,335,'335quinquies',405,406,407,408,409,410,'415bis',416,425,431,432,438,442,444,445,449,453,459,460,533,544,548,550,'554bis','554ter',585,593,648,650,655,656,665,666]))
for name in ['manifest.json','manifest-penale-extra.json']:
 p=A/name;rows=json.loads(p.read_text('utf-8'))
 for r in rows:
  if r['name']=='cpp' and str(r.get('article')) in read:
   r['readComplete']=True;r['reviewNote']='Letto per source processo penale 2026-10-03; 533c1 anche HTML, 656 soglie non consolidate senza note costituzionali.'
  if r['name']=='circolare45bis':r['readComplete']=True
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
print('Fonte penale consolidata e letture tracciate')
