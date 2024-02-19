class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)

        for i in range(2 * len(nums)):
            i = i % len(nums)

            while stack and nums[stack[-1]] < nums[i]:
                               
                ans[stack[-1]] = nums[i]
                elem = stack.pop()

            stack.append(i)

        return ans

