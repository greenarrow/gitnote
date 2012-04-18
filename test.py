#!/usr/bin/env python

import gtk

from gitnote.editor import Editor
from gitnote.note import Note

if __name__ == "__main__":
    n = Note()
    e = Editor(n)
    e.show_all()
    gtk.main()
