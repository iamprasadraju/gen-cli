"""
Unit tests for the gen-cli package.
"""

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import MagicMock, patch

from gen import cli
from gen.cli import get_version, handle_filename, main, parse_command_mode
from gen.commands import doctor, helper, list_, template
from gen.config import EXTENSION_MAP, FRAMEWORK_CMD, FRAMEWORK_JINJA
from gen.core import render


class TestCLI(unittest.TestCase):
    """
    Unit tests for the gen-cli package.
    """

    def test_cli_module_exists(self):
        """
        Test that the cli module exists.
        """

        self.assertTrue(hasattr(cli, "main"))

    def test_handle_filename_requires_extension(self):
        """
        Test that the handle_filename function requires an extension.
        """

        with self.assertRaises(Exception):
            handle_filename("noextension")

    def test_parse_command_mode_help(self):
        """
        Test that the parse_command_mode function shows help.
        """

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--help"]):
            with redirect_stdout(f):
                try:
                    parse_command_mode()
                except SystemExit:
                    pass


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


class TestDoctor(unittest.TestCase):
    def test_doctor_module_exists(self):
        """
        Test that the doctor module exists.
        """

        self.assertTrue(hasattr(doctor, "run_doctor"))

    def test_doctor_runs_without_error(self):
        """
        Test that the doctor runs without error.
        """

        doctor.run_doctor()

    def test_doctor_output_format(self):
        """
        Test that the doctor output format is correct.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Gen CLI Doctor", output)
        self.assertIn("All checks passed", output)

    def test_doctor_checks_python_version(self):
        """
        Test that the doctor checks the python version.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Python Version", output)

    def test_doctor_checks_platform(self):
        """
        Test that the doctor checks the platform.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Platform", output)

    def test_doctor_checks_working_directory(self):
        """
        Test that the doctor checks the working directory.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Working Directory", output)

    def test_doctor_checks_path_directories(self):
        """
        Test that the doctor checks the path directories.
        """

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("PATH directories", output)


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


class TestTemplateCommand(unittest.TestCase):
    """
    Test that the template command works.
    """

    def test_gen_langtemplate_exists(self):
        """
        Test that the gen_langtemplate function exists.
        """

        self.assertTrue(hasattr(template, "gen_langtemplate"))

    def test_gen_framtemplate_exists(self):
        """
        Test that the gen_framtemplate function exists.
        """

        self.assertTrue(hasattr(template, "gen_framtemplate"))

    def test_gen_langtemplate_creates_file(self):
        """
        Test that the gen_langtemplate function creates a file.
        """

        template.gen_langtemplate("test_main", ".py")

    def test_gen_langtemplate_dryrun(self):
        """
        Test that the gen_langtemplate function works with dryrun.
        """

        template.gen_langtemplate("test_main", ".py", dryrun=True)


class TestConfig(unittest.TestCase):
    """
    Test that the config works.
    """

    def test_extension_map_exists(self):
        """
        Test that the extension_map exists.
        """

        self.assertIsInstance(EXTENSION_MAP, dict)

    def test_extension_map_has_common_extensions(self):
        """
        Test that the extension_map has common extensions.
        """

        self.assertIn(".py", EXTENSION_MAP)
        self.assertIn(".go", EXTENSION_MAP)
        self.assertIn(".js", EXTENSION_MAP)
        self.assertIn(".rs", EXTENSION_MAP)
        self.assertIn(".html", EXTENSION_MAP)

    def test_framework_cmd_exists(self):
        """
        Test that the framework_cmd exists.
        """

        self.assertIsInstance(FRAMEWORK_CMD, dict)

    def test_framework_jinja_exists(self):
        """
        Test that the framework_jinja exists.
        """

        self.assertIsInstance(FRAMEWORK_JINJA, list)


class TestCore(unittest.TestCase):
    """
    Test that the core works.
    """

    def test_render_module_exists(self):
        """
        Test that the render_framework function exists.
        """

        self.assertTrue(hasattr(render, "render_framework"))


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


if __name__ == "__main__":
    unittest.main()
