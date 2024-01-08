class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mx, k = 0, False
        idx = 0
        l, r = 0,0

        while r < n:
            if nums[r] == 0 and not k:
               k = True
               idx = r
            elif nums[r] == 0 and k:
                mx = max(mx, r-l-1)
                l = idx + 1
                idx = r

         
            r += 1
        mx = max(mx, r-l-1)
    
        return mx

