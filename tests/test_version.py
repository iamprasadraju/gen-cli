"""
Unit tests for the version module.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from gen.cli import get_version, parse_command_mode


class TestVersion(unittest.TestCase):
    """
    Unit tests for the version module.
    """

    def test_get_version_function_exists(self):
        """
        Test that the get_version function exists.
        """

        self.assertTrue(callable(get_version))

    def test_get_version_returns_string(self):
        """
        Test that the get_version function returns a string.
        """

        version = get_version()
        self.assertIsInstance(version, str)
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def test_parse_command_mode_version_long(self):
        """
        Test that the parse_command_mode function shows the version.
        """

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--version"]):
            with redirect_stdout(f):
                try:
                    parse_command_mode()
                except SystemExit:
                    pass
        output = f.getvalue()
        self.assertIn("gen-cli version", output)

    def test_parse_command_mode_version_short(self):
        """
        Test that the parse_command_mode function shows the version.
        """

        f = io.StringIO()
        with patch("sys.argv", ["gen", "-v"]):
            with redirect_stdout(f):
                try:
                    parse_command_mode()
                except SystemExit:
                    pass
        output = f.getvalue()
        self.assertIn("gen-cli version", output)
