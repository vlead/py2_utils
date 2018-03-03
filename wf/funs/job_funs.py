# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0

# Additional Path utilities

# -------------------------

import os
import sys
from urlparse import urlparse
from path_utils.path import *
from type_utils.check import *
from url_utils.url_preds import *

# clone repo
# ----------
# cd's to wd, clones repo into ws
# wd is an existing directory
# repo is a valid git repo
# ws if absent takes the name from repo

def clone_repo(cjob):
    wd = cjob.wd
    repo = cjob.repo
    ws = cjob.ws
    git_args = cjob.git_args
    # check pre_condition
    check(lambda j: cjob.cond(), "Job doesn't satisfy precondition %s")
    s = format("cd %s; git clone %s %s %s" % (wd, git_args, repo, ws))
    print s
    try:
        os.system(s)
        r = GitCloneResult(sender=clone_repo, \
                           job=cjob, status="succ", \
                           ws=ws)
        return r
    except Exception(e):
        r = GitCloneResult(sender= clone_repo, job=cjob, \
                           status="fail",
                           exn=e)
        raise ResultException(r)


def git_install(job):
    check_install_shape(job)
    try:
        if if_already_cloned(job):
            r = git_pull(job)
        else:
            r = git_clone(job)
        rerturn r
    except Exception as e:
        re = ...
        raise ResultException(re)


