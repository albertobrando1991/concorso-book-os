import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
 const result = await LocalAgentMemory.fromConfig().recall({query: 'VOL-03 ministeri agenzie fiscali enti previdenza INPS INAIL correzione editoriale copertura fonti pipeline', maxResults: 10, maxTotalChars: 7000})
 console.log(result.context)
}
main()
