#!/usr/bin/env python3

import sys
import threading # Import threads module
import random

incercle = 0 # initialize global variable
 
def montecarlo(n): # generate some random point from 0 to n and do the montecarlo formule
    print("Starting thread:", threading.current_thread().name)
    global incercle # same variable as above, but we have to initialize in this block because we don't pass it to the function 
    for i in range(n): # loop to generate number of digit between 0 to n
        x = random.random() # select random number
        y = random.random()
        if ((x**2) + (y**2)) <= 1: # if the 'carré' is egal or inferior to 1, we increment a variable, to know how much number is under 1
            incercle += 1
    print("Ending thread:", threading.current_thread().name)

if __name__ == "__main__": # Initialize main program
    print("Starting thread:", threading.current_thread().name)
    index = int(sys.argv[1]) # arg of user '10 per example' so the montecarlo function will generate 10 digit
    thread = threading.Thread(target=montecarlo, args=(index,)) # Create a worker thread to do the montecarlo function 
    thread.start() # Start the worker thread
    thread.join() # Wait the worker thread
    print("PI= " + str(4 * (incercle / index))) # Calcul of PI by montecarlo function (formule)
    print("Ending thread:", threading.current_thread().name)
