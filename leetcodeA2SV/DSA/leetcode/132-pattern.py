class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        mn = nums[0]

        for i in nums[1:]:

            while stack and stack[-1][0] <= i:
                stack.pop()

            if stack and i > stack[-1][1]:
                return True

            stack.append([i, mn])
            mn = min(mn, i)
            
        return False