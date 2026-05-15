"""
Unit tests for the list command.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from gen.commands import list_
from gen.paths import langs, frameworks


class TestListCommand(unittest.TestCase):
    def test_list_languages_output(self):
        f = io.StringIO()
        with redirect_stdout(f):
            list_.print_list("Language Templates", list(langs.values()))
        output = f.getvalue()
        self.assertIn("Language Templates", output)

    def test_list_frameworks_output(self):
        f = io.StringIO()
        with redirect_stdout(f):
            list_.print_list("Frameworks Templates", list(frameworks.values()))
        output = f.getvalue()
        self.assertIn("Frameworks Templates", output)


class TestTreeCommand(unittest.TestCase):
    def test_tree_view_exists(self):
        self.assertTrue(hasattr(list_, "tree_view"))

    def test_tree_view_with_default_depth(self):
        f = io.StringIO()
        with redirect_stdout(f):
            list_.tree_view(path=".", depth=1)

    def test_tree_view_recursive(self):
        f = io.StringIO()
        with redirect_stdout(f):
            list_.tree_view(path=".", depth=None)
