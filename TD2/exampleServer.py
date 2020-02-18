#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import sysv_ipc # see exampleClient.py
 
key = 128 # see client.py
 
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT) # Create a message queue with key=128 to authenticate the other process to connect on, and set flag to create a 'mailbox')
 
value = 1
while value:
    try:
        value = int(input()) 
    except:
        print("Input error, try again!")
    message = str(value).encode() # per example >> 10 > "10" > 0a
    mq.send(message) # send byte to mailbox
 
mq.remove()
