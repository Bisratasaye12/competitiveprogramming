class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ansK = defaultdict(int)

        for i in nums2:
            while stack and stack[-1] < i:
                ansK[stack[-1]] = i
                stack.pop()

            stack.append(i)

        ans = [-1] * len(nums1)

        for i,j in enumerate(nums1):
            if j in ansK:
                ans[i] = ansK[j]

        return ans
        
