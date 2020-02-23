#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import threading # import threading module
from queue import Queue # import queue module
import statistics # import statistics module
import sys

def worker(task_queue, data, data_ready): # define a function for thread
  data_ready.wait() # thread wait to have data
  function = task_queue.get() # thread get a task to do
  res = function(data) # instance a function (ex: max) to the data
  print(function.__name__,"(",data,") =", res) # print function name and the result of it

if __name__ == "__main__": # start main program
  data = [] # tab to welcom data
  tasks = [min, max, statistics.median, statistics.mean, statistics.stdev] # tab with all function that we want to do with worker
  
  task_queue = Queue() # instance a queue (tube) to communicate with the worker thread
  for t in tasks:
    task_queue.put(t) # put all function un the tube

  data_ready = threading.Event() # wait/lock the data
  
  threads = [threading.Thread(target=worker, args=(task_queue, data, data_ready)) for i in range(len(tasks))] # create on thread for each function in the tab tasks
  for thread in threads:
    thread.start() # start all the threads
  
  print("Enter a sequence of real numbers, Ctrl+D to end.") # user enter a sequence of number

  input_str = sys.stdin.read().split() # we split the input user and loop in 
  for s in input_str:
      try:
          x = float(s)
      except ValueError:
          print("bad number", s)
      else:
          data.append(x) # put input User to a tab  

  data_ready.set() # tell to all worker trhead that data is ready
  for thread in threads:
    thread.join() # wait all worker threads to finish their job
