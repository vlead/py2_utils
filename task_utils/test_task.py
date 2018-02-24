# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
import unittest
from unittest import TestCase
from task import *
import types

class TestTask(TestCase):
    TESTING = True
    def test_incr(self):
        
        print "test_incr_pre"
        
        def action(self):
            print "running pre"
            print "self.val = %s" % self.val
            self.ans = self.val+1
            print "self.ans = %s" % self.ans

        def pre(self):
            print "running pre"
            return self.val > 0

        def post(self):
            print "running post"
            return self.ans > 1

        t = Task(name="t", val=1, run="wet")
        # install the methods in t
        t.pre = types.MethodType(pre, t)
        t.action = types.MethodType(action, t)
        t.post = types.MethodType(post, t)

        print "t.__repr__() = %s" % (t.__repr__())
#        print "dir(t) = %s" % dir(t)
        print "t = %s" % t
        
        self.assertTrue(t.pre())
        t.action()
        self.assertTrue(t.post())
        t.do()
    
if __name__ == '__main__':
    unittest.main()
        

        
    
    

        
        



