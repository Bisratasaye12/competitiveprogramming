from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input()]
    pref_count = defaultdict(int)
    pref_count[0] = 1
    r = 0

    ans = 0
    for i,j in enumerate(a):
        r += j
        pref_count[r - i - 1] += 1
        ans += pref_count[r - i - 1] - 1

    print(ans)

    