# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

# Additional Path utilities
# -------------------------
import os.path
from sh import sh
from urlparse import urlparse

# a path is a string that
# purports to denote an file on a file system

# a path is an fs_path when it exists
# on the current file system.

# is_path: any -> bool
# --------------------
def is_path(x):
    if not type(x) is str:
        return False
    a = urlparse(x)
    return a.scheme in [''] and a.path != '' \
        and a.netloc == '' and a.params == '' \
        and a.params == '' and a.query == '' \
        and a.fragment == ''

# is_dirpath: path -> bool
# ------------------------
def is_dirpath(pn):
    return pn == os.sep \
        or pn == '.' \
        or pn == '..' \
        or pn[-1] == os.sep \
        or pn[-2:] == os.sep + '.' \
        or pn[-3:] == os.sep + '..'

# to_dirpath: path -> dirpath
# ---------------------------
def to_dirpath(pn):
    if pn[-1] != os.sep:
        return pn+os.sep
    else:
        return pn


# A leaf is the last component of a path
# is_leaf: path -> bool
# -----------------------------
def is_leaf(p):
    return p == os.sep \
        or not os.sep in p


# returns the unix basename of path p
def unix_basename(p):
    return sh("basename %s" % p)

# returns the unix dirname of path p
def unix_dirname(p):
    return sh("dirname %s" % p)

# leaf: path -> leaf
def leaf(p):
    return unix_basename(p)

# trunk: path -> path
def trunk(p):
    return unix_dirname(p)

# is path a tar.gz name?
# is_targz: path -> bool
# -----------------------
def is_targz(p):
    return p.endwith(".tar.gz")

# is_tgz_name: path -> bool
# -------------------------
def is_tgz(p):
    return p.endwith(".tgz")

# Predicates for paths and paths of different types
# --------------------------------------------------

# Asks if path exists on the current file system
# is_fs_path: path -> bool
# -----------------------
def is_fs_path(p):
    return os.path.exists(p)

# is_existing_path: path -> bool
# ------------------------------
def is_existing_path(p):
    return is_fs_path(p)

# is_existing_path: path -> bool
# ------------------------------
def exists_path(p):
    return is_fs_path(p)

# is path an existing git work space?
# A git workspace is a directory path containing a
# .git directory. 
# is_git_ws: pathname -> bool
# ---------------------------
def is_git_ws(p):
    return os.path.isdir(os.path.join(p, '.git'))




    


