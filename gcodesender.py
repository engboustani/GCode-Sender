#!/usr/bin/python

import sys, glob, serial, time, re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from OpenGL import GL
from gui import Ui_MainWindow
from gcode import GCode

def serial_ports():
	if sys.platform.startswith('win'):
		ports = ['COM%s' % (i + 1) for i in range(256)]
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this excludes your current terminal "/dev/tty"
		ports = glob.glob('/dev/tty[A-Za-z]*')
	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*')
	else:
		raise EnvironmentError('Unsupported platform')

	result = []
	for port in ports:
		try:
			s = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	return result

if __name__ == '__main__':
	# Black = (0,0,0)
	# pincolor = (50,50,50)
	# size = (500,500)
	# screen = pygame.display.set_mode(size)
	# done = False

	# print(serial_ports())

	# ser = serial.Serial('COM4', 115200, timeout=1);
	# if ser.is_open == True:
	# 	ser.close()
	# ser.open()
	# ser.write(b"\r\n\r\n")
	# time.sleep(2)
	# ser.flushInput()
	# oldx = 250
	# oldy = 250
	# for code in codes:
	# 	print(code.encode('ascii'))
	# 	ser.write(code.encode('ascii'))
	# 	result = ser.readline()
	# 	print(result)
	# 	point = getPoint(code)
	# 	if point != None:
	# 		if point == "pindown":
	# 			pincolor = (255,255,255)
	# 		elif point == "pinup":
	# 			pincolor = (50,50,50)
	# 		else:
	# 			x = (point[0] * 4) + 250
	# 			y = (point[1] * 4) + 250
	# 			pygame.draw.line(screen, pincolor, [oldx, oldy], [x, y], 1)
	# 			oldx = x
	# 			oldy = y
	# 		pygame.display.flip()
	# 		pygame.event.get()
	# ser.close()
	app = QApplication(sys.argv)
	ui = Ui_MainWindow()
	ui.show()
	# oldx = 0
	# oldy = 0
	# for code in codes:
	# 	point = gcode.getPoint(code)
	# 	if point != None:
	# 		if point == "pindown":
	# 			pen.setColor(QColor(255, 255, 255, 255))
	# 		elif point == "pinup":
	# 			pen.setColor(QColor(50, 50, 50, 255))
	# 		else:
	# 			x = (point[0] * 4) + 250
	# 			y = (point[1] * 4) + 250
	# 			# pygame.draw.line(screen, pincolor, [oldx, oldy], [x, y], 1)
	# 			painter.drawLine(oldx, oldy, x, y)
	# 			oldx = x
	# 			oldy = y

	sys.exit(app.exec_())