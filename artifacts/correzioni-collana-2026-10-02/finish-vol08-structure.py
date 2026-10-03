from pathlib import Path
import re
B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters')
p=next(B.glob('03-*.md'));s=p.read_text(encoding='utf8');a=s.index('### Quiz 5');b=s.index('### Quiz 6',a)
s=s[:a]+'''### Quiz 5

Nel modello indicato, con a positivo e costante, quale termine dominante quadruplica quando n raddoppia?

- A. a.
- B. a·log₂(n).
- C. a·n.
- D. a·n².

**Risposta corretta: D.** a·(2n)²=4a·n². Il modello quadratico è Theta(n²), ma il solo limite O(n²) non dimostra questo rapporto fra costi: qui è specificata la funzione dominante.

'''+s[b:];p.write_text(s,encoding='utf8')
p=next(B.glob('07-*.md'));s=p.read_text(encoding='utf8');m='## N-TR01-07-05';s=s.replace(m,'''### Esempio di rilascio tracciabile

La richiesta R42 corregge il calcolo di una scadenza. Il commit C7 produce l'artefatto con digest H; i test verificano giorno lavorativo, festivo e fine mese. In collaudo si usa proprio H, insieme alla versione documentata dello schema dati. Se un pacchetto diverso viene ricostruito per la produzione, quei risultati non ne attestano automaticamente la qualità. Il responsabile autorizza la promozione di H e registra ambiente, ora ed esito. Prima del passaggio, una migrazione aggiunge un campo mantenendo compatibilità con la versione precedente; solo un rilascio successivo rimuove il vecchio campo dopo il controllo degli utilizzatori. Questa sequenza rende possibile un rollback applicativo senza presumere che ogni modifica distruttiva del database sia reversibile. La verifica finale confronta casi reali autorizzati, errori e tempi con la baseline.

'''+m,1)
m='## N-TR01-07-06';s=s.replace(m,'''**Esempio di capacità.** Una coda riceve 120 richieste al minuto e ne smaltisce 100: in dieci minuti, senza altri cambiamenti, l'arretrato cresce di 200. Aggiungere CPU al frontend non basta se il collo di bottiglia è il limite della dipendenza esterna. Si misura quel tratto e si valuta capacità, ammissione delle richieste e informazione agli utenti.

'''+m,1);p.write_text(s,encoding='utf8')
# Existing open solutions are valid answers, label explicitly without adding artificial MC items.
p=next(B.glob('08-*.md'));s=p.read_text(encoding='utf8').replace('**Soluzione 6.**','**Risposta corretta:** un esempio per l’esercizio 6.').replace('**Soluzione 7.**','**Risposta corretta:** un esempio per l’esercizio 7.');p.write_text(s,encoding='utf8')
p=next(B.glob('13-*.md'));s=p.read_text(encoding='utf8')
start=s.index('#### Elaborato modello:');end=s.index('### Orale',start);block=s[start:end].replace('#### Elaborato modello:', '### Elaborato modello:')
s=s[:start]+s[end:];m='## N-TR01-13-05';s=s.replace(m,block+m,1)
# Put the independent solution beside case theory; retain original simulation prompt with precise internal reference.
start=s.index('#### Soluzione commentata del caso autonomo');end=s.index('#### Prova pratica aggiuntiva',start);block=s[start:end].replace('#### Soluzione commentata', '### Soluzione commentata')
s=s[:start]+'Per il confronto, usa la soluzione commentata del caso autonomo nel nucleo «Caso tecnico: diagnosi, decisione e verifica».\n\n'+s[end:]
m='## N-TR01-13-07';s=s.replace(m,block+m,1)
p.write_text(s,encoding='utf8')
print('Esempi CI/CD e capacità; soluzioni aperte identificate; elaborato e caso ricollocati nei nuclei pertinenti.')
