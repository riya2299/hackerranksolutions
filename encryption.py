#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    sn="".join(s.split()) 
    print(sn)
    l=len(sn)
    print(l)
    sq=math.sqrt(l)
    print(sq)
    a=int(math.floor(sq))
    print (a)
    b=int(math.ceil(sq))
    print (b)
    c=""
    for i in range(0,b):
        
        for j in range(i,l,b):
            c+=sn[j]
        
        c+=" "
    return c     
s=input()
z=encryption(s)
print(z) 





   