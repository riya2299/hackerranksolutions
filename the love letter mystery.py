#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    n=len(s)//2
    c=0
    for i in range(0,n):
            x=ord(s[i])
            y=ord(s[len(s)-1-i])
            if x>y:
                c+=x-y
            elif y>x:
                c=c+(y-x)
    return c
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
