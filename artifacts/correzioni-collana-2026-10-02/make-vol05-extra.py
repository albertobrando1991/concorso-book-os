from pathlib import Path
A=Path('artifacts/correzioni-collana-2026-10-02');s=(A/'fetch-vol05.py').read_text(encoding='utf8');i=s.index('groups=');j=s.index('jobs=',i)
groups=[('consob-durata','decreto.legge:2007-12-31;248',['47quater']),('personale','decreto.legislativo:2001-03-30;165',[3]),('arera-nuova','legge:2017-12-27;205',[1])]
s=s[:i]+'groups='+repr(groups)+'\n'+s[j:];s=s.replace("out/'manifest.json'","out/'manifest-governance-extra.json'");(A/'fetch-vol05-governance-extra.py').write_text(s,encoding='utf8')
