from pathlib import Path
import hashlib,shutil,re
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/raw/correzioni-collana-2026-10-02')
def append(slug,delta,names):
 p=Path('wiki/sources')/(slug+'.md');t=p.read_text(encoding='utf8')+'\n'+delta+'\n'
 for name in names:
  if not (R/name).exists():shutil.copyfile(A/name,R/name)
  t+=f'- `raw/correzioni-collana-2026-10-02/{name}` — SHA256 {hashlib.sha256((R/name).read_bytes()).hexdigest()}.\n'
 p.write_text(re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M),encoding='utf8')
append('biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05','''## Integrazione catalografica verificata il 3 ottobre 2026

Supera, per i concetti qui circoscritti, il precedente limite che permetteva soltanto di nominare gli standard. REICAT è il codice nazionale di catalogazione; ISBD organizza elementi descrittivi, sequenza e punteggiatura; UNIMARC rappresenta dati per scambio e trattamento informatico; SBNMARC è il protocollo di colloquio con l'Indice e usa semantica UNIMARC. Non sono quattro cataloghi né quattro nomi del medesimo standard. Il codice non coincide con la codifica.

L'authority control distingue identità da stringhe: forma autorizzata, varianti, qualificazioni e relazioni evitano di separare lo stesso autore o fondere omonimi. La soggettazione descrive il contenuto concettuale con accessi controllati; il Nuovo soggettario BNCF comprende guida, thesaurus e manuale applicativo. La classificazione attribuisce una posizione in uno schema; la collocazione localizza l'esemplare. ILL movimenta un documento in prestito fra biblioteche; document delivery fornisce una riproduzione consentita, con condizioni da verificare.

Fonti lette selettivamente: REICAT introduzione 0.4.3, https://norme.iccu.sbn.it/w/index.php?title=Reicat%2FIntroduzione%2F0.4%2F0.4.3 ; ICCU, paragrafi introduttivi, descrizione bibliografica e authority, https://www.iccu.sbn.it/it/SBN/catalogazione-e-manutenzione-del-catalogo-sbn/le-attivita-di-catalogazione-e-il-protocollo-sbnmarc/index.html ; IFLA, descrizione e presentazione edizioni ISBD, https://www.ifla.org/g/isbd-rg/isbd-editions/ ; BNCF, presentazione Nuovo soggettario, https://thes.bncf.firenze.sbn.it/ . Non attestata lettura integrale dei manuali né validazione di un tracciato MARC eseguibile. Il record didattico originale usa campi leggibili, non simula una notizia SBN autentica; non inventa ISBN o identificativi reali.

Collegamenti: [[topics/m-ir02-universita-afam-fonti-e-profili]], [[entities/ministero-cultura]], [[books/moduli/m-ir02-universita-afam/chapters/09-biblioteche-cataloghi-open-access]].
''',['reicat-accessi.html','iccu-sbnmarc.html','bncf-soggettario.html','ifla-isbd.html'])
append('fonti-ufficiali-m-ir02-universita-afam-2026-07-24','''## Mobilità, tirocini e completamento AFAM — 3 ottobre 2026

Commissione europea, linee guida Learning Agreement for Studies KA131, pagina aggiornata 29 aprile 2024, consultata il 3 ottobre 2026: https://erasmus-plus.ec.europa.eu/resources-and-tools/mobility-and-learning-agreements/learning-agreements/studies-agreement-guidelines-ka131 . Letti accordo preventivo, tabelle A/B, modifiche, transcript e riconoscimento. Il Learning Agreement concorda attività e riconoscimento fra studente e due istituzioni; il Transcript of Records attesta i risultati. Le attività concordate e superate, confermate dal transcript, sono riconosciute senza imporre esami aggiuntivi; non serve corrispondenza uno-a-uno fra ogni insegnamento estero e interno. Cambiamenti approvati vanno conservati, non sovrascritti cancellando la storia. Conversione dei voti distinta dalla somma dei crediti.

Università di Bologna, pagina Tirocini: https://www.unibo.it/it/studiare/verso-il-mondo-del-lavoro/tirocini/tirocini . Letta sezione sull'attivazione, gestione e chiusura curriculare e distinzione extracurriculare. Il caso locale richiede convenzione, attivazione approvata e registro prima dell'ingresso; tutor ospitante attesta presenze e valutazione, ufficio presidia l'iter. Sicurezza e coperture si riferiscono al periodo/attività autorizzati. L'ateneo non è attualmente promotore dei tirocini extracurriculari: non estendere il ruolo curriculare a ogni forma di tirocinio. I valori numerici e le scadenze del laboratorio sono inventati come dati di traccia, non obblighi nazionali.

Letti integralmente D.P.R. 132/2003 artt. 5 e 8, a completamento del controllo AFAM: presidente rappresentante legale salvo attribuzioni del direttore, convoca e presiede CdA; consiglio accademico determina indirizzi e programma attività in rapporto al bilancio e monitora, definisce sviluppo didattica/ricerca/produzione, delibera i regolamenti previsti. URL: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2003-02-28;132~art5!vig= e art8. Confermano la tabella del capitolo 11.
''',['erasmus-la-ka131.html','unibo-tirocini.html','dpr132-art5-current.html','dpr132-art8-current.html'])
print('IR02 fonti biblioteca/mobilità/AFAM consolidate')
