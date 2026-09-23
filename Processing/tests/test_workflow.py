import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import process_notes as workflow


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.override=patch.object(workflow,'ROOT',self.root)
        self.override.start()
        (self.root/'raw').mkdir()
        (self.root/'prompts').mkdir()
        (self.root/'course_context.md').write_text('Context')

    def tearDown(self):
        self.override.stop()
        self.temp.cleanup()

    def test_prepare_folder_and_no_overwrite(self):
        folder=self.root/'raw/notes/mixed_dates'
        folder.mkdir(parents=True)
        (folder/'one.jpg').write_bytes(b'fixture')
        workflow.prepare(folder)
        self.assertTrue((self.root/'work/batches/notes/mixed_dates/manifest.json').exists())
        with self.assertRaises(ValueError):workflow.prepare(folder)

    def test_no_parent_batch_or_empty(self):
        folder=self.root/'raw/notes'
        folder.mkdir()
        with self.assertRaises(ValueError):workflow.source_manifest(folder)
        (folder/'child').mkdir()
        with self.assertRaises(ValueError):workflow.source_manifest(folder)

    def test_materials_keep_provenance_namespace(self):
        for relative in ['syllabus','assignments/assignment1']:
            folder=self.root/'raw'/relative
            folder.mkdir(parents=True)
            (folder/'one.jpg').write_bytes(b'fixture')
            workflow.prepare(folder)
            self.assertTrue((self.root/'work/batches'/relative/'02_material_review.md').exists())
        self.assertFalse((self.root/'lectures').exists())
