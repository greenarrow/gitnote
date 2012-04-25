import os
import glob
import note
import git


class Catalogue(object):
    def __init__(self, path):
        self.notes = map(note.MetaNote, glob.glob(os.path.join(path, "*.note")))
        self.sort()

        self.repo = git.Repository(path)
        if not self.repo.exists():
            self.repo.init()

    def sort(self):
        self.notes.sort(key=lambda n: n.get_mtime(), reverse=True)

    def append(self, note):
        self.notes.append(note)

    def commit(self, note):
        self.repo.add(note.get_filename())
        self.repo.commit()

    def get_new_title(self):
        titles = self.get_titles()
        new = "New Note"

        i = 2
        while new in titles:
            new = "New Note %d" % i
            i += 1

        return new

    def get_notes(self):
        return self.notes

    def get_titles(self):
        return map(lambda n: n.get_title(), self.notes)
