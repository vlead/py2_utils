# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
import path_utils.path
from sh_utils.run_cmd import run_cmd
from sh_utils.task_funs import have_internet
from wf.jobs.git_pull_job import *
from wf.jobs.git_install_job import *
from wf.funs.check_funs import *

class GitPullFun():

    @staticmethod
    def is_admissible(j):
        return isinstance(j, GitPullJob) \
            or isinstance(j, GitInstallJob) \


    @staticmethod
    def pre(job):
        return os.path.isdir(job.wd) \
            and  path_utils.path.is_git_ws(job.wd)

    
    @staticmethod    
    def do(job):
        check_admissible(GitPullFun, job)
        check_pre(GitPullFun, job)
        if have_internet():
            s = format("cd %s; git pull %s " \
                       % (job.wd, job.git_opts))
            return run_job_cmd(GitPullFun, job, s, ws_dir=job.wd)
        else:
            msg = "not online, so pull not run"
            print msg
            return Result(sender=GitPullFun, job=job, cmd=None, \
                          output=msg, \
                          ws_dir=job.wd)



    # post: r -> Bool    
    @staticmethod        
    def post(r):
        return is_git_ws(r.ws_dir)

    


