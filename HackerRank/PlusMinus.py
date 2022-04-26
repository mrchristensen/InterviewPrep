#!/bin/python3

# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # print(arr)
    pos, zero, neg = 0, 0, 0
    for num in arr:
        if num == 0:
            zero += 1
        elif num > 0:
            pos += 1
        else:
            neg +=1
    print("{:.6f}".format(pos/len(arr)))
    print("{:.6f}".format(neg/len(arr)))
    print("{:.6f}".format(zero/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
