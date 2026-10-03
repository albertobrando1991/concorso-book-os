from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');p=B/'chapters/02-indipendenza-governance-accountability-personale.md';s=p.read_text(encoding='utf8')
start=s.index('Le leggi istitutive di AGCM');end=s.index('\n\n![Figura 2.2',start)
s=s[:start]+'''Composizione, nomina e durata sono parte del programma, insieme alla funzione delle garanzie. Le tabelle seguenti ricostruiscono gli otto enti al **3 ottobre 2026**. Si studiano le regole, senza confonderle con i nomi di chi ricopre temporaneamente gli incarichi. La legge istitutiva va coordinata con le disposizioni successive: per AGCM la composizione è stata ridotta a tre; per ARERA è oggi cinque; per CONSOB la durata è sette anni, anche se la vecchia disposizione istitutiva conserva una diversa formulazione.

### Organi, nomina e mandato

| Ente e organo | Nomina | Durata e rinnovo |
| --- | --- | --- |
| AGCM: Presidente e due componenti | Determinazione d'intesa dei Presidenti di Camera e Senato | Sette anni; nessuna conferma |
| ARERA: Presidente e quattro componenti | DPR, previa deliberazione del Consiglio dei ministri e proposta ministeriale; parere favorevole delle commissioni parlamentari con maggioranza dei due terzi | Sette anni; nessuna conferma |
| AGCOM: Presidente e quattro commissari nel Consiglio | Due commissari eletti da ciascuna Camera e nominati con DPR; Presidente con DPR su proposta del Presidente del Consiglio d'intesa ministeriale, previo parere qualificato | Sette anni; non rinnovabili. Eccezione per il commissario subentrante quando mancano meno di tre anni alla scadenza ordinaria |
| CONSOB: Presidente e quattro membri | DPR su proposta del Presidente del Consiglio, previa deliberazione del Consiglio dei ministri; parere parlamentare secondo L. 14/1978 | Sette anni; nessun rinnovo, per DL 248/2007, art. 47-quater |
| Banca d'Italia: Governatore, Direttore generale e tre Vice Direttori generali nel Direttorio | Governatore con DPR su proposta del Presidente del Consiglio, previa deliberazione governativa e parere del Consiglio superiore; altri membri nominati dal Consiglio superiore su proposta del Governatore, con approvazione mediante DPR | Sei anni; un solo rinnovo |
| IVASS: Presidente e due consiglieri nel Consiglio | Presidente è il Direttore generale della Banca d'Italia; consiglieri con DPR, deliberazione governativa, iniziativa del Presidente del Consiglio, proposta del Governatore e concerto ministeriale | Per i due consiglieri: sei anni e un rinnovo; la Presidenza segue la carica di Direttore generale |
| Garante: Collegio di quattro membri | Due eletti dalla Camera e due dal Senato con voto limitato; il Collegio elegge al proprio interno Presidente e Vicepresidente | Sette anni; nessun rinnovo |
| ANAC: Presidente e quattro componenti | DPR previa deliberazione governativa; parere parlamentare dei due terzi; proposte ministeriali dell'art. 13, comma 3, D.Lgs. 150/2009 | Sei anni; nessuna conferma |

AGCOM ha anche due commissioni, per infrastrutture e reti e per servizi e prodotti: ognuna comprende il Presidente e due commissari. In IVASS il **Direttorio integrato** comprende i cinque membri del Direttorio della Banca d'Italia e i due consiglieri IVASS: assume indirizzi e provvedimenti esterni di vigilanza; il Consiglio cura l'amministrazione generale. Non si devono confondere questi due organi.

Per ANAC la proposta del Presidente è formulata dal Ministro per la pubblica amministrazione, di concerto con Giustizia e Interno; per i componenti proviene dal Ministro per la pubblica amministrazione. Il parere dei due terzi è richiesto dalla fonte ANAC e da quella ARERA: non va trasferito automaticamente alla procedura CONSOB.

### Incompatibilità: esempi normativi da distinguere

| Ente | Regola da conoscere | Fonte |
| --- | --- | --- |
| AGCM | Incompatibilità con attività professionali, consulenza, altri uffici e lavoro pubblico o privato; per tre anni dopo cessazione, divieto di seguire i procedimenti antitrust già trattati | L. 287/1990, art. 10, commi 3–3-ter |
| ARERA e AGCOM | Divieti professionali, di consulenza, altri uffici e interessi nelle imprese del settore; almeno due anni dopo cessazione, limiti a rapporti nel settore per componenti e dirigenti, con eccezione prevista per dirigenti di soli uffici di supporto | L. 481/1995, art. 2, commi 8–9; L. 249/1997, art. 1, comma 5 |
| CONSOB | Incompatibilità con professioni, consulenza, determinate cariche o partecipazioni societarie, lavoro pubblico/privato e altri uffici pubblici | DL 95/1974, art. 1 |
| Banca d'Italia | Divieti su strumenti finanziari dei vigilati e disciplina post-incarico: 24 mesi per il Direttorio, 12 per il personale nelle funzioni indicate; destinatari e decorrenza differenziati | L. 262/2005, artt. 29-ter e 29-quater, dopo D.Lgs. 208/2025 |
| IVASS | Incompatibilità politica e conflitti; divieti di attività per soggetti vigilati e di attività/cariche commerciali nei termini dello Statuto | Statuto IVASS, artt. 11–12 |
| Garante | Vietata anche la consulenza gratuita; incompatibilità con lavoro e cariche elettive. Per due anni dopo cessazione, astensione dai procedimenti davanti al Garante | D.Lgs. 196/2003, art. 153 |
| ANAC | Non possono essere scelti titolari di incarichi elettivi, cariche di partito o sindacali, anche nei tre anni precedenti; esclusi interessi in conflitto | D.Lgs. 150/2009, art. 13, comma 3 |

**Applicazione Banca d'Italia.** Una funzionaria che ha vigilato direttamente sulla banca Alfa riceve un'offerta da Alfa. Comunica senza ritardo l'offerta; l'Istituto accerta i presupposti e può assegnarla a mansioni diverse di pari livello, senza accesso ai dati sensibili, durante il periodo di incompatibilità e fino alla cessazione dell'impiego. I dodici mesi decorrono dalla cessazione delle funzioni pertinenti, non necessariamente dalle dimissioni. Per un membro del Direttorio il periodo è invece di 24 mesi dalla cessazione del mandato e il perimetro è più ampio dei soli soggetti personalmente seguiti. I contratti contrari ai divieti sono nulli.

### Personale e controlli: il confronto compilato

| Ente | Regime del personale | Rendicontazione e controlli |
| --- | --- | --- |
| AGCM | Ordinamento proprio; regolamenti su stato giuridico, trattamento e carriere, art. 10, comma 6, L. 287; art. 3 D.Lgs. 165 | Bilancio e rendiconto; controllo della Corte dei conti sul rendiconto |
| ARERA | Regolamenti propri; criteri AGCM e specifiche esigenze dell'ente, art. 2, comma 28, L. 481 | Relazione al Parlamento; bilancio/rendiconto e Corte dei conti |
| AGCOM | Regolamenti dell'Autorità secondo L. 481, per rinvio dell'art. 1, comma 9, L. 249 | Bilanci e rendiconti, trasparenza e controllo giurisdizionale sugli atti; regole proprie di accountability |
| CONSOB | Regolamenti propri, DL 95/1974 art. 1; ordinamento speciale, art. 3 D.Lgs. 165 | Controllo di legittimità governativo sui regolamenti nei termini di legge; Corte dei conti sul rendiconto; relazione istituzionale |
| Banca d'Italia | Ordinamento proprio, art. 3 D.Lgs. 165; regolamenti interni e accordi approvati dal Consiglio superiore | Consiglio superiore per gestione e controllo interno; Collegio sindacale e revisore esterno; relazione al Parlamento e al Governo |
| IVASS | Trattamento e regolamento deliberati dal Consiglio, che approva gli accordi sindacali, art. 13 DL 95/2012 | Relazione al Parlamento/Governo; revisori esterni e Corte dei conti |
| Garante | Regolamenti propri, art. 156 Codice privacy; trattamento economico raccordato ad AGCOM | Rendiconto alla Corte dei conti e controlli previsti dal GDPR |
| ANAC | Autonomia regolamentare, art. 52-quater DL 50/2017, principi L. 481 e criteri economici AGCM | Regolamenti, programmazione, trasparenza e relazione istituzionale; tutela sugli atti secondo il potere esercitato |

Le forme di rendicontazione della terza colonna sono esempi principali, non un catalogo esclusivo. Il regime speciale non elimina concorso, imparzialità o tutela. **Non esiste un rinvio automatico al CCNL Funzioni Centrali:** si applicano la fonte speciale e gli atti dell'ente; i requisiti della singola selezione si leggono nel bando.
'''+s[end:]
s=s.replace("Con questo termine si indica la capacità dell'autorità di rendere comprensibile, verificabile e contestabile l'esercizio delle proprie funzioni.","Con questo termine si indica l'obbligo dell'autorità di rendere conto delle decisioni e dei risultati: motivazione, trasparenza, rendicontazione e controlli consentono di comprenderne e valutarne l'operato.")
start=s.index('### Prova di trasferimento');s=s[:start]+'''## N-MF05-02-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Due Presidenti delle Camere nominano d'intesa un collegio di tre membri per sette anni. Quale autorità fra AGCM, ARERA e ANAC corrisponde ai dati?

**Risposta corretta:** AGCM. ARERA ha cinque membri e nomina con DPR nel procedimento governativo-parlamentare; ANAC ha cinque membri e mandato di sei anni. La composizione AGCM coordina L. 287 e art. 23 DL 201/2011.

**Quesito 2.** Per CONSOB basta leggere il mandato quinquennale nell'art. 1 DL 95/1974 per compilare la scheda corrente?

**Risposta corretta:** no. L'art. 47-quater DL 248/2007 porta il mandato a sette anni senza rinnovo. La disposizione successiva esterna va coordinata con quella istitutiva: non si sceglie il testo solo perché appare nella pagina più familiare.

**Quesito 3.** Chi presiede IVASS e chi adotta gli indirizzi strategici di vigilanza?

**Risposta corretta:** il Direttore generale della Banca d'Italia è Presidente IVASS. L'indirizzo strategico spetta al Direttorio integrato, presieduto dal Governatore; l'amministrazione generale al Consiglio. Presidenza, Consiglio e Direttorio integrato sono organi distinti.

**Quesito 4.** Un componente del Garante può svolgere una consulenza gratuita perché non percepisce reddito?

**Risposta corretta:** no. L'art. 153 Codice privacy vieta anche la consulenza non remunerata durante il mandato. L'assenza di compenso non esclude l'incompatibilità.

**Quesito 5.** Un funzionario ANAC conclude che, essendo dipendente pubblico, gli si applica senz'altro il CCNL Funzioni Centrali. Quale passaggio manca?

**Risposta corretta:** la lettura dell'art. 52-quater DL 50/2017 e del regolamento del personale dell'Autorità. L'autonomia regolamentare segue i principi della L. 481 e i criteri economici AGCM; il carattere pubblico del datore non individua da solo il contratto applicabile.

**Quesito 6.** L'obbligo di rendere conto al Parlamento trasforma una decisione tecnica in un atto soggetto a istruzioni politiche di merito?

**Risposta corretta:** no. Accountability e indipendenza svolgono funzioni complementari. La relazione espone attività, risultati e criticità; le decisioni restano fondate sulla competenza, sui fatti e sulle norme. Il controllo giurisdizionale segue i rimedi del capitolo 6.

### Caso ragionato di chiusura

**Fatti didattici.** Per un bando Garante, Elisa prepara una scheda con cinque componenti, nomina governativa, mandato settennale rinnovabile e ammissibilità della consulenza gratuita. Inserisce inoltre «CCNL Funzioni Centrali» senza fonte. Correggi la scheda in cinque righe.

**Soluzione.** I componenti sono quattro, eletti due da ciascuna Camera; il Collegio elegge Presidente e Vicepresidente. Il mandato dura sette anni e non è rinnovabile. È vietata anche la consulenza gratuita, a pena di decadenza. Il personale segue i regolamenti previsti dall'art. 156, con il raccordo economico ad AGCOM; non si presume un CCNL generale. Le fonti sono gli artt. 153 e 156 del D.Lgs. 196/2003, verificati al 3 ottobre 2026.

**Autovalutazione:** un punto per ciascuna correzione motivata; ripassa la tabella specifica se confondi la nomina Garante con quella ARERA o ANAC.

**Riferimenti normativi e professionali.** L. 287/1990, art. 10; DL 201/2011, art. 23; L. 481/1995, art. 2; L. 205/2017, art. 1, comma 528; L. 249/1997, art. 1; DL 95/1974, art. 1 e DL 248/2007, art. 47-quater; L. 262/2005, artt. 19, 29-ter e 29-quater; DL 95/2012, art. 13; D.Lgs. 196/2003, artt. 153 e 156; D.Lgs. 150/2009, art. 13; DL 50/2017, art. 52-quater; D.Lgs. 165/2001, art. 3. Testi vigenti in [Normattiva](https://www.normattiva.it/); [Statuto Banca d'Italia](https://www.bancaditalia.it/chi-siamo/funzioni-governance/disposizioni-generali/statuto.pdf), artt. 18–23; [Statuto IVASS](https://www.ivass.it/normativa/nazionale/primaria/Statuto_IVASS.pdf), artt. 11–12. Quadro verificato il 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true');s=s.replace('source_refs: [','source_refs: ["sources/vol-05-governance-verifica-2026-10-03.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/vol-05-governance-verifica-2026-10-03.md", "wiki/topics/authority-rettifiche-2026.md", ',1)
p.write_text(s,encoding='utf8');print('Applied V05-05/06; chapter 2 six specific questions and case; figures pending.')
