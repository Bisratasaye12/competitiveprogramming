class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1) // 2
        print(total)
        p = 0

        for i in range(1,n+1):
            p += i
            if 2 * p == total + i:
                return i

        return -1
