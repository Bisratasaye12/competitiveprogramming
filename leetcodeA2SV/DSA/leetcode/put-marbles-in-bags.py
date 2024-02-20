class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:   
        # We collect and sort the value of all n - 1 pairs.
        n = len(weights)
        pre = [0] * (n - 1)
        for i in range(n - 1):
            pre[i] = weights[i] + weights[i + 1]
        pre.sort()
        
       
        ans = 0
        for i in range(k - 1):
            ans += pre[n - 2 - i] - pre[i]
            
        return ans