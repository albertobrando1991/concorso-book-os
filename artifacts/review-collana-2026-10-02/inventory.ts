import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { TEXT_VOLUME_CATALOG } from '../../src/catalog/text-volumes'
import { parseFrontmatter } from '../../src/server/wiki/frontmatter'
import { parseCoverageMatrix, auditCoverageRows } from '../../src/server/editorial/didactic-coverage'
import { loadVolumeSpec } from '../../src/pipeline/spec/load-volume-spec'
import { runCommand } from '../../src/pipeline/cli/commands'
import { parseArgs } from '../../src/pipeline/cli/args'
const root = process.cwd(), out = path.join(root,'artifacts/review-collana-2026-10-02')
async function exists(p:string) {try {await fs.access(p); return true} catch {return false}}
async function walk(p:string):Promise<string[]> {if(!await exists(p))return []; const entries=await fs.readdir(p,{withFileTypes:true}); return (await Promise.all(entries.map(e=>e.isDirectory()?walk(path.join(p,e.name)):Promise.resolve([path.join(p,e.name)])))).flat()}
async function main(){
 const volumes:any[]=[]
 for(const volume of TEXT_VOLUME_CATALOG){
  let status:any; try{status=(await runCommand(parseArgs(['status',volume.code,'--json']))).payload}catch(e){status={error:String(e)}}
  const loaded=await loadVolumeSpec({wikiRoot:path.join(root,'wiki'),volumeCode:volume.code})
  const bookIds=[...volume.bookIds,...(volume.orientationBookId?[volume.orientationBookId]:[])]
  const files=(await Promise.all(bookIds.map(id=>walk(path.join(root,'wiki/books',id,'chapters'))))).flat().filter(f=>f.endsWith('.md'))
  const chapters:any[]=[]
  for(const file of files){
   const content=await fs.readFile(file,'utf8'), {data,body}=parseFrontmatter(content)
   const references=Array.isArray(data.source_refs)?data.source_refs:[]
   const missingSources=[]
   for(const ref of references){const normalized=String(ref).replace(/^wiki\//,'').replace(/\.md$/,'');if(!await exists(path.join(root,'wiki',normalized+'.md')))missingSources.push(ref)}
   const brokenLinks:any[]=[], internalLinks:any[]=[]
   for(const match of body.matchAll(/\[\[([^\]|]+)(?:\|[^\]]*)?\]\]/g)){
    const [target,anchor]=match[1].split('#'); if(!/^(books|sources|topics|entities|reviews|raw)\//.test(target))continue
    const targetFile=path.join(root,'wiki',target.replace(/\.md$/,'')+'.md')
    const line=content.slice(0,content.indexOf(body)+match.index!).split('\n').length
    if(/^(sources|topics|entities|reviews|raw)\//.test(target)||target.includes('/planning/')) internalLinks.push({line,target:match[1]})
    if(!await exists(targetFile))brokenLinks.push({line,target:match[1],reason:'missing-file'})
    else if(anchor){const dest=await fs.readFile(targetFile,'utf8'); const headings=[...dest.matchAll(/^#{1,6}\s+(.+)$/gm)].map(m=>m[1].trim()); const norm=(v:string)=>v.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/[^\p{L}\p{N}]+/gu,'-').replace(/^-|-$/g,'');if(!headings.some(h=>h===anchor||norm(h)===norm(anchor)))brokenLinks.push({line,target:match[1],reason:'unmatched-heading-candidate'})}
   }
   chapters.push({file:path.relative(root,file).replaceAll('\\','/'),sha256:createHash('sha256').update(content).digest('hex'),title:data.title,outline:data.outline_section,stage:data.draft_stage,format:data.format_version,words:body.split(/\s+/).filter(Boolean).length,sourceCount:references.length,missingSources,brokenLinks,internalLinks})
  }
  const matrices:any[]=[]
  const allFiles=(await Promise.all(bookIds.map(id=>walk(path.join(root,'wiki/books',id))))).flat()
  for(const file of allFiles.filter(f=>f.endsWith('-matrice-copertura-didattica.md'))){const content=await fs.readFile(file,'utf8'),rows=parseCoverageMatrix(content),result=auditCoverageRows(rows);matrices.push({file:path.relative(root,file).replaceAll('\\','/'),rows:rows.length,complete:result.complete,blockers:result.blockers,warnings:result.warnings,statuses:rows.reduce((a:any,r)=>{a[r.status]=(a[r.status]||0)+1;return a},{})})}
  const entry={code:volume.code,title:volume.title,promise:volume.promise,status,cutOff:loaded.spec.cutOffDate,specPath:loaded.spec.specPath,specIssues:loaded.issues,declaredChapters:loaded.spec.modules.reduce((n,m)=>n+m.chapters.length,0),chapters,matrices}
  volumes.push(entry)
  console.log(JSON.stringify({code:entry.code,files:chapters.length,declared:entry.declaredChapters,words:chapters.reduce((n,c)=>n+c.words,0),cutOff:entry.cutOff,status:status.counts||status.error,next:status.next?.id,matrices:matrices.length,matrixBlockers:matrices.reduce((n,m)=>n+m.blockers.length,0),missingSources:chapters.reduce((n,c)=>n+c.missingSources.length,0),brokenLinks:chapters.reduce((n,c)=>n+c.brokenLinks.length,0),internalLinks:chapters.reduce((n,c)=>n+c.internalLinks.length,0)}))
 }
 await fs.writeFile(path.join(out,'inventory.json'),JSON.stringify({createdAt:new Date().toISOString(),scope:'All chapter-directory Markdown files in catalog bookIds, including digital/legacy files; not equivalent to print scope.',volumes},null,2))
}
main().catch(e=>{console.error(e);process.exitCode=1})
