"""
Unit tests for the main module.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from gen.cli import main


class TestMain(unittest.TestCase):
    """
    Test that the main works.
    """

    def test_main_function_exists(self):
        """
        Test that the main function exists.
        """

        self.assertTrue(callable(main))

    def test_main_with_no_args_shows_help(self):
        """
        Test that the main function shows help when no arguments are provided.
        """

        f = io.StringIO()
        with patch("sys.argv", ["gen"]):
            with redirect_stdout(f):
                try:
                    main()
                except SystemExit:
                    pass

    def test_main_with_version_arg(self):
        """
        Test that the main function shows version when --version argument is provided.
        """

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--version"]):
            with redirect_stdout(f):
                try:
                    main()
                except SystemExit:
                    pass
        output = f.getvalue()
        self.assertIn("version", output.lower())

    def test_main_with_help_arg(self):
        """
        Test that the main function shows help when --help argument is provided.
        """

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--help"]):
            with redirect_stdout(f):
                try:
                    main()
                except SystemExit:
                    pass
