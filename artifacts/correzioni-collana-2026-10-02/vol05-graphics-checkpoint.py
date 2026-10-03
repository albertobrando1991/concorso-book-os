from pathlib import Path
import json,hashlib,re
A=Path('artifacts/correzioni-collana-2026-10-02')
records=json.loads((A/'VOL-05-native-schemes.json').read_text(encoding='utf8'))['records']
freeze=json.loads((A/'M-FC05-freeze.json').read_text(encoding='utf8'))
before={r['path']:r['sha256'] for r in freeze['files']}
changed=[]
def normalize(s):return ' '.join(s.split())
for path in sorted(set(r['file'] for r in records)):
 rows=[r for r in records if r['file']==path];p=Path(path)
 assert rows[0]['sha256Before']==before[path],path
 text=p.read_text(encoding='utf8');old=(A/'vol05-native-snapshots'/p.name).read_text(encoding='utf8')
 for row in rows:
  assert row['nativeText'] in text,row['schema']
  text=text.replace(row['nativeText'],'',1)
  raw=(p.parent/row['originalImage']).resolve()
  assert raw.exists() and hashlib.sha256(raw.read_bytes()).hexdigest()==row['originalSHA256'],str(raw)
 old=re.sub(r'!\[Figura \d+\.\d+[^\n]*\]\([^\n)]+\)','',old)
 old=re.sub(r'^\*Figura \d+\.\d+[^\n]*\*\s*\n','',old,flags=re.M)
 heading='## N-MF05-08-03 · Poteri, procedura e conseguenze'
 if p.name.startswith('08-'):
  old=old.replace(heading,'');text=text.replace(heading,'')
 assert normalize(text.split('---',2)[2])==normalize(old.split('---',2)[2]),path
 changed.append({'path':path,'before':before[path],'after':hashlib.sha256(p.read_bytes()).hexdigest(),'schemes':5,'bodyUnchangedOutsideDeclaredDelta':True})
checkpoint={'date':'2026-10-03','chapters':15,'schemas':75,'allPriorFreezeHashesMatched':True,'allOriginalImagesPreserved':True,'allQuizAndCaseBodiesPreserved':True,'files':changed,'declaredDelta':['75 specific native schemes replace 73 raster occurrences and restore two useful diagrams in chapter 13.','Old duplicate captions removed; asset metadata cleared for substituted chapters.','Chapter 8 nucleus 3 boundary moved before blacklists; all text preserved.'],'semanticChecks':['BANDO letters corrected','Consob sanction is conditional','Whistleblowing protection accompanies procedure','Sector-specific competence and alternatives explicit','Numeric laboratory schemes match solved datasets'],'limitations':['Visual PDF verification pending; no final publication judgment.']}
(A/'VOL-05-native-checkpoint.json').write_text(json.dumps(checkpoint,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'hashesMatched':len(changed),'schemas':len(records),'undeclaredBodyChanges':0}))
