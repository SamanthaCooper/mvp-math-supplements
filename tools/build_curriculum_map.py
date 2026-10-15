#!/usr/bin/env python3
"""Build the public curriculum map from the maintained Excel workbook."""
from __future__ import annotations

import json
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKBOOK = ROOT / "mvp_math1-3_complete_curriculum_map.xlsx"
OUTPUT = ROOT / "curriculum-map.html"
ROMAN_TO_COURSE = {"I": "math-1", "II": "math-2", "III": "math-3"}
REF_RE = re.compile(r"(I{1,3})\s+(\d+\.\d+[A-Za-z]?)\s+([^;]+)")


def published_lessons() -> dict[str, str]:
    """Return section identifiers for lesson links actually listed on indexes."""
    result: dict[str, str] = {}
    for index in ROOT.glob("math-*/module-*/index.html"):
        course_dir = index.parents[1].name
        source = index.read_text(encoding="utf-8")
        for href in re.findall(r'href="(section-[^"#]+\.html)"', source):
            match = re.fullmatch(r"section-(\d+)-(\d+[a-z]?)\.html", href)
            if not match:
                continue
            path = index.parent / href
            if not path.is_file() or "pending-cursory-review" in href:
                continue
            section = f"{int(match.group(1))}.{match.group(2).upper()}"
            result[f"{course_dir}:{section}"] = path.relative_to(ROOT).as_posix()
    return result


def refs(value: object, live: dict[str, str]) -> list[dict[str, str]]:
    if not value:
        return []
    result = []
    for match in REF_RE.finditer(str(value)):
        roman, section, role = (part.strip() for part in match.groups())
        course = ROMAN_TO_COURSE[roman]
        result.append({
            "course": course,
            "courseName": f"Math {roman}",
            "module": str(int(section.split(".")[0])),
            "section": section,
            "role": role,
            "href": live.get(f"{course}:{section}", ""),
        })
    return result


def read_workbook() -> dict[str, list[tuple[object, ...]]]:
    """Read the workbook's cached cell values using only Python's standard library."""
    ns = {
        "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        "pkg": "http://schemas.openxmlformats.org/package/2006/relationships",
    }
    with zipfile.ZipFile(WORKBOOK) as archive:
        shared = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            shared = ["".join(t.text or "" for t in si.findall(".//main:t", ns)) for si in root.findall("main:si", ns)]
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        targets = {item.attrib["Id"]: item.attrib["Target"] for item in rels.findall("pkg:Relationship", ns)}
        sheets = {}
        for sheet in workbook.findall("main:sheets/main:sheet", ns):
            target = targets[sheet.attrib[f"{{{ns['rel']}}}id"]]
            path = target.lstrip("/") if target.startswith("/") else f"xl/{target}"
            root = ET.fromstring(archive.read(path))
            result = []
            for row in root.findall(".//main:sheetData/main:row", ns):
                row_number = int(row.attrib["r"])
                while len(result) < row_number - 1:
                    result.append(())
                values: dict[int, object] = {}
                for cell in row.findall("main:c", ns):
                    col = 0
                    for char in re.match(r"[A-Z]+", cell.attrib["r"]).group():
                        col = col * 26 + ord(char) - 64
                    value_node = cell.find("main:v", ns)
                    if cell.attrib.get("t") == "inlineStr":
                        value = "".join(t.text or "" for t in cell.findall(".//main:t", ns))
                    elif value_node is None:
                        value = None
                    elif cell.attrib.get("t") == "s":
                        value = shared[int(value_node.text)]
                    else:
                        value = value_node.text
                    values[col - 1] = value
                result.append(tuple(values.get(i) for i in range(max(values, default=-1) + 1)))
            sheets[sheet.attrib["name"]] = result
    return sheets


def main() -> None:
    workbook = read_workbook()
    live = published_lessons()
    skill_sheet = workbook["Curriculum map"]
    lesson_sheet = workbook["Lesson coverage"]
    skills = []
    for row in skill_sheet[5:]:
        if not row[0]:
            continue
        skills.append({
            "skill": str(row[0]),
            "introduced": refs(row[1], live),
            "developed": refs(row[2], live),
            "practiced": refs(row[3], live),
            "scope": str(row[4] or ""),
        })

    lessons = []
    for row in lesson_sheet[4:]:
        if not row[0]:
            continue
        match = re.fullmatch(r"(I{1,3})\s+(\d+\.\d+[A-Za-z]?)", str(row[0]).strip())
        if not match:
            continue
        roman, section = match.groups()
        course = ROMAN_TO_COURSE[roman]
        module = str(int(section.split(".")[0]))
        lessons.append({
            "course": course,
            "courseName": f"Math {roman}",
            "module": module,
            "section": section,
            "title": str(row[1] or ""),
            "focus": str(row[2] or ""),
            "ready": str(row[3] or ""),
            "set": str(row[4] or ""),
            "go": str(row[5] or ""),
            "pages": str(row[6] or ""),
            "href": live.get(f"{course}:{section}", ""),
        })

    data = json.dumps({"skills": skills, "lessons": lessons}, ensure_ascii=False)
    data = data.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    template = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cumulative Curriculum Map — Math I–III</title><link rel="stylesheet" href="assets/site.css">
<style>
main{max-width:1500px}.map-intro{max-width:72ch}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.controls{display:grid;grid-template-columns:minmax(200px,1fr) repeat(2,minmax(145px,.55fr));gap:12px;margin:20px 0}.controls label{font-size:.88rem;font-weight:700;color:#526179}.controls input,.controls select{display:block;width:100%;min-height:44px;margin-top:4px;padding:8px 10px;border:1px solid #aab8c4;border-radius:6px;font:inherit;color:#172338;background:white}.views{display:flex;gap:8px;margin:20px 0 12px}.views button{padding:10px 16px;border:1px solid #aab8c4;border-radius:6px;background:#fff;color:#145a80;font:inherit;font-weight:700;cursor:pointer}.views button[aria-pressed=true]{background:#145a80;color:#fff;border-color:#145a80}.result-count{color:#526179;font-size:.9rem}.table-wrap{overflow-x:auto;border:1px solid #dce5eb;border-radius:8px}table{width:100%;border-collapse:collapse;min-width:800px;font-size:.9rem}th,td{text-align:left;vertical-align:top;padding:11px 12px;border-bottom:1px solid #dce5eb}th{background:#eff6fa;color:#172338;position:sticky;top:0}tbody tr:last-child td{border-bottom:0}td:first-child{font-weight:700;min-width:190px}.ref{display:inline-block;margin:1px 3px 3px 0;white-space:nowrap}.ref a{font-weight:650}.empty{color:#8591a0}.scope{min-width:230px}.download{margin:20px 0}.map-table[hidden]{display:none}.no-results{padding:20px;color:#526179}.lesson-title{min-width:220px}.lesson-title a{font-weight:700}@media(max-width:700px){.controls{grid-template-columns:1fr}}
</style></head><body><main>
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">›</span><span aria-current="page">Cumulative curriculum map</span></nav>
<div class="eyebrow">Math I · Math II · Math III</div><h1>Cumulative Curriculum Map</h1>
<p class="subtitle map-intro">See where mathematical ideas appear across the three MVP courses, or look up the focus and homework topics for a particular lesson. This map uses the MVP student packets linked on this site. It is an independent reference, not an official MVP document.</p>
<div class="note"><strong>How to read the map:</strong> Each section can introduce, develop, or give students practice with a skill. “Main” refers to the in-class task; Ready, Set, and Go refer to packet homework. A blank introduction means no introduction was verified in the supplied materials.</div>
<div class="controls"><label for="search">Search skills, lesson titles, or topics<input id="search" type="search" placeholder="For example, slope or quadratic"></label><label for="course">Course<select id="course"><option value="">All courses</option><option value="math-1">Secondary Math I</option><option value="math-2">Secondary Math II</option><option value="math-3">Secondary Math III</option></select></label><label for="module">Module<select id="module"><option value="">All modules</option></select></label></div>
<div class="views" role="group" aria-label="Map view"><button type="button" id="skills-view" aria-pressed="true">By skill</button><button type="button" id="lessons-view" aria-pressed="false">By lesson</button></div><p class="result-count" id="result-count" aria-live="polite"></p>
<div class="table-wrap"><table class="map-table" id="skills-table"><caption class="sr-only">Mathematical skills and the lessons where they are introduced, developed, practiced, or reviewed</caption><thead><tr><th scope="col">Mathematical concept or skill</th><th scope="col">Introduced</th><th scope="col">Developed</th><th scope="col">Practiced / reviewed</th><th scope="col">Scope</th></tr></thead><tbody id="skills-body"></tbody></table>
<table class="map-table" id="lessons-table" hidden><caption class="sr-only">Lesson coverage for Math I, Math II, and Math III</caption><thead><tr><th scope="col">Section</th><th scope="col">Lesson</th><th scope="col">Main-task focus</th><th scope="col">Ready</th><th scope="col">Set</th><th scope="col">Go</th><th scope="col">PDF pages</th></tr></thead><tbody id="lessons-body"></tbody></table><p class="no-results" id="no-results" hidden>No matching entries. Try changing your search or filters.</p></div>
<p class="download"><a href="mvp_math1-3_complete_curriculum_map.xlsx" download>Download the complete curriculum map workbook (Excel)</a></p>
<footer>Independent supplementary instruction for students using the Mathematics Vision Project (MVP) curriculum. Not official MVP publisher material; not affiliated with or endorsed by MVP.<p><a href="index.html">Return to home</a></p></footer></main>
<script id="map-data" type="application/json">__DATA__</script><script>
const data=JSON.parse(document.getElementById('map-data').textContent), course=document.getElementById('course'), moduleSelect=document.getElementById('module'), search=document.getElementById('search');
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const refHTML=r=>`<span class="ref" data-course="${r.course}" data-module="${r.module}">${r.href?`<a href="${esc(r.href)}">${esc(r.courseName)} ${esc(r.section)} ${esc(r.role)}</a>`:`${esc(r.courseName)} ${esc(r.section)} ${esc(r.role)}`}</span>`;
const refsHTML=list=>list.length?list.map(refHTML).join(' '):'<span class="empty">—</span>';
document.getElementById('skills-body').innerHTML=data.skills.map((s,i)=>`<tr data-search="${esc([s.skill,s.scope,...s.introduced,...s.developed,...s.practiced].map(x=>typeof x==='string'?x:[x.courseName,x.section,x.role].join(' ')).join(' ').toLowerCase())}"><td>${esc(s.skill)}</td><td>${refsHTML(s.introduced)}</td><td>${refsHTML(s.developed)}</td><td>${refsHTML(s.practiced)}</td><td class="scope">${esc(s.scope)}</td></tr>`).join('');
document.getElementById('lessons-body').innerHTML=data.lessons.map(l=>`<tr data-course="${l.course}" data-module="${l.module}" data-search="${esc([l.section,l.courseName,l.title,l.focus,l.ready,l.set,l.go].join(' ').toLowerCase())}"><td>${l.href?`<a href="${esc(l.href)}">${esc(l.courseName)} ${esc(l.section)}</a>`:`${esc(l.courseName)} ${esc(l.section)}`}</td><td class="lesson-title">${l.href?`<a href="${esc(l.href)}">${esc(l.title)}</a>`:esc(l.title)}</td><td>${esc(l.focus)||'—'}</td><td>${esc(l.ready)||'—'}</td><td>${esc(l.set)||'—'}</td><td>${esc(l.go)||'—'}</td><td>${esc(l.pages)||'—'}</td></tr>`).join('');
let active='skills';
function updateModules(){const c=course.value, found=[...new Set(data.lessons.filter(x=>!c||x.course===c).map(x=>x.module))].sort((a,b)=>+a-+b), old=moduleSelect.value;moduleSelect.innerHTML='<option value="">All modules</option>'+found.map(m=>`<option value="${m}">Module ${m}</option>`).join('');if(found.includes(old))moduleSelect.value=old;}
function filter(){const q=search.value.trim().toLowerCase(),c=course.value,m=moduleSelect.value;let count=0;document.querySelectorAll('#skills-body tr').forEach(row=>{const refs=[...row.querySelectorAll('.ref')];let refMatch=0;refs.forEach(r=>{const ok=(!c||r.dataset.course===c)&&(!m||r.dataset.module===m);r.hidden=!ok;if(ok)refMatch++});const okSearch=!q||row.dataset.search.includes(q),show=okSearch&&refMatch>0;row.hidden=!show;if(active==='skills'&&show)count++});document.querySelectorAll('#lessons-body tr').forEach(row=>{const ok=(!c||row.dataset.course===c)&&(!m||row.dataset.module===m)&&(!q||row.dataset.search.includes(q));row.hidden=!ok;if(active==='lessons'&&ok)count++});document.getElementById('skills-table').hidden=active!=='skills';document.getElementById('lessons-table').hidden=active!=='lessons';document.getElementById('no-results').hidden=count>0;document.getElementById('result-count').textContent=`${count} ${active==='skills'?'skills':'lessons'} shown`;}
function setView(view){active=view;document.getElementById('skills-view').setAttribute('aria-pressed',view==='skills');document.getElementById('lessons-view').setAttribute('aria-pressed',view==='lessons');filter();}
course.addEventListener('change',()=>{updateModules();filter()});moduleSelect.addEventListener('change',filter);search.addEventListener('input',filter);document.getElementById('skills-view').addEventListener('click',()=>setView('skills'));document.getElementById('lessons-view').addEventListener('click',()=>setView('lessons'));updateModules();filter();
</script></body></html>'''
    OUTPUT.write_text(template.replace("__DATA__", data), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({len(skills)} skills, {len(lessons)} lessons; {len(live)} published lesson links)")


if __name__ == "__main__":
    main()
