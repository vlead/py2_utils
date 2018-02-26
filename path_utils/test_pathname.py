# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

from unittest import TestCase
from path import  *


class TestPathName(TestCase):
    TESTING = True
    def test_is_path(self):
        print "test_is_path"
        self.assertTrue(is_path('/'))
        self.assertTrue(is_path('.'))
        self.assertTrue(is_path('..'))
        self.assertTrue(is_path('./'))        
        self.assertFalse(is_path('//'))
        self.assertTrue(is_path('///'))
        self.assertTrue(is_path('/a.txt'))
        self.assertFalse(is_path(5))
        self.assertFalse(is_path(['a']))
        self.assertFalse(is_path(True))
        
    def test_is_dirpath(self):
        print "test_is_dirpath"
        self.assertTrue(is_dirpath('/'))
        self.assertTrue(is_dirpath('.'))
        self.assertTrue(is_dirpath('..'))
        self.assertTrue(is_dirpath('./'))
        self.assertTrue(is_dirpath('../'))
        self.assertTrue(is_dirpath('/..'))
        self.assertTrue(is_dirpath('/./.'))
        self.assertTrue(is_dirpath("a/"))
        self.assertTrue(is_dirpath("a//"))
        self.assertTrue(is_dirpath("a/."))
        self.assertTrue(is_dirpath("a/.."))
        self.assertTrue(is_dirpath("a/../b/"))
        self.assertFalse(is_dirpath("a/b"))
        self.assertFalse(is_dirpath("a"))
        self.assertFalse(is_dirpath("a/b//b.txt"))


    def test_to_dirpath(self):
        print "test_to_dirpath"        
        self.assertEqual(to_dirpath('/'), '/')
        self.assertEqual(to_dirpath('.'), './')
        self.assertEqual(to_dirpath('..'), '../')
        self.assertEqual(to_dirpath('./'), './')
        self.assertEqual(to_dirpath('../'), '../')
        self.assertEqual(to_dirpath('/..'), '/../')
        self.assertEqual(to_dirpath('a/'), 'a/')
        self.assertEqual(to_dirpath('a//'), 'a//')
        self.assertEqual(to_dirpath('a/b'), 'a/b/')
        self.assertEqual(to_dirpath('a/b.txt'), 'a/b.txt/')
        self.assertEqual(to_dirpath('a/b.txt/..'), 'a/b.txt/../')

    def test_leaf(self):
        print "test_leaf"
        self.assertEqual(leaf('/'), '/')
        self.assertEqual(leaf('a.txt'), 'a.txt')
        self.assertEqual(leaf('a/b'), 'b')
        self.assertEqual(leaf('a/..'), '..')
        self.assertEqual(leaf('a/b/'), 'b')
        self.assertEqual(leaf('a/../'), '..')
        self.assertEqual(leaf('a/.'), '.')
        self.assertEqual(leaf('//'), '/')
        self.assertEqual(leaf('//./'), '.')
        self.assertEqual(leaf('//..//'), '..')        
        
                
