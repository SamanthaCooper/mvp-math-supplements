#!/usr/bin/env python3
"""Check Module 1 output for escaping errors; does not replace visual review."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MATH = re.compile(r'\\\(.*?\\\)|\\\[.*?\\\]', re.S)


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = False

    def handle_data(self, text):
        if not self.skip:
            self.parts.append(text)


def check(path):
    parser = Text()
    parser.feed(path.read_text())
    errors = []
    for text in parser.parts:
        if re.search(r'[\x00-\x09\x0b-\x1f]', text):
            errors.append('Unexpected control character: ' + repr(text))
        if re.search(r'(?<![\\A-Za-z])(?:qquad|quad|ldots|cdot|div)\b', text):
            errors.append('Possible stripped command: ' + text)
        for math in MATH.findall(text):
            if r'\(' in math[2:-2] or r'\[' in math[2:-2]:
                errors.append('Nested math delimiters: ' + math)
        prose = MATH.sub('', text)
        if any(token in prose for token in (r'\(', r'\)', r'\[', r'\]')):
            errors.append('Unmatched math delimiter: ' + prose)
        if re.search(r'\b[A-Za-z]\([^)]*\)\s*=|\([^)]*\^|\\(?:frac|text|times|le|ldots)\b', prose):
            errors.append('Possible undelimited math: ' + prose)
        if re.search(r'\([A-Za-z]\([A-Za-z]\)\)', prose):
            errors.append('Undelimited function name: ' + prose)
    return errors


if __name__ == '__main__':
    failures = 0
    pages = sorted((ROOT / 'math-1/module-01').glob('section-*.html'))
    for page in pages:
        errors = check(page)
        failures += len(errors)
        for error in errors:
            print(f'{page.name}: {error}')
    print(f'Checked {len(pages)} lessons; {failures} potential escaping errors.')
    raise SystemExit(bool(failures))
