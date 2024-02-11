class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        total_counts = Counter(nums)
        total_sum = defaultdict(int)
        for i,x in enumerate(nums):
            total_sum[x] += i

        count = defaultdict(int)
        pre = defaultdict(int)
        res = [0]*len(nums)

        for i,j in enumerate(nums):
            left = i * count[j] - pre[j]
            right = (total_sum[j] - pre[j] - i) - i* (total_counts[j] - count[j] - 1)
            res[i] = left + right
            count[j] += 1
            pre[j] += i

        return res



