import {readFile,writeFile} from 'node:fs/promises'
import path from 'node:path'
import {buildBookStudioData} from '../../src/server/book/book-preview'
import {FileWikiStore} from '../../src/server/wiki/file-store'
async function main(){
 const store=new FileWikiStore(path.resolve('wiki'))
 const rows=[]
 for(const id of ['volumi/vol-03','volumi/vol-06','volumi/vol-12']){
  const data=await buildBookStudioData(store,id)
  const chapters=data.chapters.filter(c=>c.sectionType==='chapter')
  const nuclei=chapters.flatMap(c=>c.blocks.filter(b=>b.nucleusId))
  const selected=chapters.filter(c=>c.path.includes('m-ir04')||c.path.includes('m-fc02')||c.path.includes('m-ir02')&&c.path.includes('/09-'))
  rows.push({id,chapters:chapters.length,nuclei:nuclei.length,selected:selected.map(c=>({path:c.path,outline:c.outlineSection,moduleOutline:c.moduleOutlineSection,nuclei:c.blocks.filter(b=>b.nucleusId).map(b=>({id:b.nucleusId,number:b.number,title:b.text}))}))})
 }
 await writeFile('artifacts/correzioni-collana-2026-10-02/projection-verification.json',JSON.stringify(rows,null,2))
 console.log(rows.map(r=>({id:r.id,chapters:r.chapters,nuclei:r.nuclei,selected:r.selected.map(c=>c.path.split('/').at(-1))})))
}
main()
