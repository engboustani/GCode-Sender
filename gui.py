# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui, QtOpenGL
from OpenGL.GL import *
from gcode import GCode

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(603, 600)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.widget = GLWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)

        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuTool = QtGui.QMenu(self.menubar)
        self.menuTool.setObjectName(_fromUtf8("menuTool"))
        self.menuPort = QtGui.QMenu(self.menubar)
        self.menuPort.setObjectName(_fromUtf8("menuPort"))
        self.menuBaud = QtGui.QMenu(self.menubar)
        self.menuBaud.setObjectName(_fromUtf8("menuBaud"))
        self.menuTool.addMenu(self.menuPort)
        self.menuTool.addMenu(self.menuBaud)
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))

        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(QtGui.QIcon('open.png'), "&Open...", self)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Open.triggered.connect(self.openFile)
        self.action_Quit = QtGui.QAction(self)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Quit.triggered.connect(self.quitapp)
        self.actionAbout = QtGui.QAction(self)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.startAction = QtGui.QAction(QtGui.QIcon('play.png'), "Start", self)
        self.stopAction = QtGui.QAction(QtGui.QIcon('stop.png'), "Stop", self)
        self.rePort = QtGui.QAction("Refresh", self)
        self.rePort.triggered.connect(self.getPorts)
        self.serialCon = QtGui.QAction(QtGui.QIcon('connection.png'), "Connect", self)
        self.serialCon.triggered.connect(self.toggleConnection)
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.action_Open)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.serialCon)
        self.toolbar.addAction(self.startAction)
        self.toolbar.addAction(self.stopAction)

        self.gcode = GCode()
        self.getPorts()
        self.setBaudrates()
        self.setBaudrate()

        self.setEnablePrintPanel(False)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "GCodeSender (Port: {0}, Baudrate: {1})".format(self.Portname, self.Baudrate), None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTool.setTitle(_translate("MainWindow", "Tool", None))
        self.menuPort.setTitle(_translate("MainWindow", "Port", None))
        self.menuBaud.setTitle(_translate("MainWindow", "Baudrate", None))
        self.action_Open.setText(_translate("MainWindow", "&Open...", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    def quitapp(self):
        self.gcode.serialDisconnect()
        sys.exit(1)

    def openFile(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self,
            "Open GCode", "", "GCode Files (*.gcode *.gc)")
        self.sourcegcode = self.gcode.openGCode(self.fileName)
        self.showList(self.sourcegcode)
        self.widget.setItems(self.sourcegcode)
        self.widget.updateGL()

    def showList(self, items):
        strgcode = ""
        for source in items:
            strgcode += source
        self.textEdit.setText(strgcode)

    def getPorts(self):
        self.menuPort.clear()
        res = self.gcode.serial_ports()
        self.portnameGroup = QtGui.QActionGroup(self, exclusive=True)
        for port in res:
            action = QtGui.QAction(port, self, checkable=True)
            action.triggered.connect(self.setPortname)
            self.portnameGroup.addAction(action)
            self.menuPort.addAction(action)
        self.menuPort.addSeparator()
        self.menuPort.addAction("Refresh")
        actions = self.portnameGroup.actions()
        if len(actions) > 0:
            actions[0].setChecked(True)
            self.Portname = actions[0].text()
        else:
            self.Portname = "None"


    def setPortname(self):
        selected = self.portnameGroup.checkedAction()
        self.Portname = selected.text()
        self.retranslateUi()

    def setBaudrates(self):
        self.baudrateGroup = QtGui.QActionGroup(self, exclusive=True)
        self.baud4800 = QtGui.QAction("4800", self, checkable=True)
        self.baud4800.triggered.connect(self.setBaudrate)
        self.baud9600 = QtGui.QAction("9600", self, checkable=True)
        self.baud9600.triggered.connect(self.setBaudrate)
        self.baud19200 = QtGui.QAction("19200", self, checkable=True)
        self.baud19200.triggered.connect(self.setBaudrate)
        self.baud38400 = QtGui.QAction("38400", self, checkable=True)
        self.baud38400.triggered.connect(self.setBaudrate)
        self.baud57600 = QtGui.QAction("57600", self, checkable=True)
        self.baud57600.triggered.connect(self.setBaudrate)
        self.baud115200 = QtGui.QAction("115200", self, checkable=True)
        self.baud115200.triggered.connect(self.setBaudrate)
        self.baudrateGroup.addAction(self.baud4800)
        self.menuBaud.addAction(self.baud4800)
        self.baudrateGroup.addAction(self.baud9600)
        self.menuBaud.addAction(self.baud9600)
        self.baudrateGroup.addAction(self.baud19200)
        self.menuBaud.addAction(self.baud19200)
        self.baudrateGroup.addAction(self.baud38400)
        self.menuBaud.addAction(self.baud38400)
        self.baudrateGroup.addAction(self.baud57600)
        self.menuBaud.addAction(self.baud57600)
        self.baudrateGroup.addAction(self.baud115200)
        self.menuBaud.addAction(self.baud115200)
        self.baud115200.setChecked(True)
        self.Baudrate = 115200

    def setBaudrate(self):
        selected = self.baudrateGroup.checkedAction()
        self.Baudrate = int(selected.text())
        self.retranslateUi()

    def setEnablePrintPanel(self, action):
        if action == True:
            self.startAction.setEnabled(True)
            self.stopAction.setEnabled(True)
        else:
            self.startAction.setEnabled(False)
            self.stopAction.setEnabled(False)

    def toggleConnection(self):
        if self.gcode.isConnected() == True:
            # try disconnect
            self.gcode.serialDisconnect()
            self.setEnablePrintPanel(False)
        else:
            res = self.gcode.serialConnect(self.Portname, self.Baudrate)
            if res == True:
                self.setEnablePrintPanel(True)
                msgBox = QtGui.QMessageBox(self)
                msgBox.setText("Connect sussfuly")
                msgBox.exec_()
            else:
                msgBox = QtGui.QMessageBox(self)
                msgBox.setText("Can not connect!")
                msgBox.exec_()


class GLWidget(QtOpenGL.QGLWidget):

    items = []

    def __init__(self, parent):
        super(GLWidget, self).__init__(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers), parent)
        self.gcode = GCode()
        self.setAutoFillBackground(False)

    def initializeGL(self):
        """Initialize OpenGL, VBOs, upload data on the GPU, etc.
        """
        # background color
        glClearColor(0,0,0,0)

    def paintGL(self):
        """Paint the scene.
        """
        # clear the buffer
        glClear(GL_COLOR_BUFFER_BIT)
        oldx = 0.0
        oldy = 0.0
        glColor3b(30,30,30)
        for item in self.items:
            # set yellow color for subsequent drawing rendering calls
            if item != None:
                if item == "pindown":
                    glColor3b(80,80,80)
                    glLineWidth(2.0)
                elif item == "pinup":
                    glColor3b(30,30,30)
                    glLineWidth(1.0)
                else:
                    x = item[0]
                    y = item[1]
                    glBegin(GL_LINES)
                    glVertex2f(oldx, oldy)
                    glVertex2f(x, y)
                    glEnd()
                    oldx = x
                    oldy = y

    def resizeGL(self, width, height):
        """Called upon window resizing: reinitialize the viewport.
        """
        # update the window size
        self.width, self.height = width, height
        # paint within the whole window
        glViewport(0, 0, width, height)
        # set orthographic projection (2D only)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # the window corner OpenGL coordinates are (-+1, -+1)
        glOrtho(-100, 100, -100, 100, 1, -1)
        glMatrixMode(GL_MODELVIEW)

    def setItems(self, listitem):
        self.items = self.gcode.getPoints(listitem)

    def wheelEvent(self, event):
        if event.delta() > 0:
            glOrtho(-1.1, 1.1, 1.1, -1.1, 1, -1)
            glOrtho(-1.1, 1.1, 1.1, -1.1, 1, -1)
        else:
            glOrtho(-0.9, 0.9, 0.9, -0.9, 1, -1)
            glOrtho(-0.9, 0.9, 0.9, -0.9, 1, -1)
        self.glDraw()
