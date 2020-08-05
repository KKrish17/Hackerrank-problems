#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    low=scores[0]
    high=scores[0]
    a=0
    b=0
    for i in range(1,len(scores)):
        if scores[i]>high:
            a+=1
            high=scores[i]
        elif scores[i]<low:
            b+=1
            low=scores[i]
        else:
            pass
    print(str(a)+" "+str(b))

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    breakingRecords(scores)
