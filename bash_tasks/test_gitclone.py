# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
import unittest
from unittest import TestCase
from gitclone import *
import os


class TestGitCloneTask(TestCase):
    TESTING = True
    
    def test_gitclone(self):
        print "test_gitclone"
        cmd = format("\\rm -rf /tmp/foo /tmp/foo.git; git init /tmp/foo.git")
        print cmd
        os.system(cmd)
        t1 = GitCloneTask(wd="/tmp", repo="/tmp/foo.git", run="wet")
        self.assertTrue(t1.pre())
        t1.action()
        self.assertTrue(t1.post())
        print "t1.cmd = %s" % t1.cmd
        print "t1.ans = %s" % t1.ans
        os.system("\\rm -rf /tmp/foo /tmp/foo.git")


    def test_gitclone2(self):
        print "test_gitclone"
        cmd = format("\\rm -rf /tmp/foo /tmp/foo.git; git init /tmp/foo.git")
        print cmd
        os.system(cmd)
        t1 = GitCloneTask(wd="/tmp", repo="/tmp/foo.git", run="wet")
        t1.do()
        print "t1.cmd = %s" % t1.cmd
        print "t1.ans = %s" % t1.ans
        os.system("\\rm -rf /tmp/foo /tmp/foo.git")

    def test_gitclone_branch(self):
        print "test_gitclone_branch"
        os.system("\\rm -rf  /tmp/publisher")
        t1 = GitCloneTask("/tmp", \
                          "https://gitlab.com/vxcg/pub/orgmode/publisher.git", \
                          branch="venkatesh", \
                          run="wet")
        self.assertTrue(t1.pre())
        t1.do()
        self.assertTrue(t1.post())
        os.system("\\rm -rf  /tmp/publisher")

        
if __name__ == '__main__':
    unittest.main()
