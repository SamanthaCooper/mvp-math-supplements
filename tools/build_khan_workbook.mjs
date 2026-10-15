import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=process.argv[2];
if(!root) throw new Error('Pass the repository absolute path as the first argument.');
const data=JSON.parse(await fs.readFile(`${root}/curriculum-analysis/khan-curriculum-map.json`,'utf8'));
const wb=Workbook.create();
const lessons=new Map(data.lessons.map(l=>[l.id,l]));
const topics=new Map(data.topics.map(t=>[t.id,t]));
const loc=id=>{const l=lessons.get(id);return `Math ${l.course} U${l.unit} L${l.lesson}`;};
const status={mapped:'MVP map match',broader_match:'Broader MVP match',provisionally_missing:'Provisionally missing',background:'Background'};
function col(n){let s='';while(n){n--;s=String.fromCharCode(65+n%26)+s;n=Math.floor(n/26);}return s;}
function sheet(name,title,note,headers,rows,widths,tableName){
 const s=wb.worksheets.add(name),last=col(headers.length),end=5+rows.length;
 s.showGridLines=false;s.freezePanes.freezeRows(5);s.freezePanes.freezeColumns(1);
 s.getRange(`A2:${last}2`).format.rowHeight=28;
 s.getRange('A2').values=[[title]];s.getRange('A2').format.font={name:'Arial',size:15,bold:true,color:'#172338'};
 s.getRange('A3').values=[[note]];s.getRange(`A3:${last}3`).format.rowHeight=22;
 s.getRange('A3').format.font={name:'Arial',size:10,color:'#526179'};
 s.getRange(`A5:${last}${end}`).values=[headers,...rows];
 s.getRange(`A5:${last}${end}`).format.font={name:'Arial',size:11,color:'#172338'};
 s.getRange(`A5:${last}${end}`).format.wrapText=true;
 s.getRange(`A5:${last}${end}`).format.verticalAlignment='top';
 const t=s.tables.add(`A5:${last}${end}`,true,tableName);t.style='TableStyleMedium2';
 s.getRange(`A5:${last}5`).format={fill:'#145A80',font:{name:'Arial',size:11,bold:true,color:'#FFFFFF'},rowHeight:34,horizontalAlignment:'center',verticalAlignment:'center',wrapText:true};
 widths.forEach((w,i)=>s.getRange(`${col(i+1)}5:${col(i+1)}${end}`).format.columnWidth=w);
 s.getRange(`A6:${last}${end}`).format.autofitRows();
 return s;
}
const topicRows=data.topics.map(t=>[
 t.label,t.first_explanation?loc(t.first_explanation):'No Khan match listed',t.further_explanations.map(loc).join('; '),t.practice_lessons.map(loc).join('; '),t.mvp_match_ids.map(id=>topics.get(id).label).join('; '),t.lessons.length?status[t.comparison_status]:'No Khan match identified',t.scope
]);
const ts=sheet('Topic map','Khan Academy curriculum map','Regular Integrated Math I–III; October 13, 2026. First/further explanations are inferred from course order. MVP map is the working baseline.',['Topic','First explanation','Further explanations','Practice locations','MVP matching entry','Comparison','Scope'],topicRows,[36,23,44,44,36,25,66],'KhanTopics');
const lessonRows=data.lessons.map(l=>[l.course,l.unit,l.lesson,l.title,l.topic_ids.map(id=>topics.get(id).label).join('; '),l.explanations.filter(a=>a.type==='Video').length,l.explanations.filter(a=>a.type==='Article').length,l.practice.length,l.url]);
const ls=sheet('Lesson coverage','Khan course sequence','44 units; 253 lesson groups. Counts are listed content items, not generated questions or instructional time.',['Math','Unit','Lesson','Lesson group','Related topics','Videos','Articles','Practice skills','Source lesson'],lessonRows,[9,9,9,55,60,10,10,15,90],'KhanLessons');
ls.getRange(`A6:C${5+lessonRows.length}`).setNumberFormat('0');ls.getRange(`F6:H${5+lessonRows.length}`).setNumberFormat('0');
const activityRows=[];
for(const l of data.lessons){for(const a of [...l.explanations,...l.practice])activityRows.push([l.course,l.unit,l.lesson,a.type,a.title,a.url]);}
for(const a of data.assessments){const u=data.units.find(u=>a.url.startsWith(u.url+'/'));activityRows.push([a.course,u?.number??null,null,a.url.includes('course-challenge')?'Course challenge':a.type==='quiz'?'Quiz':'Unit test',a.title,a.url]);}
const as=sheet('Activity references','Teaching, practice and assessment links','Sources: https://www.khanacademy.org/math/math1 ; /math/math2 ; /math/math3. Source links identify every listed item.',['Math','Unit','Lesson','Kind','Activity','Source URL'],activityRows,[9,9,9,20,62,115],'KhanActivities');
as.getRange(`A6:C${5+activityRows.length}`).setNumberFormat('0');
// Use native Excel hyperlinks: the bundled renderer cannot calculate HYPERLINK().
const nativeLinks=[];
for(let i=0;i<lessonRows.length;i++){ls.getRange(`I${i+6}`).values=[['Open lesson']];nativeLinks.push({sheet:2,cell:`I${i+6}`,url:lessonRows[i][8]});}
for(let i=0;i<activityRows.length;i++){as.getRange(`F${i+6}`).values=[['Open source activity']];nativeLinks.push({sheet:3,cell:`F${i+6}`,url:activityRows[i][5]});}
for(let i=0;i<data.topics.length;i++){let t=data.topics[i];if(t.first_explanation)nativeLinks.push({sheet:1,cell:`B${i+6}`,url:lessons.get(t.first_explanation).url});}
await fs.writeFile('/tmp/mvp-khan-map/native-links.json',JSON.stringify(nativeLinks));
wb.recalculate();
const check=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:8},maxChars:1200});
console.log(check.ndjson);
for(const name of ['Topic map','Lesson coverage','Activity references']){
 const s=wb.worksheets.getItem(name); const end=name==='Topic map'?'G8':name==='Lesson coverage'?'I9':'F10';
 const img=await wb.render({sheetName:name,range:`A1:${end}`,scale:1,format:'png'});
 await fs.writeFile(`/tmp/mvp-khan-map/${name.replaceAll(' ','-')}.png`,new Uint8Array(await img.arrayBuffer()));
}
const out=await SpreadsheetFile.exportXlsx(wb);
await out.save(`${root}/curriculum-analysis/khan_curriculum_map.xlsx`);
execFileSync('/Users/scooper/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',[`${root}/tools/add_xlsx_hyperlinks.py`,`${root}/curriculum-analysis/khan_curriculum_map.xlsx`,'/tmp/mvp-khan-map/native-links.json'],{stdio:'inherit'});
await fs.rename(`${root}/curriculum-analysis/khan_curriculum_map.xlsx.inspect.ndjson`,`${root}/authoring/khan-map-workbook-inspection.ndjson`).catch(e=>{if(e.code!=='ENOENT')throw e;});
console.log(`Saved ${data.topics.length} topics, ${lessonRows.length} lessons, ${activityRows.length} activity/assessment references.`);
