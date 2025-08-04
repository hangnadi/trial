#!/bin/python3

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
time_format = "%a %d %b %Y %H:%M:%S %z"
def time_delta(t1, t2):
    s1 = dt.datetime.strptime(t1, time_format)
    s2 = dt.datetime.strptime(t2, time_format)
    return int(abs(s1-s2).total_seconds())


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)

        # fptr.write(delta + '\n')

    # fptr.close()
