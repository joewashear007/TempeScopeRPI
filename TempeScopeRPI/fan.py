import RPi.GPIO as GPIO

PIN = 15

def Setup():
	GPIO.setup(PIN, GPIO.OUT)

def On():
	print("Fan On")
	GPIO.output(PIN, True)

def Off():
	print("Fan Off")
	GPIO.output(PIN, False)
