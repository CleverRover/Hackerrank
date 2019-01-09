#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sumArr = []
    for i in range(0,len(arr)-2) :
        for j in range(0,4) :
            sumA = sum(arr[i][j:j+3])
            sumA += sum(arr[i+2][j:j+3])
            sumA += arr[i+1][j+1]
            sumArr.append(sumA)
    return max(sumArr)

 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
