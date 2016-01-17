#!/usr/bin/python

import sys, glob, serial, time, pygame
from tkinter import *
from tkinter import ttk

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

def openGCode(path):
	fo = open(path, "r+")
	code = ""
	codes = []
	for line in fo:
		c = line
		c = c.replace(" ", "")
		if c[0] == 'G' or c[0] == 'M':
			f = c.find("(")
			if f != -1:
				c = c[:f]
			else:
				c = c[:-1]
			c += '\n'
			codes += [c]
			# print(c)
	return codes

def getPoints(gcode):
	points = []
	x = 0.0
	y = 0.0
	z = 0.0
	f = 0.0
	for code in gcode:
		if(code[:2] == "G1"):
			spilt = re.findall(r'[A-Za-z][-?\d.]+', code[2:])
			print(spilt)
			for obj in spilt:
				if obj[0] == 'x' or obj[0] == 'X':
					x = float(obj[1:])
				if obj[0] == 'y' or obj[0] == 'Y':
					y = float(obj[1:])
				if obj[0] == 'z' or obj[0] == 'Z':
					z = float(obj[1:])
				if obj[0] == 'f' or obj[0] == 'F':
					f = float(obj[1:])
			points += [(x,y,z,f)]
		elif(code[:6] == "M300S3"):
			points += ["pindown"]
		elif(code[:6] == "M300S5"):
			points += ["pinup"]
	return points

def getPoint(code):
	x = 0.0
	y = 0.0
	z = 0.0
	f = 0.0
	if(code[:2] == "G1"):
		spilt = re.findall(r'[A-Za-z][-?\d.]+', code[2:])
		print(spilt)
		for obj in spilt:
			if obj[0] == 'x' or obj[0] == 'X':
				x = float(obj[1:])
			if obj[0] == 'y' or obj[0] == 'Y':
				y = float(obj[1:])
			if obj[0] == 'z' or obj[0] == 'Z':
				z = float(obj[1:])
			if obj[0] == 'f' or obj[0] == 'F':
				f = float(obj[1:])
		return (x,y,z,f)
	elif(code[:6] == "M300S3"):
		return "pindown"
	elif(code[:6] == "M300S5"):
		return "pinup"
	else:
		return None

if __name__ == '__main__':
	pygame.init()
	Black = (0,0,0)
	pincolor = (50,50,50)
	size = (500,500)
	screen = pygame.display.set_mode(size)
	done = False
	codes = openGCode("unicorn.gcode")
	print(codes)
	print(serial_ports())
	# points = getPoints(codes)
	# screen.fill(Black)
	# oldx = (points[0][0] * 4) + 250
	# oldy = (points[0][1] * 4) + 250
	# for point in points[1:]:
	# 	if point == "pindown":
	# 		pincolor = (255,255,255)
	# 	elif point == "pinup":
	# 		pincolor = (50,50,50)
	# 	else:
	# 		x = (point[0] * 4) + 250
	# 		y = (point[1] * 4) + 250
	# 		pygame.draw.line(screen, pincolor, [oldx, oldy], [x, y], 1)
	# 		oldx = x
	# 		oldy = y
	# pygame.display.flip()

	ser = serial.Serial('COM4', 115200, timeout=1);
	if ser.is_open == True:
		ser.close()
	ser.open()
	ser.write(b"\r\n\r\n")
	time.sleep(2)
	ser.flushInput()
	oldx = 250
	oldy = 250
	for code in codes:
		print(code.encode('ascii'))
		ser.write(code.encode('ascii'))
		result = ser.readline()
		print(result)
		point = getPoint(code)
		if point != None:
			if point == "pindown":
				pincolor = (255,255,255)
			elif point == "pinup":
				pincolor = (50,50,50)
			else:
				x = (point[0] * 4) + 250
				y = (point[1] * 4) + 250
				pygame.draw.line(screen, pincolor, [oldx, oldy], [x, y], 1)
				oldx = x
				oldy = y
			pygame.display.flip()
			pygame.event.get()
	input("Press Enter to continue...")
	pygame.quit()
	ser.close()