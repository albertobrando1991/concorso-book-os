from pathlib import Path
from datetime import date,timedelta
import re,json,hashlib,math
A=Path(__file__).parent; B=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue'); checks=[]
# Exact decimal tokens introduced by punctuation normalization. Leave enumerations intact.
decimals={4:['0, 50','0, 75','18, 75','7, 50','11, 25','61, 25','71, 25','81, 25','90, 25'],8:['0, 5','1, 5','0, 001','4, 5','2, 4'],12:['0, 25','0, 50','0, 75'],14:['0, 001','0, 5','1, 5','0, 1','0, 50']}
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');n=int(p.name[:2])
 for v in sorted(decimals.get(n,[]),key=len,reverse=True):t=t.replace(v,v.replace(', ',','))
 t=re.sub(r'\b(L|SF) ([123])\b',r'\1\2',t)
 p.write_text(t,encoding='utf8')
def has(n,s):
 t=next((B/'chapters').glob(f'{n:02}-*.md')).read_text(encoding='utf8');assert s in t,(n,s)
def check(name,actual,expected):
 assert math.isclose(actual,expected,rel_tol=1e-10),(name,actual,expected)
 checks.append({'case':name,'actual':actual,'expected':expected})
check('Valore con rinnovo e opzione',144000+72000+18000,234000);has(3,'234.000')
check('Tetto piccoli lotti',234000*.2,46800);has(3,'46.800')
check('OEPV A',25*.75+20+20*.75+15*.5+20,81.25);has(4,'81,25')
check('OEPV B',25+20*.75+20+15*.75+20*190000/200000,90.25);has(4,'90,25')
check('Cumulo modifiche servizi',(18000+8000)/200000*100,13);has(8,'13%')
check('Penale esecuzione',200000*.001*8,1600);has(8,'1.600')
check('Revisione lavori',400000*(.08-.03)*.9,18000);has(8,'18.000')
check('Revisione servizi',100000*(.08-.05)*.8,2400);has(8,'2.400')
check('Anticipazione',200000*.2,40000);has(8,'40.000')
check('Contributo', (122000-22000-10000)*.8,72000);has(11,'72.000')
check('Quadratura fattura',72000+18000+10000+22000,122000);has(11,'50.000')
for extra,score in zip(range(5),[0,2,4,6,8]):check(f'CAM anni aggiuntivi {extra}',min(extra/4,1)*8,score)
check('Penale simulazione',100000*.001*10,1000);has(14,'1.000 euro')
check('Target funzionale',92/100*100,92);has(14,'92')
check('Doppio finanziamento eccedenza',60000+60000-100000,20000)
deps={'A':[],'B':['A'],'C':['A'],'D':['B','C'],'E':['B'],'F':['D','E']}
def network(b=4,c=3):
 dur={'A':2,'B':b,'C':c,'D':2,'E':1,'F':1};ef={};es={}
 for k in dur:es[k]=max([ef[d] for d in deps[k]] or [0]);ef[k]=es[k]+dur[k]
 return ef['F']
for b,c,expected in [(4,3,9),(4,4,9),(4,5,10),(6,3,11)]:check(f'Rete B={b} C={c}',network(b,c),expected)
days=[];d=date(2026,10,6)
while len(days)<11:
 if d.weekday()<5:days.append(d.isoformat())
 d+=timedelta(days=1)
assert [days[i-1] for i in [9,10,11]]==['2026-10-16','2026-10-19','2026-10-20']
has(14,'preparazione e bonifica dei dati')
missing=[];internal=[];hashes={};nuclei=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');body=t.split('---',2)[2];hashes[p.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
 internal.extend((p.name,x) for x in re.findall(r'\[\[(?:sources|topics|entities|raw|planning|reviews)/[^\]]+',body))
 for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',body):
  if not ref.startswith(('http','data:')) and not any(q.exists() for q in [p.parent/ref,Path(ref.lstrip('/')),Path('wiki')/ref.lstrip('/')]):missing.append((p.name,ref))
 nuclei+=re.findall(r'^## (N-TR02-\d{2}-\d{2})',body,re.M)
assert not internal,internal
assert not missing,missing
assert len(nuclei)==len(set(nuclei))==73
# Refresh literal evidence only; preserve the reviewed matrix and index.
mf=B/'planning/10-manifest-nuclei-format-2.json';m=json.loads(mf.read_text(encoding='utf8'))
for r in m['nuclei']:
 t=(B/'chapters'/r['file']).read_text(encoding='utf8');section=t.split('## '+r['id']+' · ',1)[1].split('\n## N-TR02-',1)[0]
 paragraphs=[x.strip() for x in section.split('\n\n')[1:] if len(x.strip())>100 and not x.lstrip().startswith(('#','|','!['))]
 r['evidenceQuote']=paragraphs[0] if paragraphs else section.strip()[:500]
mf.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf8')
out={'status':'passed','numericChecks':checks,'workDates':days,'nuclei':73,'chapters':14,'missingImages':missing,'internalReaderReferences':internal,'chapterHashes':hashes,'limits':'Calcoli ed evidenze testuali indicati; non certifica norme o PDF.'}
(A/'VOL-09-verifica-esempi.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print({'status':'passed','calculations':len(checks),'chapters':14,'nuclei':73,'missingImages':0,'internalReaderReferences':0})
