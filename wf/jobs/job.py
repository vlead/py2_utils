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



class Result(Rec):
    def __init__(self,  sender=None,  job=None,  status=None, **args):
        super(Result, self).__init__(sender=sender, job=job, \
                                  status=status, **args)
        
    def __repr__(self):
        return "Result(**%s)" % self.args


class WfExn(Exception):
    def __init__(self, message="Workflow Exception", **args):
        self.args = args
        for i in args.keys():
            self.__dict__[i] = args[i]

        super(WfExn, self).__init__("Workflow Exception")
        

    def __repr__(self):
        return "WfExn(**%s)" % self.args

    def __str__(self):
        return self.__repr__()
        
class JobIllFormed(WfExn):
    def __init__(self, sender=None, job=None, **args):
        super(JobIsInadmissible, self).__init__(sender=sender, \
                                                job=job, **args)
            
    def __repr__(self):
        return "JobIllFormed(**%s)" % self.args
    

class JobNotReady(WfExn):
    def __init__(self, sender=None, job=None, **args):
        super(JobNotReady, self).__init__(sender=sender, \
                                          job=job, **args)
            
    def __repr__(self):
        return "JobNotReady(**%s)" % self.args
    
class CmdFailed(WfExn):
    def __init__(self, sender=None, job=None, **args):
        super(CmdFailed, self).__init__(sender=sender, \
                                        job=job, **args)
            
    def __repr__(self):
        return "CmdFailed(**%s)" % self.args
    
class ResultPostFailed(WfExn):
    def __init__(self, sender=None, result=None, **args):
        super(ResultPostFailed, self).__init__(sender=sender, \
                                               result=result, **args)
            
    def __repr__(self):
        return "ResultPostFailed(**%s)" % self.args


    
    
    


    
        
        
        
        
        
        


    


    
