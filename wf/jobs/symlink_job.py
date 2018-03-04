from path_utils.check_path import *
from wf.jobs.job import *

class  SymLinkJob(Job):
    def __init__(self, sender=None, wd=None, dest=None, link="", **args):
        #1. wd is a path
        check_path(wd)
        super(SymLinkJob, self).__init__(sender=sender, \
                                          wd=wd, \
                                          dest=dest, \
                                          link=link, \
                                          **args)

    def __repr__(self):
        return "SymLinkJob(**%s)" % self.args


