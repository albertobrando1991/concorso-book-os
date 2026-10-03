from pathlib import Path
import re,json,shutil,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
p=next(B.glob('03-*.md'));t=p.read_text('utf-8');b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
before=hashlib.sha256(p.read_bytes()).hexdigest()
addition='''### Mappa degli uffici: funzione, composizione e territorio

La competenza risponde a una domanda diversa dall'organizzazione: quale giudice può trattare quel procedimento? Occorre combinare materia, valore quando rileva, territorio e grado. Un ufficio può avere più sezioni; una sezione non è necessariamente un ufficio autonomo e una sede amministrativa non determina da sola la competenza processuale.

| Ufficio giudicante | Composizione e funzione essenziale | Territorio e raccordo |
|---|---|---|
| Giudice di pace | Giudice onorario monocratico; controversie civili e reati attribuiti dalla legge. | Ambito dell'ufficio stabilito dalle norme sulla geografia giudiziaria; non ogni comune ha un proprio giudice. |
| Tribunale ordinario | Giudice monocratico oppure collegio di tre nei casi previsti; funzioni civili e penali. | Circondario; comprende più comuni secondo le tabelle, senza equivalenza necessaria con la provincia. |
| Corte d'appello | Collegio ordinario di tre; giudizio di secondo grado nei casi previsti. | Distretto, comprendente più circondari; non coincide necessariamente con una regione. |
| Corte di cassazione | Giudizio di legittimità e funzione di uniforme interpretazione della legge; non nuovo libero giudizio sul fatto. | Sede a Roma e ambito nazionale. |
| Corte d'assise | Due magistrati togati e sei giudici popolari; reati attribuiti dall'art. 5 c.p.p. | Circolo d'assise; non confondere composizione mista con collegio ordinario del tribunale. |

L'appello contro una decisione del giudice di pace, quando ammesso, non va automaticamente alla corte d'appello: il percorso delle impugnazioni dipende dalla legge processuale. Analogamente, l'assise non tratta ogni reato solo perché percepito come grave: occorre la competenza prevista dall'art. 5 c.p.p.

| Ufficio specializzato | Distinzione da ricordare |
|---|---|
| Tribunale per i minorenni | Nel quadro ancora operativo al 3 ottobre 2026, competenze specialistiche civili, penali e amministrative. Il collegio ordinario comprende due togati e due onorari esperti; il GUP minorile un togato e due onorari; il GIP minorile è monocratico. |
| Magistrato di sorveglianza | Organo monocratico con compiti propri nell'esecuzione penale, nei controlli e nei benefici attribuiti dalla legge. |
| Tribunale di sorveglianza | Organo collegiale distrettuale: due magistrati togati e due esperti; decide sulle materie assegnate, comprese misure alternative e determinati reclami. |

Il futuro tribunale per le persone, per i minorenni e per le famiglie non va sovrapposto agli uffici già operativi: l'efficacia della riforma organizzativa è stata ulteriormente differita dal DL 100/2026, convertito dalla L. 145/2026. Inoltre, l'esistenza del tribunale per i minorenni non significa che qualunque causa riguardante un minore appartenga a esso: la ripartizione con il tribunale ordinario dipende dalla materia e dalle regole processuali.

### GIP, GUP e pubblico ministero

Il **giudice per le indagini preliminari (GIP)** interviene nella fase delle indagini nei casi previsti dal codice: controlla richieste incidenti sui diritti, adotta provvedimenti cautelari quando ne ricorrono i presupposti, decide sulle richieste di archiviazione e svolge altre funzioni attribuite dalla legge. Non dirige le indagini al posto del pubblico ministero. Il **giudice dell'udienza preliminare (GUP)** svolge il controllo previsto nella relativa fase e può pronunciare sentenza di non luogo a procedere oppure disporre il giudizio, oltre alle definizioni consentite dai riti applicabili. GIP e GUP sono funzioni giudicanti, non due denominazioni della Procura.

Gli uffici requirenti comprendono la Procura della Repubblica presso il tribunale e le procure generali presso corte d'appello e Cassazione, oltre all'ufficio minorile nel quadro vigente. Il PM esercita l'azione penale e le altre attribuzioni stabilite dalla legge, anche in ambito civile; non è il difensore privato della persona offesa. La Procura ha propri registri e segreterie: non si identifica con la cancelleria del giudice solo perché i due uffici si trovano nello stesso edificio.

**Caso risolto.** Una segreteria riceve una richiesta di archiviazione predisposta dal PM. Qualificare il documento come «decisione di archiviazione della Procura» sarebbe errato: è una richiesta da sottoporre al giudice competente. L'ufficio deve distinguere registro e fascicolo della Procura, trasmissione della richiesta e successivo provvedimento giudiziale. Se invece deve preparare materiali per l'udienza preliminare, individua il GUP e la relativa cancelleria, senza attribuire al personale amministrativo la valutazione sull'accusa. Il passaggio corretto dipende dunque da autore, fase e funzione dell'atto.

'''
t=t.replace('### Merito, legittimità e sorveglianza',addition+'### Merito, legittimità e sorveglianza',1)
start=t.index('### Presidenza, capo ufficio e dirigenza amministrativa');end=t.index('### Cancelleria e segreteria',start)
t=t[:start]+'''### Capo dell'ufficio e dirigente amministrativo

Il D.Lgs. 240/2006 distingue responsabilità che devono coordinarsi. Il magistrato capo ha titolarità e rappresentanza dell'ufficio nei rapporti istituzionali, adotta i provvedimenti necessari per l'organizzazione dell'attività giudiziaria e gestisce il personale di magistratura nell'ambito delle proprie attribuzioni. Il dirigente amministrativo è responsabile del personale amministrativo, in coerenza con gli indirizzi del capo e con il programma annuale.

Le risorse finanziarie e strumentali sono assegnate dall'amministrazione centrale. Il dirigente amministrativo può adottare atti che impegnano l'amministrazione verso l'esterno, anche con spesa, **nei limiti dell'assegnazione**; non dispone di un'autorizzazione illimitata a impegnare fondi. La distinzione non crea due uffici indipendenti: serve a rendere riconoscibili responsabilità e raccordi.

| Passaggio | Regola del D.Lgs. 240/2006 |
|---|---|
| Programmazione | Capo dell'ufficio e dirigente amministrativo redigono insieme il programma annuale, indicando priorità e risorse disponibili. |
| Termine | Entro trenta giorni dalle determinazioni centrali conseguenti alla direttiva ministeriale e comunque non oltre il 15 febbraio. |
| Modifica | Durante l'anno, su concorde iniziativa dei due responsabili per sopravvenute esigenze dell'ufficio. |
| Inerzia | Il Ministro fissa un termine perentorio; se l'inerzia persiste interviene secondo il meccanismo dell'art. 4, comma 2, per gli adempimenti urgenti. |

**Applicazione.** Per recuperare un arretrato occorrono più udienze, diversa distribuzione del personale amministrativo e nuove dotazioni. Il capo organizza l'attività giudiziaria e il lavoro dei magistrati; il dirigente gestisce personale amministrativo e risorse nei limiti assegnati. I due raccordano obiettivi, priorità e mezzi nel programma. Nessuno può usare la programmazione per imporre il contenuto delle decisioni del giudice. Il progetto UPP si inserisce in questo quadro, con la specifica disciplina dell'art. 3 D.Lgs. 151/2022.

''' +t[end:]
t=re.sub(r'### Quiz commentato\n.*?(?=### Checklist di ripasso)', '''### Quiz commentato

1. **Quale abbinamento tra ufficio e territorio è corretto?**
   - A. Tribunale: distretto; corte d'appello: circondario.
   - B. Tribunale: circondario; corte d'appello: distretto.
   - C. Tribunale: comune; corte d'appello: provincia in ogni caso.
   **Risposta corretta: B.** Sono ambiti giudiziari definiti dalla legge e dalle tabelle; non coincidono necessariamente con circoscrizioni amministrative.

2. **Quale composizione distingue la corte d'assise dal tribunale collegiale ordinario?**
   - A. Tre togati anziché un giudice di pace.
   - B. Due togati e due esperti anziché tre togati.
   - C. Due togati e sei popolari anziché tre togati.
   **Risposta corretta: C.** Due togati e due esperti è la composizione del tribunale di sorveglianza; la corte d'assise comprende sei giudici popolari.

3. **Chi dirige le indagini preliminari, distinguendosi dal giudice che interviene sulle richieste previste dal codice?**
   - A. Il pubblico ministero.
   - B. Il GUP in ogni procedimento.
   - C. Il dirigente amministrativo della Procura.
   **Risposta corretta: A.** Il GIP svolge funzioni giudicanti di controllo e decisione nei casi previsti; non si sostituisce alla funzione requirente.

4. **Chi redige il programma annuale ex art. 4 D.Lgs. 240/2006?**
   - A. Il solo capo dell'ufficio, senza il dirigente amministrativo.
   - B. Il solo dirigente amministrativo, dopo la conclusione dell'anno.
   - C. Il capo dell'ufficio e il dirigente amministrativo, con priorità e risorse disponibili.
   **Risposta corretta: C.** È un atto di programmazione congiunta, entro il termine previsto e comunque non oltre il 15 febbraio; anche le modifiche richiedono concorde iniziativa.

5. **Il dirigente amministrativo può impegnare l'amministrazione verso l'esterno con atti di spesa?**
   - A. Sì, nei limiti del provvedimento di assegnazione delle risorse.
   - B. No, perché ogni atto di spesa è una decisione giurisdizionale.
   - C. Sì, senza limiti se il fabbisogno è indicato nel programma.
   **Risposta corretta: A.** Il programma non sostituisce l'assegnazione delle risorse. Amministrazione della spesa e decisione processuale restano distinte.

6. **Quale affermazione sulla sorveglianza è corretta?**
   - A. È una sezione della Procura che decide le richieste del giudice.
   - B. Comprende un organo monocratico e un tribunale collegiale con attribuzioni proprie.
   - C. È il controllo ministeriale sul contenuto delle sentenze civili.
   **Risposta corretta: B.** Magistrato e tribunale di sorveglianza operano nell'esecuzione penale secondo competenze distinte; il tribunale non è sinonimo dell'ufficio monocratico.

''',t,flags=re.S)
s='vol-04-organizzazione-upp-verifica-2026-10-03'
t=t.replace('source_refs: [',f'source_refs: [\n  "sources/{s}.md",',1).replace('last_compiled_from: [',f'last_compiled_from: [\n  "wiki/sources/{s}.md",',1)
t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
p.write_text(t,'utf-8')
(A/'VOL-04-uffici-delta.json').write_text(json.dumps({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2),'utf-8')
print('Capitolo03: mappa uffici, doppia dirigenza, caso e sei quiz applicati')
