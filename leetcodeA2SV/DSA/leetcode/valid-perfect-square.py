class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l, r = 1, num

        while l <= r:
            m = (l + r) // 2

            if m**2 == num:
                return True
            elif m**2 < num:
                l = m + 1
            else:
                r = m - 1

        return False
