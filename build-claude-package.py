"""Build the Claude upload archive from the shared skill source."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
SKILL = ROOT / 'skills' / 'pick-and-design'
DESCRIPTION = ('Research and build distinctive web UI/UX with live references, UX principles, '
               'visual directions and a maintained design system. Use for websites, web apps and web motion.')
assert len(DESCRIPTION) <= 200
entries = {}
for path in sorted(SKILL.rglob('*')):
    if not path.is_file() or any(x in path.parts for x in ('.git', '__pycache__')) or path.name == '.DS_Store' or path.suffix == '.pyc':
        continue
    data = path.read_bytes()
    if path == SKILL / 'SKILL.md':
        lines = data.decode().splitlines(keepends=True)
        assert lines[0].strip() == '---'
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
        indices = [i for i in range(1, end) if lines[i].startswith('description:')]
        assert len(indices) == 1
        lines[indices[0]] = 'description: ' + DESCRIPTION + '\n'
        data = ''.join(lines).encode()
    entries['pick-and-design/' + path.relative_to(SKILL).as_posix()] = data
for name in ('LICENSE', 'NOTICE', 'VERSION'):
    entries['pick-and-design/' + name] = (ROOT / name).read_bytes()
output = ROOT / 'pick-and-design-claude.zip'
with ZipFile(output, 'w', compression=ZIP_DEFLATED) as archive:
    for name, data in sorted(entries.items()):
        info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, data)
with ZipFile(output) as archive:
    assert archive.testzip() is None
    assert 'pick-and-design/SKILL.md' in archive.namelist()
    assert all(archive.read(name) == data for name, data in entries.items())
print(f'Built and verified {output.name}: {len(entries)} files')
