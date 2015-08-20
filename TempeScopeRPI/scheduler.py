import sched, time, random, threading
from multiprocessing import Process

q = 0
s = sched.scheduler(time.time, time.sleep)
threads = []
devices = ["pump", "mister", "fan"]

def m(q):
    cleanUp()
    print("Running Master Loop")
    threads[:] = []
    for key in devices:
        q = q + 1
        on = random.uniform(0.5,5)
        off = random.uniform(0.5,5)
        z = Process(target=cycle, args=(key, on,off, q))
        z.daemon = True
        threads.append(z)
        z.start()
    # time.sleep(5)
    s.enter(30, 1, m, (q, ))
    s.run()
    # s = threading.Timer(5, m, (q,))
    # s.start()
    # m(q)

def cleanUp():
    for t in threads:
        if t.is_alive():
            t.terminate()
            time.sleep(0.1)
            print("Killed: ", q, " => ", t.is_alive(), t.exitcode)
    # for t in threads:

def cycle(key, on, off, q):
    print(q, " => ", key , " - Active (", on ,")" )
    time.sleep(on)
    print(q, " => ", key , " - Deactive (", off ,")" )
    time.sleep(off)
    cycle(key, on, off, q)
    # s.enter(devices[i][x], 2, cycle, (i, not a))

if __name__ == "__main__":
    try:
        m(0)
    finally:
        cleanUp()
