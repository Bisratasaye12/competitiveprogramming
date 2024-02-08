class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pr_count = defaultdict(int)
        pr_count[0] = 1
        rsum, count = 0,0

        for i in range(len(nums)):
            rsum += nums[i]
            ch = rsum % k

            if ch in pr_count:
                count += pr_count[ch]

            pr_count[ch] += 1

        return count
