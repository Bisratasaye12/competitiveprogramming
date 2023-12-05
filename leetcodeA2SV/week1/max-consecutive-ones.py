class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l,r = 0,0
        m = float('-inf')
        while r < len(nums):
            if nums[r] == 1:
                r+=1
            else:
                m = max(r-l, m)
                l = r+1
                r += 1
        m = max(r-l, m)

        return m

