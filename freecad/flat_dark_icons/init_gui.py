import os
import FreeCADGui
import FreeCAD
from PySide import QtGui
from PySide import QtCore

RCCPATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Flat_Dark.rcc")
THEME_NAME = "Modern icons for Dark Themes"
# register the .rcc resource
FreeCAD.Console.PrintMessage("Running the init_gui file for our icon theme automation!\n")
FreeCAD.Console.PrintWarning(f"path is {RCCPATH}\n")

QtCore.QResource.registerResource(RCCPATH)
QtGui.QIcon.setThemeName("Flat")
