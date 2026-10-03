import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { LocalAgentMemory } from '../../src/server/memory/local-agent-memory'
const root=process.cwd(), out='artifacts/review-collana-2026-10-02'
const issues:Record<string,string>={
 'books/vol-02-enti-locali-polizia-locale/chapters/01-come-usare-vol-02-insieme-a-vol-01.md':'E05',
 'books/vol-02-enti-locali-polizia-locale/chapters/03-piano-30-60-90-giorni-vol-02.md':'E01',
 'books/vol-02-enti-locali-polizia-locale/chapters/50-simulazione-finale-vol-02.md':'E01',
 'books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md':'E07',
 'books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md':'E06',
 'books/moduli/m-fc02-agenzie-fiscali/chapters/14-appendici-operative.md':'E06',
 'books/moduli/m-ir01-scuola/chapters/02-sistema-nazionale-autonomia-organizzazione.md':'E09',
 'books/moduli/m-ir01-scuola/chapters/06-dsga-eq-ruolo-uffici-personale.md':'E02, E09',
 'books/moduli/m-ir01-scuola/chapters/12-metodologie-valutazione-digitale-didattico.md':'E03, E08, E09',
 'books/moduli/m-ir01-scuola/chapters/13-progettazione-lezione-simulata.md':'E08',
 'books/moduli/m-tr03-tecnico-ingegneristico/chapters/04-ntc-sismica-geotecnica-sicurezza-strutturale.md':'E04',
 'books/moduli/m-tr03-tecnico-ingegneristico/chapters/13-laboratorio-prove-tecniche.md':'E10',
 'books/moduli/m-tr04-ambiente-protezione-civile/chapters/08-aria-rumore-monitoraggio-dati.md':'E11',
 'books/moduli/m-tr04-ambiente-protezione-civile/chapters/11-rischi-allertamento-it-alert-emergenze.md':'E11'
}
const additionalSamples=new Set([
 'books/moduli/m-tr03-tecnico-ingegneristico/chapters/03-scienza-tecnica-costruzioni.md',
 'books/moduli/m-sa03-dirigenza-medica-sanitaria/chapters/05-epidemiologia-sanita-pubblica-dirigenza.md',
 'books/moduli/m-sp03-magistratura-avvocatura-notariato/chapters/03-avvocatura-stato-prove-ordinamento.md',
 'books/moduli/m-sp03-magistratura-avvocatura-notariato/chapters/06-piano-pluriennale.md',
 'books/il-metodo-bando/chapters/prova-scritta-teorico-pratica.md',
 'books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati.md',
 'books/moduli/m-fc02-agenzie-fiscali/chapters/05b-tutela-processo-tributario.md'
])
async function main(){
 const inventory=JSON.parse(await fs.readFile(`${out}/inventory.json`,'utf8'))
 const gates=JSON.parse(await fs.readFile(`${out}/gates.json`,'utf8')).results
 const gateByFile=new Map(gates.map((g:any)=>[g.payload?.step?.replace(/^10:/,'')||g.file,g]))
 const register:any[]=[]
 const header=`---\nid: review-registro-audit-collana-2026-10-02\ntype: review\ntitle: "Registro per capitolo — audit collana 2 ottobre 2026"\nstatus: in_progress\ndomain: concorsi-pubblici\ntopics: []\nentities: []\nsource_refs: []\nbook_refs: [VOL-01, VOL-02, VOL-03, VOL-04, VOL-05, VOL-06, VOL-07, VOL-08, VOL-09, VOL-10, VOL-11, VOL-12]\nconfidence: medium\nupdated_at: 2026-10-02\ncreated_at: 2026-10-02\nreview_required: true\ncanonical: false\ntags: [audit, registro, revisione-in-corso]\nissue_type: review_tracking\nseverity: medium\naffected_pages: []\n---\n\n# Registro di revisione della collana\n\nRapporto: [[reviews/audit-prepubblicazione-collana-2026-10-02]]. Nessuna riga rappresenta una revisione integrale completata.\n\n**Eseguito globalmente:** inventario, presenza delle source notes dichiarate, controllo dei wikilink e dei titoli di destinazione, estrazione testuale del Book Studio.\n\n**Ancora aperto su ciascun capitolo:** lettura integrale secondo i 30 controlli, verifica di tutti i claim, confronto puntuale con bandi e matrice, soluzione indipendente di tutti i quiz, controllo dell'impaginato. Le letture mirate indicate non chiudono nessuna di queste attività globali.\n\nIl gate è esclusivamente il gate 10 della pipeline: PASS non equivale a correttezza normativa o sufficienza didattica. N/D indica step non disponibile o capitolo di raccordo fuori dai target; non significa che il contenuto non sia mai stato revisionato. Un trattino nella colonna Rilievi significa soltanto nessun rilievo registrato in questo primo giro.\n`
 let markdown=header
 for(const volume of inventory.volumes){
  const reader=JSON.parse(await fs.readFile(`${out}/${volume.code}-reader.json`,'utf8'))
  markdown+=`\n## ${volume.code} — ${volume.title}\n\n| Capitolo / file | Gate 10 corrente | Lettura in questo audit | Rilievi iniziali | Revisione integrale |\n| --- | --- | --- | --- | --- |\n`
  for(const ch of reader){
   const key=ch.file.replace(/^books\//,'')
   const gate:any=gateByFile.get(key)||gateByFile.get(ch.file)||gates.find((g:any)=>g.file===ch.file||g.file===key)
   const state=gate?.payload?.result?(gate.payload.result.passed?'PASS':'NON PASSA'):'N/D'
   const issueIds=[issues[ch.file],state==='NON PASSA'?'E12':''].filter(Boolean).join(', ')||'—'
   const sample=!!issues[ch.file]||additionalSamples.has(ch.file)
   const sha=volume.chapters.find((c:any)=>c.file===`wiki/${ch.file}`)?.sha256
   const item={volume:volume.code,file:ch.file,title:ch.title,sha256:sha,gate10:state,reading:sample?'mirata/parziale':'non eseguita',issues:issueIds,fullReview:'da completare',allClaims:'da completare',allQuizzes:'da completare',visualPdf:'non eseguito'}
   register.push(item)
   markdown+=`| [[${ch.file.replace(/\.md$/,'')}|${ch.title.replaceAll('|','/')}]] | ${state} | ${item.reading} | ${issueIds} | da completare |\n`
  }
 }
 const changed=[]
 for(const volume of inventory.volumes)for(const chapter of volume.chapters){const content=await fs.readFile(chapter.file);const sha=createHash('sha256').update(content).digest('hex');if(sha!==chapter.sha256)changed.push(chapter.file)}
 await fs.writeFile('wiki/reviews/registro-audit-collana-2026-10-02.md',markdown)
 await fs.writeFile(`${out}/chapter-register.json`,JSON.stringify(register,null,2))
 const verification={at:new Date().toISOString(),sourceFiles:inventory.volumes.reduce((n:number,v:any)=>n+v.chapters.length,0),printChapters:register.length,sourceFilesChangedSinceInventory:changed,gateResults:{passed:gates.filter((g:any)=>g.payload?.result?.passed).length,failed:gates.filter((g:any)=>g.payload&&!g.payload?.result?.passed).length,unavailable:gates.filter((g:any)=>g.error).length},note:'No chapter review marked complete. Source-file hashes checked against initial inventory; no PDF visual approval.'}
 await fs.writeFile(`${out}/verification.json`,JSON.stringify(verification,null,2))
 console.log(JSON.stringify(verification))
 const capture=await LocalAgentMemory.fromConfig().captureConversation({scope:'global',route:'codex/audit-prepubblicazione-collana',messages:[{role:'user',content:'Controllare correttezza ed esaustivita dei contenuti di tutti i volumi prima della pubblicazione. Individuare correzioni e integrazioni; applicarle soltanto dopo, in una fase successiva.'}],reply:'Avviato audit collana: inventario 12 volumi, 349 file capitolo, 326 capitoli/appendici cartacei. Report iniziale e registro in wiki/reviews/audit-prepubblicazione-collana-2026-10-02.md e registro-audit-collana-2026-10-02.md. Dodici rilievi E01-E12, proposte non applicate. Revisione sostanziale integrale e PDF ancora aperti; non dichiarare volumi perfetti o interamente verificati. Preservare integrazioni VOL-01/VOL-07 gia in lavorazione e relative esclusioni. Gate positivi non attestano sufficienza semantica.',metadata:{report:'wiki/reviews/audit-prepubblicazione-collana-2026-10-02.md',chapters:register.length,fullReviewComplete:false}})
 console.log(JSON.stringify({memoryConversation:capture.conversationId,atoms: capture.atoms.length}))
 await fs.appendFile('wiki/log.md','\n- 2026-10-02 | audit_prepubblicazione_collana | VOL-01/VOL-12 | Ricognizione dei 12 volumi: 349 file, 326 capitoli/appendici cartacei; 321 gate tentati (266 PASS, 6 non passati per densita, 49 non disponibili nel run-state corrente). Primo rapporto E01-E12 e registro per capitolo in reviews/audit-prepubblicazione-collana-2026-10-02.md e reviews/registro-audit-collana-2026-10-02.md. Verifiche esterne mirate MIM/ARAN/NTC. Nessuna correzione ai libri o modifica della pipeline; revisione integrale dei contenuti, quiz e PDF NON conclusa.\n')
}
main().catch(e=>{console.error(e);process.exitCode=1})
