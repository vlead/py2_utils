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
def url_leaf_sans_exts(url):
    p = url_leaf(url)
    return sans_exts(p)
