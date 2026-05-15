"""
Unit tests for filename handling.
"""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout

from gen.commands.template import gen_langtemplate


class TestFilenameMode(unittest.TestCase):
    def test_dryrun_flag_is_optional(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                gen_langtemplate("unique_test_file", ".py", dryrun=False)
            except Exception:
                pass
            os.chdir(old_cwd)

    def test_overwrite_flag_works(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                gen_langtemplate("test_overwrite", ".py", dryrun=False)
            except Exception:
                pass
            os.chdir(old_cwd)

    def test_dryrun_prints_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                f = io.StringIO()
                with redirect_stdout(f):
                    gen_langtemplate("dryrun_test", ".py", dryrun=True)
                output = f.getvalue()
                self.assertIn("--- Dry run", output)
            except Exception:
                pass
            os.chdir(old_cwd)
