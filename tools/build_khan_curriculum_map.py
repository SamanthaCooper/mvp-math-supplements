#!/usr/bin/env python3
"""Build the Khan curriculum map from captured public outlines and reviewed topic alignments."""
from pathlib import Path
from collections import Counter
import json,html,re
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'curriculum-analysis'
def esc(s):return html.escape(str(s),quote=True)
def source_link(title,url):return f'<a href="{esc(url)}">{esc(title)}</a>'
def main():
 source=json.loads((DATA/'khan-course-outline.json').read_text())
 catalog=json.loads((DATA/'topic-catalog.json').read_text())
 topics={t['id']:dict(t,lessons=[]) for t in catalog['topics']}
 aligned=json.loads((DATA/'khan-lesson-alignment.json').read_text())
 by_lesson={(a['course'],a['lesson_order']):a for a in aligned}
 lessons=[];units=[];assessments=[]
 for c in source['courses']:
  umap={u['url']:dict(u,course=c['course'],number=int(re.search(r'UNIT (\d+)',u['title'])[1]),title=u['title'].split('\n',1)[1]) for u in c['units']}
  for u in umap.values():u['assessments']=[]
  for a in c['assessments']:
   a=dict(a,course=c['course']);assessments.append(a)
   unit_url='https://www.khanacademy.org'+'/'.join(a['url'].split('khanacademy.org')[1].split('/')[:4])
   if unit_url in umap:umap[unit_url]['assessments'].append(a)
  for n,l in enumerate(c['lessons'],1):
   a=by_lesson[c['course'],n];assert a['lesson_title']==l['title']
   url=a['lesson_url'];unit_url=url.rsplit('/',1)[0];unit=umap[unit_url]
   lesson_order=1+sum(x['course']==c['course'] and x['unit']==unit['number'] for x in lessons)
   teaching=list({x['url']:x for x in l['activities'] if x['type'] in ['Video','Article']}.values())
   practice=list({x['url']:x for x in l['activities'] if x['type']=='Exercise'}.values())
   item={'id':f"khan-{c['course']}-{unit['number']}-{lesson_order}",'course':c['course'],'unit':unit['number'],'unit_title':unit['title'],'lesson':lesson_order,'course_order':n,'title':l['title'],'url':url,'topic_ids':a['topic_ids'],'explanations':teaching,'practice':practice,'alignment_basis':a['basis'],'prerequisite_for':a.get('prerequisite_for',[])}
   lessons.append(item)
   # Normalize finer names to their reviewed broader MVP matches as well.
   related=list(item['topic_ids'])
   for id in item['topic_ids']:
    related.extend(topics[id].get('mvp_match_ids',[]))
   item['topic_ids']=list(dict.fromkeys(related))
   for id in item['topic_ids']:topics[id]['lessons'].append(item['id'])
  units.extend(umap.values())
 assert len(lessons)==len(aligned)==253 and len(units)==44
 byid={l['id']:l for l in lessons}
 for t in topics.values():
  hits=[byid[id] for id in t['lessons']]
  teaching=[l for l in hits if l['explanations'] and t['id'] not in l['prerequisite_for']]
  t['first_explanation']=teaching[0]['id'] if teaching else None
  t['further_explanations']=[l['id'] for l in teaching[1:]]
  t['practice_lessons']=[l['id'] for l in hits if l['practice']]
  t['counts']={'lesson_groups':len(hits),'explanation_items':len({a['url'] for l in hits for a in l['explanations']}),'practice_skills':len({a['url'] for l in hits for a in l['practice']})}
 counts={'units':len(units),'lesson_groups':len(lessons),'videos':sum(a['type']=='Video' for l in lessons for a in l['explanations']),'articles':sum(a['type']=='Article' for l in lessons for a in l['explanations']),'practice_skills':sum(len(l['practice']) for l in lessons),'assessments':len(assessments)}
 result={'schema_version':1,'checked':source['checked'],'scope':'Regular Khan Integrated Math I, II, III (not Illustrative Mathematics-aligned courses).','comparison_policy':catalog['comparison_policy'],'stage_rule':'First explanation means the earliest listed lesson group with videos or articles for the matched topic, in course order I–III. Further explanations are later listed groups. These are inferred inventory roles, not verified claims about prerequisite mastery or classroom introduction.','count_rule':'Counts are listed videos/articles/practice skills, not video minutes, generated questions, classroom time, or MVP exercise equivalents. Topic counts cover entire matched lesson groups; related topics can overlap, so do not sum topic counts. Deduplicate within a topic by source URL.','counts':counts,'units':units,'lessons':lessons,'topics':list(topics.values()),'assessments':assessments}
 (DATA/'khan-curriculum-map.json').write_text(json.dumps(result,indent=2)+'\n')
 cards=[]
 status_labels={'mapped':'MVP map match','broader_match':'Broader MVP match','provisionally_missing':'Provisionally missing from MVP','background':'Background'}
 for t in topics.values():
  hits=[byid[id] for id in t['lessons']]
  def loc(l):return f"Math {l['course']} · Unit {l['unit']}, Lesson {l['lesson']}: {l['title']}"
  def loclist(ids):return '<ul>'+''.join('<li>'+source_link(loc(byid[id]),byid[id]['url'])+'</li>' for id in ids)+'</ul>'
  first=source_link(loc(byid[t['first_explanation']]),byid[t['first_explanation']]['url']) if t['first_explanation'] else 'No listed Khan explanation mapped.'
  comparison=t['comparison_status'] if hits else 'not_mapped_in_khan'
  label=status_labels.get(comparison,'No Khan lesson match in this map')
  mvp_matches=[topics[id] for id in t.get('mvp_match_ids',[])]
  mvp='<p>'+esc(label)+'</p>'
  if mvp_matches:
   for m in mvp_matches:
    mvp+='<p><strong>'+source_link(m['label'],'curriculum-map.html')+'</strong></p>'
    mvp+='<details><summary>MVP map references</summary>'+''.join('<p><strong>'+esc(e['role'].replace('_',' '))+':</strong> '+esc(e['reference'])+'</p>' for e in m['mvp_evidence'])+'</details>'
  if comparison=='provisionally_missing':mvp+='<p>'+esc(t['matching_basis'])+'</p>'
  elif comparison=='broader_match':mvp+='<p>Grouped under a broader map entry; finer coverage will be revisited as packets are inventoried.</p>'
  detail=''
  for l in hits:
   def activities(items):return '<ul>'+''.join('<li>'+source_link(a['title'],a['url'])+' <small>('+esc(a['type'].lower())+')</small></li>' for a in items)+'</ul>'
   detail+='<section class="lesson"><h4>'+source_link(loc(l),l['url'])+'</h4>'
   if l['explanations']:detail+='<h5>Videos and articles</h5>'+activities(l['explanations'])
   if l['practice']:detail+='<h5>Practice skills</h5>'+activities(l['practice'])
   detail+='</section>'
  later='<details><summary>'+str(len(t['further_explanations']))+' further explanation groups</summary>'+loclist(t['further_explanations'])+'</details>' if t['further_explanations'] else ''
  prac='<details><summary>'+str(t['counts']['practice_skills'])+' practice skills in '+str(len(t['practice_lessons']))+' mapped lesson groups</summary>'+loclist(t['practice_lessons'])+'</details>' if t['practice_lessons'] else '<p>No listed Khan practice mapped.</p>'
  search=' '.join([t['label'],t['scope'],*[l['title'] for l in hits],*[a['title'] for l in hits for a in l['explanations']+l['practice']]])
  cards.append(f'<article id="{esc(t["id"])}" data-courses="{" ".join(str(c) for c in sorted({l["course"] for l in hits}))}" data-status="{comparison}" data-search="{esc(search.lower())}"><h2>{esc(t["label"])}</h2><p class="scope">{esc(t["scope"])}</p><div class="topic-grid"><section><h3>First listed explanation</h3><p>{first}</p>{later}{prac}</section><section><h3>MVP comparison</h3>{mvp}</section></div>'+('<details class="activity-detail"><summary>All '+str(len(hits))+' Khan lesson groups and their source activities</summary>'+detail+'</details>' if hits else '')+'</article>')
 unit_cards=[]
 for u in units:
  hits=[l for l in lessons if l['course']==u['course'] and l['unit']==u['number']]
  links=''.join('<li>'+source_link(f"Lesson {l['lesson']}: {l['title']}",l['url'])+' — '+esc(topics[l['topic_ids'][0]]['label'])+f" ({len(l['explanations'])} explanations, {len(l['practice'])} practice skills)</li>" for l in hits)
  assess=''.join('<li>'+source_link(a['title'],a['url'])+'</li>' for a in u['assessments'])
  unit_cards.append(f'<section class="unit" data-course="{u["course"]}"><h2>'+source_link(f"Math {u['course']} · Unit {u['number']}: {u['title']}",u['url'])+'</h2><ol>'+links+'</ol>'+('<details><summary>Quizzes and unit tests</summary><ul>'+assess+'</ul></details>' if assess else '')+'</section>')
 css='''*{box-sizing:border-box}body{margin:0;background:#f6f8fa;color:#172338;font:17px/1.6 system-ui}main{max-width:1500px;margin:auto;padding:32px}h1{line-height:1.2}h2{font-size:1.3rem;margin:0 0 10px}h3{font-size:1rem}h4{font-size:1.05rem}h5{font-size:1rem;margin:12px 0}a{color:#145a80}small,.scope,.note{color:#526179}.intro{background:#edf5fa;padding:18px}.filters{display:grid;grid-template-columns:2fr 1fr 1.5fr 1fr;gap:16px;margin:24px 0}label{font-weight:650;font-size:.85rem}input,select{width:100%;padding:10px;border:1px solid #bcc9d5;border-radius:5px;font:inherit;min-width:0}article,.unit{background:white;border:1px solid #dce5eb;border-radius:8px;padding:22px;margin:18px 0}.topic-grid{display:grid;grid-template-columns:1fr 1fr;gap:32px}summary{cursor:pointer;color:#145a80;padding:6px 0;font-weight:600}details p{margin:8px 0}.lesson{border-top:1px solid #dce5eb;padding:12px 0}li{margin:6px 0}#unit-view[hidden],#topic-view[hidden],article[hidden],.unit[hidden]{display:none}@media(max-width:850px){main{padding:16px}.filters,.topic-grid{grid-template-columns:1fr}}@media print{.filters{display:none}article{break-inside:avoid}}'''
 head=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Khan Academy curriculum map</title><style>{css}</style></head><body><main><nav><a href="index.html">Home</a> · <a href="curriculum-map.html">MVP curriculum map</a></nav><h1>Khan Academy curriculum map</h1><p>Integrated Math I–III · Regular courses · Source outlines checked {esc(source['checked'])}</p><div class="intro"><p>Browse the full course sequence or follow a topic across courses. Videos/articles, practice skills, and assessments are recorded separately. This map contains {counts['units']} units, {counts['lesson_groups']} lesson groups, and {counts['practice_skills']} listed practice skills.</p><p>For comparison, the current MVP honors map is treated as correct. Different names and broader entries are matched first; an unlisted skill is provisionally missing. Packet-level verification is deferred.</p><p>“First listed explanation” is inferred from course order, not a claim that students have never met the idea before. Item counts describe Khan’s inventory, not instructional time or numbers of generated questions. Topic counts cover the entire matched lesson groups, which can overlap; they are not counts of questions devoted exclusively to one skill.</p></div><p class="note">Sources: <a href="https://www.khanacademy.org/math/math1">Khan Math I</a> · <a href="https://www.khanacademy.org/math/math2">Khan Math II</a> · <a href="https://www.khanacademy.org/math/math3">Khan Math III</a>. Activity names and links identify original Khan content; descriptions and MVP alignments are this project’s working analysis.</p><div class="filters"><label>Search topics or activities<input id="search" placeholder="For example, systems or expected value"></label><label>Khan course<select id="course"><option value="all">All courses</option><option value="1">Math I</option><option value="2">Math II</option><option value="3">Math III</option></select></label><label>MVP comparison<select id="comparison"><option value="all">All topics</option><option value="mapped">Map match</option><option value="broader_match">Broader match</option><option value="provisionally_missing">Provisionally missing from MVP</option><option value="not_mapped_in_khan">MVP topics with no Khan match</option><option value="background">Background</option></select></label><label>View<select id="view"><option value="topics">By topic</option><option value="units">Khan course sequence</option></select></label></div><p id="count" aria-live="polite"></p><div id="topic-view">'''
 script='''<script>const topicCards=[...document.querySelectorAll('article')],units=[...document.querySelectorAll('.unit')],search=document.getElementById('search'),course=document.getElementById('course'),comparison=document.getElementById('comparison'),view=document.getElementById('view');function filter(){let q=search.value.toLowerCase().trim(),c=course.value,s=comparison.value,v=view.value;document.getElementById('topic-view').hidden=v!=='topics';document.getElementById('unit-view').hidden=v!=='units';comparison.disabled=v==='units';for(const el of topicCards)el.hidden=!(el.dataset.search.includes(q)&&(c==='all'||el.dataset.courses.split(' ').includes(c))&&(s==='all'||el.dataset.status===s));for(const el of units)el.hidden=!(el.textContent.toLowerCase().includes(q)&&(c==='all'||el.dataset.course===c));let active=v==='topics'?topicCards:units;document.getElementById('count').textContent=active.filter(x=>!x.hidden).length+(v==='topics'?' matching topics':' matching units');}for(const el of [search,course,comparison,view])el.addEventListener(el===search?'input':'change',filter);const params=new URLSearchParams(location.search);search.value=params.get('search')||'';filter();</script>'''
 (ROOT/'khan-curriculum-map.html').write_text(head+''.join(cards)+'</div><div id="unit-view" hidden>'+''.join(unit_cards)+'</div>'+script+'</main></body></html>')
 print(counts)
if __name__=='__main__':main()
