class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        res = [0]*n
        pre = 0

        for i in range(n):
            left = pre
            right = total - pre - nums[i]

            abs_diff = abs(left - i * nums[i] + ((n - i - 1) * nums[i] - right))
            res[i] = abs_diff
            pre += nums[i]

        return res
