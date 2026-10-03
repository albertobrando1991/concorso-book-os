import fs from 'node:fs/promises'
import path from 'node:path'
import { TEXT_VOLUME_CATALOG } from '../../src/catalog/text-volumes'
import { loadVolumeSpec } from '../../src/pipeline/spec/load-volume-spec'
import { runCommand } from '../../src/pipeline/cli/commands'
import { parseArgs } from '../../src/pipeline/cli/args'
async function main(){
 const results:any[]=[]
 for(const volume of TEXT_VOLUME_CATALOG){
  const {spec}=await loadVolumeSpec({wikiRoot:path.join(process.cwd(),'wiki'),volumeCode:volume.code})
  for(const module of spec.modules)for(const ch of module.chapters){
   try {const gate=await runCommand(parseArgs(['gate',volume.code,'--step','10','--module',module.code,'--chapter',ch.number,'--json']));results.push({volume:volume.code,module:module.code,chapter:ch.number,file:ch.file,payload:gate.payload})}
   catch(e){results.push({volume:volume.code,module:module.code,chapter:ch.number,file:ch.file,error:String(e)})}
  }
  const rows=results.filter(r=>r.volume===volume.code);console.log(JSON.stringify({volume:volume.code,total:rows.length,passed:rows.filter(r=>r.payload?.result?.passed).length,failed:rows.filter(r=>r.payload&&!r.payload?.result?.passed).map(r=>({chapter:r.chapter,module:r.module,blockers:r.payload?.result?.blockers})),unavailable:rows.filter(r=>r.error).length}))
 }
 await fs.writeFile('artifacts/review-collana-2026-10-02/gates.json',JSON.stringify({createdAt:new Date().toISOString(),mode:'read-only CLI gate commands; no complete/next/state changes',results},null,2))
}
main()
