class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        count, s = 0, 0
        d = defaultdict(int)
        d[0] = 1

        for i in range(n):
            s += nums[i]
            ch = s - goal

            if ch in d:
                count += d[ch]

            d[s] += 1
            

        return count