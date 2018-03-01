# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>

class Job(object):
    def __init__(self, sender=None, cat=None, **args):
        self.sender = sender
        self.cat = cat
        self.args=args
        for i in args.keys():
            self.__dict__[i] = args[i]
            
    def __repr__(self):
        return "Job(**%s)" % self.args

    def cond(self):
        raise Exception("Undefined condition")


class Result(object):
    def __init__(self,  sender=None,  job=None,  status=None, **args):
        self.job=job
        self.sender=sender
        self.status=status
        self.args = args
        for i in args.keys():
            self.__dict__[i] = args[i]

    def __repr__(self):
        return "Result(**%s)" % self.args

    def cond(self):
        raise Exception("Undefined condition")

class ResultException(Exception):
    def __init__(self, result):
        self.result = result
        

def top():
    pass

    
    
    


    
        
        
        
        
        
        


    


    
