from sys import stdin

def sign(num):
    return num>0

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().strip().split()))
    _sum = 0
    i = 0
    while i < n:
        j = i
        mx = a[i]
        while j < n and sign(a[i]) == sign(a[j]):
            mx = max(mx, a[j])
            j += 1
        
        _sum += mx
        i = j

    
    print(_sum)
