#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

from multiprocessing import Process
import os
import time
import sys
import signal

# Program to display the Fibonacci sequence up to n-th term
def child(data):
  print('My PID is:', os.getpid())
  #nterms = int(input("How many terms? "))
  nterms = data
  # first two terms
  n1, n2 = 0, 1
  count = 0
  # check if the number of terms is valid
  if nterms <= 0:
     print("Please enter a positive integer")
  elif nterms == 1:
     print("Fibonacci sequence upto",nterms,":")
     print(n1)
  else:
     print("Fibonacci sequence:")
     while count < nterms:
         print(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1
         time.sleep(2)
         print("Send Kill Signal to father Process")
         os.kill(os.getppid(), signal.SIGUSR1)

def handler(sig, stack):
    if sig == signal.SIGUSR1:
      print('Received:', sig)
      os.kill(childPID, signal.SIGKILL)

# Start algo & evalute time #
start_time = time.time() 
if __name__ == "__main__":
  arg1 = int(sys.argv[1]) # take argument script to fibonacci fct
  signal.signal(signal.SIGUSR1, handler) # send signal to handler fct
  childProcess = Process(target=child, args=((arg1,))) # create process and send one parameter
  childProcess.start() # start process
  global childPID # initialize global var, 
  childPID = childProcess.pid # PID of ChildProcess
  childProcess.join() # wait child process to finish
end_time = time.time() 
elaspTime = end_time - start_time
print("time elasped: " "%.2f" % elaspTime + " s")
