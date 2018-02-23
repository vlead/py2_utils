# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os
from urlparse import urlparse
from type_utils.check import *

def is_url(p):
    def f(s):
        a = urlparse(s)
        return p(a)
    return f

# a is the result of parsing a url
# is_url_http: str -> boolean
is_url_http = is_url(lambda a: a.scheme in ["https", "http"])
is_git_repo = is_url(lambda a: os.path.splitext(a.path)[1] == ".git")
is_filename = is_url(lambda a: a.scheme == '' and a.path != '')

is_tar_gz   = is_url(lambda a: os.path.splitext(a.path)[1] == ".gz" \
                     and \
                     os.path.splitext(os.path.splitext(a.path)[0])[1] == ".tar")

is_existing_dir = is_url(lambda a: os.path.isdir(a.path))
is_existing_file = is_url(lambda a: os.path.isfile(a.path))

is_wget_tar_gz = lambda s: is_url_http(s) and is_tar_gz(s)



# Is the given string a git repository?

check_url_http = check(is_url_http, "invalid http resource name: %s")
check_git_repo = check(is_git_repo, "invalid git resource name: %s")
check_filename = check(is_filename, "invalid filename: %s")
check_is_tar_gz = check(is_tar_gz, "invalid tar.gz filename: %")
check_is_wget_tar_gz = check(is_tar_gz, "invalid url of tar.gz resource: %")
check_existing_dir = check(is_existing_dir, "invalid or non-existent directory: %")
check_existing_file = check(is_existing_file, "invalid or non-existent file %s")


    
