class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def find(x, y, p):
            res = 1
            x = x % p
            while y > 0:
                if y % 2 == 1:
                    res = (res * x) % p
                y = y // 2
                x = (x * x) % p
            return res

        even= (n + 1) // 2
        odd = n // 2

        return (find(5, even, (10**9 + 7)) * find(4, odd, (10**9 + 7))) % (10**9 + 7)
        
