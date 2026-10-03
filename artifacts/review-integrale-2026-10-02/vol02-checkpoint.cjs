const fs=require('fs'),crypto=require('crypto');
const root='artifacts/review-integrale-2026-10-02';
const dest=root+'/VOL-02-ledger.json';
const items=JSON.parse(fs.readFileSync('artifacts/review-collana-2026-10-02/VOL-02-reader.json','utf8').replace(/^\uFEFF/,''));
let ledger=fs.existsSync(dest)?JSON.parse(fs.readFileSync(dest,'utf8')):{volume:'VOL-02',reviewStatus:'in-progress',reviewer:'review_vol02',scope:'Originali Markdown, testo, quiz e fonti; PDF affidato al coordinatore',files:items.map(x=>({path:'wiki/'+x.file,sha256:crypto.createHash('sha256').update(fs.readFileSync('wiki/'+x.file)).digest('hex'),readComplete:false,quizReview:'partial',externalClaimsChecked:[],findings:[],limitations:['Lettura integrale da completare']}))};
for(const n of process.argv.slice(2).map(Number)){ledger.files[n].readComplete=true;ledger.files[n].quizReview='complete';ledger.files[n].limitations=['Impaginazione PDF non verificata da questo agente; verifica esterna selettiva dei claim indicati'];}
ledger.updatedAt=new Date().toISOString();
fs.mkdirSync(root,{recursive:true});fs.writeFileSync(dest,JSON.stringify(ledger,null,2)+'\n');
console.log(JSON.stringify({complete:ledger.files.filter(f=>f.readComplete).length,total:ledger.files.length}));
