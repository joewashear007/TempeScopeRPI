
print("Starting Open TempeScope")
import time
import fan
import mister
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
fan.Setup()
mister.Setup()

mister.On()
fan.On()
time.sleep(5)
mister.Off()
fan.Off()

GPIO.cleanup()
