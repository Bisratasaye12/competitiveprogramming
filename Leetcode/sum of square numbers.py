class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c)) 
    
        while l <= r:
            
            sq = r**2 + l**2
            if (sq) == c:
                return True
            elif (sq) < c:
                l += 1
            else:
                r -= 1
