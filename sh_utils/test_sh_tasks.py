# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
import os
import unittest
from unittest import TestCase

from task_funs import *
from tasks import *
from path_utils.path import *


class TestShellTasks(TestCase):
    TESTING = True
    global wd
    global repo
    global test_leafname
    global test_dir
    global t1
    
    wd = "/tmp"
    repo = "https://github.com/vlead/test.git"
    test_leafname = "test"
    test_dir = os.path.join(wd, test_leafname)

    t1 = {"wd": wd, "repo": repo}
    
    def test_repo(self):
        os.system("rm -rf %s" % test_dir)
        print "test_clone_repo"
        clone_repo(**t1)
        self.assertTrue(os.path.isdir(test_dir))

        # # test pull
        # print "test_pull_repo"
        # self.assertTrue(os.path.isdir(test_dir))        
        # pull_repo(wd, test_leafname)
        # self.assertTrue(os.path.isdir(test_dir))

        # # test install: expect pull
        # print "test_install_repo:pull"
        # self.assertTrue(os.path.isdir(wd))
        # install_repo(wd, repo, test_leafname)
        # self.assertTrue(is_git_ws(test_dir))

        # # rm test_dir
        # os.system("rm -rf %s" % test_dir)        
        
        # # test install: expect clone
        # print "test_install_repo:clone"
        # self.assertTrue(os.path.isdir(wd))
        # install_repo(wd, repo, test_leafname)
        # self.assertTrue(is_git_ws(test_dir))




if __name__ == "__main__":
    unittest.main()
