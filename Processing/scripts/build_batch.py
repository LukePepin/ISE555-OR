"""Build one study/provenance document pair for an entire source folder."""
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

try:
    from .render_notes import document
except ImportError:
    from render_notes import document

ROOT = Path(__file__).resolve().parents[1]
KINDS = ('notes', 'traceability')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def batch_paths(source, root=ROOT):
    folder = Path(source)
    if not folder.is_absolute():
        folder = root / folder
    folder = folder.resolve()
    relative = folder.relative_to((root / 'raw').resolve())
    if not relative.parts or not folder.is_dir():
        raise ValueError('Use an existing input folder inside raw/.')
    return folder, relative, root / 'work/batches' / relative, root / 'final' / relative


def validate_inputs(source, root=ROOT):
    batch, relative, session, out = batch_paths(source, root)
    contents = {}
    for kind in KINDS:
        contents[kind] = (session / f'{kind}.md').read_text()
        if not contents[kind].strip():
            raise ValueError(f'Empty {kind}.md')
    if re.search(r'Documented correction|Additional (?:explanation|information)|IMG_\d|\[UNCLEAR|^\*?Sources?:',
                 contents['notes'], re.I | re.M):
        raise ValueError('Study notes contain provenance labels or unresolved readings; move them to traceability.md.')
    meta = json.loads((session / 'metadata.json').read_text())
    if (root / meta['source_batch']).resolve() != batch:
        raise ValueError('Metadata must reference this exact source folder.')
    expected = sorted(p.name for p in batch.iterdir() if p.is_file() and p.suffix.lower() in {'.jpg','.jpeg','.png','.webp'})
    if not expected or sorted(meta['images']) != expected:
        raise ValueError('Metadata must cover ALL images in the folder exactly once; no date-based subsets.')
    if any(p.is_dir() for p in batch.iterdir()):
        raise ValueError('Select a leaf input folder; nested folders are separate batches.')
    sources = []
    for name in meta['images']:
        if Path(name).name != name:
            raise ValueError('Image names must not contain paths.')
        sources.append({'file': str((batch / name).relative_to(root)), 'sha256': sha(batch / name)})
    return session, contents, meta, sources


def build_batch(source, root=ROOT):
    session, contents, meta, sources = validate_inputs(source, root)
    batch, relative, _, out = batch_paths(source, root)
    local = root / '.tools/tectonic'
    tectonic = str(local) if local.is_file() else shutil.which('tectonic')
    latexmk = shutil.which('latexmk')
    if not tectonic and not latexmk:
        raise ValueError('Install Tectonic or latexmk first.')
    env = os.environ.copy()
    env['XDG_CACHE_HOME'] = str(root / '.tools/cache')
    with tempfile.TemporaryDirectory(prefix='batch-', dir=root / 'work') as tmp:
        stage = Path(tmp)
        (stage / 'figures').mkdir()
        for figure in (root / 'figures').glob('*.pdf'):
            shutil.copyfile(figure, stage / 'figures' / figure.name)
        for kind in KINDS:
            title = meta['course'] + (': ' + meta.get('document_title', 'Lecture Notes') if kind == 'notes' else ': Traceability')
            tex = stage / f'{kind}.tex'
            tex.write_text(document(contents[kind], title, meta.get("display_date", ""), root, layout=meta.get("layout") if kind == "notes" else None, author=meta.get("author", "")))
            command = ([tectonic, '--keep-logs', '--outdir', str(stage), str(tex)] if tectonic else
                       [latexmk, '-pdf', '-interaction=nonstopmode', '-halt-on-error',
                        '-no-shell-escape', '-outdir='+str(stage), str(tex)])
            subprocess.run(command, cwd=stage, env=env, check=True)
            pdf = stage / f'{kind}.pdf'
            if not pdf.is_file() or not pdf.read_bytes().startswith(b'%PDF-'):
                raise ValueError(f'Compiler did not produce {kind}.pdf')
        # Both builds must succeed before replacing either deliverable.
        if out.exists() and any(out.iterdir()):
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
            archive = root / 'work/archive/deliveries' / relative / stamp
            shutil.copytree(out, archive)
            previous_inputs = session / 'build' / 'inputs'
            if previous_inputs.exists():
                shutil.copytree(previous_inputs, archive / 'inputs')
            if (session / 'build_report.json').exists():
                shutil.copyfile(session / 'build_report.json', archive / 'build_report.json')
        out.mkdir(parents=True, exist_ok=True)
        build = session / 'build'
        build.mkdir(exist_ok=True)
        (build / 'inputs').mkdir(exist_ok=True)
        for name in ['notes.md', 'traceability.md', 'metadata.json']:
            shutil.copyfile(session / name, build / 'inputs' / name)
        shutil.copytree(stage / 'figures', build / 'figures', dirs_exist_ok=True)
        for kind in KINDS:
            shutil.copyfile(stage / f'{kind}.pdf', out / f'{kind}.pdf')
            for ext in ['tex', 'log']:
                if (stage / f'{kind}.{ext}').exists():
                    shutil.copyfile(stage / f'{kind}.{ext}', build / f'{kind}.{ext}')
        report = {'source_batch':str(batch.relative_to(root)), 'built_at':datetime.now(timezone.utc).isoformat(),
                  'compiler':tectonic or latexmk, 'source_images':sources,
                  'inputs':{k:sha(session / f'{k}.md') for k in KINDS},
                  'outputs':{k:sha(out / f'{k}.pdf') for k in KINDS},
                  'review':'Compilation completed; semantic and visual review recorded separately.'}
        (session / 'build_report.json').write_text(json.dumps(report, indent=2)+'\n')
    print(f'Delivered: {out}/notes.pdf and traceability.pdf')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', help='raw/notes/FOLDER (all its images form one document)')
    args = parser.parse_args()
    try:
        build_batch(args.folder)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
