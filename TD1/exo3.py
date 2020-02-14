#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

from multiprocessing import *
import time

# Program to reverse sentences 
def child(data):
  sentences = child_conn.recv()
  child_conn.send(sentences[::-1])
  child_conn.close()

# Start algo & evalute time #
start_time = time.time() 
if __name__ == "__main__":
  sentences = ""
  while not sentences:
    sentences = input("Enter a sentences to reverse : ")
  parent_conn, child_conn = Pipe()
  fatherProcess = Process(target=child, args=(child_conn,))
  fatherProcess.start()
  parent_conn.send(sentences)
  print(parent_conn.recv())
  parent_conn.close()
  fatherProcess.join()  

end_time = time.time() 
elaspTime = end_time - start_time
print("time elasped: " "%.2f" % elaspTime + " s")
