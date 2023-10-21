from sys import stdin

n,m = list(map(int, stdin.readline().strip().split()))
a = list(map(int, stdin.readline().strip().split()))
b = list(map(int, stdin.readline().strip().split()))

p,q = 0,0

while p < n and q < m:
    if a[p] < b[q]:
        print(a[p], end=" ")
        p += 1
    elif a[p] > b[q]:
        print(b[q], end=" ")
        q += 1
    else:
        print(a[p], end=" ")
        print(b[q], end=' ')
        p += 1
        q += 1

if p>=n and q <m:
    for i in b[q:]:
        print(i, end=" ")
else:
    for j in a[p:]:
        print(j, end=" ")


    
