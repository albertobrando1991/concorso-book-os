from pathlib import Path
import re,json,hashlib

root=Path('wiki/reviews/pipeline/VOL-07')
p=root/'14-moduli-m-sa01-sanita-amministrativa.md'
archive=root/'archive'/'14-moduli-m-sa01-sanita-amministrativa-int-prima-correzioni.md'
archive.parent.mkdir(exist_ok=True)
if not archive.exists():archive.write_bytes(p.read_bytes())
state=json.loads(Path('artifacts/correzioni-collana-2026-10-02/VOL-07-changes.json').read_text(encoding='utf8'))
rows=[]
for n in range(1,14):
 x=state['changes'][f'V07-{n:02}'];rows.append(f"| V07-{n:02} | {Path(x['files'][0]).name} | Revisione testuale | Come audit storico | {x['change']} | Modifica applicata, confronto e calcoli riesaminati | Applicato |")
text='''---
id: review-pipeline-vol07-14-correzioni-sa01-20261002
type: editorial_review
volume_code: VOL-07
module_code: M-SA01
pipeline_step: 14
status: completed
review_date: 2026-10-02
review_required: true
canonical: true
---

# Revisione editoriale M-SA01 — Correzioni dell'audit integrale

## 1. Sintesi editoriale

Applicate le correzioni V07-01–13 ai cinque capitoli del modulo; applicata anche la parte V07-14 che riguarda gli imperativi di SA01/10. La restante occorrenza in SA02/05 è assegnata al relativo modulo. Preservate le integrazioni INT-05–08, comprese fonti e avvertenze temporali. Il rapporto precedente è conservato nell'archivio; gli audit integrali storici non sono modificati.

## 2. Punti applicati della checklist

Riesame dei punti testuali 1–26 e 28–30 sui passaggi modificati, raccordato alla lettura integrale precedente dei cinque capitoli. Controllati chiarezza, coerenza delle definizioni, copertura effettiva, esempi, calcoli e destinatario. Il punto 27 richiede nuovi PDF. Non è dichiarata una nuova lettura parola per parola di tutto il testo rimasto invariato. Fonti esterne verificate selettivamente per i nuovi claim; nessuna certificazione dell'intero ordinamento sanitario.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+'''
| V07-14 | SA01/10, elenco operativo | Lingua | Lieve | Uniformati definisci, distingui, proponi | Residuo SA02/05 da trattare nel suo modulo | Parziale per il volume |

## 4. Osservazioni per capitolo

Capitolo 04: titolo e apertura descrivono anche fondamenti SSN, LEA, organi e accreditamento. Capitolo 05: esclusione FOIA dei dati sanitari, accesso difensivo di pari rango, termini 7/30 giorni, consenso FSE/dossier, documento informatico e richiesta di integrazione. Capitolo 06: esempio di comunicazione concretamente eseguibile e rubrica con errori critici. Capitolo 09: documenti, ruoli e ciclo di bilancio; ammortamento/sterilizzazione; variazione percentuale corretta. Capitolo 10: AIC/rimborso, dispositivi, centralizzazione, NSO, FEFO e riordino.

Le nuove verifiche didattiche hanno soluzione esplicita. Calcolo costo medio: (516000/27000/20−1)×100 = −4,4444…%; punto di riordino: 100×5+200=700; disponibilità in presenza di quarantena: 680−150=530; ammortamento ipotetico: 100000/5=20000. I dati sono distinti da standard legali o clinici.

## 5. Coerenza globale

Il modulo resta rivolto ai profili amministrativi sanitari. Il rinvio MDR/IVDR va al capitolo SA04/04; la rubrica richiama SA02/10. La teoria nazionale non viene sostituita da istruzioni aziendali e non diventa un protocollo clinico. Passaggio Humanizer e micro-revisione svolti sui delta: frasi con soggetti riconoscibili, esempi circoscritti, nessuna istruzione di pipeline inserita nella prosa pubblica.

## 6. Contenuto da verificare

Audit specialistico step 15 richiesto sui claim nuovi. Il testo GU originario degli artt. 26, 29, 31 e 32 D.Lgs. 118/2011 è stato confrontato con l'applicazione istituzionale 2026 della DGR Veneto 427; Normattiva ha restituito errori tecnici. Occorre completare il controllo del consolidato prima del freeze. La norma temporale sull'accreditamento e gli aggiornamenti LEA delle integrazioni INT mantengono i limiti già documentati nelle loro source.

## 7. Suggerimenti facoltativi

Nessun ampliamento facoltativo necessario per chiudere questa revisione. Le ulteriori correzioni dei moduli SA02–04 sono obbligatorie e restano nel registro del volume.

## 8. Priorità degli interventi

Audit specialistico dei delta, correzione di eventuali residui, nuovo freeze solo dopo verifica, rigenerazione PDF e controllo degli apparati. Il test di packaging rileva due source INT non ancora tracciate da Git: i file esistono con raw e hash; il coordinatore gestisce il packaging condiviso.

## 9. Giudizio di pubblicabilità

Revisione editoriale applicata; modulo e volume non ancora dichiarati pubblicabili. Restano audit specialistico, correzioni degli altri moduli, freeze e nuovi PDF. Il passaggio dello schema automatico del report non equivale a verifica normativa o tipografica.

## 10. Limiti di questa revisione

Copertura: correzioni testuali SA01 richieste dall'audit integrale, con confronto dei passaggi pertinenti. Nessun controllo dei nuovi PDF ancora disponibili, nessuna validazione di procedure aziendali o di bilanci reali. Registro analitico: [[reviews/correzioni-collana-2026-10-02/VOL-07]].
'''
p.write_text(text,encoding='utf8')
matrix=Path('wiki/books/moduli/m-sa01-sanita-amministrativa/planning/02-matrice-copertura-didattica.md')
s=matrix.read_text(encoding='utf8')
s+='''
### Correzioni applicate ai cinque capitoli

V07-01–06: accesso documentale/FOIA, termini documentazione, FSE/dossier, documento informatico (cap. 05); V07-07: titolo e apertura SSN (cap. 04); V07-08–09: comunicazione e rubrica con errori critici (cap. 06); V07-10–11: variazione esatta, documenti/ciclo di bilancio e ammortamento (cap. 09); V07-12–13 e quota V07-14: AIC, classi, NSO, FEFO, riordino e imperativi (cap. 10). Evidenze e limiti nel report step 14 corrente e nel registro correzioni. Copertura dei delta testuali applicata; audit specialistico step 15 e nuovo freeze ancora necessari.
'''
matrix.write_text(s,encoding='utf8')
print('Report 14 archiviato e aggiornato; matrice raccordata.')
