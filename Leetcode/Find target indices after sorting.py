class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()

        l, h = 0, len(nums)-1
        res = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        return res
