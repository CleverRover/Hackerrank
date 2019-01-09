#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    numA = s.count('a')
    l = len(s)
    multiple = n//l
    countA = multiple * numA
    leftStr = n - (multiple * l)
    countA += s.count('a',0,leftStr)
    return countA


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
