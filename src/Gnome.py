#!/usr/bin/env python

# Ubuntu Tweak - PyGTK based desktop configure tool
#
# Copyright (C) 2007-2008 TualatriX <tualatrix@gmail.com>
#
# Ubuntu Tweak is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ubuntu Tweak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ubuntu Tweak; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

import pygtk
pygtk.require("2.0")
import gtk
import os
import gconf
import gettext

from Constants import *
from Widgets import ListPack
from Factory import Factory

gettext.install(App, unicode = True)

class Gnome(gtk.VBox):
	"""GNOME Settings"""

	def __init__(self, parent = None):
		gtk.VBox.__init__(self)

		hbox = gtk.HBox(False, 10)
		label = gtk.Label(_("Notification-daemon popup location"))
		label.set_alignment(0, 0.5)
		combobox = Factory.create("gconfcombobox", "popup_location", [_("Top Left"), _("Top Right"), _("Bottom Left"), _("Bottom Right")], ["top_left", "top_right", "bottom_left", "bottom_right"])
		hbox.pack_start(label, False, False, 0)
		hbox.pack_start(combobox)

		box = ListPack(_("<b>GNOME Panel and Menu</b>"), (
			Factory.create("gconfcheckbutton", _("Confirm Message when removing panel"), "confirm_panel_remove"),
			Factory.create("gconfcheckbutton", _("Complete lockdown of the Panel "), "locked_down"),
			Factory.create("gconfcheckbutton", _("Enable panel animations"), "enable_animations"),
			Factory.create("gconfcheckbutton", _("Show Input Method menu on the Context Menu"), "show_input_method_menu"),
			Factory.create("gconfcheckbutton", _("Show Unicode Method menu on the Context Menu"), "show_unicode_menu"),
			hbox,
			))
		self.pack_start(box, False, False, 0)

if __name__ == "__main__":
	from Utility import Test
	Test(Gnome)
