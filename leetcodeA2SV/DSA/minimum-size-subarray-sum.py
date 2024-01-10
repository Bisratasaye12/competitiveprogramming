class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       l,m = 0,0
       s = 0
       length = float('inf')
       while m < len(nums):
           s += nums[m]
           while s >= target:
               length = min(length, m-l+1)
               s -= nums[l]
               l += 1
           m += 1
       return 0 if length == float('inf') else length