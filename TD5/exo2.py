#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

import sys
import array
from threading import Thread, Semaphore, Lock, current_thread

BUFFER_SIZE = 5
consFlag = True

def fibo_prod(n, buffer, full, empty, mutex):
  global consFlag
  i = p = 0
  a, b = 0, 1
  while i < n:
    a, b = b, a+b
    empty.acquire()
    with mutex:
      buffer[p] = a
      print(current_thread().name, "produces:", a, "in", p, flush = True)
      p = (p+1)% BUFFER_SIZE
      i += 1
    full.release()
  consFlag = False
  
def fibo_cons(buffer, full, empty, mutex):
  q = 0
  while consFlag:
    full.acquire()
    with mutex:
      res = buffer[q]
      print(current_thread().name, "consumes:", res, "from:", q, flush = True)
      q = (q+1)%BUFFER_SIZE
    empty.release()


if __name__ == '__main__':
  
  buffer = array.array('l', range(BUFFER_SIZE))
  index = int(input("Entrez indice "))
  
  mutex = Lock()
  full = Semaphore(0)
  empty = Semaphore(BUFFER_SIZE)
  
  cons = Thread(target=fibo_cons, args=(buffer, full, empty, mutex))
  prod = Thread(target=fibo_prod, args=(index, buffer, full, empty, mutex))
  
  cons.start()
  prod.start()
  
  cons.join()
  prod.join()
