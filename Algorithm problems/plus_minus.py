#!/bin/python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive=0.0
    negative=0.0
    neutral=0.0
    for i in range(len(arr)):
        if arr[i]>0:
            positive+=1
        elif arr[i]<0:
            negative+=1
        else:
            neutral+=1
    print "{:.6f}".format(float(positive/len(arr)))
    print "{:.6f}".format(float(negative/len(arr)))
    print "{:.6f}".format(float(neutral/len(arr)))

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)

