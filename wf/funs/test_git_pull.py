# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
import unittest
from unittest import TestCase
from wf.jobs.git_clone_job import *
from wf.funs.git_clone_fun import *

from wf.jobs.git_pull_job import *
from wf.funs.git_pull_fun import *


class TestGitPull(TestCase):
    TESTING = True
    global wd
    global repo
    global test_leafname
    global test_dir

    
    wd = "/tmp"
    repo = "https://github.com/vlead/test.git"
    name = "test"
    test_dir = os.path.join(wd, name)
    
    def test_pull(self):
        print "test_pull"
        os.system("rm -rf %s" % test_dir)

        j0 = GitCloneJob(wd=wd, repo=repo)
        r0 = GitCloneFun.do(j0)
        j1 = GitPullJob(wd=r0.ws_dir)
        self.assertTrue(GitPullFun.is_admissible(j1))
        self.assertTrue(GitPullFun.pre(j1))        
        r1 = GitPullFun.do(j1)
        self.assertTrue(GitPullFun.post(r1))

if __name__ == "__main__":
    unittest.main()
