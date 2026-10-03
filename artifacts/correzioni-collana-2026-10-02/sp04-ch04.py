from pathlib import Path
import shutil
p=next(Path('wiki/books/moduli/m-sp04-prefettizia-diplomatica/chapters').glob('04-*.md'));a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp04-04.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=t.replace('Nei primi giorni misura, non tenta','Nei primi giorni misura, non tentare')
t=t.replace('La decisione viene congelata per un ciclo di lavoro, per esempio otto settimane. Cambiare lingua dopo ogni prova negativa impedisce l\'apprendimento. Alla fine del ciclo confronta indicatori e costo. Si cambia soltanto se i dati mostrano un divario strutturale e il tempo residuo consente la transizione.','La diagnosi comparativa deve precedere la scelta nella domanda e lasciare tempo per l’invio. Un ciclo di otto settimane ha senso soltanto se termina prima della scadenza pertinente. Nel bando MAECI 2026 le opzioni sono indicate nella domanda; questa può essere modificata entro il termine, con prevalenza dell’ultima domanda valida. Dopo la scadenza non si cambia lingua per effetto di una decisione didattica personale: occorrerebbe una specifica previsione o comunicazione ufficiale che lo consenta. Nel bando prefettizio si dichiarano analogamente lingua obbligatoria e facoltativa nella domanda. Conserva la ricevuta e controlla che corrisponda alla scelta.')
t=t.replace('La scelta viene riaperta solo davanti a evidenze nuove:', 'Per una futura tornata, o entro i termini in cui la domanda è ancora modificabile, la scelta può essere riesaminata davanti a evidenze nuove:')
t=t.replace('La scelta razionale avviene dopo che le obbligatorie mostrano stabilità','La scelta razionale, da formalizzare entro il termine della domanda, richiede che le obbligatorie mostrino stabilità')
anchor='## N-SP04-08-05'
s=t.index(anchor)
t=t[:s]+'''### Laboratorio originale: comprensione, risposta e dialogo

Il testo seguente è un esercizio didattico originale, non una traccia ministeriale. Si riferisce a un paese immaginario e non descrive una crisi reale. Per la prefettizia, usa il vocabolario nel compito di traduzione; per la diplomatica esegui comprensione e risposta senza dizionario. I tempi ridotti servono alla diagnosi e non sostituiscono le durate ufficiali.

**Testo inglese**

> The government of the fictional country of Lydora is considering a grant programme for small firms that depend on imported equipment. A recent disruption has increased delivery times, although prices have not risen equally across sectors. The proposed grants would cover part of the cost of replacing unreliable suppliers. Supporters argue that the measure would protect jobs and reduce exposure to future shocks. Critics warn that a poorly targeted scheme could subsidise changes that firms would have made anyway.
>
> Before deciding, the ministry plans to compare applications from firms facing similar delays. It will also publish clear eligibility rules and require recipients to report how the funds were used. These safeguards may improve accountability, but they do not prove that the grants will be effective. A useful evaluation would distinguish spending from results, compare outcomes with a credible alternative, and disclose the limits of the available evidence. If delays fall after the programme starts, that change alone will not establish that the grants caused the improvement.

**Compiti.** In dieci minuti identifica proposta, due ragioni favorevoli, rischio e limite della valutazione. Per la traduzione, rendi in italiano il secondo paragrafo in venti minuti, mantenendo condizioni e gradi di certezza. Per la risposta, scrivi in inglese, in venticinque minuti, circa 150 parole su: “Which information should the ministry collect before extending the programme, and why?” La lunghezza è un vincolo dell’esercizio, non del concorso.

**Soluzione della comprensione.** La proposta sostiene il cambio dei fornitori con contributi parziali. I sostenitori richiamano tutela dell’occupazione e riduzione dell’esposizione agli shock. Il rischio è finanziare cambiamenti che sarebbero avvenuti comunque. La diminuzione dei ritardi dopo l’avvio non dimostra da sola un effetto causale: potrebbe dipendere da altri fattori. “May improve” esprime possibilità; tradurlo con “garantiscono” aggiungerebbe una certezza assente.

**Resa italiana possibile.** “Prima di decidere, il ministero intende confrontare le domande di imprese che affrontano ritardi simili. Pubblicherà inoltre regole chiare di ammissibilità e richiederà ai beneficiari di rendicontare l’impiego dei fondi. Queste garanzie possono migliorare la responsabilità nella gestione, ma non dimostrano che i contributi saranno efficaci. Una valutazione utile distinguerebbe la spesa dai risultati, confronterebbe gli esiti con un’alternativa credibile e dichiarerebbe i limiti delle prove disponibili. Se i ritardi diminuissero dopo l’avvio del programma, questo cambiamento, da solo, non dimostrerebbe che i contributi hanno causato il miglioramento.” Sono possibili rese diverse se conservano significato, registro e cautele.

**Risposta inglese possibile.**

> Before extending the programme, the ministry should collect comparable information on delivery delays, employment and supplier changes before and after the grants. It should also record which firms applied, which received support and why others were rejected. This would help identify differences between recipients and other firms, although comparison alone would not remove every source of bias.
>
> The evaluation should examine additional results, rather than treating money spent as evidence of success. For example, firms may have planned to replace suppliers without public support. Information on those plans and on wider market conditions would therefore matter. A fall in delays across the whole economy would weaken a claim that the programme alone caused the improvement. Finally, the ministry should report administrative costs and uncertainty alongside benefits. Expansion would be easier to justify if the evidence showed a plausible contribution to resilience at a reasonable cost, with clear limits and safeguards.

**Correzione guidata.** L’apertura risponde alla domanda con dati da raccogliere. Il secondo periodo aggiunge il criterio di selezione, necessario per capire se il confronto sia attendibile. La seconda parte distingue spesa, risultati e contributo causale; la conclusione propone una decisione condizionata, senza inventare dati. “Evidence” è usato come nome non numerabile; “would weaken” conserva la forma ipotetica. Un difetto possibile da evitare è “The grants prove the policy is successful because delays decreased”: confonde successione temporale e causalità, già escluse dal testo.

**Dialogo modello.**

— Examiner: “Would you stop the programme if the first report showed no improvement?”

— Candidate: “Not automatically. I would first check the reporting period, the quality of the data and whether the expected effects could already be observed. However, I would not use those checks to postpone a decision indefinitely.”

— Examiner: “What would you tell firms asking for immediate certainty?”

— Candidate: “I would explain which rules are already fixed, when the review will take place and which evidence could change the decision. Predictable procedures are possible even when the outcome is uncertain.”

— Examiner: “Are you saying that accountability and effectiveness are the same?”

— Candidate: “No. Accountability concerns explaining and justifying the use of public funds. Effectiveness concerns whether the programme achieves its intended results. Clear reporting supports evaluation, but it does not by itself demonstrate success.”

**Retest autonomo.** Rispondi alla domanda inversa: “What evidence would justify narrowing the programme?” Registra novanta secondi, poi controlla se hai distinto criteri, dati e decisione. Una risposta valida può proporre di limitare il sostegno ai settori con ritardi documentati e minore capacità di adattamento, verificando che la selezione sia trasparente; non può affermare che quei settori siano già identificati dal testo. Nella correzione segna pertinenza, accuratezza, struttura, lingua e interazione da 0 a 2: il totale di allenamento non predice il voto ufficiale.

'''+t[s:]
p.write_text(t,encoding='utf8')
