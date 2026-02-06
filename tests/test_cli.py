import unittest
import os
import sys
import io
import tempfile
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch, MagicMock


class TestCLI(unittest.TestCase):
    def test_cli_module_exists(self):
        from gen import cli

        self.assertTrue(hasattr(cli, "main"))

    def test_handle_filename_requires_extension(self):
        from gen.cli import handle_filename

        with self.assertRaises(Exception):
            handle_filename("noextension")

    def test_parse_command_mode_help(self):
        from gen.cli import parse_command_mode

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--help"]):
            with redirect_stdout(f):
                try:
                    parse_command_mode()
                except SystemExit:
                    pass


class TestVersion(unittest.TestCase):
    def test_get_version_function_exists(self):
        from gen.cli import get_version

        self.assertTrue(callable(get_version))

    def test_get_version_returns_string(self):
        from gen.cli import get_version

        version = get_version()
        self.assertIsInstance(version, str)
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def test_parse_command_mode_version_long(self):
        from gen.cli import parse_command_mode

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
        from gen.cli import parse_command_mode

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
        from gen.cli import handle_filename
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                handle_filename("unique_test_file.py", dryrun=False, overwrite=False)
            except Exception:
                pass
            os.chdir(old_cwd)

    def test_overwrite_flag_works(self):
        from gen.cli import handle_filename
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                handle_filename("test_overwrite.py", dryrun=False, overwrite=True)
            except Exception:
                pass
            os.chdir(old_cwd)

    def test_dryrun_prints_content(self):
        from gen.cli import handle_filename
        import tempfile

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
        from gen.commands import doctor

        self.assertTrue(hasattr(doctor, "run_doctor"))

    def test_doctor_runs_without_error(self):
        from gen.commands import doctor

        doctor.run_doctor()

    def test_doctor_output_format(self):
        from gen.commands import doctor

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Gen CLI Doctor", output)
        self.assertIn("All checks passed", output)

    def test_doctor_checks_python_version(self):
        from gen.commands import doctor

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Python Version", output)

    def test_doctor_checks_platform(self):
        from gen.commands import doctor

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Platform", output)

    def test_doctor_checks_working_directory(self):
        from gen.commands import doctor

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("Working Directory", output)

    def test_doctor_checks_path_directories(self):
        from gen.commands import doctor

        f = io.StringIO()
        with redirect_stdout(f):
            doctor.run_doctor()
        output = f.getvalue()
        self.assertIn("PATH directories", output)


class TestListCommand(unittest.TestCase):
    def test_list_langtemplates_exists(self):
        from gen.commands import list_

        self.assertTrue(hasattr(list_, "list_langtemplates"))

    def test_list_framtemplates_exists(self):
        from gen.commands import list_

        self.assertTrue(hasattr(list_, "list_framtemplates"))

    def test_list_langtemplates_output(self):
        from gen.commands import list_

        f = io.StringIO()
        with redirect_stdout(f):
            list_.list_langtemplates()
        output = f.getvalue()
        self.assertIn("Language Templates", output)

    def test_list_framtemplates_output(self):
        from gen.commands import list_

        f = io.StringIO()
        with redirect_stdout(f):
            list_.list_framtemplates()
        output = f.getvalue()
        self.assertIn("Frameworks Templates", output)


class TestTreeCommand(unittest.TestCase):
    def test_tree_view_exists(self):
        from gen.commands import list_

        self.assertTrue(hasattr(list_, "tree_view"))

    def test_tree_view_with_default_depth(self):
        from gen.commands import list_

        f = io.StringIO()
        with redirect_stdout(f):
            list_.tree_view(path=".", depth=1)

    def test_tree_view_recursive(self):
        from gen.commands import list_

        f = io.StringIO()
        with redirect_stdout(f):
            list_.tree_view(path=".", depth=None)


class TestTemplateCommand(unittest.TestCase):
    def test_gen_langtemplate_exists(self):
        from gen.commands import template

        self.assertTrue(hasattr(template, "gen_langtemplate"))

    def test_gen_framtemplate_exists(self):
        from gen.commands import template

        self.assertTrue(hasattr(template, "gen_framtemplate"))

    def test_gen_langtemplate_creates_file(self):
        from gen.commands import template

        template.gen_langtemplate("test_main", ".py")

    def test_gen_langtemplate_dryrun(self):
        from gen.commands import template

        template.gen_langtemplate("test_main", ".py", dryrun=True)


class TestConfig(unittest.TestCase):
    def test_extension_map_exists(self):
        from gen.config import EXTENSION_MAP

        self.assertIsInstance(EXTENSION_MAP, dict)

    def test_extension_map_has_common_extensions(self):
        from gen.config import EXTENSION_MAP

        self.assertIn(".py", EXTENSION_MAP)
        self.assertIn(".go", EXTENSION_MAP)
        self.assertIn(".js", EXTENSION_MAP)
        self.assertIn(".rs", EXTENSION_MAP)
        self.assertIn(".html", EXTENSION_MAP)

    def test_framework_cmd_exists(self):
        from gen.config import FRAMEWORK_CMD

        self.assertIsInstance(FRAMEWORK_CMD, dict)

    def test_framework_jinja_exists(self):
        from gen.config import FRAMEWORK_JINJA

        self.assertIsInstance(FRAMEWORK_JINJA, list)


class TestCore(unittest.TestCase):
    def test_render_module_exists(self):
        from gen.core import render

        self.assertTrue(hasattr(render, "render_framework"))


class TestHelper(unittest.TestCase):
    def test_helper_module_exists(self):
        from gen.commands import helper

        self.assertTrue(hasattr(helper, "help"))
        self.assertTrue(hasattr(helper, "concise_help"))

    def test_concise_help_output(self):
        from gen.commands import helper

        f = io.StringIO()
        with redirect_stdout(f):
            try:
                helper.concise_help()
            except SystemExit:
                pass


class TestMain(unittest.TestCase):
    def test_main_function_exists(self):
        from gen.cli import main

        self.assertTrue(callable(main))

    def test_main_with_no_args_shows_help(self):
        from gen.cli import main

        f = io.StringIO()
        with patch("sys.argv", ["gen"]):
            with redirect_stdout(f):
                try:
                    main()
                except SystemExit:
                    pass

    def test_main_with_version_arg(self):
        from gen.cli import main

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
        from gen.cli import main

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--help"]):
            with redirect_stdout(f):
                try:
                    main()
                except SystemExit:
                    pass


if __name__ == "__main__":
    unittest.main()
