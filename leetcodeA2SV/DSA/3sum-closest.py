class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_d = float("inf")
        res = 0
        for i in range(n):
            first = nums[i]

            l, r = i + 1, n - 1
            while l < r:
                s = first + nums[l] + nums[r]
                if s == target:
                    return s
                elif s < target:
                    
                    l += 1
                else:
                    
                    r -= 1
                d = abs(s - target)
                if d < min_d:
                    min_d = d
                    res = s

        return res


