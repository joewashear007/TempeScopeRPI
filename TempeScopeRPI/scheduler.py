import sched
import time
import random
import states
from multiprocessing import Process

s = sched.scheduler(time.time, time.sleep)
threads = []

def schedule(ctrl):
	cleanUp()
	threads[:] = []
	try:
		print('---------------------------------------------------')
		for device in ctrl.devices:
			if device.name == "Mister":
				on, off = states.GetCloudSchedule(ctrl.w)
				print("Mister Timing: ", on, "/", off)
			if device.name == "Fan":
				on, off = states.GetWindSchedule(ctrl.w)
				print("Fan Timing: ", on, "/", off)
		        z = Process(target=cycle, args=(device, on, off))
		        z.daemon = True
		        threads.append(z)
		        z.start()
		print('---------------------------------------------------')
		s.enter(30, 1, ctrl.processWeather, () )
		s.run()
	except:
		print("Running the process had an error ...")

def cleanUp():
    for t in threads:
        if t.is_alive():
            t.terminate()
            time.sleep(0.1)
            print("Killed => ", t.is_alive(), t.exitcode)

def cycle(device, on, off):
	try:
		device.power(True)
		time.sleep(on)
		device.power(False)
		time.sleep(off)
		cycle(device, on, off)
	except:
		print("hmmm, process didn't end well")

if __name__ == "__main__":
    try:
        schedule(0)
    finally:
        cleanUp()
