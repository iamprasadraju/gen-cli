"""
Unit tests for the list command.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from gen.commands import list_


class TestListCommand(unittest.TestCase):
    def test_list_langtemplates_exists(self):
        """
        Test that the list_langtemplates function exists.
        """

        self.assertTrue(hasattr(list_, "list_langtemplates"))

    def test_list_framtemplates_exists(self):
        """
        Test that the list_framtemplates function exists.
        """

        self.assertTrue(hasattr(list_, "list_framtemplates"))

    def test_list_langtemplates_output(self):
        """
        Test that the list_langtemplates function outputs the correct format.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            list_.list_langtemplates()
        output = f.getvalue()
        self.assertIn("Language Templates", output)

    def test_list_framtemplates_output(self):
        """
        Test that the list_framtemplates function outputs the correct format.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            list_.list_framtemplates()
        output = f.getvalue()
        self.assertIn("Frameworks Templates", output)


class TestTreeCommand(unittest.TestCase):
    def test_tree_view_exists(self):
        """
        Test that the tree_view function exists.
        """

        self.assertTrue(hasattr(list_, "tree_view"))

    def test_tree_view_with_default_depth(self):
        """
        Test that the tree_view function works with default depth.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            list_.tree_view(path=".", depth=1)

    def test_tree_view_recursive(self):
        """
        Test that the tree_view function works recursively.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            list_.tree_view(path=".", depth=None)
