#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

from multiprocessing import *
import time

# Program to reverse sentences 
def child(data):
  sentences = child_conn.recv() # reveice sentence send by the father via pipe
  child_conn.send(sentences[::-1]) # send to pipe (child-side) the inverse of the sentence
  child_conn.close()

# Start algo & evalute time #
start_time = time.time() 
if __name__ == "__main__":
  sentences = "" 
  while not sentences:
    sentences = input("Enter a sentences to reverse : ")

  parent_conn, child_conn = Pipe() # initialize pipe connection one connection to daddy another for the boy
  pProcess = Process(target=child, args=(child_conn,)) # send child connection to the child process
  pProcess.start()
  parent_conn.send(sentences) # send to pipe (father-side) the sentence
  print(parent_conn.recv()) # reveice the sentence by child process
  parent_conn.close() # close pipe
  pProcess.join()  # wait child process
end_time = time.time() 
elaspTime = end_time - start_time
print("time elasped: " "%.2f" % elaspTime + " s")
