from pathlib import Path
import json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione')
p=B/'chapters/02-tslb-processo-laboratorio-qualita-biosicurezza.md';t=p.read_text(encoding='utf8');anchor='| 8 | 107 | +3,5 |'
assert anchor in t
t=t.replace(anchor,anchor+'''

![Serie di controllo: otto sedute con z da 0 a 3,5 e andamento crescente](../assets/correzioni-2026-10/serie-controllo-qc.png)

*Figura — Serie didattica di controllo: andamento crescente rispetto alla media. I valori standardizzati permettono di osservare il trend; le decisioni dipendono dalle regole del piano QC. Non sono risultati di un paziente.*''',1);p.write_text(t,encoding='utf8')
q=B/'chapters/03-tsrm-imaging-dosimetria-radioprotezione.md';t=q.read_text(encoding='utf8');anchor='### La ripetizione non è automatica';assert anchor in t
t=t.replace(anchor,'''### Due confronti visivi: movimento e rumore

![Oggetto di prova: pannello A con contorni netti, pannello B con sfocatura direzionale](../assets/correzioni-2026-10/movimento-dettaglio.png)

*Figura — Effetto schematico del movimento sul dettaglio. A: contorni netti; B: contorni allargati e sfocati. Oggetto di prova originale, senza valore diagnostico. Il confronto illustra una causa di perdita di qualità, non la diagnosi di un artefatto in un paziente.*

**Domanda.** Nel pannello B il dettaglio è meno distinguibile. Questo basta a giustificare una nuova esposizione? Indica due verifiche preliminari.

**Soluzione.** No. Occorre valutare se l’immagine sia adeguata al quesito e identificare la causa del difetto. Si controllano dati della prestazione e condizioni di acquisizione, quindi si condivide la decisione secondo responsabilità e procedura. Una ripetizione non motivata aggiunge esposizione senza un beneficio dimostrato.

![Disco a basso contrasto: contrasto medio identico nei pannelli, rumore maggiore nel pannello B](../assets/correzioni-2026-10/rumore-contrasto.png)

*Figura — Rumore e riconoscibilità di un dettaglio a basso contrasto. I due pannelli hanno lo stesso contrasto medio; nel pannello B il rumore rende il disco meno distinguibile. Simulazione originale per lo studio della qualità, non test diagnostico né calibrazione di un sistema.*

**Domanda.** Perché aumentare indiscriminatamente l’esposizione non è la risposta generale al pannello B? Quale obiettivo guida l’ottimizzazione?

**Soluzione.** L’obiettivo è ottenere qualità sufficiente per il quesito con un’esposizione appropriata. Rumore e qualità dipendono anche da persona, tecnica, ricostruzione e apparecchiatura; il solo schema non consente di scegliere nuovi parametri. Il TSRM applica il protocollo appropriato e collabora alla verifica della qualità entro le proprie competenze.

'''+anchor,1);q.write_text(t,encoding='utf8')
spec=Path('wiki/reviews/correzioni-collana-2026-10-02/V07-39-specifica-apparati.md');t=spec.read_text(encoding='utf8').replace('contorni duplicati e sfocati','contorni allargati e sfocati');t+='\n## Consegna del 3 ottobre 2026\n\nInserite le tre immagini originali nei capitoli SA04/02 e SA04/03, con alternative testuali, didascalie, quesiti e soluzioni. Originali verificati visivamente dal coordinamento; resta da controllare il nuovo PDF dei capitoli.\n';spec.write_text(t,encoding='utf8')
state=json.loads((A/'VOL-07-changes.json').read_text(encoding='utf8'))['changes'];x=state['V07-35'];x['change']+=' Inserito grafico originale Levey–Jennings coerente con la tabella e con il quesito.';x['evidence']+=' Valori z controllati; originale ispezionato dal coordinamento. Resa del nuovo PDF pendente.';x['files']+=[str(B/'assets/correzioni-2026-10/serie-controllo-qc.png').replace('\\','/')]
y={'change':'Inseriti due apparati originali movimento/dettaglio e rumore/contrasto, con didascalie, alternative testuali, domande e soluzioni.','files':[str(q).replace('\\','/'),str(spec).replace('\\','/')]+[str(B/f'assets/correzioni-2026-10/{n}.png').replace('\\','/') for n in ['movimento-dettaglio','rumore-contrasto']],'evidence':'Originali creati e ispezionati dal coordinamento; collegamenti locali presenti. Controllo delle pagine PDF ancora necessario.','status':'applicato'}
(A/'VOL-07-batch08.json').write_text(json.dumps({'V07-35':x,'V07-39':y},ensure_ascii=False,indent=2),encoding='utf8')
for stem,source,arts in [('dlgs118','contabilita-budget-aziende-sanitarie',[26,29,31,32]),('dlgs101','radioprotezione-qualita-immagine-apparecchiature-dlgs-101-2020',[146,166])]:
 sp=Path('wiki/sources',source+'.md');s=sp.read_text(encoding='utf8');s+='\n## Riscontro consolidato Normattiva, 3 ottobre 2026\n\nSuperato il precedente limite di accesso: scaricati e letti integralmente gli articoli '+', '.join(map(str,arts))+' nel testo consolidato restituito dall’endpoint `!vig=`. Le copie sono conservate nel raw delle correzioni. '
 s+=('Confermati documenti di bilancio, sterilizzazione ex art. 29, adozione 30 aprile, approvazione regionale 31 maggio e consolidato 30 giugno. Il confronto supporta le regole utilizzate nel capitolo SA01/09; non equivale alla lettura integrale di tutto il decreto.' if stem=='dlgs118' else 'Confermati i limiti per lavoratori e popolazione dell’art. 146 e le distinte responsabilità e precauzioni gravidanza/allattamento dell’art. 166. Il confronto supporta tabella e testo di SA04/03, senza validare protocolli locali o l’intero decreto.')+'\n\n'
 for art in arts:
  raw=Path('wiki/raw/correzioni-collana-2026-10-02',f'{stem}-art{art}-current.html');data=(A/raw.name).read_bytes()
  if not raw.exists():raw.write_bytes(data)
  urn='2011-06-23;118' if stem=='dlgs118' else '2020-07-31;101'
  s+=f'- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:{urn}~art{art}!vig= — SHA256 `{hashlib.sha256(data).hexdigest()}`.\n'
 sp.write_text(s,encoding='utf8')
print('Tre figure inserite; due riscontri consolidati nelle fonti.')
