class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1: return 0
        curr = nums[-1]
        count = 0

        for i in range(n-2, -1,-1):
            if nums[i] > curr:
                spaces = math.ceil(nums[i]/curr)
                curr = nums[i] // spaces
                count += (spaces - 1)
            else:
                curr = nums[i]

        return count



