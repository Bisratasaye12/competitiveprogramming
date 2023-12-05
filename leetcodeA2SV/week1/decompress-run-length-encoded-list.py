class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            if 2*i >= len(nums):
                break
            f, v = nums[2*i], nums[2*i + 1]
            res += [v]*f

        return res
