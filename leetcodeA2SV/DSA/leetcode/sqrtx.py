class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x
        if x == 0 or x == 1:
            return x
        res = 0

        while l < r:
            m = ( l + r ) // 2
            ms = m ** 2
            if ms == x:
                return m
            elif ms < x:
                l = m + 1
                res = m
            else:
                r = m 

        return res 