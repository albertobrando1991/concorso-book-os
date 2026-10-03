import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
 const result = await LocalAgentMemory.fromConfig().recall({query: 'VOL-08 ICT cyber cloud NIS2 AI open data procurement correzione editoriale copertura fonti pipeline', maxResults: 10, maxTotalChars: 7000})
 console.log(result.context)
}
main()
