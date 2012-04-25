import os
import subprocess


class GitError(Exception):
    pass


class Repository(object):
    def __init__(self, path):
        self.path = path

    def _shell(self, args):
        prev = os.getcwd()
        os.chdir(self.path)

        try:
            p = subprocess.Popen(["git"] + list(args))
            if p.wait() != 0:
                raise GitError

        finally:
            os.chdir(prev)

    def exists(self):
        return os.path.isdir(os.path.join(self.path, ".git"))

    def init(self):
        self._shell(["init"])

    def add(self, filename):
        self._shell(["add", filename])

    def commit(self, msg="Auto Commit"):
        self._shell(["commit", "--author=gitnote <gitnote@null.null>",
                     "--message=%s" % msg])

