# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os
import sys
from sh_utils.run_cmd import run_cmd
from wf.jobs.targz_install_job import *
from wf.funs.check_funs import *

class TargzInstallFun:

    @staticmethod
    def is_admissible(j):
        return isinstance(j, TargzInstallJob) \

    
    @staticmethod
    def pre(job):
        return os.path.isdir(job.wd)


    
    @staticmethod    
    def do(job):
        check_admissible(TargzInstallFun, job)
        check_pre(TargzInstallFun, job)

        if os.path.exists(job.ws_dir):
            print "%s already installed" % job.ws_dir
            return Result(sender=TargzInstallFun, job=job, ws_dir=job.ws_dir)
        else:
            #wget
            s =format("cd %s; wget %s" % (job.wd, job.url))
            r = run_job_cmd(TargzInstallFun, job, \
                            s, ws_dir=job.ws_dir)
            #untar
            s=format("cd %s; tar -xzvf %s" % (job.wd, job.ws_targz))
            r = run_job_cmd(TargzInstallFun, job, s, \
                            ws_dir=job.ws_dir)
            check_post(TargzInstallFun, r)
            return r

    # post: r -> Bool    
    @staticmethod        
    def post(r):
        return os.path.isdir(r.ws_dir)


    


