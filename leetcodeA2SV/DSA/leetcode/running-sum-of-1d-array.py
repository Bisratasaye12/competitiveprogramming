class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r = 0
        for i in range(len(nums)):
            r += nums[i]
            nums[i] = r

        return nums
        
