import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

import time, datetime

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")

        self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0xFFFF, 0xFFFF, 0xFFFF))

        hbox = Gtk.Box(spacing=80)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=80)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=80)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        self.label11 = Gtk.Label('<span size="50000">' + str(datetime.datetime.now().date()) + '</span>')
        self.label11.set_use_markup(True)
        self.label11.set_line_wrap(True)
        vbox_left.pack_start(self.label11, True, True, 0)

        self.label21 = Gtk.Label('<span size="50000">' + str(datetime.datetime.now().time()) + '</span>')
        self.label21.set_use_markup(True)
        self.label21.set_justify(Gtk.Justification.CENTER)
        vbox_right.pack_start(self.label21, True, True, 0)

        self.add(hbox)

    def redraw(self):
        self.label11.set_label('<span size="50000">' + str(datetime.datetime.now().date()) + '</span>')
        self.label21.set_label('<span size="50000">' + str(datetime.datetime.now().time()) + '</span>')
        return True
        
    def start_refresh_clock_timer(self):
        GObject.timeout_add(1000, self.redraw)        
        return True

win = Window()
win.connect("delete-event", Gtk.main_quit)
# self.fullscreen()
win.start_refresh_clock_timer()
win.show_all()
Gtk.main()
