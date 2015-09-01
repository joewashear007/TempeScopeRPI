from weather import GetWeather
from device import Device
import time
import scheduler

# Simulation
# ---------------------------------------
try:
	simMode = False
	import RPi.GPIO as GPIO
except:
	simMode = True

class Ctrl:
    def __init__(self):
        if not simMode:
            GPIO.setmode(GPIO.BOARD)
        self.devices = [
		Device("Mister", 7, simMode),
		Device("Fan", 15, simMode),
		Device("Pump", 11, simMode)
	]

    def main(self):
        self.processWeather()

    def processWeather(self):
        self.w = GetWeather()
        scheduler.schedule(self)

    def cleanup(self):
	print("")
	print("")
	print("")
	print("Ctrl is being good and Cleaning up!")
	print('----------------------------------')
	for d in self.devices:
		d.power(False)
	print("")
	print("")

def main():
    ctrl = Ctrl()
    try:
        ctrl.main()
    finally:
	ctrl.cleanup()
	if not simMode:
		GPIO.cleanup()
        scheduler.cleanUp()

if __name__ == "__main__":
    main()
