#
# Example Text Editor
# Ryan Paul (SegPhault) - 07/12/2009
#

import gtk, webkit

class Editor(gtk.Window):
  def __init__(self, note, catalogue=None):
    self.catalogue = catalogue
    self.note = note

    gtk.Window.__init__(self)
    self.set_title(note.get_title())
    self.resize(500, 500)

    self.editor = webkit.WebView()
    self.editor.set_editable(True)
    self.editor.load_html_string(note.get_html(), "file:///")

    scroll = gtk.ScrolledWindow()
    scroll.add(self.editor)
    scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

    self.ui = self.generate_ui()
    self.add_accel_group(self.ui.get_accel_group())
    self.toolbar = self.ui.get_widget("/toolbar_main")

    self.layout = gtk.VBox()
    self.layout.pack_start(self.toolbar, False)
    self.layout.pack_start(scroll, True, True)
    self.add(self.layout)

  def generate_ui(self):
    ui_def = """
    <ui>
      <toolbar name="toolbar_main">
        <toolitem action="undo" />
        <toolitem action="redo" />
        <separator />
        <toolitem action="cut" />
        <toolitem action="copy" />
        <toolitem action="paste" />
        <separator />
        <toolitem action="bold" />
        <toolitem action="italic" />
        <toolitem action="underline" />
        <toolitem action="strikethrough" />
        <separator />
        <toolitem action="font" />
        <toolitem action="color" />
        <separator />
        <toolitem action="justifyleft" />
        <toolitem action="justifyright" />
        <toolitem action="justifycenter" />
        <toolitem action="justifyfull" />
        <separator />
        <toolitem action="insertunorderedlist" />
      </toolbar>
      <accelerator action="bold" />
      <accelerator action="italic" />
      <accelerator action="underline" />
      <accelerator action="strikethrough" />
      <accelerator action="font" />
      <accelerator action="insertunorderedlist" />
    </ui>
    """

    actions = gtk.ActionGroup("Actions")
    actions.add_actions([
      ("undo", gtk.STOCK_UNDO, "_Undo", None, None, self.on_action),
      ("redo", gtk.STOCK_REDO, "_Redo", None, None, self.on_action),

      ("cut", gtk.STOCK_CUT, "_Cut", None, None, self.on_action),
      ("copy", gtk.STOCK_COPY, "_Copy", None, None, self.on_action),
      ("paste", gtk.STOCK_PASTE, "_Paste", None, None, self.on_paste),

      ("bold", gtk.STOCK_BOLD, "_Bold", "<ctrl>B", None, self.on_action),
      ("italic", gtk.STOCK_ITALIC, "_Italic", "<ctrl>I", None, self.on_action),
      ("underline", gtk.STOCK_UNDERLINE, "_Underline", "<ctrl>U", None,
       self.on_action),
      ("strikethrough", gtk.STOCK_STRIKETHROUGH, "_Strike", "<ctrl>S", None,
       self.on_action),
      ("font", gtk.STOCK_SELECT_FONT, "Select _Font", "<ctrl>F", None,
       self.on_select_font),
      ("color", gtk.STOCK_SELECT_COLOR, "Select _Color", None, None,
       self.on_select_color),

      ("justifyleft", gtk.STOCK_JUSTIFY_LEFT, "Justify _Left", None, None,
       self.on_action),
      ("justifyright", gtk.STOCK_JUSTIFY_RIGHT, "Justify _Right", None, None,
       self.on_action),
      ("justifycenter", gtk.STOCK_JUSTIFY_CENTER, "Justify _Center", None, None,
       self.on_action),
      ("justifyfull", gtk.STOCK_JUSTIFY_FILL, "Justify _Full", None, None,
       self.on_action),

      ("insertunorderedlist", gtk.STOCK_INDEX, "Insert _UnorderedList",
       "<alt>Right", None, self.on_action),

    ])

    self.connect("delete_event", self.on_delete)

    ui = gtk.UIManager()
    ui.insert_action_group(actions)
    ui.add_ui_from_string(ui_def)
    return ui

  def on_delete(self, event, data=None):
    self.note.set_html(self.get_html())
    self.note.save()

    if self.catalogue is not None:
      self.catalogue.commit(self.note)

  def on_action(self, action):
    self.editor.execute_script(
      "document.execCommand('%s', false, false);" % action.get_name())

  def on_paste(self, action):
    self.editor.paste_clipboard()

  def on_select_font(self, action):
    dialog = gtk.FontSelectionDialog("Select a font")
    if dialog.run() == gtk.RESPONSE_OK:
      fname = dialog.fontsel.get_family().get_name()
      fsize = dialog.fontsel.get_size()
      self.editor.execute_script("document.execCommand('fontname', null, '%s');"
                                 % fname)
      self.editor.execute_script("document.execCommand('fontsize', null, '%s');"
                                 % fsize)
    dialog.destroy()

  def on_select_color(self, action):
    dialog = gtk.ColorSelectionDialog("Select Color")
    if dialog.run() == gtk.RESPONSE_OK:
      gc = str(dialog.colorsel.get_current_color())
      color = "#" + "".join([gc[1:3], gc[5:7], gc[9:11]])
      self.editor.execute_script("document.execCommand('forecolor', null, " \
                                 "'%s');" % color)
    dialog.destroy()

  def get_html(self):
    self.editor.execute_script("document.title=document.documentElement" \
                               ".innerHTML;")
    return self.editor.get_main_frame().get_title()


