class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = 0
        q = x

        while q != 0:
            r = q % 10
            n = n * 10 + r
            q = q // 10

        return n == x

       
    
        