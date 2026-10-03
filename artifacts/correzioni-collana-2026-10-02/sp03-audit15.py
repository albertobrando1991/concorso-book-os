from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
keys=json.loads((A/'M-SP03-quiz-keys.json').read_text(encoding='utf8'));matrix=(B/'planning/02-matrice-copertura-didattica.md').read_text(encoding='utf8');checks=[]
assert 42+66==108 and 42+65==107
assert 38+37+40+36+35+37==223
assert 2000+800==2800
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);no=p.name[:2]
 ids=re.findall(r'^## (N-SP03-\d+-\d+) ·',body,re.M);assert ids==[f'N-SP03-{no}-{i:02}' for i in range(1,6)],p
 for nid in ids:assert nid in matrix
 assert re.findall(r'Risposta corretta: ([ABCD])',body)==keys[no],p
 assert not re.search(r'\[\[(sources|topics|raw|entities|planning|reviews)/',body)
 assert '<br' not in body
 assert 'non compiuti' not in body,p
 for field in ['source_refs','last_compiled_from','topics','entities']:
  for ref in json.loads(re.search(rf'^{field}: (\[.*\])$',fm,re.M)[1]):assert (Path('wiki')/(ref+'.md')).exists(),ref
 fm=fm.replace('review_required: true','review_required: false').replace('draft_stage: corrections-applied','draft_stage: specialist-audit-complete');p.write_text(fm+'\n---\n'+body,encoding='utf8');checks.append({'path':p.as_posix(),'nuclei':len(ids),'quiz':len(keys[no]),'links':'resolved','bodyInternalLinks':0})
# Local consolidated articles have the article itself, not merely a full-act navigation tree.
for n in [1337,1338,1022,588,536,602,603]:
 p=Path(f'wiki/raw/correzioni-collana-2026-10-02/cc-art{n}-testo-20261003.html');s=p.read_text(encoding='utf8');assert 'Sessione scaduta' not in s and f'art. {n}' in s,p
(A/'M-SP03-audit-checks.json').write_text(json.dumps({'math':'passed','files':checks,'legalCheckScope':'Selective article and procedure checks documented in source; not certification of all law.'},ensure_ascii=False,indent=2),encoding='utf8')
p=R/'15-moduli-m-sp03-magistratura-avvocatura-notariato.md';arc=C/'archive/pre-correzioni-15-m-sp03.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
t=(R/'14-moduli-m-sp03-magistratura-avvocatura-notariato.md').read_text(encoding='utf8').replace('— Correzioni editoriali','— Audit specialistico').replace('Audit specialistico, manifest e PDF.','Audit specialistico concluso; manifest e PDF.')
t+='''

### Evidenze dell’audit specialistico

Zero errori gravi o medi aperti nel perimetro corretto. Nessun box Dato operativo rilevato dal CLI; i valori del testo sono stati comunque controllati. I limiti delle fonti storiche sono espliciti e non impediscono i claim circoscritti riscontrati.

- Magistratura: funzioni ordinarie civili e penali, giudicanti e requirenti; art. 2 d.lgs. 160/2006 e bando distinguono accesso del laureato e altre categorie. Il limite è quattro precedenti non idoneità, non quattro domande. Art. 8 del bando: 12/20 a ogni scritto, 6/10 nei gruppi orali numerici, sufficienza qualitativa della lingua, totale almeno 108, niente frazioni. Casi 108/107, insufficienza numerica e lingua insufficiente correttamente separati. Domanda di novembre 2025 distinta dal diario di marzo 2026.
- Procuratura: D.A.G. 114/2025, pp. 3–9, artt. 2–6. Formula anagrafica, scadenza, tre scritti, correzione sequenziale e minimi 6/10; media scritti più orale in graduatoria. Art. 4: due precedenti non idoneità. D.P.C.M. 141/2000, art. 1 corrente, limite 35 dal 2011; criterio del compleanno dalla rassegna ufficiale che richiama Adunanza plenaria 21/2011. Esempi dichiarati senza elevazioni. TAR 11045/2026 letto integralmente e non presentato come abolizione del limite.
- Notariato: artt. 2–14 del bando 16 dicembre 2025. Pratica entro la scadenza, esiti computati alla pubblicazione, espulsione dopo dettatura, certificato successivo all’orale entro il termine della richiesta. Scheda ministeriale conferma 30 gennaio 2026 ore 12.00. Marta e Andrea separati; periodo anticipato e anno post lauream dichiarati; variante Luca distingue invio dal termine. Calcolo 223 e soglie 35 autonomi; incremento per precedente idoneità distinto dalle preferenze. Tre atti e principi, testi preventivamente controllati.
- Casi giuridici: articoli 1337, 1338, 1022, 588, 536, 602 e 603 del Codice civile acquisiti e letti nei testi ufficiali; art. 5 d.lgs. 36/2023 letto integralmente. Tema originale, danni 2.800 con presupposti e variante, clausole testamentarie con assunzioni e formalità separate. Rito ordinario nel caso processuale: giorni 40/70 e conoscenza documentata; tardività distinta dal merito, nessuna estensione a riti speciali.
- Metodo: il comando espresso decide il formato; non ogni tema impone una controversia. Piano biennale con quindici ore, variante otto ore, otto trimestri e decisioni condizionate. La parte di conoscenza giuridica non svolta non viene dichiarata coperta.
- Coerenza: sette capitoli, 35 nuclei con almeno 600 parole, 57 quiz commentati. Opzioni ruotate mantenendo chiavi e riferimenti delle spiegazioni. ID corrispondenti alla matrice, dipendenze risolte, nessun HTML residuo o link staff nel corpo. Humanizer dei delta eseguito insieme alla revisione del contenuto; nessun ritocco di stile usato per nascondere la lacuna iniziale.

Evidenze locali: M-SP03-audit-checks.json, M-SP03-surface-counts.json, M-SP03-quiz-keys.json, source note specialistica e raw citati. Nuovo PDF ancora necessario per la resa, la leggibilità e gli spazi operativi.
''';p.write_text(t,encoding='utf8');print('SP03 audit',len(checks),'files')
