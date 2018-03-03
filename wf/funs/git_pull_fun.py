# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
import path_utils.path
from sh_utils.run_cmd import run_cmd
from wf.jobs.git_pull_job import *

class GitPullFun():

    @staticmethod
    def is_admissible(j):
        print "id(j.__class__) = %s" % id(j.__class__)
        print "id(GitPullJob) = %s" % id(GitPullJob)
        return isinstance(j, GitPullJob)

    @staticmethod
    def pre(job):
        b = os.path.isdir(job.wd) \
            and  path_utils.path.is_git_ws(job.wd)
        return b
        
    @staticmethod    
    def do(job):
        print "running GitPullFun.do on job %s ..." % job        
        if not GitPullFun.is_admissible(job):
            r = Result(sender=GitPullFun, job=job, status='fail', \
                       err=format("job not admissible: %s" % job))
            raise ResultException(r)
        
        if not GitPullFun.pre(job):
            r = Result(sender=GitPullFun, job=job, status="fail",\
                       err=format("job not ready: %s" % job))
            raise ResultException(r)

        try: 
            s = format("cd %s; git pull %s " \
                       % (job.wd, job.git_opts))
            print s
            ans = run_cmd(s)
            print "ans =  %s" % ans
            r = Result(sender=GitPullFun, job=job, \
                       status="succ", cmd=s, output=ans, \
                       ws_dir=job.wd)
            print "GitPullFun.do ... succ" 
            return r
        except Exception as e:
            print "exception: e %s " % e
            r = Result(sender=GitPullFun, job=job, status="fail", \
                       cmd=s, err=format("system exception: %s" % e), exn=e)
            raise ResultException(r)

    # post: r -> Bool    
    @staticmethod        
    def post(r):
        print "running GitPullFun.post on result %s ..." % r        
        b = r.status == "succ" \
            and is_git_ws(r.ws_dir)
        print "post returns %s" % b
        return b

    


