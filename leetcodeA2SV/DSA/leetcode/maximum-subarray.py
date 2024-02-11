class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        r = 0

        for i in range(n):
            r += nums[i]
            pre[i] = r
            if r < 0:
                r = 0

           
        
        return max(pre)
