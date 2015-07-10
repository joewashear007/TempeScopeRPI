import RPi.GPIO as GPIO

PIN = 7

def Setup():
	GPIO.setup(PIN, GPIO.OUT)

def On():
	print("Mister On")
	GPIO.output(PIN, True)

def Off():
	print("Mister Off")
	GPIO.output(PIN, False)
