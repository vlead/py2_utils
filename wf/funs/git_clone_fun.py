# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
from sh_utils.run_cmd import run_cmd
from wf.jobs.git_clone_job import *
from wf.jobs.git_install_job import *
from wf.funs.check_funs import *

class GitCloneFun:


    @staticmethod
    def is_admissible(j):
        return isinstance(j, GitCloneJob) \
            or isinstance(j, GitInstallJob)

    
    @staticmethod
    def pre(job):
        b = os.path.isdir(job.wd) \
            and not os.path.exists(job.ws_dir)
        return b

    
    @staticmethod    
    def do(job):
        check_admissible(GitCloneFun, job)
        check_pre(GitCloneFun, job)

        s = format("cd %s; git clone %s %s %s" \
                   % (job.wd, job.git_opts, job.repo, job.ws_name))
        
        return run_job_cmd(GitCloneFun, job, s, ws_dir=job.ws_dir)


    # post: r -> Bool    
    @staticmethod        
    def post(r):
        return is_git_ws(r.ws_dir)


    


