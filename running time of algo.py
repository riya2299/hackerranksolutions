#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    c=0
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[i]<arr[j]:
                k=arr[i]
                arr[i]=arr[j]
                arr[j]=k
                i=i-1
                c=c+1
                print(c)
            
        
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()