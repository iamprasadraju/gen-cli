"""
Unit tests for the config module.
"""

import unittest

from gen.paths import langs, frameworks


class TestConfig(unittest.TestCase):
    """
    Test that the config works.
    """

    def test_extension_map_exists(self):
        self.assertIsInstance(langs, dict)

    def test_extension_map_has_common_extensions(self):
        self.assertIn(".py", langs.values())
        self.assertIn(".go", langs.values())
        self.assertIn(".js", langs.values())
        self.assertIn(".rs", langs.values())
        self.assertIn(".html", langs.values())

    def test_framework_cmd_exists(self):
        self.assertIsInstance(frameworks, dict)

    def test_framework_jinja_exists(self):
        self.assertIn("flask", frameworks.values())
