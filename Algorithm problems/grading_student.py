#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]%5==0 or grades[i]<38:
            print(grades[i])
        elif grades[i]%5!=0 and ((grades[i]+(5-grades[i]%5))-grades[i])==3:
            print(grades[i])
        else:
            grades[i]=grades[i]+(5-grades[i]%5)
            print(grades[i])


if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    gradingStudents(grades)
