from weather import GetWeather
from mister import Device
import RPi.GPIO as GPIO
import time

class Ctrl:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		self.mister = Device("Mister", 7)
		self.fan = Device("Fan", 15)
		self.pump = Device("Pump", 11)

	def main(self):
		w = GetWeather()
		self.processWeather(w)

	def processWeather(self, w):
		clouds = w['clouds'] /4
		print("Clouds: ", clouds)
		self.mister.power(True)
		self.fan.power(True)
		rain = 0
		if "3h" in w['rain']:
			rain = w['rain']['3h']

		for i in range(1,25):
			self.fan.power((not self.fan.on) and self.mister.on)
			if i > clouds:
				self.mister.power(False)
			if i < rain :
				self.pump.power(True)
			else:
				self.pump.power(False)
			time.sleep(1)

	def __del__(self):
		GPIO.cleanup()

		
def main():
	ctrl = Ctrl()
	ctrl.main()

if __name__ == "__main__":
	main()
