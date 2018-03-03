from job import *

# print the val attribute of a job
def printer(j):
    print "printing %s" % j.val


def adder(j):
    if j.cat == "add":
        s = sum(j.val)
        r = Result(sender=adder, job=j, status="succ", val=s)
        return r
    else:
        r = Result(sender=adder, job=j, status="fail", \
                   err=format("msg not understood: %s" % j.cat))
        raise ResultException(r)
    
def main():
    j1 = Job(sender=top, cat="print", val="hello")
    printer(j1)
    try:
        adder(j1)
    except ResultException as e:
        print "e.status = %s" % e.result.status
        print "e.err = %s" % e.result.err
    
    j = Job(sender=top, cat="add", val=[1, 2, 3])
    r = adder(j)
    pj = Job(sender=adder, cat="print", val=r.val)
    printer(pj)

if __name__ == '__main__':
    main()
    
