#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

from multiprocessing import Process, Manager
import os
import time
import sys

# Program to display the Fibonacci sequence up to n-th term
def sequenceFib(data, lst):
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
     print("Fibonacci sequence via child process:")
     while count < nterms:
         print(n1)
         lst.append(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1


# Start algo & evalute time #
start_time = time.time() # start_time = 0 
if __name__ == "__main__":
  arg1 = int(sys.argv[1]) # arg1 = 10 per exemple
  with Manager() as manager: # create of context manager (share memory)
      lst = manager.list()
      if len(sys.argv) < 2:
        print("require valid arg", file=sys.stderr)
        sys.exit(1)
      try:
        p = Process(target=sequenceFib, args=((arg1, lst)))
        p.start()
        p.join()
        print("Liste fib via father process:", lst) # display variable after edited by child Process
      except ValueError as err:
        print(err)
end_time = time.time()
elaspTime = end_time - start_time
print("time elasped: " "%.2f" % elaspTime + " s")
