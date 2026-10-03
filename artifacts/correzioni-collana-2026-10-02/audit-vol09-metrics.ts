import { readFileSync, readdirSync, writeFileSync } from 'node:fs'
import { analyzeDidacticDensity, runDidacticDensityGate } from '../../src/pipeline/gates/didactic-density-gate'
const base='wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters'
const rows=readdirSync(base).filter(x=>x.endsWith('.md')).sort().map(file=>{
 const content=readFileSync(`${base}/${file}`,'utf8');const metrics=analyzeDidacticDensity(content)
 return {file,metrics,gate:runDidacticDensityGate({content,chapterPath:`${base}/${file}`})}
})
writeFileSync('artifacts/correzioni-collana-2026-10-02/vol09-density.json',JSON.stringify(rows,null,2))
console.log(JSON.stringify(rows.map(x=>({file:x.file,words:x.metrics.chapterWords,nuclei:x.metrics.nuclei.map(n=>[n.id,n.words]),quiz:x.metrics.quizzes,cases:x.metrics.cases,blockers:x.gate.blockers,warnings:x.gate.warnings})),null,2))
