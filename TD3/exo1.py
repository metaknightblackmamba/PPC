#!/usr/bin/env python3

import sys
import threading
import random

incercle = 0

def montecarlo(n):
    print("Starting thread:", threading.current_thread().name)
    global incercle
    for i in range(n):
        x = random.random()
        y = random.random()
        if ((x**2) + (y**2)) <= 1:
            incercle += 1
    print("Ending thread:", threading.current_thread().name)

if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)
    index = int(sys.argv[1])
    thread = threading.Thread(target=montecarlo, args=(index,))
    thread.start()
    thread.join()
    print("PI= " + str(4 * (incercle / index)))
    print("Ending thread:", threading.current_thread().name)
