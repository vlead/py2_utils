# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
import unittest
from unittest import TestCase
from wf.funs.targz_install_fun import *
from wf.jobs.targz_install_job import *

class TestTargzInstall(TestCase):
    TESTING = True
    global wd
    global url
    global name
    global test_dir

    
    wd = "/tmp/a"
    url = "http://pascal.iiit.ac.in/~choppell/test.tar.gz"
    name = "test"
    test_dir = os.path.join(wd, name)
    
    def test_targz_install(self):
        print "test_targz_install"
        print "wd = %s" % wd
        print "url = %s" % url
        print "name = %s" % name
        print "test_dir = %s" % test_dir

        os.system("mkdir -p %s" % wd)
        os.system("rm -rf %s" % test_dir)
        
        j1 = TargzInstallJob(wd=wd, url=url)

        self.assertTrue(TargzInstallFun.is_admissible(j1))
        self.assertTrue(TargzInstallFun.pre(j1))
        r1 = TargzInstallFun.do(j1)
        print "r1 = %s" % r1.__repr__()
        self.assertTrue(TargzInstallFun.post(r1))

if __name__ == "__main__":
    unittest.main()
