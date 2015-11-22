simMode = False
try:
    import RPi.GPIO as GPIO
except:
    simMode = True


class Device:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.on = False
        if not simMode:
            GPIO.setup(pin, GPIO.OUT)
            
    def power(self, on):
        self.on = on
        print(self.name, " => ", self.on)
        if not simMode:
            GPIO.output(self.pin, self.on)

