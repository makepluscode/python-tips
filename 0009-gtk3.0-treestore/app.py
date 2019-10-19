import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

COLS = ("datetime", "lat", "lon", "speed")
ROWS = (
    ("2019-09-29 13:31:20", 37.4852379, 127.0360678, 42),    \
    ("2019-09-29 13:31:20", 37.4854221, 127.0360642, 53),    \
    ("2019-09-29 13:31:20", 37.4857363, 127.0360620, 61),    \
    )

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Treeview Example")
        self.set_default_size(960, 540)

        self.liststore = Gtk.ListStore(str, float, float, int)

        for row in ROWS:
            self.liststore.append(row)

        treeview = Gtk.TreeView(model=self.liststore)

        for i in range(len(COLS)):
            # CellRendererText ia an object that renders text into a TreeView cell
            renderer_text = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn(COLS[i], renderer_text, text=i)
            col.set_expand(True)
            treeview.append_column(col)

        self.add(treeview)

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
