#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    l=[]
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                l.append(abs(j-i))
                print(abs(j-i))

    print(l)
    if l !=[]:
        return (min(l))
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()