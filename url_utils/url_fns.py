# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os
from urlparse import urlparse
from type_utils.check import *
from  url_preds import *
from path_utils.path import *

# given a url, extract pathname
# -----------------------------

# url_path: url -> path
def url_path(url):
    a = urlparse(url)
    return a.path

# for posix sys
def url_leaf(url):
    p = url_path(url)
    return leaf(p)

# for posix systems
# org-8.2.10.tar.gz => org
def url_leaf_sans_exts(url):
    p = url_leaf(url)
    return sans_exts(p)

def strip_exts(p, le):
    for e in le:
        if p.endswith(e):
            return p.rstrip(e)
    return p
            
def url_leaf_strip_targz(url):
    p = url_leaf(url)
    return strip_exts(p, ['.tar.gz', '.tgz', '.tar'])
