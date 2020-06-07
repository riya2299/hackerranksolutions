#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(n,p):
    l=[]
    for i in range(1,n+1):
        for j in range(n):
            if i ==p[j]:
                x=j+1
                for k in range(n):
                    if x==p[k]:
                        l.append(k+1)
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(n,p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

