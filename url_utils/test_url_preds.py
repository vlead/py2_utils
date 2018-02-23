# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import unittest
from unittest import TestCase
from type_utils.check import  *
from url_preds import *


class TestUrlPreds(TestCase):
    TESTING = True
    def test_is_url(self):
        print "test_is_url"
        self.assertEqual(is_url_http("http://vlabs.ac.in/exp/01"), True)
        self.assertEqual(is_url_http("vlabs.ac.in/exp/01"), False)
        self.assertEqual(is_git_repo("http://vlabs.ac.in/bar/foo.git"), True)     
        self.assertEqual(is_filename("vlabs.ac.in/exp/01"), True)
        self.assertEqual(is_wget_tar_gz("foo.bar/f.tar.gz"), False)
#        self.assertEqual(is_existing_file("/bin/cat"), True)


if __name__ == '__main__':
    unittest.main()

##        self.assertEqual(is_git_repo("vlabs.ac.in/foo.git"), True)

##        self.assertEqual(is_tar_gz("http://foo.bar/f.tar.gz"), True)
##      self.assertEqual(is_wget_tar_gz("http://foo.bar/f.tar.gz"), True)    
##        self.assertEqual(is_existing_dir("./"), True)
