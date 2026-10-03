from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico'); changes=[]
def load(n):
 p=next((base/'chapters').glob(f'{n:02}-*.md'));return p,p.read_text(encoding='utf8')
def before(s,anchor,body):
 assert s.count(anchor)==1,anchor
 return s.replace(anchor,body.strip()+'\n\n'+anchor)
def save(p,s):
 p.write_text(s,encoding='utf8');changes.append(p.as_posix())
p,s=load(1)
s=re.sub(r'Affidamento, procurement, RUP e PNRR avanzati ricadono.*?materia coperta\.', 'Affidamento, RUP e gestione dei fondi sono approfonditi nel volume 9, Appalti, PNRR e fondi UE: capitoli 3–6 per soggetti, programmazione, procedure e gara; capitoli 10–12 per fondi, progetto finanziato e rendicontazione. Il presente volume mantiene il percorso tecnico necessario a progettazione, direzione lavori e collaudo.',s)
save(p,s)
p,s=load(2)
s=before(s,'## N-TR03-02-07', '''### Tre funzioni della conferenza

L'art. 14 della L. 241/1990 distingue la funzione della conferenza dalle sue modalità organizzative. «Istruttoria» e «decisoria» indicano a che cosa serve; «semplificata» e «simultanea» indicano come si svolge.

La **conferenza istruttoria** è facoltativa: l'amministrazione procedente può convocarla per esaminare insieme gli interessi pubblici di un procedimento o di procedimenti connessi. Per esempio, prima di definire un intervento su una scuola, ufficio tecnico e altre amministrazioni coinvolte confrontano accessi, rete viaria e servizi. Il confronto prepara l'istruttoria; non sostituisce automaticamente gli assensi necessari.

La **conferenza decisoria** è obbligatoria quando la conclusione positiva richiede più pareri, intese, nulla osta o altri assensi di amministrazioni diverse, inclusi gestori di beni o servizi pubblici. Se un progetto richiede due distinti assensi esterni, l'amministrazione procedente organizza l'acquisizione secondo gli artt. 14 e seguenti; la determinazione conclusiva produce gli effetti previsti dalla legge. Non basta chiamare una riunione «conferenza» per attribuirle quegli effetti.

La **conferenza preliminare** può essere indetta, su motivata richiesta corredata da studio di fattibilità, per progetti particolarmente complessi o insediamenti produttivi. Serve a conoscere prima della domanda completa le condizioni alle quali ottenere gli assensi. Un'impresa che prospetta un insediamento complesso può così orientare il progetto. Le condizioni espresse non sono un'autorizzazione a costruire; nel procedimento successivo possono essere modificate motivatamente in presenza dei significativi elementi previsti dalla norma.

**Verifica rapida.** Per confrontare interessi prima della decisione: istruttoria. Per acquisire plurimi assensi necessari alla conclusione: decisoria. Per conoscere preventivamente le condizioni di un progetto complesso: preliminare. La scelta dipende dal presupposto, non dalla preferenza per una riunione più breve.''')
save(p,s)
p,s=load(3)
s=before(s,'## N-TR03-03-02', '''### Tre vincoli nel piano

Un corpo rigido libero nel piano ha tre gradi di libertà: traslazione orizzontale u_x, traslazione verticale u_y e rotazione θ. Un vincolo ideale impedisce alcuni di questi movimenti e può trasmettere le reazioni corrispondenti.

| Vincolo ideale | Movimento impedito | Reazioni incognite |
| --- | --- | --- |
| Carrello su piano orizzontale | u_y | R_y |
| Cerniera fissa | u_x e u_y | R_x e R_y |
| Incastro | u_x, u_y e θ | R_x, R_y e momento M |

Il carrello lascia libera la traslazione lungo il piano di appoggio e la rotazione; se il piano è inclinato, la sua reazione è normale a quel piano. La cerniera consente la rotazione e non trasmette momento. L'incastro impedisce anche la rotazione. Queste sono idealizzazioni: il collegamento reale deve giustificare il modello scelto.

![Vincoli piani: spostamenti impediti e reazioni](../assets/correzioni-2026-10/vincoli-piani.png)

Tre reazioni incognite non garantiscono da sole stabilità e isostaticità: conta anche la disposizione dei vincoli. Reazioni tutte parallele, per esempio, possono lasciare un movimento non contrastato. Si controllano prima i movimenti possibili, poi il numero delle incognite.''')
s=before(s,'## N-TR03-03-04', '''### Esempio svolto: trave con carico uniforme

Considera una trave rettilinea orizzontale di luce L = 4 m, cerniera in A e carrello in B. Il carico verticale uniforme è q = 10 kN/m su tutta la luce. Il modello è piano, statico, con piccoli spostamenti; q rappresenta il carico complessivo assegnato, senza aggiungere un peso proprio non fornito. Non stiamo verificando una sezione reale né applicando coefficienti NTC.

**1. Corpo libero.** Sostituisci i vincoli con R_Ax, R_Ay e R_By. Il carico distribuito ha risultante qL = 40 kN, applicata a metà luce, a 2 m da A. Questa sostituzione serve all'equilibrio globale; per una sezione interna si considera solo il carico che agisce sulla porzione isolata.

**2. Equilibrio.** Assumi forze verso destra e verso l'alto positive, momenti esterni antiorari positivi:

- ΣF_x = 0: R_Ax = 0;
- ΣM_A = 0: 4R_By − 40 × 2 = 0, dunque R_By = 20 kN;
- ΣF_y = 0: R_Ay + 20 − 40 = 0, dunque R_Ay = 20 kN.

Controllo: la somma delle reazioni verticali è 40 kN, uguale al carico totale; per simmetria le due reazioni sono uguali.

**3. Sezione a distanza x da A.** Per 0 < x < 4 m, il taglio positivo è definito come risultante algebrica delle forze verticali a sinistra della sezione: V(x) = R_Ay − qx = 20 − 10x kN. Nel corpo libero del tronco sinistro, la corrispondente azione interna positiva sulla faccia di taglio è diretta verso il basso. Il momento positivo tende le fibre inferiori: M(x) = R_Ay x − qx²/2 = 20x − 5x² kN·m. Il normale è nullo.

| x in m | V in kN | M in kN·m |
| --- | --- | --- |
| 0⁺ | +20 | 0 |
| 1 | +10 | 15 |
| 2 | 0 | 20 |
| 3 | −10 | 15 |
| 4⁻ | −20 | 0 |

Il taglio scende linearmente e il momento è parabolico. Poiché dM/dx = V, il massimo del momento è dove V si annulla: x = 2 m, M_max = qL²/8 = 20 kN·m. In corrispondenza di B la reazione produce il salto del taglio da −20 a zero. Il momento è nullo ai due appoggi, coerentemente con i vincoli ideali.

![Trave di 4 m: carico, reazioni, taglio e momento](../assets/correzioni-2026-10/trave-carico-taglio-momento.png)

Nella figura i valori positivi dei diagrammi sono disegnati sopra l'asse. È una convenzione grafica dichiarata, distinta dal significato fisico del momento positivo. **Controllo autonomo:** raddoppiando q con L invariata, reazioni, taglio e momento raddoppiano; raddoppiando L con q invariato, le reazioni raddoppiano e il momento massimo quadruplica. Confondere kN con kN·m rende impossibile questo controllo dimensionale.''')
save(p,s)
p,s=load(4)
s=before(s,'## N-TR03-04-03', '''### Valori e relazione da usare

Il §2.4 delle NTC 2018 distingue vita nominale e classe d'uso. I valori minimi della vita nominale V_N sono 10 anni per costruzioni temporanee e provvisorie, 50 per prestazioni ordinarie e 100 per prestazioni elevate. «Temporanea» non significa semplicemente smontabile e riutilizzabile. La fase di costruzione ha inoltre regole proprie.

| Classe | Criterio essenziale | Coefficiente C_U |
| --- | --- | --- |
| I | Presenza occasionale di persone, edifici agricoli | 0,7 |
| II | Normali affollamenti, assenza di funzioni essenziali e contenuti pericolosi | 1,0 |
| III | Affollamenti significativi o rilevanti conseguenze ambientali e di interruzione | 1,5 |
| IV | Funzioni pubbliche o strategiche importanti, anche per la protezione civile | 2,0 |

La tabella è una sintesi: il §2.4.2 specifica anche reti, ponti, industrie e dighe. Non tutte le opere pubbliche sono automaticamente strategiche. La funzione concreta e gli atti che la qualificano sostengono la scelta.

Il periodo di riferimento sismico si calcola con **V_R = V_N × C_U**. Esempio didattico: per un edificio con V_N = 50 anni e classe III assegnata dalla traccia, V_R = 50 × 1,5 = 75 anni. A parità di vita nominale, una costruzione in classe IV ha V_R = 100 anni. Nessuno dei due risultati indica quando l'edificio dovrà essere demolito.''')
s=before(s,'## N-TR03-04-04', '''### Stati sismici e combinazioni essenziali

Per il sisma, gli stati di esercizio sono **SLO**, operatività, e **SLD**, danno; quelli ultimi sono **SLV**, salvaguardia della vita, e **SLC**, prevenzione del collasso. La progressione ammette livelli di danno differenti. «Salvaguardia della vita» non significa edificio immediatamente utilizzabile dopo l'evento.

Nel §2.5.3, G₁ indica permanenti strutturali, G₂ permanenti non strutturali, P la precompressione, Q_k le azioni variabili caratteristiche, E il sisma. γ sono coefficienti parziali; ψ riducono le azioni variabili secondo concomitanza e durata. Q_k1 è l'azione variabile principale della combinazione: se sono possibili più azioni principali, si esaminano le alternative pertinenti.

- **Fondamentale, generalmente SLU:** γ_G1 G₁ + γ_G2 G₂ + γ_P P + γ_Q1 Q_k1 + Σ γ_Qj ψ_0j Q_kj, con j ≥ 2.
- **Caratteristica o rara, generalmente SLE irreversibili:** G₁ + G₂ + P + Q_k1 + Σ ψ_0j Q_kj, con j ≥ 2.
- **Frequente, generalmente SLE reversibili:** G₁ + G₂ + P + ψ_11 Q_k1 + Σ ψ_2j Q_kj, con j ≥ 2.
- **Quasi permanente, effetti a lungo termine:** G₁ + G₂ + P + Σ ψ_2j Q_kj, su tutte le variabili pertinenti.
- **Sismica:** E + G₁ + G₂ + P + Σ ψ_2j Q_kj.

Per azioni eccezionali si usa la specifica combinazione con A_d. I segni «+» significano «combinato con»; direzione dell'azione, effetti favorevoli/sfavorevoli e regole del materiale restano da considerare. I coefficienti numerici si scelgono nelle tabelle NTC pertinenti, non per analogia con un altro edificio.

**Esercizio.** Una traccia assegna, per una combinazione quasi permanente senza precompressione, G₁ = 100 kN, G₂ = 20 kN, una sola Q_k = 50 kN e ψ₂ = 0,3. Il carico combinato è 100 + 20 + 0,3 × 50 = **135 kN**, non 170 kN. Il coefficiente è un dato dell'esercizio; non è universale per ogni destinazione d'uso.''')
s=before(s,'## N-TR03-04-08', '''### Qualificare l'intervento sull'esistente

Il §8.4 NTC distingue tre categorie in base agli effetti sulla struttura, non al costo dell'opera.

**Riparazione o intervento locale.** Riguarda singole parti o elementi; non modifica sostanzialmente il comportamento globale e non riduce la sicurezza preesistente. Può ripristinare un elemento danneggiato, migliorarne resistenza o duttilità, impedire un meccanismo locale. Esempio: riparazione di una porzione danneggiata di solaio, con dimostrazione che rigidezza, carichi e interazioni non alterano la risposta complessiva. La valutazione può concentrarsi sulle parti coinvolte e interagenti, motivando il confine.

**Miglioramento.** Aumenta la sicurezza preesistente senza dover raggiungere necessariamente i livelli dell'adeguamento. La valutazione interessa la struttura nel suo insieme e tutte le parti il cui comportamento può cambiare. Esempio: un insieme di rinforzi distribuiti che riduce la vulnerabilità di un edificio, senza attivare i presupposti obbligatori dell'adeguamento. Per l'azione sismica, salvo specificità dei beni culturali, le classi III scolastiche e IV devono raggiungere ζ_E almeno 0,6; per classe II e restanti III l'incremento deve essere almeno 0,1. ζ_E esprime il rapporto tra azione sismica massima sopportabile e quella di una nuova costruzione.

**Adeguamento.** Raggiunge i livelli prescritti dal §8.4.3 ed è obbligatorio, in sintesi, quando si sopraeleva; si amplia con opere strutturalmente connesse che alterano significativamente la risposta; si cambia uso aumentando oltre il 10% i carichi globali verticali in fondazione, calcolati come prescritto; si trasforma il sistema strutturale nelle condizioni della norma; oppure si passa alla classe III a uso scolastico o alla IV. Esempio: una sopraelevazione richiede progetto e verifiche dell'intera costruzione, non soltanto del piano aggiunto. Nei casi di sopraelevazione, ampliamento significativo e trasformazione strutturale ζ_E deve essere almeno 1; per i cambi d'uso/carico o classe indicati può essere almeno 0,8. L'eccezione per cordoli sommitali o modifiche della copertura senza nuova superficie abitabile non rende libera qualunque sopraelevazione.

Gli interventi di miglioramento e adeguamento sono sottoposti a collaudo statico; per quelli locali rimangono progettazione, verifiche e adempimenti dovuti nel loro specifico regime. Escludere interventi in fondazione richiede la motivazione del progettista secondo le NTC.

**Nuovo ed esistente.** Il §8.3 consente la valutazione di sicurezza e il progetto di intervento sull'esistente con riferimento ai soli SLU; per classe IV richiede anche gli SLE indicati dal §7.3.6, ammettendo livelli prestazionali ridotti. Questa previsione non va trasferita alla progettazione ordinaria delle nuove costruzioni e non elimina esigenze di funzionalità o cautele nell'uso.''')
s=s.replace('No. Deve soddisfare anche gli stati limite di esercizio e gli altri requisiti pertinenti. Una struttura può essere lontana dal collasso ma risultare eccessivamente deformabile, fessurata, vibrante o non funzionale.', 'Per una nuova costruzione, no: occorrono anche le verifiche di esercizio e gli altri requisiti pertinenti. Una struttura può essere resistente ma troppo deformabile, vibrante o non funzionale. Per la valutazione delle esistenti va invece applicato il campo del §8.3 NTC: riferimento ai soli SLU ammesso, con la previsione specifica degli SLE per classe IV spiegata nel nucleo precedente.')
save(p,s)
p,s=load(5)
s=before(s,'## N-TR03-05-04', '''### Zone A–F e standard nazionali

Il D.M. 1444/1968 usa zone territoriali omogenee. **A**: agglomerati storici, artistici o di particolare pregio e aree integranti; **B**: parti edificate diverse da A, con i requisiti di copertura e densità del decreto; **C**: nuovi complessi insediativi in aree inedificate o sotto i limiti della B; **D**: nuovi insediamenti industriali e assimilati; **E**: usi agricoli, salvo frazionamenti che richiedano insediamenti da C; **F**: attrezzature e impianti di interesse generale. Per la B parzialmente edificata servono superficie coperta almeno 12,5% della fondiaria e densità territoriale superiore a 1,5 m³/m². I nomi degli ambiti regionali possono differire: occorre ricondurli alla disciplina applicabile, senza equipararli per assonanza.

L'art. 3 stabilisce il riferimento residenziale generale di **18 m² per abitante**, insediato o da insediare, escluse le sedi viarie. La ripartizione ordinaria è:

| Dotazione | m² per abitante |
| --- | --- |
| Istruzione | 4,5 |
| Attrezzature di interesse comune | 2 |
| Verde attrezzato, gioco e sport | 9 |
| Parcheggi pubblici | 2,5 |

Non è un valore indistinto per ogni zona. L'art. 4 prevede articolazioni: nelle **A**, se è dimostrata l'impossibilità di reperire aree idonee, il Comune deve spiegare come soddisfare altrimenti i fabbisogni; nelle **B**, alle condizioni previste, si cercano aree adiacenti o accessibili. Le aree per standard nelle A/B sono computate in misura doppia dell'effettiva. Nelle **C** il minimo generale si applica integralmente, ma nei comuni con popolazione prevista non superiore a 10.000 abitanti è 12 m², di cui 4 scolastici; il decreto contempla anche l'ipotesi dei nuovi complessi a bassa densità nei comuni maggiori. Per particolari rapporti visuali con connotati naturali o storico-artistici il verde sale a 15 m², con l'eccezione prevista per le aree contigue a porti di interesse nazionale.

Nelle **E** sono richiesti 6 m² per abitante, complessivamente per istruzione e interesse comune. Per le attrezzature generali delle **F**, quando necessarie, il riferimento alla popolazione servita è almeno 1,5 m² per istruzione superiore all'obbligo (università escluse), 1 per sanità/ospedali e 15 per parchi urbani e territoriali. Questi valori non vanno sommati automaticamente ai 18 senza identificare funzione e popolazione di riferimento.

L'art. 5 usa altre basi: per nuovi insediamenti industriali in D, almeno il **10% della superficie destinata all'insediamento** per gli spazi indicati, escluse strade; per nuovi insediamenti commerciali/direzionali, almeno **80 m² ogni 100 m² di superficie lorda di pavimento**, almeno metà a parcheggi. Nelle A/B quest'ultima quantità è dimezzabile con le attrezzature integrative previste. Parcheggi pertinenziali e parcheggi pubblici da standard sono distinti.

**Caso numerico.** La traccia assegna 400 abitanti in una nuova zona C di un Comune con popolazione prevista di 30.000 abitanti, esclude le ipotesi speciali dell'art. 4 e applica la ripartizione ordinaria. Occorrono 400 × 18 = **7.200 m²**: 1.800 istruzione, 800 interesse comune, 3.600 verde e 1.000 parcheggi. Una strada di 900 m² non riduce queste quantità. Se il progetto offre soltanto 6.800 m² utili, mancano 400 m²; bisogna anche controllare ciascuna destinazione, perché il totale non sana una dotazione funzionale insufficiente.

La legge regionale, il piano e le deroghe ammesse vanno controllati dopo avere individuato questo quadro. Il calcolo dell'esercizio non autorizza a convertire liberamente aree pubbliche in monetizzazione.''')
s=before(s,'### Vincoli paesaggistici e di settore', '''Il vincolo preordinato all'esproprio dell'art. 9 D.P.R. 327/2001 dura **cinque anni** dall'efficacia dell'atto che lo appone. Entro tale termine deve intervenire il provvedimento comportante la dichiarazione di pubblica utilità. Se manca, il vincolo decade e si applica la disciplina richiamata dall'art. 9 del testo unico edilizia; non nasce automaticamente una destinazione liberamente edificabile.

La reiterazione richiede motivazione e rinnovo del procedimento, tenendo conto degli standard; l'art. 39 prevede indennità commisurata al danno effettivamente prodotto. Esempio: un vincolo efficace dal 15 giugno 2021 senza dichiarazione di pubblica utilità nel quinquennio non può essere trattato come ancora efficace nell'ottobre 2026. L'ufficio verifica atti e decorrenze e, se persiste l'interesse, istruisce la reiterazione. Non confondere questo termine con quello della dichiarazione di pubblica utilità o con la durata di un vincolo conformativo.''')
save(p,s)
p,s=load(6)
s=before(s,'## N-TR03-06-03', '''### Le categorie dell'art. 3, con un esempio

**Manutenzione ordinaria:** riparare, rinnovare o sostituire finiture e mantenere efficienti impianti esistenti; per esempio rifare una tinteggiatura senza altre trasformazioni. **Manutenzione straordinaria:** rinnovare o sostituire parti anche strutturali e integrare servizi, nei limiti di volumetria e destinazione d'uso della norma; un frazionamento può rientrarvi se rispetta i relativi presupposti. **Restauro e risanamento conservativo:** insieme sistematico di opere che conserva l'organismo e ne assicura la funzionalità rispettandone elementi tipologici, formali e strutturali; per esempio consolidamento e rinnovo compatibile di parti degradate.

**Ristrutturazione edilizia:** trasformazione sistematica che può produrre un organismo in tutto o in parte diverso. Comprende le ipotesi di demolizione/ricostruzione definite dalla norma, con limiti più restrittivi per immobili tutelati e ambiti storici. **Nuova costruzione:** trasformazione edilizia o urbanistica fuori dalle categorie precedenti, comprendente le ipotesi specifiche elencate dall'articolo. **Ristrutturazione urbanistica:** sostituzione del tessuto esistente mediante interventi sistematici che possono modificare lotti, isolati e rete stradale.

La categoria descrive l'intervento; il regime disciplina come realizzarlo. Una manutenzione straordinaria strutturale non segue la stessa procedura di un intervento interno senza parti strutturali. La denominazione usata dal privato non vincola la qualificazione dell'ufficio.''')
s=before(s,'### Permesso di costruire', '''Nel quadro nazionale, la CILA dell'art. 6-bis copre gli interventi residuali rispetto agli artt. 6, 10 e 22; il tecnico assevera, tra l'altro, il mancato interessamento delle parti strutturali. La SCIA dell'art. 22 comprende manutenzione straordinaria sulle strutture o sui prospetti, restauro strutturale e ristrutturazione diversa da quella dell'art. 10, comma 1, lett. c.

| Regime | Avvio e controllo essenziale |
| --- | --- |
| Edilizia libera, art. 6 | Senza titolo edilizio nei casi elencati; restano norme e assensi di settore |
| CILA, art. 6-bis | Comunicazione asseverata prima dei lavori; controlli secondo disciplina regionale |
| SCIA ordinaria, art. 22 | Avvio dalla presentazione, se sussistono tutti i presupposti; potere ordinario di controllo edilizio entro 30 giorni |
| SCIA alternativa, art. 23 | Presentazione almeno 30 giorni prima dell'inizio; efficacia massima 3 anni, salvo disciplina speciale applicabile |
| Permesso, artt. 10 e 20 | Attendere il titolo espresso o la formazione del silenzio-assenso alle condizioni di legge |

La SCIA alternativa è ammessa nelle ipotesi dell'art. 23, comma 01: ristrutturazione pesante e determinate nuove costruzioni/ristrutturazioni urbanistiche già governate da disposizioni planovolumetriche sufficientemente precise. Non è una scelta alternativa universale per qualsiasi nuova opera. Se servono assensi su vincoli, i trenta giorni decorrono secondo i commi 3–4 dall'assenso o dall'esito della conferenza; non basta aver depositato una segnalazione incompleta. Il decorso del controllo ordinario della SCIA non rende irrilevanti falsità, vigilanza edilizia e poteri successivi nei rispettivi presupposti.''')
s=s.replace('Il permesso di costruire è il provvedimento espresso previsto', 'Il permesso di costruire è il titolo abilitativo previsto')
s=before(s,'### Atti ulteriori e discipline concorrenti', '''L'art. 20, comma 8, prevede il **silenzio-assenso** decorso inutilmente il termine conclusivo senza motivato diniego, nelle condizioni procedimentali previste. Non basta contare giorni da una domanda priva dei presupposti: richieste istruttorie, sospensioni e atti intervenuti incidono sul percorso. La conclusione può dunque essere espressa oppure tacita.

Per immobili con vincoli idrogeologici, ambientali, paesaggistici o culturali si applica la conferenza di servizi. Dal 18 dicembre 2025, la modifica della L. 182/2025, art. 40, fa salva la formazione del silenzio-assenso sul permesso se per il **medesimo intervento e gli stessi elaborati** sono già acquisiti e validi gli assensi formali delle autorità di tutela. Un'autorizzazione scaduta o riferita a un progetto diverso non basta. Questa disposizione non fa formare per silenzio l'autorizzazione paesaggistica mancante.

**Confronto.** Progetto vincolato senza assenso della tutela: non si conclude invocando automaticamente il silenzio sul permesso; occorre il percorso previsto. Stesso progetto, assenso formale già acquisito e valido, domanda completa e termini correttamente decorsi senza diniego: può operare la fattispecie di silenzio-assenso dell'art. 20, comma 8.''')
s=before(s,'## N-TR03-06-07', '''### Tre istituti da non confondere

**Art. 36: doppia conformità.** Per assenza o totale difformità dal permesso, oppure dalla SCIA alternativa nelle ipotesi indicate, l'intervento deve essere conforme alla disciplina urbanistica ed edilizia sia quando fu realizzato sia quando viene presentata la domanda. La risposta deve intervenire entro 60 giorni; il silenzio equivale a rifiuto. Una conformità sopravvenuta non soddisfa da sola questa doppia verifica.

**Art. 36-bis: conformità differenziata.** Per parziali difformità, assenza/difformità della SCIA nelle ipotesi dell'art. 37 e variazioni essenziali, serve conformità urbanistica al momento della domanda ed edilizia al momento della realizzazione. Occorrono attestazione, prova dell'epoca, pagamento e gli altri presupposti; il SUE può prescrivere gli interventi tecnici necessari o la rimozione delle parti non sanabili secondo il comma 2. Sul permesso in sanatoria il termine è 45 giorni, con silenzio-assenso; per la SCIA si applica il termine edilizio di 30 giorni. I procedimenti paesaggistici e le esigenze istruttorie producono le sospensioni/interruzioni previste: i due termini non sono un automatismo isolato dal fascicolo.

**Art. 34-bis: tolleranze.** Gli scostamenti entro i limiti di legge non costituiscono violazione edilizia; non si tratta quindi di un condono. La regola generale è il 2% delle misure previste dal titolo. Per interventi realizzati entro il 24 maggio 2024 la norma articola i limiti secondo superficie utile assentita: 2% oltre 500 m², 3% nella fascia 300–500, 4% nella fascia 100–300, 5% sotto 100 e 6% sotto 60. Per valori esattamente di confine si deve leggere la formulazione normativa e la disciplina applicabile, senza arrotondare per scegliere la fascia più favorevole. Restano requisiti sismici, condizioni delle tolleranze esecutive e diritti dei terzi.

**Esempi risolti.** Una difformità parziale realizzata nel 2020 è conforme all'urbanistica oggi e ai requisiti edilizi del 2020, ma non all'urbanistica del 2020: può rientrare nel percorso dell'art. 36-bis se soddisfa tutti gli altri presupposti; non soddisferebbe la doppia conformità dell'art. 36. Un nuovo edificio integralmente privo di permesso non passa al 36-bis solo perché oggi è urbanisticamente compatibile. Per una unità di 80 m² assentiti, intervento del 2020 e parametro progettato di 4 m, uno scostamento di 0,16 m è il 4%: entro il 5% della fascia applicabile, ferme le altre condizioni. La sola percentuale non certifica l'intero stato legittimo.''')
s=before(s,'## N-TR03-06-08', '''### Qualificazione su dati completi

**Caso A.** Appartamento legittimo, non vincolato; sostituzione delle sole finiture e manutenzione degli impianti esistenti, senza altre opere: manutenzione ordinaria, edilizia libera nel quadro nazionale. **Caso B.** Spostamento di tramezzi non strutturali e rinnovo servizi, senza cambiare volume, prospetti, destinazione o altre condizioni che portino agli artt. 10/22: manutenzione straordinaria, CILA. **Caso C.** Apertura in una parete portante nell'ambito di manutenzione straordinaria, senza ristrutturazione pesante né vincoli ulteriori: SCIA art. 22, oltre agli adempimenti strutturali/sismici pertinenti. La SCIA edilizia non li assorbe.

I dati dei tre casi sono ipotesi assegnate, non fatti da presumere durante un sopralluogo. Per un edificio tutelato o una disciplina regionale diversa si ricostruisce anche quel regime, mantenendolo distinto dalla qualificazione nazionale.''')
save(p,s)
Path('artifacts/correzioni-collana-2026-10-02/VOL-10-first-changes.json').write_text(json.dumps(changes,indent=2),encoding='utf8')
print('Updated',len(changes),'chapters')
