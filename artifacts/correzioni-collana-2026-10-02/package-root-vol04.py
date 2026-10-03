from pathlib import Path
import json,hashlib,shutil
A=Path(__file__).parent;R=A/'vol04-proof';W=Path('wiki/reviews/correzioni-collana-2026-10-02');D=Path('delivery/VOL-04/candidate-2026-10-03');label='vol-04-reader-final-20261003'
load=lambda p:json.loads(p.read_text('utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
v=load(A/(label+'-verification.json'));vis=load(R/'visual-review.json');f=load(A/'M-FC04-freeze.json')
assert vis['allContactSheetsViewed'] and vis['pdfSha256']==v['sha256'] and v['pages']==367
assert len(v['indexEntries'])==17 and not v['indexMismatches'] and not v['overflowPages'] and not v['internalLeaks'] and v['allFontsEmbedded']
assert all(sha(Path(r['path']))==r['sha256'] for r in f['files'])
D.mkdir(parents=True,exist_ok=True)
cp(A/(label+'-proof.pdf'),D/'vol-04-interior-kdp.pdf')
for src,dest in [(R/'payload-frontmatter.json','payload.json'),(R/'source-payload-frontmatter.json','source-payload.json'),(R/'frontmatter-projection-manifest.json','projection-manifest.json'),(R/'frontmatter-proof-verification.json','projection-verification.json'),(R/'visual-review.json','visual-review.json'),(A/(label+'-verification.json'),'verification.json'),(A/(label+'-proof-metrics.json'),'dom-metrics.json'),(A/(label+'-proof-audit/metrics.json'),'pdf-geometry.json')]:cp(src,D/dest)
paths={Path(r['path']) for r in f['files']}
paths.update(Path('wiki/books/vol-04-giustizia-upp/front-matter').glob('*.md'))
for p in sorted(paths):cp(p,D/'masters'/p.relative_to('wiki'))
for p in (A/(label+'-proof-audit')).glob('*.png'):cp(p,D/'visual'/p.name)
for p in R.rglob('*.png'):cp(p,D/'visual'/p.name)
for p in [W/'VOL-04.md',W/'PDF-VOL-04.md',*Path('wiki/reviews/pipeline/VOL-04').glob('1[3456]-*.md'),Path('wiki/reviews/pipeline/VOL-04/21-vol-04.md')]:cp(p,D/'reports'/p.name)
for n in ['VOL-04-ledger.json','M-FC04-freeze.json','VOL-04-text-verifica.json','VOL-04-layout-delta.json','VOL-04-bibliography-links.json','VOL-04-tail-polish.json','VOL-04-quiz-uniformazione.json','VOL-04-quiz78-uniformazione.json']:cp(A/n,D/'reports'/n)
src=(A/'export-vol04-frontmatter-proof.mjs').read_text('utf8').replace("from '../../scripts/","from '../../../../scripts/").replace("const out=path.resolve('artifacts/correzioni-collana-2026-10-02')","const out=path.resolve('delivery/VOL-04/candidate-2026-10-03/reproduced');await fs.mkdir(out,{recursive:true})").replace("fs.readFile('artifacts/correzioni-collana-2026-10-02/vol04-proof/payload-frontmatter.json','utf8')","fs.readFile(new URL('../payload.json',import.meta.url),'utf8')")
(D/'reproduction').mkdir(exist_ok=True);(D/'reproduction/export-vol04-frontmatter-proof.mjs').write_text(src,'utf8')
src=(A/'build-vol04-frontmatter-proof.ts').read_text('utf8').replace("from '../../src/","from '../../../../src/")
(D/'reproduction/build-vol04-frontmatter-proof.ts').write_text(src,'utf8')
renderers=[Path('src/book/pagination.ts'),Path('src/server/book/book-preview.ts'),Path('app/globals.css'),Path('app/components/book-studio-panel.tsx'),Path('scripts/book-studio-pdf-export-core.mjs'),Path('scripts/book-studio-layout-options.mjs')]
save(D/'renderer-source-hashes.json',[dict(path=p.as_posix(),sha256=sha(p)) for p in renderers])
(D/'README.md').write_text(f'''# VOL-04 — interno revisionato del 3 ottobre 2026

[PDF Giustizia e UPP](vol-04-interior-kdp.pdf): **367 pagine**, formato 6,69 × 9,61 pollici. SHA-256 `{v['sha256']}`.

17 capitoli e apparati, 84 quiz a quattro alternative e sei simulazioni svolte. Corretti 29 rilievi testuali e quattro di produzione. Indice 17/17 verificato; font incorporati; zero overflow, testo fuori pagina o immagini mancanti. Tutte le 23 tavole panoramiche finali e 17 dettagli sono stati esaminati; il rapporto distingue questa copertura dalla lettura del testo.

FM1 e FM3 derivano dai master corretti e non contengono la promessa commerciale standard dell'API. **Usare questa proiezione:** il normale export generico non è equivalente. Il payload e gli script sono inclusi, insieme a master, fonti, report e hash.

Riproduzione dal checkout con server, dipendenze, renderer e font dichiarati: `node delivery/VOL-04/candidate-2026-10-03/reproduction/export-vol04-frontmatter-proof.mjs`. Il comando usa il payload congelato; il builder separato ricostruisce invece la proiezione dai master correnti. Una nuova generazione va ricontrollata.

**Confezione finale ancora da completare:** preflight del canale, identificativi editoriali, copertina/dorso per 367 pagine e carta scelta, prova di stampa e conferma conclusiva. La vecchia copertina nella cartella candidate riguarda un altro numero di pagine e non fa parte di questo pacchetto. Nessun upload né signoff 24.
''','utf8')
save(D/'package-manifest.json',dict(volume='VOL-04',date='2026-10-03',pdfSha256=v['sha256'],files=[dict(path=p.relative_to(D).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-manifest.json']))
print(json.dumps(dict(package=D.as_posix(),pages=v['pages'],files=len(load(D/'package-manifest.json')['files'])),ensure_ascii=False))
