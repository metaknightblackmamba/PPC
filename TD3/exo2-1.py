#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import threading
from queue import Queue
import statistics
import sys

def worker(task_queue, data, data_ready, res_queue):
  data_ready.wait()
  function = task_queue.get()
  res = function(data)
  res_queue.put([function.__name__,"(",data,") =", res])

if __name__ == "__main__":
  data = []
  tasks = [min, max, statistics.median, statistics.mean, statistics.stdev]
  
  task_queue = Queue()
  for t in tasks:
    task_queue.put(t)

  data_ready = threading.Event()
  res_queue = Queue() # create an additional queue (tube) to insert result of worker threads

  threads = [threading.Thread(target=worker, args=(task_queue, data, data_ready, res_queue)) for i in range(len(tasks))]
  for thread in threads:
    thread.start()
  
  print("Enter a sequence of real numbers, Ctrl+D to end.")

  input_str = sys.stdin.read().split()
  for s in input_str:
      try:
          x = float(s)
      except ValueError:
          print("bad number", s)
      else:
          data.append(x)

  data_ready.set()
  for thread in threads:
    thread.join()
 
   
  while not res_queue.empty(): # we loop until the queue resultat is empty
    res = res_queue.get() # we grab one resultat in queue of worker threading 
    print(res) # we print all result of worker thread
