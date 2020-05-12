n=int(input())
arr=[]
for i in range(0,n):
    arr.append(int(input()))
d={}
    for i in ar:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    print(d)        
    c=0        
    for k,v in d.items():
        if v%2==0:
            c=c+1
        else:pass
    print (c)        
