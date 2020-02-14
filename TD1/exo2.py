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
def sequenceFib(data):
  time.sleep(1)
  print('My PID is:', os.getpid())
  os.kill(os.getppid(), signal.SIGKILL)
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

def receive_signal(signum, stack):
    if signum == signal.SIGKILL:
      print('Received:', signum)
      os.kill(sequenceFibPID, signal.SIGKILL)

# Start algo & evalute time #
start_time = time.time() 

if __name__ == "__main__":
  arg1 = int(sys.argv[1])
  if len(sys.argv) < 2:
    print("require valid arg", file=sys.stderr)
    sys.exit(1)
  try:
    p = Process(target=sequenceFib, args=((arg1,)))
    p.start()
    global sequenceFibPID
    sequenceFibPID = sequenceFib.pid
    signal.signal(signal.SIGKILL, receive_signal) 
    p.join()
  except ValueError as err:
    print(err)

end_time = time.time()
elaspTime = end_time - start_time
print("time elasped: " "%.2f" % elaspTime + " s")
