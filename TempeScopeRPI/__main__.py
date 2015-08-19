from weather import GetWeather
import time
import fan
import mister
import pump
import light
import RPi.GPIO as GPIO

def main():
	w = GetWeather()
	print(w)
	mister.On()
	fan.On()
	pump.On()
	light.On()
	time.sleep(5)
	mister.Off()
	fan.Off()
	pump.Off()
	light.Off()

def startup():
	GPIO.setmode(GPIO.BOARD)
	fan.Setup()
	pump.Setup()
	mister.Setup()
	light.Setup()

def shutdown():
	GPIO.cleanup()


if __name__ == "__main__":
	startup()
	main()
	shutdown()
