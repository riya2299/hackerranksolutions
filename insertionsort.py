def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i-1,-1,-1):
            if l[i]<l[j]:
                k=l[i]
                l[i]=l[j]
                l[j]=k
                i=i-1
           
    return l

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))