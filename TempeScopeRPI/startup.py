import RPi.GPIO as GPIO
from time import sleep

def flash():
    GPIO.output(12, True)
    GPIO.output(16, True)
    sleep(1)
    GPIO.output(12, False)
    GPIO.output(16, False)
    sleep(1)

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

def stop():
    GPIO.cleanup()

def main():
    init()
    flash()
    flash()
    flash()
    flash()
    flash()
    stop()

if __name__ == "__main__":
    main()

