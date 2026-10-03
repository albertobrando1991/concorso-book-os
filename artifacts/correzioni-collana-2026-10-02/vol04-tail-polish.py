from pathlib import Path
import json,re,hashlib,shutil
A=Path(__file__).parent; B=Path('wiki/books/moduli/m-fc04-giustizia/chapters');rows=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for prefix in ['02-','07-']:
 p=next(B.glob(prefix+'*.md'));t=p.read_text('utf8');old=t.strip().split('\n')[-1]
 assert old.startswith('Se una risposta è incerta,')
 new='Annota nel diario le distinzioni incerte e ripassa le relative funzioni.'
 backup=A/'vol04-tails-before'/p.name;backup.parent.mkdir(exist_ok=True);shutil.copy2(p,backup)
 before=sha(p);p.write_text(t.replace(old,new),'utf8');rows.append(dict(path=p.as_posix(),before=before,after=sha(p),old=old,new=new,reason='Richiamo ripetitivo al diario condensato; distinzioni già sviluppate nel capitolo e nella checklist. Nessuna modifica a norme, quiz o soluzioni.'))
f=A/'M-FC04-freeze.json';d=json.loads(f.read_text('utf8'))
for row in d['files']:row['sha256']=sha(Path(row['path']))
d['controlledTailPolish']=rows;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
(A/'VOL-04-tail-polish.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
p=A/'VOL-04-text-verifica.json';d=json.loads(p.read_text('utf8'))
for row in d['chapters']:row['sha256']=sha(Path(row['path']))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
print('2 finali sintetizzati; quiz e norme invariati')
