import gtk

from editor import Editor
from note import Note
# TODO right click menu

class Tray(object):
    def __init__(self, catalogue):
        self.catalogue = catalogue

        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_visible(True)
        self.statusicon.set_from_stock(gtk.STOCK_HOME)
        self.statusicon.set_tooltip("Open notes")
        self.statusicon.connect("activate", self.on_activate)

    def on_activate(self, thing):
        self.catalogue.sort()

        rect = self.statusicon.get_geometry()[1]

        menu = gtk.Menu()

        new = gtk.MenuItem("Create &New Note")
        new.connect("activate", self.on_click_new_note)
        menu.append(new)

        for note in self.catalogue.get_notes():
            item = gtk.MenuItem(note.get_title())
            item.connect("activate", self.on_click_note, note)
            menu.append(item)

        quit = gtk.MenuItem("Quit")
        quit.connect("activate", gtk.main_quit)
        menu.append(quit)
        
        menu.show_all()
        
        menu.popup(None, None, lambda i: (rect.x, rect.y + rect.height, True),3,
                   gtk.get_current_event_time())

    def on_click_note(self, item, note):
        n = Note.from_meta(note)
        e = Editor(n)
        e.show_all()

    def on_click_new_note(self, item):
        n = Note.create(self.catalogue.get_new_title())
        self.catalogue.append(n)
        e = Editor(n)
        e.show_all()

