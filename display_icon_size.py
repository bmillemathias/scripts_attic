#!/usr/bin/env python
# author: Baptiste Mille-Mathias
# This script displays all sizes (provided by Gtk.IconSize) for a given icon and
# will also display its symbolic counterpart

import sys
from gi.repository import Gtk

try:
    icon_name = sys.argv[1]
except IndexError:
    print "provide an icon name (see http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html)"
    sys.exit(1)

w = Gtk.Window()
w.connect("delete-event", Gtk.main_quit)

box = Gtk.Box()
w.add(box)

# TODO: Find a way to enumerate all Gtk.IconSize
for size in range(0,7):
    vbox = Gtk.VBox()

    i1 = Gtk.Image()
    i1.set_from_icon_name(icon_name, size)

    i2 = Gtk.Image()
    i2.set_from_icon_name(icon_name + "-symbolic", size)

    b1 = Gtk.Button()
    b1.set_image(i1)

    b2 = Gtk.Button()
    b2.set_image(i2)

    vbox.add(b1)
    vbox.add(b2)
    box.add(vbox)

w.show_all()
Gtk.main()
