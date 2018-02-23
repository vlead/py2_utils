# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

from unittest import TestCase
from pathname import  *


class TestPathName(TestCase):
    TESTING = True
    def test_is_dirname(self):
        print "test_is_dirname"
        self.assertTrue(is_dirname('/'))
        self.assertTrue(is_dirname('.'))
        self.assertTrue(is_dirname('..'))
        self.assertTrue(is_dirname('./'))
        self.assertTrue(is_dirname('../'))
        self.assertTrue(is_dirname('/..'))
        self.assertTrue(is_dirname('/./.'))
        self.assertTrue(is_dirname("a/"))
        self.assertTrue(is_dirname("a//"))
        self.assertTrue(is_dirname("a/."))
        self.assertTrue(is_dirname("a/.."))
        self.assertTrue(is_dirname("a/../b/"))
        self.assertFalse(is_dirname("a/b"))
        self.assertFalse(is_dirname("a"))
        self.assertFalse(is_dirname("a/b//b.txt"))


    def test_to_dirname(self):
        print "test_to_dirname"        
        self.assertEqual(to_dirname('/'), '/')
        self.assertEqual(to_dirname('.'), './')
        self.assertEqual(to_dirname('..'), '../')
        self.assertEqual(to_dirname('./'), './')
        self.assertEqual(to_dirname('../'), '../')
        self.assertEqual(to_dirname('/..'), '/../')
        self.assertEqual(to_dirname('a/'), 'a/')
        self.assertEqual(to_dirname('a//'), 'a//')
        self.assertEqual(to_dirname('a/b'), 'a/b/')
        self.assertEqual(to_dirname('a/b.txt'), 'a/b.txt/')
        self.assertEqual(to_dirname('a/b.txt/..'), 'a/b.txt/../')

    def test_leafname(self):
        print "test_leafname"
        self.assertEqual(leafname('/'), '/')
        self.assertEqual(leafname('a.txt'), 'a.txt')
        self.assertEqual(leafname('a/b'), 'b')
        self.assertEqual(leafname('a/..'), '.')
        self.assertEqual(leafname('a/b/'), 'b')
        self.assertEqual(leafname('a/../'), '.')
        self.assertEqual(leafname('a/.'), 'a')
        self.assertEqual(leafname('//'), '/')
        self.assertEqual(leafname('//./'), '/')
        self.assertEqual(leafname('//..//'), '/')        
        
                
