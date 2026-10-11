#!/usr/bin/env python3
"""Refresh publisher links on indexes and the lessons they publish."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
ROMAN = {1: 'I', 2: 'II', 3: 'III'}
BASE = 'https://www.mathematicsvisionproject.org/'
PDF_BASE = BASE + 'uploads/1/1/6/3/11636986/'
PACKETS = {(1,2): 'm1_mod2_se_5_2015f.pdf', (1,3): 'm1_mod3_se_52016f.pdf', **{(2,m): f'm2_mod{m}_se_52017f.pdf' for m in range(2,7)}}
def course_url(course):
    return BASE + 'secondary-mathematics-' + ROMAN[course].lower() + '.html'
def box(course, module=None, section=None):
    name = f'Math {ROMAN[course]}'
    if module is None:
        body = f'<strong>Get the original MVP materials</strong><a href="{course_url(course)}">Official MVP {name} packets and teacher notes</a>'
    else:
        filename = PACKETS.get((course,module))
        if filename is None:
            raise ValueError(f'Verify a publisher student PDF for {course}/{module} before publishing.')
        body = f'<strong>Use this supplement with your MVP packet</strong><a href="{PDF_BASE + filename}">Open {name} · Module {module} student packet (PDF)</a>'
        if section:
            body += f'<span>This supplement accompanies Section {section}.</span>'
        body += f'<a class="publisher-all" href="{course_url(course)}">All MVP {name} materials, including teacher notes and honors editions</a>'
    return '<aside class="publisher-materials" aria-label="Original MVP materials">' + body + '</aside>'
def update(path, markup, lesson=False):
    text = path.read_text()
    text = re.sub(r'<aside class="publisher-materials".*?</aside>', '', text, flags=re.S)
    if lesson:
        if 'publisher-links.css' not in text:
            text = text.replace('</head>', '<link rel="stylesheet" href="../../assets/publisher-links.css"></head>')
        pattern = r'(<p class="meta">.*?</p>)' if 'class="meta"' in text else r'(<p class="subtitle">.*?</p>)'
    else:
        pattern = r'(<p class="subtitle">.*?</p>)'
    text, count = re.subn(pattern, lambda m: m[1] + markup, text, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f'Missing expected header in {path}')
    path.write_text(text)
def main():
    home = ROOT / 'index.html'
    text = home.read_text()
    text = re.sub(r'<section id="mvp-materials">.*?</section>', '', text, flags=re.S)
    block = '<section id="mvp-materials"><h2>Get the MVP packets</h2><p>Use these supplements alongside the corresponding MVP packet. Download the original materials from the publisher:</p><p>' + ' · '.join(f'<a href="{course_url(c)}">Math {ROMAN[c]}</a>' for c in ROMAN) + '</p></section>'
    text = text.replace('<h2 id="about">', block + '<h2 id="about">')
    home.write_text(text)
    count = 0
    for course in ROMAN:
        update(ROOT / f'math-{course}/index.html', box(course))
        for module_index in sorted((ROOT / f'math-{course}').glob('module-*/index.html')):
            module = int(module_index.parent.name.split('-')[1])
            update(module_index, box(course,module))
            links = re.findall(r'href="([^"#]+[.]html)"', module_index.read_text())
            for filename in sorted(set(links)):
                if '/' in filename or filename == 'index.html':
                    continue
                lesson = module_index.parent / filename
                match = re.fullmatch(r'section-(\d+)-(\d+[a-z]?)\.html', filename)
                section = f'{match[1]}.{match[2].upper()}' if match else None
                update(lesson, box(course,module,section), lesson=True)
                count += 1
    print(f'Updated home, course and module indexes, and {count} published lessons/resources.')
if __name__ == '__main__':
    main()
