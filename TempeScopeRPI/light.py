import RPi.GPIO as GPIO
import time

PIN_RED = 12
PIN_BLUE = 16

_red = None
_blue = None
def Setup():
	GPIO.setup(PIN_RED, GPIO.OUT)
	GPIO.setup(PIN_BLUE, GPIO.OUT)
	_red = GPIO.PWM(PIN_RED, 50)
	_blue = GPIO.PWM(PIN_BLUE, 50)

def On():
	print("Light On")
	GPIO.output(PIN_BLUE, True)
	GPIO.output(PIN_RED, True)

def Off():
	print("Light Off")
	GPIO.output(PIN_BLUE, False)
	GPIO.output(PIN_RED, False)

def Play():
	for t in range(0,101,5):
		_red.ChangeDutyCycle(t)
		_blue.ChangeDutyCycle(t)
		time.sleep(0.1)
