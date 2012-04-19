import os
import re
import uuid


class MetaNote(object):
    def __init__(self, filename):
        self.filename = filename
        self._read_meta(open(self.filename).read())
        self._read_mtime()

    def _read_meta(self, html):
        result = re.findall(r"<head>.*<title>(.*)</title>.*</head>", html,
                            re.DOTALL)
        assert len(result) == 1

        self.title = result[0].strip()

    def _read_mtime(self):
        self.mtime = os.stat(self.filename).st_mtime

    def get_title(self):
        return self.title

    def get_mtime(self):
        return self.mtime


class Note(MetaNote):
    title = "New Note"
    html = "<html>\n<head>\n<title>\n%s\n</title>\n</head>\n" \
           "<body contenteditable=\"true\">\ntest\n</body>\n</html>" % title

    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(filename):
            return

        self.html = open(filename).read()
        self._read_meta(self.html)
        self._read_mtime()

    @staticmethod
    def create():
        return Note(os.path.join(os.path.expanduser("~"), ".gitnote", "notes",
                    "%s.note" % uuid.uuid4()))

    @staticmethod
    def from_meta(meta):
        return Note(meta.filename)

    def save(self):
       open(self.filename, "w").write(self.html)
       self._read_mtime()

    def get_html(self):
        return self.html

    def set_html(self, value):
        value = re.sub(r"([^\n])<", lambda i: "%s\n<" % i.groups()[0].rstrip(),
                       value)
        value = re.sub(r">([^\n])", lambda i: ">\n%s" % i.groups()[0].lstrip(),
                       value)
        self.html = value
