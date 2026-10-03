from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def refs(p):
 s=p.read_text(encoding='utf8');s=s.lstrip('\ufeff');front=s.split('---',2)[1] if s.startswith('---') else ''
 found=set(re.findall(r'(?:wiki/)?(sources/[A-Za-z0-9_.-]+(?:\.md)?)',front))
 found.update(re.findall(r'\[\[(?:wiki/)?(sources/[^\]|#]+)',s))
 return {r if r.endswith('.md') else r+'.md' for r in found}
for v,prefix in [('06','ir'),('07','sa'),('12','sp')]:
 out=Path(f'delivery/VOL-{v}/candidate-2026-10-03');manifest=json.loads((out/'manifest.json').read_text(encoding='utf8'))
 originals=[]
 for i in range(1,5):
  module=next(Path('wiki/books/moduli').glob(f'm-{prefix}{i:02}-*'))
  originals.extend(module.joinpath('chapters').glob('*.md'));originals.extend(module.joinpath('planning').glob('*matrice*.md'))
 todo=[(p,p) for p in originals];seen=set();edges=[];missing=[]
 while todo:
  p,origin=todo.pop()
  if p in seen:continue
  seen.add(p)
  for r in refs(p):
   target=Path('wiki')/r;exists=target.exists();packaged=(out/target).exists()
   row={'from':p.as_posix(),'to':target.as_posix(),'exists':exists,'packaged':packaged,'direct':p in originals}
   edges.append(row)
   if not exists or not packaged:missing.append(row)
   elif target not in seen:todo.append((target,origin))
 audit={'volume':'VOL-'+v,'scope':'Dipendenze sources dichiarate nel frontmatter o in wikilink dei capitoli/matrici, e dipendenze delle source note raggiunte. URL esterni esclusi.','edges':edges,'issues':missing}
 dst=A/f'VOL-{v}-package-source-graph.json';dst.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(out/dst).write_bytes(dst.read_bytes())
 manifest['unresolvedReferencedNotes']=sorted({x['to'] for x in missing});manifest['sourceGraphAudit']=dst.as_posix();manifest['directSourceGraphIssues']=[x for x in missing if x['direct']]
 manifest['files']=[{'path':p.relative_to(out).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file() and p.name!='manifest.json']
 (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 assert all(sha(out/f['path'])==f['sha256'] for f in manifest['files'])
 print(json.dumps({'volume':v,'sourceEdges':len(edges),'issues':missing,'filesVerified':len(manifest['files'])},ensure_ascii=False))
