import fs from 'node:fs/promises'
import path from 'node:path'
import crypto from 'node:crypto'
import {parseStudentChapterForExport, type BookStudioData} from '../../../../src/server/book/book-preview'
async function main(){
const out='artifacts/correzioni-collana-2026-10-02/vol03-proof';await fs.mkdir(out,{recursive:true})
const response=await fetch('http://127.0.0.1:3020/api/book-studio?bookId=volumi%2Fvol-03');if(!response.ok)throw Error('API '+response.status)
const payload:BookStudioData=await response.json();await fs.writeFile(path.join(out,'source-payload.json'),JSON.stringify(payload))
const main=payload.chapters.filter(c=>c.sectionType==='chapter')
for(const c of main){
 const raw=await fs.readFile('wiki/'+c.path,'utf8')
 for(const m of raw.matchAll(/\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]/g)){
  const ref=m[1].replace(/\.md$/,'');if(awaitReadCache.has(ref))continue
  try{const target=await fs.readFile('wiki/'+ref+'.md','utf8');const title=/^title:\s*["']?(.+?)["']?\s*$/m.exec(target)?.[1];if(title)awaitReadCache.set(ref,title)}catch{}
 }
}
const maps:Record<string,Record<string,string>>={};const bypath=new Map(main.map(c=>[c.path.replace(/\.md$/,''),c]))
for(const c of main){const key=/^(\d+[ab]?)-/i.exec(path.basename(c.path))?.[1].replace(/^0/,'').toUpperCase();if(key)(maps[c.volumeModuleCode!]??={})[key]=c.outlineSection}
const changes:any[]=[],hashes:any[]=[],linkChanges:any[]=[]
const workbookChanges:any[]=[]
function align(text:string,mod:string,p:string):string{
 const map=maps[mod]||{};let result=text
 // These two explicit references target the fiscal module from EPNE.
 if(mod==='M-FC03') result=result.replace(/capitolo 12 (?=(?:del modulo Agenzie fiscali|«Civile e commerciale))/gi,'capitolo @FISCAL12@ ')
 result=result.replace(/((?:capitol[oi]|cap\.)\s+)(\d+[ab]?(?:(?:\s*,\s*|\s+e\s+|[–-])\d+[ab]?)*)(?![\d.,/]\d)/gi,(match,prefix,list,offset)=>{
  const previous=result.slice(Math.max(0,offset-20),offset)
  if(/VOL-\d\d,?\s*$/i.test(previous))return match
  // All numbered references were reviewed in VOL-03-numbered-refs.json.
  return prefix+list.replace(/\d+[ab]?/gi,(n:string)=>map[n.replace(/^0/,'').toUpperCase()]||n)
 })
 result=result.replaceAll('@FISCAL12@',maps['M-FC02']['12'])
 if(mod==='M-FC03'){
  result=result.replace('33–40 per le materie; 11–12 per casi e situazionali.','33–40 per le materie; 42–43 per casi e situazionali.')
  result=result.replace(/Appendice A(?:-F|, B, C, D, E o F)/g,'appendici A–F (capitoli 45–50)')
  result=result.replace(/\b(Appendice [A-F])\b/gi,(m:string)=>`${m} (capitolo ${45+m.slice(-1).toUpperCase().charCodeAt(0)-65})`)
 }
 if(result!==text)changes.push({path:p,before:text,after:result})
 return result
}
for(const c of main){
 const file='wiki/'+c.path;const raw=await fs.readFile(file,'utf8');hashes.push({path:file,sha256:crypto.createHash('sha256').update(raw).digest('hex')})
 const parts=raw.split('---');const fm=parts.slice(0,2).join('---')+'---';let body=parts.slice(2).join('---')
 const links:string[]=[]
 body=body.replace(/\[\[([^\]]+)\]\]/g,(full,inner:string)=>{
  const [target,...aliasParts]=inner.split('|');const [ref,anchor]=target.split('#');const dest=bypath.get(ref.replace(/\.md$/,''))
  let label=aliasParts.join('|')
  if(!label){
   let title=dest?.title
   if(!title)title=awaitReadCache.get(ref.replace(/\.md$/,''))
   if(!title)title=ref.split('/').at(-1)!.replace(/^\d+[ab]?-/,'').replace(/-/g,' ')
   let section=anchor?.replace(/^N-[A-Z0-9-]+\s*[·—-]\s*/,'').replace(/^\d+\.\s*/,'')
   label=(dest?`capitolo ${dest.outlineSection}, `:'')+title+(section?` — «${section}»`:'')
   linkChanges.push({path:c.path,target,label})
  }else if(dest){
   label=label.replace(/capitolo\s+\d+[ab]?/gi,`capitolo ${dest.outlineSection}`)
  }
  links.push(label);return `@@LINK${links.length-1}@@`
 })
 body=body.split('\n').map(line=>line.startsWith('#')?line:align(line,c.volumeModuleCode!,c.path)).join('\n')
 body=body.replace(/@@LINK(\d+)@@/g,(_,n)=>links[Number(n)])
 // Native scheme numbers refer to the visible volume chapter, not the module-local one.
 body=body.replace(/Schema \d+\.(\d+) —/g,`Schema ${c.outlineSection}.$1 —`)
 // A heading keeps each scheme title with its first content block in pagination.
 body=body.replace(/^\*\*(Schema .+)\*\*\s*$/gm,'#### $1')
 if(c.outlineSection==='30'){
  let mapChanged=false
  body=body.replace(/\| Passaggio \| Domanda guida \| Applicazione al capitolo \|\r?\n(?:\|[^\n]*\n?)+/,(table:string)=>{
   const rows=table.trim().split('\n').slice(2).map(line=>line.trim().slice(1,-1).split('|').map(s=>s.trim()))
   if(rows.length!==5)throw Error('Unexpected BANDO map rows')
   const result='| Passaggio e domanda | Applicazione al capitolo |\n|---|---|\n'+rows.map(r=>`| **${r[0]}** — ${r[1]} | ${r[2]} |`).join('\n')+'\n'
   mapChanged=true;workbookChanges.push({path:c.path,kind:'BANDO map two-column projection',original:table,vertical:result});return result
  })
  if(!mapChanged)throw Error('Missing map projection')
 }
 if(['13','14','31'].includes(c.outlineSection)){
  body=body.replace(/^\|[^\n]*(?:\n\|[^\n]*)+/gm,(table:string)=>{
   const lines=table.trim().split('\n');const cells=(s:string)=>s.trim().slice(1,-1).split('|').map(v=>v.trim());const headers=cells(lines[0])
   if(headers.length<8)return table
   const rows=lines.slice(2).map(cells);if(rows.length!==1)throw Error('Unexpected workbook rows')
   const blank='________________________<br>________________________'
   const result='| Campo | Compilazione |\n|---|---|\n'+headers.map((h,i)=>`| ${h} | ${rows[0][i]||blank} |`).join('\n')
   workbookChanges.push({path:c.path,headers,original:table,vertical:result});return result
  })
 }
 const parsed=parseStudentChapterForExport(fm+body,c.path).blocks
 const oldNumbers=new Map(c.blocks.filter(b=>b.nucleusId).map(b=>[b.nucleusId,b.number]))
 for(const b of parsed)if(b.nucleusId)b.number=oldNumbers.get(b.nucleusId)
 if(parsed.filter(b=>b.nucleusId).length!==oldNumbers.size)throw Error('Nucleus loss '+c.path)
 c.blocks=parsed
 await fs.writeFile(path.join(out,path.basename(c.path)),fm+body)
}
await fs.writeFile(path.join(out,'payload.json'),JSON.stringify(payload))
await fs.writeFile(path.join(out,'manifest.json'),JSON.stringify({mainChapters:main.length,sourceHashes:hashes,numberMaps:maps,referenceChanges:changes,linkChanges,workbookChanges,notes:['Projection only: master module numbering preserved','All chapter/nucleus order inherited from canonical current API','Digital promise and publisher details remain common unresolved dependency']},null,2))
console.log(JSON.stringify({main:main.length,numberedReferenceChanges:changes.length,readableLinkLabels:linkChanges.length,images:main.flatMap(c=>c.blocks).filter(b=>b.type==='image').length}))
}
// External fallback labels are cosmetic; actual internal targets use the current volume index.
const awaitReadCache=new Map<string,string>()
main().catch(e=>{console.error(e);process.exit(1)})
