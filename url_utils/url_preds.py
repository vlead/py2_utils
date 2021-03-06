# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os
from urlparse import urlparse
from type_utils.check import *


# is_url: any -> False + url_parse structure
def is_url(s):
    try:
        a = urlparse(s)
        return True
    except:
        return False

# pred is a predicate on a urlparse structure
def is_url_pred(pred):
    def f(s):
        try:
            a = urlparse(s)
        except:
            return False
        return pred(a)
    return f

is_url_http = is_url_pred(lambda a: a.scheme in ["https", "http"])
is_url_path = is_url_pred(lambda a: \
                               a.scheme in ['file', ''] \
                               and a.netloc == '' and a.params == '' \
                               and a.params == '' and a.query == '' \
                               and a.fragment == '' and a.path != '')

# Git Repository names
# --------------------
# A bare git repository is any path ending with '.git'
is_url_git_bare = is_url_pred(lambda a: os.path.splitext(a.path)[1] == ".git")

# A git http bare git repository is any
# - http url
# - whose path is a bare git repo
is_url_http_git_bare = lambda s: is_url_http(s) and is_url_git_bare(s)


is_url_tar_gz   = is_url_pred(lambda a: a.path.endswith(".tar.gz"))
is_url_tgz   = is_url_pred(lambda a: a.path.endswith(".tgz"))
is_url_targz   = lambda s: is_url_tar_gz(s) or is_url_tgz(s)

is_http_tar_gz = lambda s: is_url_http(s) and is_url_tar_gz(s)
is_http_tgz = lambda s: is_url_http(s) and is_url_tgz(s)
is_http_targz  = lambda s: is_http_tar_gz(s) or is_http_tgz(s)

is_url_fs_path = lambda s: is_url_path(s) \
                 and  os.path.exists(urlparse(s).path)

is_url_dir = lambda s: is_url_path(s) \
              and  os.path.isdir(urlparse(s).path)

is_url_file = lambda s: is_url_path(s) \
              and  os.path.isfile(urlparse(s).path)

is_url_git_ws = lambda s: is_url_path(s) \
                and  os.path.isdir(os.path.join(urlparse(s).path, '.git'))


check_url =  check(is_url, "invalid url: %s")
check_url_http = check(is_url_http, "invalid http resource name: %s")
check_url_path = check(is_url_path, "invalid path: %s")
check_url_git_bare = check(is_url_git_bare, "invalid git resource name: %s")
check_url_http_git_bare = check(is_url_http_git_bare, "invalid git resource name: %s")
check_filename = check(is_url_path, "invalid filename: %s")
check_url_tar_gz = check(is_url_tar_gz, "invalid tar.gz filename: %s")
check_url_tgz = check(is_url_tgz, "invalid .tgz filename: %s")
check_url_targz = check(is_url_targz, "invalid .tgz or .tar.gz filename: %s")
check_http_tar_gz = check(is_http_tar_gz, "invalid url of tar.gz resource: %s")
check_http_tgz = check(is_http_tgz, "invalid url of .tgz resource: %s")
check_http_targz = check(is_http_targz, "invalid url of .tgz or .tar.gz resource: %s")
check_url_fs_path = check(is_url_fs_path, "invalid or non-existent directory: %s")
check_url_dir = check(is_url_dir, "invalid or non-existent directory: %s")
check_url_file = check(is_url_file, "invalid or non-existent file %s")
check_url_git_ws = check(is_url_git_ws, "invalid or non-existent git workspace %s")

    
