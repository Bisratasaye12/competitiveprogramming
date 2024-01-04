class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        res_set = set()
        for i in range(n):
            first = nums[i]
            target = -1 * first

            l,r = i+1, n - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    h = [first, nums[l], nums[r]]
                    g = tuple(h)
                    if g not in res_set:
                        res.append(h)
                        res_set.add(g)
                    l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1 

        return res
                