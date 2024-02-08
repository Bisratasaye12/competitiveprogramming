class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        pre = post = 1

        for i in range(n):
            res.append(pre)
            pre *= nums[i]

        for i in range(n-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        
        return res
            