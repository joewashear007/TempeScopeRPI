import sched
import time
import random
from multiprocessing import Process

s = sched.scheduler(time.time, time.sleep)
threads = []

def schedule(ctrl):
    cleanUp()
    threads[:] = []
    timeMax = 0
    print('---------------------------------------------------')
    for device in ctrl.devices:
        on = random.uniform(0.5,5)
        off = random.uniform(0.5,5)
        z = Process(target=cycle, args=(device, on, off))
        z.daemon = True
        threads.append(z)
        print(' =>', device.name, ' - On:', on, '/ Off:', off)
        timeMax = max(timeMax, on + off)
        z.start()
    print(' => Time Loop: ', timeMax, ' Cycles:', (30 / timeMax))
    print('---------------------------------------------------')
    s.enter(30, 1, schedule, (ctrl, ))
    s.run()

def cleanUp():
    for t in threads:
        if t.is_alive():
            t.terminate()
            time.sleep(0.1)
            print("Killed => ", t.is_alive(), t.exitcode)

def cycle(device, on, off):
    device.power(True)
    time.sleep(on)
    device.power(False)
    time.sleep(off)
    cycle(device, on, off)

if __name__ == "__main__":
    try:
        schedule(0)
    finally:
        cleanUp()
