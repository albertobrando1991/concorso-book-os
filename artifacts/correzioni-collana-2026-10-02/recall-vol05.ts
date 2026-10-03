import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
async function main() {
 const result = await LocalAgentMemory.fromConfig().recall({query: 'VOL-05 authority AGCM ARERA AGCOM CONSOB IVASS Banca Italia Garante ANAC economia regolazione sanzioni correzione editoriale copertura fonti pipeline', maxResults: 10, maxTotalChars: 7000})
 console.log(result.context)
}
main()
