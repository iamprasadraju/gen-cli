"""
Unit tests for the core module.
"""

import unittest

from gen.core import render


class TestCore(unittest.TestCase):
    """
    Test that the core works.
    """

    def test_render_module_exists(self):
        """
        Test that the render_framework function exists.
        """

        self.assertTrue(hasattr(render, "render_framework"))
