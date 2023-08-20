class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        real_sum = (n + 1) * n // 2
        app_sum = sum(nums)
        res = real_sum - app_sum
        return res
        
