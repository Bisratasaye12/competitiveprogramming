class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # using difference array technique to find the frequently requested cells
        n = len(nums)
        m = 10**9 + 7
        pre = [0] * n

        for s,e in requests:
            pre[s] += 1
            if e < n-1:
                pre[e+1] -= 1

        for i in range(1, n):
            pre[i] += pre[i-1]

        nums.sort()
        pre.sort()

        _sum = 0
        for i in range(n): 
            _sum += (nums[i] * pre[i])

        return _sum % m

        