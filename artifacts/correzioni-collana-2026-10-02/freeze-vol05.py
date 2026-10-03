from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');R=Path('wiki/reviews/pipeline/VOL-05')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
chapters=sorted((B/'chapters').glob('*.md'));assert len(chapters)==15
assert not json.loads((A/'VOL-05-FC05-links.json').read_text(encoding='utf8'))
g=json.loads((A/'VOL-05-FC05-gates.json').read_text(encoding='utf8'));assert len(g)==15 and all(x['result']['passed'] and not x['result']['warnings'] for x in g)
assert sum(len(re.findall(r'\*\*Quesito \d',p.read_text(encoding='utf8'))) for p in chapters)==90
for p in chapters:
 s=p.read_text(encoding='utf8');assert 'review_required: false' in s;s=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',s,flags=re.M);p.write_text(s,encoding='utf8')
p=B/'index.md';s=p.read_text(encoding='utf8');s+='\n## Congelamento del testo\n\nTesto verificato al 3 ottobre 2026; audit 14 e 15 superati. Freeze 16 manuale con manifest SHA-256 perché il gate automatico non è implementato. Trentatré rilievi testuali chiusi; schemi, PDF aggiornato e pacchetto finale in lavorazione. Ogni modifica sostanziale riapre i gate pertinenti.\n';p.write_text(s,encoding='utf8')
ledger=json.loads((A/'VOL-05-ledger.json').read_text(encoding='utf8'))
# Seven-column audit contract, retaining exact diagnostic positions.
table='| ID | File e posizione | Categoria | Gravità | Evidenza consolidata | Correzione applicata | Stato finale |\n|---|---|---|---|---|---|---|\n'
for r in ledger['findings']:
 n=int(r['id'][-2:]);category='Didattica e struttura' if n in [1,2,3,4,8,13,30,31,32,33] else 'Normativa e procedura';r['category']=category;r['evidence']='Note di verifica VOL-05 del 3 ottobre 2026, fonti nel frontmatter; gate e calcoli nel ledger';r['status']='Risolto nel testo; PDF separato'
 table+='| '+' | '.join([r['id'],r['position'],category,r['severity'],r['evidence'],r['correction'],r['status']])+' |\n'
for p in [Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-05.md'),R/'14-moduli-m-fc05-authority-indipendenti.md',R/'15-moduli-m-fc05-authority-indipendenti.md']:
 s=p.read_text(encoding='utf8');a=s.index('| ID |');b=s.index('\n## 4.',a);s=s[:a]+table+s[b:];s=s.replace('Chiudere audit specialistico e freeze tramite CLI;','Audit specialistico 14/15 superato e freeze 16 manuale documentato;');p.write_text(s,encoding='utf8')
files=chapters+[B/'index.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/03-bibbia-del-modulo.md',B/'planning/00-piano-editoriale.md',Path('wiki/books/vol-05-authority-regolazione/index.md'),Path('wiki/topics/authority-rettifiche-2026.md')]+sorted(Path('wiki/sources').glob('vol-05-*-verifica-2026-10-03.md'))+[Path('wiki/sources/vol-05-bandi-authority-2022-2025.md'),Path('wiki/sources/vol-05-aggiornamento-specialistico-2026-08-22.md')]
checks=['15 capitoli letti integralmente nella baseline e modifiche riesaminate nel contesto.','33 ID testuali risolti; 90 quesiti aperti, 15 casi finali e 10 simulazioni verificati.','75 nuclei e 15 unità aggregate corretti; nessuno stato di copertura incompleto.','15 gate di capitolo senza blocker o warning; audit CLI 14 e 15 superati.','Rinvii del corpo risolti, indice e percorsi coerenti.','Humanizer e micro-revisione dei passaggi sostanziali completati; niente stampi generici nelle verifiche.','Fonti consolidate con lettura mirata dichiarata, data 3 ottobre 2026.','Gate text-freeze non implementato: verifica manuale eseguita senza simularne automazione.']
manifest={'volume':'VOL-05','module':'M-FC05','date':'2026-10-03','verification':'manuale dopo gate-not-implemented','checks':checks,'files':[{'path':p.as_posix(),'sha256':sha(p),'status':'text-frozen'} for p in files],'limitations':['Figure e PDF in lavorazione; pubblicabilità finale non attestata.','Nessun commit o pubblicazione. Riscontri normativi limitati ai passaggi documentati.']};save(A/'M-FC05-freeze.json',manifest)
text='# M-FC05 — Freeze del testo, 3 ottobre 2026\n\nVerifica manuale del gate non implementato, audit 14 e 15 superati.\n\n'+'\n'.join('- '+x for x in checks)+'\n\n| File | Stato | SHA-256 |\n|---|---|---|\n'+''.join('| '+r['path']+' | text-frozen | '+r['sha256']+' |\n' for r in manifest['files'])+'\n## Limiti\n\n'+' '.join(manifest['limitations'])+'\n'
for p in [R/'16-moduli-m-fc05-authority-indipendenti.md',B/'planning/18-text-freeze-manifest.md']:p.write_text(text,encoding='utf8')
for r in ledger['files']:r['sha256']=sha(Path(r['path']))
ledger.update(freezeManifest=(A/'M-FC05-freeze.json').as_posix(),textVerified=True,finalVerified=False);save(A/'VOL-05-ledger.json',ledger)
p=A/'VOL-05-reading-checkpoint.json';d=json.loads(p.read_text(encoding='utf8'));d['frozenFiles']=[r for r in manifest['files'] if '/chapters/' in r['path']];save(p,d)
p=A/'VOL-05-progress.json';d=json.loads(p.read_text(encoding='utf8'));d['textStatus']='33 rilievi chiusi; audit 14/15 superati e freeze manuale';d['pending']=['Chiusura CLI 16','Schemi nativi specifici','Prova PDF e pacchetto'];save(p,d);print('Manual freeze prepared:',len(files),'files.')
