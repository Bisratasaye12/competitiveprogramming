class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        violation_count = 0

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if violation_count == 1 or (1 < i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False 
                violation_count += 1


        return True
