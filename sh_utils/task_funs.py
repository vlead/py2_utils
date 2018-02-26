# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

# Additional Path utilities
# -------------------------

import os
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

def clone_repo(wd, repo, ws=""):
    s = format("cd %s; git clone %s %s" % (wd, repo, ws))
    print s
    os.system(s)
        

# pull_repo
# ---------
# cd's to wd/ws and runs git pull
def pull_repo(wd, ws):
    s = format("cd %s; cd %s; git pull" % (wd, ws))
    print s
    os.system(s)

# install repo
# ------------
# clones repo if ws doesn't exist,
# pulls if it does
def install_repo(wd, repo, ws=None):
    if ws == None:
        ws_name = leafname(os.path.splitext(urlparse(repo).path)[0])
    else:
        ws_name = ws
    if (os.path.isdir(os.path.join(wd, ws_name))):
        print "%s is already installed" % ws_name
        pull_repo(wd, ws_name)
    else:
        print "%s doesn't exist: cloning it ..." % ws
        clone_repo(wd, repo, ws_name)

# sym_link
# --------
# cd's to dr
def sym_link(wd, target, link=""):
    check(os.path.exists, \
          "error: directory does not exist: %s")(wd)
    
    check(os.path.exists, \
          "error: symlink target does not exist: %s") \
          (os.path.join(wd, target))

    
    r = os.path.relpath(target, wd)
    print "target = %s" % target
    print "wd = %s" % wd
    print "relative path from wd to target = %s" % r
    s=format("cd %s; ln -sf %s %s" % (wd, r, link))
    print "cd_ing  to %s and creating sym link %s to %s ..." \
        % (wd, link, r)
    print(s)
    os.system(s)

# cd's to wd.
# wgets the http_url.
# returns the leaf of the pathname of the http_url
# wget: (path, http_url) -> path
def wget(wd, url):
    check_url_fs_path(wd)
    check_url_http(url)
    s = format("cd %s; wget %s" % (wd, url))
    os.system(s)
    return leaf(urlparse(url).path)


# untar_targz
# -----------
# wd is relative to python cwd
# p is either absolute path or
#   a path relative to wd like a/b/foo.tar.gz
# returns the head part of the targz file, 
# i.e., foo

# Assumptions
# -----------
# foo.tar.gz is a zipped tar version
# of the directory foo.

def untar_targz(wd, p):
    check_url_fs_path(wd)
    check_url_fs_path(os.path.join(wd, p))
    check_url_targz(p)
    s = format("cd %s; tar -xzvf %s" % (wd, p))
    print s
    os.system(s)
    # p   = /a/b/foo.tar.gz
    # ans = foo
    ans = leaf(p).split('.')[0]
    print "cd_d to  %s, and untarred to %s " % (wd, ans)
    return ans
    
def install_targz(wd, url):
    p = wget(wd, url)
    return untar_targz(wd, p)

    
def del_path(fn):
    s = "rm -rf %s" % fn
    os.system(s)
    
