import os
import glob
import note


class Catalogue(object):
    def __init__(self, path):
        self.notes = map(note.MetaNote, glob.glob(os.path.join(path, "*.note")))
        self.notes.sort(key=lambda n: n.get_mtime(), reverse=True)

    def get_notes(self):
        return self.notes

    def get_titles(self):
        return map(lambda n: n.get_title(), self.notes)
