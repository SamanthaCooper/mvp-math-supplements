#!/usr/bin/env python3
"""Refresh static review badges from the published navigation and lesson notes."""
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tiles = []
        self.reviewed = False
        self.pending = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if tag == 'a' and 'tile' in classes:
            self.tiles.append(attrs.get('href', ''))
        if 'human-review-complete' in classes:
            self.reviewed = True
        if 'review-pending' in classes:
            self.pending = True


def target(page, href):
    if not href or href.startswith(('http:', 'https:', '#')):
        return None
    path = (page.parent / href.split('#')[0]).resolve()
    if not path.is_relative_to(ROOT) or path.suffix != '.html':
        return None
    # Curriculum maps and other navigation tools have no lesson-review status.
    if path.relative_to(ROOT).parts[0] not in ('math-1', 'math-2', 'math-3'):
        return None
    if not path.is_file():
        raise ValueError(f'Missing published target: {path}')
    return path


@lru_cache(None)
def lessons(path):
    if path.name != 'index.html':
        return frozenset([path])
    result = set()
    for href in Page(path.read_text()).tiles:
        child = target(path, href)
        if child:
            result.update(lessons(child))
    return frozenset(result)


def badge(path):
    published = lessons(path)
    reviewed = 0
    for lesson in published:
        page = Page(lesson.read_text())
        if page.reviewed and page.pending:
            raise ValueError(f'Conflicting review markers: {lesson}')
        reviewed += page.reviewed
    total = len(published)
    status = 'complete' if total and reviewed == total else 'partial' if reviewed else 'pending'
    if path.name != 'index.html':
        label = 'Human reviewed' if reviewed else 'Human review pending'
    elif not total:
        label = 'No lessons published'
    else:
        label = ('All human reviewed' if reviewed == total else
                 'Partly human reviewed' if reviewed else 'None human reviewed')
        if 0 < reviewed < total:
            label += f' · {reviewed} of {total}'
    return (f'<span class="review-badge review-badge--{status}" '
            f'data-reviewed="{reviewed}" data-total="{total}">'
            f'<span class="review-dot" aria-hidden="true"></span>{label}</span>')


def main():
    indexes = [ROOT / 'index.html', *sorted(ROOT.glob('math-*/index.html')),
               *sorted(ROOT.glob('math-*/module-*/index.html'))]
    count = 0
    for index in indexes:
        text = index.read_text()
        def replace(match):
            nonlocal count
            opening, content = match.groups()
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', opening))
            if 'tile' not in attrs.get('class', '').split():
                return match.group(0)
            linked = target(index, attrs.get('href', ''))
            if linked is None:
                return match.group(0)
            content = re.sub(r'<span class="review-badge\b[^>]*>.*?</span>.*?</span>',
                             '', content, flags=re.S)
            count += 1
            return opening + content + badge(linked) + '</a>'
        updated = re.sub(r'(<a\b[^>]*>)(.*?)</a>', replace, text, flags=re.S)
        if updated != text:
            index.write_text(updated)
    print(f'Refreshed {count} review badges across {len(indexes)} navigation pages.')


if __name__ == '__main__':
    main()
