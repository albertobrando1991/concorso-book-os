from pathlib import Path
import hashlib,json,shutil,re,pymupdf
ART=Path(__file__).parent
T=ART/'vol02-tomi'
OUT=Path('delivery/VOL-02/candidate-tomi-2026-10-03')
OUT.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
closeups={1:[141,181,257,292,297,324,325,327,329,330,332,592,610,611,612,615,617,619,659,696,697],2:[6,94,127,222,253,264,265,266]}
manifest={'volume':'VOL-02','date':'2026-10-03','status':'reviewable-interiors-pending-common-front-matter','pipelineSignoff24':False,'digitalServicesVerified':False,'tomes':[],'files':[]}
for i in [1,2]:
 ident=f'tomo-{i}';pdf=T/f'vol-02-{ident}-proof.pdf'
 v=json.loads((T/f'{ident}-verification.json').read_text(encoding='utf8'))
 assert v['pdfSha256']==sha(pdf) and not v['indexMismatches'] and not v['overflowPages'] and not v['internalLeaks']
 assert v['budgetAmountPreserved'] and v['newReferenceTablePresent']
 d=pymupdf.open(pdf);fonts=[]
 for x in sorted({f[0] for p in d for f in p.get_fonts(full=True)}):
  name,ext,typ,program=d.extract_font(x);obj=d.xref_object(x);glyphs=typ=='Type3' and '/CharProcs' in obj;fonts.append({'xref':x,'name':name,'extension':ext,'type':typ,'embeddedBytes':len(program),'embeddedType3CharProcs':glyphs})
 assert all(f['embeddedBytes']>0 or f['embeddedType3CharProcs'] for f in fonts)
 geo=json.loads((T/f'vol-02-{ident}-proof-audit/metrics.json').read_text(encoding='utf8'))
 assert not any(p['textOutsidePage'] or p['replacementGlyphs'] for p in geo['pagesData'])
 visual={'pdf':str(pdf),'pdfSha256':sha(pdf),'contactSheetsSeen':geo['contacts'],'pagesCovered':len(d),'method':'All contact sheets inspected; full-page closeups at selected critical pages. Not full-resolution proofreading of every page.','closeupsSeen':closeups[i],'allTenNativeSchemesSeen':i==1,'finalDeltas':{'292':'profile-reference cells checked enlarged','659':'reference dashes checked enlarged'} if i==1 else {},'limitations':['Common digital promise and publisher metadata unverified','No physical proof or KDP Previewer']}
 save(T/f'{ident}-visual-checkpoint.json',visual)
 tech={'pdfSha256':sha(pdf),'pages':len(d),'sizePt':[d[0].rect.width,d[0].rect.height],'fonts':fonts,'indexEntriesChecked':len(v['indexEntries']),'indexMismatches':0,'geometricOverflow':0,'bodyNominalPt':11,'indexMinimumPt':9.5,'croquisNominalPt':9.5 if i==2 else None,'kdpLimit':828,'kdpScope':'6.69x9.61in black ink white paper; local checks only'}
 save(T/f'{ident}-technical-manifest.json',tech)
 old=json.loads((T/f'{ident}-manifest.json').read_text(encoding='utf8'));old.update({'pagesPending':False,'pages':len(d),'pdfSha256':sha(pdf),'visualReview':f'{ident}-visual-checkpoint.json','technicalReview':f'{ident}-technical-manifest.json'});save(T/f'{ident}-manifest.json',old)
 dest=OUT/ident;dest.mkdir(exist_ok=True)
 for f in [pdf,T/f'{ident}-payload.json',T/f'{ident}-manifest.json',T/f'{ident}-verification.json',T/f'{ident}-technical-manifest.json',T/f'{ident}-visual-checkpoint.json',T/f'{ident}-orientamento.md',T/f'{ident}-simulazione.md',T/f'{ident}-conclusione.md']:
  shutil.copy2(f,dest/f.name)
 manifest['tomes'].append({'id':ident,'pdf':str((dest/pdf.name).relative_to(OUT)),'sha256':sha(pdf),'pages':len(d),'indexEntries':len(v['indexEntries'])})
for name in ['build-vol02-tomi.ts','export-vol02-tomo.mjs','verify-vol02-tomi.py','inspect-current-pdf.py']:
 dest=OUT/'reproduction';dest.mkdir(exist_ok=True);shutil.copy2(ART/name,dest/name)
for name in ['reference-alignment.json','tomo-1-profile-table-delta.json','tomo-1-dash-delta.json']:
 shutil.copy2(T/name,OUT/name)
# Reconcile existing records without rerunning the earlier mutating quiz script.
h=ART/'VOL-02-text-handoff.json';handoff=json.loads(h.read_text(encoding='utf8'))
for f in handoff['files']:f['sha256']=sha(f['path'])
handoff['limits']=['Local two-tome proofs reviewed; see PDF-VOL-02 report','Common front matter and external print approval unresolved'];handoff['proofs']=manifest['tomes'];save(h,handoff)
for code in ['M-FL01','M-FL02','M-FL03','M-FL04']:
 p=ART/f'{code}-freeze.json';d=json.loads(p.read_text(encoding='utf8'))
 for f in d['files']:
  path=f.get('file',f.get('path'));assert f['sha256']==sha(path),(code,path)
 d['pdfChecked']=True;d['pdfReviewMethod']='Whole-PDF contact sheets plus targeted closeups; see PDF-VOL-02.md, not all-page full-resolution reading';d['pdfProof']=manifest['tomes'][1 if code=='M-FL04' else 0];save(p,d)
ledger=ART/'VOL-02-changes.json';data=json.loads(ledger.read_text(encoding='utf8'))
for key,entry in data['changes'].items():
 entry['sha256']={f:sha(f) for f in entry['files']}
 if key in ['V02-01','V02-02','V02-52','V02-FM1','V02-FM2','V02-FM3','V02-FM4']:
  entry['status']='Applicato e riesaminato; apparati e prove dei due tomi verificati'
  entry['evidence']+=' Verifica finale nei due tomi: indice, selezione, rinvii e soluzioni; rapporto PDF-VOL-02.'
data['productionReport']='wiki/reviews/correzioni-collana-2026-10-02/PDF-VOL-02.md';data['proofs']=manifest['tomes'];data['openDependencies']=['Common digital services and editorial metadata','Formal gates21-23 after common dependency, signoff24','External print preview/covers'];save(ledger,data)
report=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-02.md');text=report.read_text(encoding='utf8')
text=text.replace('Applicato nel testo; riesame finale e PDF aperti','Applicato e riesaminato; apparati e prove dei due tomi verificati')
text=text.split('## Gate e limiti')[0]+'''## Gate e limiti

- 58/58 ID con intervento scritto e riesame documentato; apparati derivati e simulazioni dei due tomi verificati.
- Gate14/15 dei quattro moduli passati; freeze16 manuali dichiarati per gate non implementato. Hash riconciliati dopo gli schemi nativi e i delta tipografici.
- Prove: Tomo I700 pagine e Tomo II268, corpo11 pt; 272 voci di indice verificate e nessun overflow. [Rapporto PDF](PDF-VOL-02.md).
- Step21 resta aperto per condizioni digitali e dati editoriali comuni non verificati; step22/23 non dichiarati chiusi, nessun signoff24. Le prove locali sono evidenza preparatoria, non un salto dei gate.
- Pacchetto reviewabile: `delivery/VOL-02/candidate-tomi-2026-10-03/`. Nessun caricamento o pubblicazione.
'''
report.write_text(text,encoding='utf8')
canonical=Path('wiki/reviews/pipeline/VOL-02/21-vol-02.md');archive=ART/'VOL-02-step21-before-corrections.md'
if not archive.exists():shutil.copy2(canonical,archive)
shutil.copy2(ART/'VOL-02-step21-current.md',canonical)
for f in [report,Path('wiki/reviews/correzioni-collana-2026-10-02/PDF-VOL-02.md'),canonical]:shutil.copy2(f,OUT/f.name)
for p in OUT.rglob('*'):
 if p.is_file() and p.name!='manifest.json':manifest['files'].append({'path':str(p.relative_to(OUT)),'sha256':sha(p),'bytes':p.stat().st_size})
save(OUT/'manifest.json',manifest)
print(json.dumps({'package':str(OUT),'tomes':manifest['tomes'],'files':len(manifest['files'])},ensure_ascii=False))
