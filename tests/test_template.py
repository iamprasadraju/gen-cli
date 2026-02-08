"""
Unit tests for the template command.
"""

import unittest

from gen.commands import template


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
