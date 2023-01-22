#!/bin/python3
#https://www.hackerrank.com/challenges/python-time-delta/problem

import math
import os
import random
import re
import sys
import datetime

def time_delta(t1, t2):
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    t1 = datetime.datetime.strptime(t1,"%a %d %b %Y %X %z")
    t2 = datetime.datetime.strptime(t2,"%a %d %b %Y %X %z")
    #t2 = datetime.datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    c = t1 - t2
    return str(abs(int(c.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
