from pathlib import Path
import re,json,hashlib
root=Path('.');out=Path('artifacts/correzioni-collana-2026-10-02');rows=[]
for n in (13,14):
 p=next(Path('wiki/books/moduli/m-fc04-giustizia/chapters').glob(f'{n}-*.md'));s=p.read_text(encoding='utf8')
 qs=re.findall(r'(?ms)^\*\*Q(\d+)\..*?(?=^\*\*Q\d+\.|^### |\Z)',s)
 blocks=re.findall(r'(?ms)^\*\*Q\d+\..*?(?=^\*\*Q\d+\.|^### |\Z)',s)
 assert len(blocks)==6
 for b in blocks:
  assert re.findall(r'(?m)^([ABCD])\) ',b)==list('ABCD')
  assert len(re.findall(r'\*\*Risposta [ABCD]\.\*\*',b))==1
 keys=re.findall(r'\*\*Risposta ([ABCD])\.\*\*',s)
 assert len(set(keys))==4
 assert 'adeguatamente informati' not in s and '| Si |' not in s and 'Non serve qui sviluppare tutte le soglie' not in s
 fm=s.split('---',2)[1]
 refs=re.findall(r'"((?:sources|topics)/[^"\n]+\.md)"',fm)
 missing=[r for r in refs if not Path('wiki',r).exists()];assert not missing,missing
 assert '[[sources/' not in s.split('---',2)[2]
 rows.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(s.split()),'readComplete':True,'quizCount':6,'quizKeys':keys,'quizOptions':'ABCD','quizReview':'complete','linkedDependenciesExist':True,'pdfReview':'pending','scope':'current chapter text and changed normative claims; not certification of whole legal system'})
assert 60//10==6 and 60*8==480
result={'volume':'VOL-04','chapters':[13,14],'checks':'passed','rows':rows,'workedCalculations':{'sixtyDaysReduction':6,'sixtyDaysMoney':480},'unchangedScope':['chapter15','chapters01-12','run-state','historical-audit'],'limitations':['No new PDF inspected','Therapeutic special regimes cited as distinct, not exhaustive clinical/legal manual','Source acquisition errors explicitly excluded in source note']}
(out/'VOL-04-cap13-14-verifica.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2))
