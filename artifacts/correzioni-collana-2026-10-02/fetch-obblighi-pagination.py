from pathlib import Path
import subprocess,re,json,hashlib,ast
base=Path('wiki/raw/correzioni-collana-2026-10-02')
art=Path(__file__).parent
# Reuse only the parser definition, without running another agent's downloader.
tree=ast.parse((art/'fetch-tuel.py').read_text(encoding='utf8'))
ns={};exec('from html.parser import HTMLParser\nimport re',ns)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.ClassDef)],type_ignores=[]),'parser','exec'),ns)
Extractor=ns['Extractor'];results=[]
for stem,urn,nums,progress in [('l296-obblighi','2006-12-27;296',[449,450],5),('l208-obblighi','2015-12-28;208',[510,512,516],6)]:
 initial=base/f'{stem}-session-20261003.html';block=base/f'{stem}-block-20261003.html';cookie=art/f'{stem}-cookie.txt'
 url=f'https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:{urn}~art1!vig=2026-10-03'
 if not initial.exists():subprocess.run(['curl.exe','-sS','-L','-c',str(cookie),'--max-time','45',url,'-o',str(initial)],check=True)
 links=re.findall(r"showArticle\('([^']+)'\)",initial.read_text(encoding='utf8'))
 assert links,stem
 target='https://www.normattiva.it'+re.sub(r'art.progressivo=\d+',f'art.progressivo={progress}',links[-1]).replace(' ','%20').replace('&amp;','&')
 if not block.exists():subprocess.run(['curl.exe','-sS','-L','-b',str(cookie),'--max-time','45',target,'-o',str(block)],check=True)
 parser=Extractor();parser.feed(block.read_text(encoding='utf8'))
 selected=[x for x in parser.parts if (m:=re.match(r'^(\d+)\.',x)) and int(m[1]) in nums]
 assert len(selected)==len(nums),(stem,len(selected),block.stat().st_size)
 print(stem+'\n'+'\n\n'.join(selected),flush=True)
 results.append({'file':block.as_posix(),'url':target,'commas':nums,'sha256':hashlib.sha256(block.read_bytes()).hexdigest()})
(art/'obblighi-commi-manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
