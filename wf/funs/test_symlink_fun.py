#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
import unittest
import os.path
from unittest import TestCase
from wf.jobs.symlink_job import *
from wf.funs.symlink_fun import *


class TestSymLink(TestCase):
    TESTING = True
    global wd
    global dest
    global name
    global link
    global test_dir

    
    wd = "/tmp"
    dest = '/tmp/bar'
    link = 'foo'
    name = "test"
    test_dir = os.path.join(wd, name)
    
    def test_symlink(self):
        print "test_symlink"
        os.system("\\rm -rf /tmp/foo /tmp/test/foo")
        os.system('cd /tmp; mkdir -p test')
        j0 = SymLinkJob(wd=wd, dest=dest, link=link)
        r0 = SymLinkFun.do(j0)
        self.assertTrue(SymLinkFun.post(r0))        
        j1 = SymLinkJob(wd=test_dir, dest=dest)
        r1 = SymLinkFun.do(j1)
        self.assertTrue(SymLinkFun.post(r1))

if __name__ == "__main__":
    unittest.main()

