class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       
        n = len(nums)
        mx, k2 = 0, k
        l, r = 0, 0

        while r < n:
            if nums[r] == 0 and k2 > 0:
                k2 -= 1

            elif nums[r] == 0 and k2 == 0:
                while nums[l] != 0:
                    l += 1
                l += 1  

            mx = max(mx, r - l + 1)
            r += 1

        return mx
