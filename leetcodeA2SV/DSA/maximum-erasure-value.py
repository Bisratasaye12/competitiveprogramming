class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ms = 0
        l, r = 0, 0
        u = set()
        r_sum = 0

        l = 0
        for r in range(n):
            while nums[r] in u:
                r_sum -= nums[l]
                #print(r_sum)
                u.remove(nums[l])
                l += 1

            u.add(nums[r])
            r_sum += nums[r]
            #print(r_sum)
            ms = max(ms, r_sum)

        return ms



