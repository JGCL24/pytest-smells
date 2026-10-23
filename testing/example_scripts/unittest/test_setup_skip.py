# mypy: allow-untyped-defs
"""Skipping an entire subclass with unittest.skip() should *not* call setUp from a base class."""

from __future__ import annotations

import unittest


class Base(unittest.TestCase):
    def setUp(self):
        self.setup_done = False


@unittest.skip("skip all tests")
class Test(Base):
    def test_foo(self):
        assert self.setup_done
