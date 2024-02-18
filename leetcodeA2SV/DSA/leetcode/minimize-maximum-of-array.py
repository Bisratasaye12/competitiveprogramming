class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        r = 0
        mx = nums[0]

        for i, j in enumerate(nums):
            r += j
            nw = math.ceil(r/(i+1))

            mx = max(mx, nw)

        return mx
       