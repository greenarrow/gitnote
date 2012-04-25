#!/usr/bin/env python

import os
import sys
import gtk

from gitnote.editor import Editor
from gitnote.tray import Tray
from gitnote.note import Note
from gitnote.catalogue import Catalogue


PATH_NOTES = os.path.join(os.path.expanduser("~"), ".gitnote", "notes")


if __name__ == "__main__":
    assert len(sys.argv) > 1

    if sys.argv[1] == "catalogue":
        c = Catalogue(PATH_NOTES)
        for title in c.get_titles():
            print title

        sys.exit(0)

    elif sys.argv[1] == "new":
        c = Catalogue(PATH_NOTES)
        n = Note.create(c.get_new_title())
        e = Editor(n)
        e.show_all()

    elif sys.argv[1] == "load":
        c = Catalogue(PATH_NOTES)
        for arg in sys.argv[2:]:
            n = Note(arg)
            e = Editor(n, c)
            e.show_all()

    elif sys.argv[1] =="tray":
        c = Catalogue(PATH_NOTES)
        t = Tray(c)

    else:
        sys.exit(1)

    gtk.main()

