import {LocalAgentMemory} from '../../src/server/memory/local-agent-memory'
async function main() {
 const r=await LocalAgentMemory.fromConfig().recall({scope:'global',query:'consegna collana 577 preflight copertine digitale pubblicabilità',maxResults:6,maxTotalChars:6500});
 console.log(r.context);
}
main().catch(e=>{console.error(e);process.exitCode=1});
