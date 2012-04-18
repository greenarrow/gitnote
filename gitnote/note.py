import os
import uuid

class Note(object):
    html = ""
    title = "New Note"

    def __init__(self, filename):
        self.filename = filename

        if os.path.exists(filename):
            self.html = open(filename).read()

    @staticmethod
    def create():
        return Note(os.path.join(os.path.expanduser("~"), ".gitnote",
                    "%s.note" % uuid.uuid4()))
    def save(self):
       open(self.filename, "w").write(self.html)

    def get_title(self):
        return self.title
	
