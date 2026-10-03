"""Restore the previously verified two-page ending when live pagination orphans its H2.
No chapter content is rewritten. Both pages must have exactly the same ordered words.
"""
from pathlib import Path
import hashlib,json,re,sys,shutil
import pymupdf as fitz
A=Path(__file__).parent
source=A/'vol-01-reader-final-20261003-proof.pdf'
target=Path(sys.argv[1]) if len(sys.argv)>1 else A/'vol-01-publication-refined-20261003-proof.pdf'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='0ad5da004f152d53d4eef5998b89b838a68fb276ade3ea9e9cc49517cfbc3670'
s=fitz.open(source);d=fitz.open(target);assert len(d)==len(s)==686
def words(doc):
 lines='\n'.join(doc[i].get_text() for i in [50,51]).splitlines()
 return re.sub(r'\s+',' ',' '.join(l for l in lines if l not in ['Il Metodo BANDO','3. IL METODO BANDO','CONTINUA','51','52'])).strip()
assert words(s)==words(d),'Refuse to replace pages with changed content'
before=hashlib.sha256(target.read_bytes()).hexdigest()
changed=d[50].get_text()!=s[50].get_text()
if changed:
 assert 'Da sapere in 5 righe' in d[50].get_text() and 'Da sapere in 5 righe' not in d[51].get_text()
 backup=A/'vol-01-publication-before-orphan-normalization.pdf'
 shutil.copy2(target,backup)
 for page in [51,50]:
  d.delete_page(page);d.insert_pdf(s,from_page=page,to_page=page,start_at=page)
 tmp=target.with_suffix('.normalized.pdf');d.save(tmp,garbage=4,deflate=True);d.close();tmp.replace(target)
else:d.close()
(A/'VOL-01-orphan-normalization.json').write_text(json.dumps(dict(source=str(source),sourceSha256=hashlib.sha256(source.read_bytes()).hexdigest(),target=str(target),before=before,after=hashlib.sha256(target.read_bytes()).hexdigest(),changed=changed,pages=[51,52],orderedContentPreserved=True,reason='Restore heading with its five-point body using the identical verified pages'),ensure_ascii=False,indent=2)+'\n','utf8')
print('Base: heading and body kept together; ordered content verified')
