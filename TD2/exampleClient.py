#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import sysv_ipc # Import message passing module
 
key = 128 # key to authenticate with the mailbox
 
mq = sysv_ipc.MessageQueue(key) # Open an existing message queue (the server created)
 
while True: 
    message, t = mq.receive() # Receive the first msg who arrive
    value = message.decode() # decode the rcv byte to str
    value = int(value) # convert str to int 
    if value:
        print("received:", value)
    else:
        print("exiting.")
        break

