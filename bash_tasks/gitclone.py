# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os
from task_utils.task import *
from py_utils.url_utils.url_preds import *
from py_utils.pathname_utils.pathname import *

from urlparse import urlparse

class GitCloneTask(Task):
    def __init__(self, wd, repo, branch=None, cmd="", run="dry", ws=None, **args):
        self.wd = wd
        self.repo = repo
        self.ws = ws
        self.branch = branch
        self.run=run
        super(GitCloneTask, self).__init__(**args)

    # pre:
    # 1. repo looks like a git repo
    # 2. wd is an existing directory
    # 3. join(wd, ws) is non existing
    # 
    def pre(self):
        if not is_git_repo(self.repo):  # 1
            return False
        if not os.path.isdir(self.wd):  # 2
            return False
        if (self.ws == None):
            self.init_ws = self.ws
            self.ws = (os.path.splitext(leafname(urlparse(self.repo).path)))[0]
        return not os.path.isdir(os.path.join(self.wd, self.ws)) # 3

    # run = dry | wet
    def action(self):
        if self.branch == None:
            branch_option = " "
        else:
            branch_option = "-b " + self.branch + " --single-branch "
        cmd = format("cd %s; git clone %s %s %s" \
                     % (self.wd, branch_option, self.repo, self.ws))
        self.cmd = cmd
        print cmd
        if self.run == "wet":
            os.system(cmd)
        self.ans = os.path.abspath(os.path.join(self.wd, self.ws))
        if os.path.isdir(self.repo):
            self.abs_repo = os.path.abspath(self.repo)
        else:
            self.abs_repo = self.repo
        print "cloned %s into %s" % (self.abs_repo, self.ans)
        self.status = "succ"

    # the repository is cloned at ans/.git
    def post(self):
        return os.path.isdir(os.path.join(self.ans, ".git"))

        
        
        
        

    
