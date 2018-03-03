# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
from sh_utils.run_cmd import run_cmd
from wf.jobs.git_clone_job import *

class GitCloneFun:

    @staticmethod
    def is_admissible(j):
        print "id(j.__class__) = %s" % id(j.__class__)
        print "id(GitCloneJob) = %s" % id(GitCloneJob)
        return isinstance(j, GitCloneJob)

    @staticmethod
    def pre(job):
        print "running GitCloneFun.pre on job %s ..." % job
        b = os.path.isdir(job.wd) \
            and not os.path.exists(job.ws_dir)
        print "... pre returns %s" % b
        return b
        
    @staticmethod    
    def do(job):
        print "running GitCloneFun.do on job %s ..." % job        
        if not GitCloneFun.is_admissible(job):
            r = Result(sender=GitCloneFun, job=job, status='fail', \
                       err=format("job not admissible: %s" % job))
            raise ResultException(r)
        
        if not GitCloneFun.pre(job):
            r = Result(sender=GitCloneFun, job=job, status="fail",\
                       err=format("job not ready: %s" % job))
            raise ResultException(r)

        try: 
            s = format("cd %s; git clone %s %s %s" \
                       % (job.wd, job.git_opts, job.repo, job.ws_name))
            print s
            ans = run_cmd(s)
            print "ans =  %s" % ans
            r = Result(sender=GitCloneFun, job=job, \
                       status="succ", cmd=s, output=ans, \
                       ws_dir=job.ws_dir)
            print "GitCloneFun.do ... succ" 
            return r
        except Exception as e:
            print "exception: e %s " % e
            r = Result(sender=GitCloneFun, job=job, status="fail", \
                       cmd=s, err=format("system exception: %s" % e), exn=e)
            raise ResultException(r)

    # post: r -> Bool    
    @staticmethod        
    def post(r):
        print "running GitCloneFun.post on result %s ..." % r        
        b = r.status == "succ" \
            and is_git_ws(r.ws_dir)
        print "post returns %s" % b
        return b

    


