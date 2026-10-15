#!/usr/bin/env python3
"""Report verified practice counts separately from uncounted packet summaries."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--topic',default='systems-linear-algebraic',help='Topic ID from curriculum-analysis/topic-catalog.json')
p.add_argument('--course',type=int,choices=[1,2,3])
p.add_argument('--component',choices=['Main','Ready','Set','Go'])
p.add_argument('--search',default='',help='Optional text filter on inherited summaries (not verified skill matching)')
a=p.parse_args()
catalog=json.loads((ROOT/'curriculum-analysis/topic-catalog.json').read_text())
byid={t['id']:t for t in catalog['topics']}
if a.topic not in byid:p.error('Unknown topic ID: '+a.topic)
ids={a.topic}
while True:
 new=ids|{t['id'] for t in byid.values() if t['parent_id'] in ids}
 if new==ids:break
 ids=new
records=json.loads((ROOT/'curriculum-analysis/packet-coverage.json').read_text())['records']
records=[r for r in records if (not a.course or r['course']==a.course) and (not a.component or r['component']==a.component) and (not a.search or a.search.lower() in str(r['summary']).lower())]
hits={}
for r in records:
 for item in r['activities']:
  if item['kind']=='student_exercise' and item['role'] in ['practice','review'] and item.get('required') is True and ids.intersection(item['topic_ids']):
   key=(r['course'],r['section'],r['component'],item['problem'],item['subpart'])
   hits[key]=item
print('Topic:',byid[a.topic]['label'])
print('Verified response units:',len(hits))
print('Distinct numbered problems:',len({k[:4] for k in hits}))
for key in hits: print(f'  Math {key[0]} {key[1]} {key[2]} {key[3]}'+(str(key[4]) if key[4] else ''))
unknown=sum(r['status']!='packet_verified' for r in records)
print(f'Unverified components in selected scope: {unknown} of {len(records)}')
print('This is a verified lower bound, not the curriculum total. Unknown counts are not zero.')
if a.search:
 print('Summary matches (not included in the count):')
 for r in records:
  if r['status']!='packet_verified':print(f"  Math {r['course']} {r['section']} {r['component']}: {r['summary']}")
