# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
import os
import unittest
from unittest import TestCase

from task_funs import *
from path_utils.path import *



class TestShellFuns(TestCase):
    TESTING = True
    global wd
    global repo
    global test_leafname
    global test_dir
    
    wd = "/tmp"
    repo = "https://github.com/vlead/test.git"
    test_leafname = "test"
    test_dir = os.path.join(wd, test_leafname)
    
    def test_repo(self):
        os.system("rm -rf %s" % test_dir)
        print "test_clone_repo"
        clone_repo(wd, repo)
        self.assertTrue(os.path.isdir(test_dir))

        # test pull
        print "test_pull_repo"
        self.assertTrue(os.path.isdir(test_dir))        
        pull_repo(wd, test_leafname)
        self.assertTrue(os.path.isdir(test_dir))

        # test install: expect pull
        print "test_install_repo:pull"
        self.assertTrue(os.path.isdir(wd))
        install_repo(wd, repo, test_leafname)
        self.assertTrue(is_git_ws(test_dir))

        # rm test_dir
        os.system("rm -rf %s" % test_dir)        
        
        # test install: expect clone
        print "test_install_repo:clone"
        self.assertTrue(os.path.isdir(wd))
        install_repo(wd, repo, test_leafname)
        self.assertTrue(is_git_ws(test_dir))

    def test_symlink(self):
        os.system("mkdir -p /tmp/test")
        os.system("rm -rf /tmp/test_link")
        sym_link("/tmp", "/tmp/test", link="test_link")
        self.assertTrue(os.path.islink("/tmp/test_link"))

        os.system("rm -rf /tmp/usr")
        sym_link("/tmp", "/usr")
        self.assertTrue(os.path.islink("/tmp/usr"))

        os.system("rm -rf /tmp/xyz")
        sym_link("/tmp", "/usr", "xyz")
        self.assertTrue(os.path.islink("/tmp/xyz"))

    def test_untar(self):
        os.system("mkdir -p /tmp/a")
        install_targz("/tmp/a", "http://pascal.iiit.ac.in/~choppell/test.tar.gz")
        self.assertTrue(os.path.isdir("/tmp/a/test"))
        os.system("rm -rf /tmp/a")
                        
        

        

        
                        
        
                   
        


        
