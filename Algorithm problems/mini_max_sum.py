#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini=0
    maxi=0
    arr.sort()
    for i in range(len(arr)):
        if i!=4:
            mini+=arr[i]
    for i in range(len(arr)):
        if i!=0:
            maxi+=arr[i]
    print(str(mini)+" "+str(maxi))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
