# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

import os.path


# a pathname is a string that
# purports to denote a filename in a
# does pathname p denote a directory name
# A pathname denotes a directory name if it ends with a
# a file name separator ('/' in Unix)
def is_dirname(p):
    
    return p == os.sep \
        or p == '.' \
        or p == '..' \
        or p[-1] == os.sep \
        or p[-2:] == os.sep + '.' \
        or p[-3:] == os.sep + '..'

# Coerce pathname to a directory name
def to_dirname(p):
    if p[-1] != os.sep:
        return p+os.sep
    else:
        return p

# Get leaf of pathname
def leafname(p):
    # normpath removes the trailing separator, if any
    q = os.path.normpath(p)
    if q == os.sep:
        return q
    elif q == os.sep+os.sep:
        return os.sep
    else:
        return os.path.split(q)[1]
    
    
