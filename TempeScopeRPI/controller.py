import time
import sched
import states
from weather import GetWeather
from device import Device
from multiprocessing import Process

simMode = False
try :
    import RPi.GPIO as GPIO
except:
    simMode = True

    
# how many seconds should pass between fetching the weather info
LOOP_TIMEOUT = 10

class Ctrl:
    def __init__(self):
        if not simMode:
            GPIO.setmode(GPIO.BOARD)
        
        self.devices = [Device("Mister", 7), Device("Fan", 15), Device("Pump", 11)]
        
        self.threads = []

    def run(self):
        self._setupScheduler()
        while True:
            self._runTasks()

    def _setupScheduler(self):
        self.threads[:] = []
        self.sched = sched.scheduler(time.time, time.sleep)
        
    def _addTasks(self, weather):
        print('--> ADDING DEVICES ')
        self.threads = []
        for device in self.devices:
            on, off = states.GetSchedule(device.name, weather)
            print(device.name, " Timing: ", on, "/", off)
            self.threads.append(Process(target=self.processWeather, args=(device, on, off)))
        print(' --> Done!')
        
    def _cleanTasks(self):
        for t in self.threads:
            if t.is_alive():
                t.terminate()
                # time.sleep(0.1)
                # print("Killed => ", t.is_alive(), t.exitcode)
        
    def _runTasks(self):
        print(" --> RUNING!")
        self._addTasks(GetWeather());   
        for t in self.threads:
            t.daemon = True
            t.start()
        time.sleep(LOOP_TIMEOUT)
        self._cleanTasks()
        # self.sched.enter(LOOP_TIMEOUT, 1, self._runTasks, () )
        # self.sched.run()
        
        
    def processWeather(self, device, on , off):
        try:
            device.power(True)
            time.sleep(on)
            device.power(False)
            time.sleep(off)
            self.processWeather(device, on, off)
        except Exception as e:
            print("hmmm, process didn't end well")
            print(e)
        # clouds = w['clouds'] /4
        # print("Clouds: ", clouds)
        # self.mister.power(True)
        # self.fan.power(True)
        # rain = 0
        # if "3h" in w['rain']:
            # rain = w['rain']['3h']

        # for i in range(1,25):
            # self.fan.power((not self.fan.on) and self.mister.on)
            # if i > clouds:
                # self.mister.power(False)
            # if i < rain :
                # self.pump.power(True)
            # else:
                # self.pump.power(False)
            # time.sleep(1)

    def __del__(self):
        if not simMode:
            GPIO.cleanup()


            
if __name__ == "__main__":
    ctrl = Ctrl()
    ctrl.run()
