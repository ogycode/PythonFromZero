print("Threading, (c) Verloka Vadim 2018\n\n\n")

import threading
import time

tLock = threading.Lock()

def Timer(name, delaySec, repeat, lock = False):
    print("Timer {} started.".format(name))

    if lock:
        tLock.acquire()

    while repeat > 0:
        time.sleep(delaySec)
        print("{}: {}".format(name, time.ctime(time.time())))
        repeat -= 1

    if lock:
        tLock.release()

    print("Timer {} completed.".format(name))

def Main():
    #Четыри потока, которые будут работать одновременно
    t1 = threading.Thread(target=Timer, args=("Timer 1", 1, 5, True))
    t2 = threading.Thread(target=Timer, args=("Timer 2", 1, 5, True))
    t3 = threading.Thread(target=Timer, args=("Timer 3", 1, 5, True))
    t4 = threading.Thread(target=Timer, args=("Timer 3", 1, 5, True))
    t5 = threading.Thread(target=Timer, args=("Timer 4", 1, 5, False))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    print("Main is completed.")

if __name__ == "__main__":
    Main()