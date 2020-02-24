#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import os
import sys
import time
import sysv_ipc
import threading
import concurrent.futures

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


  with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
    while True:
        m, t = mq.receive() 
        if t == 1:
          executor.submit(worker, mq, m)
        if t == 2: 
          mq.remove()
          break
    print("Terminating time server.")
    print("Ending thread:", threading.current_thread().name)
