from wf.jobs.job import Result
from wf.jobs.job import ResultException

from sh_utils.run_cmd import run_cmd

def check_admissible(cls, job):
    if not cls.is_admissible(job):
        raise Result(sender=cls, job=job, status='fail', \
                     err=format("job not admissible: %s" % job))

def check_pre(cls, job):
    if not cls.pre(job):
        raise Result(sender=cls, job=job, status='fail', \
                     err=format("job not ready: %s" % job))

def check_do(cls, job, s, **args):
    try:
        print s
        ans = run_cmd(s)
        print "ans =  %s" % ans
        return Result(sender=cls, job=job, \
                   status="succ", cmd=s, output=ans, \
                   **args)
    except Exception as e:
        print "exception:  %s " % e
        r = Result(sender=cls, job=job, status="fail", \
                   cmd=s, err=format("system exception: %s" % e), \
                   exn=e)
        raise ResultException(r)


