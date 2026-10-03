from pathlib import Path
import json,hashlib,shutil,re
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');D=A/'before-text/VOL-05';D.mkdir(parents=True,exist_ok=True)
old=json.loads(Path('artifacts/review-integrale-2026-10-02/VOL-05-ledger.json').read_text(encoding='utf8'));oldhash={r['path']:r['sha256'] for r in old['files']}
paths=sorted((B/'chapters').glob('*.md'))+[B/'index.md']+sorted((B/'planning').glob('*.md'));rows=[]
for p in paths:
 h=hashlib.sha256(p.read_bytes()).hexdigest();rows.append({'path':p.as_posix(),'sha256':h,'auditReadComplete':p.as_posix() in oldhash,'unchangedSinceIntegralAudit':oldhash.get(p.as_posix())==h});target=D/p.name
 if not target.exists():shutil.copy2(p,target)
(A/'VOL-05-baseline.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
(A/'VOL-05-plan.md').write_text('''# VOL-05 — Piano delle correzioni autorizzate

1. Baseline, lettura dei 15 capitoli e fonti pertinenti; confronto con audit.
2. Fonti primarie: governance di otto enti, procedimento e rimedi, settori e soglie aggiornate.
3. Consolidamento source notes e topic prima delle integrazioni; ambiti di lettura espliciti.
4. Integrazioni per 33 rilievi; 90 quesiti aperti specifici, 15 casi di chiusura, 10 simulazioni svolte.
5. Matrice veritiera (75 nuclei e 90 quesiti complessivi), indici, rinvii e repertori leggibili.
6. Gate di capitolo, Humanizer, audit CLI 14/15, freeze 16 con hash. PDF e figure separati, coordinatore responsabile produzione.

Nessuna riduzione della promessa editoriale. Nessun commit o pubblicazione. Rilievi grafici P05-20/21 coordinati con root; le figure ripetitive non sostituiscono spiegazioni, calcoli o prove.
''',encoding='utf8')
s=(A/'fetch-vol11.py').read_text(encoding='utf8');start=s.index('groups=');end=s.index('jobs=',start)
groups=[('agcm','legge:1990-10-10;287',[10,11,14,'14bis','14ter','14quater',15,16]),('arera','legge:1995-11-14;481',[2]),('agcom','legge:1997-07-31;249',[1]),('collegi','decreto.legge:2011-12-06;201',[23]),('consob','decreto.legge:1974-04-08;95',[1]),('risparmio','legge:2005-12-28;262',[19]),('ivass','decreto.legge:2012-07-06;95',[13]),('privacy','decreto.legislativo:2003-06-30;196',[153,155,156,157,158,166]),('anac','decreto.legge:2014-06-24;90',[19]),('civit','decreto.legislativo:2009-10-27;150',[13]),('tuf','decreto.legislativo:1998-02-24;58',[5,21,94,106,'187septies',195]),('tub','decreto.legislativo:1993-09-01;385',[5,53,67,80,145]),('processo','decreto.legislativo:2011-09-01;150',[10]),('consumo','decreto.legislativo:2005-09-06;206',[20,21,22,23,24,25,26,27,'37bis']),('whistle','decreto.legislativo:2023-03-10;24',[1,2,3,4,5,6,8,12,16,17,19]),('contratti','decreto.legislativo:2023-03-31;36',[220,222])]
s=s[:start]+'groups='+repr(groups)+'\n'+s[end:];s=s.replace('correzioni-vol11','correzioni-vol05').replace('norme-vol11','norme-vol05');(A/'fetch-vol05.py').write_text(s,encoding='utf8')
print('Baseline',len(rows),'files; unchanged chapters',sum(r['unchangedSinceIntegralAudit'] for r in rows if '/chapters/' in r['path']))
