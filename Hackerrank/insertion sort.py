#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    p = arr[-1]
    flag = False
    for i in range(n-2,-1,-1):
        if arr[i] < p:
            flag = True
            arr[i+1] = p
            print(" ".join(list(map(str,arr))))
            break
        else:
            arr[i+1] = arr[i]
            print(" ".join(list(map(str,arr))))
    if not flag:
        arr[0]=p
        print(" ".join(list(map(str,arr))))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
