# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0
# -------------------------
import os.path
import path_utils.path
from sh_utils.run_cmd import run_cmd
from wf.jobs.symlink_job import *
from wf.funs.check_funs import *

class SymLinkFun():

    @staticmethod
    def is_admissible(j):
        return isinstance(j, SymLinkJob)



    @staticmethod
    def pre(job):
        return os.path.isdir(job.wd)

    # cwd = "/prj/publisher"
    # wd = "../src"
    # dest="ext/labtheme/org-templates"
    # wd_abs = '/prj/src'
    # dest_abs = '/prj/publisher/ext/labtheme/org-templates'
    # rpath = os.path.relpath(wd_abs, dest_abs)
    #       = '../publisher/ext/labtheme/org-templates

    
    @staticmethod    
    def do(job):
        check_admissible(SymLinkFun, job)
        check_pre(SymLinkFun, job)
        
        wd_abspath=os.path.abspath(job.wd)
        dest_abspath=os.path.abspath(job.dest)
        rp = os.path.relpath(dest_abspath, wd_abspath)
        s = "cd %s; ln -sf %s %s" % (wd_abspath, rp, job.link)
        print "s = %s" % s  
        return check_do(SymLinkFun, job, s, rpath=rp)

    # post: r -> Bool    
    @staticmethod        
    def post(r):
        sl = os.path.join(r.job.wd, r.job.link)
        print "link %s -> %s" % (sl, r.rpath)
        return  is_path(r.rpath) \
#            and os.path.islink(sl)

    


