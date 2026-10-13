#!/usr/bin/env python3
"""Refresh honors packet links throughout the site from the verified packet manifest."""
from pathlib import Path
import json,os,re
ROOT=Path(__file__).resolve().parents[1]
ROMAN={1:'I',2:'II',3:'III'}
BASE='https://www.mathematicsvisionproject.org/'
PDF_BASE=BASE+'uploads/1/1/6/3/11636986/'
PACKETS={(r['course'],r['module']):r['publisher_filename'] for r in json.loads((ROOT/'tools/mvp_packets.json').read_text())}
def course_url(course):
    return f'honors-packets.html#math-{course}'
def box(course,module=None,section=None,depth=0):
    name=f'Math {ROMAN[course]}'
    hub='../'*depth+course_url(course)
    if module is None:
        body=f'<strong>Get the MVP honors materials</strong><a href="{hub}">MVP {name} honors student packets</a>'
    else:
        body=f'<strong>Use this supplement with your MVP honors packet</strong><a href="{PDF_BASE+PACKETS[course,module]}">Open {name} · Module {module} honors student packet (PDF)</a>'
        if section:body+=f'<span>This supplement accompanies Section {section}.</span>'
        body+=f'<a class="publisher-all" href="{hub}">All MVP {name} honors student packets</a>'
    return '<aside class="publisher-materials" aria-label="Original MVP materials">'+body+'</aside>'
def main():
    count=0
    for path in ROOT.rglob('*.html'):
        if any(x in path.relative_to(ROOT).parts for x in ['authoring','.git']):continue
        text=path.read_text();old=text
        # Standard filenames are used by the publisher for modules without separate honors additions.
        for (c,m),filename in PACKETS.items():
            pattern=(rf'm{c}_mod{m}_se(?:h)?_[^/"\s#<>]*\.pdf' if c<3 else rf'sec3mod{m}se(?:h)?[^/"\s#<>]*\.pdf')
            text=re.sub(pattern,filename,text)
        depth=len(path.relative_to(ROOT).parts)-1
        for c,roman in ROMAN.items():
            text=text.replace(BASE+f'secondary-mathematics-{roman.lower()}.html','../'*depth+course_url(c))
            text=text.replace(f'Official MVP Math {roman} packets and teacher notes',f'MVP Math {roman} honors student packets')
            text=text.replace(f'All MVP Math {roman} materials, including teacher notes and honors editions',f'All MVP Math {roman} honors student packets')
        text=text.replace('Get the original MVP materials','Get the MVP honors materials').replace('Use this supplement with your MVP packet','Use this supplement with your MVP honors packet')
        text=re.sub(r'(?<!honors )student packet \(PDF\)', 'honors student packet (PDF)', text, flags=re.I)
        if text!=old:path.write_text(text);count+=1
    print(f'Refreshed honors links on {count} pages.')
if __name__=='__main__':main()
