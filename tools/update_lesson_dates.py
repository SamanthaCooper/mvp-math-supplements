#!/usr/bin/env python3
"""Stamp lesson headers and footers using Git history, or today's date for edited/new lessons."""
from datetime import datetime, date
from zoneinfo import ZoneInfo
from pathlib import Path
import argparse, re, subprocess
ROOT = Path(__file__).resolve().parents[1]
STAMP = re.compile(r'<p class="lesson-updated(?: lesson-updated--top)?">.*?</p>\s*', re.S)
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()
def lessons():
    paths = set()
    for index in ROOT.glob('math-*/module-*/index.html'):
        for name in re.findall(r'href=["\'](section-[^"\']+\.html)["\']', index.read_text()):
            if '/' not in name:
                paths.add(index.parent / name)
    for p in ROOT.glob('math-*/module-*/section-*-pending-cursory-review.html'):
        if 'publisher-links.css' in p.read_text():
            paths.add(p)
    return sorted(paths)
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='*', help='Explicit lessons to stamp with today’s date')
    parser.add_argument('--preserve-dates', action='store_true', help='Update placement without changing existing dates')
    args = parser.parse_args()
    today = datetime.now(ZoneInfo('America/Los_Angeles')).date().isoformat()
    changed = set(git('diff', '--name-only', 'HEAD').splitlines())
    paths = [ROOT / name for name in args.paths] if args.paths else lessons()
    count = 0
    for p in paths:
        rel = str(p.relative_to(ROOT))
        previous = git('log', '-1', '--format=%cs', '--', rel)
        stamp = today if args.paths or rel in changed or not previous else previous
        existing = re.search(r'<p class="lesson-updated[^"]*">Last updated <time datetime="([^"]+)"', p.read_text())
        if args.preserve_dates and existing:
            stamp = existing.group(1)
        value = date.fromisoformat(stamp)
        label = f'{value:%B} {value.day}, {value.year}'
        s = STAMP.sub('', p.read_text())
        footer = f'<p class="lesson-updated">Last updated <time datetime="{stamp}">{label}</time>.</p>\n'
        top = footer.replace('class="lesson-updated"', 'class="lesson-updated lesson-updated--top"')
        s, inserted = re.subn(r'(<main\b[^>]*>)', lambda m: m.group(1) + top, s, count=1)
        assert inserted == 1, rel
        assert '</main>' in s, rel
        s = s.replace('</main>', footer + '</main>', 1)
        if s != p.read_text():
            p.write_text(s)
            count += 1
    print(f'Updated dates on {count} of {len(paths)} lessons.')
if __name__ == '__main__':
    main()
