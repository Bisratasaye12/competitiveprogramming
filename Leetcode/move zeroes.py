class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        p = 0
        while p < len(nums) and s < len(nums):
            if nums[s] != 0:
                nums[s], nums[p] = nums[p], nums[s]
                p+=1
                s = p
            else:
                s += 1

    
