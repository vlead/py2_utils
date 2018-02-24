# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>

import os
from task_utils.task import *
from url_utils.url_preds import *

class SymLinkTask(Task):
    def __init__(self, wd, dest, link=None):
        self.wd = wd
        self.dest = dest
        self.link = link

    def pre(self):
        print "in SymLinkTask.pre"
        return os.path.exists(self.wd)


    def action(self):
        print "in SymLinkTask.action"
        wd = os.path.abspath(self.wd)
        relpath = os.path.relpath(self.dest, self.wd)
        if self.link == None:
         
            link = os.path.split(relpath)[1]
            if link[1] == '':
                link = os.path.split(link[0])[1]
            cmd=format("cd %s; ln -s %s" % (wd, relpath))
        else:
            link = self.link
            cmd=format("cd %s; ln -s %s" % (wd, relpath, link))
        print "cmd = %s" % cmd        
        os.system(cmd)
        self.ans = os.path.join(wd, link)
            
    
    def post(self):
        print "in SymLinkTask.post"
        return os.path.islink(self.ans)




