n=int(input())
t=n
r=[]
d=[]
while (n>0):
    r.append(n%10)
    n=n//10
print(r)
for i in r:
    if i is not 0:
        if t%i==0:
            d.append(i)
print (d)
c=0
for i in d:
    c=c+1
print(c)        
        