#!/usr/bin/env python3
"""Exploratory time-budget estimate; does not replace verified practice counts."""
import json,re,statistics,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/'curriculum-analysis'/name).read_text())
def main():
 protected=ROOT/'khan-curriculum-map.html';digest=hashlib.sha256(protected.read_bytes()).hexdigest()
 k=read('khan-curriculum-map.json');comparison=read('curriculum-comparison.json');catalog={t['id']:t for t in k['topics']}
 rows={r['id']:dict(id=r['id'],label=r['label'],status=r['status']) for r in comparison['rows'] if r['overview']}
 # Preserve unmatched background as an explicit budget bucket rather than silently dropping it.
 rows['unassigned-background']={'id':'unassigned-background','label':'Background / outside the broad comparison','status':'background'}
 def canonical(ids):
  out=set()
  for i in ids:
   if i in rows:out.add(i)
   else:out.update(x for x in catalog.get(i,{}).get('mvp_match_ids',[]) if x in rows)
  return sorted(out) or ['unassigned-background']
 components={}
 for r in comparison['rows']:
  if not r['overview']:continue
  for stage in ['introduced','developed','practiced']:
   for ref in r['mvp'][stage]:
    for part in re.findall(r'Main|Ready|Set|Go',ref['role']):
     key=(int(ref['course'].split('-')[1]),ref['section'],part)
     components.setdefault(key,set()).add(r['id'])
 summaries={(r['course'],r['section'],r['component']):r for r in read('packet-coverage.json')['records']}
 pilot={('3.1','Ready'):(30,18,48),('3.1','Set'):(18,10,30),('3.1','Go'):(18,9,30),('3.2','Ready'):(36,24,54),('3.2','Set'):(18,12,30),('3.2','Go'):(24,12,36),('3.6','Ready'):(12,8,20),('3.6','Set'):(35,22,55),('3.6','Go'):(18,12,30)}
 units=[]
 for (course,section,part),topics in sorted(components.items()):
  source=summaries.get((course,section,part),{});summary=source.get('summary','')
  if part=='Main':central,low,high=50,25,90;kind='guided';basis='Generic guided-task allowance; not measured classroom time'
  else:
   kind='practice';central,low,high=24,12,48;basis='Generic homework-component allowance; exercise counts not yet verified'
   if course==1 and (section,part) in pilot:central,low,high=pilot[section,part];basis='Inspected Math I Module 3 problem load; working-time judgment'
  units.append(dict(curriculum='mvp',course=course,key=f'{course}:{section}:{part}',kind=kind,topics=sorted(topics),central=central,low=low,high=high,basis=basis,summary=summary,source=source.get('source_range','')))
 samples=read('coverage-video-samples.json')['samples']
 def minutes(s):a,b=map(int,s.split(':'));return a+b/60
 measured={s['url']:minutes(s['duration']) for s in samples};median=statistics.median(measured.values());seen=set()
 for lesson in k['lessons']:
  topics=canonical(lesson['topic_ids'])
  for a in lesson['explanations']+lesson['practice']:
   key=a['url']
   if key in seen:continue
   seen.add(key)
   typ=a['type']
   if typ=='Video':
    runtime=measured.get(key,median);central=runtime*1.25;low=runtime if key in measured else 2.3;high=runtime*1.5 if key in measured else 15;kind='guided';basis='Measured player duration × pause allowance' if key in measured else 'Sample median video duration × pause allowance'
   elif typ=='Article':central,low,high=5,2,10;kind='guided';basis='Judgment-based reading allowance'
   else:central,low,high=12,6,24;kind='practice';basis='Scenario: four questions per skill, three minutes each (not actual adaptive question count)'
   units.append(dict(curriculum='khan',course=lesson['course'],key=key,title=a['title'],kind=kind,topics=topics,central=central,low=low,high=high,basis=basis))
 data={'checked':'2026-10-13','video_sample_count':len(samples),'median_video_minutes':median,'rows':list(rows.values()),'units':units,'assumptions':{'mvp_main_minutes':[25,50,90],'mvp_homework_minutes':[12,24,48],'khan_questions_per_skill':4,'khan_minutes_per_question':3,'khan_article_minutes':[2,5,10],'khan_video_pause_multiplier':1.25},'allocation':'Each source component/activity has one budget, split equally among its mapped broad topics. These shares are provisional, not verified topic-specific minutes.'}
 (ROOT/'curriculum-analysis/coverage-mass.json').write_text(json.dumps(data,indent=2)+'\n')
 template=(ROOT/'tools/coverage-mass-template.html').read_text()
 (ROOT/'coverage-mass.html').write_text(template.replace('PAYLOAD',json.dumps(data).replace('<','\\u003c')))
 assert hashlib.sha256(protected.read_bytes()).hexdigest()==digest
 for curriculum in ['mvp','khan']:
  selected=[u for u in units if u['curriculum']==curriculum]
  print(curriculum,len(selected),'budget units;',round(sum(u['central'] for u in selected)/60,1),'scenario hours')
if __name__=='__main__':main()
