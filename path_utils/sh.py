# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0

# Additional Path utilities
# -------------------------

import commands
# shell returns the output of a shell command
# -------------------------------------------
def sh(s):
    (status, ans) = commands.getstatusoutput(s)
    if status != 0:
        raise Exception("error running sh command %s" % s)
    return ans

def shell(s):
    return sh(s)

