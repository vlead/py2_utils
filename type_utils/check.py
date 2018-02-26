# -*- coding: utf-8 -*-
# Author:  Venkatesh Choppella <venkatesh.choppell@iiit.ac.in>
# Licence: GPL v3.0


# Takes a predicate pred and a format string msg
# Returns a function that takes an arg.
# if pred(a) is true, returns arg
# Otherwise, raises an Assertion Error
# creating an error message
# formatted using  msg and arg.

# E.g,,
# q = check(lambda y: y > 0, "Type Error: %s not > 0")
# q(-3)
# check: [t -> bool, str] -> t -> t + TypeErr
def check(pred, msg):
    def f(arg):
        if (pred(arg)):
            return arg
        else:
            emsg = format(msg % arg)
            print emsg
            raise TypeError(emsg)
        
    return f

# Takes a predicate pred, a format string msg, and
# and field names (keywords). 
# Returns a function f that takes variable arity keyword args.
# If pred is true on args, returns args.
# Otherwise, prints an error message and then raises an Assertion
# Error.
# The format string of the error uses msg and the fields.
#
# E.g.,
# q = check2(lambda r: r["x"] > r["y"], "%s not > %s", "x", "y")
# q(x=3, y=4)
# raises an Assertion Error. 

def check2(pred, msg, *fields):
    def f(**args):
        if (pred(args)):
            return args
        else:
            fvals = map(lambda x: args[x], fields)
            emsg = format(msg % tuple(fvals))
            print emsg
            raise TypeError(emsg)            
    
    return f




