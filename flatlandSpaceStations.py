#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, s):
    s = sorted(s)
    r = s[0]
    
    for i in range(1, len(s)):
        r = max(r, (s[i] - s[i-1])//2)
        print (r)
        
    r = max(r, n-1 - s[-1])
        
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
