#!/usr/bin/env python3
"""Add native hyperlink relationships missing from the spreadsheet renderer API."""
import json,sys,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
book=Path(sys.argv[1]);links=json.loads(Path(sys.argv[2]).read_text())
MAIN='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG='http://schemas.openxmlformats.org/package/2006/relationships'
ET.register_namespace('',MAIN);ET.register_namespace('r',REL)
with zipfile.ZipFile(book) as z:parts={n:z.read(n) for n in z.namelist()}
for sheet in sorted({x['sheet'] for x in links}):
 path=f'xl/worksheets/sheet{sheet}.xml';rp=f'xl/worksheets/_rels/sheet{sheet}.xml.rels'
 root=ET.fromstring(parts[path]);rels=ET.fromstring(parts[rp]) if rp in parts else ET.Element(f'{{{PKG}}}Relationships')
 used={r.attrib['Id'] for r in rels};node=root.find(f'{{{MAIN}}}hyperlinks')
 if node is None:
  node=ET.Element(f'{{{MAIN}}}hyperlinks')
  # Hyperlinks precede print/page/drawing/table elements in the worksheet schema.
  after={'sheetPr','dimension','sheetViews','sheetFormatPr','cols','sheetData','sheetCalcPr','sheetProtection','protectedRanges','scenarios','autoFilter','sortState','dataConsolidate','customSheetViews','mergeCells','phoneticPr','conditionalFormatting','dataValidations'}
  index=0
  for i,child in enumerate(root):
   if child.tag.split('}')[-1] in after:index=i+1
  root.insert(index,node)
 for item in [x for x in links if x['sheet']==sheet]:
  num=1
  while f'rIdNativeLink{num}' in used:num+=1
  id=f'rIdNativeLink{num}';used.add(id)
  ET.SubElement(node,f'{{{MAIN}}}hyperlink',{'ref':item['cell'],f'{{{REL}}}id':id})
  ET.SubElement(rels,f'{{{PKG}}}Relationship',{'Id':id,'Type':REL+'/hyperlink','Target':item['url'],'TargetMode':'External'})
 parts[path]=ET.tostring(root,encoding='utf-8',xml_declaration=True);parts[rp]=ET.tostring(rels,encoding='utf-8',xml_declaration=True)
temp=book.with_suffix('.tmp.xlsx')
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as z:
 for name,data in parts.items():z.writestr(name,data)
temp.replace(book)
print(f'Added {len(links)} native Excel hyperlinks.')
