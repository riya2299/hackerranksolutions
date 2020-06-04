#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    el=[]
    d=[]
    for i in range(max(arr)+1):
        el.append(0)
    for i in arr:
        el[i]=el[i]+1
    for i in range(0,len(el)):
        for j in range(el[i]):
            d.append(i)
    return d

        

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = countingSort(arr)
print(" ".join(map(str,result)))

