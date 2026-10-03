from pathlib import Path
import json,re,hashlib
A=Path(__file__).parent;root=A.parent.parent
p=root/'wiki/books/moduli/m-sa02-professioni-sanitarie/chapters/05-valutazione-clinica-triage-urgenza-emergenza.md'
before=hashlib.sha256(p.read_bytes()).hexdigest();text=p.read_text(encoding='utf8')
assert 'dati_operativi_audit:' not in text
metadata=[]
names={'DO-SA02-05-NEWS2-ER-2024':'NEWS2: calcolo, scale e limiti','DO-SA02-05-TRIAGE-2019':'Triage: codici e tempi di accesso'}
def replace(m):
    block=m.group(0);lines=[re.sub(r'^> ?', '', l) for l in block.splitlines()]
    id=re.search(r'DO-SA02-05-[A-Z0-9-]+',lines[0])[0]
    source=re.search(r'^Fonte: (.*?) · Versione: (.*?) · Verificata al: (.*?)$', '\n'.join(lines),re.M)
    metadata.append({'id':id,'title':names[id],'heading':names[id],'auditArea':'clinico-assistenziale','source':source[1],'version':source[2],'verifiedAt':source[3],'recheck':'Prima di ogni nuova edizione e al cut-off del volume, confrontando versione e protocollo del setting.'})
    body=[]
    for line in lines[1:]:
        if line.startswith('Audit automatico:') or line.startswith('**Data di ricontrollo editoriale:**'):continue
        if line.startswith('Fonte:'):
            if 'NEWS2' in id:continue
            line='**Fonte e versione:** Ministero della Salute, *Linee di indirizzo nazionali sul triage intraospedaliero*, 2019, tabelle 1–2. Quadro verificato al 3 ottobre 2026.'
        body.append(line)
    return '### '+names[id]+'\n\n'+'\n'.join(body).strip()+'\n'
text=re.sub(r'^> \*\*Dato operativo · DO-SA02-05-.*(?:\n>.*)*',replace,text,flags=re.M)
assert len(metadata)==2
text=text.replace('dati_operativi: ["DO-SA02-05-NEWS2-ER-2024", "DO-SA02-05-TRIAGE-2019"]','dati_operativi: ["DO-SA02-05-NEWS2-ER-2024", "DO-SA02-05-TRIAGE-2019"]\ndati_operativi_audit: '+json.dumps(metadata,ensure_ascii=False))
text=text.replace('Il box seguente riporta i valori','La tabella seguente riporta i valori')
p.write_text(text,encoding='utf8',newline='\n')
after=hashlib.sha256(p.read_bytes()).hexdigest()
delta={'path':p.relative_to(root).as_posix(),'beforeSHA256':before,'sha256':after,'change':'Due dati operativi: metadati di audit nel frontmatter, tabelle NEWS2 e triage native e leggibili. Dati, ambito, fonti, versioni e cautele cliniche conservati; istruzione di ricontrollo editoriale esclusa dal corpo.','status':'applied; PDF verification pending'}
(A/'VOL-07-production-native-changes.json').write_text(json.dumps([delta],ensure_ascii=False,indent=2),encoding='utf8')
freeze=A/'M-SA02-freeze.json';data=json.loads(freeze.read_text(encoding='utf8'));data['controlledPrintCorrections']={'date':'2026-10-03','files':[delta],'verification':'Dati clinici invariati; modifica di proiezione autorizzata. Nuova prova PDF pendente.'};freeze.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(delta,ensure_ascii=False))
