#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import time
import random
import multiprocessing
 
def is_prime(n):
    if n <= 3:
      return n > 1
    else:
      if (n % 2 == 0) or (n % 3 == 0):
        return (n, False)
    i = 5 
    while i * i <= n:
      if (n % i == 0) or (n % (i + 2) == 0):
        return (n, False)
      i = i + 6
    return (n, True)

 
if __name__ == "__main__":
    indexes = [random.randint(10000, 10000000000) for i in range(100000)] # create 10 value between 0 and 100
 
    with multiprocessing.Pool(processes = 4) as pool:
        start = time.time()
        results = pool.map(is_prime, indexes)
        end = time.time()
        elaspTime = end - start
        print("Synchronous map :" + "%.2f" % elaspTime + " s")
        
        start = time.time()
        results = pool.map_async(is_prime, indexes).get()
        end = time.time()
        elaspTime = end - start
        print("Asynchronous map :" + "%.2f" % elaspTime + " s")
 
        start = time.time()
        results = [pool.map_async(is_prime, (n,)).get() for n in indexes]
        end = time.time()
        elaspTime = end - start
        print("Asynchronous apply :" + "%.2f" % elaspTime + " s")
 
