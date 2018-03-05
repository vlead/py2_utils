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
    return os.path.join(wd, ws)

# install repo
# ------------
# clones repo if ws doesn't exist,
# pulls if it does
def install_repo(wd, repo, ws=None):
    if ws == None:
        ws_name = leaf(os.path.splitext(urlparse(repo).path)[0])
    else:
        ws_name = ws
    ans = os.path.join(wd, ws_name)
    if (os.path.isdir(ans)):
        print "%s is already installed" % ws_name
        pull_repo(wd, ws_name)
    else:
        print "%s doesn't exist: cloning it ..." % ws_name
        clone_repo(wd, repo, ws_name)
    return ans

# sym_link
# --------
# cd's to dr
def sym_link(wd, target, link=""):
    check(os.path.exists, \
          "error: directory does not exist: %s")(wd)
    
    check(os.path.exists, \
          "error: symlink target does not exist: %s")(target)

    
    r = os.path.relpath(target, wd)
    print "target = %s" % target
    print "wd = %s" % wd
    print "relative path from wd to target = %s" % r
    s=format("cd %s; ln -sf %s %s" % (wd, r, link))
    print "cd_ing  to %s and creating sym link %s to %s ..." \
        % (wd, link, r)
    print(s)
    os.system(s)
    return os.path.join(wd, leaf(r))

# cd's to wd.
# wgets the http_url.
# returns the leaf of the pathname of the http_url
# wget: (path, http_url) -> path
def wget(wd, url):
    check_url_fs_path(wd)
    check_url_http(url)
    s = format("cd %s; wget %s" % (wd, url))
    print s
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
    # p   = foo.tar.gz
    # ans = foo
    ans = leaf(p).split('.')[0]
    print "cd_d to  %s, and untarred to %s " % (wd, ans)
    return os.path.abspath(ans)

# wd is the working directory
# url the is a url of a targz file
# 
def install_targz(wd, url):
    fn = leaf(urlparse(url).path)
    fqtf = os.path.join(os.path.abspath(wd), fn)
    print "tar file name = %s" % fqtf
    if os.path.exists(fqtf):
        print "untarred file %s already exists" % fqtf
        return fqtf
    else:
        print "need to wget ..."
        p = wget(wd, url)
        return untar_targz(wd, p)
    

    
def del_path(fn):
    s = "rm -rf %s" % fn
    os.system(s)



# reads a file as a module and returns it.
import importlib

def import_file(p):
    check_url_file(p)
    check(lambda p: extension(p) == ".py", "Path %s does not have .py extenion")(p)
    (trunk, leaf) = os.path.split(p)
    mod_name = os.path.splitext(leaf)[0]
    sys.path.append(trunk)
    m = importlib.import_module(mod_name)
    return m


# p: path referring to emacs executable
def emacs_ver(p):
    full_ver_str = run_cmd(format("%s --version  | head -1 " \
                                   % p)).rsplit()[2]
    print "emacs version: %s" % full_ver_str
    ver_num = int(full_ver_str.rsplit('.')[0])
    return ver_num




task_funs_catalog =  {"clone_repo": clone_repo, \
                       "pull_repo": pull_repo, \
                       "install_repo": install_repo, \
                       "sym_link": sym_link, \
                       "wget": wget, \
                       "untar_targz": untar_targz, \
                       "install_targz": install_targz \
}
                       



