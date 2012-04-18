import os
import uuid

class Note(object):
    title = "New Note"
    html = "<html>\n<head>\n<title>\n%s\n</title>\n</head>\n" \
           "<body contenteditable=\"true\">\ntest\n</body>\n</html>" % title

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

    def get_html(self):
        return self.html

    def set_html(self, value):
        # TODO munge here: new lines & contenteditable
        self.html = value	
