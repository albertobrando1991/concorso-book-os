from pathlib import Path
import json,re,hashlib,shutil
from urllib.parse import urlparse
A=Path(__file__).parent;R=A/'vol05-proof';source=R/'source-payload.json'
if not source.exists():shutil.copy2(R/'payload.json',source)
payload=json.loads(source.read_text(encoding='utf8'));changes=[];moves=[]
for c in payload['chapters']:
 if c['sectionType']!='chapter':continue
 for b in c['blocks']:
  if b['type']!='paragraph':continue
  old=b['text']
  def link(m):
   label,url=m[1],m[2];printed=label+' ('+urlparse(url).netloc+')'
   changes.append({'path':c['path'],'label':label,'url':url,'printed':printed});return printed
  b['text']=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',link,old)
 if '/02-' in c['path']:
  idx=next(i for i,b in enumerate(c['blocks']) if b['type']=='heading' and b['text']=="Applicazione alla documentazione dell'ente")
  title=c['blocks'].pop(idx)['text'];assert c['blocks'][idx]['type']=='paragraph'
  c['blocks'][idx]['text']=title+'. '+c['blocks'][idx]['text']
  moves.append({'path':c['path'],'change':'Breve sottotitolo incorporato nel capoverso dopo il nucleo 2.4; tutte le parole preservate.','reason':'Due titoli consecutivi impedivano il recupero dello spazio a pagina 35.'})
 if '/14-' in c['path']:
  last=c['blocks'][-1];assert last['type']=='paragraph' and last['text'].startswith('Riferimenti normativi')
  c['blocks'].pop();idx=next(i for i,b in enumerate(c['blocks']) if b['type']=='heading' and b['text']=='Caso ragionato di chiusura')
  c['blocks'].insert(idx,last);moves.append({'path':c['path'],'change':'Bibliografia collocata prima del caso finale, nello stesso nucleo; nessun testo omesso.','reason':'La prova iniziale lasciava la sola bibliografia a pagina 220.'})
  idx=next(i for i,b in enumerate(c['blocks']) if b['type']=='heading' and b['text']=='Caso ragionato di chiusura')
  assert c['blocks'][idx+1]['type']==c['blocks'][idx+2]['type']=='paragraph'
  c['blocks'][idx+1]['text']+=' '+c['blocks'].pop(idx+2)['text']
  moves.append({'path':c['path'],'change':'Traccia e primo capoverso di soluzione riuniti nello stesso paragrafo; parole invariate.','reason':'Tenere titolo e porzione sostanziale del caso insieme, riequilibrando la chiusura.'})
hashes=[{'path':'wiki/'+c['path'],'sha256':hashlib.sha256(Path('wiki/'+c['path']).read_bytes()).hexdigest()} for c in payload['chapters'] if c['sectionType']=='chapter']
(R/'payload.json').write_text(json.dumps(payload,ensure_ascii=False),encoding='utf8')
(R/'projection-manifest.json').write_text(json.dumps({'sourceHashes':hashes,'externalLinkChanges':changes,'blockMoves':moves,'masterChanges':False,'allNormativeReferencesPreserved':True},ensure_ascii=False,indent=2),encoding='utf8')
script=(A/'export-proof.mjs').read_text(encoding='utf8')
script=script.replace("const bookId=process.argv[2]||'volumi/vol-12'","const bookId='volumi/vol-05'").replace("const label=process.argv[3]||bookId.split('/').at(-1)","const label='vol-05-candidate-20261003'")
script=script.replace('try {\n  await page.goto',"try {\n  const payload=JSON.parse(await fs.readFile('artifacts/correzioni-collana-2026-10-02/vol05-proof/payload.json','utf8'))\n  await page.route('**/api/book-studio?**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)}))\n  await page.goto")
(A/'export-vol05-proof.mjs').write_text(script,encoding='utf8')
print('Links:',len(changes),'moves:',len(moves))
