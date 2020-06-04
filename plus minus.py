#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    m=0
    p=0
    z=0
    for i in arr:
        if i <0:
            m=m+1
        elif i>0:
            p=p+1
        else:
            z=z+1
    sum=float(p+m+z)
    print(float(p/sum))
    print(m/sum)
    print(z/sum)
    
        



n = int(input())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)

