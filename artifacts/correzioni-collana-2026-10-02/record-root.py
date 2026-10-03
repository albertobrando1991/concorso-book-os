from pathlib import Path
import json,hashlib,sys

base=Path('artifacts/correzioni-collana-2026-10-02')
root=Path('wiki/books/il-metodo-bando/chapters')
if sys.argv[1]=='constitution':
    p=root/'costituzione-e-ordinamento-dello-stato.md'
    text=p.read_text(encoding='utf8')
    ref='sources/vol-01-costituzione-correzioni-2026-10-02.md'
    for key in ['source_refs','last_compiled_from']:
        lines=text.splitlines()
        line=next(l for l in lines if l.startswith(key+':'))
        if ref not in line:
            text=text.replace(line,line[:-1]+', "'+ref+'"]',1)
    text=text.replace('correction_source_refs: ["'+ref+'"]\n','')
    p.write_text(text,encoding='utf8')
    topic=Path('wiki/topics/diritto-costituzionale.md')
    current=topic.read_text(encoding='utf8')
    if '## Correzioni consolidate del 2 ottobre 2026' not in current:
        with topic.open('a',encoding='utf8') as out:
            out.write('\n\n## Correzioni consolidate del 2 ottobre 2026\n\n[[sources/vol-01-costituzione-correzioni-2026-10-02]] distingue riunioni e preavviso, trattamenti obbligatori, collocazione dello sport, controlli della Corte dei conti e decisioni UE. Consolida inoltre composizione/elettorato, maggioranze e procedimenti parlamentari, fiducia e revisione costituzionale con esempi e quiz nel capitolo 4. I rinvii specialistici agli enti locali restano da verificare sulla versione corretta del VOL-02.\n')
    reg=base/'registro-applicazione.json'
    rows=json.loads(reg.read_text(encoding='utf8'))
    for r in rows:
        if r['id'] in ['V01-02','V01-03','V01-04','V01-05','V01-06','V01-07','V01-08','V01-09']:
            r['status']='applicato-da-verificare'
            r['changedFiles']=[str(p).replace('\\','/'),'wiki/'+ref,'wiki/topics/diritto-costituzionale.md']
            r['verification']=['Fonte ufficiale e nota consolidata; rilettura del delta, 6 quiz e caso con quorum; controllo indipendente e PDF ancora da eseguire']
            r['sourceSha256']=hashlib.sha256(p.read_bytes()).hexdigest()
    reg.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
    print('Recorded V01-02 through V01-09 as applied, independent verification pending')
