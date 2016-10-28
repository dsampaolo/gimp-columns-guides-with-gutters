#!/usr/bin/env python2

from gimpfu import *
import gtk


def python_columnvguides(image, columns_num, gutter_width):
    total_gutters_width = (columns_num + 1) * gutter_width
    columns_available_width = image.width - total_gutters_width
    column_width = columns_available_width / columns_num

    offset = 0
    for i in range(0, columns_num):
        if gutter_width > 0:
            offset += gutter_width
            offset = int(offset)
            pdb.gimp_image_add_vguide(image, offset)

        offset += column_width
        offset = int(offset)
        pdb.gimp_image_add_vguide(image, offset)

    return


class VguidesWindow(gtk.Window):
    def __init__(self, img, *args):
        self.img = img
        win = gtk.Window.__init__(self, *args)
        self.connect("destroy", gtk.main_quit)

        self.columns_num = 6
        self.gutter_width = 50

        self.set_border_width(10)
        vbox = gtk.VBox(spacing=10, homogeneous=False)
        self.add(vbox)
        label = gtk.Label("Add V-Guides for Columns with Gutters")
        vbox.add(label)
        label.show()

        table = gtk.Table(rows=2, columns=2, homogeneous=False)
        table.set_col_spacings(10)
        vbox.add(table)

        label = gtk.Label("Number of Columns")
        label.set_alignment(xalign=0.0, yalign=1.0)
        table.attach(label, 0, 1, 0, 1, xoptions=gtk.FILL, yoptions=0)
        label.show()

        self.txt_num_columns = gtk.Entry(0)
        self.txt_num_columns.set_activates_default(True)
        self.txt_num_columns.set_text(str(self.columns_num))
        table.attach(self.txt_num_columns, 1, 2, 0, 1)
        self.txt_num_columns.show()

        label = gtk.Label("Gutter width (px)")
        label.set_alignment(xalign=0.0, yalign=1.0)
        table.attach(label, 0, 1, 1, 2, xoptions=gtk.FILL, yoptions=0)
        label.show()

        self.txt_gutter_width = gtk.Entry(0)
        self.txt_gutter_width.set_activates_default(True)
        self.txt_gutter_width.set_text(str(self.gutter_width))
        table.attach(self.txt_gutter_width, 1, 2, 1, 2)
        self.txt_gutter_width.show()

        table.show()

        hbox = gtk.HBox(spacing=20)

        btn = gtk.Button("Create my Guides !")
        btn.connect("clicked", self.create_vguides)
        hbox.add(btn)

        vbox.add(hbox)

        btn.show()
        hbox.show()

        vbox.show()

        self.show()
        return win

    def change_columns_num(self, val):
        self.columns_num = int(val.value)

    def change_gutter_width(self, val):
        self.gutter_width = int(val.value)

    def create_vguides(self, dummy):
        self.columns_num = int(self.txt_num_columns.get_text())
        self.gutter_width = int(self.txt_gutter_width.get_text())

        total_gutters_width = (self.columns_num + 1) * self.gutter_width
        columns_available_width = self.img.width - total_gutters_width
        column_width = columns_available_width / self.columns_num

        offset = 0
        for i in range(0, self.columns_num):
            if self.gutter_width > 0:
                offset += self.gutter_width
                offset = int(offset)
                pdb.gimp_image_add_vguide(self.img, offset)

            offset += column_width
            offset = int(offset)
            pdb.gimp_image_add_vguide(self.img, offset)

        gtk.main_quit()


def vguides_designer(image, layer):
    v = VguidesWindow(image)
    gtk.main()


register(
    "python_fu_columnvguides",
    "Multi V-Guides",
    "Add vertical Guides for columns with gutters",
    "DSampaolo",
    "DSampaolo",
    "2016",
    "<Image>/Image/Guides/VGuides...",
    "*",
    [],
    [],
    vguides_designer)

main()
