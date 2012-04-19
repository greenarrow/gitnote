#!/usr/bin/env python

import os
import sys
import glob
import gtk

from gitnote.editor import Editor
from gitnote.note import Note


PATH_NOTES = os.path.join(os.path.expanduser("~"), ".gitnote", "notes")


if __name__ == "__main__":
    assert len(sys.argv) > 1

    if sys.argv[1] == "catalogue":
        for filename in glob.glob(os.path.join(PATH_NOTES, "*.note")):
            print Note(filename).get_title()

        sys.exit(0)

    elif sys.argv[1] == "new":
        n = Note.create()
        e = Editor(n)
        e.show_all()

    elif sys.argv[1] == "load":
        for arg in sys.argv[2:]:
            n = Note(arg)
            e = Editor(n)
            e.show_all()

    gtk.main()

