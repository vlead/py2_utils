# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
import unittest
from unittest import TestCase
from wf.funs.git_install_fun import *
from wf.jobs.git_install_job import *

class TestGitInstall(TestCase):
    TESTING = True
    global wd
    global repo
    global name
    global test_dir

    
    wd = "/tmp"
    repo = "https://github.com/vlead/test.git"
    name = "test"
    test_dir = os.path.join(wd, name)
    
    def test_install(self):
        print "test_install"
        os.system("rm -rf %s" % test_dir)

        j1 = GitInstallJob(wd=wd, repo=repo)
        self.assertTrue(GitInstallFun.is_admissible(j1))
        self.assertTrue(GitInstallFun.pre(j1))
        r1 = GitInstallFun.do(j1)
        self.assertTrue(GitInstallFun.post(r1))

        j2 = GitInstallJob(wd=wd, repo=repo)
        self.assertTrue(GitInstallFun.is_admissible(j2))
        self.assertTrue(GitInstallFun.pre(j2))
        r2 = GitInstallFun.do(j2)
        self.assertTrue(GitInstallFun.post(r2))
        



if __name__ == "__main__":
    unittest.main()
