# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
import unittest
from unittest import TestCase
from wf.funs.git_clone_fun import *
from wf.jobs.git_clone_job import *

class TestGitClone(TestCase):
    TESTING = True
    global wd
    global repo
    global test_leafname
    global test_dir

    
    wd = "/tmp"
    repo = "https://github.com/vlead/test.git"
    test_leafname = "test"
    test_dir = os.path.join(wd, test_leafname)
    
    def test_clone(self):
        print "test_clone"
        
        j1 = GitCloneJob(wd=wd, repo=repo)
        self.assertTrue(GitCloneFun.is_admissible(j1))
        
        os.system("rm -rf %s" % test_dir)
        self.assertTrue(GitCloneFun.pre(j1))
        
        r1 = GitCloneFun.do(j1)
        self.assertTrue(GitCloneFun.post(r1))



if __name__ == "__main__":
    unittest.main()
