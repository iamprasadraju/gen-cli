"""
Unit tests for the doctor command.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from gen.commands import doctor


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
