import time
import RPi.GPIO as GPIO

def Start():
    pin = 26
    pin2 = 22
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    p = GPIO.PWM(pin, 50)  # channel=12 frequency=50Hz
    z = GPIO.PWM(pin2, 50)  # channel=12 frequency=50Hz
    p.start(0)
    z.start(0)
    try:
        while 1:
            for dc in range(0, 101, 5):
                print("Setting pin: ", pin , " to ", dc)
                p.ChangeDutyCycle(dc)
                z.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                print("Setting pin: ", pin  , " to ", dc)
                p.ChangeDutyCycle(dc)
                z.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    p.stop()
    z.stop()
    GPIO.cleanup()
