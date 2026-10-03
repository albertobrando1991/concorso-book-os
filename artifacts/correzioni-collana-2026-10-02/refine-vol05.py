from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti/chapters');O=Path('artifacts/correzioni-collana-2026-10-02')
adds={
(1,5):'''### Un controllo del piano già compilato

Se scegli il percorso E, una settimana dedicata soltanto a definizioni istituzionali non verifica la priorità quantitativa. Inserisci una prova con dati, una correzione aritmetica e una risposta sul significato economico del risultato. Se il calcolo è corretto ma attribuisci il potere all'autorità sbagliata, programma anche il ripasso della competenza: i due errori richiedono azioni diverse.
''',
(2,4):'''### Applicazione alla documentazione dell'ente

Confronta la tabella degli organi con un bando che richiede «ordinamento e regolamenti dell'Autorità». La prima fornisce composizione e nomina; il secondo può richiedere anche unità organizzative, contabilità e regole del concorso. Non sostituire il dato strutturale con i nomi dei titolari correnti. In una scheda di ripasso separa quindi legge istitutiva, statuto, regolamento organizzativo e bando, indicando per ciascuno quale domanda risolve.
''',
(2,5):'''**Variante del caso.** Se al posto del Garante la traccia riguardasse ARERA, non conserveresti la nomina parlamentare: cambiano organo proponente, procedimento di nomina e composizione. La garanzia di indipendenza resta una finalità comune, ma non rende intercambiabili le due risposte.
''',
(3,5):'''### Dalla sigla all'atto

Un documento EBA reca «consultation paper» e propone uno standard tecnico. Nella risposta non lo presenti come regolamento già applicabile: identifichi il progetto, la consultazione e il successivo atto della Commissione eventualmente adottato. Se invece la traccia contiene una decisione vincolante EDPB su una controversia fra autorità, ne spieghi presupposto ed effetti nel meccanismo GDPR. Entrambi i documenti provengono dal livello europeo, ma fonte, destinatari e forza giuridica sono diversi. Questa distinzione deve restare visibile anche in una risposta orale di novanta secondi.
''',
(4,5):'''### Verifica della scelta nella mini-AIR

Riprendi la soluzione numerica del capitolo e controlla separatamente tre operazioni: sottrazione dei costi dai benefici, confronto incrementale delle alternative e analisi dello scenario avverso. Una misura con beneficio lordo maggiore può avere un beneficio netto appena superiore e un rischio più alto. Nella motivazione indica quali gruppi sostengono i costi e quali ricevono i benefici: il saldo aggregato non mostra da solo la distribuzione. Infine associa l'obiettivo a un indicatore osservabile e a una fonte dati, senza usare il numero di consultazioni svolte come prova automatica del miglioramento del servizio.
''',
(5,5):'''### Un documento che non basta

Una schermata mostra una condizione contrattuale, ma non indica la data. Prima di trattarla come prova della campagna contestata, acquisisci URL, versione, periodo di pubblicazione e percorso seguito dall'utente. Confrontala con contratto effettivamente concluso e comunicazioni conservate. Il file può essere autentico e tuttavia riferirsi a una versione successiva: autenticità e pertinenza temporale sono controlli distinti. Nella richiesta non domandare indistintamente tutti i dati di ogni cliente; delimita periodo e campione pertinenti, motiva l'utilità e proteggi i dati personali e i segreti secondo il procedimento applicabile. La quantità di documenti non sostituisce la qualità dell'evidenza.
''',
(6,4):'''**Verifica della variante.** Se l'impresa viola successivamente gli impegni resi obbligatori, non si conclude che quegli impegni fossero una semplice promessa privata. Si applica la specifica disciplina di controllo e delle conseguenze dell'inottemperanza, distinguendola dall'esecuzione di una sentenza.
''',
(9,5):'''**Variante numerica.** Se, ferme le altre ipotesi del caso, il recupero fosse 60 anziché 80, la somma preliminare salirebbe a 1.060. Il limite ipotetico di 1.030 resterebbe però decisivo: non basta dividere automaticamente la nuova somma per le unità. Verifica prima il metodo, il limite e il procedimento di approvazione.
''',
(10,4):'''**Controllo del destinatario.** Nella doppia fatturazione il reclamo è rivolto all'operatore; la conciliazione segue il sistema competente. Nella sospensione dell'account occorre prima qualificare il servizio digitale. La stessa persona può presentare due problemi senza che esista un unico procedimento risolutivo.
''',
(10,5):'''**Controllo finale:** SMP, VLOP e gatekeeper sono qualificazioni diverse. Non trasferire la designazione, la fonte o il rimedio da una colonna all'altra della tua scheda.
''',
(11,1):'''**Prima distinzione pratica.** Una società che pubblica il prospetto agisce come emittente; la banca che raccomanda quel titolo presta un servizio al cliente. L'approvazione del prospetto non risolve la verifica di adeguatezza della raccomandazione.
'''
}
for p in sorted(B.glob('*.md')):
 s=p.read_text(encoding='utf8');n=int(p.name[:2])
 for (c,k),txt in adds.items():
  if c!=n:continue
  pat=r'^## N-MF05-'+f'{n:02d}-{k:02d}'+r'[^\n]*\n';m=re.search(pat,s,re.M);assert m,(c,k);a=m.end();s=s[:a]+'\n'+txt+'\n'+s[a:]
 if n==1:
  anchors={'costituzione-e-ordinamento-dello-stato':'lo-stato-in-una-pagina','diritto-amministrativo-per-candidati':'quadro-essenziale','pubblico-impiego-e-organizzazione-pa':'quadro-essenziale','trasparenza-anticorruzione-privacy':'quadro-essenziale','contabilita-pubblica-essenziale':'quadro-essenziale','informatica-pa-digitale-competenze-digitali':'quadro-di-priorità-per-lo-studio','inglese-concorsuale-essenziale':'qcercefr-e-livello-richiesto','contratti-pubblici-essenziali':'quadro-essenziale'}
  for slug,anchor in anchors.items():s=s.replace('/'+slug+'|','/'+slug+'#'+anchor+'|')
 p.write_text(s,encoding='utf8')
print('Added focused applications and exact base anchors.')
