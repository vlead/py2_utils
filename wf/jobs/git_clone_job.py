# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os
from urlparse import urlparse
from wf.jobs.job import *
from path_utils.path import *
from path_utils.check_path import *
from url_utils.url_preds import *
from url_utils.url_fns import *


class GitCloneJob(Job):
    def __init__(self, sender=None, wd=None, repo=None, \
                 branch=None, ws=None, **args):
        # 1. wd is a path
        check_path(wd)
        # 2. repo is a git repo
        check_url(repo)

        if ws == None:
            nws = os.path.join(wd, url_leaf_sans_exts(repo))
        else:
            nws = os.path.join(wd, ws)
        # 3. nws is a path
        check_path(nws)

        # 4. branch
        if branch == None:
            git_opts = ""
        else:
            check(lambda a: type(a) is str,
                  "arg branch is not a string: % s")(branch)
            git_opts = "--branch %s --single-branch " % branch
            
        super(GitCloneJob, self).__init__(sender=sender, \
                                          wd=wd, repo=repo, \
                                          ws=nws, \
                                          git_opts=git_opts,
                                          **args)
    def __repr__(self):
        return "GitCloneJob(**%s)" % self.args

def GitCloneResult(Result):
    def __init__(self, sender=None, job=None, \
                 status=None, **args):

        super(GitCloneResult, self).__init__(sender=sender,\
                                             job=job,\
                                             status=status,\
                                             **args)
        
    def __repr__(self):
        return "GitCloneResult(**%s)" % self.args
    
        
    def cond(self):
        return is_git_ws(self.ws)

    
        
        
        

    
