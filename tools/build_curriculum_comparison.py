#!/usr/bin/env python3
"""Build a topic-by-topic side-by-side view, preserving the separate curriculum maps."""
from pathlib import Path
import hashlib,html,json
from build_curriculum_map import read_workbook,published_lessons,refs
ROOT=Path(__file__).resolve().parents[1]
def esc(x):return html.escape(str(x),quote=True)
def slug(x):
 import re
 return re.sub('[^a-z0-9]+','-',x.lower()).strip('-')
def main():
 protected=ROOT/'khan-curriculum-map.html';before=hashlib.sha256(protected.read_bytes()).hexdigest()
 khan=json.loads((ROOT/'curriculum-analysis/khan-curriculum-map.json').read_text())
 lessons={l['id']:l for l in khan['lessons']}
 live=published_lessons();mvp={}
 for r in read_workbook()['Curriculum map'][5:]:
  if r and r[0]:mvp[slug(r[0])]={'label':r[0],'scope':r[4] or '', 'introduced':refs(r[1],live),'developed':refs(r[2],live),'practiced':refs(r[3],live)}
 rows=[]
 for t in khan['topics']:
  matches=[mvp[id] for id in t['mvp_match_ids'] if id in mvp]
  joined={}
  for role in ['introduced','developed','practiced']:
   joined[role]=list({(r['course'],r['section'],r['role']):r for m in matches for r in m[role]}.values())
  joined['matches']=[{'label':m['label'],'scope':m['scope']} for m in matches]
  hits=[lessons[id] for id in t['lessons']]
  status=t['comparison_status'] if hits else 'no_khan_match'
  overview=t['id'] in mvp or status=='provisionally_missing'
  rows.append({'id':t['id'],'label':t['label'],'scope':t['scope'],'overview':overview,'status':status,'mvp':joined,'khan':{'first':[lessons[t['first_explanation']]] if t['first_explanation'] else [],'further':[lessons[id] for id in t['further_explanations']],'practice':[lessons[id] for id in t['practice_lessons']],'lesson_count':len(hits),'counts':t['counts']}})
 data={'checked':khan['checked'],'policy':khan['comparison_policy'],'rows':rows}
 (ROOT/'curriculum-analysis/curriculum-comparison.json').write_text(json.dumps(data,indent=2)+'\n')
 payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
 page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MVP and Khan curriculum comparison</title><link rel="stylesheet" href="assets/site.css"><style>
 main{max-width:1700px}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}h1{line-height:1.2}.intro{max-width:100ch}.controls{display:grid;grid-template-columns:2fr 1fr 1.5fr 1fr;gap:16px;margin:24px 0}.controls label{font-weight:650;font-size:.88rem;color:#526179}.controls input,.controls select{display:block;width:100%;padding:10px;border:1px solid #aab8c4;border-radius:6px;font:inherit;margin-top:4px;min-width:0;background:white;color:#172338}.table-wrap{overflow:auto;border:1px solid #dce5eb;border-radius:8px}table{width:100%;table-layout:fixed;border-collapse:collapse;min-width:950px;font-size:.9rem}th,td{padding:16px;vertical-align:top;border-bottom:1px solid #dce5eb;text-align:left}thead th{background:#edf5fa;font-size:1.02rem}thead th:first-child{width:24%}thead th:not(:first-child){width:38%}td:nth-child(2),td:nth-child(3){border-left:1px solid #dce5eb}tbody tr:nth-child(even){background:#fafcfd}.topic{font-weight:700;font-size:1rem}.scope{font-size:.86rem;color:#526179;margin:8px 0}.status{font-size:.82rem;color:#526179;margin:10px 0}.status.gap{color:#8a420d}.role{margin:0 0 13px}.role h3{font-size:.88rem;margin:0 0 4px}.role ul{list-style:none;padding:0;margin:0}.role li{margin:3px 0}.empty{color:#8591a0}.counts,.broader,.filtered-note{font-size:.82rem;color:#526179}.counts{margin:4px 0 8px}details summary{cursor:pointer;color:#145a80;font-size:.85rem;font-weight:600;margin:6px 0}.ref a{font-weight:600}a{color:#145a80}tr[hidden]{display:none}#count{font-size:.9rem;color:#526179}.note{margin:18px 0}.role:last-child{margin-bottom:0}@media(max-width:800px){main{padding:16px}.controls{grid-template-columns:1fr 1fr}table{min-width:900px}th,td{padding:12px}}@media print{.controls{display:none}table{min-width:0}thead{display:table-header-group}details{display:block}}
 </style></head><body><main><nav class="breadcrumbs"><a href="index.html">Home</a> › Curriculum comparison</nav><h1>MVP and Khan: topics side by side</h1><p class="subtitle intro">Compare where the same topics appear in MVP honors and the regular Khan Integrated Math I–III courses. Read across each row; expand a list to see all its locations.</p><p><a href="coverage-mass.html">Estimated coverage mass</a> · <a href="curriculum-map.html">Original MVP map</a> · <a href="khan-curriculum-map.html">Full Khan map and activity links</a></p><div class="note"><strong>Comparison basis:</strong> The current MVP map is the working baseline. Equivalent names and broader entries are matched first; unlisted skills are provisionally missing. MVP’s introduction/development/practice roles come from its map. Khan’s first/further explanations are inferred from course order. Counts describe mapped locations or listed practice skills, not equal amounts of instructional time or questions.</div><div class="controls"><label for="search">Search topics or locations<input id="search" type="search" placeholder="For example, systems, sequences, or probability"></label><label for="course">Course in either curriculum<select id="course"><option value="">All three courses</option><option value="1">Math I</option><option value="2">Math II</option><option value="3">Math III</option></select></label><label for="coverage">Coverage comparison<select id="coverage"><option value="">All comparisons</option><option value="matched">Matched in both maps</option><option value="broader_match">Broader MVP matches</option><option value="provisionally_missing">Provisionally missing from MVP</option><option value="no_khan_match">No identified Khan match</option></select></label><label for="detail">Topic detail<select id="detail"><option value="overview">Broad topics and provisional gaps</option><option value="all">Include finer subskills</option></select></label></div><p id="count" aria-live="polite"></p><div class="table-wrap"><table><caption class="sr-only">Topic-by-topic comparison of MVP and Khan Academy explanations and practice</caption><thead><tr><th scope="col">Topic</th><th scope="col">MVP honors</th><th scope="col">Khan Academy</th></tr></thead><tbody id="body"></tbody></table></div><p class="scope">Source snapshot: October 13, 2026. <a href="https://www.khanacademy.org/math/math1">Khan I</a> · <a href="https://www.khanacademy.org/math/math2">Khan II</a> · <a href="https://www.khanacademy.org/math/math3">Khan III</a>. A topic without an identified Khan match is not a claim that Khan lacks it everywhere. Detailed source activity links remain in the full Khan map.</p></main><script id="comparison-data" type="application/json">PAYLOAD</script><script>
 const data=JSON.parse(document.getElementById('comparison-data').textContent),search=document.getElementById('search'),course=document.getElementById('course'),coverage=document.getElementById('coverage'),detail=document.getElementById('detail');
 const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const courseNo=r=>r.course.replace('math-','');
 const mref=r=>`<span class="ref">${r.href?`<a href="${esc(r.href)}">${esc(r.courseName)} ${esc(r.section)} · ${esc(r.role)}</a>`:`${esc(r.courseName)} ${esc(r.section)} · ${esc(r.role)}`}</span>`;
 const kref=r=>`<a href="${esc(r.url)}">Math ${r.course} · Unit ${r.unit}, Lesson ${r.lesson}</a> <span class="scope">${esc(r.title)}</span>`;
 function list(items,ref){if(!items.length)return '<span class="empty">—</span>';let shown=items.slice(0,3),rest=items.slice(3);return '<ul>'+shown.map(x=>'<li>'+ref(x)+'</li>').join('')+'</ul>'+(rest.length?`<details><summary>${rest.length} more locations</summary><ul>${rest.map(x=>'<li>'+ref(x)+'</li>').join('')}</ul></details>`:'');}
 const role=(title,items,ref)=>`<section class="role"><h3>${esc(title)}</h3>${list(items,ref)}</section>`;
 const labels={mapped:'Matched in both maps',broader_match:'Broader MVP match',provisionally_missing:'Provisionally missing from MVP',no_khan_match:'No identified Khan match',background:'Background'};
 function render(){let q=search.value.trim().toLowerCase(),c=course.value,s=coverage.value,all=detail.value==='all',shown=0;
 document.getElementById('body').innerHTML=data.rows.map(r=>{
 let mr=[...r.mvp.introduced,...r.mvp.developed,...r.mvp.practiced],kr=[...r.khan.first,...r.khan.further,...r.khan.practice];let text=[r.label,r.scope,...mr.map(x=>`${x.courseName} ${x.section} ${x.role}`),...kr.map(x=>`Math ${x.course} Unit ${x.unit} ${x.title}`)].join(' ').toLowerCase();
 const match=(!q||text.includes(q))&&(!c||mr.some(x=>courseNo(x)===c)||kr.some(x=>String(x.course)===c))&&(!s||(s==='matched'?['mapped','broader_match'].includes(r.status):r.status===s))&&(all||r.overview);if(!match)return '';shown++;
 const mf=items=>items.filter(x=>!c||courseNo(x)===c),kf=items=>items.filter(x=>!c||String(x.course)===c);
 let mvpCell=r.mvp.matches.length?(r.status==='broader_match'?`<p class="broader">Mapped under: ${r.mvp.matches.map(x=>esc(x.label)).join('; ')}. These references cover the broader entry, not solely this subskill.</p>`:'')+role('Introduced',mf(r.mvp.introduced),mref)+role('Developed',mf(r.mvp.developed),mref)+role('Practice / review',mf(r.mvp.practiced),mref):'<p class="empty">No matching entry in the current MVP map.</p>';
 if(c&&r.mvp.matches.length&&!mr.some(x=>courseNo(x)===c))mvpCell='<p class="empty">No mapped location in this course.</p>';
 let practice=kf(r.khan.practice),skillCount=new Set(practice.flatMap(x=>x.practice.map(a=>a.url))).size;
 let first=kf(r.khan.first),further=kf(r.khan.further);let khanCell=r.khan.lesson_count?role('First listed explanation',first,kref)+role('Further explanations',further,kref)+`<p class="counts">${skillCount} listed practice ${skillCount===1?'skill':'skills'} in ${practice.length} mapped lesson ${practice.length===1?'group':'groups'}</p>`+role('Practice locations',practice,kref):'<p class="empty">No lesson match identified in these Khan courses.</p>';
 if(c&&r.khan.lesson_count&&!kr.some(x=>String(x.course)===c))khanCell='<p class="empty">No matched lesson group in this course.</p>';
 const countM=new Set(mf(mr).map(x=>`${x.course}:${x.section}:${x.role}`)).size;
 return `<tr id="${esc(r.id)}"><td><div class="topic">${esc(r.label)}</div><p class="scope">${esc(r.scope)}</p><p class="status ${r.status==='provisionally_missing'?'gap':''}">${esc(labels[r.status])}</p><p class="counts">${countM} MVP mapped locations · ${new Set(kf(kr).map(x=>x.id)).size} Khan lesson groups</p><a class="scope" href="khan-curriculum-map.html#${esc(r.id)}">Open full Khan topic</a></td><td>${mvpCell}</td><td>${khanCell}</td></tr>`;
 }).join('');document.getElementById('count').textContent=shown+' topics shown'+(c?' · Locations shown for Math '+c+' in each curriculum':'');}
 for(const el of [search,course,coverage,detail])el.addEventListener(el===search?'input':'change',render);search.value=new URLSearchParams(location.search).get('search')||'';render();
 </script></body></html>'''.replace('PAYLOAD',payload)
 (ROOT/'curriculum-comparison.html').write_text(page)
 assert hashlib.sha256(protected.read_bytes()).hexdigest()==before
 print(f'Built comparison: {len(rows)} topic rows; standalone Khan map unchanged.')
if __name__=='__main__':main()
