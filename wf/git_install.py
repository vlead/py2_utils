# Clone a repo if it doesn't exist, pull it otherwise

# check if ws directory exists.
import os

class GitInstallTask(Task):
    def __init__(self, wd, repo, branch=None, cmd="", ws=None,  **args):
        self.wd = wd
        self.repo = repo
        
        self.ws = ws
        self.branch = branch
        self.run=run
        super(GitInstallTask, self).__init__(**args)

    # pre:
    # repo looks like a git repo
    # wd is an existing directory
    def pre(self):
        if not is_git_repo(self.repo):  # 1
            return False
        if not os.path.isdir(self.wd):  # 2
            return False

    def action(self):
        if (self.ws == None):
            self.init_ws = self.ws
            self.ws = (os.path.splitext(leafname(urlparse(self.repo).path)))[0]
        if os.path.isdir(os.path.join(self.wd, self.ws)):
            # it's a git pull
            git_pull
        else:
            git_clone

        

        

        

        

