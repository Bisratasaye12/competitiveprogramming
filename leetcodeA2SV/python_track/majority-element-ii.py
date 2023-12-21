class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for i in nums:
            counts[i] = nums.count(i)

        target = math.floor(len(nums)/3)
        res = []
        for i in counts:
            if counts[i] > target:
                res.append(i)

        return res