# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
from wf.jobs.git_clone_job import *

class GitCloneFun:

    @staticmethod
    def is_admissible(j):
        print "id(j.__class__) = %s" % id(j.__class__)
        print "id(GitCloneJob) = %s" % id(GitCloneJob)
        return isinstance(j, GitCloneJob)

    @staticmethod
    def pre(job):
        return os.path.isdir(job.wd) \
            and not os.path.exists(job.ws)
        
    @staticmethod    
    def do(job):
        if not GitCloneFun.is_admissible(job):
            raise ResultException(Result(sender=GitCloneFun, job=job, status='fail', \
                                         err=format("job not admissible: %s" % job)))
        
        if not GitCloneFun.pre(job):
            raise ResultException(Result(sender=GitCloneFun, job=job, status="fail",\
                                         err=format("job not ready: %s" % job)))
        
        s = format("cd %s; git clone %s %s %s" % (job.wd, job.git_opts, job.repo, job.ws))
        print s
        os.system(s)
        return Result(sender=GitCloneFun, job=job, status="succ", ws=job.ws)

    # post: r -> Bool    
    @staticmethod        
    def post(r):
        return r.status == "succ" \
            and is_git_ws(r.ws)

    


