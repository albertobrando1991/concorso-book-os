from pathlib import Path
import json, hashlib, collections, difflib, re
import fitz
from PIL import Image,ImageDraw
A=Path('artifacts/correzioni-collana-2026-10-02'); R=A/'vol04-proof'; D=R/'details';D.mkdir(exist_ok=True)
old=A/'vol-04-final-20261003-proof.pdf';new=A/'vol-04-reader-final-20261003-proof.pdf'
before=json.loads((A/'vol-04-final-20261003-proof-metrics.json').read_text(encoding='utf8'))
after=json.loads((A/'vol-04-reader-final-20261003-proof-metrics.json').read_text(encoding='utf8'))
a=fitz.open(old);b=fitz.open(new)
def group(metrics):
    result=collections.defaultdict(list)
    for p in metrics['pages']:result[p['path']].append(p)
    return result
ga=group(before);gb=group(after)
def text(rows):
    return ' '.join(' '.join(re.sub(r'\n\d+\s*$','',r['text']).split()) for r in rows)
comparisons=[]; changed=[]; same=[]
for path,rows in gb.items():
    prev=ga.get(path,[])
    # FM1/FM3 paths intentionally change; keep explicit pairing.
    if not prev and '/front-matter/' in path:
        oldpath=next((p for p in ga if ('fm1-' if '01-servizi' in path else 'fm3-') in p),None)
        prev=ga.get(oldpath,[])
    aa=text(prev);bb=text(rows)
    delta=[{'operation':tag,'before':' '.join(aa.split()[i:j]),'after':' '.join(bb.split()[k:l])} for tag,i,j,k,l in difflib.SequenceMatcher(None,aa.split(),bb.split(),autojunk=False).get_opcodes() if tag!='equal']
    comparisons.append({'path':path,'oldPages':[p['page'] for p in prev],'newPages':[p['page'] for p in rows],'textEqual':aa==bb,'wordDeltas':delta})
    for i,row in enumerate(rows):
        n=row['page'];oldn=prev[i]['page'] if i<len(prev) else None
        equal=False
        if oldn:
            pa=a[oldn-1];pb=b[n-1]
            # Ignore running footer number after the two deleted tail pages.
            crop=fitz.Rect(0,0,min(pa.rect.width,pb.rect.width),pa.rect.height-38)
            equal=pa.get_pixmap(clip=crop).samples==pb.get_pixmap(clip=crop).samples
        (same if equal else changed).append({'page':n,'oldPage':oldn,'path':path})
for row in changed:
    n=row['page'];b[n-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(D/f'page-{n:03}.png')
manifest=json.loads((R/'frontmatter-projection-manifest.json').read_text(encoding='utf8'))
hash_check=[r['path'] for r in manifest['sourceHashes'] if hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()!=r['sha256']]
result={'baselinePages':len(a),'currentPages':len(b),'pdfSha256':hashlib.sha256(new.read_bytes()).hexdigest(),'baselinePdfSha256':hashlib.sha256(old.read_bytes()).hexdigest(),'indexMinimumPt':after['indexMinimumPt'],'overflowPages':[p['page'] for p in after['pages'] if p['overflows']],'missingImages':after['missingImages'],'literalBr':after['literalBr'],'sourceHashMismatches':hash_check,'fmPages':{k:[p['page'] for p in v] for k,v in gb.items() if '/front-matter/01-' in k or '/front-matter/03-' in k},'chapterComparison':comparisons,'pixelComparisonScope':'72 dpi, matching chapter pages, crop excludes bottom 38 pt running footer','unchangedContentPages':same,'changedContentPages':changed,'visualReviewPending':[r['page'] for r in changed]}
(R/'frontmatter-proof-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['chapterComparison','unchangedContentPages','changedContentPages']},ensure_ascii=False))
print('Text-delta chapters:',[(r['path'],r['wordDeltas']) for r in comparisons if not r['textEqual']])
assert len(b)==after['pageCount']
assert not hash_check
assert all(len(v)==1 for v in result['fmPages'].values())
out=R/'contacts';out.mkdir(exist_ok=True);sheets=[]
for start in range(0,len(b),16):
    sheet=Image.new('RGB',(1280,1904),'#cccccc');draw=ImageDraw.Draw(sheet)
    for j in range(min(16,len(b)-start)):
        page=b[start+j];pix=page.get_pixmap(matrix=fitz.Matrix(0.6,0.6));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((310,447));x=(j%4)*320;y=(j//4)*476;sheet.paste(im,(x+5,y+24));draw.text((x+8,y+6),f'PDF p. {start+j+1}',fill='black')
    name=f'contact-{start//16+1:02}.jpg';sheet.save(out/name,quality=90);sheets.append({'file':name,'pages':list(range(start+1,min(start+16,len(b))+1)),'viewed':False})
(R/'contact-ledger.json').write_text(json.dumps(sheets,indent=2),encoding='utf8')
