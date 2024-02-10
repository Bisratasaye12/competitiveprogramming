class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        pre = [0]*n
        suff = [0]*n
        f, b = 0, 0
        for i in range(n):
            if s[i] == "0":
                f += 1
            if s[n-i-1] == "1":
                b += 1

            pre[i] = f
            suff[n-i-1] = b
        
        #print(pre, suff)
        
        return max(i+j for i,j in zip(pre[:-1], suff[1:]))
