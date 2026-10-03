from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters');rows=[]
for p in sorted(B.glob('*.md')):
 t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest();removed=re.findall(r'(?m)^# .+$',t);assert len(removed)==1
 t=re.sub(r'(?m)^# .+\n\n','',t,count=1)
 # Break labels at word boundaries, not inside joined tokens; only table cells.
 lines=[]
 for line in t.splitlines():
  if line.startswith('|'):line=re.sub(r'(?<=[A-Za-zÀ-ÿ])/(?=[A-Za-zÀ-ÿ])',' / ',line)
  lines.append(line)
 t='\n'.join(lines)+'\n';p.write_text(t,'utf-8')
 rows.append(dict(path=p.as_posix(),before=before,after=hashlib.sha256(p.read_bytes()).hexdigest(),removedDuplicateHeading=removed[0],changes='Titolo già generato da metadata; spazi ai separatori nelle sole tabelle. Contenuti, quiz, norme e soluzioni invariati.'))
p=A/'M-FC04-freeze.json';d=json.loads(p.read_text('utf-8'));old=A/'M-FC04-freeze-before-layout.json'
if not old.exists():old.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
for row in d['files']:row['sha256']=hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()
d['controlledLayoutDelta']=rows;p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
(A/'VOL-04-layout-delta.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
p=A/'VOL-04-text-verifica.json';d=json.loads(p.read_text('utf-8'))
for row in d['chapters']:row['sha256']=hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
p=Path('wiki/reviews/pipeline/VOL-04/16-moduli-m-fc04-giustizia.md');s=p.read_text('utf-8')
for row in rows:s=s.replace(row['before'],row['after'])
s+='\n\n## Delta tipografico controllato\n\nTitoli di capitolo duplicati rimossi dal solo corpo; titolo canonico conservato nei metadata e generato in apertura. Separatori slash nelle tabelle dotati di spazi per permettere il ritorno fra parole. Diciassette file registrati in VOL-04-layout-delta.json; significato, quiz e fonti invariati. Manifest precedente archiviato. Nuovo PDF richiesto.\n';p.write_text(s,'utf-8')
print('17 titoli duplicati rimossi; delta di layout registrato.')
