class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        target = Counter(nums)
        k = len(target)
        count = 0

        for i in range(n):
            win = defaultdict(int)
            for j in range(i,n):
                win[nums[j]] += 1
                if len(win) ==  k:
                    count += 1

        return count

