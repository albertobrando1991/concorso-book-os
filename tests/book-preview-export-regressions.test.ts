import { mkdir, mkdtemp, rm, writeFile } from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { describe, expect, it } from 'vitest'
import { buildBookStudioData, parseStudentChapterForExport } from '@/src/server/book/book-preview'
import { FileWikiStore } from '@/src/server/wiki/file-store'

const sourcePath = 'books/moduli/m-ir02-universita-ricerca/chapters/09-biblioteche.md'
function chapter(body: string, title = 'Capitolo di prova') {
  return `---\ntitle: ${title}\noutline_section: 9\n---\n${body}`
}

describe('export editorial regression coverage', () => {
  it('attaches an italic paragraph caption to the preceding image', () => {
    const result=parseStudentChapterForExport(chapter('Una spiegazione introduttiva presenta lo schema e il relativo percorso operativo con tutte le informazioni necessarie al lettore.\n\n![Mappa](../assets/mappa.png)\n\n*Figura 2.1 - La mappa collega requisiti, prove e piano di studio.*\n\nIl paragrafo successivo resta nel corpo del capitolo.'),sourcePath)
    expect(result.blocks.find(b=>b.type==='image')).toMatchObject({caption:'Figura 2.1 - La mappa collega requisiti, prove e piano di studio.'})
    expect(result.blocks.filter(b=>b.type==='paragraph').some(b=>b.text?.startsWith('Figura 2.1'))).toBe(false)
    expect(result.blocks.at(-1)?.text).toBe('Il paragrafo successivo resta nel corpo del capitolo.')
  })

  it('does not discard surplus cells from a malformed wide source table', () => {
    const result=parseStudentChapterForExport(chapter('Questa tabella del manoscritto ha celle senza intestazione: i dati devono essere conservati e il difetto resta da correggere.\n\n| Chiave | A | B | C | D |\n| --- | --- | --- | --- | --- |\n| R1 | uno | due | tre | quattro | cinque | sei | sette | VALORE DA NON PERDERE |'),sourcePath)
    expect(JSON.stringify(result.blocks)).toContain('VALORE DA NON PERDERE')
  })

  it('keeps question, options and explanation in source order without requiring blank lines', () => {
    const result=parseStudentChapterForExport(chapter('Un’introduzione spiega come risolvere i quiz e controllare il ragionamento dopo aver scelto la risposta corretta.\n\n1. Quale regola si applica al caso?\nA. Prima alternativa\nB. Seconda alternativa\nC. Terza alternativa\nD. Quarta alternativa\nRisposta corretta: B. La seconda alternativa applica la regola al caso concreto.\n\n## Sezione successiva'),sourcePath)
    const content=result.blocks.slice(1).map(b=>b.type==='list'?b.items?.join(' / '):b.text)
    expect(content).toEqual(['Quale regola si applica al caso?','A. Prima alternativa / B. Seconda alternativa / C. Terza alternativa / D. Quarta alternativa','Risposta corretta: B. La seconda alternativa applica la regola al caso concreto.','Sezione successiva'])
  })

  it('keeps line breaks and literal pipes inside table cells without adding columns', () => {
    const result=parseStudentChapterForExport(chapter('Un’introduzione presenta questa tabella didattica completa, con simboli e più righe nella stessa cella.\n\n| Campo | Valore |\n| --- | --- |\n| Accesso | Primo<br>Secondo<br />Terzo |\n| Simboli | `A|B` e [[topics/prova|alias]] e C\\|D |'),sourcePath)
    const table=result.blocks.find(b=>b.type==='table')!
    const rows=result.blocks.filter(b=>b.type==='table').flatMap(b=>b.rows||[])
    expect(table.headers).toEqual(['Campo','Valore'])
    expect(rows).toEqual([['Accesso','Primo\nSecondo\nTerzo'],['Simboli','A|B e alias e C|D']])
  })

  it('divides a wide table into readable panels while retaining every keyed field', () => {
    const result=parseStudentChapterForExport(chapter('Una tabella con molti campi deve restare completa e leggibile nel formato paperback della collana.\n\n| Caso | A | B | C | D | E | F | G |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| R1 | a1 | b1 | c1 | d1 | e1 | f1 | g1 |\n| R2 | a2 | b2 | c2 | d2 | e2 | f2 | g2 |'),sourcePath)
    const tables=result.blocks.filter(b=>b.type==='table')
    expect(tables.every(t=>(t.headers?.length||0)<=4)).toBe(true)
    for(const table of tables) expect(table.headers?.[0]).toBe('Caso')
    const reconstructed: Record<string,Record<string,string>>={}
    for(const table of tables) for(const row of table.rows||[]) for(let c=1;c<row.length;c++) (reconstructed[row[0]]??={})[table.headers![c]]=row[c]
    expect(reconstructed).toEqual({R1:{A:'a1',B:'b1',C:'c1',D:'d1',E:'e1',F:'f1',G:'g1'},R2:{A:'a2',B:'b2',C:'c2',D:'d2',E:'e2',F:'f2',G:'g2'}})
  })

  it('removes the repeated opening title after an introductory note without removing the note', () => {
    const result = parseStudentChapterForExport(chapter('> [!NOTE]\n> Nota introduttiva da conservare perché chiarisce il perimetro e le condizioni di utilizzo del capitolo.\n\n## Capitolo di prova\n\n### Obiettivo\n\nTesto autosufficiente destinato al candidato.'), sourcePath)
    expect(result.blocks.filter(b=>b.type==='heading' && b.text==='Capitolo di prova')).toHaveLength(0)
    expect(result.blocks[0].text).toContain('Nota introduttiva da conservare')
  })

  it('keeps an explicit caption attached to its image with the full explanatory text', () => {
    const result = parseStudentChapterForExport(chapter('Un’introduzione abbastanza estesa accompagna lo schema didattico e lo collega al percorso del lettore.\n\n![Descrizione accessibile](../assets/schema.png)\n\n> Figura 1 — Il percorso\n> Una spiegazione completa della figura che deve restare leggibile anche alla fine della pagina.'), sourcePath)
    const image = result.blocks.find(b=>b.type==='image')
    expect(image).toMatchObject({alt:'Descrizione accessibile',caption:'Figura 1 — Il percorso\nUna spiegazione completa della figura che deve restare leggibile anche alla fine della pagina.'})
    expect(result.blocks.filter(b=>b.calloutType==='caption')).toHaveLength(0)
  })

  it('uses a unique progressive display number while retaining distinct nucleus ids', async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), 'export-nuclei-'))
    try {
      const dir = path.join(root,'books/moduli/m-fc02-agenzie-fiscali/chapters')
      await mkdir(dir,{recursive:true})
      await writeFile(path.join(dir,'../index.md'),'---\ntitle: Agenzie fiscali\n---\n# Agenzie fiscali')
      await writeFile(path.join(dir,'01.md'), chapter('### N-FC02-01-01 · Primo nucleo\n\nContenuto del primo nucleo didattico conservato integralmente.\n\n### N-SP01-01-01 · Secondo nucleo\n\nContenuto del secondo nucleo didattico conservato integralmente.'))
      const data=await buildBookStudioData(new FileWikiStore(root),'volumi/vol-03')
      const headings=data.chapters.find(c=>c.sectionType==='chapter')!.blocks.filter(b=>b.nucleusId)
      expect(headings.map(b=>[b.number,b.nucleusId])).toEqual([['1.1','N-FC02-01-01'],['1.2','N-SP01-01-01']])
    } finally { await rm(root,{recursive:true,force:true}) }
  })

  it('addresses the reader in generated preliminaries rather than production staff', async () => {
    const root=await mkdtemp(path.join(os.tmpdir(),'export-prelim-'))
    try {
      for (const id of ['volumi/vol-07','volumi/vol-10']) {
        const data=await buildBookStudioData(new FileWikiStore(root),id)
        const copy=JSON.stringify(data.chapters.filter(c=>c.sectionType==='front_matter').flatMap(c=>c.blocks))
        expect(copy).not.toMatch(/prima della pubblicazione|pubblicazione definitiva|Verticale profondo|forte bisogno di review/)
        expect(copy).toContain('fonti ufficiali')
      }
    } finally { await rm(root,{recursive:true,force:true}) }
  })

  it('keeps teaching sections and all five nuclei in the fallback while excluding staff notes', () => {
    const content = chapter(`## Spiegazione\n${Array.from({length:5}, (_, i) => `### N-IR02-09-0${i+1} · Nucleo ${i+1}\n\nContenuto didattico indispensabile numero ${i+1}: definizione, funzione e applicazione al caso del candidato.`).join('\n\n')}\n\n## Esempi\n\nL’esempio concreto resta parte del libro e consente di applicare le cinque regole appena apprese.\n\n## Note di review\n\nNOTA STAFF RISERVATA`)
    const result = parseStudentChapterForExport(content, sourcePath)
    expect(result.blocks.filter(b => b.nucleusId).map(b => b.nucleusId)).toEqual(['N-IR02-09-01','N-IR02-09-02','N-IR02-09-03','N-IR02-09-04','N-IR02-09-05'])
    expect(result.markdown).toContain('L’esempio concreto resta parte del libro')
    expect(result.markdown).not.toContain('NOTA STAFF RISERVATA')
  })

  it('preserves every block of a long published chapter in Book Studio', async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), 'export-long-'))
    try {
      const dir = path.join(root, 'books/test-book/chapters')
      await mkdir(dir, {recursive:true})
      await writeFile(path.join(dir,'01.md'), chapter(Array.from({length:540},(_,i)=>`Paragrafo ${i+1}: contenuto didattico da preservare integralmente nella versione stampata.`).join('\n\n')))
      const data = await buildBookStudioData(new FileWikiStore(root), 'test-book')
      expect(data.chapters[0].blocks).toHaveLength(540)
      expect(data.chapters[0].blocks.at(-1)?.text).toContain('Paragrafo 540:')
    } finally { await rm(root, {recursive:true,force:true}) }
  })

  it('sorts numeric chapter labels and letter suffixes before the next chapter', async () => {
    const root = await mkdtemp(path.join(os.tmpdir(), 'export-order-'))
    try {
      const dir = path.join(root, 'books/test-book/chapters')
      await mkdir(dir, {recursive:true})
      for (const [label,title] of [['Capitolo 10','A'],['5b','B'],['5a','C'],['6','D'],['5','E'],['Capitolo 02','Z'],['A','Appendice']]) {
        await writeFile(path.join(dir,`${title}.md`), `---\ntitle: ${title}\noutline_section: ${label}\n---\nUn capitolo pubblico con contenuti autosufficienti e informazioni utili alla prova del candidato.`)
      }
      const data = await buildBookStudioData(new FileWikiStore(root), 'test-book')
      expect(data.chapters.map(c=>c.outlineSection)).toEqual(['Capitolo 02','5','5a','5b','6','Capitolo 10','A'])
    } finally { await rm(root, {recursive:true,force:true}) }
  })
})
