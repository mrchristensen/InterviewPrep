#!/bin/python3

# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    sum = 0

    for num in arr:
        sum += num

        if(num < min):
            min = num
        elif(num > max):
            max = num

    print(str(sum - max) + " " + str(sum - min))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
