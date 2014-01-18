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
w.set_title("Icon Viewer")
w.connect("delete-event", Gtk.main_quit)

grid = Gtk.Grid()
grid.set_column_homogeneous(True)

label = Gtk.Label()
label.set_markup("<b>%s</b>" % icon_name)
grid.attach(label, 0, 0, 7, 1)

# TODO: Find a way to enumerate all Gtk.IconSize
for size in Gtk.IconSize.__enum_values__:
    i1 = Gtk.Image()
    i1.set_from_icon_name(icon_name, size)

    i2 = Gtk.Image()
    i2.set_from_icon_name(icon_name + "-symbolic", size)

    b1 = Gtk.Button()
    b1.set_image(i1)
    b1.set_tooltip_text(Gtk.IconSize.__enum_values__[size].__str__())

    b2 = Gtk.Button()
    b2.set_image(i2)
    b2.set_tooltip_text(Gtk.IconSize.__enum_values__[size].__str__())

    grid.attach(b1, size, 1, 1, 1)
    grid.attach(b2, size, 2, 1, 1)

w.add(grid)
w.show_all()
Gtk.main()
