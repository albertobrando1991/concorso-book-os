import json, hashlib, pathlib, re
import pymupdf as fitz
from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / 'artifacts/review-integrale-2026-10-02/pdf'
OUT.mkdir(parents=True, exist_ok=True)
summaries = []
for file in sorted((ROOT/'delivery').glob('VOL-*/candidate/*interior*.pdf')):
    code = file.parents[1].name
    dest = OUT/code/file.stem
    dest.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(file)
    pages, texts = [], []
    thumbnails = []
    for index, page in enumerate(doc):
        data = page.get_text('dict')
        spans = [s for b in data['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
        text = page.get_text()
        texts.append({'page':index+1,'text':text})
        outside = [s for s in spans if s['bbox'][0]<-0.5 or s['bbox'][1]<-0.5 or s['bbox'][2]>page.rect.width+.5 or s['bbox'][3]>page.rect.height+.5]
        small = [s for s in spans if s['size'] < 7]
        replacement = text.count('\ufffd')
        row={'page':index+1,'width':page.rect.width,'height':page.rect.height,'chars':len(text),'spanCount':len(spans),'outside':[{'text':s['text'],'bbox':s['bbox']} for s in outside], 'under7pt':[{'text':s['text'],'size':s['size']} for s in small], 'replacementChars':replacement, 'images':len(page.get_images()),'fonts':sorted(set(s['font'] for s in spans))}
        pages.append(row)
        pix=page.get_pixmap(matrix=fitz.Matrix(0.44,0.44),alpha=False)
        image=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        thumbnails.append((index+1,image))
        if len(thumbnails)==24 or index==len(doc)-1:
            cellw,cellh=224,328
            canvas=Image.new('RGB',(cellw*6,cellh*4),'#cccccc')
            draw=ImageDraw.Draw(canvas)
            for j,(number,thumb) in enumerate(thumbnails):
                x,y=(j%6)*cellw,(j//6)*cellh
                canvas.paste(thumb,(x+4,y+19))
                draw.text((x+6,y+3),f'{code} / {number}',fill='black')
            canvas.save(dest/f'contact-{thumbnails[0][0]:04}-{thumbnails[-1][0]:04}.jpg',quality=86)
            thumbnails=[]
    summary={'volume':code,'file':str(file.relative_to(ROOT)).replace('\\','/'),'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'pages':len(doc),'outsidePages':[p['page'] for p in pages if p['outside']],'smallFontPages':[p['page'] for p in pages if p['under7pt']],'replacementPages':[p['page'] for p in pages if p['replacementChars']],'blankPages':[p['page'] for p in pages if p['chars']<30],'contactSheets':len(list(dest.glob('contact-*.jpg')))}
    (dest/'page-metrics.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf8')
    (dest/'page-text.json').write_text(json.dumps(texts,ensure_ascii=False,indent=2),encoding='utf8')
    summaries.append(summary)
    print(json.dumps(summary),flush=True)
    (OUT/'inventory.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2),encoding='utf8')
