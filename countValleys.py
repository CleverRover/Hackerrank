#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    nValleys = 0
    for i in s :
        if i == 'D' :
            level = level - 1
        else :
            level = level + 1
        if level == 0 and i == 'U' :
            nValleys+=1
    return nValleys
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
