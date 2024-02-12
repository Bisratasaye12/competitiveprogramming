class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        tar = len(nums) // 2

        for i in count:
            if count[i] > tar:
                return i