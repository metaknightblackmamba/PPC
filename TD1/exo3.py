#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a awesome
    python script...!"""

from multiprocessing import *
import os
import time
import sys
import signal


def f(conn):
    
    reverses = child_conn.recv()
    child_conn.send(reverses.reverse())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    global sentences
    sentences = ['1','2','3','4','5','6','7','8','9']
    p = Process(target=f, args=(child_conn, ))
    p.start()
    parent_conn.send(sentences)
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
