#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import os
import sys
import time
import sysv_ipc
import threading

key = 999

def worker(mq, m):
  print("Starting thread:", threading.current_thread().name)
  datetime = time.asctime()
  message = str(datetime).encode() # encode current time
  pid = int(m.decode()) # decode the PID of the thread client (send by the client)
  t = pid + 3 # unique type of message queue, is for the client, like this he can filter his own msg
  time.sleep(5) # just sleep to look behavior with several client
  mq.send(message, type=t) # put in mailbox the current datetime and type of the msg who is PID+3
  print("Ending thread:", threading.current_thread().name)
  

if __name__ == "__main__":
  print("Starting thread:", threading.current_thread().name)
 
  try:
    mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREX) # create a mailbox/tube
  except ExistentialError:
    print("Message queue", key, "already exist, terminating.")
    sys.exit(1)

  print("Starting time server.")

  threads = []

  while True:
      m, t = mq.receive() 
      if t == 1: 
        p = threading.Thread(target=worker, args=(mq, m)) # create a thread worker to execute the datetime cmd. We have one thread for each client, which isn't secure. Because we can overflow the server 
        p.start()
        threads.append(p) # create a list of the current worker thread like this we can wait all worker
      if t == 2: 
        print("Shutdown Server.")
        for thread in threads:
          thread.join() # we wait all current worker to finish
        mq.remove() # delete the mailbox/tube
        break
  print("Terminating time server.")
  print("Ending thread:", threading.current_thread().name)
