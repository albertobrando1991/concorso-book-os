from pathlib import Path
import json,hashlib,shutil,re
A=Path(__file__).parent;W=Path('wiki/reviews/correzioni-collana-2026-10-02');D=Path('delivery/VOL-01/candidate-2026-10-03');label='vol-01-reader-final-20261003'
load=lambda p:json.loads(p.read_text('utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
v=load(A/(label+'-verification.json')); vis=load(A/'VOL-01-reader-final-visual-review.json');ix=load(A/'VOL-01-index-verification.json');freeze=load(A/'M-PA01-freeze.json');payload=load(A/'vol01-final-payload.json')
assert v['sha256']==vis['pdfSha256'] and vis['allContactSheetsViewed']
assert v['pages']==686 and v['pageCountMatch'] and v['allFontsEmbedded'] and not v['overflowPages'] and not v['internalLeaks']
assert len(ix['entries'])==437 and not ix['mismatches']
assert all(sha(Path(r['path']))==r['sha256'] for r in freeze['files'])
D.mkdir(parents=True,exist_ok=True)
cp(A/(label+'-proof.pdf'),D/'vol-01-interior-kdp.pdf')
cp(A/'vol01-final-payload.json',D/'payload.json')
for src,dest in [(A/(label+'-verification.json'),'verification.json'),(A/(label+'-proof-metrics.json'),'dom-metrics.json'),(A/(label+'-proof-audit/metrics.json'),'pdf-geometry.json'),(A/'VOL-01-reader-final-visual-review.json','visual-review.json'),(A/'VOL-01-index-verification.json','index-verification.json')]:cp(src,D/dest)
printed={r['path'] for r in load(A/(label+'-proof-metrics.json'))['pages']}
print_chapters=[c for c in payload['chapters'] if c['path'] in printed]
assert len(print_chapters)==38
paths={Path('wiki')/c['path'] for c in print_chapters if (Path('wiki')/c['path']).exists()}
for p in sorted(paths):cp(p,D/'masters'/p.relative_to('wiki'))
images={Path('wiki')/b['path'] for c in print_chapters for b in c['blocks'] if b['type']=='image'}
assert len(images)==20
for old in (D/'masters/books/il-metodo-bando/chapters').glob('*.md'):
 if not any(old.name==p.name for p in paths):
  assert old.resolve().is_relative_to(D.resolve());old.unlink()
for p in images:cp(p,D/'masters'/p.relative_to('wiki'))
for p in sorted(Path('wiki/sources').glob('vol-01-*correzioni-2026-10-*.md')):cp(p,D/'sources'/p.name)
for p in sorted((A/(label+'-proof-audit')).glob('contact-*.png')):cp(p,D/'visual'/p.name)
for p in sorted((A/'vol01-final-details').glob('page-*.png')):cp(p,D/'visual'/p.name)
report=W/'PDF-VOL-01.md';cp(report,D/'reports'/report.name)
cp(W/'VOL-01.md',D/'reports/VOL-01.md');cp(W/'VOL-01-schemi-nativi.md',D/'reports/VOL-01-schemi-nativi.md')
names=['M-PA01-freeze.json','VOL-01-final-labels.json','VOL-01-index-labels.json','VOL-01-native-inventory.json','VOL-01-native-ledger.json','VOL-01-native-verifica.json','VOL-01-native-release-visual-ledger.json','VOL-01-native-release-chain-audit.json','figure-vol01-corrette-manifest.json','vol01-esempi-verificati.json']
for n in names:cp(A/n,D/'reports'/n)
src=(A/'export-vol01-final.mjs').read_text('utf8').replace("from '../../scripts/","from '../../../../scripts/")
src=src.replace("const out=path.resolve('artifacts/correzioni-collana-2026-10-02')","const out=path.resolve('delivery/VOL-01/candidate-2026-10-03/reproduced');await fs.mkdir(out,{recursive:true})")
src=re.sub(r"  const response=await fetch\(.*?await fs.writeFile\(path.join\(out,'vol01-final-payload.json'\),JSON.stringify\(payload\)\);", "  const payload=JSON.parse(await fs.readFile(new URL('../payload.json',import.meta.url),'utf8'));",src)
assert 'const response=await fetch' not in src
(D/'reproduction').mkdir(exist_ok=True);(D/'reproduction/export-vol01-final.mjs').write_text(src,'utf8')
renderers=[Path('src/book/pagination.ts'),Path('src/server/book/book-preview.ts'),Path('app/globals.css'),Path('app/components/book-studio-panel.tsx'),Path('scripts/book-studio-pdf-export-core.mjs'),Path('scripts/book-studio-layout-options.mjs')]
save(D/'renderer-source-hashes.json',[dict(path=p.as_posix(),sha256=sha(p)) for p in renderers])
(D/'README.md').write_text(f'''# VOL-01 — candidato revisionato del 3 ottobre 2026

[Interno PDF](vol-01-interior-kdp.pdf): **686 pagine**, formato 6,69 × 9,61 pollici. SHA-256 `{v['sha256']}`.

32 unità autoriali, 133 schemi nativi, 19 figure didattiche e QR. Indice: 437/437 destinazioni corrette; font incorporati; zero overflow e testo fuori pagina. Tutte le 43 tavole sono esaminate, con 14 dettagli finali del coordinatore e ulteriori riscontri degli apparati registrati nei report. Non è una nuova rilettura parola per parola dell'intero PDF.

**Restano aperti V01-50 e V01-51:** attivazione e condizioni del mese digitale promesso, canale effettivo di assistenza/errata e dati editoriali da confermare. Nessuna autorizzazione alla pubblicazione, prova fisica o accettazione KDP. Copertina e confezione finale sono passaggi distinti.

I master e gli asset usati, il payload, i registri di verifica e gli hash sono inclusi. La proiezione abbrevia le etichette dell'indice per impedirne la sovrapposizione; i titoli e le destinazioni sono preservati. Riproduzione dal checkout con server e dipendenze già presenti: `node delivery/VOL-01/candidate-2026-10-03/reproduction/export-vol01-final.mjs`. Usa il payload incluso, il renderer e i font registrati e gli asset del repository; ogni nuova generazione richiede verifica.

Le altre prove VOL-01 in delivery e artifacts sono storiche e non sostituiscono questo candidato.
''','utf8')
save(D/'package-manifest.json',dict(volume='VOL-01',date='2026-10-03',pdfSha256=v['sha256'],files=[dict(path=p.relative_to(D).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-manifest.json']))
canonical=Path('wiki/reviews/pipeline/VOL-01/21-vol-01.md')
if canonical.exists():cp(canonical,A/'VOL-01-step21-before-production.md')
canonical.write_text('---\nstatus: review\nreview_required: true\nupdated: 2026-10-03\n---\n\n'+report.read_text('utf8'),'utf8')
freeze['pdfChecked']=dict(path=(D/'vol-01-interior-kdp.pdf').as_posix(),sha256=v['sha256'],pages=686,indexEntries=437,visualLedger=(A/'VOL-01-reader-final-visual-review.json').as_posix(),finalSignoff=False)
save(A/'M-PA01-freeze.json',freeze)
cp(A/'M-PA01-freeze.json',D/'reports/M-PA01-freeze.json')
save(D/'package-manifest.json',dict(volume='VOL-01',date='2026-10-03',pdfSha256=v['sha256'],files=[dict(path=p.relative_to(D).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-manifest.json']))
print(json.dumps(dict(package=D.as_posix(),pages=v['pages'],files=len(load(D/'package-manifest.json')['files'])),ensure_ascii=False))
