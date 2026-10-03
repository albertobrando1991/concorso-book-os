from pathlib import Path
import json,re,hashlib
B=Path('wiki/books/moduli/m-ir01-scuola');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06')
for name in ['index.md','planning/02-matrice-copertura-didattica.md']:
 p=B/name;t=p.read_text();t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M)
 if name=='index.md':
  t=t.replace('editorial_revision','text_frozen').replace('editorial-revision','text-frozen').replace('testo corretto; audit specialistico e PDF da completare','testo corretto e audit specialistico concluso; nuovo PDF da verificare').replace('Correzioni autorizzate del 3 ottobre 2026 presenti; audit specialistico e verifica del nuovo impaginato sono tracciati separatamente nella pipeline.','Correzioni autorizzate del 3 ottobre 2026 presenti; audit specialistico passed. Manifest del testo corrente nello step 16. Il nuovo impaginato deve essere verificato prima della pubblicazione.')
 else:t+='\n### Chiusura dell’audit testuale\n\nStep 15 passed senza blocker o warning il 3 ottobre 2026. Il manifest dello step 16 documenta il testo corrente; il controllo PDF resta distinto.\n'
 p.write_text(t,encoding='utf8')
entries=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text();assert 'review_required: false' in t
 body=t.split('\n---\n',1)[1];assert not re.search(r'\[\[(sources|topics|entities|planning|raw|reviews)/',body)
 entries.append({'path':str(p).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03','words':len(re.findall(r"\b[\w’]+\b",body))})
assert len(entries)==13
manifest={'volume':'VOL-06','module':'M-IR01','date':'2026-10-03','verification':'manuale del manifest; stato CLI registrato separatamente','files':entries,'checks':['13 capitoli canonici presenti e collegati nell’indice.','Matrice riconciliata con teoria, casi e verifiche del perimetro dichiarato.','Audit15 passed, zero blocker e warning.','V06-01–08 e quota scolastica23/33/35 corretti; Humanizer e micro-revisione dei delta.','Fonti e data dichiarate; D.L.170/2026 vigente, senza anticipare conversione.','Nessun collegamento staff nel corpo.'],'limitations':['Formato legacy conservato, non attestato formato2.','Nuovo PDF non ancora verificato.','Altri moduli del volume in correzione; nessuna pubblicabilità complessiva.']}
(A/'M-IR01-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'16-moduli-m-ir01-scuola.md';arc=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-16-m-ir01.md')
if not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('# M-IR01 — Manifest del testo, 3 ottobre 2026\n\nVerifica manuale; esito del gate CLI registrato separatamente.\n\n'+'\n'.join('- '+x for x in manifest['checks'])+'\n\n| File | Stato | Data | SHA-256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+e['path']+' | text-freeze | '+e['date']+' | '+e['sha256']+' |' for e in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
print('Manifest IR01, 13 capitoli, parole',sum(e['words'] for e in entries))
