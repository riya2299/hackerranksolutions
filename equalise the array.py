#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    max=0        
    for k,v in d.items():
        if v>max:
            max=v
    x=len(arr)-max 
    return x       



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
