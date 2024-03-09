class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, h = 0, len(nums) - 1
        res = [-1, -1]

        while l <= h:
            m = (l + h) // 2

            if nums[m] == target:
                res[0] = m
                h = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1

        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2

            if nums[m] == target:
                res[1] = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1

        return res
