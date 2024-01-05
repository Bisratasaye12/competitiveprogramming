class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        m = k
        _sum = sum(nums[:k])
        s = _sum
        while m < len(nums):
        
            s = s - nums[l] + nums[m]
            _sum = max(_sum, s)
            m += 1
            l += 1

        return _sum/k





