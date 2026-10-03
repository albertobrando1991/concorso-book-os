import fs from 'node:fs/promises'
import path from 'node:path'
import { TEXT_VOLUME_CATALOG } from '../../src/catalog/text-volumes'
import { buildBookStudioData } from '../../src/server/book/book-preview'
import { FileWikiStore } from '../../src/server/wiki/file-store'
import { loadVolumeSpec } from '../../src/pipeline/spec/load-volume-spec'
import { parseFrontmatter } from '../../src/server/wiki/frontmatter'
import { runCommand } from '../../src/pipeline/cli/commands'
import { parseArgs } from '../../src/pipeline/cli/args'
const out='artifacts/review-collana-2026-10-02'
async function main(){
 const store=new FileWikiStore(path.join(process.cwd(),'wiki')), volumes:any[]=[]
 for(const volume of TEXT_VOLUME_CATALOG){
  const data=await buildBookStudioData(store,volume.code)
  const chapters=data.chapters.filter(c=>c.bookScope==='main'&&c.sectionType==='chapter')
  const textOf=(b:any):string=>[b.text,b.title,...(b.items||[]),...(b.headers||[]),...(b.rows||[]).flat()].filter(Boolean).join(' ')
  const texts=chapters.map(c=>({file:c.path,title:c.title,wordCount:c.wordCount,blocks:c.blocks.length,text:c.blocks.map(textOf).join('\n\n')}))
  await fs.writeFile(`${out}/${volume.code}-reader.json`,JSON.stringify(texts,null,2))
  const suspicious=texts.flatMap(c=>c.text.split('\n').map((t,i)=>({file:c.file,line:i+1,text:t})).filter(r=>/source note|fonti consolidate|audit specialistico|pipeline|text.freeze|da sviluppare|da verificare|capitolo in preparazione|\[\[(?:sources|topics|entities)\//i.test(r.text)))
  const spec=await loadVolumeSpec({wikiRoot:store.getRoot(),volumeCode:volume.code})
  const gates:any[]=[]
  for(const module of spec.spec.modules){const ch=module.chapters[0];if(!ch)continue;try{const result=await runCommand(parseArgs(['gate',volume.code,'--step','10','--module',module.code,'--chapter',ch.number,'--json']));gates.push({module:module.code,chapter:ch.number,payload:result.payload})}catch(e){gates.push({module:module.code,error:String(e)})}}
  const row={code:volume.code,summary:data.summary,printChapters:chapters.length,printWords:chapters.reduce((n,c)=>n+c.wordCount,0),suspicious,gates}
  volumes.push(row)
  console.log(JSON.stringify({code:row.code,printChapters:row.printChapters,printWords:row.printWords,suspicious:suspicious.length,gates:gates.map(g=>({module:g.module,passed:g.payload?.result?.passed,codes:g.payload?.result?.blockers?.map((b:any)=>b.code),error:g.error}))}))
 }
 await fs.writeFile(`${out}/reader-audit.json`,JSON.stringify({createdAt:new Date().toISOString(),note:'Text blocks from current Book Studio; no visual PDF inspection. One chapter coverage gate per module, read-only.',volumes},null,2))
}
main().catch(e=>{console.error(e);process.exitCode=1})
