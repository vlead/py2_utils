# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
from sh_utils.run_cmd import run_cmd
from wf.jobs.git_install_job import *
from wf.funs.git_clone_fun import *
from wf.funs.git_pull_fun import *
from wf.funs.check_funs import *

class GitInstallFun:

    @staticmethod
    def is_admissible(j):
        return isinstance(j, GitInstallJob)


    @staticmethod
    def pre(job):
        return os.path.isdir(job.wd)
        
    @staticmethod    
    def do(job):
        check_admissible(GitInstallFun, job)
        check_pre(GitInstallFun, job)

        if GitCloneFun.pre(job):
            return GitCloneFun.do(job)
        else:
            print "already cloned, pulling ..."
            nj = GitPullJob(sender=job.sender, \
                            wd=os.path.join(job.wd, job.ws_name))
            return GitPullFun.do(nj)

        
    # post: r -> Bool    
    @staticmethod        
    def post(r):
        print "running GitInstallFun.post on result %s ..." % r        
        return is_git_ws(r.ws_dir)

    


