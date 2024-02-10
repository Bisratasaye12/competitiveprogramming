class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p
        if target == 0: return 0

        pre = 0
        preToIdx = defaultdict(int)
        preToIdx[0] = -1
        mn = n 
        
        for i in range(n):
            pre += nums[i] 
            pre %= p
            ch = (pre - target) % p
        
            if ch in preToIdx:
                mn = min(mn, i - preToIdx[ch])

            preToIdx[pre] = i

        return mn if mn < n else -1

