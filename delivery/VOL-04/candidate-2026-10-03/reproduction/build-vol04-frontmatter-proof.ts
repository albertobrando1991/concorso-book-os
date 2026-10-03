import fs from 'node:fs/promises'
import path from 'node:path'
import crypto from 'node:crypto'
import assert from 'node:assert/strict'
import {parseStudentChapterForExport, type BookStudioData} from '../../../../src/server/book/book-preview'
import {LocalAgentMemory} from '../../../../src/server/memory/local-agent-memory'

async function main() {
  const memory = await LocalAgentMemory.fromConfig().recall({query:'VOL-04 preliminari digitali colophon proiezione PDF KDP master fonte verificata nessuna promessa servizi non disponibili', maxResults:6,maxTotalChars:5000})
  console.log(memory.context)
  const out='artifacts/correzioni-collana-2026-10-02/vol04-proof'
  await fs.mkdir(out,{recursive:true})
  const response=await fetch('http://127.0.0.1:3020/api/book-studio?bookId=volumi%2Fvol-04')
  assert(response.ok,`API ${response.status}`)
  const payload:BookStudioData=await response.json()
  const original=JSON.stringify(payload)
  await fs.writeFile(path.join(out,'source-payload-frontmatter.json'),original)
  const sourceHashes=[]
  const changes=[]
  const targets=[['FM1','01-servizi-digitali.md'],['FM3','03-copyright-colophon.md']]
  for(const [id,file] of targets){
    const chapter=payload.chapters.find(c=>c.outlineSection===id)
    assert(chapter,`Missing ${id}`)
    const sourcePath=`books/vol-04-giustizia-upp/front-matter/${file}`
    const raw=await fs.readFile('wiki/'+sourcePath,'utf8')
    const parsed=parseStudentChapterForExport(raw,sourcePath)
    assert(parsed.blocks.length>0)
    const before=structuredClone(chapter)
    // Dedicated front matter renders the title from blocks, unlike normal chapters.
    chapter.blocks=[{type:'heading',level:1,text:parsed.title},...parsed.blocks]
    chapter.title=parsed.title
    chapter.path=sourcePath
    assert.deepEqual({...chapter,blocks:before.blocks,title:before.title,path:before.path},before)
    sourceHashes.push({path:'wiki/'+sourcePath,sha256:crypto.createHash('sha256').update(raw).digest('hex')})
    changes.push({id,before,after:chapter,allowedFields:['blocks','title','path']})
  }
  const before:BookStudioData=JSON.parse(original)
  const untouched=payload.chapters.filter(c=>!targets.some(([id])=>id===c.outlineSection))
  assert.deepEqual(untouched,before.chapters.filter(c=>!targets.some(([id])=>id===c.outlineSection)))
  for(const chapter of untouched){
    try {const raw=await fs.readFile('wiki/'+chapter.path);sourceHashes.push({path:'wiki/'+chapter.path,sha256:crypto.createHash('sha256').update(raw).digest('hex')})}catch(error){if(!chapter.isGenerated)throw error}
  }
  assert.deepEqual({...payload,chapters:before.chapters},before)
  const output=JSON.stringify(payload)
  await fs.writeFile(path.join(out,'payload-frontmatter.json'),output)
  await fs.writeFile(path.join(out,'frontmatter-projection-manifest.json'),JSON.stringify({scope:'Only FM1 and FM3 blocks, title and path; source files and renderer unchanged',createdAt:new Date().toISOString(),changes,sourceHashes,unchangedChapters:untouched.length,sourcePayloadSha256:crypto.createHash('sha256').update(original).digest('hex'),projectedPayloadSha256:crypto.createHash('sha256').update(output).digest('hex')},null,2))
  const base=await fs.readFile('artifacts/correzioni-collana-2026-10-02/export-proof.mjs','utf8')
  const helper=base.replace("const bookId=process.argv[2]||'volumi/vol-12'","const bookId='volumi/vol-04'")
    .replace("const label=process.argv[3]||bookId.split('/').at(-1)","const label='vol-04-reader-final-20261003'")
    .replace('page.setDefaultTimeout(180000)',`page.setDefaultTimeout(180000)\nconst frozenPayload=await fs.readFile('artifacts/correzioni-collana-2026-10-02/vol04-proof/payload-frontmatter.json','utf8')\nawait page.route('**/api/book-studio?**', async route=>{const url=new URL(route.request().url()); if(url.searchParams.get('bookId')===bookId) await route.fulfill({status:200,contentType:'application/json',body:frozenPayload}); else await route.continue()})`)
  assert.notEqual(helper,base)
  await fs.writeFile('artifacts/correzioni-collana-2026-10-02/export-vol04-frontmatter-proof.mjs',helper)
  console.log(JSON.stringify({changed:changes.map(c=>c.id),unchangedChapters:untouched.length,sourceHashes:sourceHashes.length}))
}
main().catch(e=>{console.error(e);process.exit(1)})
