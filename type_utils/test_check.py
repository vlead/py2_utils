# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import unittest
from unittest import TestCase
from check import  *

class TestCheck(TestCase):
    TESTING = True
    def test_check(self):
        q = check(lambda y: y > 0, "Type Error: %s not > 0")
        self.assertEqual(q(4), 4)
        self.assertRaises(TypeError, q, -3)

    def test_check2(self):
        q = check2(lambda r: r["x"] > r["y"], "%s not > %s", "x", "y")
        self.assertTrue(q(x=7, y=4))
        self.assertEqual(q(x=7, y=4), {'x':7, 'y':4})
        self.assertRaises(TypeError, q, {'x':3, 'y': 4})


if __name__ == '__main__':
    unittest.main()


