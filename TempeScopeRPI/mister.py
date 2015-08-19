import RPi.GPIO as GPIO

PIN = 7
FULL = 10

def Setup():
	GPIO.setup(PIN, GPIO.OUT)

def On():
	print("Mister On")
	GPIO.output(PIN, True)

def Off():
	print("Mister Off")
	GPIO.output(PIN, False)

def play(val):
	timeon = FULL * val / 100;
	# ???
	timeoff = timeon

class Device:
	def __init__(self, name, pin):
		self.name = name
		self.pin = pin
		self.on = False
		GPIO.setup(pin, GPIO.OUT)
	def power(self, on):
		self.on = on
		print(self.name, " => ", self.on)
		GPIO.output(self.pin, self.on)

