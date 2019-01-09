#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    cur = 0
    while cur < len(c)-1 :
        if cur+2 <= len(c)-1 :
            if c[cur+2] == 0 :
                jumps += 1
                cur = cur + 2
            elif c[cur+1] == 0 :
                jumps += 1
                cur = cur + 1
        else :
            if c[cur+1] == 0 :
                jumps += 1
                cur = cur + 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
