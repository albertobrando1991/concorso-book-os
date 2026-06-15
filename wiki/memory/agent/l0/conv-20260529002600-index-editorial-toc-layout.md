# 2026-05-29 - Indice editoriale con puntini guida e numeri pagina

Richiesta: rendere l'indice piu simile a un indice editoriale professionale, con struttura a capitoli e sottocapitoli, numerazione progressiva e numeri di pagina, occupando meglio la pagina.

Interventi:
- sostituito il layout compatto a tag con righe tipografiche dedicate;
- introdotti blocchi `index-part`, `index-chapter` e `index-row`;
- aggiunta numerazione dei sottocapitoli nel formato `1.1`, `1.2`, ecc.;
- aggiunti puntini guida e colonna pagina allineata a destra;
- stimati i numeri pagina dei capitoli e dei sottocapitoli a partire dalla paginazione dei blocchi;
- regolata la stima di impaginazione per riempire la pagina senza sovrapporsi al footer.

Verifiche:
- `npm test -- book-preview.test.ts`
- `npm run typecheck`
- `npm run build`
- `git diff --check`
- Playwright headless su `http://127.0.0.1:3000/`: dashboard visibile, CSS applicato, indice con 13 capitoli, 116 righe sottocapitolo e numeri pagina visibili.
