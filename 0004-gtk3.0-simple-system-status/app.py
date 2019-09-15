import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject

import os, sys
import time, datetime

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK3.0 Example")
        self.set_default_size(400,360)

        st = os.statvfs("/")
        self.total = (st.f_blocks * st.f_frsize)/1024/1024/1024
        self.used = ((st.f_blocks - st.f_bfree) * st.f_frsize)/1024/1024/1024
        self.free = (st.f_bavail * st.f_frsize)/1024/1024/1024
        self.usage = self.used/self.total

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        vbox.set_valign(Gtk.Align.START)

        # total (GB)
        label = Gtk.Label("Disk Total")
        vbox.pack_start(label, True, True, 8)
        entry = Gtk.Entry()
        entry.set_text(str(self.total)[0:5] + " GB")
        vbox.pack_start(entry, True, True, 0)

        # used (GB)
        label = Gtk.Label("Used Space")
        vbox.pack_start(label, True, True, 8)
        entry = Gtk.Entry()
        entry.set_text(str(self.used)[0:5] + " GB")
        vbox.pack_start(entry, True, True, 0)

        # free (GB)
        label = Gtk.Label("Free Space")
        vbox.pack_start(label, True, True, 8)
        entry = Gtk.Entry()
        entry.set_text(str(self.free)[0:5] + " GB")
        vbox.pack_start(entry, True, True, 0)

        # usage (%)
        label = Gtk.Label("Disk Usage (" + str(self.usage*100)[0:4] + " %) Used")
        vbox.pack_start(label, True, True, 4)
        pbar = Gtk.ProgressBar()
        pbar.set_fraction(self.usage)
        vbox.pack_start(pbar, True, True, 16)

        frm = Gtk.Frame()
        frm.set_border_width(16)
        frm.add(vbox)
        frm.set_label("SYSTEM STATUS")
        self.add(frm)

        self.connect("delete-event", Gtk.main_quit)
        # self.fullscreen()
        self.show_all()
        Gtk.main()

if __name__ == '__main__':
    win = Window()