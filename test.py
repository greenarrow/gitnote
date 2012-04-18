#!/usr/bin/env python

import sys
import gtk

from gitnote.editor import Editor
from gitnote.note import Note

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = Note(sys.argv[1])
    else:
        n = Note.create()

    e = Editor(n)
    e.show_all()
    gtk.main()

