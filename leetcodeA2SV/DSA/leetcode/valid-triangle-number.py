class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0

        for e in range(n-1, -1, -1):
            l,r = 0, e-1

            while l < r:
                if nums[l] + nums[r] > nums[e]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1

        return count


