#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:]=="AM" and s[:2]=='12':
        print("00"+str(s[2:-2]))
    elif s[-2:]=="AM":
        print(s[:-2])
    elif s[-2:]=="PM" and s[:2]=='12':
        print(str(s[:-2]))
    else:
        print((str(int(s[:2])+12))+s[2:-2])

    
if __name__ == '__main__':
    s = input()
    timeConversion(s)
