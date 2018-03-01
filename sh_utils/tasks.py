# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

# Implements tasks related to shell utilities
import os
import sys
from task_utils.task import Task
from path_utils.path import *

class RepoTask(Task):
    def __init__(self, wd, repo, ws=None,  **kwargs):
        self.wd = wd
        self.repo = repo
        if ws == None:
            self.ws = leaf_sans_exts(urlparse(repo).path)
        else:
            self.ws = ws
        super(RepoTask, self).__init__(**kwargs)


    


        
            

        
        
        
        
