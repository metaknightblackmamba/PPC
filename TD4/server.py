#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import random
import concurrent.futures
import sysv_ipc
import sys
import threading
from queue import Queue
import time

key = 666

try: 
  maillbox = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT) # the server create a "mailbox", and now we can share data with clients
except:
  print("Message Queue", key, "already exist, terminating.")

print("Starting Server")

def worker(maillbox, pid):
  datetime = time.asctime()
  message = str(datetime).encode()
  time.sleep(5)
  print(pid)
  maillbox.send(message, type = pid + 3) # here, our message flag is set to 3, like this the customer can filter on his side this message specially
  


while True:
    mq, t = maillbox.receive() # We take all type(flag) of message and parse it
    if t == 1: # if the msg flag is set to 1, we send datetime, encode it to str then byte and post it at Laposte
      pid = int(mq.decode())
      thread = threading.Thread(target=worker, args=(maillbox, pid))
      thread.start()
      thread.join()
    if t == 2: 
      print("Shutdown Server.")
      maillbox.remove() # if the clients send us a msg with type(flag)=2 we close our "mailbox" properly
      break 
