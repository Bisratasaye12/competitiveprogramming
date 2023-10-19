class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        cn = nums.copy()
        cn.sort()
        l = 0
        m = 0
        res = [0 for i in range(len(nums))]
        c = 0
        while l < len(nums):
            if cn[m] < nums[l]:
                m+=1
                c += 1
            else:
                m = 0
                res[l] = c
                c = 0
                l += 1
        return res
