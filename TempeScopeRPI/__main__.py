
print("Starting Open TempeScope")
import time
import fan
import mister
import pump
import light
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
fan.Setup()
pump.Setup()
mister.Setup()
light.Setup()

mister.On()
fan.On()
pump.On()
light.On()
time.sleep(5)
mister.Off()
fan.Off()
pump.Off()
light.Off()

GPIO.cleanup()
