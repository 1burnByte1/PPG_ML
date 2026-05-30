import json
import pathlib
import re

path = pathlib.Path('d:/PPG_ML/data_cleaning.ipynb')
text = path.read_text(encoding='utf-8')
pattern = re.compile(r'<VSCode\.Cell[^>]*language="(?P<lang>[^"]+)"[^>]*>(?P<source>.*?)</VSCode\.Cell>', re.S)

cells = []
for match in pattern.finditer(text):
    lang = match.group('lang')
    source = match.group('source')
    # Strip a leading newline if present
    if source.startswith('\n'):
        source = source[1:]
    # Remove trailing newline at end if present
    if source.endswith('\n'):
        source = source[:-1]
    lines = source.split('\n')
    if lang == 'python':
        cells.append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': [line + '\n' for line in lines],
        })
    elif lang == 'markdown':
        cells.append({
            'cell_type': 'markdown',
            'metadata': {},
            'source': [line + '\n' for line in lines],
        })
    else:
        cells.append({
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': [line + '\n' for line in lines],
        })

nb = {
    'cells': cells,
    'metadata': {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'name': 'python',
            'version': '3.x'
        }
    },
    'nbformat': 4,
    'nbformat_minor': 5
}

out_path = pathlib.Path('d:/PPG_ML/data_cleaning_fixed.ipynb')
out_path.write_text(json.dumps(nb, indent=2), encoding='utf-8')
print(f'Wrote {out_path} with {len(cells)} cells')
