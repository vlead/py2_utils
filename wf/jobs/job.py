# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>

class Rec(object):
    def __init__(self, **args):
        self.args = args
        for i in args.keys():
            self.__dict__[i] = args[i]

    def __repr__(self):
        return "Rec(**%s)" % self.args

    def __str__(self):
        return self.__repr__()
        

class Job(Rec):
    def __init__(self, sender=None, cat=None, **args):
        super(Job, self).__init__(sender=sender, cat=cat, **args)
            
    def __repr__(self):
        return "Job(**%s)" % self.args

    def cond(self):
        raise Exception("Undefined condition")


class Result(Rec):
    def __init__(self,  sender=None,  job=None,  status=None, **args):
        super(Result, self).__init__(sender=sender, job=job, \
                                  status=status, **args)
        
    def __repr__(self):
        return "Result(**%s)" % self.args


    def cond(self):
        raise Exception("Undefined condition")

class ResultException(Exception):
    def __init__(self, result):
        self.result = result
        

def top():
    pass

    
    
    


    
        
        
        
        
        
        


    


    
