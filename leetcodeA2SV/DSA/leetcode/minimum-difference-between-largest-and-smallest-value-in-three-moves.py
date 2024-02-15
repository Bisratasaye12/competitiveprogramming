class Solution:
    def minDifference(self, nums: List[int]) -> int:
        arr = nums.copy()
        n = len(nums)
        nums.sort()
        if n <= 4: return 0

        mins = nums[:5]
        maxs = nums[-4:]

        mn = max(nums) - min(nums)
        for i,j in zip(mins, maxs):
            mn = min((j-i), mn)

        return mn

