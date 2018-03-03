# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os
from task_utils.task import *
from py_utils.url_utils.url_preds import *
from py_utils.pathname_utils.pathname import *

from urlparse import urlparse

class GitPullTask(Task):
    def __init__(self, wd, repo,  **args):
        self.wd = wd
        self.repo = repo
        super(GitPullTask, self).__init__(**args) 
       
    # pre:
    # repo looks like a git repo
    # wd is an existing git workspace,
    # i.e., contains a .git
    def pre(self):
        return  is_git_workspace(self.wd) \
            and is_git_repo(self.repo)

    def action(self):
        self.status = "bot"
        cmd = format("cd %s; git pull" % self.wd)
        self.cmd = cmd
        if self.run == "wet":
            os.system(cmd)
        self.ans = os.path.abspath(self.wd)
        if os.path.isdir(self.repo):
            self.abs_repo = os.path.abspath(self.repo)
        else:
            self.abs_repo = self.repo
        print "pulled %s into %s" % (self.abs_repo, self.ans)
        self.status = "succ"

    def post(self):
        return os.path.isdir(os.path.join(self.ans, ".git"))

# install repo
def install_repo(pdir, ws, repo):
    if (os.path.isdir(os.path.join(pdir, ws))):
        print "%s is already installed" % ws
        pull_repo(pdir, ws)
    else:
        print "%s doesn't exist: cloning it ..." % ws
        clone_repo(pdir, ws, repo)

        
        
