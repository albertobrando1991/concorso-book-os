import fs from 'node:fs';
import crypto from 'node:crypto';
const [vol, action, a,b,c]=process.argv.slice(2);
const base='artifacts/review-integrale-2026-10-02/';
const lp=base+vol+'-ledger.json';
if(action==='init'){
 const inv=JSON.parse(fs.readFileSync(`artifacts/review-collana-2026-10-02/${vol}-reader.json`,'utf8').replace(/^\uFEFF/,''));
 const chapters=inv.map((x:any)=>{const path='wiki/'+x.file,txt=fs.readFileSync(path,'utf8');return{path,title:x.title,sha256:crypto.createHash('sha256').update(txt).digest('hex'),lines:txt.split('\n').length,words:txt.split(/\s+/).length,readComplete:false,quizReview:'pending',externalClaimsChecked:[],findings:[],limitations:[]};});
 fs.writeFileSync(lp,JSON.stringify({volume:vol,date:'2026-10-02',status:'in-progress',chapters,externalClaimsChecked:[],findings:[],limitations:['PDF e frontmatter delegati al coordinatore.']},null,2));
 console.log(chapters.map((x:any,i:number)=>`${i+1}. ${x.path} (${x.lines} righe, ${x.words} parole)`).join('\n'));
}else{const ledger=JSON.parse(fs.readFileSync(lp,'utf8'));
 if(action==='read'){const ch=ledger.chapters[Number(a)-1];const lines=fs.readFileSync(ch.path,'utf8').split('\n');const start=Number(b)||1,end=Number(c)||lines.length;console.log(ch.path+'\n'+lines.slice(start-1,end).map((x:string,i:number)=>`${i+start}: ${x}`).join('\n'));}
 if(action==='done'){const ch=ledger.chapters[Number(a)-1];ch.readComplete=true;ch.quizReview='complete';ch.findings=(b||'').split('|').filter(Boolean);fs.writeFileSync(lp,JSON.stringify(ledger,null,2));console.log({done:ledger.chapters.filter((x:any)=>x.readComplete).length,total:ledger.chapters.length});}
}
