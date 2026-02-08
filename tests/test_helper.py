"""
Unit tests for the helper command.
"""

import io
import unittest
from contextlib import redirect_stdout

from gen.commands import helper


class TestHelper(unittest.TestCase):
    """
    Test that the helper works.
    """

    def test_helper_module_exists(self):
        """
        Test that the helper module exists.
        """

        self.assertTrue(hasattr(helper, "help"))
        self.assertTrue(hasattr(helper, "concise_help"))

    def test_concise_help_output(self):
        """
        Test that the concise_help function outputs the correct format.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            try:
                helper.concise_help()
            except SystemExit:
                pass
