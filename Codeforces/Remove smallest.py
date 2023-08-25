from sys import stdin
import math
t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    a = sorted(list(map(int, stdin.readline().strip().split())))

    flag = True
    for j in range(n - 1,-1,-1):
        if a[j] - a[j - 1] > 1:
            flag = False

    if flag:
        print("YES")
    else:
        print("NO")


 
