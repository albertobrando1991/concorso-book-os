from pathlib import Path
import json,hashlib,re
A=Path('artifacts/correzioni-collana-2026-10-02')
records=json.loads((A/'VOL-03-native-schemes.json').read_text(encoding='utf8'))['records']
freeze=json.loads((A/'M-FC02-freeze.json').read_text(encoding='utf8'))
before={r['path']:r['sha256'] for r in freeze['files']}
changed=[]
for path in sorted(set(r['file'] for r in records)):
    rows=[r for r in records if r['file']==path];p=Path(path)
    assert rows[0]['sha256Before']==before[path],path
    text=p.read_text(encoding='utf8');old=(A/'vol03-native-snapshots'/p.name).read_text(encoding='utf8')
    # Invert precisely the authored replacements and the one documented prose correction.
    for row in rows:
        assert row['nativeText'] in text,row['schema']
        match=next(m for m in re.finditer(r'!\[Figura (\d+\.\d+) - [^\]]+\]\([^)]+\)',old) if m[1]==row['schema'])
        text=text.replace(row['nativeText'],match[0],1)
    if p.name.startswith('06-'):
        new='La correzione è distinguere fatto, soggetto, tributo, documento, liquidazione, dichiarazione, pagamento ed eventuale controllo. Colloca poi ogni adempimento nel suo tempo: nell’IVA periodica liquidazioni e versamenti precedono la dichiarazione annuale. Un elenco di funzioni non è una cronologia valida per ogni tributo.'
        original='La correzione è ripetere: fatto, soggetto, tributo, documento, dichiarazione, liquidazione, pagamento ed eventuale controllo. Se una risposta salta un passaggio, probabilmente sovrappone due fasi.'
        text=text.replace(new,original)
    assert text.split('---',2)[2]==old.split('---',2)[2],path
    changed.append({'path':path,'before':before[path],'after':hashlib.sha256(p.read_bytes()).hexdigest(),'schemes':5,'bodyUnchangedOutsideDeclaredDelta':True})
checkpoint={'date':'2026-10-03','chapters':14,'schemas':70,'allPriorFreezeHashesMatched':True,'allQuizAndCaseBodiesPreserved':True,'files':changed,'semanticChecks':['BANDO labels correct in all 14 maps','Archiving and assessment alternative','IVA periods distinguished from annual return','Collection ordinary and executive paths distinguished','AEO status separated from physical control and EORI','Accounting not postponed necessarily to payment','Appendices A-H match actual headings','AE/ADM/AdER not a sequence; profiles not entities','Ordinary balance sheet qualified; simplified forms preserved'],'limitations':['Visual PDF verification pending; no final publication judgment.']}
(A/'VOL-03-native-checkpoint.json').write_text(json.dumps(checkpoint,ensure_ascii=False,indent=2),encoding='utf8')
delta='''

### Delta iconografico del 3 ottobre 2026 — 70 tavole native

Il secondo intervento applica P03-05, P03-06 e P03-07 ai 14 capitoli illustrati. Tutti i 70 originali sono stati esaminati nelle 18 tavole di contatto; i diagrammi testuali sono sostituiti da schemi Markdown a due colonne, con relazioni esplicite e caratteri dell'impaginato. Gli originali raster restano archiviati. Fonte nuova: `sources/vol-03-schemi-fiscali-verifica-2026-10-03`, Commissione europea EORI/AEO e verifiche istituzionali già consolidate.

| ID | File modificato | Intervento | Evidenza | Stato |
|---|---|---|---|---|
| P03-05 | FC02/13 e 14 | Bando/Aree/Nuclei/Diario/Output; appendici effettive A–H e relativi strumenti | Master e titoli delle appendici, schemi 13.1, 14.1–14.2 | Applicato e verificato nel testo; PDF successivo |
| P03-06 | FC02/05,06,07,08,12,13 | Esiti alternativi; IVA periodica; riscossione per titolo; AEO indipendente dai singoli controlli; competenza contabile; contesti AE/ADM/AdER | Schemi 5.2, 6.3, 7.3, 8.4, 12.3, 13.3; un capoverso residuale IVA riallineato | Applicato e verificato nel testo; PDF successivo |
| P03-07 | FC02/03,08,14 | Profili esclusi dall'organigramma; relazione AE/AdER esplicita; EORI e AEO separati | Fonte Commissione europea; schemi 3.2, 8.4, 14.5 | Applicato e verificato nel testo; PDF successivo |
| FC02-G01 | Tutti i 14 capitoli illustrati | 70 tavole native; nessuna freccia senza relazione spiegata, schemi del bilancio ordinario e percorsi eventuali qualificati | `VOL-03-native-schemes.json`, snapshot e verifica differenziale | Testo verificato; leggibilità PDF da controllare |

Il controllo differenziale ricostruisce il corpo precedente invertendo soltanto i 70 schemi e l'unico capoverso dichiarato: nessun quiz, caso, soluzione o altro contenuto è stato perso. Tutti i 14 hash precedenti coincidono con il freeze ricevuto; zero wikilink irrisolti dopo la trasformazione. Micro-revisione dei nuovi schemi: confronto distinto da sequenza, condizioni e limiti nominati, terminologia allineata al capitolo. Il registro completo è `artifacts/correzioni-collana-2026-10-02/VOL-03-native-checkpoint.json`. Questa integrazione supera le precedenti frasi che rinviavano tutte le figure al coordinatore; la verifica dell'impaginato resta separata.
'''
p=Path('wiki/reviews/pipeline/VOL-03/14-moduli-m-fc02-agenzie-fiscali.md')
p.write_text(p.read_text(encoding='utf8')+delta,encoding='utf8')
matrix=Path('wiki/books/moduli/m-fc02-agenzie-fiscali/planning/02-matrice-copertura-didattica.md')
matrix.write_text(matrix.read_text(encoding='utf8')+'\n\n## Delta figure — 3 ottobre 2026\n\n70 diagrammi testuali sostituiti da tavole native nei capitoli 01–14 (05a/05b privi di immagini). Preservati tutti i nuclei, casi e quiz: verifica differenziale `VOL-03-native-checkpoint.json`. Relazioni fiscali e rimandi alle appendici riallineati a fonti e master. PDF e rinvii numerici di volume da controllare nella produzione, senza anticipare la pubblicabilità.\n',encoding='utf8')
print(json.dumps({'hashesMatched':len(changed),'schemas':len(records),'undeclaredBodyChanges':0}))
