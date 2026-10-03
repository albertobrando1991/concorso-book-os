from pathlib import Path
import json,hashlib,re,sys,unicodedata,pymupdf
A=Path(__file__).parent;label=sys.argv[1];pdf=A/(label+'-proof.pdf');d=pymupdf.open(pdf);dom=json.loads((A/(label+'-proof-metrics.json')).read_text(encoding='utf8'))
def norm(s):return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',s)).lower()
index=[]
for i,p in enumerate(d):
 text=p.get_text()
 if 'Indice completo' not in text and 'INDICE COMPLETO' not in text:continue
 for m in re.finditer(r'Cap\.\s*(\d+)\s*\n(.*?)\n(\d+)\s*(?:\n|$)',text,re.S):
  num,title,printed=int(m[1]),' '.join(m[2].split()),int(m[3]);pages=[r for r in dom['pages'] if r.get('path') and '/chapters/' in r['path']];paths=[]
  for r in pages:
   if r['path'] not in paths:paths.append(r['path'])
  path=paths[num-1] if num<=len(paths) else None;actual=next((r['page'] for r in pages if r['path']==path),None)
  titleMatch=norm(title) in norm(d[printed-1].get_text()) if printed<=len(d) else False
  index.append({'number':num,'title':title,'indexPage':i+1,'printedPage':printed,'actualPage':actual,'titleOnTarget':titleMatch,'match':actual==printed and titleMatch,'path':path})
fonts=[]
for x in sorted({f[0] for p in d for f in p.get_fonts(full=True)}):
 name,ext,typ,program=d.extract_font(x);fonts.append({'name':name,'type':typ,'embedded':bool(program) or typ=='Type3' and '/CharProcs' in d.xref_object(x)})
text='\n'.join(p.get_text() for p in d)
out={'pdf':str(pdf),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(d),'domPages':dom['pageCount'],'pageCountMatch':len(d)==dom['pageCount'],'sizePt':[d[0].rect.width,d[0].rect.height],'indexEntries':index,'indexMismatches':[r for r in index if not r['match']],'fonts':fonts,'allFontsEmbedded':all(r['embedded'] for r in fonts),'overflowPages':[p['page'] for p in dom['pages'] if p['overflows']],'internalLeaks':re.findall(r'wiki/(?:sources|topics|books)|\[\[|source_refs|review_required|<br\s*/?>',text),'replacementGlyphs':text.count('\ufffd'),'missingImages':dom.get('missingImages'),'indexMinimumPt':dom.get('indexMinimumPt'),'limits':['Verifica tecnica locale; non equivale a revisione visiva o certificazione normativa.','Nessuna prova fisica o KDP Previewer eseguita.']}
(A/(label+'-verification.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in out.items() if k not in ['indexEntries','fonts','limits']},ensure_ascii=False))
