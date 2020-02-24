#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import time
import random
import multiprocessing
 
def fibonacci(n):
    print(multiprocessing.current_process().name)
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a+b
        i += 1
    return (n, a)
 
if __name__ == "__main__":
    indexes = [random.randint(0, 100) for i in range(10)] # create 10 value between 0 and 100
 
    with multiprocessing.Pool(processes = 4) as pool: # create a pool of process (number = 4, one per cpu)
        print("*** Synchronous call in one process")
        result = pool.apply(fibonacci, (10,)) # block until get the response
        print(result)
 
        print("*** Asynchronous call in one process")
        result = pool.apply_async(fibonacci, (10,)) # no block
        print(result.get()) # block until get the result , result is an object
 
        print("*** Synchronous map")
        for x in pool.map(fibonacci, indexes): # apply function on a sequence (parallelism); block until finish instruction
            print(x)
 
        print("*** Asynchronous map")
        for x in pool.map_async(fibonacci, indexes).get(): # reply a list
            print(x)
 
        print("*** Lazy map")
        for x in pool.imap(fibonacci, indexes):
            print(x)
 
        print("*** Deliberate timeout")
        result = pool.apply_async(time.sleep, (5,)) # sleep > pause a process
        print(result.get(timeout=1)) #  block until 1s 

