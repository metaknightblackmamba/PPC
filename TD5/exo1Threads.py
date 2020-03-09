#!/usr/bin/env python3

import sys
import threading # Import threads module
import random

pointsInside = 0 # initialize global variable
 
def pi(points, lock): 
    #print("Starting thread:", threading.current_thread().name)
    global pointsInside # same variable as above, but we have to initialize in this block because we don't pass it to the function 
    for i in range(points):
        x = random.uniform(-1, 1) 
        y = random.uniform(-1, 1)
        if ((x**2) + (y**2)) <= 1: 
          with lock:
            pointsInside += 1
    print("Ending thread:", threading.current_thread().name)





if __name__ == "__main__": # Initialize main program
    print("Starting thread:", threading.current_thread().name)
   
    # default #
    points = 10000 
    nThreads = 4
    
    lock = threading.Lock()
    
    threads = [threading.Thread(target=pi, args=(points, lock)) for i in range(nThreads)]
    
    for thread in threads:
      thread.start()

    for thread in threads:
      thread.join()

    print("PI= ",  4 * pointsInside / (nThreads * points))
    print("Ending thread:", threading.current_thread().name)
