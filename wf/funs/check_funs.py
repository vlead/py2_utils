from wf.jobs.job import *

from sh_utils.run_cmd import run_cmd

def check_admissible(cls, job):
    b = cls.is_admissible(job)
    if not b:
        raise JobIllFormed(sender=cls, job=job)
    else:
        return job

def check_pre(cls, job):
    b = cls.pre(job)
    if not b:
        raise JobNotReady(sender=cls, job=job)
    else:
        return job


def check_post(cls, res):
    b = cls.post(res)
    if not b:
        raise ResultPostFailed(sender=cls, result=res)
    else:
        return res

def run_job_cmd(cls, job, s, **args):
    try:
        print s
        ans = run_cmd(s)
        print "ans =  %s" % ans
        return Result(sender=cls, job=job, \
                   cmd=s, output=ans, \
                   **args)
    except Exception as e:
        raise CmdFailed(sender=cls, job=job,  \
                   cmd=s, exn=e, **args)


