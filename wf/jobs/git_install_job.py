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


class GitInstallJob(Job):
    def __init__(self, sender=None, wd=None, repo=None, \
                 branch=None, ws_name=None, **args):
        # 1. wd is a path
        check_path(wd)
        # 2. repo is a git repo
        check_url(repo)

        # 3. ws is either None ...
        if ws_name == None:
            ws_name = url_leaf_sans_exts(repo)
            ws_dir = os.path.join(wd, ws_name)
        else:
            # ... or a simple path
            check_simple(ws_name)
            ws_dir = os.path.join(wd, ws)

        # 4. branch
        if branch == None:
            git_opts = ""
        else:
            check_simple(branch)
            git_opts = "--branch %s --single-branch " % branch
            
        super(GitInstallJob, self).__init__(sender=sender, \
                                          wd=wd, repo=repo, \
                                          ws_name=ws_name, \
                                          ws_dir= ws_dir, \
                                          branch=branch, \
                                          git_opts=git_opts,
                                          **args)
    def __repr__(self):
        return "GitInstallJob(**%s)" % self.args

    

