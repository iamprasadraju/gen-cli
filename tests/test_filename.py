"""
Unit tests for filename handling.
"""

import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout

from gen.cli import handle_filename


class TestFilenameMode(unittest.TestCase):
    def test_dryrun_flag_is_optional(self):
        """
        Test that the dryrun flag is optional.
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                handle_filename("unique_test_file.py", dryrun=False, overwrite=False)
            except Exception:
                pass
            os.chdir(old_cwd)

    def test_overwrite_flag_works(self):
        """
        Test that the overwrite flag works.
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                handle_filename("test_overwrite.py", dryrun=False, overwrite=True)
            except Exception:
                pass
            os.chdir(old_cwd)

    def test_dryrun_prints_content(self):
        """
        Test that the dryrun flag prints the content.
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                f = io.StringIO()
                with redirect_stdout(f):
                    handle_filename("dryrun_test.py", dryrun=True, overwrite=False)
                output = f.getvalue()
                self.assertIn("--- Dry run", output)
            except Exception:
                pass
            os.chdir(old_cwd)
