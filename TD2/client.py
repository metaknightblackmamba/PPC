#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import sysv_ipc # import module message passing 
import sys

key = 999 # key to authenticate this process to the "mailbox"

def user():
  rep = 3 # While boucle to ask what user want to do
  while rep not in [1,2]: # if user answer not in list, spam the USER=)
    print("1 >> to get current date/time")
    print("2 >> to close server")
    try:
      rep = int(input()) # return an int to tell server what to do (indeed with this return we gonna pass a type flag to messageQueue :s:s ?? I ll explain below
    except ValueError as e:
      print("Please enter 1 (datetime) or 2 to quit")
  return rep

try:
  maillbox = sysv_ipc.MessageQueue(key) # open existing mailbox created by the server (when u launch it)
except ExistentialError: # If error like the mailbox doesn't exist, kill this process
  print("Can't connect to message queue", key, ", terminating.")
  sys.exit()

t = user() # initialize t like type for message passing, like this we will filter our receive message  example: t=1

if t == 1: # if the user enter 1
  message = b"" # initialize a empty byte
  maillbox.send(message) # we tell server that we want the datetime
  message, t = maillbox.receive(type = 3) # Now we wait the answer(default = blocking) of the server, and we set the flag to 3, like this we can filter the mailbox, we gonna rcv only message that have flag set(by the server) to 3
  reps = message.decode() # decode Byte receive to str
  print("Server response:", reps)

if t == 2:
  message = b"" # same as above
  maillbox.send(message, type = 2) # here, we send an empty message byte with a flag(type) = 2, like this the server can filter the msg and do what we want to do

