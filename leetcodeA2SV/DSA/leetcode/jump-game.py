class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        nums = nums[::-1]
        s,p = 0,0

        while s < len(nums):
            if (s - nums[s]) <= p:
                p = s
            s += 1

        if p == len(nums) - 1:
            return True

        return False