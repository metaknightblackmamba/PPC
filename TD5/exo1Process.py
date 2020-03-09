#!/usr/bin/env python3

import sys
import multiprocessing # Import multiprocessing module
import random

 
def pi(points, pointsInside): 
    print("Starting thread:", multiprocessing.current_process().name)
    for i in range(points):
        x = random.uniform(-1, 1) 
        y = random.uniform(-1, 1)
        if ((x**2) + (y**2)) <= 1: 
          with pointsInside.get_lock():
            pointsInside.value += 1
    print("Ending thread:", multiprocessing.current_process().name)





if __name__ == "__main__": # Initialize main program
    print("Starting thread:", multiprocessing.current_process().name)
   
    # default #
    points = 10000 
    nProcess = 4
    
    pointsInside = multiprocessing.Value('d', 0.0)
    
    processes = [multiprocessing.Process(target=pi, args=(points, pointsInside)) for i in range(nProcess)]
    
    for process in processes:
      process.start()

    for process in processes:
      process.join()

    print("PI= ",  4 * pointsInside.value / (nProcess * points))
    print("Ending process:", multiprocessing.current_process().name)
