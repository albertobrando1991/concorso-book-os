from pathlib import Path
import re,json
src=Path('wiki/sources/valutazione-e-competenze-digitali-docenti-dlgs-62-2017-om-172-digcompedu.md')
t=src.read_text(encoding='utf8').replace('updated_at: 2026-07-29','updated_at: 2026-10-03')
t=t.replace('D.Lgs. 62/2017, O.M. 172/2020 e DigCompEdu','D.Lgs. 62/2017, O.M. 3/2025 e DigCompEdu')
t=t.replace("L'O.M. 172/2020 e le relative linee guida riguardano la valutazione periodica e finale degli apprendimenti nella scuola primaria.","L’O.M. 172/2020 è il riferimento storico sostituito dall’O.M. 3/2025 per la valutazione periodica e finale degli apprendimenti nella primaria, con decorrenza transitoria dall’ultimo periodo dell’anno scolastico 2024/2025.")
t+='''
## Aggiornamento verificato il 3 ottobre 2026

Letti gli articoli 1–7 dell’O.M. 3 del 9 gennaio 2025 e l’Allegato A nella copia ministeriale ospitata dall’istituto statale Via Luigi Rizzo; il collegamento MIM ha restituito un errore di accesso. La regola transitoria è **ultimo periodo** dell’anno scolastico 2024/2025, non necessariamente secondo quadrimestre in ogni organizzazione scolastica. Da quel periodo cessa l’efficacia dell’O.M. 172/2020. L’art. 3 prevede per ciascuna disciplina, compresa educazione civica, ottimo, distinto, buono, discreto, sufficiente, non sufficiente, correlati alle descrizioni dell’Allegato A. La valutazione in itinere conserva le forme formative coerenti con i criteri collegiali. Art. 4: valutazione correlata al PEI per disabilità e attenta al PDP per DSA. Art. 5: comportamento in decimi nella secondaria di primo grado; voto finale inferiore a sei comporta non ammissione. Non estendere quest’ultima regola alla primaria.

Fonti lette:
- https://www.icvialuigirizzo.edu.it/wp-content/uploads/2025/01/VALUTAZIONE-APPRENDIMENTI-SCUOLA-PRIMARIA-E-COMPORTAMENTO-SCUOLA-SECONDARIA-DI-PRIMO-GRADO2.pdf
- https://www.icvialuigirizzo.edu.it/wp-content/uploads/2025/01/Allegato-A_OM-9-gennaio-2025_n.3-signed-1.pdf
- https://joint-research-centre.ec.europa.eu/scientific-activities/key-competences-lifelong-learning/digcompedu/digcompedu-framework_en

Il JRC distingue sei aree: coinvolgimento professionale, risorse digitali, insegnamento e apprendimento, valutazione, valorizzazione delle potenzialità dei discenti, sviluppo della competenza digitale dei discenti. La prima riguarda anche comunicazione, collaborazione, riflessione e sviluppo professionale docente: non va sostituita dalla sola progettazione didattica.
'''
src.write_text(t,encoding='utf8')
old='valutazione-competenze-digitali-docenti-dlgs-62-2017-om-172-digcompedu'
new='valutazione-e-competenze-digitali-docenti-dlgs-62-2017-om-172-digcompedu'
changed=[]
for base in [Path('wiki/books/moduli/m-ir01-scuola'),Path('wiki/topics')]:
 for p in base.rglob('*.md'):
  t=p.read_text(encoding='utf8')
  if old in t:
   p.write_text(t.replace(old,new),encoding='utf8');changed.append(str(p).replace('\\','/'))
p=next(Path('wiki/books/moduli/m-ir01-scuola/chapters').glob('12-*.md'));t=p.read_text(encoding='utf8')
a=t.index('Il D.Lgs. 62/2017 disciplina');b=t.index('\n\n',a)
t=t[:a]+'''Il D.Lgs. 62/2017 disciplina valutazione e certificazione delle competenze nel primo ciclo e gli esami di Stato. Per gli apprendimenti nella scuola primaria, l’O.M. 3 del 9 gennaio 2025 ha introdotto sei giudizi sintetici, correlati alle descrizioni dei livelli dell’Allegato A: **ottimo, distinto, buono, discreto, sufficiente, non sufficiente**. Il giudizio riguarda ciascuna disciplina, compresa educazione civica. Le scuole declinano i descrittori per disciplina e anno di corso nei criteri del Piano triennale dell’offerta formativa. Non è una conversione automatica del punteggio di una singola prova in giudizio finale.

La decorrenza transitoria è l’ultimo periodo in cui ciascuna scuola ha suddiviso l’anno scolastico 2024/2025; nelle scuole organizzate in quadrimestri, il secondo quadrimestre. Da quel momento l’O.M. 172/2020 cessa di produrre effetti. Va dunque citata solo per ricostruire il precedente sistema, senza proporla come regola operativa corrente.

La valutazione **in itinere** continua a usare forme comprensibili e utili all’apprendimento, coerenti con i criteri collegiali: osservazioni, restituzioni sul compito e indicazioni per migliorarlo. Per l’alunno con disabilità gli obiettivi valutati sono correlati al Piano educativo individualizzato; per i disturbi specifici dell’apprendimento si tiene conto del Piano didattico personalizzato. Diversa è la regola sul **comportamento nella secondaria di primo grado**: l’O.M. 3/2025 prevede il voto in decimi e la non ammissione deliberata dal consiglio di classe quando nello scrutinio finale il voto è inferiore a sei. Non applicare questa previsione alla primaria.''' +t[b:]
a=t.index('Il framework europeo DigCompEdu');b=t.index('\n\n',a)
t=t[:a]+'''Il framework europeo **DigCompEdu**, elaborato dal Joint Research Centre della Commissione europea, descrive 22 competenze organizzate in sei aree:

1. coinvolgimento e valorizzazione professionale: comunicazione, collaborazione, riflessione e formazione continua del docente;
2. risorse digitali: selezione, creazione, gestione e condivisione;
3. insegnamento e apprendimento: uso educativo degli strumenti, guida e collaborazione;
4. valutazione: raccolta e interpretazione delle evidenze, feedback e riprogettazione;
5. valorizzazione delle potenzialità dei discenti: accessibilità, differenziazione e partecipazione;
6. sviluppo della competenza digitale dei discenti: uso critico, creativo e responsabile delle tecnologie.

Il framework non impone una piattaforma e non sostituisce il programma del concorso. La progettazione attraversa più aree; non costituisce una settima area né prende il posto di quella professionale.''' +t[b:]
t=t.replace('La source note sul digitale nel Metodo BANDO propone una regola pratica:', 'Una regola pratica del Metodo BANDO è questa:')
p.write_text(t,encoding='utf8')
batch={
'V06-01':{'change':'Sostituita la presentazione corrente dell’O.M. 172/2020 con O.M. 3/2025, sei giudizi, ultimo periodo 2024/2025, valutazione in itinere e distinto comportamento nella secondaria di primo grado.','files':[str(p).replace('\\','/'),str(src).replace('\\','/')],'evidence':'Confronto artt. 1–7 e Allegato A della copia ministeriale ospitata da istituto statale; rilettura della nuova sezione.','status':'applicato'},
'V06-02':{'change':'Elencate le sei aree DigCompEdu, ripristinata l’area professionale.','files':[str(p).replace('\\','/'),str(src).replace('\\','/')],'evidence':'Pagina canonica JRC DigCompEdu framework letta; corrispondenza aree controllata.','status':'applicato'},
'V06-03':{'change':'Aggiornata la nota preesistente con “e” nello slug, riallineati i riferimenti del modulo e del topic senza duplicare una fonte obsoleta.','files':changed+[str(src).replace('\\','/')],'evidence':'Fonte esistente consolidata con O.M. 3/2025 e JRC; controllo riferimenti dopo le correzioni del modulo.','status':'applicato'}}
Path('artifacts/correzioni-collana-2026-10-02/VOL-06-batch01.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8')
print('Fonte valutazione e capitolo 12 aggiornati; riferimenti riallineati:',len(changed))
