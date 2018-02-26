# cmd returns the output of a shell command
# -------------------------------------------
import commands
def run_cmd(s):
    (status, ans) = commands.getstatusoutput(s)
    if status != 0:
        raise Exception("error running sh command %s" % s)
    return ans

