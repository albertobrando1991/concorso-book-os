import fs from 'node:fs/promises'
import path from 'node:path'
import { TEXT_VOLUME_CATALOG } from '../../src/catalog/text-volumes'
import { buildBookStudioData } from '../../src/server/book/book-preview'
import { FileWikiStore } from '../../src/server/wiki/file-store'
const out='artifacts/review-integrale-2026-10-02'
const clean=(s:string)=>s.replace(/\[([^\]]+)\]\([^)]*\)/g,'$1').replace(/^[>\s]*(?:\d+\.|-)\s+/,'').replace(/[*_`\[\]#|>]/g,'').replace(/\s+/g,' ').trim().toLowerCase()
async function main(){
 const store=new FileWikiStore(path.join(process.cwd(),'wiki')); const rows:any[]=[]
 for(const v of TEXT_VOLUME_CATALOG){
  const data=await buildBookStudioData(store,v.code)
  const reader=data.chapters.filter(c=>c.bookScope==='main')
  await fs.writeFile(`${out}/${v.code}-current-export.json`,JSON.stringify(reader,null,2))
  for(const c of reader){
   if(c.sectionType!=='chapter')continue
   const raw=await fs.readFile(path.join('wiki',c.path),'utf8')
   const txt=c.blocks.map((b:any)=>[b.text,b.title,...(b.items||[]),...(b.headers||[]),...(b.rows||[]).flat()].filter(Boolean).join(' ')).join('\n')
   const n=clean(txt)
   const nuclei=[...raw.matchAll(/^#{2,4}\s+(N-[A-Z0-9-]+)[^\n]*\n+([^#\n][^\n]*)/gm)].filter(m=>!m[2].startsWith('![')).map(m=>({id:m[1],sample:m[2].slice(0,160),present:n.includes(clean(m[2].slice(0,160)))}))
   rows.push({volume:v.code,file:'wiki/'+c.path,words:c.wordCount,sectionType:c.sectionType,nuclei,missing:nuclei.filter(x=>!x.present).length})
  }
  console.log(v.code,reader.length,'reader units')
 }
 await fs.writeFile(`${out}/export-audit.json`,JSON.stringify(rows,null,2))
 console.log(JSON.stringify(rows.filter(r=>r.missing).map(r=>({volume:r.volume,file:r.file,nuclei:r.nuclei.length,missing:r.missing}))))
}
main().catch(e=>{console.error(e);process.exitCode=1})
