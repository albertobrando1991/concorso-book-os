from pathlib import Path
import json,re,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/correzioni-collana-2026-10-02');ROOT=Path.cwd()
cfg={'06':('vol-06-release-20261003',617,50,36,'IR'),'07':('vol-07-release-20261003',456,25,41,'SA'),'12':('vol-12-final-20261003',492,32,66,'SP')}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def copy(p,out):
 p=Path(p);dst=out/p;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
def normpath(s):return str(s).replace('\\','/')
def flatten(data):
 if isinstance(data,list):
  for x in data:yield from flatten(x)
 elif isinstance(data,dict):
  p=data.get('path',data.get('file'));h=data.get('sha256',data.get('after'))
  if p and isinstance(h,str):yield normpath(p),h
  for k,x in data.items():
   if isinstance(x,(dict,list)):yield from flatten(x)
for v,(label,pages,nchap,nfind,prefix) in cfg.items():
 freezes=[];chapters=[];effective={}
 for i in range(1,5):
  p=A/f'M-{prefix}{i:02}-freeze.json';d=json.loads(p.read_text(encoding='utf8'));freezes.append((p,d))
  for row in d['files']:chapters.append(Path(row.get('path',row.get('file'))))
  for path,h in flatten(d):effective[path]=h
 assert len(chapters)==nchap,(v,len(chapters))
 bad=[p for p,h in effective.items() if sha(p)!=h]
 assert not bad,(v,'freeze mismatch',bad)
 visual=json.loads((A/f'VOL-{v}-production-visual-checkpoint.json').read_text(encoding='utf8'))
 assert visual['sha256']==sha(A/(label+'-proof.pdf')) and visual['panoramaCoverageComplete']
 print(v,'frozen manuscripts verified',nchap)
 # Preserve initial evidence; add the effective post-print hashes explicitly.
 for p,d in freezes:
  d['productionReview']={'pdf':label+'-proof.pdf','sha256':visual['sha256'],'report':str(R/f'PDF-VOL-{v}.md'),'method':visual['method'],'effectiveFileHashes':{normpath(ch):sha(ch) for ch in chapters if ch.parent.parent.name.lower().startswith(d['module'].lower())},'frontMatterUnresolved':True}
  if 'controlledPrintCorrections' in d:d['controlledPrintCorrections']['verification']='Verificato nella prova di produzione e nel registro visivo del 3 ottobre 2026; nessuna attestazione normativa aggiuntiva.'
  save(p,d)
 changespath=A/f'VOL-{v}-changes.json';changes=json.loads(changespath.read_text(encoding='utf8'));assert len(changes['changes'])==nfind
 before=A/f'VOL-{v}-changes-before-production.json'
 if not before.exists():shutil.copy2(changespath,before)
 for ident,row in changes['changes'].items():
  row['previousEvidence']=row.get('previousEvidence',row['evidence'])
  evidence=row['previousEvidence']
  for phrase in ['Audit step15 e PDF ancora pendenti.','Nuovo PDF e controlli di volume ancora necessari.','Nuovo PDF da controllare.','Nuovo PDF ancora necessario.','PDF ancora necessario.','Controllo delle pagine PDF ancora necessario.','controllo specialistico e PDF successivi ancora necessari.','Grafico QC richiesto al coordinatore per V07-35; testo e dati pronti.','Resa del nuovo PDF pendente.']:
   evidence=evidence.replace(phrase,'')
  row['evidence']=' '.join(evidence.split())+f' Audit specialistici conclusi; prova di produzione {pages} pagine verificata nel perimetro dichiarato in PDF-VOL-{v}.md. Hash dei file riconciliati.'
  if ident in ['V07-35','V07-39']:row['evidence']+=' Figure controllate a piena risoluzione alle pagine 404 e 423–424.'
  row['status']='verificato';row['verificationScope']='Riesame testuale e specialistico dei delta; panoramica PDF completa e ingrandimenti mirati. Non certificazione normativa generale.'
  row['sha256']={f:sha(f) for f in row['files']}
 changes['productionReport']=str(R/f'PDF-VOL-{v}.md');changes['limitations']=['Promesse digitali e dati editoriali comuni non verificati; step 21 aperto.','Nessuna prova fisica, anteprima esterna o signoff 24.','Controlli normativi selettivi come documentati negli audit specialistici.'];save(changespath,changes)
 report=R/f'VOL-{v}.md';archive=A/f'VOL-{v}-register-before-production.md'
 if not archive.exists():shutil.copy2(report,archive)
 lines=[f'# VOL-{v} — Registro delle correzioni autorizzate','',f'{nfind}/{nfind} rilievi testuali applicati e riesaminati. Il termine verificato indica il perimetro delle evidenze dichiarate; non certifica ogni fonte normativa né la pubblicabilità complessiva. Gli audit storici restano immutati.','','| ID | Modifica | File | Evidenza | Stato |','| --- | --- | --- | --- | --- |']
 for ident,row in sorted(changes['changes'].items()):
  links=', '.join(f'[{Path(f).name}](../../../{normpath(f)})' for f in row['files'])
  lines.append('| '+' | '.join([ident,row['change'].replace('|','/'),links,row['evidence'].replace('|','/'),'verificato'])+' |')
 lines+=['','## Verifiche e limiti','',f'[Rapporto della prova di produzione](PDF-VOL-{v}.md): {pages} pagine. Tutti i capitoli congelati e le correzioni di stampa autorizzate sono riconciliati negli hash; il manifest registra il PDF preciso.','',f'Gli stati dei rilievi PDF sono distinti in `VOL-{v}-production-findings.json`. Restano aperte le promesse digitali e i dati editoriali comuni (FM{v}-01/02); non chiusi gli step 21–24. Copertina, preflight esterno e prova fisica appartengono alle fasi successive.','',f'Pacchetto preparatorio: `delivery/VOL-{v}/candidate-2026-10-03/`. Nessun caricamento o pubblicazione.']
 report.write_text('\n'.join(lines)+'\n',encoding='utf8')
 # Canonical final review uses the same ten sections and explicit current judgment.
 canonical=Path(f'wiki/reviews/pipeline/VOL-{v}/21-vol-{v}.md');archive=A/f'VOL-{v}-step21-before-production.md'
 if canonical.exists() and not archive.exists():shutil.copy2(canonical,archive)
 review=(R/f'PDF-VOL-{v}.md').read_text(encoding='utf8')
 titles={'2. Checklist dei 30 controlli':'2. Punti applicati della checklist','3. Registro dei rilievi e degli interventi':'3. Tabella errori','4. Osservazioni per capitolo e modulo':'4. Osservazioni per capitolo','5. Coerenza e verifiche tecniche':'5. Coerenza globale','6. Contenuti da verificare esternamente':'6. Contenuto da verificare','7. Miglioramenti facoltativi':'7. Suggerimenti facoltativi (non errori)','8. Priorità operative':'8. Priorità degli interventi','10. Copertura e limiti':'10. Limiti di questa revisione'}
 for x,y in titles.items():review=review.replace('## '+x,'## '+y)
 review=review.replace('Interno revisionabile e documentato, ma pubblicabilità complessiva non dichiarata:', '**Non pubblicabile allo stato attuale.** Interno revisionabile e documentato:')
 review=review.replace(f'(VOL-{v}.md)',f'(../../correzioni-collana-2026-10-02/VOL-{v}.md)')
 canonical.write_text(review,encoding='utf8')
 out=Path(f'delivery/VOL-{v}/candidate-2026-10-03');out.mkdir(parents=True,exist_ok=True)
 inputs=set(chapters)
 for ch in chapters:
  module=ch.parent.parent
  inputs.add(module/'index.md')
  inputs.update((module/'planning').glob('*matrice*.md'))
 for row in changes['changes'].values():inputs.update(Path(f) for f in row['files'])
 # Package every source/topic/entity note referenced directly by manuscript, matrix or changed note.
 todo=list(inputs);seen=set();missing=set()
 while todo:
  p=todo.pop()
  if p in seen or not p.exists():continue
  seen.add(p)
  if p.suffix.lower()!='.md':continue
  s=p.read_text(encoding='utf8')
  for ref in re.findall(r'(?:wiki/)?((?:sources|topics|entities)/[A-Za-z0-9_./-]+)',s):
   ref=ref.rstrip('.')
   if not ref.endswith('.md'):ref+='.md'
   target=Path('wiki')/ref
   if target.exists():inputs.add(target);todo.append(target)
   else:missing.add(ref)
 for p in inputs:
  if p.exists():copy(p,out)
 for p,d in freezes:copy(p,out)
 for p in [A/(label+'-proof.pdf'),A/(label+'-verification.json'),A/(label+'-proof-audit/metrics.json'),A/(label+'-render-comparison.json'),A/f'VOL-{v}-production-visual-checkpoint.json',A/f'VOL-{v}-page-audit.json',A/f'VOL-{v}-production-findings.json',changespath,report,R/f'PDF-VOL-{v}.md',canonical]:copy(p,out)
 sub=A/(label+'-index-subentries.json')
 if sub.exists():copy(sub,out)
 for p in A.glob(f'VOL-{v}-production-*-changes.json'):copy(p,out)
 copy(A/'VOL-06-07-12-production-reference-changes.json',out)
 for name in ['export-proof.mjs','inspect-current-pdf.py','production-pdf-verify.py','production-index-subentries.py']:
  p=A/name;copy(p,out)
 manifest={'volume':'VOL-'+v,'date':'2026-10-03','status':'reviewable-interior-pending-common-front-matter','pdf':str(A/(label+'-proof.pdf')),'pdfSha256':visual['sha256'],'pages':pages,'chapters':nchap,'textFindingsVerified':nfind,'pipelineSignoff24':False,'digitalServicesVerified':False,'coverage':str(A/f'VOL-{v}-production-visual-checkpoint.json'),'unresolvedReferencedNotes':sorted(missing),'files':[]}
 (out/'README.md').write_text(f'''# VOL-{v} — Pacchetto preparatorio dell’interno

PDF: `{A.as_posix()}/{label}-proof.pdf` ({pages} pagine). Hash e inventario in `manifest.json`. Per leggere gli esiti aprire `wiki/reviews/correzioni-collana-2026-10-02/PDF-VOL-{v}.md` e il registro delle correzioni accanto.

Stato: **interno revisionabile, front matter comune da completare**. Servizi digitali e dati editoriali non attestati; step 21 aperto, nessuna chiusura 22/23/24. Non è un pacchetto pronto da caricare su KDP: copertina finale, preflight esterno e prova fisica non inclusi.

Sono inclusi manoscritti, matrici pertinenti, source/topic/entity notes raggiungibili, asset modificati, freeze e controlli del PDF. Le raw immutabili restano nell’archivio del progetto; l’inclusione di una source note non significa che ogni sua affermazione sia stata ricertificata. Eventuali riferimenti bibliografici interni irrisolti sono elencati nel manifest.

Riproduzione: i quattro helper sotto `artifacts/correzioni-collana-2026-10-02` vanno eseguiti dalla radice della repo completa con ambiente già configurato; non sono un’applicazione autonoma. Conservare questa prova e usare un prefisso nuovo per un export successivo. Il manifest include gli hash, non promette identità binaria di PDF rigenerati.
''',encoding='utf8')
 for p in sorted(out.rglob('*')):
  if p.is_file() and p.name!='manifest.json':manifest['files'].append({'path':p.relative_to(out).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size})
 save(out/'manifest.json',manifest)
 assert all(sha(out/f['path'])==f['sha256'] for f in manifest['files'])
 print(v,'package',len(manifest['files']),'files; unresolved note links',len(missing))
