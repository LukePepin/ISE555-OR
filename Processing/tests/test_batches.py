import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from scripts import build_batch
from scripts.render_notes import render


class BatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.day = '2026-09-14'
        self.source = f'raw/notes/{self.day}'
        self.session = self.root / 'work/batches/notes' / self.day
        self.session.mkdir(parents=True)
        (self.root / 'raw/notes' / self.day).mkdir(parents=True)
        (self.root / 'raw/notes' / self.day / 'one.jpg').write_bytes(b'fixture')
        (self.root / 'figures').mkdir()
        (self.root / '.tools').mkdir()
        (self.root / '.tools/tectonic').touch()
        (self.session / 'notes.md').write_text('# Model\n\n## Variables\n\n$x\\ge0$.\n')
        (self.session / 'traceability.md').write_text('# Sources\n\nSource: one.jpg\n')
        (self.session / 'metadata.json').write_text(json.dumps(dict(date=self.day,course='Test',source_batch=f'raw/notes/{self.day}',images=['one.jpg'],date_evidence='image')))

    def tearDown(self):
        self.tmp.cleanup()

    def compile_stub(self, command, **kwargs):
        tex = Path(command[-1])
        tex.with_suffix('.pdf').write_bytes(b'%PDF-test')

    def test_failed_companion_keeps_previous_pair(self):
        out = self.root / 'final/notes' / self.day
        out.mkdir(parents=True)
        for kind in build_batch.KINDS:
            (out / f'{kind}.pdf').write_bytes(b'previous')
        def fail_second(command, **kwargs):
            if Path(command[-1]).stem == 'traceability':
                raise subprocess.CalledProcessError(1, command)
            self.compile_stub(command)
        with patch.object(build_batch.subprocess, 'run', side_effect=fail_second):
            with self.assertRaises(subprocess.CalledProcessError):
                build_batch.build_batch(self.source, self.root)
        self.assertEqual({p.read_bytes() for p in out.iterdir()}, {b'previous'})

    def test_pair_and_archive_use_previous_sources(self):
        with patch.object(build_batch.subprocess, 'run', side_effect=self.compile_stub):
            build_batch.build_batch(self.source, self.root)
            old = (self.session / 'notes.md').read_text()
            (self.session / 'notes.md').write_text('# Updated content\n')
            build_batch.build_batch(self.source, self.root)
        self.assertEqual({p.name for p in (self.root / 'final/notes' / self.day).iterdir()}, {'notes.pdf','traceability.pdf'})
        archived = list((self.root / 'work/archive/deliveries/notes' / self.day).glob('*/inputs/notes.md'))
        self.assertEqual(len(archived),1)
        self.assertEqual(archived[0].read_text(),old)

    def test_no_provenance_in_study_and_required_companion(self):
        (self.session / 'notes.md').write_text('Documented Correction: wrong sign')
        with self.assertRaises(ValueError):
            build_batch.validate_inputs(self.source,self.root)
        (self.session / 'notes.md').write_text('Clean theory')
        (self.session / 'traceability.md').write_text('')
        with self.assertRaises(ValueError):
            build_batch.validate_inputs(self.source,self.root)

    def test_missing_image_rejected_even_if_another_date(self):
        (self.root / self.source / 'two.jpg').write_bytes(b'other date')
        with self.assertRaises(ValueError):
            build_batch.validate_inputs(self.source,self.root)
        meta=json.loads((self.session/'metadata.json').read_text())
        meta['images'].append('two.jpg')
        meta['image_dates']={'one.jpg':'2026-09-14','two.jpg':'2026-09-16'}
        (self.session/'metadata.json').write_text(json.dumps(meta))
        with patch.object(build_batch.subprocess, 'run', side_effect=self.compile_stub):
            build_batch.build_batch(self.source,self.root)
        self.assertEqual(len(list((self.root/'final/notes').iterdir())),1)
        text=render('## Equality\n\n$$\n-\\sum_i P_i\\le-1\n$$\n',self.root)
        self.assertIn(r'-\sum_i P_i\le-1',text)

    def test_folder_identity_not_normalized_date(self):
        for name in ['14_09_2026','2026-09-14']:
            p=self.root/'raw/notes'/name
            p.mkdir(exist_ok=True)
        a=build_batch.batch_paths('raw/notes/14_09_2026',self.root)
        b=build_batch.batch_paths('raw/notes/2026-09-14',self.root)
        self.assertNotEqual(a[2],b[2])
        self.assertNotEqual(a[3],b[3])
