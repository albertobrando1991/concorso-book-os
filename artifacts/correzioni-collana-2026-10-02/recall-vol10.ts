import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
 const result = await LocalAgentMemory.fromConfig().recall({query: 'VOL-10 NTC edilizia urbanistica esecuzione collaudo strutture BIM catasto correzione editoriale copertura fonti pipeline', maxResults: 10, maxTotalChars: 7000})
 console.log(result.context)
}
main()
