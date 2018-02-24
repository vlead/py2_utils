# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>

class Task(object):
    def __init__(self,  **args):
        self.ans = None
        self.args = args
        for i in args.keys():
            self.__dict__[i] = args[i]

    def __repr__(self):
        return "Task(**%s)" % self.args

    def pre(self):
        return True

    def action(self):
        self.ans = None

    def rollback(self):
        pass
    
    def post(self):
        return True
    
    def do(self):
        print "entering run ..."
        assert self.pre()
        try:
            self.action()
        except Exception as e:
            self.status = "fail"
            self.err_msg = e.__str__()
            self.rollback()
            raise Exception("action failed on task %s: %s" \
                            % (self, e))
        assert self.post()
        print "exiting run ..."
    


                                
                                

