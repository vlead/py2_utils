from path_utils.check_path import *
from wf.jobs.job import *

class  GitPullJob(Job):
    def __init__(self, sender=None, wd=None, git_opts="", **args):
        #1. wd is a path
        check_path(wd)
        super(GitPullJob, self).__init__(sender=sender, \
                                          wd=wd, \
                                          git_opts=git_opts, \
                                          **args)

    def __repr__(self):
        return "GitPullJob(**%s)" % self.args


