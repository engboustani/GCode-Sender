#!/usr/bin/python

import sys, glob, serial, time, re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from OpenGL import GL
from gui import Ui_MainWindow
from gcode import GCode

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui = Ui_MainWindow()
	ui.show()
	sys.exit(app.exec_())