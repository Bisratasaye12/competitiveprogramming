class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        glob, loc = 0, 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                glob += loc
            else:
                loc += 1
                glob += loc

        return glob