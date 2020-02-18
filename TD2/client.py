#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import sysv_ipc # import module message passing 
import sys

key = 999

def user():
  rep = 3 # While boucle to ask what user want to do
  while rep not in [1,2]:
    print("1 >> to get current date/time")
    print("2 >> to close server")
    rep = int(input())
  return rep

try:
  maillbox = sysv_ipc.MessageQueue(key)
except ExistentialError:
  print("Can't connect to message queue", key, ", terminating.")
  sys.exit()

t = user() # initiale t like type for message passing

if t == 1:
  message = b"" # initialize a empty byte
  maillbox.send(message)
  message, t = maillbox.receive(type = 3)
  reps = message.decode()
  print("Server response:", reps)

if t == 2:
  message = b""
  maillbox.send(message, type = 2)

