from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
def f(x):return next(B.glob(x+'*.md'))
def insert(pre,head,txt):
 p=f(pre);s=p.read_text(encoding='utf8');assert head in s;s=s.replace(head,head+'\n\n'+txt,1);p.write_text(s,encoding='utf8')
p=f('appendice-f');s=p.read_text(encoding='utf8');a=s.index('### Simulazione mista di dieci minuti');b=s.index('### Checklist di autonomia',a)
s=s[:a]+'''### Simulazione mista di dieci minuti

Dedica due minuti a ciascuna traccia; assegna due punti per ogni soluzione: uno per la distinzione corretta, uno per la sua applicazione. Totale dieci punti. Leggi le correzioni soltanto dopo avere risposto.

**1. Fonti UE.** Un ufficio rinvia l'applicazione di un regolamento UE vigente perché attende una legge nazionale di recepimento. Distingui il regolamento dalla direttiva e individua l'errore.

**2. Contratto.** Un fornitore, vincolato da un contratto valido, non consegna entro il termine essenziale concordato e invoca una generica difficoltà interna. Quali istituti esamini: nullità, adempimento, risoluzione o risarcimento? Indica il dato da accertare.

**3. Sicurezza.** Un'impresa fornisce guanti, ma omette una protezione collettiva tecnicamente necessaria per un macchinario. Dopo una lesione afferma che l'assicurazione INAIL renda irrilevante l'omissione. Distingui misura preventiva e tutela assicurativa.

**4. Finanze.** Un programma di prevenzione costa 100.000 euro e raggiunge 200 imprese; un secondo costa 120.000 e ne raggiunge 300. Confronta il costo medio per impresa e indica perché il solo confronto non basta a giudicare l'efficacia.

**5. Condotta.** Un funzionario incaricato di un acquisto riceve dal fornitore la promessa di denaro per favorirlo. Non deve formulare una sentenza, ma deve individuare il rischio giuridico e la condotta immediata corretta. Può qualificare il fatto come «abuso d'ufficio vigente»?

### Correzione delle cinque tracce

**1.** Il regolamento è direttamente applicabile e non richiede recepimento come condizione generale; la direttiva vincola al risultato lasciando forme e mezzi ai destinatari, nei limiti del diritto UE. Si verifica la disposizione e la decorrenza, senza inventare un'attesa generalizzata. Un punto per la distinzione, uno per correggere il rinvio dell'ufficio.

**2.** Si tratta di inadempimento di un contratto valido, non di nullità dimostrata dai fatti. Si verificano obbligo, termine essenziale, condotta e causa dell'inadempimento, quindi disciplina della risoluzione ed eventuale danno risarcibile. La generica difficoltà interna non prova da sola la causa non imputabile dell'articolo 1218. Un punto per la categoria, uno per accertamenti e rimedio pertinente.

**3.** Il dispositivo individuale non sostituisce la misura collettiva necessaria. L'obbligo di prevenzione e la prestazione INAIL sono distinti: la copertura assicurativa non giustifica l'omessa protezione. Si ricostruiscono obblighi e fatti senza anticipare l'accertamento delle responsabilità. Un punto per la gerarchia delle misure, uno per la separazione dei piani.

**4.** Il costo medio è 500 euro nel primo programma e 400 nel secondo. Il secondo è meno costoso per impresa raggiunta, a parità delle altre condizioni; per l'efficacia occorrono risultati sulla riduzione del rischio e qualità degli interventi. Un punto per i calcoli, uno per il limite dell'indicatore.

**5.** La promessa collegata al favore pone il tema delle fattispecie corruttive e, secondo i fatti, dell'istigazione; il dipendente rifiuta, preserva le evidenze e attiva i canali e gli obblighi di segnalazione pertinenti. L'articolo 323 è abrogato dalla legge 114/2024. Un punto per la distinzione penale corretta, uno per la condotta; non si attribuisce una qualificazione definitiva senza tutti gli elementi.

''' +s[b:]
s=s.replace('sezioni «Patologie del contratto» e «Responsabilità»','sezioni «7. Invalidità e scioglimento» e «5. Responsabilità civile»')
p.write_text(s,encoding='utf8')
# Correct the promise of the routing table, while preserving existing explanatory sections.
p=f('appendice-e');s=p.read_text(encoding='utf8')
s=s.replace('| Funzionario amministrativo, giuridico, economico o contabile presso INPS, INAIL o altro EPNE compatibile | Sì, con eventuali appendici | M-FC03 resta modulo principale. |','| Funzionario amministrativo presso INPS/INAIL | Percorso principale, con VOL-01 e verifica del programma | Capitoli 2–9 per le materie; 11–12 per casi e situazionali. |')
s=s.replace('| Vigilanza previdenziale o assicurativa INPS-INAIL | Sì, ma con sottoprofilo | Attivare Appendice A e capitolo 12 per situazionali. |','| Vigilanza previdenziale o assicurativa INPS-INAIL | Copertura essenziale degli istituti qui spiegati | Appendice A, «Poteri, atti e garanzie della vigilanza» e «Le due diffide e la conciliazione»; ulteriori fattispecie del bando da integrare. |')
s=s.replace('| ACI, ENAC, ISTAT, ENEA, ASI, CONI, CRI in profili amministrativi | Sì, come orientamento | Attivare Appendice C e verificare fonti ufficiali. |','| ACI, ENAC, CONI; enti di ricerca e CRI per confronto | Orientamento, non equivalenza di ordinamento o comparto | Appendice C, scheda del singolo ente e «Natura dell’ente, comparto e percorso di studio». |')
s=s.replace('Se il bando contiene vigilanza previdenziale o assicurativa, non devi cambiare modulo: devi usare l\'Appendice A.','Se il bando contiene vigilanza previdenziale o assicurativa, parti dall’Appendice A per poteri, atti, diffide e rimedi. Completa le specifiche fattispecie di lavoro e sicurezza richieste dal programma: l’appendice non prova da sola una copertura esaustiva.')
s=s.replace('Questo è sufficiente per profili amministrativi ordinari.','Questo offre il raccordo EPNE con la teoria del VOL-01, capitolo Contratti pubblici essenziali, sezioni «9. Soglie e scelta della procedura» e «16. Consip, Acquisti in Rete, MEPA, convenzioni e accordi quadro». La sufficienza rispetto alla prova dipende dal programma effettivo.')
s=s.replace('### Controllo dei riferimenti prima della pubblicazione','### Controllo dei riferimenti prima dello studio')
routes=[
('Ricerca, anche personale amministrativo','VOL-06','m-ir03-enti-ricerca','03-profili-organizzazione','03'),
('Sicurezza informatica','VOL-09','m-tr01-ict-trasformazione-digitale','08-cybersecurity-rischio-controlli-vulnerabilita','08'),
('Strumenti di acquisto specialistici','VOL-10','m-tr02-appalti-pnrr-fondi-ue','07-consip-mepa-aq-sdapa-asp','07'),
('Fisco, dogane e riscossione','VOL-03','m-fc02-agenzie-fiscali','01-','01'),
('Autorità indipendenti','VOL-08','m-fc05-authority-indipendenti','01-','01')]
rows=[];evidence=[]
for label,vol,mod,pre,num in routes:
 target=next(Path('wiki/books/moduli',mod,'chapters').glob(pre+'*.md'));t=target.read_text(encoding='utf8');title=re.search(r'^title:\s*(.+)$',t,re.M).group(1).strip('"')
 heads=re.findall(r'^#{2,3} (.+)$',t,re.M);head=next((h for h in heads if not h.startswith('N-') and 'Apertura' not in h),heads[0])
 rows.append(f'| {label} | {vol}, capitolo {num}: {title}; sezione «{head}» | Avvio del percorso; confrontare poi i nuclei del programma. |')
 evidence.append({'label':label,'path':target.as_posix(),'section':head,'exists':True})
table='''### Destinazioni disponibili e limite del rinvio

Queste destinazioni esistono nella collana. La sezione indicata avvia il percorso: non sostituisce i capitoli successivi né dimostra che ogni programma specialistico sia già coperto. Per professioni sanitarie e carriere speciali si sceglie il profilo del rispettivo volume; per il servizio sociale professionale non si promette qui un modulo completo disponibile.

| Materia | Destinazione | Uso |
| --- | --- | --- |
'''+'\n'.join(rows)+'''\n
Per civile e responsabilità: in questo VOL-03, modulo Agenzie fiscali, capitolo 12 «Civile e commerciale applicati a fisco, dogane e riscossione», sezioni «5. Responsabilità civile» e «7. Invalidità e scioglimento». Per le differenze INPS/INAIL usa qui i capitoli 3 e 4, non una scheda di un altro ente. Se il bando introduce una materia non sviluppata nella destinazione, la registri come integrazione necessaria: il rinvio non la rende completa per definizione.

'''
s=s.replace('### Scheda dei rinvii ragionati',table+'### Scheda dei rinvii ragionati',1);p.write_text(s,encoding='utf8')
(A/'FC03-destinazioni.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf8')
# Readable replacements, confined to reader bodies and preserving legitimate content.
repl={
'nel perimetro redazionale':'nelle schede comparative',
'fonti normative consolidate nel wiki':'fonti normative',
'fonti settoriali già censite':'fonti settoriali',
'La fonte Garante consolidata nel wiki insiste proprio su questo punto:':'Le regole sulla protezione dei dati chiariscono questo punto:',
'Il topic consolidato su anticorruzione e trasparenza ricorda che questi strumenti servono a':'Gli strumenti di anticorruzione e trasparenza servono a',
'La fonte sulla responsabilità dirigenziale, pur richiedendo review per citazioni specialistiche, è utile come orientamento:':'La responsabilità dirigenziale riguarda anche l’organizzazione:',
'Il bando INAIL/RIPAM 308 unità, già consolidato nel wiki,':'Il bando INAIL/RIPAM 308 unità del 2024',
'prima della pubblicazione o della prova':'prima della prova',
'Il documento ufficiale da verificare prima della pubblicazione è:':'Il documento ufficiale da verificare prima della prova è:',
'esempio consolidato':'esempio storico',
'### Testo editoriale\n\n':'',
}
for p in B.glob('*.md'):
 s=p.read_text(encoding='utf8');parts=s.split('---',2);body=parts[2]
 for a,b in repl.items():body=body.replace(a,b)
 p.write_text('---'+parts[1]+'---'+body,encoding='utf8')
# Add useful application detail to short, intact semantic sections.
insert('05-','### Servizi digitali e documenti informatici','''L'identità digitale autentica chi accede, ma non prova da sola il potere di agire per un terzo. Per esempio, l'accesso di un figlio con le proprie credenziali non autorizza automaticamente a consultare la posizione del genitore. Si verifica la delega o il diverso titolo previsto dal servizio, mantenendo separati identificazione, autorizzazione e finalità. Anche un documento ricevuto digitalmente va associato alla pratica corretta e controllato per pertinenza e integrità, evitando copie indiscriminate in cartelle personali.\n''')
insert('07-','### Perché il PIAO conta negli EPNE','''Esempio di obiettivo verificabile: ridurre, entro l'anno, il tempo mediano di una tipologia di pratica da trenta a venticinque giorni, senza aumentare il tasso di rettifica. Il valore iniziale, il perimetro delle pratiche e la fonte dei dati devono essere definiti. Altrimenti un apparente miglioramento potrebbe dipendere dall'esclusione dei casi complessi dal conteggio. Il monitoraggio collega quindi indicatore quantitativo, qualità e regola di rilevazione; non premia il solo numero più favorevole.\n''')
insert('09-','### Il ciclo dell\'acquisto EPNE','''Nel fascicolo si distingue il fabbisogno dalla soluzione già immaginata dal fornitore. Se l'ufficio chiede assistenza per tre sportelli, prima descrive prestazioni, tempi, livelli di servizio e modalità di verifica; poi stima il valore e sceglie lo strumento conforme. Indicare subito una marca senza motivazione o spezzare il medesimo servizio in ordini separati può alterare la scelta. Una scheda di fabbisogno verificabile permette invece di confrontare offerte e controllare l'esecuzione rispetto a risultati concordati.\n''')
insert('09-','### Strumenti digitali, MEPA e Consip','''L'assenza di un prodotto in un catalogo non dimostra l'assenza di una convenzione o di un accordo pertinente. Occorre identificare oggetto, amministrazione obbligata, caratteristiche essenziali e strumenti disponibili. Nel caso di strumenti alternativi si registra perché quello scelto soddisfa il fabbisogno e quali obblighi restano applicabili. La piattaforma è il mezzo attraverso cui si compie un acquisto disciplinato: non rende di per sé legittima una procedura scelta senza verificare valore, oggetto e competenza.\n''')
insert('appendice-c','### Esercizio di aggiornamento','''Conserva separatamente il dato stabile e quello mobile. «Ente pubblico di ricerca» identifica un ordinamento; il nome del presidente e la data del prossimo concorso sono informazioni mobili. Per ciascuna annota atto, data e campo di applicazione. Se cambia il titolare di un organo, non si riscrive automaticamente la competenza dell'organo; se cambia il CCNQ, invece, può essere necessario rivedere il comparto. La scheda deve mostrare quale elemento è cambiato e quale rimane valido.\n''')
insert('appendice-d','### Errore 8: sottovalutare prove, soglie e output','''Una soglia di idoneità non coincide con il punteggio necessario per entrare fra i vincitori. Se la prova richiede almeno 21 su 30, quel valore indica l'ammissibilità alla fase o l'idoneità prevista; la posizione utile dipende da graduatoria, posti e regole del bando. Registrare separatamente soglia, punteggio e posti evita di trasformare un requisito minimo in una previsione di assunzione. Anche riserve e preferenze operano secondo regole proprie, non come punti aggiuntivi inventati.\n''')
print('Simulazioni, destinazioni, pulizia e applicazioni completate.')
