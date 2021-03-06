# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppella@iiit.ac.in>
# Licence: GPL v3.0

import os.path
from wf.jobs.job import Job 
# from path_utils.path import *
from path_utils.check_path import check_path
from url_utils.url_preds import check_http_tar_gz
from url_utils.url_fns import url_leaf
from url_utils.url_fns import url_leaf_strip_targz


class TargzInstallJob(Job):
    def __init__(self, sender=None, wd=None, http_proxy="", \
                 https_proxy="", url=None, **args):
        # 1. wd is a path
        check_path(wd)
        # 2. url is an http url
        check_http_tar_gz(url)

        ws_targz = url_leaf(url)
        print "ws_targz = %s" % ws_targz
        # https://org-mode.org/org-8.2.10.tar.gz => org-8.2.10
        ws_name = url_leaf_strip_targz(url)
        print "ws_name = %s" % ws_name
        ws_dir = os.path.join(wd, ws_name)
        
        super(TargzInstallJob, self).__init__(sender=sender, \
                                              wd=wd, url=url, \
                                              http_proxy=http_proxy, \
                                              https_proxy=https_proxy, \
                                              ws_name=ws_name, \
                                              ws_targz=ws_targz,\
                                              ws_dir=ws_dir, \
                                              **args)
    def __repr__(self):
        return "TargzInstallJob(**%s)" % self.args


