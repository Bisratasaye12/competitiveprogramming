class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        op_count = 0
        l,r = 0, len(nums)-1

        while l < r:
            _sum = nums[l] + nums[r]
            if _sum == k:
                op_count += 1
                l += 1
                r -= 1
            elif _sum < k:
                l += 1
            else:
                r -= 1

        return op_count
