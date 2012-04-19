import os
import re
import uuid

class Note(object):
    title = "New Note"
    html = "<html>\n<head>\n<title>\n%s\n</title>\n</head>\n" \
           "<body contenteditable=\"true\">\ntest\n</body>\n</html>" % title

    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(filename):
            return

        self.html = open(filename).read()

        result = re.findall(r"<head>.*<title>(.*)</title>.*</head>", self.html,
                            re.DOTALL)
        assert len(result) == 1

        self.title = result[0].strip()

    @staticmethod
    def create():
        return Note(os.path.join(os.path.expanduser("~"), ".gitnote", "notes",
                    "%s.note" % uuid.uuid4()))
    def save(self):
       open(self.filename, "w").write(self.html)

    def get_title(self):
        return self.title

    def get_html(self):
        return self.html

    def set_html(self, value):
        value = re.sub(r"([^\n])<", lambda i: "%s\n<" % i.groups()[0].rstrip(),
                       value)
        value = re.sub(r">([^\n])", lambda i: ">\n%s" % i.groups()[0].lstrip(),
                       value)
        self.html = value
