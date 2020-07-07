#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d=Counter(magazine)
    d1=Counter(note)
    #give me one grand today night
    #give one grand today
    #print(d,d1)
    for i,v in d1.items() :
        if i in d:
            if d[i]>=d1[i]:
                #print("inner loop1",d1[i],d[i],i)
                x="Yes"
                d[i]-=1
            else :
                #print("inner loop else")
                x="No"
                break
        if i not in d:
            #print("else")
            x="No"
            break
    print (x)



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
