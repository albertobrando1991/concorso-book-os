from pathlib import Path
import json,re,shutil
B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale');A=Path('artifacts/correzioni-collana-2026-10-02');mp=B/'planning/10-manifest-nuclei-format-2.json';d=json.loads(mp.read_text(encoding='utf8'));matrix=B/'planning/02-matrice-copertura-didattica.md';m=matrix.read_text(encoding='utf8')
shutil.copy2(mp,A/'before-text/VOL-08'/mp.name)
q=json.loads((A/'VOL-08-quiz-review.json').read_text(encoding='utf8'))['rewritten']
for a in d['verificationAttestations']:
 n=a['nucleusId'];ch=int(n[7:9]);idx=int(n[-2:]);filename=next((B/'chapters').glob(f'{ch:02}-*.md')).name
 if ch==9 and idx in [2,3,4,6]:
  qi={2:1,3:3,4:4,6:6}[idx];a['target']=f'Quiz {qi}. '+q['9'][qi-1][0]
 if ch==10 and idx<=6:a['target']=f'Quiz {idx}. '+q['10'][idx-1][0]
 a.update(sourceLocation=f'planning/verifiche/{filename}#apparato-di-verifica-dei-nuclei',checkedAt='2026-10-03',reviewer='codex-audit-integrale-delta')
 # Counts must reflect real targets, not previous quiz wording.
 counts='Q:1 C:0 E:0' if re.search(r'\bquiz\b',a['target'],re.I) else 'Q:0 C:1 E:0' if re.search(r'\bcaso\b',a['target'],re.I) else 'Q:0 C:0 E:1'
 lines=[]
 for line in m.splitlines():
  if line.startswith(f'| `{n}` |') and len(line.strip('|').split('|'))==14:line=re.sub(r'Q:\d+ C:\d+ E:\d+',counts,line)
  lines.append(line)
 m='\n'.join(lines)+'\n'
# Preserve source-specific historical evidence where still exact. Replace only superseded quotes with reviewed new paragraphs.
starts={'N-TR01-03-06':'La **complessità temporale**','N-TR01-04-02':'Considera `Assegnazione','N-TR01-09-06':'Il d.lgs.','N-TR01-11-07':'Il regolamento (UE) 2024/1689','N-TR01-12-04':'Il **RUP**'}
for kind in ['attestations','didacticAttestations']:
 for a in d[kind]:
  p=B/a['sourceLocation'].split('#')[0];s=p.read_text(encoding='utf8');old=a['evidenceQuote']
  if old in s:continue
  nid=a['nucleusId'];start=s.index('## '+nid);end=s.find('\n## ',start+1);section=s[start:end if end>=0 else len(s)]
  prefix=starts[nid]
  if kind=='didacticAttestations' and nid=='N-TR01-09-06':prefix='**Caso svolto.**'
  if kind=='didacticAttestations' and nid=='N-TR01-11-07':prefix='**Caso.**' if a['dimension']=='application' else 'Per un sistema ad alto rischio'
  matches=[x.strip() for x in section.split('\n\n') if x.strip().startswith(prefix)]
  assert len(matches)==1,(nid,prefix)
  new=matches[0];m=m.replace(old,new);a.update(evidenceQuote=new,checkedAt='2026-10-03',reviewer='codex-audit-integrale-delta',dossier='wiki/reviews/pipeline/VOL-08/15-moduli-m-tr01-ict-trasformazione-digitale.md')
  if kind=='attestations':a.update(sourceRef='sources/ict-rettifiche-specialistiche-2026-10-03',cutoff='2026-10-03',sourceUrls=['https://www.acn.gov.it/portale/nis/la-normativa'] if nid.startswith('N-TR01-09') else ['https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32026R1744'] if nid.startswith('N-TR01-11') else ['https://opendatastructures.org/ods-python/1_3_Mathematical_Background.html'])
for chapter in d['chapters']:
 file=chapter['file'];out=B/'planning/verifiche'/file;out.parent.mkdir(exist_ok=True)
 rows=[a for a in d['verificationAttestations'] if a['sourceLocation'].split('#')[0]==f'planning/verifiche/{file}']
 text='---\ntype: editorial_evidence\nstatus: verified\nupdated_at: 2026-10-03\ncanonical: false\n---\n\n# Mappa staff delle verifiche — capitolo '+chapter['number']+'\n\n## Apparato di verifica dei nuclei\n\n| Nucleo ID | Apparato di verifica |\n| --- | --- |\n'
 text+=''.join(f"| `{a['nucleusId']}` | {a['target']} |\n" for a in rows)+'\n## Limite\n\nLa tabella è un mapping interno. I target devono esistere integralmente nel testo leggibile del capitolo; questa pagina non vale come domanda o soluzione del libro.\n'
 out.write_text(text,encoding='utf8')
mp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8');matrix.write_text(m,encoding='utf8')
print('82 mapping trasferiti in planning; attestazioni supersedute e conteggi riconciliati.')
