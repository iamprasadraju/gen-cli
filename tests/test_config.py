"""
Unit tests for the config module.
"""

import unittest

from gen.config import EXTENSION_MAP, FRAMEWORK_CMD, FRAMEWORK_JINJA


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
