#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import sysv_ipc # import module message passing 
import sys
import time

key = 999

try: 
  maillbox = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
except:
  print("Message Queue", key, "already exist, terminating.")

print("Starting Server")

while True:
  mq, t = maillbox.receive()
  if t == 1:
    datetime = time.asctime()
    message = str(datetime).encode()
    maillbox.send(message, type=3)
  if t == 2:
    print("Shutdown Server.")
    maillbox.remove()
    break
