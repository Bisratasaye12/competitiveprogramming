from sys import stdin

n,m = list(map(int, stdin.readline().strip().split()))
a = list(map(int, stdin.readline().strip().split()))
b = list(map(int, stdin.readline().strip().split()))

p,q, c = 0,0,0

while p < n and q < m:
    if a[p] < b[q]:
        c+=1
        p += 1
    else:
        print(c, end=" ")
        q += 1

if p>=n and q <m:
    for i in b[q:]:
        print(c, end=" ")
