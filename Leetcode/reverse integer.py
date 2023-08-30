class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        r = 0
        q = 1
        if x < 0:
            flag = True
            x = -1 * x
        
        while q != 0:
            r = r * 10 + (x % 10)
            q = x // 10
            x = q
            
        up = 2147483647
        down = -2147483648
            
        if r < down or r > up:
            return 0
        else:
            if flag:
                return -r
            return r
        
