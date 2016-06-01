#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest


class TestMountain(unittest.TestCase):

    def setUp(self):
        pass

    def test_it_is_true(self):
        self.assertTrue(1 == 0)
        #self.assertTrue(1 != 0)

    def test_it_is_false(self):
        self.assertFalse(1 == 0)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestMountain))
    return suite

if __name__ == '__main__':
    res = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(0)
