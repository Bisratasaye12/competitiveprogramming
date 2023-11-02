class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        s, count = 0,0

        for i in range(len(nums)):
            s += nums[i]
            c = s - k

            if c in prefix_count:
                count += prefix_count[c]
            prefix_count[s] += 1

        return count

