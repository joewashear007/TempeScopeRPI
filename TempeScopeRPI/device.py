class Device:
    def __init__(self, name, pin, simMode):
        self.name = name
        self.pin = pin
        self.on = False
        self.simulation = simMode
        if not self.simulation:
                  GPIO.setup(pin, GPIO.OUT)
    def power(self, on):
        self.on = on
        print(self.name, "=>", self.on)
        if not self.simulation:
                  GPIO.output(self.pin, self.on)
