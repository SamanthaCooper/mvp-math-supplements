#!/usr/bin/env python3
"""Check published lesson answer-key structure, references, and math setup."""
from pathlib import Path
import re
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Inspector(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.keys=[];self.current=None;self.depth=0;self.script_text=[];self.in_script=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.append(a['id'])
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='script':self.in_script=True
  if tag=='details' and a.get('id') in ('ready-answer-key','set-answer-key','go-answer-key'):
   self.current={'id':a['id'],'open':'open' in a,'text':'','summaries':0};self.keys.append(self.current);self.depth=1
  elif self.current and tag=='details':self.depth+=1
  if self.current and tag=='summary':self.current['summaries']+=1
 def handle_endtag(self,tag):
  if tag=='script':self.in_script=False
  if self.current and tag=='details':
   self.depth-=1
   if not self.depth:self.current=None
 def handle_data(self,data):
  if self.current:self.current['text']+=data
  if self.in_script:self.script_text.append(data)
def published():
 for index in sorted(ROOT.glob('math-*/module-*/index.html')):
  for filename in sorted(set(re.findall(r'href=["\'](section-[^"\']+\.html)["\']',index.read_text()))):
   if '/' not in filename and 'pending' not in filename:yield index.parent/filename

def check():
 errors=[];count=0;keys=0
 for p in published():
  count+=1;s=p.read_text();d=Inspector();d.feed(s);label=str(p.relative_to(ROOT))
  for part in ('ready','set','go'):
   matched=[k for k in d.keys if k['id']==part+'-answer-key']
   if len(matched)!=1:errors.append(f'{label}: {part} has {len(matched)} answer keys');continue
   k=matched[0];keys+=1
   if k['open']:errors.append(f'{label}: {part} key is not collapsed')
   if k['summaries']!=1 or len(k['text'].strip())<55:errors.append(f'{label}: empty or malformed {part} key')
   if any(c in k['text'] for c in '½¼¾⅓⅔'):errors.append(f'{label}: Unicode fraction in {part} key')
  for href in d.links:
   if href.startswith('#') and href[1:] not in d.ids:errors.append(f'{label}: broken fragment {href}')
  for keyid in ('ready-answer-key','set-answer-key','go-answer-key'):
   if d.ids.count(keyid)>1:errors.append(f'{label}: duplicate {keyid}')
  if any('\\(' in k['text'] or '\\[' in k['text'] for k in d.keys):
   if not re.search(r'<script[^>]+src=["\'][^"\']*(?:mathjax|katex)',s,re.I):errors.append(f'{label}: raw math but no renderer script')
   js=''.join(d.script_text)
   if 'MathJax' in js and "'\\\\('" not in js and '"\\\\("' not in js:errors.append(f'{label}: check escaped MathJax inline delimiters')
 return count,keys,errors
if __name__=='__main__':
 count,keys,errors=check()
 for e in errors:print(e)
 print(f'{count} published lessons; {keys} answer keys; {len(errors)} issues.')
 raise SystemExit(bool(errors))
