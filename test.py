#!/usr/bin/env python

import gtk

from gitnote.editor import Editor

if __name__ == "__main__":
    e = Editor()
    e.show_all()
    gtk.main()
