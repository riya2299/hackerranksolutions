 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    lis=[]
    for i in range(p,q+1):
        d=0
        j=pow(i,2)
        k=pow(i,2)
        while(k>0):
           k= k//10
           d=d+1
        st=str(j)
        if d==1:
            a=i**2
            if a==i:
                lis.append(i)
        
        else:
            s1=st[0:d//2]
            s2=st[d//2:len(st)]
            
            sum=int(s1)+int(s2)
            
            if i==sum:
                lis.append(i)
    
    if lis==[]:
        print("INVALID RANGE") 
    print(" ".join(map(str,lis)))
            
        
        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
