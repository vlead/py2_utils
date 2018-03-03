# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

# Additional Path utilities
# -------------------------
import os.path
from sh_utils.run_cmd import run_cmd
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

# splits a path into its components
def components(p):
    return p.rsplit(os.sep)

# conjecture:
# -----------
# for all paths p:
#  os.path.join(*components(p)) == p

def is_normpath(p):
    return p == os.path.normpath(p)

# A path is simple if
# it is a normal path of size one and not equal 
# to any of the constant singleton paths.
def is_simple(p):
    return is_normpath(p) \
        and len(components(p)) == 1 \
        and p not in ['/', '//', '.', '..']
    
# a component of a
# "a/b/c"
# ".." and "." are not atoms
# they are operators.

    
# is_dirpath: path -> bool
# ------------------------
def is_dirpath(p):
    return p == os.sep \
        or p == '.' \
        or p == '..' \
        or p[-1] == os.sep \
        or p[-2:] == os.sep + '.' \
        or p[-3:] == os.sep + '..'

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

# returns the unix basename of normalized path p
def unix_basename(p):
    return run_cmd("basename %s" % p)

# returns the unix dirname of normalized path p
def unix_dirname(p):
    return run_cmd("dirname %s" % p)

# leaf: path -> leaf
def leaf(p):
    return unix_basename(os.path.normpath(p))

# trunk: path -> path
def trunk(p):
    return unix_dirname(os.path.normpath(p))

# is path a tar.gz name?
# is_targz: path -> bool
# -----------------------
def is_tar_gz(p):
    return p.endwith(".tar.gz")

# is_tgz_name: path -> bool
# -------------------------
def is_tgz(p):
    return p.endwith(".tgz")

def is_targz(p):
    return is_tar_gz(p) or is_tgz(p)

# pathname without any extensions
# sans_exts("a/b/c.d.e") = "a/b/c"

# sans_exts : leaf -> 
def sans_exts(p):
    q = os.path.normpath(p)
    if q in  ['.', '..', '/', '//']:
        return q
    else:
        return q.split('.')[0]
    
# leaf_san_extns(a/b.c/./e.f.tgz)
# = e
# sans_exts : leaf -> 
def leaf_sans_exts(p):
    return sans_exts(leaf(p))

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

# extension: path -> str
def extension(p):
    return os.path.splitext(p)[1]


    




    


