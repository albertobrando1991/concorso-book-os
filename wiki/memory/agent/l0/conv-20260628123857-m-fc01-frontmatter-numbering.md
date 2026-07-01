# M-FC01 front matter e numerazione

Data: 2026-06-28T12:38:57+02:00

Richiesta: sistemare il modulo M-FC01 per avere, come il libro base, servizi digitali inclusi, frontespizio, copyright e note, sommario, premessa e indice prima dei capitoli; correggere la numerazione per evitare capitoli mostrati come 1.1 o doppi numeri.

Esito:
- creato `front-matter/` con FM1-FM6 per M-FC01;
- spostato il piano editoriale interno in `planning/00-piano-editoriale.md`;
- rimossi i numeri dal campo `title` e dall'H1 dei capitoli 1-14;
- lasciata la numerazione solo in `outline_section`;
- impostate le appendici come `outline_section: A`;
- aggiornato il template modulo con la regola: front matter obbligatorio e titoli senza numero incorporato;
- verificata via API dashboard la sequenza FM1-FM6, capitoli 1-14, appendici A.

Regola da riusare: nei moduli specialistici il corpo libro deve iniziare dai capitoli numerati 1, 2, 3; il piano editoriale non deve stare in `chapters/`.
